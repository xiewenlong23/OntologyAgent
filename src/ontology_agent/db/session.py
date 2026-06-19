from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from ontology_agent.config import get_settings

settings = get_settings()

engine = create_async_engine(settings.database_url, echo=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
