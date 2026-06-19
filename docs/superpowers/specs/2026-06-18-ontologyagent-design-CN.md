# OntologyAgent 设计规格说明书

## 项目概述

**项目名称：** OntologyAgent
**类型：** 知识图谱增强的 AI Agent 平台（SaaS，多租户）
**MVP 目标：** 构建一个可运行的本体感知 Agent，能够加载本体、与用户对话、调用工具完成简单任务。
**目标行业：** 零售（第一个垂直落地场景），但设计为通用平台。

---

## 架构

### 五层技术栈（对齐 Palantir + AI Native 扩展）

```
┌─────────────────────────────────────────────────────────────────────────┐
│  第5层：用户交换入口                                              │
│  对话式 UI（A2UI）│ 任务触发 │ 定时自动化作业                       │
├─────────────────────────────────────────────────────────────────────────┤
│  第4层：Agent 层（AI Native 扩展）                                 │
│  多 Agent 动态协作（DeepAgent Harness）                            │
│  Main Agent │ Planner │ Tool │ Reasoner │ Reporter                   │
├─────────────────────────────────────────────────────────────────────────┤
│  第3层：Tools → Action Types → Skills                              │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Tools：底层原子操作（http_call, db_query, file_read/write）   │   │
│  │ Action Types：业务原子操作（create_order, update_inventory）  │   │
│  │ Skills：流程编排（组合多个 Action Type）                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────────────┤
│  第2层：Ontology 层（对齐 Palantir Foundry）                       │
│  ┌──────────────┬───────────────┬────────────────┐                 │
│  │   语义元素   │   动态元素    │   接口元素     │                 │
│  │  Object Type     │  Action Type │  Interface      │                 │
│  │  Property    │  Function    │               │                 │
│  │  Link Type    │              │               │                 │
│  │  (Palantir)    │  (Palantir)  │  (Palantir)    │                 │
│  └──────────────┴───────────────┴────────────────┘                 │
├─────────────────────────────────────────────────────────────────────────┤
│  第1层：LLM                                                      │
│          MiniMax / DeepSeek / Qwen（国产模型统一抽象）              │
└─────────────────────────────────────────────────────────────────────────┘
```

### 与 Palantir Foundry 架构对比

| 层次 | Palantir Foundry | OntologyAgent |
|------|-----------------|---------------|
| 用户应用层 | Object Explorer / Workshop / Quiver | **A2UI 对话式 UI** |
| 运营层 | Ontology（Object/Action/Function） | Ontology + **多 Agent 协作** |
| 数据集成层 | Dataset / Virtual Table / Model | PostgreSQL + LLM |

**OntologyAgent 的独特优势：**
- **多 Agent 协作**：Palantir 是单 Actor 模型，OntologyAgent 支持多 Agent 动态协作
- **A2UI 富 UI**：自然语言驱动的对话式交互，而非预定义表单
- **DeepAgent Harness**：开箱即用的 AI Native 执行骨架
- **国产模型**：MiniMax / DeepSeek / Qwen，不依赖国外模型

---

## 第1层：LLM

- 使用 MiniMax / DeepSeek / Qwen 作为基础模型（国产模型统一抽象）。
- MVP 阶段不做微调，通过 Prompt Engineering 路由请求到对应 Agent。

---

## 第2层：Ontology 层

### 设计原则（Palantir 四大原则）

**原则 1：领域驱动设计（Domain-Driven Design）**
> Ontology 建模的是现实世界，而不是源数据。

- Object 代表语义上有意义的概念（`Product`、`Order`、`Customer`），而非数据库表名
- Link Type 代表真实关系（"商品 → 供应商"），而非外键
- 禁止 1:1 映射源系统列（如 `dtLastInspMod` → `lastInspectionDate`）

**原则 2：不要重复自己（DRY / Rule of Three）**
> 同一语义出现三次，就该重构。

- 跨团队协作防止重复
- 使用 Shared Property 避免多处重复属性定义
- Link Type 的复用优先于新 Link Type 的创建

**原则 3：开放扩展、封闭修改（Open-Closed Principle）**
> 保护核心模型，开放扩展能力。

- 核心 Object Type 保持稳定
- 通过 Interface 扩展抽象层
- 新业务需求通过新 Object Type / Skill 实现，而非修改既有定义

**原则 4：组合优于深层继承（Composition over Inheritance）**
> 用 Interface 多继承替代深层类层次。

- 避免宽而稀疏的 Object Type（包含大量可选字段）
- 用 Interface 对共享特征建模
- Object Type 可以实现多个 Interface，支持多重多态

### Palantir 术语对照

| Palantir Foundry | 本文对应 | 说明 |
|----------------|---------|------|
| **Object Type** | **Object Type** | 业务实体类型定义 |
| **Object** | **Object** | 单个实体实例 |
| **Object Set** | **Object Set** | 一组对象的集合 |
| **Link Type** | **Link Type** | 关系类型定义 |
| **Interface** | **Interface** | 抽象接口，支持多态继承 |
| **Action Type** | **Action Type** | 原子事务，改变数据的操作单位 |
| **Function** | **Function** | 服务器端业务逻辑（Query / Ontology Edit） |
| **—** | **Skill** | 流程编排，组合多个 Action Type（本文新增）|

### 元数据（Metadata）

每个 Ontology 资源都有完整元数据：

| 元数据 | 说明 |
|--------|------|
| **status** | `active` / `experimental` / `deprecated` |
| **api_name** | 编程时引用的名称 |
| **display_name** | 用户界面显示的名称 |
| **visibility** | `prominent` / `normal` / `hidden` |
| **description** | 业务含义说明 |

### Object Type（对应 Palantir Object Type）

**存储于 PostgreSQL，使用 JSONB 列。**

| 字段 | 描述 |
|------|------|
| `id` | UUID |
| `tenant_id` | UUID（多租户隔离） |
| `api_name` | API 名称（如 `product`） |
| `display_name` | 显示名称（如"商品"） |
| `description` | 业务含义 |
| `status` | `active` / `experimental` / `deprecated` |
| `visibility` | `prominent` / `normal` / `hidden` |
| `backing_data_source` | 指向哪个数据集/表 |
| `interfaces` | 实现的 Interface 列表 |
| `properties` | JSONB — 属性定义列表 |
| `relations` | JSONB — 关系定义列表 |

**Object Type 结构（JSONB）：**
```json
{
  "api_name": "product",
  "display_name": "商品",
  "description": "零售商品实体",
  "status": "active",
  "visibility": "prominent",
  "interfaces": ["sellable_item"],
  "properties": [
    { "api_name": "name", "display_name": "名称", "type": "string", "required": true },
    { "api_name": "sku", "display_name": "SKU", "type": "string", "required": true },
    { "api_name": "price", "display_name": "价格", "type": "float", "required": true },
    { "api_name": "category", "display_name": "品类", "type": "string" }
  ],
  "relations": [
    { "api_name": "sold_by", "target_concept": "supplier", "cardinality": "many-to-many" },
    { "api_name": "belongs_to_category", "target_concept": "category", "cardinality": "many-to-one" }
  ]
}
```

### Interface（Palantir 独有概念）

Interface 描述 Object Type 的**形状（shape）**和**能力**，提供多态性：

```
Interface: SellableItem（可售商品）
    ├── Property: price, name
    └── 可被实现：
        ├── Product（实现 SellableItem + 独有属性 stock_count）
        ├── Service（实现 SellableItem + 独有属性 duration）
        └── Subscription（实现 SellableItem + 独有属性 billing_cycle）
```

**Interface 结构（JSONB）：**
```json
{
  "api_name": "sellable_item",
  "display_name": "可售商品",
  "description": "所有可销售的商品和服务共同接口",
  "properties": [
    { "api_name": "price", "display_name": "价格", "type": "float" },
    { "api_name": "name", "display_name": "名称", "type": "string" }
  ]
}
```

**Interface vs Object Type：**

| | Object Type（Object Type） | Interface |
|--|--------------------|-----------|
| 性质 | 具体（concrete） | 抽象（abstract） |
| 实例化 | 可以直接实例化 | 必须通过实现的 Object Type 实例化 |
| 后端数据 | 有 backing datasource | 无 backing datasource |

### Property（属性）

Property 是 Object Type 的特征，分为两种：

- **Local Property**：直接在 Object Type 上定义
- **Shared Property**：跨多个 Object Type 共享的标准化属性

**Property 结构（JSONB）：**
```json
{
  "api_name": "price",
  "display_name": "价格",
  "type": "float",
  "description": "商品单价",
  "required": false,
  "shared": false
}
```

**类型支持：** `string`、`int`、`float`、`bool`、`datetime`、`ref`（引用其他 Object）

### Link Type（对应 Palantir Link Type）

Link Type 定义两个 Object Type 之间的关系，Link Type Instance 是该关系的单个实例。

**Cardinality（基数）：**

| 类型 | 说明 | 示例 |
|------|------|------|
| `one-to-one` | 一个 Object 对应一个 Object | 员工 → 工位 |
| `one-to-many` | 一个 Object 对应多个 Object | 供应商 → 商品 |
| `many-to-many` | 双向多对多 | 商品 ↔ 标签（需要 join table） |

**Link Type 结构（JSONB）：**
```json
{
  "api_name": "sold_by",
  "display_name": "销售方",
  "source_concept": "product",
  "target_concept": "supplier",
  "cardinality": "many-to-many",
  "description": "商品与供应商的关系"
}
```

**自引用 Link Type（同一 Object Type 内部）：**
```json
{
  "api_name": "manager",
  "display_name": "上级经理",
  "source_concept": "employee",
  "target_concept": "employee",
  "cardinality": "many-to-one"
}
```

### Object（对应 Palantir Object）

**存储于 PostgreSQL 关系表。**

- `entities`：id, tenant_id, concept_id, created_at, updated_at
- `entity_properties`：entity_id, property_api_name, value (JSONB)
- `entity_relations`：entity_id, relation_api_name, target_entity_id

### Object Set（对象集）

一组 Object 的集合，支持过滤、聚合操作：

```json
{
  "object_type": "product",
  "filters": [
    { "property": "category", "operator": "eq", "value": "electronics" },
    { "property": "price", "operator": "gte", "value": 1000 }
  ],
  "sort": { "property": "sales_7d", "direction": "desc" },
  "limit": 20
}
```

### 反模式（Anti-Patterns）

| 反模式 | 描述 | 正确做法 |
|--------|------|---------|
| **Kitchen Sink** | 一个 Object Type 包含大量无关字段，镜像源系统 | 按领域实体拆分 Object Type |
| **Golden Hammer** | 用 Pipeline/Function 处理本该用 Skill 的人工决策 | Skill 用于人类决策，Function 用于自动化 |
| **系统镜像** | Object Type 等于源系统表 | 按业务语义建模 |
| **孤岛团队** | 单团队设计 Ontology | 多团队协作，防止重复 |
| **无文档** | 不记录 Object Type/Property 业务含义 | 在 Ontology Manager 中完整记录元数据 |

### MVP 简化

- 不引入专用图数据库（PostgreSQL 足够支撑 MVP 查询）
- MVP 不做 Schema 版本管理
- 图遍历通过 SQL JOIN 实现
- MVP 暂不实现 Interface 继承机制（v2 再加）
- MVP 暂不实现 Ontology Branching（v2 再加）

---

## 第3层：Tools、Action Types、Functions 和 Skills

### 核心理念

基于权威研究（AgentOS、Arcade、SoK: Agentic Skills），本项目采用以下分层：

| 层级 | 概念 | 本质 | 示例 |
|------|------|------|------|
| **底层** | **Tool** | 可执行函数，Agent 的"手" | `http_call`, `db_query`, `file_read` |
| **中层** | **Action Type** | 业务原子操作，对应 Palantir | `create_order`, `update_inventory` |
| **上层** | **Skill** | 流程编排，组合多个 Action Type | `place_order_skill` |

**Tool vs Skill 的本质区别（基于 AgentOS 定义）：**

> **"Skills tell the LLM *when* to do something. Tools are the things the LLM actually invokes."**

| | Tool | Skill |
|--|------|-------|
| **本质** | 可执行函数 | 提示词模块/流程定义 |
| **LLM 看到什么** | 函数名 + 描述 + 参数 schema | 系统提示词的一部分 |
| **何时运行** | LLM 生成时调用 | Agent 构建时注入 |
| **做什么** | 执行操作 | 教 LLM 何时/如何使用 |

### Tool（底层原子操作）

Tool 是 Agent 实际调用的底层函数，有明确定义的输入、输出和副作用。

#### 基础原子操作（生产环境中仅管理员可调用）

| Tool | 描述 |
|------|------|
| `http_call` | 向外部系统发起 HTTP 请求 |
| `db_query` | 执行 PostgreSQL 查询 |
| `file_read` | 读取文件系统文件 |
| `file_write` | 写入文件系统文件 |

#### 业务操作类（Agent 可调用）

| Tool | 描述 |
|------|------|
| `ontology_read` | 读取 Ontology Schema（Object Type、Property、Link Type） |
| `ontology_write` | 创建/更新 Ontology Schema |
| `entity_search` | 查询 Object（商品、客户等） |
| `entity_write` | 写入/更新 Object |
| `entity_set_query` | 查询 Object Set（对象集） |
| `external_api_call` | 调用外部零售系统 API（ERP、WMS、POS） |

### Action Type（业务原子操作，对应 Palantir）

Action Type 是 Ontology 中**改变数据的交易单位**，对应 Palantir 的 Action Type。

**Action Type 的特点：**
- **原子性**：一笔交易，失败则回滚
- **可组合**：一次 Action 可修改多个 Object 的多个 Property
- **副作用（Side Effects）**：可发送通知、触发 Pipeline 等
- **授权控制**：通过 submission criteria 限制谁能执行

```
Action Type: Assign Employee Role（分配员工角色）
    ├── 参数定义：用户输入新角色（表单）
    ├── 业务逻辑：修改 Employee.role property
    ├── 自动行为：在 Employee ↔ Manager 之间创建 Link Type
    └── 副作用（Side Effects）：通知新旧 Manager
```

**Action Type 结构（JSONB）：**
```json
{
  "api_name": "assign_employee_role",
  "display_name": "分配员工角色",
  "description": "将员工分配到新的工作岗位",
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

**Action Type 示例：**

| Action Type | 描述 |
|------------|------|
| `create_order` | 创建订单（原子事务） |
| `update_inventory` | 更新库存（原子事务） |
| `assign_employee_role` | 分配员工角色 |
| `transfer_product` | 商品调拨 |
| `approve_reorder` | 审批补货请求 |

### Function（服务器端逻辑，对应 Palantir）

Function 是在服务器端隔离环境中执行的业务逻辑，支持 Python。

**典型用例：**

| 场景 | 说明 |
|------|------|
| 派生属性 | function-backed column（派生列） |
| 聚合计算 | Object Set 聚合统计 |
| 复杂查询 | 跨多个 Object 的复杂过滤 |
| 外部查询 | external function（查询外部系统丰富 Ontology） |
| AI 集成 | Function 调用 Language Model |

**Function 结构（JSONB）：**
```json
{
  "api_name": "calculate_inventory_reorder_point",
  "display_name": "计算库存补货点",
  "description": "根据历史销量计算最佳补货点",
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

### Function vs Skill 的区别

| | **Function** | **Skill** |
|--|-------------|----------|
| **层级** | 底层 | 上层 |
| **本质** | 服务端代码逻辑 | 流程编排 |
| **对应** | Palantir Function | 本文新增层 |
| **格式** | Python 代码 | Markdown + YAML Frontmatter |
| **做什么** | 执行计算/查询 | 组合多个 Action Type |

**Function vs Skill 关系图：**
```
Skill（流程编排）
    │
    ├── step_1: validate_payment (Action Type)
    │
    ├── step_2: check_inventory (Action Type)
    │       │
    │       └── 可能调用 Function (calculate_reorder_point)
    │
    ├── step_3: create_order (Action Type)
    │
    └── step_4: send_notification (Action Type)
```

| 场景 | Function | Skill |
|------|----------|-------|
| 计算补货点 | ✅ `calculate_reorder_point()` | — |
| 下单完整流程 | — | ✅ `place_order` |
| 退款完整流程 | — | ✅ `refund_order` |
| 聚合统计 | ✅ `aggregate_sales()` | — |

**一句话总结：**
- **Function** = 做计算/查询的代码
- **Skill** = 把多个操作串起来的流程

---

### Skill（流程编排层）

**Skill 是业务流程的编排单元，通过组合多个 Action Type 完成完整业务流程。**

这是我们新增的一层，填补了 Palantir 在设计时没有考虑的 Agent 编排层。

#### Skill vs Action Type 的关系

```
Skill（编排层）
├── 组合多个 Action Type
├── 定义执行顺序和流程控制
├── 处理参数传递和错误处理
└── 可以被用户意图触发或 Agent 决策触发

Action Type（原子层）
├── 单个业务原子操作
├── 原子性：失败则回滚
└── 由 Skill 调用，或直接由 Agent 调用
```

#### Skill 结构（Markdown + YAML Frontmatter）

Skill 是 **markdown 文件**，头部包含 YAML frontmatter，用于声明元数据；body 部分是自然语言指令，在 agent 构建时注入到 system prompt。

```markdown
---
name: place_order
description: 完成客户下单的完整流程
type: workflow
triggers:
  - intent: "我想下单"
  - intent: "创建订单"
---

# Place Order Workflow

当用户表达下单意图时，执行以下步骤：

## Step 1: Validate Payment
调用 `validate_payment` action，传入：
- `payment_method`: 支付方式（从 context 获取）
- `amount`: 订单金额（从 context 获取）

如果验证失败，终止流程并返回错误。

## Step 2: Check Inventory
调用 `check_inventory` action，传入：
- `product_id`: 产品 ID
- `quantity`: 购买数量

如果库存不足，终止流程并返回错误。

## Step 3: Create Order
调用 `create_order` action，传入：
- `customer_id`: 客户 ID（从 context 获取）
- `product_id`: 产品 ID
- `quantity`: 购买数量

保存返回的 `order_id` 供后续步骤使用。

## Step 4: Send Notification
调用 `send_notification` action，传入：
- `channel`: "wechat"
- `template`: "order_created"
- `variables.order_id`: 上一步返回的 order_id

即使通知发送失败，订单创建仍视为成功。

## Error Handling
- 支付验证失败：abort（终止整个流程）
- 库存不足：abort
- 订单创建失败：rollback（自动回滚之前的操作）
- 通知发送失败：continue（不影响主流程）
```

#### Skill 执行流程

```
用户: "我想下单购买 iPhone"
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
      返回结果给用户
```

#### Skill 的触发方式

| 触发方式 | 说明 |
|---------|------|
| **用户意图** | 用户说"我想下单"，Agent 匹配到 `place_order` Skill |
| **Agent 决策** | Agent 根据上下文判断需要执行某个 Skill |
| **定时触发** | CRON 触发，如"每天凌晨检查库存" |

#### Skill 的参数传递

在 Skill 的 markdown 正文中，使用以下语法引用变量：

```markdown
从 context 获取：{{ context.payment_method }}
引用上一步输出：{{ step_3.output.order_id }}
```

#### Skill 存储位置

Skill 文件存储在 `skills/` 目录下，每个 Skill 一个 markdown 文件：

```
skills/
├── place_order.md      # 下单流程
├── refund_order.md     # 退款流程
└── reorder_check.md    # 补货检查
```

Agent 构建时，Skill 文件被读取、解析 frontmatter 元数据，并注入 body 到 system prompt。

#### MVP Skill 示例

| Skill | 描述 | Action Types 组合 |
|-------|------|-----------------|
| `place_order` | 下单流程 | validate_payment → check_inventory → create_order → send_notification |
| `refund_order` | 退款流程 | validate_refund → process_payment_refund → update_inventory → send_notification |
| `reorder_check` | 补货检查 | check_inventory → calculate_reorder_point → create_purchase_request |

**MVP 简化：**
- 无 Skill 注册系统，v1 版为硬编码
- 无 Skill 版本管理或热加载
- MVP 暂不实现 Side Effects 机制（v2 再加）
- MVP 暂不实现 Function 的代码编辑器（v2 再加）
- MVP 暂不实现 Skill 嵌套和条件执行（v2 再加）

---

## 第4层：Agent 层

### 架构：动态任务分解 + 固定子 Agent 角色

```
┌─────────────────────────────────────────────────────────┐
│                    Main Agent                           │
│  - 接收用户请求                                        │
│  - 调用 Planner 分解任务                                │
│  - 协调子 Agent 执行                                    │
│  - 将最终输出路由给 Reporter                            │
└─────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│  固定子 Agent（MVP — 4 种角色）                        │
│                                                         │
│  Planner Agent     → 任务分解与规划                     │
│  Tool Agent       → 调用 Tools                         │
│  Reasoner Agent   → 推理与分析                         │
│  Reporter Agent   → 生成自然语言输出                    │
└─────────────────────────────────────────────────────────┘
```

### 消息格式（点对点）

```json
{
  "from": "planner",
  "to": "tool",
  "type": "task",
  "content": {
    "action": "entity_search",
    "params": {
      "object_type": "product",
      "filters": { "category": "electronics" },
      "limit": 10
    }
  },
  "reply_to": "planner",
  "msg_id": "uuid"
}
```

**MVP 简化：**
- 子 Agent 数量固定为 4 个（无动态创建）
- 使用内存 asyncio.Queue 做消息传递（无持久化消息代理）
- 无跨会话持久化记忆（重启后丢失）

---

## 第5层：用户交换入口

### 对话式 UI（MVP）

- 单会话网页聊天 UI（类 ChatGPT）
- 用户输入自然语言 → Agent 处理 → 回复展示在聊天中
- 支持多轮对话和简单任务执行
- MVP 不支持文件上传和多模态

### 任务触发

- 用户可通过自然语言触发一次性任务（"查询..." / "生成..."）
- 简单操作直接执行；复杂操作触发多轮确认

### 定时自动化作业

- 用户通过对话配置定时任务（CRON 表达式）
- 到点触发 → Agent 执行 → 存储/通知结果
- MVP：独立 UI，暂通过对话命令配置

**MVP 简化：**
- 无独立定时任务 UI
- MVP 不做任务历史持久化
- MVP 不做邮件/通知集成

---

### 富 UI（A2UI 标准）

对话式 UI 支持由 AI 响应渲染的富交互组件，使用 Google 开源的 **A2UI（Agent-to-User Interface）** 标准。

### 为什么用 A2UI

| 传统方案 | A2UI 方案 |
|---------|----------|
| Agent 生成 HTML/JS（安全风险） | Agent 发送声明式 JSON（安全，如数据般可控） |
| 固定 UI 组件 | 10+ 组件类型，LLM 可按需请求任意组件 |
| LLM 难以增量生成 | 扁平组件列表，易于增量更新 |
| 绑定单一前端框架 | 框架无关：Lit / React / Flutter 均可 |

### A2UI 协议概述

**A2UI 流程：**
```
1. 生成：Agent 生成 A2UI JSON payload
2. 传输：通过 AG-UI 协议发送（WebSocket）
3. 解析：客户端 A2UI Renderer 解析 JSON
4. 渲染：将抽象组件映射为原生组件
```

### 支持的组件类型

| 组件 | 用途 | 交互 |
|------|------|------|
| `table` | 列表数据 | 排序、筛选、多选、行点击 |
| `card` | 单个实体详情 | 点击查看详情 |
| `form` | 参数输入 | 填写并提交 |
| `chart` | 统计图表 | 悬停查看数据 |
| `metric_card` | KPI 展示 | 趋势指示器 |
| `timeline` | 时间线 | - |
| `button` | 操作触发 | 点击执行 action |

### A2UI 组件数据结构

**Table 组件：**
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

**Card 组件：**
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

**Form 组件：**
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

**Chart 组件（ECharts）：**
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

**Metric Card 组件：**
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

### 前端渲染架构

```
┌─────────────────────────────────────────────────────┐
│  ChatMessageRenderer                                 │
│  ├── TextRenderer          → 纯文本/Markdown        │
│  ├── A2UIRenderer         → A2UI 组件映射          │
│  │   ├── TableComponent   → A2UI table            │
│  │   ├── CardComponent   → A2UI card             │
│  │   ├── FormComponent   → A2UI form             │
│  │   ├── ChartComponent  → A2UI chart (ECharts) │
│  │   ├── MetricComponent → A2UI metric           │
│  │   └── ButtonComponent → A2UI button           │
│  └── AG-UI EventBus      → A2UI 事件 → Agent      │
└─────────────────────────────────────────────────────┘
```

### WebSocket + AG-UI 通信

**连接方式：**
```
ws://host/api/v1/ws/{session_id}
- Token 认证
- AG-UI 协议做事件分发
```

**双向消息格式：**
```json
// Agent → 前端（通过 AG-UI）
{ "type": "a2ui", "streamId": "msg_xxx", "components": [...] }
{ "type": "text", "content": "查到了以下热销商品：" }

// 前端 → Agent（用户交互，通过 AG-UI）
{ "type": "ui_action", "blockId": "bk_table_001", "action": "generate_report", "payload": {} }
```

### UI 布局

```
┌─────────────────────────────────────────────────────────────────┐
│  Logo   OntologyAgent          [租户: 零售商家A]  [用户: 张三]    │
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
│               │  │ │ 1   │ iPhone 15  │ 1,200    │       │ │ │
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

Harness 是控制 Agent 运行、协作和调用工具的执行骨架，由 6 个核心组件构成。

### 组件1：Agent 执行引擎（AgentRunner）

```
┌─────────────────────────────────────────────────────────────┐
│                     AgentRunner (Main)                       │
│  - 启动/停止所有 Agent                                     │
│  - 管理 Agent 生命周期                                      │
│  - 接收用户请求 → 分发给 Main Agent                         │
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

每个 Agent 作为独立 asyncio.Task 运行，共享同一事件循环。
```

**Main Agent 职责：**
- 接收用户输入
- 生成 `msg_id`，创建任务
- 调用 Planner 分解任务
- 跟踪所有子 Agent 任务状态
- 聚合结果 → 交给 Reporter

---

### 组件2：消息路由（MessageRouter）

**标准消息结构：**
```python
class AgentMessage(BaseModel):
    msg_id: str           # 全局唯一
    from_agent: str       # 发送者名称
    to_agent: str        # 接收者名称（"*" = 广播）
    msg_type: str         # "task" | "result" | "error" | "heartbeat"
    content: dict         # 负载
    reply_to: str | None  # 回复目标 msg_id
    created_at: datetime
    ttl: int = 30         # 秒，超时丢弃
    retries: int = 0       # 重试次数
```

**路由机制：**
```
每个 Agent 有自己的 inbox（asyncio.Queue）
MessageRouter 根据 to_agent 字段将消息投递给对应 inbox
广播消息投递给所有 Agent
```

**超时与重试：**
```
- 发送 task 消息后，等待方设置超时时间（默认 60s）
- 超时后自动重试（最多 3 次）
- 3 次都失败 → 返回 error 消息给发送方
- 失败消息进入 Dead Letter Queue（记录，不阻塞）
```

**消息流示例（商品查询）：**
```
用户 → Main: "查最近7天销量前10商品"
Main → Planner: task{action: "plan", goal: "查销量前10商品"}
Planner → Main: result{plan: [step1: search, step2: aggregate, step3: report]}
Main → Tool:   task{action: "entity_search", object_type: "product", filters: ...}
Tool → Main:   result{products: [...]}
Main → Reasoner: task{action: "aggregate", data: [...], metric: "sales_volume"}
Reasoner → Main: result{top10: [...]}
Main → Reporter: task{action: "format", data: top10, format: "table"}
Reporter → Main: result{"表格：商品 | 销量..."}
Main → 用户: 最终回复
```

---

### 组件3：Tool 调用协议（Tool Protocol）

**Tool 标准接口：**
```python
class Tool(ABC):
    name: str                          # 全局唯一标识
    description: str                   # 供 LLM 理解用途
    params_schema: dict                 # JSON Schema for parameters
    is_admin_only: bool = False        # 管理员专属标记

    @abstractmethod
    async def execute(self, params: dict, context: AgentContext) -> ToolResult:
        """执行 Tool，返回结果或抛出 ToolExecutionError"""
        ...

class ToolResult(BaseModel):
    success: bool
    data: dict | None = None
    error: str | None = None
    execution_time_ms: int
```

**Tool 注册表（ToolRegistry）：**
```
全局单例，维护 name → Tool 实例 映射
Agent 调用：tool_agent.execute("tool_name", params)
ToolRegistry 负责找到对应 Tool 并调用
```

**Tool 实现列表：**

| Tool | 类别 | 实现方式 |
|------|------|---------|
| `ontology_read` | 业务操作 | 查询 PostgreSQL ontology schema |
| `ontology_write` | 业务操作 | 写入 PostgreSQL ontology schema |
| `entity_search` | 业务操作 | SQL 查询 instance data |
| `entity_write` | 业务操作 | SQL 写入 instance data |
| `external_api_call` | 业务操作 | HTTP 请求到外部系统 |
| `http_call` | 基础原子 | httpx 库调用 |
| `db_query` | 基础原子 | SQLAlchemy 执行 |
| `file_read` / `file_write` | 基础原子 | aiofiles |

---

### 组件4：LLM 网关（LLM Gateway）

**LLM 调用接口：**
```python
class LLMGateway:
    """全局单例，所有 Agent 共享"""

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

**各 Agent 的 Prompt 模板：**

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

**MVP 简化：**
- 模型固定（不动态选择）
- 不做 Prompt 版本管理
- 不做模型降级（failover）

---

### 组件5：Context 管理器（Context Manager）

**会话上下文：**
```python
class ConversationContext(BaseModel):
    """一次用户会话的完整上下文"""
    session_id: str
    tenant_id: str
    user_id: str
    messages: list[Message]          # 完整对话历史
    ontology_ids: list[str]           # 本会话加载的 ontology
    variables: dict                  # 共享变量（跨 Agent）
    created_at: datetime
    updated_at: datetime
```

**滚动窗口策略：**
```
- 保留最近 N 条消息（默认 N=50）
- 超出时丢弃最老的
- Tool 返回的原始数据不进入 context，只进入最终结果
```

**上下文溢出处理：**
```
1. 估算当前 context token 数（估算：中文 ~2 chars/token，英文 ~4 chars/token）
2. 超过阈值（默认 8k tokens）→ 触发压缩
3. 压缩方式：summary（LLM 生成摘要替换原始消息）
4. 压缩后仍超过 → 截断最老消息
```

**跨 Agent 变量共享：**
```
Main Agent 维护 session_variables
子 Agent 可读写自己的 context，也可访问共享 variables
variables 结构：{"step1_result": {...}, "aggregated_data": [...]}
```

---

### 组件6：状态管理器（Task State Machine）

**任务状态机：**
```
                    ┌─────────────────────────────────┐
                    │                                 │
                    ▼                                 │
PENDING ──→ RUNNING ──→ COMPLETED                     │
    │            │                                    │
    │            ├──→ FAILED（可重试）                │
    │            │                                    │
    │            └──→ TIMEOUT（超过最大执行时间）       │
    │                                                 │
    └──→ CANCELLED（用户主动取消）                       │
                                                  │
                    ┌─────────────────────────────┘
                    │  （重试：最多3次）
                    ▼
                  RETRYING ──→ RUNNING
                       │
                       └──→ FAILED（重试耗尽）
```

**执行跟踪：**
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

**Main Agent 任务 DAG：**
```
用户请求
  │
  ▼
┌─────────────────┐
│  Planner         │ ──生成步骤 DAG──→ step1 → step2 → step3
└─────────────────┘
  │
  ▼
每个步骤是一个 TaskExecution，Main Agent 跟踪所有步骤状态
关键路径失败 → 整个请求标记失败
非关键路径失败 → 可选降级继续
```

**超时配置（按 action 类型）：**
```
ontology_read:     10s
entity_search:   15s
external_api_call: 30s
llm_call:          60s
report_generate:    30s
```

---

### Harness 全局架构图

```
┌──────────────────────────────────────────────────────────────────┐
│                         AgentRunner                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    MessageRouter                          │   │
│  │  （每个 Agent 一个 asyncio.Queue + 广播支持）               │   │
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
│  │                    LLMGateway（单例）                       │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │ ToolRegistry ──── Tool 实现                       │  │   │
│  │  │  ├── ontology_read / write                         │  │   │
│  │  │  ├── entity_search / write                       │  │   │
│  │  │  ├── external_api_call                             │  │   │
│  │  │  ├── http_call / db_query / file_read/write        │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                   │
│                              ▼                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              ContextManager（按会话）                       │   │
│  │  - 滚动窗口（最近 N 条消息）                               │   │
│  │  - 溢出时上下文压缩                                        │   │
│  │  - 跨 Agent 共享变量                                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                   │
│                              ▼                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              StateManager（任务状态机）                      │   │
│  │  - 任务 DAG 跟踪                                          │   │
│  │  - 超时 / 重试 / 死信队列                                  │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 数据存储汇总

| 数据类型 | 技术 | 说明 |
|---------|------|------|
| 语义数据（Schema） | PostgreSQL + JSONB | 灵活 Schema 存储 |
| 实例数据 | PostgreSQL | 关系存储，JOIN 查询 |
| Agent 消息 | 内存 | 重启后丢失 |
| 用户会话 | 内存 | 重启后丢失 |
| 定时任务 | PostgreSQL | CRON 任务持久化 |

---

## MVP 范围边界

**v1.0 在范围内：**
- 5 层架构端到端运行
- Ontology CRUD（Schema + 实例）
- 多 Agent 协作（4 个固定角色）
- 带基础任务执行的对话语 UI
- 业务 Tools：ontology_read/write、entity_search/write
- 业务 Action Types：create_order、update_inventory、product_query、customer_query
- 业务 Functions：order_summary、calculate_reorder_point
- 业务 Skills：place_order、refund_order、reorder_check
- 多租户隔离（数据层 tenant_id）
- 通过对话配置定时任务

**未来版本范围外：**
- Action Type / Function / Skill 注册系统（v1 为硬编码）
- 动态子 Agent 产生
- 跨会话持久化 Agent 记忆
- Action Type / Function / Skill 版本管理
- Ontology Schema 版本管理
- 细粒度 Tool/Action Type/Skill 权限控制
- 邮件/通知集成
- 对话 UI 文件上传
- 图数据库后端（需要时再引入）

---

## 技术栈（最终版）

| 组件 | 技术 | 说明 |
|------|------|------|
| 编程语言 | Python 3.11+ | |
| Web 框架 | FastAPI | 异步高性能 |
| 数据库 | PostgreSQL 15+ | JSONB 存储 ontology schema |
| ORM | SQLAlchemy 2.0 | |
| Agent Harness | **DeepAgent** | LangChain 官方，Batteries-included |
| Agent 引擎 | **LangGraph** | DeepAgent 内部调用，无需直接操作 |
| LLM | **MiniMax / DeepSeek / Qwen** | 国产模型统一抽象 |
| UI 协议 | **A2UI** | Google 开源，Agent 生成富 UI 的标准 |
| 前端渲染器 | **A2UI Lit** | Web Components 渲染器（官方支持） |
| 传输层 | **AG-UI** | CopilotKit 标准，对接 A2UI |
| 图表 | ECharts | 通过 A2UI chart 组件 |
| 定时任务 | APScheduler | |
| 身份认证 | Auth0 / Clerk / JWT | |

---

## Harness 实现映射

本文档定义的 Harness 6 大组件，与 DeepAgent 的对应关系：

| Harness 设计组件 | DeepAgent 内置对应 |
|----------------|------------------|
| 组件1：AgentRunner | DeepAgent `create_deep_agent()` 完整封装 |
| 组件2：MessageRouter | DeepAgent 内部事件/消息系统 |
| 组件3：ToolProtocol | DeepAgent `tools` 参数 + MCP 集成 |
| 组件4：LLMGateway | DeepAgent model-agnostic 调用（任何 tool-calling 模型） |
| 组件5：ContextManager | DeepAgent 内置滚动窗口 + 压缩 |
| 组件6：StateManager | LangGraph checkpointing（DeepAgent 内置） |

**DeepAgent 未涵盖的自研部分（需要自己实现）：**
- Ontology 存储层（PostgreSQL schema + instance）
- 业务 Tools（`ontology_read/write`、`entity_search/write`）
- 业务 Action Types（`create_order`、`update_inventory`）
- 业务 Functions（`order_summary`、`calculate_reorder_point`）
- 业务 Skills（`place_order`、`refund_order`）
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

## 权限控制（Permission Control）

### Palantir 双层安全模型

与 Palantir Foundry 保持一致，采用**两层权限控制**：

| 层次 | 控制对象 | 说明 |
|------|---------|------|
| **Ontology Resources** | Object Type、Link Type、Action Type 的 Schema | 定义权限（谁可以看/编辑类型定义） |
| **Objects & Links** | 具体的数据行和关系 | 行级安全（谁可以看/编辑哪条数据） |

```
┌─────────────────────────────────────────────────────────────┐
│                    权限控制两层模型                           │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: Ontology Resources（资源定义层）                   │
│  ├── 谁能看/编辑 Object Type Schema                         │
│  ├── 谁能看/编辑 Link Type 定义                             │
│  └── 谁能看/编辑 Action Type 定义                           │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: Objects & Links（数据实例层）                      │
│  ├── 谁能看/编辑哪一行数据（行级安全）                        │
│  └── 谁能看/编辑哪一条关系（Link 级安全）                     │
└─────────────────────────────────────────────────────────────┘
```

### 设计原则

- **最小权限原则：** 每个用户/角色仅能访问其工作所需的最小权限范围。
- **纵深防御：** 多层权限检查，而非单一检查点。
- **租户隔离：** 权限体系建立在租户隔离之上，跨租户访问永远被拒绝。
- **元数据驱动：** 权限规则作为 Ontology 元数据的一部分，统一管理。

### 权限模型

**基于 RBAC（Role-Based Access Control）+ ABAC（Attribute-Based Access Control）混合：**

```
用户 → 角色 → 权限集合 → 可操作资源
              ↑
         属性条件（时间、IP、租户等）
```

### Layer 1: Ontology Resources 权限

| Ontology 资源 | 可用角色 | 说明 |
|-------------|---------|------|
| Object Type 定义读取 | `admin`、`operator`、`viewer` | 所有登录用户可查看类型定义 |
| Object Type 定义编辑 | `admin` | 仅管理员可修改类型 Schema |
| Link Type 定义编辑 | `admin` | 仅管理员可修改关系定义 |
| Action Type 定义编辑 | `admin` | 仅管理员可修改操作定义 |
| Interface 定义编辑 | `admin` | 仅管理员可修改接口定义 |

### Layer 2: Objects & Links 权限

**行级数据权限（Row-Level Security）：**

同一 Tenant 下，按数据属性进一步限制：

```
用户 A：可查看 region = "华东" 的订单
用户 B：可查看 region = "华南" 的订单
用户 C（管理员）：可查看所有region的订单
```

**Link 级权限：**

```
用户 A：可查看自己创建的 Link Type
用户 B：可查看分配给自己的 Link Type
管理员：可查看所有 Link Type
```

**实现方式：** 数据权限在 `entity_search` Tool 层面注入 filter，自动带上用户所属区域/部门等属性限制。

### Tool / Action Type / Function / Skill 权限映射

| 类型 | 名称 | 资源层级 | 可用角色 | 说明 |
|------|------|---------|---------|------|
| Tool | `entity_search`、`link_search` | Objects & Links | `admin`、`operator`、`viewer` | 查询类，权限宽松 |
| Tool | `entity_write`、`link_write` | Objects & Links | `admin`、`operator` | 写操作权限更严格 |
| Action Type | `action_execute` | Objects & Links | `admin`、`operator` | Action 执行需要操作权限 |
| Tool | `ontology_read` | Ontology Resources | `admin`、`operator`、`viewer` | 所有登录用户可查看 |
| Tool | `ontology_write` | Ontology Resources | `admin` | 仅管理员可修改定义 |
| Tool | 基础原子类（`http_call`、`db_query`） | - | 仅 `admin` | 危险操作，仅管理员可调用 |
| Function | `order_summary` | Objects & Links | `admin`、`operator`、`viewer` | 查询类，权限宽松 |
| Skill | `place_order` | Objects & Links | `admin`、`operator` | 流程执行需要操作权限 |

### UI 组件权限

| 组件/操作 | 资源层级 | 可用角色 | 说明 |
|-----------|---------|---------|------|
| 表格排序/筛选 | - | 所有登录用户 | 无限制 |
| 表格导出 CSV | Objects & Links | `admin`、`operator` | 可能涉及敏感数据 |
| 卡片详情查看 | - | 所有登录用户 | 无限制 |
| 表单提交/修改 | Objects & Links | `admin`、`operator` | 写操作 |
| 定时任务管理 | Ontology Resources | `admin` | 最高权限 |
| Ontology Schema 编辑 | Ontology Resources | `admin` | 最高权限 |

### 权限检查流程

```
用户请求
    │
    ▼
┌─────────────────┐
│  认证中间件      │ → 验证 token，提取 user_id / tenant_id / roles
└─────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│  Layer 1: Ontology Resources 权限检查     │ → 检查用户是否有权访问此类型定义
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│  Layer 2: Objects & Links 权限检查       │ → 在查询中注入行级/Link级权限条件
└─────────────────────────────────────────┘
    │
    ▼
执行操作
```

---

## 可观测性（Observability）

### 设计原则

- **三位一体：** Logging + Metrics + Tracing 缺一不可。
- **面向失败设计：** 优先记录错误、延迟、异常，而非成功路径。
- **低开销：** 可观测性采集本身不应影响系统性能。

### Logging（结构化日志）

**日志格式（JSON）：**
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
  "params": { "object_type": "product", "limit": 10 },
  "duration_ms": 45,
  "status": "success",
  "tenant_id": "tenant_001",
  "user_id": "user_001"
}
```

**日志级别规范：**

| 级别 | 使用场景 |
|------|---------|
| DEBUG | 开发环境，详细执行步骤 |
| INFO | 正常业务流程关键节点（请求开始/结束、Tool 调用） |
| WARNING | 异常但可恢复（超时重试、限流触发） |
| ERROR | 执行失败（Tool 调用失败、LLM API 错误） |
| CRITICAL | 系统级故障（数据库连接失败、熔断触发） |

**需要记录的关键事件：**

- 用户请求开始/结束
- Agent 消息发送/接收
- Tool 调用开始/成功/失败
- LLM API 调用（包含 token 用量）
- 定时任务触发/完成
- 权限检查拒绝
- 限流/熔断触发

### Metrics（指标）

**系统级指标：**

| 指标 | 类型 | 说明 |
|------|------|------|
| `requests_total` | Counter | 总请求数（按 endpoint、status 标签） |
| `request_duration_seconds` | Histogram | 请求延迟分布 |
| `active_websocket_connections` | Gauge | 当前活跃 WebSocket 连接数 |
| `agent_tasks_running` | Gauge | 当前运行中的 Agent 任务数 |
| `agent_tasks_queue_depth` | Gauge | 各 Agent inbox 队列深度 |

**业务级指标：**

| 指标 | 类型 | 说明 |
|------|------|------|
| `tool_calls_total` | Counter | Tool 调用总次数（按 tool_name） |
| `tool_call_duration_seconds` | Histogram | Tool 调用延迟（按 tool_name） |
| `llm_calls_total` | Counter | LLM API 调用次数（按 model、status） |
| `llm_call_duration_seconds` | Histogram | LLM API 延迟（按 model） |
| `llm_token_usage` | Counter | Token 消耗（input/output 分别统计） |
| `scheduled_jobs_triggered_total` | Counter | 定时任务触发次数 |

**报警阈值建议：**

| 指标 | 报警阈值 |
|------|---------|
| ERROR 日志频率 | > 10条/分钟 |
| 请求 P99 延迟 | > 5s |
| Tool 调用错误率 | > 5% |
| LLM API 错误率 | > 1% |
| WebSocket 连接数 | > 阈值上限的 80% |
| Agent inbox 队列深度 | > 100 |

### Tracing（链路追踪）

**追踪粒度：**

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

**传播方式：** trace_id 通过消息传递扩散到所有子 Agent，保证端到端可追踪。

**实现建议：** 使用 OpenTelemetry 标准，兼容 Jaeger/Zipkin/Tempo 等后端。

---

## 安全（Security）

### 输入安全

| 风险 | 防护措施 |
|------|---------|
| SQL 注入 | 所有数据库查询使用参数化查询（SQLAlchemy ORM） |
| Prompt 注入 | 用户输入在传入 LLM 前做清洗，去除特殊指令字符 |
| SSRF | Tool `http_call` 限制目标 IP/域名，非白名单不准请求 |
| 文件路径遍历 | `file_read/write` 限制在专用目录，禁止 `../` |
| 超长输入 | 请求 body 有 size limit，LLM context 有 max tokens 限制 |

### 认证与授权

| 项目 | 实现方式 |
|------|---------|
| 身份认证 | JWT Token（短期 access_token + 长期 refresh_token） |
| Token 分发 | 首次登录 / Token 刷新 |
| Tenant 隔离 | 所有数据库查询强制带 tenant_id 条件 |
| 权限检查 | RBAC + ABAC（在 Tool/Skill 调用前检查） |

### 敏感数据保护

```
敏感数据（密码、API Key等）
    │
    ▼
存入环境变量或密钥管理服务（Vault/AWS Secrets Manager）
    │
    ▼
代码中通过 env var 或 secret manager 读取，不硬编码
    │
    ▼
日志中脱敏（手机号、身份证等打码处理）
```

---

## 限流与熔断（Rate Limiting & Circuit Breaker）

### 限流

**多层级限流：**

| 限流维度 | 粒度 | 限制值（示例） |
|---------|------|---------------|
| 用户级 | per user_id | 60 请求/分钟 |
| Tenant 级 | per tenant_id | 1000 请求/分钟 |
| Tool 级 | per tool_name | 100 调用/分钟 |
| LLM API 级 | per model | 60 请求/分钟（受 API quota 限制） |

**超出限流时：**
- 返回 HTTP 429 Too Many Requests
- 附带 `Retry-After` 头告知客户端重试时间

### 熔断

**熔断器模式（Circuit Breaker）：**

```
正常：CLOSED 状态，请求直接通过
    │
    │  连续 N 次失败（阈值可配置）
    ▼
OPEN 状态：所有请求直接返回错误，不发到下游
    │
    │  冷却时间后，进入 HALF_OPEN，允许部分请求通过
    ▼
    │  通过则 CLOSED；失败则继续 OPEN
```

**熔断对象：**
- LLM API 调用（外部依赖，最脆弱）
- 外部系统 API（`external_api_call`）
- 数据库连接

---

## 配置管理（Configuration Management）

### 配置层级

```
环境变量（容器/K8s 注入）
    │
    ▼
应用配置（config.yaml / config.json）
    │
    ▼
本地覆盖（.env 文件，开发环境用）
```

### 敏感配置

| 配置项 | 存储方式 |
|--------|---------|
| 数据库密码 | 环境变量 或 密钥管理服务 |
| LLM API Key | 环境变量 或 密钥管理服务 |
| JWT Secret | 环境变量 |
| 外部系统凭证 | 密钥管理服务 |

### 配置项清单

```yaml
# 数据库
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

# 限流
RATE_LIMIT_USER: 60/minute
RATE_LIMIT_TENANT: 1000/minute

# 可观测性
OTEL_EXPORTER: jaeger
OTEL_ENDPOINT: http://jaeger:4318
LOG_LEVEL: INFO
```

---

## WebSocket 管理（WebSocket Management）

### 连接生命周期

```
客户端发起连接（带 JWT token）
    │
    ▼
服务器验证 token，解析 user_id / tenant_id
    │
    ▼
建立 WebSocket 连接，分配 session_id
    │
    ▼
连接加入 Tenant 房间（支持 Tenant 内广播）
    │
    ▼
心跳保活（ping/pong，间隔可配置）
    │
    ▼
客户端主动关闭 / 超时断开 / 心跳失败断开
    │
    ▼
清理 session 状态，关闭所有子任务
```

### 连接数管理

| 限制项 | 值 | 超出处理 |
|--------|---|---------|
| 单用户最大连接数 | 3 | 拒绝新连接 |
| 单 Tenant 最大连接数 | 500 | 拒绝新连接 |
| 全局最大连接数 | 10000 | 拒绝新连接 |

### 断线重连策略

- 客户端检测到断线后，等待 1s / 2s / 4s / 8s...（指数退避）后重连
- 最大重试次数可配置
- 重连成功后，客户端发送 `sync` 消息，服务端补充缺失的上下文

---

## 审计日志（Audit Logging）

### 审计事件清单

| 事件 | 记录内容 | 重要性 |
|------|---------|--------|
| 用户登录/登出 | user_id, IP, 时间, 成功/失败 | 高 |
| 权限拒绝 | user_id, 试图访问的资源, 时间 | 高 |
| Tool 调用 | user_id, tool_name, params, 结果 | 中 |
| 数据变更 | user_id, 操作类型, 涉及实体, 变更前后 | 高 |
| Ontology 变更 | user_id, ontology_id, 操作类型, 变更内容 | 高 |
| 定时任务变更 | user_id, job_id, 操作类型 | 中 |
| 管理员操作 | user_id, 操作内容, 影响范围 | 高 |

### 审计日志存储

- 独立审计日志表（append-only）
- 或写入独立审计日志服务（如 Elasticsearch）
- 保留期限：至少 1 年（合规要求）

---

## 部署与运维（Deployment & Operations）

### 部署架构

```
                    ┌─────────────┐
                    │   Nginx     │
                    │ (负载均衡)   │
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
                    │  (主从)     │
                    └─────────────┘
```

### 容器化

- **镜像：** Python 3.11 + 所有依赖，打成 Docker 镜像
- **健康检查：** `/health` endpoint，检测 DB 连接 + Agent 状态
- **优雅关闭：** SIGTERM 时等待正在处理的请求完成（最多 30s）

### 环境

| 环境 | 用途 |
|------|------|
| `dev` | 本地开发 |
| `staging` | 预发布测试 |
| `prod` | 生产环境 |

### 关键运维命令

```
# 查看运行状态
kubectl get pods

# 查看日志
kubectl logs -f deployment/ontology-agent

# 扩缩容
kubectl scale deployment/ontology-agent --replicas=5

# 执行滚动更新
kubectl rollout restart deployment/ontology-agent
```

---

## 下一步

1. 编写实现计划（通过 writing-plans skill）
2. 脚手架项目结构
3. 实现第1-2层：LLM + Ontology 存储
4. 实现第3层：Tools
5. 实现第4层：Agent 协作
6. 实现第5层：对话 UI
7. 集成定时任务
8. 端到端测试
