import pytest
from ontology_agent.agent.messages import AgentMessage
from ontology_agent.agent.prompts import (
    PLANNER_PROMPT,
    TOOL_AGENT_PROMPT,
    REASONER_PROMPT,
    REPORTER_PROMPT,
)
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.tools.registry import ToolRegistry
from ontology_agent.tools.base import Tool, ToolResult


@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset the ToolRegistry singleton before each test."""
    ToolRegistry._instance = None
    yield
    ToolRegistry._instance = None


class DummyTool(Tool):
    """A dummy tool for testing."""

    def __init__(self, name="dummy", is_admin_only=False):
        self.name = name
        self.description = "A dummy tool for testing"
        self.params_schema = {"type": "object", "properties": {}}
        self.is_admin_only = is_admin_only

    async def execute(self, params: dict, context: dict) -> ToolResult:
        return ToolResult(success=True, data={"result": "ok"}, execution_time_ms=10)


class TestAgentMessage:
    def test_agent_message_creation(self):
        msg = AgentMessage(
            msg_id="msg1",
            from_agent="planner",
            to_agent="tool",
            msg_type="task",
            content={"task": "do something"},
        )
        assert msg.msg_id == "msg1"
        assert msg.from_agent == "planner"
        assert msg.to_agent == "tool"
        assert msg.msg_type == "task"
        assert msg.content == {"task": "do something"}
        assert msg.reply_to is None
        assert msg.ttl == 30
        assert msg.retries == 0
        assert msg.created_at is not None

    def test_agent_message_with_reply_to(self):
        msg = AgentMessage(
            msg_id="msg2",
            from_agent="tool",
            to_agent="planner",
            msg_type="result",
            content={"result": "done"},
            reply_to="msg1",
        )
        assert msg.reply_to == "msg1"

    def test_agent_message_broadcast(self):
        msg = AgentMessage(
            msg_id="msg3",
            from_agent="planner",
            to_agent="*",
            msg_type="task",
            content={},
        )
        assert msg.to_agent == "*"


class TestPrompts:
    def test_planner_prompt_contains_task_placeholder(self):
        assert "{task_description}" in PLANNER_PROMPT
        assert "{context}" in PLANNER_PROMPT

    def test_tool_agent_prompt_contains_step_placeholder(self):
        assert "{step_description}" in TOOL_AGENT_PROMPT
        assert "{available_tools}" in TOOL_AGENT_PROMPT

    def test_reasoner_prompt_contains_data_placeholder(self):
        assert "{task_description}" in REASONER_PROMPT
        assert "{data}" in REASONER_PROMPT

    def test_reporter_prompt_contains_format_placeholder(self):
        assert "{data}" in REPORTER_PROMPT
        assert "{format}" in REPORTER_PROMPT


class TestAgentHarness:
    def test_harness_initialization(self):
        registry = ToolRegistry.get_instance()
        registry.register(DummyTool())
        harness = AgentHarness()
        assert harness.registry is registry
        assert len(harness.tools) >= 1

    def test_get_system_prompts(self):
        harness = AgentHarness()
        prompts = harness.get_system_prompts()
        assert "planner" in prompts
        assert "tool_agent" in prompts
        assert "reasoner" in prompts
        assert "reporter" in prompts
        assert PLANNER_PROMPT in prompts["planner"]
        assert TOOL_AGENT_PROMPT in prompts["tool_agent"]
        assert REASONER_PROMPT in prompts["reasoner"]
        assert REPORTER_PROMPT in prompts["reporter"]

    def test_get_available_tools(self):
        registry = ToolRegistry.get_instance()
        registry.register(DummyTool(name="test_tool"))
        harness = AgentHarness()
        tools = harness.get_available_tools()
        assert len(tools) >= 1
        tool_names = [t["name"] for t in tools]
        assert "test_tool" in tool_names

    @pytest.mark.asyncio
    async def test_process_message_unknown_agent(self):
        harness = AgentHarness()
        message = AgentMessage(
            msg_id="msg1",
            from_agent="planner",
            to_agent="unknown",
            msg_type="task",
            content={},
        )
        llm_fn = lambda system_prompt, messages: "response"

        result = await harness.process_message(message, llm_fn)

        assert result.msg_type == "error"
        assert "Unknown agent" in result.content["error"]
        assert result.from_agent == "harness"
        assert result.to_agent == "planner"
        assert result.reply_to == "msg1"

    @pytest.mark.asyncio
    async def test_handle_tool_executes_registered_tool(self):
        registry = ToolRegistry.get_instance()
        registry.register(DummyTool(name="exec_tool"))
        harness = AgentHarness()

        message = AgentMessage(
            msg_id="msg1",
            from_agent="planner",
            to_agent="tool",
            msg_type="task",
            content={"action": "exec_tool", "params": {}, "context": {}},
        )
        llm_fn = lambda system_prompt, messages: "response"

        result = await harness.process_message(message, llm_fn)

        assert result.msg_type == "result"
        assert result.from_agent == "tool"
        assert result.to_agent == "planner"
        assert "result" in result.content

    @pytest.mark.asyncio
    async def test_handle_tool_returns_error_for_unknown_tool(self):
        harness = AgentHarness()
        message = AgentMessage(
            msg_id="msg1",
            from_agent="planner",
            to_agent="tool",
            msg_type="task",
            content={"action": "nonexistent_tool", "params": {}, "context": {}},
        )
        llm_fn = lambda system_prompt, messages: "response"

        result = await harness.process_message(message, llm_fn)

        assert result.msg_type == "result"
        assert result.content["result"]["success"] is False
        assert "not found" in result.content["result"]["error"]

    @pytest.mark.asyncio
    async def test_handle_planner_calls_llm(self):
        harness = AgentHarness()
        message = AgentMessage(
            msg_id="msg1",
            from_agent="user",
            to_agent="planner",
            msg_type="task",
            content={"task": "do something"},
        )

        async def mock_llm(system_prompt, messages):
            return '{"steps": [{"step_id": 1, "action": "test", "params": {}}]}'

        result = await harness.process_message(message, mock_llm)

        assert result.msg_type == "result"
        assert result.from_agent == "planner"
        assert "plan" in result.content

    @pytest.mark.asyncio
    async def test_handle_reasoner_calls_llm(self):
        harness = AgentHarness()
        message = AgentMessage(
            msg_id="msg1",
            from_agent="tool",
            to_agent="reasoner",
            msg_type="task",
            content={"data": "some data"},
        )

        async def mock_llm(system_prompt, messages):
            return "analysis result"

        result = await harness.process_message(message, mock_llm)

        assert result.msg_type == "result"
        assert result.from_agent == "reasoner"
        assert "analysis" in result.content

    @pytest.mark.asyncio
    async def test_handle_reporter_calls_llm(self):
        harness = AgentHarness()
        message = AgentMessage(
            msg_id="msg1",
            from_agent="reasoner",
            to_agent="reporter",
            msg_type="task",
            content={"data": "some data"},
        )

        async def mock_llm(system_prompt, messages):
            return "final report"

        result = await harness.process_message(message, mock_llm)

        assert result.msg_type == "result"
        assert result.from_agent == "reporter"
        assert "report" in result.content
