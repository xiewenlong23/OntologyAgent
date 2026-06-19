from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.models import Object, ObjectLink
from ontology_agent.ontology.types import ObjectCreate, ObjectResponse


class InstanceStorage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_object(self, tenant_id: str, ontology_id: str, obj: ObjectCreate) -> Object:
        object_ = Object(
            tenant_id=tenant_id,
            ontology_id=ontology_id,
            object_type=obj.object_type,
            api_name=obj.api_name,
            display_name=obj.display_name,
            properties=obj.properties,
        )
        self.session.add(object_)
        await self.session.commit()
        await self.session.refresh(object_)
        return object_

    async def search_objects(
        self,
        tenant_id: str,
        ontology_id: str,
        object_type: str | None = None,
        filters: dict | None = None,
        limit: int = 100,
    ) -> list[Object]:
        query = select(Object).where(
            Object.tenant_id == tenant_id,
            Object.ontology_id == ontology_id,
        )
        if object_type:
            query = query.where(Object.object_type == object_type)
        query = query.limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_object(self, object_id: str, tenant_id: str, properties: dict) -> Object | None:
        result = await self.session.execute(
            select(Object).where(Object.id == object_id, Object.tenant_id == tenant_id)
        )
        object_ = result.scalar_one_or_none()
        if not object_:
            return None
        object_.properties = {**object_.properties, **properties}
        await self.session.commit()
        await self.session.refresh(object_)
        return object_
