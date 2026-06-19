import pytest
from ontology_agent.tools.base import Tool, ToolResult, ToolExecutionError
from ontology_agent.tools.registry import ToolRegistry


@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset the ToolRegistry singleton before each test."""
    ToolRegistry._instance = None
    yield
    ToolRegistry._instance = None


class DummyTool(Tool):
    """A concrete implementation of Tool for testing."""

    def __init__(self, name="dummy", is_admin_only=False):
        self.name = name
        self.description = "A dummy tool for testing"
        self.params_schema = {"type": "object", "properties": {}}
        self.is_admin_only = is_admin_only
        self.call_count = 0

    async def execute(self, params: dict, context: dict) -> ToolResult:
        self.call_count += 1
        return ToolResult(success=True, data={"result": "ok"}, execution_time_ms=10)


@pytest.mark.asyncio
async def test_tool_result_dataclass():
    result = ToolResult(success=True, data={"key": "value"}, error=None, execution_time_ms=100)
    assert result.success is True
    assert result.data == {"key": "value"}
    assert result.error is None
    assert result.execution_time_ms == 100


@pytest.mark.asyncio
async def test_tool_result_defaults():
    result = ToolResult(success=False, error="something went wrong")
    assert result.success is False
    assert result.data is None
    assert result.error == "something went wrong"
    assert result.execution_time_ms == 0


def test_tool_execution_error():
    err = ToolExecutionError("test error")
    assert str(err) == "test error"
    assert isinstance(err, Exception)


def test_tool_is_abstract():
    with pytest.raises(TypeError):
        Tool()


def test_tool_registry_singleton():
    registry1 = ToolRegistry.get_instance()
    registry2 = ToolRegistry.get_instance()
    assert registry1 is registry2


def test_tool_registry_register():
    registry = ToolRegistry.get_instance()
    tool = DummyTool(name="register_test")
    registry.register(tool)
    assert registry.get("register_test") is tool


def test_tool_registry_register_duplicate_raises():
    registry = ToolRegistry.get_instance()
    tool = DummyTool(name="dup_test")
    registry.register(tool)
    with pytest.raises(ValueError, match="already registered"):
        registry.register(tool)


def test_tool_registry_get_missing():
    registry = ToolRegistry.get_instance()
    assert registry.get("nonexistent") is None


def test_tool_registry_list_tools():
    registry = ToolRegistry.get_instance()
    tool1 = DummyTool(name="list_tool1")
    tool2 = DummyTool(name="list_tool2")
    registry.register(tool1)
    registry.register(tool2)
    tools = registry.list_tools()
    assert len(tools) >= 2
    names = [t.name for t in tools]
    assert "list_tool1" in names
    assert "list_tool2" in names


@pytest.mark.asyncio
async def test_tool_registry_execute_success():
    registry = ToolRegistry.get_instance()
    tool = DummyTool(name="exec_tool")
    registry.register(tool)
    result = await registry.execute("exec_tool", {}, {})
    assert result.success is True
    assert result.data == {"result": "ok"}


@pytest.mark.asyncio
async def test_tool_registry_execute_not_found():
    registry = ToolRegistry.get_instance()
    result = await registry.execute("nonexistent_tool", {}, {})
    assert result.success is False
    assert "not found" in result.error


@pytest.mark.asyncio
async def test_tool_registry_execute_exception():
    registry = ToolRegistry.get_instance()

    class FailingTool(Tool):
        def __init__(self):
            self.name = "failing"
            self.description = "A failing tool"
            self.params_schema = {}

        async def execute(self, params: dict, context: dict) -> ToolResult:
            raise RuntimeError("intentional failure")

    registry.register(FailingTool())
    result = await registry.execute("failing", {}, {})
    assert result.success is False
    assert "intentional failure" in result.error


@pytest.mark.asyncio
async def test_tool_execute_is_async():
    tool = DummyTool()
    result = await tool.execute({}, {})
    assert isinstance(result, ToolResult)
