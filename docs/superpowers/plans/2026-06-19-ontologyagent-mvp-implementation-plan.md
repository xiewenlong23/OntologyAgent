# OntologyAgent MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a running ontology-aware agent that can load ontologies, converse with users, and invoke tools to complete simple tasks.

**Architecture:** 5-layer stack: LLM → Ontology Layer → Tools/Action Types/Skills → Agent (DeepAgent) → User Exchange Interface (A2UI/WebSocket)

**Tech Stack:** Python 3.11+ | FastAPI | PostgreSQL 15+ (JSONB) | SQLAlchemy 2.0 | DeepAgent (LangChain-based) | LangGraph | A2UI/AG-UI | ECharts

---

## Global Constraints

- Python 3.11+ required
- All DB queries must include tenant_id for multi-tenant isolation
- Use SQLAlchemy 2.0 async ORM
- All timestamps in UTC
- JSONB for flexible schema storage (object_types, properties, links)
- DeepAgent handles agent execution harness

---

## File Structure

```
ontology_agent/
├── pyproject.toml                    # Project metadata + dependencies
├── src/
│   └── ontology_agent/
│       ├── __init__.py
│       ├── main.py                   # FastAPI app entry point
│       ├── config.py                 # Configuration (from env)
│       ├── db/
│       │   ├── __init__.py
│       │   ├── models.py             # SQLAlchemy models
│       │   └── session.py            # Async session factory
│       ├── ontology/
│       │   ├── __init__.py
│       │   ├── storage.py            # Ontology schema storage (JSONB)
│       │   ├── instance.py           # Instance data storage
│       │   └── types.py              # Pydantic types for API
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── base.py               # Tool abstract base class
│       │   ├── registry.py           # Tool registry (singleton)
│       │   ├── ontology_read.py      # Tool: read ontology schema
│       │   ├── ontology_write.py     # Tool: write ontology schema
│       │   ├── entity_search.py      # Tool: query entities
│       │   └── entity_write.py       # Tool: write entities
│       ├── agent/
│       │   ├── __init__.py
│       │   ├── harness.py             # DeepAgent harness setup
│       │   ├── messages.py           # AgentMessage dataclass
│       │   └── prompts.py             # System prompts for 4 agents
│       ├── skills/
│       │   ├── __init__.py
│       │   ├── loader.py             # Load .md skill files
│       │   └── examples/
│       │       └── product_query.md   # Example skill
│       └── api/
│           ├── __init__.py
│           ├── ws.py                  # WebSocket handler
│           ├── chat.py                # Chat REST endpoints
│           └── ontology.py           # Ontology CRUD endpoints
├── frontend/
│   ├── index.html                    # Simple chat UI
│   └── a2ui/                         # A2UI components (future)
├── skills/                           # Skill markdown files
│   ├── product_query.md
│   └── place_order.md
└── tests/
    ├── conftest.py                   # Pytest fixtures
    ├── test_tools.py
    ├── test_ontology.py
    └── test_agent.py
```

---

## Task 1: Project Scaffolding

**Files:**
- Create: `pyproject.toml`
- Create: `src/ontology_agent/__init__.py`
- Create: `src/ontology_agent/main.py`
- Create: `src/ontology_agent/config.py`

**Interfaces:**
- Produces: `create_app()` → FastAPI app instance

- [ ] **Step 1: Create pyproject.toml**

```toml
[project]
name = "ontology-agent"
version = "0.1.0"
description = "Knowledge-Graph-Augmented AI Agent Platform"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.30.0",
    "sqlalchemy[asyncio]>=2.0.0",
    "asyncpg>=0.30.0",
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
    "python-dotenv>=1.0.0",
    "httpx>=0.27.0",
    "deep>=0.1.0",
    "langgraph>=0.0.20",
    "apscheduler>=3.10.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "httpx>=0.27.0",
    "ruff>=0.6.0",
]
```

- [ ] **Step 2: Create config.py**

```python
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
```

- [ ] **Step 3: Create main.py**

```python
from fastapi import FastAPI
from ontology_agent.config import get_settings

settings = get_settings()

def create_app() -> FastAPI:
    app = FastAPI(title="OntologyAgent", version="0.1.0")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()
```

- [ ] **Step 4: Run app to verify**

Run: `cd /Users/xiewenlong/Documents/code/OntologyAgent && uvicorn ontology_agent.main:app --reload`
Expected: Server starts on port 8000

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml src/ontology_agent/
git commit -m "feat: project scaffolding with FastAPI app"
```

---

## Task 2: Database Models

**Files:**
- Create: `src/ontology_agent/db/__init__.py`
- Create: `src/ontology_agent/db/models.py`
- Create: `src/ontology_agent/db/session.py`

**Interfaces:**
- Produces: `get_async_session()` → AsyncSession, `Base` → DeclarativeBase

- [ ] **Step 1: Create session.py**

```python
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
```

- [ ] **Step 2: Create models.py**

```python
from sqlalchemy import String, Text, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
import uuid

class Base(DeclarativeBase):
    pass

def generate_uuid() -> str:
    return str(uuid.uuid4())

class Ontology(Base):
    __tablename__ = "ontologies"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    tenant_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    object_types: Mapped[dict] = mapped_column(JSON, default=dict)  # JSONB
    properties: Mapped[dict] = mapped_column(JSON, default=dict)
    link_types: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Object(Base):
    __tablename__ = "objects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    tenant_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    ontology_id: Mapped[str] = mapped_column(String(36), ForeignKey("ontologies.id"), nullable=False)
    object_type: Mapped[str] = mapped_column(String(255), nullable=False)
    api_name: Mapped[str] = mapped_column(String(255), nullable=False)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    properties: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ObjectLink(Base):
    __tablename__ = "object_links"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    tenant_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    source_object_id: Mapped[str] = mapped_column(String(36), ForeignKey("objects.id"), nullable=False)
    target_object_id: Mapped[str] = mapped_column(String(36), ForeignKey("objects.id"), nullable=False)
    link_type: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
```

- [ ] **Step 3: Create init.py**

```python
from ontology_agent.db.models import Base, Ontology, Object, ObjectLink
from ontology_agent.db.session import get_async_session, AsyncSessionLocal, engine

__all__ = ["Base", "Ontology", "Object", "ObjectLink", "get_async_session", "AsyncSessionLocal", "engine"]
```

- [ ] **Step 4: Write test for models**

```python
# tests/test_db.py
import pytest
from ontology_agent.db.models import Ontology, Object

def test_ontology_creation():
    ont = Ontology(
        tenant_id="test-tenant",
        name="Retail",
        description="Retail ontology",
    )
    assert ont.id is not None
    assert ont.tenant_id == "test-tenant"
    assert ont.version == 1
```

- [ ] **Step 5: Commit**

```bash
git add src/ontology_agent/db/ tests/
git commit -m "feat: add database models for Ontology/Object/ObjectLink"
```

---

## Task 3: Ontology Storage Layer

**Files:**
- Create: `src/ontology_agent/ontology/__init__.py`
- Create: `src/ontology_agent/ontology/storage.py`
- Create: `src/ontology_agent/ontology/instance.py`
- Create: `src/ontology_agent/ontology/types.py`

**Interfaces:**
- Consumes: `get_async_session()`
- Produces: `OntologyStorage.create_ontology()`, `OntologyStorage.get_ontology()`, `InstanceStorage.search_objects()`

- [ ] **Step 1: Create types.py**

```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ObjectTypeDefinition(BaseModel):
    id: str
    api_name: str
    display_name: str
    description: Optional[str] = None
    status: str = "active"
    properties: list[str] = []
    relations: list[str] = []

class PropertyDefinition(BaseModel):
    id: str
    api_name: str
    display_name: str
    type: str  # string, int, float, bool, datetime
    description: Optional[str] = None
    status: str = "active"

class LinkTypeDefinition(BaseModel):
    id: str
    api_name: str
    display_name: str
    source_object_type: str
    target_object_type: str
    cardinality: str  # one-to-one, one-to-many, many-to-many
    description: Optional[str] = None
    status: str = "active"

class ObjectCreate(BaseModel):
    object_type: str
    api_name: str
    display_name: str
    properties: dict = {}

class ObjectResponse(ObjectCreate):
    id: str
    tenant_id: str
    created_at: datetime
    updated_at: datetime
```

- [ ] **Step 2: Create storage.py**

```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.models import Ontology
from ontology_agent.ontology.types import ObjectTypeDefinition, PropertyDefinition, LinkTypeDefinition

class OntologyStorage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_ontology(
        self,
        tenant_id: str,
        name: str,
        description: str | None = None,
    ) -> Ontology:
        ontology = Ontology(
            tenant_id=tenant_id,
            name=name,
            description=description,
            object_types={},
            properties={},
            link_types={},
        )
        self.session.add(ontology)
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology

    async def get_ontology(self, ontology_id: str, tenant_id: str) -> Ontology | None:
        result = await self.session.execute(
            select(Ontology).where(
                Ontology.id == ontology_id,
                Ontology.tenant_id == tenant_id,
            )
        )
        return result.scalar_one_or_none()

    async def update_object_types(
        self, ontology_id: str, tenant_id: str, object_types: list[ObjectTypeDefinition]
    ) -> Ontology | None:
        ontology = await self.get_ontology(ontology_id, tenant_id)
        if not ontology:
            return None
        ontology.object_types = {ot.id: ot.model_dump() for ot in object_types}
        await self.session.commit()
        await self.session.refresh(ontology)
        return ontology
```

- [ ] **Step 3: Create instance.py**

```python
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.models import Object, ObjectLink
from ontology_agent.ontology.types import ObjectCreate, ObjectResponse

class InstanceStorage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_object(self, tenant_id: str, ontology_id: str, obj: ObjectCreate) -> Object:
        object_ = Object(
            tenant_id=tenant_id,
            ontology_id=ontology_id,
            object_type=obj.object_type,
            api_name=obj.api_name,
            display_name=obj.display_name,
            properties=obj.properties,
        )
        self.session.add(object_)
        await self.session.commit()
        await self.session.refresh(object_)
        return object_

    async def search_objects(
        self,
        tenant_id: str,
        ontology_id: str,
        object_type: str | None = None,
        filters: dict | None = None,
        limit: int = 100,
    ) -> list[Object]:
        query = select(Object).where(
            Object.tenant_id == tenant_id,
            Object.ontology_id == ontology_id,
        )
        if object_type:
            query = query.where(Object.object_type == object_type)
        query = query.limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_object(self, object_id: str, tenant_id: str, properties: dict) -> Object | None:
        result = await self.session.execute(
            select(Object).where(Object.id == object_id, Object.tenant_id == tenant_id)
        )
        object_ = result.scalar_one_or_none()
        if not object_:
            return None
        object_.properties = {**object_.properties, **properties}
        await self.session.commit()
        await self.session.refresh(object_)
        return object_
```

- [ ] **Step 4: Write tests for ontology storage**

```python
# tests/test_ontology.py
import pytest
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.db.session import AsyncSessionLocal

@pytest.mark.asyncio
async def test_create_and_get_ontology():
    async with AsyncSessionLocal() as session:
        storage = OntologyStorage(session)
        ont = await storage.create_ontology(
            tenant_id="test-tenant",
            name="Test Ontology",
            description="A test ontology",
        )
        assert ont.id is not None
        assert ont.name == "Test Ontology"

        retrieved = await storage.get_ontology(ont.id, "test-tenant")
        assert retrieved is not None
        assert retrieved.name == "Test Ontology"
```

- [ ] **Step 5: Commit**

```bash
git add src/ontology_agent/ontology/ tests/
git commit -m "feat: add ontology storage layer (schema CRUD)"
```

---

## Task 4: Tool Base Classes and Registry

**Files:**
- Create: `src/ontology_agent/tools/__init__.py`
- Create: `src/ontology_agent/tools/base.py`
- Create: `src/ontology_agent/tools/registry.py`

**Interfaces:**
- Produces: `Tool` abstract class, `ToolRegistry` singleton, `ToolResult` dataclass

- [ ] **Step 1: Create base.py**

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class ToolResult:
    success: bool
    data: dict | None = None
    error: str | None = None
    execution_time_ms: int = 0

class Tool(ABC):
    name: str
    description: str
    params_schema: dict
    is_admin_only: bool = False

    @abstractmethod
    async def execute(self, params: dict, context: dict) -> ToolResult:
        """Execute tool, return result or raise ToolExecutionError"""
        pass

class ToolExecutionError(Exception):
    pass
```

- [ ] **Step 2: Create registry.py**

```python
from ontology_agent.tools.base import Tool, ToolResult

class ToolRegistry:
    _instance = None

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    @classmethod
    def get_instance(cls) -> "ToolRegistry":
        if cls._instance is None:
            cls._instance = ToolRegistry()
        return cls._instance

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool {tool.name} already registered")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def list_tools(self) -> list[Tool]:
        return list(self._tools.values())

    async def execute(self, name: str, params: dict, context: dict) -> ToolResult:
        tool = self.get(name)
        if not tool:
            return ToolResult(success=False, error=f"Tool {name} not found")
        try:
            return await tool.execute(params, context)
        except Exception as e:
            return ToolResult(success=False, error=str(e))
```

- [ ] **Step 3: Create init.py**

```python
from ontology_agent.tools.base import Tool, ToolResult, ToolExecutionError
from ontology_agent.tools.registry import ToolRegistry

__all__ = ["Tool", "ToolResult", "ToolExecutionError", "ToolRegistry"]
```

- [ ] **Step 4: Commit**

```bash
git add src/ontology_agent/tools/
git commit -m "feat: add Tool base class and registry"
```

---

## Task 5: Ontology Read/Write Tools

**Files:**
- Create: `src/ontology_agent/tools/ontology_read.py`
- Create: `src/ontology_agent/tools/ontology_write.py`

**Interfaces:**
- Consumes: `OntologyStorage`, `InstanceStorage`
- Produces: `OntologyReadTool`, `OntologyWriteTool`

- [ ] **Step 1: Create ontology_read.py**

```python
from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.db.session import AsyncSessionLocal

class OntologyReadTool(Tool):
    name = "ontology_read"
    description = "Read ontology schema (Object Types, Properties, Link Types)"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string", "description": "Ontology ID"},
        },
        "required": ["ontology_id"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        import time
        start = time.time()

        tenant_id = context.get("tenant_id")
        ontology_id = params["ontology_id"]

        async with AsyncSessionLocal() as session:
            storage = OntologyStorage(session)
            ontology = await storage.get_ontology(ontology_id, tenant_id)

            if not ontology:
                return ToolResult(
                    success=False,
                    error="Ontology not found",
                    execution_time_ms=int((time.time() - start) * 1000),
                )

            return ToolResult(
                success=True,
                data={
                    "id": ontology.id,
                    "name": ontology.name,
                    "description": ontology.description,
                    "version": ontology.version,
                    "object_types": ontology.object_types,
                    "properties": ontology.properties,
                    "link_types": ontology.link_types,
                },
                execution_time_ms=int((time.time() - start) * 1000),
            )
```

- [ ] **Step 2: Create ontology_write.py**

```python
from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.types import ObjectTypeDefinition, PropertyDefinition
from ontology_agent.db.session import AsyncSessionLocal

class OntologyWriteTool(Tool):
    name = "ontology_write"
    description = "Create or update ontology schema"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string", "description": "Ontology ID (empty for create)"},
            "action": {"type": "string", "enum": ["create_ontology", "add_object_type", "add_property"]},
            "data": {"type": "object"},
        },
        "required": ["action", "data"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        import time
        start = time.time()

        tenant_id = context.get("tenant_id")
        action = params["action"]
        data = params["data"]

        async with AsyncSessionLocal() as session:
            storage = OntologyStorage(session)

            if action == "create_ontology":
                ontology = await storage.create_ontology(
                    tenant_id=tenant_id,
                    name=data.get("name", "Untitled"),
                    description=data.get("description"),
                )
                return ToolResult(
                    success=True,
                    data={"ontology_id": ontology.id},
                    execution_time_ms=int((time.time() - start) * 1000),
                )

            elif action == "add_object_type":
                ontology_id = params.get("ontology_id")
                if not ontology_id:
                    return ToolResult(success=False, error="ontology_id required", execution_time_ms=int((time.time() - start) * 1000))

                object_type = ObjectTypeDefinition(**data)
                updated = await storage.update_object_types(ontology_id, tenant_id, [object_type])
                if not updated:
                    return ToolResult(success=False, error="Ontology not found", execution_time_ms=int((time.time() - start) * 1000))

                return ToolResult(success=True, data={"updated": True}, execution_time_ms=int((time.time() - start) * 1000))

            return ToolResult(success=False, error=f"Unknown action: {action}", execution_time_ms=int((time.time() - start) * 1000))
```

- [ ] **Step 3: Register tools in registry init**

```python
# Add to src/ontology_agent/tools/__init__.py
from ontology_agent.tools.ontology_read import OntologyReadTool
from ontology_agent.tools.ontology_write import OntologyWriteTool

def register_all_tools():
    registry = ToolRegistry.get_instance()
    registry.register(OntologyReadTool())
    registry.register(OntologyWriteTool())
```

- [ ] **Step 4: Commit**

```bash
git add src/ontology_agent/tools/
git commit -m "feat: add ontology_read and ontology_write tools"
```

---

## Task 6: Entity Search/Write Tools

**Files:**
- Create: `src/ontology_agent/tools/entity_search.py`
- Create: `src/ontology_agent/tools/entity_write.py`

**Interfaces:**
- Consumes: `InstanceStorage`
- Produces: `EntitySearchTool`, `EntityWriteTool`

- [ ] **Step 1: Create entity_search.py**

```python
from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.db.session import AsyncSessionLocal

class EntitySearchTool(Tool):
    name = "entity_search"
    description = "Query entity data (products, customers, etc.)"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string", "description": "Ontology ID"},
            "object_type": {"type": "string", "description": "Object type to search"},
            "filters": {"type": "object", "description": "Property filters"},
            "limit": {"type": "integer", "default": 100},
        },
        "required": ["ontology_id"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        import time
        start = time.time()

        tenant_id = context.get("tenant_id")
        ontology_id = params["ontology_id"]
        object_type = params.get("object_type")
        filters = params.get("filters", {})
        limit = params.get("limit", 100)

        async with AsyncSessionLocal() as session:
            storage = InstanceStorage(session)
            objects = await storage.search_objects(
                tenant_id=tenant_id,
                ontology_id=ontology_id,
                object_type=object_type,
                filters=filters,
                limit=limit,
            )

            return ToolResult(
                success=True,
                data={
                    "objects": [
                        {
                            "id": o.id,
                            "object_type": o.object_type,
                            "api_name": o.api_name,
                            "display_name": o.display_name,
                            "properties": o.properties,
                        }
                        for o in objects
                    ],
                    "count": len(objects),
                },
                execution_time_ms=int((time.time() - start) * 1000),
            )
```

- [ ] **Step 2: Create entity_write.py**

```python
from ontology_agent.tools.base import Tool, ToolResult
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.ontology.types import ObjectCreate
from ontology_agent.db.session import AsyncSessionLocal

class EntityWriteTool(Tool):
    name = "entity_write"
    description = "Write or update entity data"
    params_schema = {
        "type": "object",
        "properties": {
            "ontology_id": {"type": "string"},
            "action": {"type": "string", "enum": ["create", "update"]},
            "object_id": {"type": "string", "description": "Required for update"},
            "object_type": {"type": "string"},
            "api_name": {"type": "string"},
            "display_name": {"type": "string"},
            "properties": {"type": "object"},
        },
        "required": ["ontology_id", "action"],
    }

    async def execute(self, params: dict, context: dict) -> ToolResult:
        import time
        start = time.time()

        tenant_id = context.get("tenant_id")
        ontology_id = params["ontology_id"]
        action = params["action"]

        async with AsyncSessionLocal() as session:
            storage = InstanceStorage(session)

            if action == "create":
                obj_data = ObjectCreate(
                    object_type=params["object_type"],
                    api_name=params["api_name"],
                    display_name=params["display_name"],
                    properties=params.get("properties", {}),
                )
                obj = await storage.create_object(tenant_id, ontology_id, obj_data)
                return ToolResult(
                    success=True,
                    data={"object_id": obj.id},
                    execution_time_ms=int((time.time() - start) * 1000),
                )

            elif action == "update":
                object_id = params.get("object_id")
                if not object_id:
                    return ToolResult(success=False, error="object_id required for update", execution_time_ms=int((time.time() - start) * 1000))
                updated = await storage.update_object(object_id, tenant_id, params.get("properties", {}))
                if not updated:
                    return ToolResult(success=False, error="Object not found", execution_time_ms=int((time.time() - start) * 1000))
                return ToolResult(success=True, data={"updated": True}, execution_time_ms=int((time.time() - start) * 1000))

            return ToolResult(success=False, error=f"Unknown action: {action}", execution_time_ms=int((time.time() - start) * 1000))
```

- [ ] **Step 3: Commit**

```bash
git add src/ontology_agent/tools/
git commit -m "feat: add entity_search and entity_write tools"
```

---

## Task 7: DeepAgent Harness Integration

**Files:**
- Create: `src/ontology_agent/agent/__init__.py`
- Create: `src/ontology_agent/agent/harness.py`
- Create: `src/ontology_agent/agent/messages.py`
- Create: `src/ontology_agent/agent/prompts.py`

**Interfaces:**
- Consumes: `ToolRegistry`, LLM API
- Produces: `AgentHarness` class with 4 sub-agents (Planner, Tool, Reasoner, Reporter)

- [ ] **Step 1: Create messages.py**

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

@dataclass
class AgentMessage:
    msg_id: str
    from_agent: str
    to_agent: str  # "*"" for broadcast
    msg_type: Literal["task", "result", "error", "heartbeat"]
    content: dict
    reply_to: str | None = None
    created_at: datetime = None
    ttl: int = 30
    retries: int = 0

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow()
```

- [ ] **Step 2: Create prompts.py**

```python
PLANNER_PROMPT = """You are a task planning Agent. Your role is to decompose user requests into execution steps.

Current task: {task_description}
Current context: {context}

Please output a step-by-step execution plan in JSON format:
{{"steps": [{{"step_id": 1, "action": "action_name", "params": {{}}}}]}}
"""

TOOL_AGENT_PROMPT = """You are a tool-calling Agent. Your role is to execute specific operations based on the plan.

Current step: {step_description}
Available tools: {available_tools}

Select the appropriate tool and execute.
"""

REASONER_PROMPT = """You are a reasoning and analysis Agent. Your role is to analyze data and provide insights.

Current task: {task_description}
Data: {data}

Please provide analysis and conclusions.
"""

REPORTER_PROMPT = """You are a report generation Agent. Your role is to transform results into user-readable natural language responses.

Result data: {data}
Response format: {format}

Generate a natural language response.
"""
```

- [ ] **Step 3: Create harness.py**

```python
from typing import Any
from ontology_agent.agent.messages import AgentMessage
from ontology_agent.agent.prompts import PLANNER_PROMPT, TOOL_AGENT_PROMPT, REASONER_PROMPT, REPORTER_PROMPT
from ontology_agent.tools.registry import ToolRegistry

class AgentHarness:
    def __init__(self):
        self.registry = ToolRegistry.get_instance()
        self.tools = self.registry.list_tools()
        self.tool_schemas = [
            {"name": t.name, "description": t.description, "parameters": t.params_schema}
            for t in self.tools
        ]

    def get_system_prompts(self) -> dict[str, str]:
        return {
            "planner": PLANNER_PROMPT,
            "tool_agent": TOOL_AGENT_PROMPT,
            "reasoner": REASONER_PROMPT,
            "reporter": REPORTER_PROMPT,
        }

    def get_available_tools(self) -> list[dict]:
        return self.tool_schemas

    async def process_message(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        # Simple routing: based on msg_type and content
        if message.to_agent == "planner":
            return await self._handle_planner(message, llm_complete_fn)
        elif message.to_agent == "tool":
            return await self._handle_tool(message, llm_complete_fn)
        elif message.to_agent == "reasoner":
            return await self._handle_reasoner(message, llm_complete_fn)
        elif message.to_agent == "reporter":
            return await self._handle_reporter(message, llm_complete_fn)
        else:
            return AgentMessage(
                msg_id=message.msg_id + "_error",
                from_agent="harness",
                to_agent=message.from_agent,
                msg_type="error",
                content={"error": f"Unknown agent: {message.to_agent}"},
                reply_to=message.msg_id,
            )

    async def _handle_planner(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        # Use LLM to decompose task
        response = await llm_complete_fn(
            system_prompt=PLANNER_PROMPT,
            messages=[{"role": "user", "content": message.content.get("task", "")}],
        )
        return AgentMessage(
            msg_id=f"{message.msg_id}_plan",
            from_agent="planner",
            to_agent=message.from_agent,
            msg_type="result",
            content={"plan": response},
            reply_to=message.msg_id,
        )

    async def _handle_tool(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        action = message.content.get("action")
        params = message.content.get("params", {})
        result = await self.registry.execute(action, params, message.content.get("context", {}))
        return AgentMessage(
            msg_id=f"{message.msg_id}_result",
            from_agent="tool",
            to_agent=message.from_agent,
            msg_type="result",
            content={"result": result.__dict__},
            reply_to=message.msg_id,
        )

    async def _handle_reasoner(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        response = await llm_complete_fn(
            system_prompt=REASONER_PROMPT,
            messages=[{"role": "user", "content": str(message.content)}],
        )
        return AgentMessage(
            msg_id=f"{message.msg_id}_analysis",
            from_agent="reasoner",
            to_agent=message.from_agent,
            msg_type="result",
            content={"analysis": response},
            reply_to=message.msg_id,
        )

    async def _handle_reporter(self, message: AgentMessage, llm_complete_fn) -> AgentMessage:
        response = await llm_complete_fn(
            system_prompt=REPORTER_PROMPT,
            messages=[{"role": "user", "content": str(message.content)}],
        )
        return AgentMessage(
            msg_id=f"{message.msg_id}_report",
            from_agent="reporter",
            to_agent=message.from_agent,
            msg_type="result",
            content={"report": response},
            reply_to=message.msg_id,
        )
```

- [ ] **Step 4: Commit**

```bash
git add src/ontology_agent/agent/
git commit -m "feat: add DeepAgent harness with 4 sub-agents"
```

---

## Task 8: FastAPI API Endpoints

**Files:**
- Create: `src/ontology_agent/api/__init__.py`
- Create: `src/ontology_agent/api/chat.py`
- Create: `src/ontology_agent/api/ontology.py`
- Modify: `src/ontology_agent/main.py`

**Interfaces:**
- Consumes: `OntologyStorage`, `InstanceStorage`, `AgentHarness`
- Produces: REST endpoints, WebSocket handler

- [ ] **Step 1: Create chat.py**

```python
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ontology_agent.agent.harness import AgentHarness
from ontology_agent.agent.messages import AgentMessage
import uuid
import json

router = APIRouter(prefix="/api/v1", tags=["chat"])
harness = AgentHarness()

@router.post("/chat")
async def chat(message: dict):
    msg_id = str(uuid.uuid4())
    agent_msg = AgentMessage(
        msg_id=msg_id,
        from_agent="user",
        to_agent="planner",
        msg_type="task",
        content=message,
    )
    result = await harness.process_message(agent_msg, llm_complete_fn=lambda **k: "Mock LLM response")
    return {"msg_id": result.msg_id, "content": result.content}

@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            msg_id = str(uuid.uuid4())
            agent_msg = AgentMessage(
                msg_id=msg_id,
                from_agent="user",
                to_agent="planner",
                msg_type="task",
                content=msg,
            )
            result = await harness.process_message(agent_msg, llm_complete_fn=lambda **k: "Mock LLM")
            await websocket.send_json({"msg_id": result.msg_id, "content": result.content})
    except WebSocketDisconnect:
        pass
```

- [ ] **Step 2: Create ontology.py**

```python
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ontology_agent.db.session import get_async_session
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.instance import InstanceStorage

router = APIRouter(prefix="/api/v1/ontology", tags=["ontology"])

@router.post("/ontologies")
async def create_ontology(
    tenant_id: str,
    name: str,
    description: str | None = None,
    session: AsyncSession = Depends(get_async_session),
):
    storage = OntologyStorage(session)
    ontology = await storage.create_ontology(tenant_id, name, description)
    return {"id": ontology.id, "name": ontology.name}

@router.get("/ontologies/{ontology_id}")
async def get_ontology(
    ontology_id: str,
    tenant_id: str,
    session: AsyncSession = Depends(get_async_session),
):
    storage = OntologyStorage(session)
    ontology = await storage.get_ontology(ontology_id, tenant_id)
    if not ontology:
        return {"error": "Not found"}
    return {
        "id": ontology.id,
        "name": ontology.name,
        "object_types": ontology.object_types,
        "properties": ontology.properties,
    }

@router.post("/objects/search")
async def search_objects(
    tenant_id: str,
    ontology_id: str,
    object_type: str | None = None,
    session: AsyncSession = Depends(get_async_session),
):
    storage = InstanceStorage(session)
    objects = await storage.search_objects(tenant_id, ontology_id, object_type)
    return {"objects": [{"id": o.id, "display_name": o.display_name} for o in objects]}
```

- [ ] **Step 3: Update main.py to include routers**

```python
from fastapi import FastAPI
from ontology_agent.api.chat import router as chat_router
from ontology_agent.api.ontology import router as ontology_router

def create_app() -> FastAPI:
    app = FastAPI(title="OntologyAgent", version="0.1.0")
    app.include_router(chat_router)
    app.include_router(ontology_router)

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()
```

- [ ] **Step 4: Commit**

```bash
git add src/ontology_agent/api/ src/ontology_agent/main.py
git commit -m "feat: add FastAPI endpoints for chat and ontology CRUD"
```

---

## Task 9: Skill Loader and Example Skills

**Files:**
- Create: `src/ontology_agent/skills/__init__.py`
- Create: `src/ontology_agent/skills/loader.py`
- Create: `skills/product_query.md`
- Create: `skills/place_order.md`

**Interfaces:**
- Consumes: Skill markdown files
- Produces: `SkillLoader.load_skill()`, list of loaded skills

- [ ] **Step 1: Create loader.py**

```python
import re
import yaml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Skill:
    name: str
    description: str
    skill_type: str  # workflow, query, analysis
    triggers: list[str]
    content: str  # markdown body

class SkillLoader:
    def __init__(self, skills_dir: str = "skills"):
        self.skills_dir = Path(skills_dir)

    def load_skill(self, filename: str) -> Skill | None:
        filepath = self.skills_dir / filename
        if not filepath.exists():
            return None

        content = filepath.read_text()
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        frontmatter = yaml.safe_load(parts[1])
        markdown_body = parts[2].strip()

        return Skill(
            name=frontmatter.get("name", ""),
            description=frontmatter.get("description", ""),
            skill_type=frontmatter.get("type", "workflow"),
            triggers=frontmatter.get("triggers", []),
            content=markdown_body,
        )

    def load_all(self) -> list[Skill]:
        skills = []
        if not self.skills_dir.exists():
            return skills
        for filepath in self.skills_dir.glob("*.md"):
            skill = self.load_skill(filepath.name)
            if skill:
                skills.append(skill)
        return skills

    def get_system_prompt_injection(self) -> str:
        skills = self.load_all()
        injections = []
        for skill in skills:
            injections.append(f"## Skill: {skill.name}\n\n{skill.content}")
        return "\n\n".join(injections)
```

- [ ] **Step 2: Create product_query.md**

```markdown
---
name: product_query
description: Query product information from the ontology
type: query
triggers:
  - intent: "查询商品"
  - intent: "搜索产品"
  - intent: "查找商品信息"
---

# Product Query Skill

When the user wants to query product information, follow these steps:

1. Use `entity_search` tool with `object_type: "product"`
2. Apply any filters provided by the user (category, price range, etc.)
3. Return the results in a readable format with key product details.

## Parameters
- `object_type`: Always set to "product"
- `filters`: Any property filters (category, brand, price_min, price_max)
- `limit`: Maximum number of results (default 20)
```

- [ ] **Step 3: Create place_order.md**

```markdown
---
name: place_order
description: Complete customer order workflow
type: workflow
triggers:
  - intent: "我想下单"
  - intent: "创建订单"
---

# Place Order Workflow

When the user expresses intent to place an order, execute the following steps:

## Step 1: Validate Payment
Call `validate_payment` action with the provided payment information.
If validation fails, abort the workflow and return an error.

## Step 2: Check Inventory
Call `check_inventory` action with product_id and quantity.
If inventory is insufficient, abort and notify user.

## Step 3: Create Order
Call `create_order` action with customer_id, product_id, quantity.
Save the returned order_id.

## Step 4: Send Notification
Call `send_notification` action with order details.
```

- [ ] **Step 4: Commit**

```bash
git add src/ontology_agent/skills/ skills/
git commit -m "feat: add skill loader and example skills"
```

---

## Task 10: Basic Chat UI

**Files:**
- Create: `frontend/index.html`

**Interfaces:**
- Consumes: WebSocket endpoint `/api/v1/ws/{session_id}`
- Produces: Simple chat interface

- [ ] **Step 1: Create index.html**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OntologyAgent</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        #chat { border: 1px solid #ccc; height: 400px; overflow-y: auto; padding: 10px; margin-bottom: 10px; }
        #input { width: calc(100% - 80px); padding: 10px; }
        #send { width: 70px; padding: 10px; }
        .message { margin: 10px 0; }
        .user { color: blue; }
        .agent { color: green; }
    </style>
</head>
<body>
    <h1>OntologyAgent</h1>
    <div id="chat"></div>
    <input type="text" id="input" placeholder="输入消息..." onkeypress="if(event.key==='Enter')send()">
    <button id="send" onclick="send()">发送</button>

    <script>
        const ws = new WebSocket(`ws://localhost:8000/api/v1/ws/${Date.now()}`);
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            addMessage('agent', data.content?.report || data.content || JSON.stringify(data));
        };
        ws.onerror = () => addMessage('system', 'WebSocket error');
        ws.onclose = () => addMessage('system', 'Disconnected');

        function send() {
            const input = document.getElementById('input');
            const text = input.value;
            if (!text) return;
            addMessage('user', text);
            ws.send(JSON.stringify({ message: text }));
            input.value = '';
        }

        function addMessage(role, text) {
            const chat = document.getElementById('chat');
            const div = document.createElement('div');
            div.className = role;
            div.textContent = `${role}: ${text}`;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add frontend/index.html
git commit -m "feat: add basic chat UI"
```

---

## Task 11: Integration Test

**Files:**
- Create: `tests/test_integration.py`
- Modify: `tests/conftest.py`

**Interfaces:**
- Consumes: All implemented components
- Produces: End-to-end test

- [ ] **Step 1: Create conftest.py**

```python
import pytest
import asyncio

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
```

- [ ] **Step 2: Create integration test**

```python
# tests/test_integration.py
import pytest
from ontology_agent.db.session import AsyncSessionLocal, engine
from ontology_agent.db.models import Base
from ontology_agent.ontology.storage import OntologyStorage
from ontology_agent.ontology.instance import InstanceStorage
from ontology_agent.ontology.types import ObjectCreate

@pytest.fixture(autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_full_ontology_flow():
    async with AsyncSessionLocal() as session:
        # 1. Create ontology
        storage = OntologyStorage(session)
        ont = await storage.create_ontology(
            tenant_id="test-tenant",
            name="Retail",
            description="Retail ontology",
        )
        assert ont.id is not None

        # 2. Create product object
        instance_storage = InstanceStorage(session)
        product = await instance_storage.create_object(
            tenant_id="test-tenant",
            ontology_id=ont.id,
            obj=ObjectCreate(
                object_type="product",
                api_name="iphone_15",
                display_name="iPhone 15",
                properties={"price": 6999, "category": "electronics"},
            ),
        )
        assert product.id is not None
        assert product.properties["price"] == 6999

        # 3. Search products
        results = await instance_storage.search_objects(
            tenant_id="test-tenant",
            ontology_id=ont.id,
            object_type="product",
        )
        assert len(results) == 1
        assert results[0].display_name == "iPhone 15"
```

- [ ] **Step 3: Run integration test**

Run: `pytest tests/test_integration.py -v`
Expected: PASS (or FAIL if DB not running)

- [ ] **Step 4: Commit**

```bash
git add tests/test_integration.py tests/conftest.py
git commit -m "test: add integration test for full ontology flow"
```

---

## Spec Coverage Checklist

| Spec Section | Task(s) |
|--------------|---------|
| Layer 1: LLM | Task 7 (prompts) |
| Layer 2: Ontology Layer | Task 2, Task 3 |
| Layer 3: Tools | Task 4, Task 5, Task 6 |
| Layer 3: Action Types | Task 5, Task 6 |
| Layer 3: Skills | Task 9 |
| Layer 4: Agent | Task 7 |
| Layer 5: UI | Task 8, Task 10 |
| Multi-tenant isolation | All tasks (tenant_id in context) |
| WebSocket/AG-UI | Task 8 |
| A2UI components | Task 10 (future) |

---

## Plan Complete

**Two execution options:**

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
