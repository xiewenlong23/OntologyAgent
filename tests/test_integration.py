import pytest
from ontology_agent.db.session import AsyncSessionLocal, engine
from ontology_agent.db.models import Base
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.ontology.types import ObjectCreate

@pytest.fixture(autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_full_ontology_flow():
    async with AsyncSessionLocal() as session:
        # 1. Create ontology
        storage = OntologyStorage(session)
        ont = await storage.create_ontology(
            tenant_id="test-tenant",
            name="Retail",
            description="Retail ontology",
        )
        assert ont.id is not None

        # 2. Create product object
        instance_storage = InstanceStorage(session)
        product = await instance_storage.create_object(
            tenant_id="test-tenant",
            ontology_id=ont.id,
            obj=ObjectCreate(
                object_type="product",
                api_name="iphone_15",
                display_name="iPhone 15",
                properties={"price": 6999, "category": "electronics"},
            ),
        )
        assert product.id is not None
        assert product.properties["price"] == 6999

        # 3. Search products
        results = await instance_storage.search_objects(
            tenant_id="test-tenant",
            ontology_id=ont.id,
            object_type="product",
        )
        assert len(results) == 1
        assert results[0].display_name == "iPhone 15"
