# OntologyAgent

Knowledge-Graph-Augmented AI Agent Platform

## Overview

OntologyAgent is a FastAPI-based platform that combines large language models with knowledge graph capabilities. It uses a multi-agent architecture where specialized agents collaborate to process complex tasks.

## Architecture

```
┌─────────────┐
│     LLM     │
└──────┬──────┘
       │
┌──────▼──────┐
│  Ontology   │
└──────┬──────┘
       │
┌──────▼──────┐
│    Tools    │
│ Action Types│
│   Skills    │
└──────┬──────┘
       │
┌──────▼──────┐
│    Agent    │
└──────┬──────┘
       │
┌──────▼──────┐
│User Exchange│
└─────────────┘
```

## Tech Stack

- **FastAPI** - Async web framework
- **PostgreSQL** - Primary database with JSONB for flexible schema
- **WebSocket** - Real-time chat communication
- **DeepAgent** - Multi-agent harness (Planner, Tool, Reasoner, Reporter)

## Quick Start

```bash
# Install dependencies
pip install -e .

# Start server
python -m uvicorn src.ontology_agent.main:app --reload

# Access UI
open http://localhost:8000/
```

## API

### REST Chat
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello", "tenant_id": "test-tenant"}'
```

### WebSocket Chat
```
ws://localhost:8000/api/v1/ws/{session_id}?tenant_id={tenant_id}
```

## Features

- Multi-tenant knowledge graph storage
- Skill-based tool system (markdown + YAML frontmatter)
- Real-time WebSocket communication
- Async/await throughout
