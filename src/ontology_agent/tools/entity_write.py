from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.ontology.types import ObjectCreate
from ontology_agent.db.session import AsyncSessionLocal


class EntityWriteTool(Tool):
    name = "entity_write"
    description = "Write or update entity data"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string"},
            "action": {"type": "string", "enum": ["create", "update"]},
            "object_id": {"type": "string", "description": "Required for update"},
            "object_type": {"type": "string"},
            "api_name": {"type": "string"},
            "display_name": {"type": "string"},
            "properties": {"type": "object"},
        },
        "required": ["ontology_id", "action"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        import time
        start = time.time()

        tenant_id = context.get("tenant_id")
        ontology_id = params["ontology_id"]
        action = params["action"]

        async with AsyncSessionLocal() as session:
            storage = InstanceStorage(session)

            if action == "create":
                obj_data = ObjectCreate(
                    object_type=params["object_type"],
                    api_name=params["api_name"],
                    display_name=params["display_name"],
                    properties=params.get("properties", {}),
                )
                obj = await storage.create_object(tenant_id, ontology_id, obj_data)
                return ToolResult(
                    success=True,
                    data={"object_id": obj.id},
                    execution_time_ms=int((time.time() - start) * 1000),
                )

            elif action == "update":
                object_id = params.get("object_id")
                if not object_id:
                    return ToolResult(success=False, error="object_id required for update", execution_time_ms=int((time.time() - start) * 1000))
                updated = await storage.update_object(object_id, tenant_id, params.get("properties", {}))
                if not updated:
                    return ToolResult(success=False, error="Object not found", execution_time_ms=int((time.time() - start) * 1000))
                return ToolResult(success=True, data={"updated": True}, execution_time_ms=int((time.time() - start) * 1000))

            return ToolResult(success=False, error=f"Unknown action: {action}", execution_time_ms=int((time.time() - start) * 1000))
