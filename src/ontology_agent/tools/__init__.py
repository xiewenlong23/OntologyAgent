from ontology_agent.tools.base import Tool, ToolResult, ToolExecutionError
from ontology_agent.tools.registry import ToolRegistry
from ontology_agent.tools.ontology_read import OntologyReadTool
from ontology_agent.tools.ontology_write import OntologyWriteTool
from ontology_agent.tools.entity_search import EntitySearchTool
from ontology_agent.tools.entity_write import EntityWriteTool

__all__ = ["Tool", "ToolResult", "ToolExecutionError", "ToolRegistry"]


def register_all_tools():
    registry = ToolRegistry.get_instance()
    # Only register tools that aren't already registered (idempotent)
    if registry.get("ontology_read") is None:
        registry.register(OntologyReadTool())
    if registry.get("ontology_write") is None:
        registry.register(OntologyWriteTool())
    if registry.get("entity_search") is None:
        registry.register(EntitySearchTool())
    if registry.get("entity_write") is None:
        registry.register(EntityWriteTool())
