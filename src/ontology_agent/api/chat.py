from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.agent.messages import AgentMessage
from ontology_agent.llm import create_llm_client
import uuid
import json
import logging

router = APIRouter(prefix="/api/v1", tags=["chat"])
harness = AgentHarness()
llm_client = create_llm_client()

logger = logging.getLogger(__name__)


async def get_llm_complete_fn():
    """Get the LLM completion function, falls back to mock if no client."""
    if llm_client is None:
        async def mock_llm(**k):
            return "Mock LLM response"
        return mock_llm

    async def real_llm(**k):
        prompt = k.get("prompt", "")
        system = k.get("system", "")
        try:
            return await llm_client.complete(prompt, system)
        except Exception as e:
            logger.error(f"LLM call failed: {e}")
            return f"LLM error: {str(e)}"

    return real_llm


@router.post("/chat")
async def chat(message: dict):
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
    tenant_id = websocket.query_params.get("tenant_id")
    await websocket.accept()
    try:
        llm_fn = await get_llm_complete_fn()
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            msg_id = str(uuid.uuid4())
            agent_msg = AgentMessage(
                msg_id=msg_id,
                from_agent="user",
                to_agent="planner",
                msg_type="task",
                content={"tenant_id": tenant_id, **msg},
            )
            result = await harness.process_message(agent_msg, llm_complete_fn=llm_fn)
            await websocket.send_json({"msg_id": result.msg_id, "content": result.content})
    except WebSocketDisconnect:
        pass