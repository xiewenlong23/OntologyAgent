import httpx
import json
from typing import Optional
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential
from ontology_agent.config import get_settings
import logging

logger = logging.getLogger(__name__)

_RETRYABLE_HTTP_STATUS = {408, 425, 429, 500, 502, 503, 504}
_MAX_ATTEMPTS = 3


class _RetryableHTTPError(Exception):
    """Wraps an HTTP response whose status code we want to retry on."""


def _is_retryable_status(response: httpx.Response) -> bool:
    return response.status_code in _RETRYABLE_HTTP_STATUS


class LLMClient:
    """Simple LLM client supporting OpenAI-compatible APIs."""

    def __init__(
        self,
        api_key: str,
        base_url: str = None,
        model: str = None,
    ):
        settings = get_settings()
        self.api_key = api_key
        self.base_url = (base_url or settings.llm_base_url).rstrip("/")
        self.model = model or settings.llm_model
        self.client = httpx.AsyncClient(timeout=60.0)
        logger.info("LLMClient initialized: base_url=%s, model=%s", self.base_url, self.model)

    async def aclose(self) -> None:
        await self.client.aclose()

    async def _post_with_retry(self, url: str, headers: dict, payload: dict) -> httpx.Response:
        @retry(
            retry=retry_if_exception_type((httpx.TransportError, _RetryableHTTPError)),
            stop=stop_after_attempt(_MAX_ATTEMPTS),
            wait=wait_exponential(multiplier=0.5, min=0.5, max=4),
            reraise=True,
        )
        async def _do_post() -> httpx.Response:
            response = await self.client.post(url, headers=headers, json=payload)
            if _is_retryable_status(response):
                raise _RetryableHTTPError(f"HTTP {response.status_code}")
            return response

        return await _do_post()

    async def complete(self, prompt: str = "", system: Optional[str] = None, messages: list = None, system_prompt: str = None) -> str:
        """Send a completion request to the LLM."""
        request_messages = []

        sys_content = system or system_prompt
        if sys_content:
            request_messages.append({"role": "system", "content": sys_content})

        if messages:
            request_messages.extend(messages)
        elif prompt:
            request_messages.append({"role": "user", "content": prompt})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": request_messages,
            "max_tokens": 1024,
        }

        logger.debug(
            "LLM request: %s/chat/completions model=%s msg_count=%d",
            self.base_url, self.model, len(request_messages),
        )

        response = await self._post_with_retry(
            f"{self.base_url}/chat/completions", headers, payload
        )
        logger.info("LLM response status: %d", response.status_code)
        response.raise_for_status()
        data = response.json()
        logger.debug("LLM response body: %s", data)

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        return ""


def create_llm_client() -> Optional[LLMClient]:
    """Create an LLM client based on settings."""
    settings = get_settings()
    if not settings.llm_api_key:
        return None

    return LLMClient(
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        model=settings.llm_model,
    )
