import httpx
import json
from typing import Optional
from ontology_agent.config import get_settings


class LLMClient:
    """Simple LLM client supporting OpenAI-compatible APIs."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.minimax.chat/v1",
        model: str = "MiniMax-01",
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.client = httpx.AsyncClient(timeout=60.0)

    async def complete(self, prompt: str, system: Optional[str] = None) -> str:
        """Send a completion request to the LLM."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 1024,
        }

        response = await self.client.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()

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
        model=settings.llm_model,
    )
