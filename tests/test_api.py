import pytest
from httpx import AsyncClient, ASGITransport
from ontology_agent.main import create_app
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.agent.messages import AgentMessage
from unittest.mock import AsyncMock, patch


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
async def client(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestHealthEndpoint:
    @pytest.mark.asyncio
    async def test_health_returns_ok(self, client):
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


class TestChatEndpoint:
    @pytest.mark.asyncio
    async def test_chat_post_returns_msg_id_and_content(self, client):
        with patch.object(AgentHarness, 'process_message', new_callable=AsyncMock) as mock_process:
            mock_result = AgentMessage(
                msg_id="test-msg-id",
                from_agent="planner",
                to_agent="user",
                msg_type="result",
                content={"plan": "test plan"},
            )
            mock_process.return_value = mock_result

            response = await client.post("/api/v1/chat", json={"task": "test task"})

            assert response.status_code == 200
            data = response.json()
            assert data["msg_id"] == "test-msg-id"
            assert data["content"] == {"plan": "test plan"}

    @pytest.mark.asyncio
    async def test_chat_post_creates_agent_message(self, client):
        with patch.object(AgentHarness, 'process_message', new_callable=AsyncMock) as mock_process:
            mock_result = AgentMessage(
                msg_id="test-msg-id",
                from_agent="planner",
                to_agent="user",
                msg_type="result",
                content={},
            )
            mock_process.return_value = mock_result

            await client.post("/api/v1/chat", json={"task": "test task"})

            call_args = mock_process.call_args
            agent_msg = call_args[0][0]
            assert agent_msg.from_agent == "user"
            assert agent_msg.to_agent == "planner"
            assert agent_msg.msg_type == "task"
            assert agent_msg.content == {"task": "test task"}


class TestWebSocketEndpoint:
    @pytest.mark.asyncio
    async def test_websocket_endpoint_exists(self, app):
        routes = [route.path for route in app.routes]
        assert "/api/v1/ws/{session_id}" in routes or "/ws/{session_id}" in [r.replace("/api/v1", "") for r in routes]


class TestOntologyEndpoints:
    @pytest.mark.asyncio
    async def test_create_ontology_returns_ontology_id_and_name(self, client):
        mock_ontology = type('MockOntology', (), {
            'id': 'test-ontology-id',
            'name': 'test-ontology',
            'object_types': {},
            'properties': {},
        })()

        with patch('ontology_agent.api.ontology.OntologyStorage') as MockStorage:
            mock_instance = AsyncMock()
            mock_instance.create_ontology.return_value = mock_ontology
            MockStorage.return_value = mock_instance

            response = await client.post(
                "/api/v1/ontology/ontologies",
                json={"tenant_id": "test", "name": "test-ontology"},
            )

            assert response.status_code == 201
            data = response.json()
            assert data["id"] == "test-ontology-id"
            assert data["name"] == "test-ontology"

    @pytest.mark.asyncio
    async def test_get_ontology_returns_ontology_data(self, client):
        mock_ontology = type('MockOntology', (), {
            'id': 'test-ontology-id',
            'name': 'test-ontology',
            'object_types': {'type1': {'name': 'Type1'}},
            'properties': {'prop1': {'name': 'Prop1'}},
        })()

        with patch('ontology_agent.api.ontology.OntologyStorage') as MockStorage:
            mock_instance = AsyncMock()
            mock_instance.get_ontology.return_value = mock_ontology
            MockStorage.return_value = mock_instance

            response = await client.get("/api/v1/ontology/ontologies/test-ontology-id?tenant_id=test")

            assert response.status_code == 200
            data = response.json()
            assert data["id"] == "test-ontology-id"
            assert data["name"] == "test-ontology"
            assert data["object_types"] == {'type1': {'name': 'Type1'}}

    @pytest.mark.asyncio
    async def test_get_ontology_returns_404_for_missing(self, client):
        with patch('ontology_agent.api.ontology.OntologyStorage') as MockStorage:
            mock_instance = AsyncMock()
            mock_instance.get_ontology.return_value = None
            MockStorage.return_value = mock_instance

            response = await client.get("/api/v1/ontology/ontologies/nonexistent-id?tenant_id=test")

            assert response.status_code == 404
            assert response.json()["detail"] == "Ontology not found"

    @pytest.mark.asyncio
    async def test_search_objects_returns_object_list(self, client):
        mock_object1 = type('MockObject', (), {'id': 'obj1', 'display_name': 'Object 1'})()
        mock_object2 = type('MockObject', (), {'id': 'obj2', 'display_name': 'Object 2'})()

        with patch('ontology_agent.api.ontology.InstanceStorage') as MockStorage:
            mock_instance = AsyncMock()
            mock_instance.search_objects.return_value = [mock_object1, mock_object2]
            MockStorage.return_value = mock_instance

            response = await client.post(
                "/api/v1/ontology/objects/search",
                json={"tenant_id": "test", "ontology_id": "ont-id"},
            )

            assert response.status_code == 200
            data = response.json()
            assert len(data["objects"]) == 2
            assert data["objects"][0]["id"] == "obj1"
            assert data["objects"][0]["display_name"] == "Object 1"


class TestAPIRoutes:
    def test_chat_router_included(self, app):
        routes = [route.path for route in app.routes]
        chat_routes = [r for r in routes if "chat" in r]
        assert len(chat_routes) > 0

    def test_ontology_router_included(self, app):
        routes = [route.path for route in app.routes]
        ontology_routes = [r for r in routes if "ontology" in r]
        assert len(ontology_routes) > 0

    def test_health_endpoint_exists(self, app):
        routes = [route.path for route in app.routes]
        health_routes = [r for r in routes if "health" in r]
        assert len(health_routes) > 0