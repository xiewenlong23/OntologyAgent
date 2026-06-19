import pytest
import asyncio
import sys
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from ontology_agent.db.models import Base


_engine = None
_session_factory = None


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def db_engine():
    """Create a fresh engine for each test."""
    global _engine, _session_factory

    _engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost:5432/ontology",
        echo=False,
    )

    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    _session_factory = async_sessionmaker(
        _engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    yield _engine

    await _engine.dispose()


@pytest.fixture(scope="function")
async def db_session(db_engine):
    """Create a fresh session for each test with rollback."""
    async with _session_factory() as session:
        yield session
        await session.rollback()


@pytest.fixture(scope="function", autouse=True)
async def patch_modules(db_engine):
    """Patch tools to use test session factory."""
    global _session_factory

    modules_to_patch = [
        'ontology_agent.tools.ontology_read',
        'ontology_agent.tools.ontology_write',
        'ontology_agent.tools.entity_search',
        'ontology_agent.tools.entity_write',
        'ontology_agent.ontology.storage',
        'ontology_agent.ontology.instance',
    ]

    patched = {}
    for name in modules_to_patch:
        if name in sys.modules:
            module = sys.modules[name]
            if hasattr(module, 'AsyncSessionLocal'):
                patched[name] = module.AsyncSessionLocal
                module.AsyncSessionLocal = _session_factory

    yield

    # Restore
    for name, original in patched.items():
        sys.modules[name].AsyncSessionLocal = original
