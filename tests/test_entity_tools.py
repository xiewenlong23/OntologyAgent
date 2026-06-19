import pytest
from ontology_agent.tools.entity_search import EntitySearchTool
from ontology_agent.tools.entity_write import EntityWriteTool
from ontology_agent.tools.registry import ToolRegistry
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.ontology.types import ObjectCreate
from ontology_agent.db.session import AsyncSessionLocal


@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset the ToolRegistry singleton before each test."""
    ToolRegistry._instance = None
    yield
    ToolRegistry._instance = None


@pytest.fixture
async def created_ontology():
    """Create a test ontology and return its ID."""
    async with AsyncSessionLocal() as session:
        storage = OntologyStorage(session)
        ont = await storage.create_ontology(
            tenant_id="test-tenant",
            name="Test Ontology",
            description="A test ontology description",
        )
        return ont.id


@pytest.fixture
async def created_object(created_ontology):
    """Create a test object and return its ID."""
    async with AsyncSessionLocal() as session:
        storage = InstanceStorage(session)
        obj_data = ObjectCreate(
            object_type="product",
            api_name="Product",
            display_name="Test Product",
            properties={"price": 100, "color": "red"},
        )
        obj = await storage.create_object("test-tenant", created_ontology, obj_data)
        return obj.id


@pytest.mark.asyncio
async def test_entity_search_tool_returns_empty_list_for_new_ontology(created_ontology):
    tool = EntitySearchTool()
    params = {"ontology_id": created_ontology}
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["objects"] == []
    assert result.data["count"] == 0
    assert result.execution_time_ms >= 0


@pytest.mark.asyncio
async def test_entity_search_tool_finds_created_object(created_ontology, created_object):
    tool = EntitySearchTool()
    params = {"ontology_id": created_ontology}
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["count"] == 1
    assert len(result.data["objects"]) == 1
    obj = result.data["objects"][0]
    assert obj["id"] == created_object
    assert obj["object_type"] == "product"
    assert obj["api_name"] == "Product"
    assert obj["display_name"] == "Test Product"
    assert obj["properties"] == {"price": 100, "color": "red"}


@pytest.mark.asyncio
async def test_entity_search_tool_filters_by_object_type(created_ontology, created_object):
    tool = EntitySearchTool()
    params = {
        "ontology_id": created_ontology,
        "object_type": "product",
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["count"] == 1

    params["object_type"] = "nonexistent"
    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["count"] == 0


@pytest.mark.asyncio
async def test_entity_search_tool_respects_limit(created_ontology):
    tool = EntitySearchTool()
    params = {
        "ontology_id": created_ontology,
        "limit": 5,
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["count"] == 0


@pytest.mark.asyncio
async def test_entity_write_tool_creates_object(created_ontology):
    tool = EntityWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "create",
        "object_type": "customer",
        "api_name": "Customer",
        "display_name": "Test Customer",
        "properties": {"name": "John", "email": "john@example.com"},
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert "object_id" in result.data
    assert result.execution_time_ms >= 0

    search_tool = EntitySearchTool()
    search_result = await search_tool.execute(
        {"ontology_id": created_ontology}, context
    )
    assert search_result.data["count"] == 1
    assert search_result.data["objects"][0]["api_name"] == "Customer"


@pytest.mark.asyncio
async def test_entity_write_tool_updates_object(created_ontology, created_object):
    tool = EntityWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "update",
        "object_id": created_object,
        "properties": {"price": 200, "size": "large"},
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["updated"] is True

    search_tool = EntitySearchTool()
    search_result = await search_tool.execute(
        {"ontology_id": created_ontology}, context
    )
    obj = search_result.data["objects"][0]
    assert obj["properties"]["price"] == 200
    assert obj["properties"]["size"] == "large"
    assert obj["properties"]["color"] == "red"


@pytest.mark.asyncio
async def test_entity_write_tool_update_requires_object_id(created_ontology):
    tool = EntityWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "update",
        "properties": {"price": 200},
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "object_id required for update" in result.error


@pytest.mark.asyncio
async def test_entity_write_tool_update_nonexistent_object(created_ontology):
    tool = EntityWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "update",
        "object_id": "nonexistent-id",
        "properties": {"price": 200},
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert result.error == "Object not found"


@pytest.mark.asyncio
async def test_entity_write_tool_unknown_action(created_ontology):
    tool = EntityWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "unknown_action",
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "Unknown action: unknown_action" in result.error
