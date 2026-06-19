from ontology_agent.tools.base import Tool, ToolResult


class ToolRegistry:
    _instance = None

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    @classmethod
    def get_instance(cls) -> "ToolRegistry":
        if cls._instance is None:
            cls._instance = ToolRegistry()
        return cls._instance

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool {tool.name} already registered")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def list_tools(self) -> list[Tool]:
        return list(self._tools.values())

    async def execute(self, name: str, params: dict, context: dict) -> ToolResult:
        tool = self.get(name)
        if not tool:
            return ToolResult(success=False, error=f"Tool {name} not found")
        try:
            return await tool.execute(params, context)
        except Exception as e:
            return ToolResult(success=False, error=str(e))
