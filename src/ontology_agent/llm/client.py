import httpx
import json
from typing import Optional
from ontology_agent.config import get_settings
import logging

logger = logging.getLogger(__name__)


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
        logger.info(f"LLMClient initialized: base_url={self.base_url}, model={self.model}")

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

        logger.info(f"LLM request: {self.base_url}/chat/completions, model={self.model}, messages={request_messages}")

        response = await self.client.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload,
        )
        logger.info(f"LLM response status: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        logger.info(f"LLM response data: {data}")

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
