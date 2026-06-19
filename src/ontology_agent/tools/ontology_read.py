import time

from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.db.session import AsyncSessionLocal


class OntologyReadTool(Tool):
    name = "ontology_read"
    description = "Read ontology schema (Object Types, Properties, Link Types)"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string", "description": "Ontology ID"},
        },
        "required": ["ontology_id"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        start = time.time()

        tenant_id = context.get("tenant_id")
        ontology_id = params["ontology_id"]

        async with AsyncSessionLocal() as session:
            storage = OntologyStorage(session)
            ontology = await storage.get_ontology(ontology_id, tenant_id)

            if not ontology:
                return ToolResult(
                    success=False,
                    error="Ontology not found",
                    execution_time_ms=int((time.time() - start) * 1000),
                )

            return ToolResult(
                success=True,
                data={
                    "id": ontology.id,
                    "name": ontology.name,
                    "description": ontology.description,
                    "version": ontology.version,
                    "object_types": ontology.object_types,
                    "properties": ontology.properties,
                    "link_types": ontology.link_types,
                },
                execution_time_ms=int((time.time() - start) * 1000),
            )
