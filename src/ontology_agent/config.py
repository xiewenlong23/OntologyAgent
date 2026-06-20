from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ontology"
    db_echo: bool = False
    db_pool_size: int = 20
    db_max_overflow: int = 10
    db_pool_timeout: int = 30
    llm_provider: str = "minimax"
    llm_base_url: str = "https://api.minimax.io/v1"
    llm_api_key: str = ""
    llm_model: str = "MiniMax-M3"
    deep_agent_enabled: bool = True
    a2ui_renderer_url: str = "http://localhost:5173"
    ws_max_connections: int = 1000
    ws_ping_interval: int = 30
    ws_ping_timeout: int = 10
    internal_shared_secret: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()
