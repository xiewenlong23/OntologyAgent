from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, Header, status
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.agent.messages import AgentMessage
from ontology_agent.llm import create_llm_client
from ontology_agent.config import get_settings
import uuid
import json
import logging

router = APIRouter(prefix="/api/v1", tags=["chat"])
harness = AgentHarness()
llm_client = create_llm_client()

logger = logging.getLogger(__name__)
settings = get_settings()


def _check_internal_secret(secret: str | None) -> None:
    """Verify the internal shared secret. If unset, allow (dev mode).

    Reject when server has a secret configured but client didn't provide one,
    or when they don't match.
    """
    if not settings.internal_shared_secret:
        return
    if not secret or secret != settings.internal_shared_secret:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid internal secret")


async def get_llm_complete_fn():
    """Get the LLM completion function, falls back to mock if no client."""
    if llm_client is None:
        async def mock_llm(**k):
            return "Mock LLM response"
        return mock_llm

    async def real_llm(**k):
        prompt = k.get("prompt", "")
        system = k.get("system", "")
        messages = k.get("messages")
        system_prompt = k.get("system_prompt") or system
        logger.debug("real_llm called: prompt_len=%d system_len=%d messages=%d", len(prompt), len(system_prompt or ""), len(messages or []))
        try:
            result = await llm_client.complete(prompt=prompt, system=system, messages=messages, system_prompt=system_prompt)
            logger.debug("LLM result len=%d", len(result))
            return result
        except Exception as e:
            logger.exception("LLM call failed")
            raise

    return real_llm


@router.post("/chat")
async def chat(
    message: dict,
    x_internal_secret: str | None = Header(default=None, alias="X-Internal-Secret"),
):
    _check_internal_secret(x_internal_secret)
    msg_id = str(uuid.uuid4())
    llm_fn = await get_llm_complete_fn()
    agent_msg = AgentMessage(
        msg_id=msg_id,
        from_agent="user",
        to_agent="planner",
        msg_type="task",
        content=message,
    )
    result = await harness.process_message(agent_msg, llm_complete_fn=llm_fn)
    return {"msg_id": result.msg_id, "content": result.content}


@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    # TODO: replace with real JWT-based tenant_id extraction once auth is implemented.
    tenant_id = websocket.query_params.get("tenant_id")
    presented_secret = websocket.headers.get("X-Internal-Secret")
    if settings.internal_shared_secret and presented_secret != settings.internal_shared_secret:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    await websocket.accept()
    try:
        llm_fn = await get_llm_complete_fn()
        while True:
            try:
                data = await websocket.receive_text()
                msg = json.loads(data)
            except json.JSONDecodeError as e:
                await websocket.send_json({"content": {"error": f"Invalid JSON: {e}"}})
                continue
            except WebSocketDisconnect:
                raise

            msg_id = str(uuid.uuid4())
            agent_msg = AgentMessage(
                msg_id=msg_id,
                from_agent="user",
                to_agent="planner",
                msg_type="task",
                content={"tenant_id": tenant_id, **msg},
            )
            try:
                result = await harness.process_message(agent_msg, llm_complete_fn=llm_fn)
                await websocket.send_json({"msg_id": result.msg_id, "content": result.content})
            except Exception as e:
                logger.exception("harness.process_message failed")
                await websocket.send_json({"content": {"error": f"Processing failed: {e}"}})
    except WebSocketDisconnect:
        pass