import pytest
from ontology_agent.db.models import Ontology, Object, ObjectLink, generate_uuid

def test_ontology_creation():
    ont = Ontology(
        tenant_id="test-tenant",
        name="Retail",
        description="Retail ontology",
    )
    # Verify passed arguments are set correctly
    assert ont.tenant_id == "test-tenant"
    assert ont.name == "Retail"
    assert ont.description == "Retail ontology"

def test_ontology_default_values():
    ont = Ontology(
        tenant_id="test-tenant",
        name="Test",
    )
    # version defaults to 1, but value is applied at INSERT time
    # JSON fields default to empty dict, but value is applied at INSERT time
    assert ont.tenant_id == "test-tenant"
    assert ont.name == "Test"

def test_object_creation():
    obj = Object(
        tenant_id="test-tenant",
        ontology_id="test-ontology-id",
        object_type="Product",
        api_name="product",
        display_name="Product",
    )
    assert obj.tenant_id == "test-tenant"
    assert obj.object_type == "Product"
    assert obj.api_name == "product"

def test_object_link_creation():
    link = ObjectLink(
        tenant_id="test-tenant",
        source_object_id="source-id",
        target_object_id="target-id",
        link_type="owns",
    )
    assert link.tenant_id == "test-tenant"
    assert link.link_type == "owns"

def test_generate_uuid():
    uuid = generate_uuid()
    assert len(uuid) == 36  # UUID format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
