from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.db.session import AsyncSessionLocal


class EntitySearchTool(Tool):
    name = "entity_search"
    description = "Query entity data (products, customers, etc.)"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string", "description": "Ontology ID"},
            "object_type": {"type": "string", "description": "Object type to search"},
            "filters": {"type": "object", "description": "Property filters"},
            "limit": {"type": "integer", "default": 100},
        },
        "required": ["ontology_id"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        import time
        start = time.time()

        tenant_id = context.get("tenant_id")
        ontology_id = params["ontology_id"]
        object_type = params.get("object_type")
        filters = params.get("filters", {})
        limit = params.get("limit", 100)

        async with AsyncSessionLocal() as session:
            storage = InstanceStorage(session)
            objects = await storage.search_objects(
                tenant_id=tenant_id,
                ontology_id=ontology_id,
                object_type=object_type,
                filters=filters,
                limit=limit,
            )

            return ToolResult(
                success=True,
                data={
                    "objects": [
                        {
                            "id": o.id,
                            "object_type": o.object_type,
                            "api_name": o.api_name,
                            "display_name": o.display_name,
                            "properties": o.properties,
                        }
                        for o in objects
                    ],
                    "count": len(objects),
                },
                execution_time_ms=int((time.time() - start) * 1000),
            )
