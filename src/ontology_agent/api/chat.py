from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.agent.messages import AgentMessage
import uuid
import json

router = APIRouter(prefix="/api/v1", tags=["chat"])
harness = AgentHarness()


async def mock_llm(**k):
    return "Mock LLM response"


@router.post("/chat")
async def chat(message: dict):
    msg_id = str(uuid.uuid4())
    agent_msg = AgentMessage(
        msg_id=msg_id,
        from_agent="user",
        to_agent="planner",
        msg_type="task",
        content=message,
    )
    result = await harness.process_message(agent_msg, llm_complete_fn=mock_llm)
    return {"msg_id": result.msg_id, "content": result.content}


@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    # TODO: Extract tenant_id from JWT token for proper isolation (security gap - MVP uses query param)
    tenant_id = websocket.query_params.get("tenant_id")
    await websocket.accept()
    try:
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
            result = await harness.process_message(agent_msg, llm_complete_fn=mock_llm)
            await websocket.send_json({"msg_id": result.msg_id, "content": result.content})
    except WebSocketDisconnect:
        pass