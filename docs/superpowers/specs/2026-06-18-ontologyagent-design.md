# OntologyAgent Design Specification

## Project Overview

**Project Name:** OntologyAgent
**Type:** Knowledge-Graph-Augmented AI Agent Platform (SaaS, Multi-tenant)
**MVP Goal:** Build a running ontology-aware agent that can load ontologies, converse with users, and invoke tools to complete simple tasks.
**Target Industry:** Retail (first vertical落地场景), but designed as a general-purpose platform.

---

## Architecture

### Five-Layer Stack

```
┌─────────────────────────────────────────────────────────┐
│  Layer 5: User Exchange Interface                       │
│          Conversational UI │ Task Trigger │ Scheduled Jobs │
├─────────────────────────────────────────────────────────┤
│  Layer 4: Agent Layer                                  │
│          Multi-Agent Dynamic Collaboration             │
│          (Point-to-Point Message Passing)              │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Tools → Action Types → Skills                │
│  ┌─────────────────────────────────────────────────┐   │
│  │ Tools: Low-level atoms (http_call, db_query)    │   │
│  │ Action Types: Business atoms (create_order)      │   │
│  │ Skills: Workflow orchestration (place_order)      │   │
│  └─────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Ontology Layer                               │
│          Semantic Data + Instance Data                 │
│          (Mesh-Composable + Dynamic Loading)           │
├─────────────────────────────────────────────────────────┤
│  Layer 1: LLM                                         │
│          GPT-4o / Claude (foundation model)           │
└─────────────────────────────────────────────────────────┘
```

---

## Layer 1: LLM

- Use **MiniMax / DeepSeek / Qwen** as the foundation model (domestic Chinese models).
- No specific fine-tuning in MVP; use prompt engineering to route requests to appropriate agents.

---

## Layer 2: Ontology Layer

### Alignment with Palantir Foundry

The Ontology Layer aligns with Palantir Foundry's methodology:

| Palantir Term | Our Term | Description |
|---------------|----------|-------------|
| Object Type | **Concept** | Schema definition (type) |
| Object | **Entity** | Single instance |
| Object Set | **Entity Set** | Collection of objects |
| Property | **Property** | Attributes of Object Type |
| Link Type | **Relation** | Relationships between objects |
| Interface | **Interface** | Abstract type for polymorphism |
| Action Type | **Action Type** | Atomic transaction that modifies data |
| Function | **Function** | Server-side logic (Query / Ontology Edit) |
| — | **Skill** | Workflow orchestration combining Action Types (new in this spec) |
| Interface | **Interface** | Abstract type for polymorphism |
| Action Type | **Skill** | Transactional operations |
| Function | **Skill** | Server-side business logic |

### Palantir 4 Design Principles

| Principle | Description |
|-----------|-------------|
| **Domain-Driven Design** | Ontology models the real world, not source data systems |
| **DRY (Rule of Three)** | Same semantics appear 3 times → refactor |
| **Open-Closed** | Core types stable; extend via Interface |
| **Composition over Inheritance** | Use Interface multi-inheritance, avoid deep class hierarchies |

### Anti-Patterns (Avoid)

| Anti-Pattern | Description | Correct Approach |
|--------------|-------------|-----------------|
| **Kitchen Sink** | One type with all fields mirroring source system | Split by domain entity |
| **Golden Hammer** | Use Pipeline for human decisions | Use Action (Skill) for human decisions |
| **System Mirror** | Object Type = source system table | Model real-world semantics |
| **Siloed Teams** | Design Ontology alone | Multi-team collaboration |
| **No Documentation** | No business meaning recorded | Record in metadata |

### Design Principles

- **Mesh-Composable:** Ontology instances cross-reference each other via relation types, forming a knowledge graph network.
- **Dynamic Loading:** Ontologies are loaded on demand, not all pre-loaded at startup.
- **Multi-tenant:** Each tenant has isolated ontologies and instance data.

### Semantic Data (Schema)

**Stored in PostgreSQL with JSONB columns.**

| Field | Description |
|-------|-------------|
| `id` | UUID |
| `tenant_id` | UUID (multi-tenant isolation) |
| `name` | Ontology name |
| `description` | Text |
| `version` | Integer |
| `concepts` | JSONB — list of concept definitions |
| `properties` | JSONB — property definitions |
| `relations` | JSONB — relation type definitions |

**Metadata (per resource):**

| Field | Description |
|-------|-------------|
| `status` | `active` / `experimental` / `deprecated` |
| `api_name` | Programming reference name |
| `display_name` | UI display name |
| `visibility` | `prominent` / `normal` / `hidden` |
| `description` | Business meaning |

**Concept structure (JSONB):**
```json
{
  "id": "product",
  "api_name": "product",
  "display_name": "Product",
  "description": "Retail product entity",
  "status": "active",
  "properties": ["name", "sku", "price", "category"],
  "relations": ["sold_by", "belongs_to_category"]
}
```

**Property structure (JSONB):**
```json
{
  "id": "price",
  "api_name": "price",
  "display_name": "Price",
  "type": "float",
  "description": "Unit price",
  "status": "active"
}
```

**Relation structure (JSONB):**
```json
{
  "id": "sold_by",
  "api_name": "sold_by",
  "display_name": "Sold By",
  "source_concept": "product",
  "target_concept": "supplier",
  "cardinality": "many-to-many",
  "description": "Supplier that sells this product"
}
```

**Cardinality types:**

| Type | Description |
|------|-------------|
| `one-to-one` | Each product has one supplier |
| `one-to-many` | One supplier supplies many products |
| `many-to-many` | Products can have multiple suppliers |
| `self-referential` | Employee ↔ Manager (same type) |

**Interface structure (JSONB):**
```json
{
  "id": "facility",
  "api_name": "facility",
  "display_name": "Facility",
  "description": "Physical facility",
  "properties": ["facility_name", "location"],
  "implemented_by": ["airport", "manufacturing_plant"]
}
```

### Instance Data (Knowledge Graph)

**Stored in PostgreSQL relational tables.**

- `entities`: id, tenant_id, ontology_id, concept_id, created_at, updated_at
- `entity_properties`: entity_id, property_id, value (JSONB)
- `entity_relations`: entity_id, relation_id, target_entity_id

**Entity structure (JSONB):**
```json
{
  "id": "entity_001",
  "api_name": "iphone_15",
  "display_name": "iPhone 15",
  "concept": "product",
  "properties": {
    "name": "iPhone 15",
    "sku": "PHONE-001",
    "price": 6999.00
  }
}
```

**MVP simplifications:**
- No dedicated graph database (PostgreSQL is sufficient for MVP queries)
- No schema versioning in MVP
- Graph traversal via SQL JOINs

---

## Layer 3: Tools, Action Types, Functions, and Skills

### Core Concepts (Based on AgentOS, Arcade Research)

Based on authoritative research (AgentOS, Arcade, SoK: Agentic Skills), this project uses the following layer structure:

| Layer | Concept | Nature | Example |
|-------|---------|--------|---------|
| **Bottom** | **Tool** | Executable function, Agent's "hands" | `http_call`, `db_query`, `file_read` |
| **Middle** | **Action Type** | Business atomic operation (Palantir-aligned) | `create_order`, `update_inventory` |
| **Top** | **Skill** | Workflow orchestration, combines multiple Action Types | `place_order_skill` |

**Tool vs Skill (AgentOS definition):**

> **"Skills tell the LLM *when* to do something. Tools are the things the LLM actually invokes."**

| | Tool | Skill |
|--|------|-------|
| **Nature** | Executable function | Prompt module / workflow definition |
| **What LLM sees** | Function name + description + parameter schema | Part of system prompt |
| **When it runs** | Called during LLM generation | Injected at agent construction |
| **Purpose** | Execute operations | Teach LLM when/how to use |

### Tool (Low-level Atomic Operations)

Tool is the low-level function that Agent actually calls, with well-defined inputs, outputs, and side effects.

#### Maintenance Atomics (Admin-only in production; MVP no enforcement)

| Tool | Description |
|------|-------------|
| `http_call` | Make HTTP requests to external systems |
| `db_query` | Execute PostgreSQL queries |
| `file_read` | Read files from filesystem |
| `file_write` | Write files to filesystem |

#### Business Operations (Agent-callable)

| Tool | Description |
|------|-------------|
| `ontology_read` | Read ontology schema (concepts, properties, relations) |
| `ontology_write` | Create/update ontology schema |
| `entity_search` | Query entity data (products, customers, etc.) |
| `entity_write` | Write/update entity data |
| `entity_set_query` | Query entity sets |
| `external_api_call` | Call external retail systems (ERP, WMS, POS) |

### Action Type (Business Atomic Operation, Palantir-aligned)

Action Type is the unit that **modifies data in the Ontology**, corresponding to Palantir's Action Type.

**Action Type characteristics:**
- **Atomic:** One transaction, rollback on failure
- **Composable:** One Action can modify multiple Entities' properties
- **Side Effects:** Can send notifications, trigger Pipelines
- **Authorization:** Via submission criteria, controls who can execute

```
Action Type: Assign Employee Role
    ├── Parameter: User inputs new role (form)
    ├── Business logic: Modify Employee.role property
    ├── Auto behavior: Create Relation between Employee ↔ Manager
    └── Side Effects: Notify old and new Manager
```

**Action Type structure (JSONB):**
```json
{
  "api_name": "assign_employee_role",
  "display_name": "Assign Employee Role",
  "description": "Assign employee to a new position",
  "status": "active",
  "parameters": [
    { "name": "employee_id", "type": "ref:employee", "required": true },
    { "name": "new_role", "type": "string", "required": true }
  ],
  "submission_criteria": {
    "roles": ["admin", "hr_manager"]
  },
  "side_effects": [
    { "type": "notification", "template": "role_changed", "recipients": ["employee_id", "manager_id"] }
  ]
}
```

**Action Type examples:**

| Action Type | Description |
|------------|-------------|
| `create_order` | Create order (atomic transaction) |
| `update_inventory` | Update inventory (atomic transaction) |
| `assign_employee_role` | Assign employee role |
| `transfer_product` | Transfer product |
| `approve_reorder` | Approve reorder request |

### Function (Server-side Logic, Palantir-aligned)

Function is business logic executed in an isolated server-side environment, supporting Python.

**Typical use cases:**

| Scenario | Description |
|----------|-------------|
| Derived properties | function-backed column |
| Aggregation | Entity Set aggregation statistics |
| Complex queries | Cross-Entity filtering |
| External queries | Query external systems to enrich Ontology |
| AI integration | Function calls Language Model |

**Function structure (JSONB):**
```json
{
  "api_name": "calculate_inventory_reorder_point",
  "display_name": "Calculate Inventory Reorder Point",
  "description": "Calculate optimal reorder point based on historical sales",
  "status": "active",
  "parameters": [
    { "name": "product_id", "type": "ref:product", "required": true },
    { "name": "lead_time_days", "type": "int", "required": false }
  ],
  "return_type": "float",
  "language": "python",
  "code": "def calculate_reorder_point(product_id, lead_time_days=7): ..."
}
```

### Skill (Workflow Orchestration)

**Skill is the unit for orchestrating business workflows, combining multiple Action Types to complete a full business process.**

This is a new layer we added to fill the gap that Palantir didn't consider when designing (no Agent Tool/Skill concepts existed).

#### Skill vs Action Type

```
Skill (Orchestration Layer)
├── Combines multiple Action Types
├── Defines execution order and flow control
├── Handles parameter passing and error handling
└── Can be triggered by user intent or Agent decision

Action Type (Atomic Layer)
├── Single business atomic operation
├── Atomic: rollback on failure
└── Called by Skill, or directly by Agent
```

#### Skill Structure (YAML)

```yaml
skill:
  id: "place_order"
  name: "Place Order"
  description: "Complete customer order workflow"
  type: "workflow"  # workflow | query | analysis

  steps:
    - id: "step_1"
      name: "Validate Payment"
      action_type: "validate_payment"
      parameters:
        payment_method: "{{ context.payment_method }}"
        amount: "{{ context.amount }}"
      on_failure: "abort"  # abort | skip | retry

    - id: "step_2"
      name: "Check Inventory"
      action_type: "check_inventory"
      parameters:
        product_id: "{{ context.product_id }}"
        quantity: "{{ context.quantity }}"
      on_failure: "abort"

    - id: "step_3"
      name: "Create Order"
      action_type: "create_order"
      parameters:
        customer_id: "{{ context.customer_id }}"
        product_id: "{{ context.product_id }}"
        quantity: "{{ context.quantity }}"
      on_failure: "rollback"  # rollback previous steps

    - id: "step_4"
      name: "Send Notification"
      action_type: "send_notification"
      parameters:
        channel: "wechat"
        template: "order_created"
        variables:
          order_id: "{{ step_3.output.order_id }}"
      on_failure: "continue"  # continue, doesn't affect main flow
```

#### Skill Execution Flow

```
User: "I want to order an iPhone"
         │
         ▼
┌─────────────────────────────────────┐
│  Skill: place_order                  │
│                                     │
│  Step 1: validate_payment ──✅────→ │
│  Step 2: check_inventory ──✅────→ │
│  Step 3: create_order ────✅────→ │
│  Step 4: send_notification ──✅──→ │
└─────────────────────────────────────┘
         │
         ▼
      Return result to user
```

#### Skill Trigger Methods

| Trigger | Description |
|---------|-------------|
| **User Intent** | User says "I want to order", Agent matches `place_order` Skill |
| **Agent Decision** | Agent determines which Skill to execute based on context |
| **Scheduled** | CRON trigger, e.g., "Check inventory every day at 2am" |

#### Skill Parameter Passing

```yaml
# Variable reference syntax
"{{ context.xxx }}"        # Variable from context
"{{ step_X.output.yyy }}"  # Output from previous step
```

#### MVP Skill Examples

| Skill | Description | Action Types Combined |
|-------|-------------|---------------------|
| `place_order` | Order workflow | validate_payment → check_inventory → create_order → send_notification |
| `refund_order` | Refund workflow | validate_refund → process_payment_refund → update_inventory → send_notification |
| `reorder_check` | Reorder check | check_inventory → calculate_reorder_point → create_purchase_request |

**MVP simplifications:**
- No skill registration system; skills are hardcoded in v1
- No skill versioning or hot-reload
- MVP doesn't implement Side Effects mechanism (v2)
- MVP doesn't implement Function code editor (v2)
- MVP doesn't implement Skill nesting and conditional execution (v2)

---

## Layer 4: Agent Layer

### Architecture: Dynamic Task Decomposition + Fixed Sub-Agent Roles

```
┌─────────────────────────────────────────────────────────┐
│                    Main Agent                           │
│  - Receives user request                               │
│  - Invokes Planner to decompose task                  │
│  - Coordinates sub-agent execution                    │
│  - Routes final output to Reporter                    │
└─────────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────┐
│  Fixed Sub-Agents (MVP — 4 roles)                     │
│                                                         │
│  Planner Agent     → Task decomposition & planning     │
│  Tool Agent        → Invokes Tools                    │
│  Reasoner Agent    → Reasoning and analysis            │
│  Reporter Agent    → Generates natural language output  │
└─────────────────────────────────────────────────────────┘
```

### Message Format (Point-to-Point)

```json
{
  "from": "planner",
  "to": "tool",
  "type": "task",
  "content": {
    "action": "entity_search",
    "params": {
      "concept": "product",
      "filters": { "category": "electronics" },
      "limit": 10
    }
  },
  "reply_to": "planner",
  "msg_id": "uuid"
}
```

**MVP simplifications:**
- Sub-agent count is fixed at 4 (no dynamic agent spawning)
- In-memory asyncio.Queue for message passing (no persistent message broker)
- No persistent memory across sessions (lost on restart)

---

## Layer 5: User Exchange Interface

### Conversational UI (MVP)

- Single-session web chat UI (ChatGPT-style)
- User enters natural language → Agent processes → Response displayed in chat
- Supports multi-turn conversation and simple task execution
- No file upload, no multimodal in MVP

### Task Trigger

- Users can trigger one-shot tasks via natural language ("查询..." / "生成...")
- Simple operations execute directly; complex operations trigger multi-turn confirmation

### Scheduled Automated Jobs

- Users configure timed tasks via CRON expressions in conversation
- At scheduled time → trigger Agent execution → store/notify results
- MVP: No standalone UI; configured via conversational commands

**MVP simplifications:**
- No independent scheduled jobs UI
- No job history persistence in MVP
- No email/notification integration in MVP

---

## Layer 5: Rich UI (A2UI Standard)

The conversational UI supports rich interactive components rendered from AI responses, using the **A2UI (Agent-to-User Interface)** open standard from Google.

### Why A2UI

| Traditional Approach | A2UI Approach |
|---------------------|-----------------|
| Agent generates HTML/JS (security risk) | Agent sends declarative JSON (safe, like data) |
| Fixed UI components | 10+ component types, LLM can request any |
| Hard for LLMs to generate incrementally | Flat component list, easy to update incrementally |
| Tied to one frontend framework | Framework-agnostic: Lit / React / Flutter |

### A2UI Protocol Overview

**A2UI flow:**
```
1. Generation: Agent generates A2UI JSON payload
2. Transport: Sent via AG-UI protocol (WebSocket)
3. Resolution: Client's A2UI Renderer parses JSON
4. Rendering: Maps abstract components to native widgets
```

### Supported Component Types

| Component | Purpose | Interactions |
|-----------|---------|--------------|
| `table` | List data | Sort, filter, multi-select, row click |
| `card` | Single entity detail | Click to view detail |
| `form` | Parameter input | Fill and submit |
| `chart` | Statistical charts | Hover for data (ECharts) |
| `metric_card` | KPI display | Trend indicator |
| `timeline` | Timeline | - |
| `button` | Action trigger | Click to execute action |

### A2UI Component Data Structures

**Table Component:**
```json
{
  "type": "table",
  "id": "bk_table_001",
  "columns": [
    { "id": "name", "label": "商品名称", "sortable": true },
    { "id": "category", "label": "品类" },
    { "id": "sales_7d", "label": "7日销量", "sortable": true }
  ],
  "rows": [...],
  "pagination": { "page": 1, "pageSize": 20, "total": 100 }
}
```

**Card Component:**
```json
{
  "type": "card",
  "id": "bk_card_001",
  "title": "iPhone 15",
  "subtitle": "SKU: PHONE-001",
  "media": { "type": "image", "url": "..." },
  "fields": [
    { "label": "价格", "value": "¥6,999" },
    { "label": "库存", "value": "2,450", "status": "normal" },
    { "label": "7日销量", "value": "+12.5%", "trend": "up" }
  ],
  "tags": ["手机", "苹果", "热销"]
}
```

**Form Component:**
```json
{
  "type": "form",
  "id": "bk_form_001",
  "title": "创建商品",
  "fields": [
    { "id": "name", "label": "商品名称", "type": "text", "required": true },
    { "id": "category", "label": "品类", "type": "select",
      "options": ["手机", "电视", "电脑", "配件"] }
  ],
  "submitLabel": "确认创建"
}
```

**Chart Component (ECharts):**
```json
{
  "type": "chart",
  "id": "bk_chart_001",
  "chartType": "line",
  "title": "月销量趋势",
  "xAxis": { "data": ["1月", "2月", "3月", "4月"] },
  "series": [{ "name": "销量", "data": [120, 150, 180, 200] }]
}
```

**Metric Card Component:**
```json
{
  "type": "metric_card",
  "id": "bk_metric_001",
  "title": "总销量",
  "value": "12,450",
  "unit": "件",
  "trend": { "value": "+12.5%", "direction": "up", "label": "环比" }
}
```

### Frontend Rendering Architecture

```
┌─────────────────────────────────────────────────────┐
│  ChatMessageRenderer                                 │
│  ├── TextRenderer          → Plain text/Markdown    │
│  ├── A2UIRenderer         → A2UI component mapping  │
│  │   ├── TableComponent   → A2UI table            │
│  │   ├── CardComponent    → A2UI card             │
│  │   ├── FormComponent    → A2UI form             │
│  │   ├── ChartComponent   → A2UI chart (ECharts)  │
│  │   ├── MetricComponent  → A2UI metric           │
│  │   └── ButtonComponent  → A2UI button           │
│  └── AG-UI EventBus      → A2UI events → Agent    │
└─────────────────────────────────────────────────────┘
```

### WebSocket + AG-UI Communication

**Connection:**
```
ws://host/api/v1/ws/{session_id}
- Token authentication
- AG-UI protocol for event dispatch
```

**Bidirectional format:**
```json
// Agent → Frontend (via AG-UI)
{ "type": "a2ui", "streamId": "msg_xxx", "components": [...] }
{ "type": "text", "content": "查到了以下热销商品：" }

// Frontend → Agent (user interaction via AG-UI)
{ "type": "ui_action", "blockId": "bk_table_001", "action": "generate_report", "payload": {} }
```

### UI Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Logo   OntologyAgent          [Tenant: 零售商家A]  [用户: 张三]  │
├───────────────┬───────────────────────────────────────────────────┤
│               │                                                   │
│  侧边栏        │  主对话区                                          │
│               │                                                   │
│  🏠 首页       │  ┌─────────────────────────────────────────────┐ │
│  💬 对话      │  │ 张三 12:30                                  │ │
│  📊 数据查询  │  │ 查一下最近7天销量前10的商品                    │ │
│  ⚙️ 设置      │  └─────────────────────────────────────────────┘ │
│               │                                                   │
│  ━━━━━━━━━━━  │  ┌─────────────────────────────────────────────┐ │
│  🏢 商家切换   │  │ OntologyAgent 12:30                         │ │
│               │  │ 查到了以下热销商品：                            │ │
│               │  │                                              │ │
│               │  │ ┌─────────────────────────────────────────┐ │ │
│               │  │ │ 🔥 销量前10商品              [导出][报告] │ │ │
│               │  │ ├─────┬──────────────┬────────────┤       │ │ │
│               │  │ │ #   │ 商品名称     │ 7日销量   │       │ │ │
│               │  │ ├─────┼──────────────┼────────────┤       │ │ │
│               │  │ │ 1   │ iPhone 15   │ 1,200    │       │ │ │
│               │  │ │ 2   │ 三星电视     │ 980      │       │ │ │
│               │  │ │ ... │              │          │       │ │ │
│               │  │ └─────┴──────────────┴────────────┘       │ │ │
│               │  │                                              │ │
│               │  │ ┌──────────┐ ┌──────────┐ ┌──────────┐   │ │
│               │  │ │ 总销量   │ │ 环比     │ │ 在架率   │   │ │
│               │  │ │ 12,450   │ │ +12.5%↑ │ │ 98.2%   │   │ │
│               │  │ └──────────┘ └──────────┘ └──────────┘   │ │
│               │  └─────────────────────────────────────────────┘ │
│               │                                                   │
├───────────────┴───────────────────────────────────────────────────┤
│  [  🖊️ 输入消息...                    ] [发送] [⚡快捷指令▼]     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent Harness

The Harness is the execution skeleton that controls how agents run, collaborate, and invoke tools. It consists of 6 core components.

### Component 1: Agent Execution Engine (AgentRunner)

```
┌─────────────────────────────────────────────────────────────┐
│                     AgentRunner (Main)                       │
│  - Start/stop all agents                                     │
│  - Manage agent lifecycle                                    │
│  - Receive user requests → dispatch to Main Agent            │
└─────────────────────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │ Planner  │    │   Tool   │    │ Reasoner │
  │  Agent  │    │  Agent   │    │  Agent   │
  │ inbox:Q │    │ inbox:Q  │    │ inbox:Q  │
  └──────────┘    └──────────┘    └──────────┘
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  ┌──────────┐
                  │ Reporter │
                  │  Agent   │
                  │ inbox:Q │
                  └──────────┘

Each agent runs as an independent asyncio.Task, sharing the same event loop.
```

**Main Agent responsibilities:**
- Receive user input
- Generate `msg_id`, create task
- Invoke Planner to decompose task
- Track all sub-agent task states
- Aggregate results → pass to Reporter

---

### Component 2: Message Router

**Standard message structure:**
```python
class AgentMessage(BaseModel):
    msg_id: str           # Globally unique
    from_agent: str       # Sender name
    to_agent: str         # Receiver name ("*" = broadcast)
    msg_type: str         # "task" | "result" | "error" | "heartbeat"
    content: dict         # Payload
    reply_to: str | None  # Reply target msg_id
    created_at: datetime
    ttl: int = 30         # seconds, discard if exceeded
    retries: int = 0      # Retry count
```

**Routing mechanism:**
```
Each agent has its own inbox (asyncio.Queue)
MessageRouter delivers messages based on the to_agent field
Broadcast messages are delivered to all agents
```

**Timeout and retry:**
```
- After sending a task message, the waiting party sets a timeout (default 60s)
- On timeout, auto-retry (up to 3 times)
- All 3 retries fail → return error message to sender
- Failed messages enter Dead Letter Queue (logged, non-blocking)
```

**Example message flow (product query):**
```
User → Main: "查最近7天销量前10商品"
Main → Planner: task{action: "plan", goal: "查销量前10商品"}
Planner → Main: result{plan: [step1: search, step2: aggregate, step3: report]}
Main → Tool:   task{action: "entity_search", concept: "product", filters: ...}
Tool → Main:   result{products: [...]}
Main → Reasoner: task{action: "aggregate", data: [...], metric: "sales_volume"}
Reasoner → Main: result{top10: [...]}
Main → Reporter: task{action: "format", data: top10, format: "table"}
Reporter → Main: result{"表格：商品 | 销量..."}
Main → User: final response
```

---

### Component 3: Tool Calling Protocol

**Tool standard interface:**
```python
class Tool(ABC):
    name: str                          # Globally unique
    description: str                   # For LLM to understand purpose
    params_schema: dict                 # JSON Schema for parameters
    is_admin_only: bool = False        # Admin-only flag

    @abstractmethod
    async def execute(self, params: dict, context: AgentContext) -> ToolResult:
        """Execute tool, return result or raise ToolExecutionError"""
        ...

class ToolResult(BaseModel):
    success: bool
    data: dict | None = None
    error: str | None = None
    execution_time_ms: int
```

**Tool Registry (ToolRegistry):**
```
Global singleton, maps name → Tool instance
Agent calls: tool_agent.execute("tool_name", params)
ToolRegistry locates the corresponding tool and invokes it
```

**Tool implementations:**

| Tool | Category | Implementation |
|------|----------|----------------|
| `ontology_read` | Business Operation | Query PostgreSQL ontology schema |
| `ontology_write` | Business Operation | Write PostgreSQL ontology schema |
| `entity_search` | Business Operation | SQL query entity data |
| `entity_write` | Business Operation | SQL write entity data |
| `external_api_call` | Business Operation | HTTP request to external system |
| `http_call` | Maintenance Atomic | httpx library call |
| `db_query` | Maintenance Atomic | SQLAlchemy execute |
| `file_read` / `file_write` | Maintenance Atomic | aiofiles |

---

### Component 4: LLM Gateway

**LLM calling interface:**
```python
class LLMGateway:
    """Global singleton, shared by all agents"""

    async def complete(
        self,
        system_prompt: str,
        messages: list[dict],   # [{"role": "user", "content": "..."}]
        model: str = "gpt-4o",
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ) -> LLMResponse:
        ...
```

**Per-agent prompt templates:**

```
Planner Agent System Prompt:
"""
你是一个任务规划 Agent。你的职责是将用户请求分解成执行步骤。
当前任务：{task_description}
当前上下文：{context}
请输出分步骤执行计划，格式为 JSON。
"""

Tool Agent System Prompt:
"""
你是一个工具调用 Agent。你的职责是根据规划执行具体操作。
当前步骤：{step_description}
可用的工具：{available_tools}
请选择合适的工具并执行。
"""

Reasoner Agent System Prompt:
"""
你是一个推理分析 Agent。你的职责是对数据进行分析和推理。
当前任务：{task_description}
数据：{data}
请给出分析结论。
"""

Reporter Agent System Prompt:
"""
你是一个报告生成 Agent。你的职责是将结果转化为用户可读的自然语言回复。
结果数据：{data}
回复格式：{format}
请生成自然语言回复。
"""
```

**MVP simplifications:**
- Model is fixed (no dynamic selection)
- No prompt version management
- No model fallback (failover)

---

### Component 5: Context Manager

**Conversation context:**
```python
class ConversationContext(BaseModel):
    """Complete context for one user session"""
    session_id: str
    tenant_id: str
    user_id: str
    messages: list[Message]          # Full conversation history
    ontology_ids: list[str]           # Ontologies loaded in this session
    variables: dict                  # Shared variables (cross-agent)
    created_at: datetime
    updated_at: datetime
```

**Rolling window strategy:**
```
- Keep the most recent N messages (default N=50)
- Discard oldest when exceeding
- Raw tool return data does not enter context; only final results do
```

**Context overflow handling:**
```
1. Estimate current context token count (approx: Chinese ~2 chars/token, English ~4 chars/token)
2. Exceeding threshold (default 8k tokens) → trigger compression
3. Compression: summary (LLM generates summary to replace original messages)
4. Still exceeding after compression → truncate oldest messages
```

**Cross-agent variable sharing:**
```
Main Agent maintains session_variables
Sub-agents can read/write their own context, and also access shared variables
variables structure: {"step1_result": {...}, "aggregated_data": [...]}
```

---

### Component 6: State Manager (Task State Machine)

**Task state machine:**
```
                    ┌─────────────────────────────────┐
                    │                                 │
                    ▼                                 │
PENDING ──→ RUNNING ──→ COMPLETED                     │
    │            │                                    │
    │            ├──→ FAILED (retryable)             │
    │            │                                    │
    │            └──→ TIMEOUT (max execution time exceeded)
    │                                                 │
    └──→ CANCELLED (user-initiated cancel)            │
                                                  │
                    ┌─────────────────────────────┘
                    │  (retry: up to 3 times)
                    ▼
                  RETRYING ──→ RUNNING
                       │
                       └──→ FAILED (retries exhausted)
```

**Execution tracking:**
```python
class TaskExecution(BaseModel):
    task_id: str
    msg_id: str
    from_agent: str
    to_agent: str
    action: str
    status: TaskStatus
    created_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    error: str | None
    retry_count: int = 0
    result: dict | None = None
```

**Main Agent task DAG:**
```
User request
  │
  ▼
┌─────────────────┐
│  Planner         │ ──generate step DAG──→ step1 → step2 → step3
└─────────────────┘
  │
  ▼
Each step is a TaskExecution, Main Agent tracks all step states
Critical path failure → entire request marked as failed
Non-critical path failure → optional degraded continuation
```

**Timeout configuration (per action type):**
```
ontology_read:     10s
entity_search:     15s
external_api_call: 30s
llm_call:          60s
report_generate:   30s
```

---

### Harness Global Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         AgentRunner                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    MessageRouter                          │   │
│  │  (asyncio.Queue per Agent + broadcast support)           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                   │
│    ┌─────────┬─────────┬─────────┬─────────┐                   │
│    ▼         ▼         ▼         ▼         ▼                    │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                  │
│ │ Main │ │Planner│ │ Tool │ │Reason│ │Report│                  │
│ │Agent │ │Agent  │ │Agent │ │Agent │ │Agent │                  │
│ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘                  │
│    │        │        │        │        │                        │
│    └────────┴────────┴────────┴────────┘                        │
│                         │                                        │
│                         ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    LLMGateway (Singleton)                 │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │ ToolRegistry ──── Tool implementations           │  │   │
│  │  │  ├── ontology_read / write                        │  │   │
│  │  │  ├── entity_search / write                        │  │   │
│  │  │  ├── external_api_call                             │  │   │
│  │  │  ├── http_call / db_query / file_read/write      │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                   │
│                              ▼                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              ContextManager (per session)                 │   │
│  │  - Rolling window (last N messages)                      │   │
│  │  - Context compression on overflow                       │   │
│  │  - Shared variables across agents                        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                   │
│                              ▼                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              StateManager (Task State Machine)            │   │
│  │  - Task DAG tracking                                     │   │
│  │  - Timeout / Retry / Dead Letter Queue                   │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## Data Storage Summary

| Data Type | Technology | Notes |
|-----------|------------|-------|
| Semantic Data (Schema) | PostgreSQL + JSONB | Flexible schema storage |
| Instance Data | PostgreSQL | Relational storage, join queries |
| Agent Messages | In-memory | Lost on restart |
| User Sessions | In-memory | Lost on restart |
| Scheduled Jobs | PostgreSQL | Persisted CRON jobs |

---

## MVP Scope Boundaries

**In Scope (v1.0):**
- 5-layer architecture running end-to-end
- Ontology CRUD (schema + entities)
- Multi-agent collaboration (4 fixed roles)
- Conversational UI with basic task execution
- Business Tools: ontology_read/write, entity_search/write
- Business Skills: product_query, customer_query, order_summary, inventory_alert
- Multi-tenant isolation (tenant_id at data level)
- Scheduled jobs (configured via conversation)

**Out of Scope (future versions):**
- Skill registration system (hardcoded skills)
- Dynamic sub-agent spawning
- Persistent agent memory across sessions
- Skill version management
- Ontology schema versioning
- Fine-grained tool/skill permission control
- Email/notification integration
- File upload in chat UI
- Graph database backend (save for later if needed)

---

## Tech Stack (Final)

| Component | Technology | Notes |
|-----------|------------|-------|
| Language | Python 3.11+ | |
| Web Framework | FastAPI | 异步高性能 |
| Database | PostgreSQL 15+ | JSONB 存储 ontology schema |
| ORM | SQLAlchemy 2.0 | |
| Agent Harness | **DeepAgent** | LangChain 官方，Batteries-included |
| Agent Engine | **LangGraph** | DeepAgent 内部调用，不需要直接操作 |
| LLM | **MiniMax / DeepSeek / Qwen** | 国产模型统一抽象 |
| UI Protocol | **A2UI** | Google 开源，Agent 生成富 UI 的标准 |
| Frontend Renderer | **A2UI Lit** | Web Components 渲染器（官方支持） |
| Transport / Protocol | **AG-UI** | CopilotKit 标准，对接 A2UI |
| Charts | ECharts | via A2UI chart component |
| Scheduled Jobs | APScheduler | |
| Authentication | Auth0 / Clerk / JWT | |

---

## Harness 实现映射

本文档第六部分定义的 Harness 6 大组件，与 DeepAgent 的对应关系：

| 本文 Harness 设计 | DeepAgent 内置对应 |
|-----------------|-------------------|
| Component 1: AgentRunner | DeepAgent `create_deep_agent()` 完整封装 |
| Component 2: MessageRouter | DeepAgent 内部事件/消息系统 |
| Component 3: ToolProtocol | DeepAgent `tools` 参数 + MCP 集成 |
| Component 4: LLMGateway | DeepAgent model-agnostic 调用（任何 tool-calling 模型） |
| Component 5: ContextManager | DeepAgent 内置 rolling window + 压缩 |
| Component 6: StateManager | LangGraph checkpointing（DeepAgent 内置） |

**DeepAgent 未涵盖的自研部分（需要自己实现）：**
- Ontology 存储层（PostgreSQL schema + entity）
- Business Tools（`ontology_read/write`、`entity_search/write`）
- Business Skills（`product_query`、`inventory_alert` 等业务能力）
- A2UI 组件映射（`table`、`card`、`chart` → A2UI Lit components）

---

## 技术栈层次关系

```
业务代码（自研）
    │
    ├── DeepAgent（Harness 层）
    │       │
    │       └── LangGraph（底层图执行引擎）
    │               │
    │               └── LangChain（模型/Tool 集成）
    │                       │
    │                       └── MiniMax / DeepSeek / Qwen
    │
    └── A2UI Lit Renderer（UI 渲染层）
            │
            └── AG-UI（传输协议）
```

---

## Permission Control

### Palantir Two-Tier Security Model

Aligned with Palantir Foundry's two-layer permission control:

| Layer | Control Object | Description |
|-------|---------------|-------------|
| **Ontology Resources** | Object Type, Link Type, Action Type Schema | Define permissions (who can view/edit type definitions) |
| **Objects & Links** | Specific data rows and relationships | Row-level security (who can view/edit which data) |

```
┌─────────────────────────────────────────────────────────────┐
│                    Two-Tier Security Model                   │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: Ontology Resources (Schema Definition Layer)      │
│  ├── Who can view/edit Object Type Schema                   │
│  ├── Who can view/edit Link Type Definition                 │
│  └── Who can view/edit Action Type Definition               │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: Objects & Links (Data Instance Layer)             │
│  ├── Who can view/edit which data rows (Row-Level Security) │
│  └── Who can view/edit which relationships (Link-Level)     │
└─────────────────────────────────────────────────────────────┘
```

### Design Principles

- **Principle of Least Privilege:** Each user/role only gets the minimum permissions needed.
- **Defense in Depth:** Multiple permission checkpoints, not a single gate.
- **Tenant Isolation:** Permission system sits on top of tenant isolation; cross-tenant access is always denied.
- **Metadata-Driven:** Permission rules as Ontology metadata, unified management.

### Permission Model

**RBAC + ABAC hybrid:**

```
User → Roles → Permission Set → Operable Resources
              ↑
         Attribute Conditions (time, IP, tenant, etc.)
```

### Layer 1: Ontology Resources Permissions

| Ontology Resource | Allowed Roles | Notes |
|-----------------|---------------|-------|
| Object Type definition read | `admin`, `operator`, `viewer` | All logged-in users can view type definitions |
| Object Type definition edit | `admin` | Only admin can modify type Schema |
| Link Type definition edit | `admin` | Only admin can modify relation definitions |
| Action Type definition edit | `admin` | Only admin can modify operation definitions |
| Interface definition edit | `admin` | Only admin can modify interface definitions |

### Layer 2: Objects & Links Permissions

**Row-Level Data Permissions:**

Within the same tenant, further restrict by data attributes:

```
User A: can view orders where region = "East China"
User B: can view orders where region = "South China"
User C (admin): can view all regions
```

**Link-Level Permissions:**

```
User A: can view Relations they created
User B: can view Relations assigned to them
Admin: can view all Relations
```

**Implementation:** Data permissions are injected as filters at the `entity_search` Tool level, automatically带上用户所属 region/department 等属性限制.

### Tool/Skill Permission Mapping

| Tool/Skill Category | Resource Layer | Allowed Roles | Notes |
|----------------|---------|-------------|-------|
| `entity_search`, `link_search` | Objects & Links | `admin`, `operator`, `viewer` | Query-type, broad access |
| `entity_write`, `link_write` | Objects & Links | `admin`, `operator` | Write operations more restricted |
| `action_execute` | Objects & Links | `admin`, `operator` | Action execution requires operator access |
| `ontology_read` | Ontology Resources | `admin`, `operator`, `viewer` | All logged-in users can view |
| `ontology_write` | Ontology Resources | `admin` | Only admin can modify definitions |
| Maintenance Atomics (`http_call`, `db_query`) | - | `admin` only | Dangerous operations |

### UI Component Permissions

| Component/Action | Resource Layer | Allowed Roles | Notes |
|----------------|---------|-------------|-------|
| Table sort/filter | - | All logged-in users | Unrestricted |
| Table export CSV | Objects & Links | `admin`, `operator` | May contain sensitive data |
| Card detail view | - | All logged-in users | Unrestricted |
| Form submit/edit | Objects & Links | `admin`, `operator` | Write operations |
| Scheduled job management | Ontology Resources | `admin` | Highest privilege |
| Ontology Schema editing | Ontology Resources | `admin` | Highest privilege |

### Permission Check Flow

```
User request
    │
    ▼
┌─────────────────┐
│  Auth Middleware │ → Verify token, extract user_id / tenant_id / roles
└─────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│  Layer 1: Ontology Resources Permission  │ → Check if user has right to access this type definition
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│  Layer 2: Objects & Links Permission     │ → Inject row-level/Link-level permission conditions into query
└─────────────────────────────────────────┘
    │
    ▼
Execute operation
```

---

## Observability

### Design Principles

- **Three Pillars:** Logging + Metrics + Tracing — all three are required.
- **Failure-Oriented:** Prioritize recording errors, latency, and anomalies over happy paths.
- **Low Overhead:** Observability collection itself must not degrade system performance.

### Logging (Structured Logs)

**Log format (JSON):**
```json
{
  "timestamp": "2026-06-18T12:30:00.123Z",
  "level": "INFO",
  "trace_id": "abc123",
  "span_id": "def456",
  "service": "ontology-agent",
  "agent_id": "main",
  "component": "tool_agent",
  "event": "tool_execution",
  "tool_name": "entity_search",
  "params": { "concept": "product", "limit": 10 },
  "duration_ms": 45,
  "status": "success",
  "tenant_id": "tenant_001",
  "user_id": "user_001"
}
```

**Log level guidelines:**

| Level | Usage |
|-------|-------|
| DEBUG | Development, detailed execution steps |
| INFO | Key business flow nodes (request start/end, tool calls) |
| WARNING | Anomalous but recoverable (timeout retry, rate limit triggered) |
| ERROR | Execution failure (tool call failed, LLM API error) |
| CRITICAL | System-level failure (DB connection lost, circuit breaker triggered) |

**Key events to log:**
- User request start/end
- Agent message send/receive
- Tool call start/success/failure
- LLM API call (including token usage)
- Scheduled job trigger/complete
- Permission check denial
- Rate limit / circuit breaker trigger

### Metrics

**System-level metrics:**

| Metric | Type | Description |
|--------|------|-------------|
| `requests_total` | Counter | Total requests (by endpoint, status labels) |
| `request_duration_seconds` | Histogram | Request latency distribution |
| `active_websocket_connections` | Gauge | Current active WebSocket connections |
| `agent_tasks_running` | Gauge | Currently running Agent tasks |
| `agent_tasks_queue_depth` | Gauge | Per-agent inbox queue depth |

**Business-level metrics:**

| Metric | Type | Description |
|--------|------|-------------|
| `tool_calls_total` | Counter | Total tool calls (by tool_name) |
| `tool_call_duration_seconds` | Histogram | Tool call latency (by tool_name) |
| `llm_calls_total` | Counter | LLM API calls (by model, status) |
| `llm_call_duration_seconds` | Histogram | LLM API latency (by model) |
| `llm_token_usage` | Counter | Token consumption (input/output separate) |
| `scheduled_jobs_triggered_total` | Counter | Scheduled job triggers |

**Alert thresholds:**

| Metric | Alert Threshold |
|--------|-----------------|
| ERROR log frequency | > 10/min |
| Request P99 latency | > 5s |
| Tool call error rate | > 5% |
| LLM API error rate | > 1% |
| WebSocket connections | > 80% of limit |
| Agent inbox queue depth | > 100 |

### Tracing (Distributed Tracing)

**Trace granularity:**

```
User Request (trace_id: abc)
    │
    ├─► Main Agent (span: main_001)
    │       │
    │       ├─► Planner Agent (span: planner_001)
    │       │       └─► LLM call (span: llm_001)
    │       │
    │       ├─► Tool Agent (span: tool_001)
    │       │       └─► Tool: entity_search (span: db_001)
    │       │
    │       ├─► Reasoner Agent (span: reasoner_001)
    │       │       └─► LLM call (span: llm_002)
    │       │
    │       └─► Reporter Agent (span: reporter_001)
    │               └─► LLM call (span: llm_003)
    │
    └─► A2UI Render (span: render_001)
```

**Propagation:** trace_id propagates through message passing to all sub-agents, ensuring end-to-end traceability.

**Implementation:** Use OpenTelemetry standard, compatible with Jaeger/Zipkin/Tempo backends.

---

## Security

### Input Security

| Risk | Mitigation |
|------|-----------|
| SQL injection | All DB queries use parameterized queries (SQLAlchemy ORM) |
| Prompt injection | User input sanitized before LLM, strip special instruction characters |
| SSRF | `http_call` Tool restricts target IP/domain to whitelist only |
| Path traversal | `file_read/write` restricted to designated directories, `../` forbidden |
| Oversized input | Request body size limit + LLM context max tokens limit |

### Authentication & Authorization

| Item | Implementation |
|------|---------------|
| Identity auth | JWT Token (short-lived access_token + long-lived refresh_token) |
| Token issuance | Initial login / Token refresh |
| Tenant isolation | All DB queries enforced with tenant_id condition |
| Permission check | RBAC + ABAC (checked before Tool/Skill invocation) |

### Sensitive Data Protection

```
Sensitive data (passwords, API keys, etc.)
    │
    ▼
Store in environment variables or secret manager (Vault/AWS Secrets Manager)
    │
    ▼
Code reads from env var or secret manager, no hardcoding
    │
    ▼
Mask in logs (phone numbers, ID numbers, etc.)
```

---

## Rate Limiting & Circuit Breaker

### Rate Limiting

**Multi-layer rate limiting:**

| Dimension | Granularity | Limit (example) |
|-----------|-------------|-----------------|
| Per user | user_id | 60 requests/minute |
| Per tenant | tenant_id | 1000 requests/minute |
| Per tool | tool_name | 100 calls/minute |
| Per LLM model | model | 60 requests/minute (API quota) |

**On limit exceeded:**
- Return HTTP 429 Too Many Requests
- Include `Retry-After` header telling client when to retry

### Circuit Breaker

```
Normal: CLOSED state, requests pass through
    │
    │  N consecutive failures (configurable threshold)
    ▼
OPEN state: All requests return error immediately, no downstream call
    │
    │  After cool-down period, enter HALF_OPEN, allow test requests
    ▼
    │  Success → CLOSED; Failure → stay OPEN
```

**Circuit breaker targets:**
- LLM API calls (external dependency, most fragile)
- External system APIs (`external_api_call`)
- Database connections

---

## Configuration Management

### Configuration Hierarchy

```
Environment variables (injected by container/K8s)
    │
    ▼
Application config (config.yaml / config.json)
    │
    ▼
Local override (.env file, for development)
```

### Sensitive Configuration

| Config Item | Storage |
|------------|---------|
| Database password | Environment variable or secret manager |
| LLM API Key | Environment variable or secret manager |
| JWT Secret | Environment variable |
| External system credentials | Secret manager |

### Configuration清单

```yaml
# Database
DATABASE_URL: postgresql://user:pass@host:5432/ontology

# LLM
LLM_PROVIDER: minimax  # minimax | deepseek | qwen
LLM_API_KEY: xxx
LLM_MODEL: minimax-01

# DeepAgent
USE_DEEP_AGENT: true

# A2UI
A2UI_RENDERER_URL: http://localhost:5173

# WebSocket
WS_MAX_CONNECTIONS: 1000
WS_PING_INTERVAL: 30s
WS_PING_TIMEOUT: 10s

# Rate Limiting
RATE_LIMIT_USER: 60/minute
RATE_LIMIT_TENANT: 1000/minute

# Observability
OTEL_EXPORTER: jaeger
OTEL_ENDPOINT: http://jaeger:4318
LOG_LEVEL: INFO
```

---

## WebSocket Management

### Connection Lifecycle

```
Client initiates connection (with JWT token)
    │
    ▼
Server verifies token, resolves user_id / tenant_id
    │
    ▼
WebSocket connection established, session_id assigned
    │
    ▼
Connection joins Tenant room (supports Tenant-wide broadcast)
    │
    ▼
Heartbeat keepalive (ping/pong, configurable interval)
    │
    ▼
Client-initiated close / timeout / heartbeat failure
    │
    ▼
Clean up session state, close all subtasks
```

### Connection Limits

| Limit Type | Value | Exceeded Behavior |
|------------|-------|-------------------|
| Max per user | 3 | Reject new connection |
| Max per Tenant | 500 | Reject new connection |
| Global max | 10000 | Reject new connection |

### Reconnection Strategy

- On disconnect detected, client waits 1s / 2s / 4s / 8s... (exponential backoff) before retrying
- Max retry count configurable
- After successful reconnect, client sends `sync` message, server provides missed context

---

## Audit Logging

### Audit Event清单

| Event | Logged Content | Importance |
|-------|---------------|-----------|
| User login/logout | user_id, IP, time, success/failure | High |
| Permission denied | user_id, attempted resource, time | High |
| Tool invocation | user_id, tool_name, params, result | Medium |
| Data modification | user_id, operation type, entities affected, before/after | High |
| Ontology modification | user_id, ontology_id, operation type, changes | High |
| Scheduled job modification | user_id, job_id, operation type | Medium |
| Admin operations | user_id, operation content, scope of impact | High |

### Audit Log Storage

- Separate audit log table (append-only)
- Or write to separate audit log service (e.g., Elasticsearch)
- Retention: minimum 1 year (compliance requirement)

---

## Deployment & Operations

### Deployment Architecture

```
                    ┌─────────────┐
                    │   Nginx     │
                    │ (LB)        │
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   ┌──────────┐    ┌──────────┐    ┌──────────┐
   │ FastAPI   │    │ FastAPI   │    │ FastAPI   │
   │ Instance 1│    │ Instance 2│    │ Instance 3│
   └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
         │                 │                 │
         └─────────────────┼─────────────────┘
                           ▼
                    ┌─────────────┐
                    │ PostgreSQL  │
                    │ (Primary/Replica) │
                    └─────────────┘
```

### Containerization

- **Image:** Python 3.11 + all dependencies, packaged as Docker image
- **Health check:** `/health` endpoint, checks DB connection + Agent status
- **Graceful shutdown:** On SIGTERM, wait for in-flight requests to complete (max 30s)

### Environments

| Environment | Purpose |
|-------------|---------|
| `dev` | Local development |
| `staging` | Pre-release testing |
| `prod` | Production |

### Key Ops Commands

```bash
# Check status
kubectl get pods

# View logs
kubectl logs -f deployment/ontology-agent

# Scale
kubectl scale deployment/ontology-agent --replicas=5

# Rolling update
kubectl rollout restart deployment/ontology-agent
```

---

## Next Steps

1. Write implementation plan (via writing-plans skill)
2. Scaffold project structure
3. Implement Layer 1-2: LLM + Ontology storage
4. Implement Layer 3: Tools
5. Implement Layer 4: Agent collaboration
6. Implement Layer 5: Chat UI
7. Integrate scheduled jobs
8. End-to-end testing
