import pytest
from ontology_agent.tools.ontology_read import OntologyReadTool
from ontology_agent.tools.ontology_write import OntologyWriteTool
from ontology_agent.tools.registry import ToolRegistry
from ontology_agent.ontology.storage import OntologyStorage


@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset the ToolRegistry singleton before each test."""
    ToolRegistry._instance = None
    yield
    ToolRegistry._instance = None


@pytest.fixture
async def created_ontology(db_session):
    """Create a test ontology and return its ID."""
    storage = OntologyStorage(db_session)
    ont = await storage.create_ontology(
        tenant_id="test-tenant",
        name="Test Ontology",
        description="A test ontology description",
    )
    return ont.id


@pytest.mark.asyncio
async def test_ontology_read_tool_reads_existing_ontology(created_ontology):
    tool = OntologyReadTool()
    params = {"ontology_id": created_ontology}
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["id"] == created_ontology
    assert result.data["name"] == "Test Ontology"
    assert result.data["description"] == "A test ontology description"
    assert result.data["object_types"] == {}
    assert result.data["properties"] == {}
    assert result.data["link_types"] == {}
    assert result.execution_time_ms >= 0


@pytest.mark.asyncio
async def test_ontology_read_tool_returns_error_for_nonexistent():
    tool = OntologyReadTool()
    params = {"ontology_id": "nonexistent-id"}
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert result.error == "Ontology not found"


@pytest.mark.asyncio
async def test_ontology_write_tool_creates_ontology():
    tool = OntologyWriteTool()
    params = {
        "action": "create_ontology",
        "data": {"name": "New Ontology", "description": "Created by test"},
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert "ontology_id" in result.data
    assert result.execution_time_ms >= 0


@pytest.mark.asyncio
async def test_ontology_write_tool_adds_object_type(created_ontology):
    tool = OntologyWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "add_object_type",
        "data": {
            "id": "person",
            "api_name": "Person",
            "display_name": "Person",
            "description": "A person object type",
            "properties": ["name", "age"],
            "relations": [],
        },
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["updated"] is True


@pytest.mark.asyncio
async def test_ontology_write_tool_adds_property(created_ontology):
    tool = OntologyWriteTool()
    params = {
        "ontology_id": created_ontology,
        "action": "add_property",
        "data": {
            "id": "name",
            "api_name": "name",
            "display_name": "Name",
            "type": "string",
            "description": "The name property",
        },
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is True
    assert result.data["updated"] is True


@pytest.mark.asyncio
async def test_ontology_write_tool_requires_ontology_id_for_add_property():
    tool = OntologyWriteTool()
    params = {
        "action": "add_property",
        "data": {
            "id": "name",
            "api_name": "name",
            "display_name": "Name",
            "type": "string",
        },
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "ontology_id required" in result.error


@pytest.mark.asyncio
async def test_ontology_write_tool_add_property_not_found():
    tool = OntologyWriteTool()
    params = {
        "ontology_id": "nonexistent-id",
        "action": "add_property",
        "data": {
            "id": "name",
            "api_name": "name",
            "display_name": "Name",
            "type": "string",
        },
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "Ontology not found" in result.error


@pytest.mark.asyncio
async def test_ontology_write_tool_requires_ontology_id_for_add_object_type():
    tool = OntologyWriteTool()
    params = {
        "action": "add_object_type",
        "data": {
            "id": "person",
            "api_name": "Person",
            "display_name": "Person",
        },
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "ontology_id required" in result.error


@pytest.mark.asyncio
async def test_ontology_write_tool_unknown_action():
    tool = OntologyWriteTool()
    params = {
        "action": "unknown_action",
        "data": {},
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "Unknown action" in result.error


@pytest.mark.asyncio
async def test_ontology_write_tool_add_object_type_not_found():
    tool = OntologyWriteTool()
    params = {
        "ontology_id": "nonexistent-id",
        "action": "add_object_type",
        "data": {
            "id": "person",
            "api_name": "Person",
            "display_name": "Person",
        },
    }
    context = {"tenant_id": "test-tenant"}

    result = await tool.execute(params, context)

    assert result.success is False
    assert "Ontology not found" in result.error


@pytest.mark.asyncio
async def test_tools_registered_in_registry():
    from ontology_agent.tools import register_all_tools

    register_all_tools()
    registry = ToolRegistry.get_instance()

    read_tool = registry.get("ontology_read")
    assert read_tool is not None
    assert isinstance(read_tool, OntologyReadTool)

    write_tool = registry.get("ontology_write")
    assert write_tool is not None
    assert isinstance(write_tool, OntologyWriteTool)
