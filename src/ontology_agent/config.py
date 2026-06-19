from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ontology"
    llm_provider: str = "minimax"
    llm_api_key: str = ""
    llm_model: str = "minimax-01"
    deep_agent_enabled: bool = True
    a2ui_renderer_url: str = "http://localhost:5173"
    ws_max_connections: int = 1000
    ws_ping_interval: int = 30
    ws_ping_timeout: int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()
