from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.models import Ontology
from ontology_agent.ontology.types import ObjectTypeDefinition, PropertyDefinition, LinkTypeDefinition


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
        ontology.object_types = {ot.id: ot.model_dump() for ot in object_types}
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology

    async def update_properties(
        self, ontology_id: str, tenant_id: str, properties: list[PropertyDefinition]
    ) -> Ontology | None:
        ontology = await self.get_ontology(ontology_id, tenant_id)
        if not ontology:
            return None
        ontology.properties = {p.id: p.model_dump() for p in properties}
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology
