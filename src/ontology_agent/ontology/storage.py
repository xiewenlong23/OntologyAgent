from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.models import Ontology
from ontology_agent.ontology.types import ObjectTypeDefinition, PropertyDefinition


class OntologyStorage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_ontology(
        self,
        tenant_id: str,
        name: str,
        description: str | None = None,
    ) -> Ontology:
        ontology = Ontology(
            tenant_id=tenant_id,
            name=name,
            description=description,
            object_types={},
            properties={},
            link_types={},
        )
        self.session.add(ontology)
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology

    async def get_ontology(self, ontology_id: str, tenant_id: str) -> Ontology | None:
        result = await self.session.execute(
            select(Ontology).where(
                Ontology.id == ontology_id,
                Ontology.tenant_id == tenant_id,
            )
        )
        return result.scalar_one_or_none()

    async def update_object_types(
        self, ontology_id: str, tenant_id: str, object_types: list[ObjectTypeDefinition]
    ) -> Ontology | None:
        ontology = await self.get_ontology(ontology_id, tenant_id)
        if not ontology:
            return None
        merged = dict(ontology.object_types or {})
        for ot in object_types:
            merged[ot.id] = ot.model_dump()
        ontology.object_types = merged
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology

    async def update_properties(
        self, ontology_id: str, tenant_id: str, properties: list[PropertyDefinition]
    ) -> Ontology | None:
        ontology = await self.get_ontology(ontology_id, tenant_id)
        if not ontology:
            return None
        merged = dict(ontology.properties or {})
        for p in properties:
            merged[p.id] = p.model_dump()
        ontology.properties = merged
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology
