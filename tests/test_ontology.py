import pytest
from ontology_agent.ontology.storage import OntologyStorage


@pytest.mark.asyncio
async def test_create_and_get_ontology(db_session):
    storage = OntologyStorage(db_session)
    ont = await storage.create_ontology(
        tenant_id="test-tenant",
        name="Test Ontology",
        description="A test ontology",
    )
    assert ont.id is not None
    assert ont.name == "Test Ontology"

    retrieved = await storage.get_ontology(ont.id, "test-tenant")
    assert retrieved is not None
    assert retrieved.name == "Test Ontology"
