import time

from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.types import ObjectTypeDefinition, PropertyDefinition
from ontology_agent.db.session import AsyncSessionLocal


class OntologyWriteTool(Tool):
    name = "ontology_write"
    description = "Create or update ontology schema"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string", "description": "Ontology ID (empty for create)"},
            "action": {"type": "string", "enum": ["create_ontology", "add_object_type", "add_property"]},
            "data": {"type": "object"},
        },
        "required": ["action", "data"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        start = time.time()

        tenant_id = context.get("tenant_id")
        action = params["action"]
        data = params["data"]

        async with AsyncSessionLocal() as session:
            storage = OntologyStorage(session)

            if action == "create_ontology":
                ontology = await storage.create_ontology(
                    tenant_id=tenant_id,
                    name=data.get("name", "Untitled"),
                    description=data.get("description"),
                )
                return ToolResult(
                    success=True,
                    data={"ontology_id": ontology.id},
                    execution_time_ms=int((time.time() - start) * 1000),
                )

            elif action == "add_object_type":
                ontology_id = params.get("ontology_id")
                if not ontology_id:
                    return ToolResult(success=False, error="ontology_id required", execution_time_ms=int((time.time() - start) * 1000))

                object_type = ObjectTypeDefinition(**data)
                updated = await storage.update_object_types(ontology_id, tenant_id, [object_type])
                if not updated:
                    return ToolResult(success=False, error="Ontology not found", execution_time_ms=int((time.time() - start) * 1000))

                return ToolResult(success=True, data={"updated": True}, execution_time_ms=int((time.time() - start) * 1000))

            elif action == "add_property":
                ontology_id = params.get("ontology_id")
                if not ontology_id:
                    return ToolResult(success=False, error="ontology_id required", execution_time_ms=int((time.time() - start) * 1000))

                property_def = PropertyDefinition(**data)
                updated = await storage.update_properties(ontology_id, tenant_id, [property_def])
                if not updated:
                    return ToolResult(success=False, error="Ontology not found", execution_time_ms=int((time.time() - start) * 1000))

                return ToolResult(success=True, data={"updated": True}, execution_time_ms=int((time.time() - start) * 1000))

            return ToolResult(success=False, error=f"Unknown action: {action}", execution_time_ms=int((time.time() - start) * 1000))
