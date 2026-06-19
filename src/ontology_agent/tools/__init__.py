from ontology_agent.tools.base import Tool, ToolResult, ToolExecutionError
from ontology_agent.tools.registry import ToolRegistry
from ontology_agent.tools.ontology_read import OntologyReadTool
from ontology_agent.tools.ontology_write import OntologyWriteTool

__all__ = ["Tool", "ToolResult", "ToolExecutionError", "ToolRegistry"]


def register_all_tools():
    registry = ToolRegistry.get_instance()
    registry.register(OntologyReadTool())
    registry.register(OntologyWriteTool())
