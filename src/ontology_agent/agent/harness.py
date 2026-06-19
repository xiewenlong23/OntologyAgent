from typing import Any
from ontology_agent.agent.messages import AgentMessage
from ontology_agent.agent.prompts import PLANNER_PROMPT, TOOL_AGENT_PROMPT, REASONER_PROMPT, REPORTER_PROMPT
from ontology_agent.tools.registry import ToolRegistry


class AgentHarness:
    def __init__(self):
        self.registry = ToolRegistry.get_instance()
        self.tools = self.registry.list_tools()
        self.tool_schemas = [
            {"name": t.name, "description": t.description, "parameters": t.params_schema}
            for t in self.tools
        ]

    def get_system_prompts(self) -> dict[str, str]:
        return {
            "planner": PLANNER_PROMPT,
            "tool_agent": TOOL_AGENT_PROMPT,
            "reasoner": REASONER_PROMPT,
            "reporter": REPORTER_PROMPT,
        }

    def get_available_tools(self) -> list[dict]:
        return self.tool_schemas

    async def process_message(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        # Simple routing: based on msg_type and content
        if message.to_agent == "planner":
            return await self._handle_planner(message, llm_complete_fn)
        elif message.to_agent == "tool":
            return await self._handle_tool(message, llm_complete_fn)
        elif message.to_agent == "reasoner":
            return await self._handle_reasoner(message, llm_complete_fn)
        elif message.to_agent == "reporter":
            return await self._handle_reporter(message, llm_complete_fn)
        else:
            return AgentMessage(
                msg_id=message.msg_id + "_error",
                from_agent="harness",
                to_agent=message.from_agent,
                msg_type="error",
                content={"error": f"Unknown agent: {message.to_agent}"},
                reply_to=message.msg_id,
            )

    async def _handle_planner(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        # Extract user message - frontend sends "message", REST API sends "task"
        user_input = message.content.get("task") or message.content.get("message", "")
        response = await llm_complete_fn(
            system_prompt=PLANNER_PROMPT,
            messages=[{"role": "user", "content": user_input}],
        )
        # Strip thinking tags from LLM response
        import re
        response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()
        return AgentMessage(
            msg_id=f"{message.msg_id}_plan",
            from_agent="planner",
            to_agent=message.from_agent,
            msg_type="result",
            content={"plan": response},
            reply_to=message.msg_id,
        )

    async def _handle_tool(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        action = message.content.get("action")
        params = message.content.get("params", {})
        result = await self.registry.execute(action, params, message.content.get("context", {}))
        return AgentMessage(
            msg_id=f"{message.msg_id}_result",
            from_agent="tool",
            to_agent=message.from_agent,
            msg_type="result",
            content={"result": result.__dict__},
            reply_to=message.msg_id,
        )

    async def _handle_reasoner(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        response = await llm_complete_fn(
            system_prompt=REASONER_PROMPT,
            messages=[{"role": "user", "content": str(message.content)}],
        )
        return AgentMessage(
            msg_id=f"{message.msg_id}_analysis",
            from_agent="reasoner",
            to_agent=message.from_agent,
            msg_type="result",
            content={"analysis": response},
            reply_to=message.msg_id,
        )

    async def _handle_reporter(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        response = await llm_complete_fn(
            system_prompt=REPORTER_PROMPT,
            messages=[{"role": "user", "content": str(message.content)}],
        )
        return AgentMessage(
            msg_id=f"{message.msg_id}_report",
            from_agent="reporter",
            to_agent=message.from_agent,
            msg_type="result",
            content={"report": response},
            reply_to=message.msg_id,
        )
