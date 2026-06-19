from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.agent.messages import AgentMessage
import uuid
import json

router = APIRouter(prefix="/api/v1", tags=["chat"])
harness = AgentHarness()


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
    result = await harness.process_message(agent_msg, llm_complete_fn=lambda **k: "Mock LLM response")
    return {"msg_id": result.msg_id, "content": result.content}


@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
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
                content=msg,
            )
            result = await harness.process_message(agent_msg, llm_complete_fn=lambda **k: "Mock LLM")
            await websocket.send_json({"msg_id": result.msg_id, "content": result.content})
    except WebSocketDisconnect:
        pass