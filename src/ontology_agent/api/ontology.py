from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.session import get_async_session
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.instance import InstanceStorage

router = APIRouter(prefix="/api/v1/ontology", tags=["ontology"])


@router.post("/ontologies")
async def create_ontology(
    tenant_id: str,
    name: str,
    description: str | None = None,
    session: AsyncSession = Depends(get_async_session),
):
    storage = OntologyStorage(session)
    ontology = await storage.create_ontology(tenant_id, name, description)
    return {"id": ontology.id, "name": ontology.name}


@router.get("/ontologies/{ontology_id}")
async def get_ontology(
    ontology_id: str,
    tenant_id: str,
    session: AsyncSession = Depends(get_async_session),
):
    storage = OntologyStorage(session)
    ontology = await storage.get_ontology(ontology_id, tenant_id)
    if not ontology:
        return {"error": "Not found"}
    return {
        "id": ontology.id,
        "name": ontology.name,
        "object_types": ontology.object_types,
        "properties": ontology.properties,
    }


@router.post("/objects/search")
async def search_objects(
    tenant_id: str,
    ontology_id: str,
    object_type: str | None = None,
    session: AsyncSession = Depends(get_async_session),
):
    storage = InstanceStorage(session)
    objects = await storage.search_objects(tenant_id, ontology_id, object_type)
    return {"objects": [{"id": o.id, "display_name": o.display_name} for o in objects]}