import pytest
from unittest.mock import AsyncMock, patch
import httpx
from ontology_agent.llm.client import LLMClient, _RetryableHTTPError, _is_retryable_status


def _mock_response(status: int, body: dict) -> httpx.Response:
    """Build an httpx.Response with a request attached so raise_for_status works."""
    request = httpx.Request("POST", "http://test/chat/completions")
    return httpx.Response(status, request=request, json=body)


def test_is_retryable_status():
    assert _is_retryable_status(httpx.Response(429)) is True
    assert _is_retryable_status(httpx.Response(503)) is True
    assert _is_retryable_status(httpx.Response(500)) is True
    assert _is_retryable_status(httpx.Response(400)) is False
    assert _is_retryable_status(httpx.Response(401)) is False
    assert _is_retryable_status(httpx.Response(200)) is False


@pytest.mark.asyncio
async def test_complete_builds_correct_payload():
    client = LLMClient(api_key="test-key", base_url="https://api.example.com/v1", model="test-model")
    try:
        captured = {}

        async def fake_post(url, headers, json):
            captured["url"] = url
            captured["headers"] = headers
            captured["payload"] = json
            return _mock_response(200, {"choices": [{"message": {"content": "ok"}}]})

        with patch.object(client.client, "post", side_effect=fake_post):
            result = await client.complete(
                prompt="hi",
                system="be terse",
                messages=[{"role": "user", "content": "hi"}],
            )

        assert result == "ok"
        assert captured["url"] == "https://api.example.com/v1/chat/completions"
        assert captured["headers"]["Authorization"] == "Bearer test-key"
        assert captured["payload"]["model"] == "test-model"
        assert captured["payload"]["messages"][0] == {"role": "system", "content": "be terse"}
        assert captured["payload"]["messages"][1] == {"role": "user", "content": "hi"}
        assert captured["payload"]["max_tokens"] == 1024
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_complete_uses_prompt_when_no_messages():
    client = LLMClient(api_key="k", base_url="https://api.example.com", model="m")
    try:
        captured = {}

        async def fake_post(url, headers, json):
            captured["payload"] = json
            return _mock_response(200, {"choices": [{"message": {"content": "x"}}]})

        with patch.object(client.client, "post", side_effect=fake_post):
            await client.complete(prompt="hello")

        assert captured["payload"]["messages"] == [{"role": "user", "content": "hello"}]
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_complete_returns_empty_when_no_choices():
    client = LLMClient(api_key="k", base_url="https://api.example.com", model="m")
    try:
        async def fake_post(url, headers, json):
            return _mock_response(200, {"choices": []})

        with patch.object(client.client, "post", side_effect=fake_post):
            result = await client.complete(prompt="hi")

        assert result == ""
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_complete_retries_on_503():
    client = LLMClient(api_key="k", base_url="https://api.example.com", model="m")
    try:
        call_count = {"n": 0}

        async def fake_post(url, headers, json):
            call_count["n"] += 1
            if call_count["n"] < 3:
                return _mock_response(503, {"error": "unavailable"})
            return _mock_response(200, {"choices": [{"message": {"content": "recovered"}}]})

        with patch.object(client.client, "post", side_effect=fake_post):
            result = await client.complete(prompt="hi")

        assert result == "recovered"
        assert call_count["n"] == 3
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_complete_does_not_retry_on_400():
    client = LLMClient(api_key="k", base_url="https://api.example.com", model="m")
    try:
        call_count = {"n": 0}

        async def fake_post(url, headers, json):
            call_count["n"] += 1
            return _mock_response(400, {"error": "bad request"})

        with patch.object(client.client, "post", side_effect=fake_post):
            with pytest.raises(httpx.HTTPStatusError):
                await client.complete(prompt="hi")

        assert call_count["n"] == 1
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_complete_gives_up_after_max_attempts():
    client = LLMClient(api_key="k", base_url="https://api.example.com", model="m")
    try:
        call_count = {"n": 0}

        async def fake_post(url, headers, json):
            call_count["n"] += 1
            return _mock_response(502, {"error": "bad gateway"})

        with patch.object(client.client, "post", side_effect=fake_post):
            with pytest.raises(_RetryableHTTPError):
                await client.complete(prompt="hi")

        assert call_count["n"] == 3
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_create_llm_client_returns_none_when_no_api_key():
    from ontology_agent.config import Settings
    with patch("ontology_agent.llm.client.get_settings", return_value=Settings(llm_api_key="")):
        from ontology_agent.llm.client import create_llm_client
        assert create_llm_client() is None
