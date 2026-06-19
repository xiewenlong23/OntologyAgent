<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/ontology-anti-patterns/
---
# Ontology design: Anti-patterns
即使是经验丰富的 Ontology 设计者也可能会陷入常见的设计陷阱，这些陷阱乍一看似乎合理，但随着 Ontology 的增长会产生严重问题。本节将识别反复出现的反模式，解释它们发生的原因，并提供避免或解决这些问题的具体指导。

Even experienced Ontology designers can fall into common design traps that seem reasonable initially but create significant problems as the Ontology grows. This section identifies recurring anti-patterns, explains why they occur, and provides concrete guidance for avoiding or resolving them.
避免这些反模式将帮助您构建一个准确表示业务领域、减少维护开销并支持强大的跨职能工作流的 Ontology。

Avoiding these anti-patterns will help you build an Ontology that accurately represents your business domain, reduces maintenance overhead, and enables powerful cross-functional workflows.
| Anti-pattern | Description | Solution |
|-------------|-------------|----------|
| [System Silos](#anti-pattern-system-silos) | Creating separate object types for each source system. | Merge data in pipelines; create unified object types. |
| [The Kitchen Sink](#anti-pattern-the-kitchen-sink) | Including unnecessary technical columns as properties. | Curate properties intentionally; exclude ETL metadata. |
| [Department Silos](#anti-pattern-department-silos) | Each department creates their own version of shared entities. | Create shared object types; use properties and links for department-specific data. |
| [The God Object](#anti-pattern-the-god-object) | One object type represents multiple distinct entities. | Create distinct object types; use interfaces for shared characteristics. |
| [The Golden Hammer](#anti-pattern-the-golden-hammer) | Relying too heavily on a single tool (action types, pipelines, or functions, for example) for every problem instead of choosing the right capability. | Match the tool to the job: batch or streaming pipelines for data processing, actions for human decisions, automations for event-driven reactions, functions for complex real-time logic. |
| [Action Sprawl](#anti-pattern-action-sprawl) | Creating many single-property actions instead of cohesive business operations. | Design actions around business operations that bundle related changes into meaningful workflows. |
| [The Time Machine](#anti-pattern-the-time-machine) | Modeling historical versions as separate objects or object types. | Use a single object per entity with linked history/amendment objects and time series properties. |
| [The Misnomer](#anti-pattern-the-misnomer) | Using vague, generic, or misleading names for Ontology elements.	| Use specific, descriptive names; qualify ambiguous properties; name links by relationship. |
## Anti-pattern: System Silos
System Silos（系统孤岛）发生在您根据数据来源系统而非实体本身，为同一现实世界实体创建单独的 object type 时。

System Silos occur when you create separate object types for the same real-world entity based on the source system the data originates from, rather than modeling the entity itself.
### Common causes
* 不同团队拥有不同的源系统并独立构建
* 对如何合并来自多个源的数据存在不确定性
* 希望保留系统特定的字段，而无需决定哪些是必需的

* Different teams own different source systems and build independently
* Uncertainty about how to merge data from multiple sources
* Desire to preserve system-specific fields without deciding what's essential
### Example
您的组织在三个系统中拥有员工数据：HR 系统、门禁系统和项目管理工具。您没有创建一个单一的 `Employee` object type，而是创建了：

Your organization has employee data in three systems: an HR system, a badge access system, and a project management tool. Instead of creating a single `Employee` object type, you create:
* `HR System Employee`
* `Badge System Employee`
* `Project Management Employee`
* `HR System Employee`
* `Badge System Employee`
* `Project Management Employee`
### Problems
| Problem | Impact |
|---------|--------|
| Fragmented view of reality | End users cannot see a unified view of an employee; they must navigate multiple object types to understand the full picture. |
| Duplicated effort | Action types, link types, and applications must be built multiple times for what is conceptually the same entity. |
| Inconsistent data | The same employee may have conflicting information across object types with no clear source of truth. |
| Complex maintenance | Changes to business logic must be replicated across all system-specific object types. |
### Solution
创建一个代表现实世界实体的单一 object type，并使用 data pipelines 将来自多个源系统的信息合并到一个统一的 backing dataset 中。

Create a single object type representing the real-world entity and use data pipelines to merge information from multiple source systems into a unified backing dataset.
```
✗ Avoid                          ✓ Prefer
─────────────────────────────    ─────────────────────────────
HR System Employee               Employee
Badge System Employee         →  (backed by merged dataset
Project Management Employee      from all three systems)
```
要实现这一点：

To implement this:
1. 确定跨系统唯一标识实体的主键（例如，员工 ID）。

2. 构建一个 transform，将来自所有源系统的数据连接起来。
3. 为冲突值定义明确的优先级规则（例如，HR 系统是职位的权威来源）。

4. 创建一个由合并后的 dataset 支持的单一 object type。

1. Identify the primary key that uniquely identifies the entity across systems (for example, employee ID).
2. Build a transform that joins data from all source systems.
3. Define clear precedence rules for conflicting values (for example, HR system is authoritative for job title).
4. Create a single object type backed by the merged dataset.
***
## Anti-pattern: The Kitchen Sink
这种反模式（也称为"everything but the kitchen sink"）发生在 object type 包含来自外部系统的无关紧要的列时，这些列在 Ontology 上下文中没有任何业务相关性，从而用技术性冗余数据使数据模型变得杂乱。

This anti-pattern (also known as "everything but the kitchen sink") occurs when object types include unnecessary columns from external systems that have no business relevance in the Ontology context, cluttering the data model with technical artifacts.
### Common causes
* "以防万一"的心态（保留以后可能有用的字段）
* 缺乏对哪些字段有意义的明确性
* 直接从源系统映射而无需筛选整理
* 担心通过排除列而丢失数据

* "Just in case" mentality (keeping fields that might be useful later)
* Lack of clarity on what fields are meaningful
* Direct mapping from source systems without curation
* Fear of losing data by excluding columns
### Example
当从 CRM 系统集成的数据创建 `Customer` object type 时，您包含了所有可用的列：

When creating a `Customer` object type from a CRM system integration, you include all available columns:
* customer\_id ✓
* customer\_name ✓
* email ✓
* \_crm\_extracted\_at ✗
* \_crm\_received\_at ✗
* \_crm\_batched\_at ✗
* \_crm\_sequence ✗
* \_crm\_table\_version ✗
* \_crm\_internal\_record\_id ✗
* last\_etl\_update\_timestamp ✗
* customer\_id ✓
* customer\_name ✓
* email ✓
* \_crm\_extracted\_at ✗
* \_crm\_received\_at ✗
* \_crm\_batched\_at ✗
* \_crm\_sequence ✗
* \_crm\_table\_version ✗
* \_crm\_internal\_record\_id ✗
* last\_etl\_update\_timestamp ✗
### Problems
| Problem  | Impact |
|----------|--------|
| Confusion  | End users see irrelevant technical fields alongside business data.  |
| Performance degradation  | Unnecessary properties increase data scale, compute, index size, and slow down searches.  |
| Obscured insights | Important business properties are buried among system metadata.  |
### Solution
有意地筛选整理 properties。仅包含具有明确业务含义并将用于 workflow 的列。

Curate properties intentionally. Only include columns that have clear business meaning and will be useful for workflows.
在决定包含哪些 properties 时，请使用以下准则：

Use these guidelines when deciding which properties to include:
| Include  | Exclude  |
|----------|----------|
| Business identifiers (customer ID, order number) | Pipeline metadata |
| Human-readable attributes (name, description) | Internal system IDs with no business meaning |
| Dates relevant to business processes | Timestamps only relevant to data engineering |
| Status fields needed for filtering or actions | Audit columns for pipeline debugging |
要实现这一点：

To implement this:
1. 审查每一列并问："是否有人需要查看、搜索或按此筛选？"

2. 将技术性元数据保留在 backing dataset 中用于调试，但不要将其暴露为 properties。

3. 使用 property visibility 设置隐藏那些必须存在但很少需要的边界情况 properties。

4. 记录每个 property 存在的原因以及谁在使用它。

1. Review each column and ask: "Would someone ever need to see, search, or filter by this?"
2. Keep technical metadata in the backing dataset for debugging, but do not expose it as properties.
3. Use property visibility settings to hide any borderline properties that must exist but are rarely needed.
4. Document why each property exists and who uses it.
***
## Anti-pattern: Department Silos
部门孤岛（Department Silos）发生在不同部门创建同一 object type 的各自版本时，导致 Ontology 碎片化，镜像组织结构而非业务现实。

Department Silos occur when different departments create their own versions of the same object type, leading to a fragmented Ontology that mirrors organizational structure rather than business reality.
### Common causes
* 各部门孤立运作，缺乏跨职能协同
* 每个团队都认为其对客户的理解是独一无二的

* 缺乏治理或中央 Ontology 设计权威
* 团队希望对"其"数据拥有自治权和控制权

* Departments work in isolation without cross-functional coordination
* Each team believes their view of the customer is unique
* Lack of governance or central Ontology design authority
* Teams want autonomy and control over "their" data
### Example
多个部门需要使用客户数据，并且每个部门都创建自己的 Object Type：

Multiple departments need to work with customer data, and each creates their own object type:
* 销售团队创建 `Sales Customer`

* 支持团队创建 `Support Customer`

* 财务团队创建 `Billing Customer`

* 营销团队创建 `Marketing Contact`

* Sales team creates `Sales Customer`
* Support team creates `Support Customer`
* Finance team creates `Billing Customer`
* Marketing team creates `Marketing Contact`
这四个 Object Type 代表的都是同一个现实世界中的实体：客户。

All four object types represent the same real-world entity: a customer.
### Problems
| Problem | Impact |
|---------|--------|
| No single source of truth | Different departments have conflicting information about the same customer. |
| Impossible cross-functional workflows | Cannot easily answer questions like "Show me all interactions with this customer across sales, support, and billing". |
| Duplicated development | Each department builds redundant actions, links, and applications. |
| Governance nightmare | Data quality issues multiply; fixes in one object type do not propagate to others. |
### Solution
创建可服务多个部门的共享 Object Type，并使用 Property 和 Link 在需要时捕获部门特定信息。

Create shared object types that serve multiple departments, using properties and links to capture department-specific information where needed.
```
✗ Avoid                          ✓ Prefer
─────────────────────────────    ─────────────────────────────
Sales Customer                   Customer
Support Customer           →       ├── sales_status (property)
Billing Customer                   ├── support_tier (property)
Marketing Contact                  ├── billing_account_id (property)
└── Links to:
├── Sales Opportunities
├── Support Tickets
└── Invoices
```
实施方法：

To implement this:
1. 识别跨部门存在的实体。

2. 成立跨职能工作组以定义共享 Object Type。

3. 使用 Property 在共享 Object 上捕获部门特定属性。

4. 使用 Link Type 将共享 Object 连接到部门特定 Object（例如 `Customer` → `Support Ticket`）。

5. 如果部门需要对同一底层实体的不同"视图"，可利用 Object View 或经过策划的 Workshop 和 OSDK 应用。

6. 如果特定 Property 仅限特定团队访问，可使用 Restricted View。

1. Identify entities that exist across departmental boundaries.
2. Establish a cross-functional working group to define shared object types.
3. Use properties to capture department-specific attributes on shared objects.
4. Use link types to connect shared objects to department-specific objects (such as `Customer` → `Support Ticket`).
5. Leverage object views or curated Workshop and OSDK applications if departments need different "views" of the same underlying entity.
6. Use restricted views if specific properties can only be accessible by a specific team.
***
## Anti-pattern: The God Object
God Object 反模式发生于当一个 Object Type 被过度使用以表示多个不同的现实世界实体，导致其臃肿、混乱且难以维护。

The God Object anti-pattern occurs when a single object type is overloaded to represent multiple distinct real-world entities, resulting in a bloated, confusing, and unmaintainable object type.
### Common causes
* 由表面相似性驱动的过度抽象（"它们都是资产"）

* 希望最小化 Object Type 数量的倾向
* 在构建之前缺乏明确的实体定义

* 随着更多用例被加入现有 Object Type 而导致的范围蔓延

* Over-abstraction driven by superficial similarities ("they are all assets")
* Desire to minimize the number of object types
* Lack of clear entity definitions before building
* Scope creep as more use cases are added to an existing object type
### Indicators
* Object Type 拥有许多经常为 null 的 Property

* Property 含义根据另一个 Property 的值而变化（例如 type 或 category）

* 在查看 Object 时发现自己会问"这是哪种 `[Object]`？"

* 业务规则和验证需要基于 Object "type" 的大量条件逻辑

* An object type has many properties that are frequently null
* Property meanings change based on another property's value (such as type or category)
* You find yourself asking "What kind of `[Object]` is this?" when viewing an object
* Business rules and validations require extensive conditional logic based on object "type"
### Example
你创建了一个 `Asset` Object Type，旨在表示"任何有价值的事物"，最终却包含了：

You create an `Asset` object type intended to represent "anything valuable," which ends up including:
* 物理设备（卡车、机械）
* 软件许可
* 房地产物业
* 金融工具
* 员工（作为"人力资产"）

* Physical equipment (trucks, machinery)
* Software licenses
* Real estate properties
* Financial instruments
* Employees (as "human assets")
该 Object Type 拥有 150+ 个 Property，其中大多数对于任何给定 Object 而言都是 null，并且像 value、location 和 status 这类 Property 的含义完全取决于 Object 所代表的"资产"类型。

The object type has 150+ properties, most of which are null for any given object, and the meaning of properties like value, location, and status varies completely depending on what kind of "asset" the object represents.
### Problems
| Problem | Impact |
|---------|--------|
| Semantic confusion | End users cannot understand what an `Asset` actually represents. |
| Sparse data | Most properties are null for most objects, making the data hard to interpret. |
| Impossible validation | Cannot enforce business rules because rules differ by entity type. |
| Poor search experience | Searching for `Assets` returns a mix of unrelated things. |
| Action type complexity | Actions must handle wildly different entity types with complex conditional logic. |
### Solution
为不同的现实世界实体创建不同的 Object Type。当实体确实共享共同 Property 或行为时，使用 Interface 来建模共享特征。

Create distinct object types for distinct real-world entities. Use interfaces to model shared characteristics when entities genuinely share common properties or behaviors.
```
✗ Avoid                          ✓ Prefer
─────────────────────────────    ─────────────────────────────
Asset                            Equipment
- asset_type                   Vehicle
- asset_subtype                Software License
- value                  →     Property (Real Estate)
- location                     Financial Instrument
- status
- 145 more properties...       Interface: Depreciable Asset
- purchase_date
- purchase_value
- depreciation_schedule
```
实施方法：

To implement this:
1. 列出当前由该 object type 表示的不同真实世界实体。

2. 为每个不同实体创建单独的 object type。

3. 识别真正共享的 property 和行为。

4. 使用 interface 对跨 object type 的共享特征进行建模。

5. 将现有 object 迁移到适当的新 object type。

1. List the distinct real-world entities currently represented by the object type.
2. Create separate object types for each distinct entity.
3. Identify genuinely shared properties and behaviors.
4. Use interfaces to model shared characteristics across object types.
5. Migrate existing objects to appropriate new object types.
***
## Anti-pattern: The Golden Hammer
Golden Hammer 反模式发生在你过度依赖单一工具去解决每个问题时，即使其他方法更为合适。其名称源自于谚语：["If all you have is a hammer, everything looks like a nail" ↗](https://en.wikipedia.org/wiki/Law_of_the_instrument)。

The Golden Hammer anti-pattern occurs when you rely too heavily on a single tool to solve every problem, even when other approaches are more appropriate. The name comes from the saying: ["If all you have is a hammer, everything looks like a nail" ↗](https://en.wikipedia.org/wiki/Law_of_the_instrument).
此反模式表现为：对更适合用 pipeline 完成的工作过度使用 action type，为本应是事件驱动 automation 的逻辑构建 pipeline，或为本可在 transform 中预先计算的计算编写 function。

This anti-pattern manifests in the overuse of action types in work better suited for pipelines, building pipelines for logic that should be event-driven automations, or writing functions for calculations that are better pre-computed in a transform.
### Common causes
* 因团队中对该工具的熟悉度和可见度而过度依赖
* 希望让终端用户"掌控"计算发生的时机

* 对完整平台（包括 pipeline、automation、function 和 scheduled build）缺乏了解

* 仅在一个层面进行思考（Ontology 优先、pipeline 优先或 code 优先），而未考虑完整的工具集

* Overreliance on a tool due to familiarity and visibility within the team
* Desire to give end users "control" over when computations happen
* Lack of familiarity with the full platform (including pipelines, automations, functions, and scheduled builds)
* Thinking exclusively in one layer (Ontology-first, pipeline-first, or code-first) without considering the full toolkit
### Examples
**过度依赖 action type：**

**Overreliance on action types:**
你需要为仪表板计算按区域显示总销售额的聚合 metric。你没有使用 data pipeline 来预先计算这些 metric，而是创建了一个名为 `Calculate Regional Sales Totals` 的 action type，要求终端用户手动触发。结果通过该 action 写回 object。

You need to calculate aggregate metrics for a dashboard showing total sales by region. Instead of using a data pipeline to pre-compute these metrics, you create an action type called `Calculate Regional Sales Totals` that end users must manually trigger. Results are written back to objects via the action.
**过度依赖 pipeline：**

**Overreliance on pipelines:**
当传感器读数超过阈值时，由 pipeline 创建一个 alert object。你希望自动将该 alert 分派给 on-call 工程师并发送通知。你没有使用响应新 object 的 automation，而是构建了额外的 pipeline 逻辑，尝试解析被分派人并将分派结果写入底层 dataset，将 operational workflow 逻辑混入 data integration。

An alert object is created by a pipeline when sensor readings exceed a threshold. You want to automatically assign that alert to the on-call engineer and send a notification. Instead of using an automation that reacts to the new object, you build additional pipeline logic that tries to resolve the assignee and write the assignment into the backing dataset, mixing operational workflow logic into data integration.
**过度依赖 function：**

**Overreliance on functions:**
你将类似 `full_name` = `first_name` + `last_name` 的简单 property 派生实现为 function-backed column，增加了运行时开销和需要维护的 code repository，而单个 pipeline 的 `concat` 表达式就足以完成。

You implement a simple property derivation like `full_name` = `first_name` + `last_name` as a function-backed column, adding runtime overhead and a code repository to maintain, when a single pipeline `concat` expression would suffice.
### Problems
| Problem | Impact |
|---------|--------|
| Scalability limits | Each tool has different execution limits; using the wrong one hits ceilings early. |
| Unnecessary complexity | Maintaining logic in the wrong layer increases the number of moving parts. |
| User burden | End users must perform steps that the platform could handle automatically. |
| Performance issues | Real-time calculations via actions or functions are slower than pre-computed pipeline results. Conversely, scheduled pipelines are too slow for event-driven reactions. |
| Difficult debugging | When logic lives in the wrong layer, failures are harder to diagnose and resolve. |
### Solution
根据用例为工作选择合适的工具：

Choose the right tool for the job based on your use case:
| Tool | Best for | Not ideal for |
|------|----------|---------------|
| Action types | Human decisions, user-initiated edits to one or a few objects, input-driven changes that should apply immediately. | Batch calculations, scheduled updates, event-driven reactions with no human involvement. |
| Pipelines (batch) | Batch data processing, aggregations, cleansing, enrichment, pre-computing derived values on a schedule or on data arrival. | Real-time reactions to individual object changes, logic that requires human input. |
| Pipelines (streaming) | Continuous, low-latency data processing where results must stay current as source data arrives (real-time dashboards, live status tracking, continuous enrichment). | Infrequent updates where batch is sufficient, logic that requires human input, reacting to Ontology-level events (use automations). |
| Automations | Event-driven reactions to Ontology changes (object created, property updated, schedule triggered), orchestrating actions or notifications without user involvement. | Heavy data processing, complex multi-dataset joins, logic that requires human judgment. |
| Functions | Complex real-time computations across multiple objects, validation logic, derived values that depend on live Ontology state and cannot be pre-computed. | Simple derivations computable in a pipeline, batch processing of large datasets. |
| Schedules | Recurring pipeline builds, time-based or event-based orchestration of data refresh. | Reacting to individual object-level changes in real time. |
应用此指导的示例：

Examples of applying this guidance:
```
✗ Avoid                                          ✓ Prefer
──────────────────────────────────────────────   ──────────────────────────────────────────────
Action: "Calculate Regional Sales"          →    Pipeline that aggregates sales data daily
into a "Regional Sales Summary" object type.

Action: "Standardize Address Format"        →    Pipeline that cleanses addresses on ingestion.

Action: "Update Inventory Status"           →    Pipeline that sets status based on quantity
(based on quantity thresholds)                   thresholds during each sync.

Action: "Assign Risk Score"                 →    Pipeline or model that calculates risk scores
(using a formula)                                and writes to the backing dataset.

Pipeline that assigns alerts to on-call     →    Automation that triggers an "Assign Alert"
engineers by writing to the backing dataset      action when a new "Alert" object is created.

Pipeline that sends a notification when     →    Automation that monitors for the condition
an object meets a condition                      and sends a notification or triggers an action.

Batch pipeline polling every minute for     →    Streaming pipeline that continuously processes
new IoT sensor readings                          sensor data as it arrives.

Function-backed column for                  →    Pipeline that computes full_name = first_name
full_name = first_name + " " + last_name         + " " + last_name in the backing dataset.

Scheduled pipeline running every minute     →    Automation that reacts to the specific object
to check for objects needing follow-up           change and triggers the follow-up immediately.
```
要实施此做法：

To implement this:
1. **在创建 action type 之前**，先问："这是否需要人工判断或用户输入？" 如果不需要，它很可能应该放在 pipeline 或 automation 中。

2. **在为 pipeline 添加逻辑之前**，先问："这是 data transformation，还是 operational workflow？" 数据清洗、聚合和 enrichment 属于 pipeline；分派工作、发送通知以及响应单个变更属于 automation。

3. **在编写 function 之前**，先问："这是否可以在底层 pipeline 中预先计算？" 如果结果仅依赖于源 data column 并且不需要实时的 Ontology 遍历，那么应在上游进行计算。

4. **在构建轮询 pipeline 之前**（每 N 分钟运行一次以检测变更），先问："automation 是否可以直接响应该事件？" Automation 几乎可以实时响应 Ontology 的变更，而无需 scheduled build 的开销。如果需求是来自源系统的持续数据处理，则应考虑 streaming pipeline。

5. **在默认使用 batch pipeline 之前**，先问："此数据是否需要持续保持最新？" 如果消费者依赖低延迟的新鲜度，streaming pipeline 可以避免 batch 调度带来的折衷。

6. **使用 automation** 来桥接"发生了变更"和"应该执行某操作"之间的差距，而无需用户点击按钮或轮询 pipeline。

1. **Before creating an action type**, ask: "Does this require human judgment or user input?" If not, it likely belongs in a pipeline or automation.
2. **Before adding logic to a pipeline**, ask: "Is this a data transformation, or is it an operational workflow?" Data cleansing, aggregation, and enrichment belong in pipelines. Assigning work, sending notifications, and reacting to individual changes belong in automations.
3. **Before writing a function**, ask: "Can this be pre-computed in the backing pipeline?" If the result only depends on source data columns and does not need live Ontology traversal, compute it upstream.
4. **Before building a polling pipeline** (running every N minutes to detect changes), ask: "Can an automation react to this event directly?" Automations respond to Ontology changes in near-real-time without the overhead of scheduled builds. If the need is for continuous data processing from a source system, consider a streaming pipeline instead.
5. **Before defaulting to a batch pipeline**, ask: "Does this data need to be continuously current?" If consumers depend on low-latency freshness, a streaming pipeline avoids the compromise of a batch schedule.
6. **Use automations** to bridge the gap between "something changed" and "something should happen", without requiring a user to click a button or poll a pipeline.
***
## Anti-pattern: Action Sprawl
Action Sprawl 发生在你创建大量范围狭窄的 action type、每个仅修改单个 property 时，而不是设计代表有意义业务操作的内聚 action。

Action Sprawl occurs when you create many narrowly-scoped action types that each modify a single property, rather than designing cohesive actions that represent meaningful business operations.
### Common causes
* 将 Action 视为数据库列更新而非业务操作

* 增量构建 Action 而未考虑整体用户体验

* 缺乏对 Action 如何捆绑多个 Property 变更的理解

* 模仿传统应用程序开发中的 CRUD 操作

* Thinking of actions as database column updates rather than business operations
* Building actions incrementally without considering the overall user experience
* Lack of understanding of how actions can bundle multiple property changes
* Mimicking CRUD operations from traditional application development
### Indicators
* 单一 Object Type 拥有超过 10 个 Action Type

* 多个总是按顺序执行的 Action

* Action 名称读起来像 `Set [Property]` 或 `Update [Property]`
* 终端用户抱怨完成任务需要太多步骤

* More than 10 action types for a single object type
* Multiple actions that are always performed in sequence
* Action names that read like `Set [Property]` or `Update [Property]`
* End users complaining about too many steps to complete a task
### Example
对于 `Employee` Object Type，你没有创建有意义的业务 Action，而是创建了：

For an `Employee` object type, instead of creating meaningful business actions, you create:
* `Update Employee First Name`
* `Update Employee Last Name`
* `Update Employee Email`
* `Update Employee Phone`
* `Update Employee Department`
* `Update Employee Manager`
* ……以及另外 20 多个单 Property 的 Action

* `Update Employee First Name`
* `Update Employee Last Name`
* `Update Employee Email`
* `Update Employee Phone`
* `Update Employee Department`
* `Update Employee Manager`
* ...and 20 more single-property actions
### Problems
| Problem | Impact |
|---------|--------|
| Overwhelming experience | End users face a long, cluttered list of actions and struggle to find the right one. |
| Fragmented workflows | Simple updates require multiple action submissions to complete a single business task. |
| No cohesive business representation | Actions do not map to real-world processes, making the Ontology unintuitive. |
| Fragmented audit trails | History of changes is scattered across many small actions, making it difficult to understand what happened and why. |
### Solution
围绕业务操作而非数据库更新来设计 Action Type。创建能够将相关变更捆绑为有意义工作流的 Action。

Design action types around business operations, not database updates. Create actions that bundle related changes into meaningful workflows.
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Update Employee First Name                 Update Employee Contact Information
Update Employee Last Name            →       - first_name
Update Employee Email                        - last_name
Update Employee Phone                        - email
- phone

Update Employee Department                 Transfer Employee to New Department
Update Employee Manager              →       - new_department
Update Employee Location                     - new_manager
- new_location
- effective_date

Create Employee Record                     Onboard New Employee
Set Employee Start Date              →       - All required fields for a new hire
Assign Employee Badge                        - Triggers downstream workflows
Assign Employee Equipment                    (badge assignment, equipment request)
```
要实现这一点：

To implement this:
1. 梳理涉及 Object 数据变更的真实业务流程。

2. 将相关的 Property 变更分组成单一 Action，以表示这些流程。

3. 使用 Action 参数，允许在同一个内聚 Action 中包含可选字段。

4. 以业务操作命名 Action：`Transfer Employee`、`Approve Purchase Order`、`Escalate Support Ticket`。

5. 使用 Action 规则和验证逻辑在 Action 内部强制执行业务约束。

1. Map out the real business processes that involve changing object data.
2. Group related property changes into single actions that represent those processes.
3. Use action parameters to allow optional fields within a cohesive action.
4. Name actions after the business operation: `Transfer Employee`, `Approve Purchase Order`, `Escalate Support Ticket`.
5. Use action rules and validation logic to enforce business constraints within the action.
***
## Anti-pattern: The Time Machine
Time Machine 反模式指的是将实体的历史版本建模为单独的 Object 或 Object Type，而不是使用时序数据、快照或适当的版本控制策略。

The Time Machine anti-pattern occurs when you model historical versions of an entity as separate objects or object types rather than using time series data, snapshots, or proper versioning strategies.
### Common causes
* 希望保留每一次变更的完整历史记录

* 误解了如何在 Ontology 中建模时态数据

* 将文件版本控制的思维模型（v1、v2、v3）应用于 Object 设计

* 缺乏对时序 Property 或链接历史模式的了解

* Desire to preserve a complete history of every change
* Misunderstanding of how to model temporal data in the Ontology
* Applying file-versioning mental models (v1, v2, v3) to object design
* Lack of awareness of time series properties or linked history patterns
### Indicators
* Object Type 包含多个 Object，表示同一现实世界实体在不同时间点的状态

* 存在 version、revision 或 is_current 等 Property 来区分副本

* Object 数量随变更次数而非实体数量成比例增长

* 终端用户对应该引用或链接到哪个 Object 感到困惑

* Object type contains multiple objects representing the same real-world entity at different points in time
* Properties like version, revision, or is\_current exist to distinguish copies
* Object counts grow proportionally with the number of changes rather than the number of entities
* End users are confused about which object to reference or link to
### Example
为了跟踪 `Contract` 的变更，你创建了：

To track changes to a `Contract`, you create:
* 在同一 Object Type 中，将 `Contract v1`、`Contract v2`、`Contract v3` 创建为单独的 Object

* 更糟糕的是：按年份为每年创建单独的 Object Type，如 `Contract 2023`、`Contract 2024`、`Contract 2025`

* `Contract v1`, `Contract v2`, `Contract v3` as separate objects within the same object type
* Or worse: `Contract 2023`, `Contract 2024`, `Contract 2025` as separate object types for each year
每个"版本"都是 Contract 的完整副本，Property 值略有不同，并且到其他 Object（如 `Vendor` 或 `Department`）的 Link 会在所有版本中重复。

Each "version" is a full copy of the contract with slightly different property values, and links to other objects (such as `Vendor` or `Department`) are duplicated across all versions.
### Problems
| Problem | Impact |
|---------|--------|
| Object count explosion | Every change creates a new object, rapidly inflating the Ontology with redundant data. |
| Ambiguous current state | It is difficult to identify which version is the "current" or authoritative version. |
| Ambiguous links | Links to contracts become unclear; which version should a `Vendor` or `Department` link to? |
| Complex reporting | Reporting across time periods requires filtering and deduplication logic that is error-prone. |
### Solution
对每个实体使用单一 Object，并使用 Property 表示当前状态。将历史变更存储在单独的链接 Object Type 中，启用编辑历史记录，或利用时序 Property。

Use a single object per entity with properties for current state. Store historical changes in a separate linked object type, enable edits history, or leverage time series properties.
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Contract v1 (object)                       Contract (single object per contract)
Contract v2 (object)                 →       - current_value
Contract v3 (object)                         - current_status
- effective_date
— OR —                                       - Links to:
└── Contract Amendments
Contract 2023 (object type)                        - amendment_date
Contract 2024 (object type)                        - previous_value
Contract 2025 (object type)                        - new_value
- change_reason
```
要实现这一点：

To implement this:
1. 每个真实世界实体使用单一 Object，并通过 Property 反映其当前状态。

2. 创建一个单独链接的 Object Type（如 `Contract Amendment` 或 `Contract History`）以捕获历史变更。

3. 对于频繁变化且需要时间跟踪的值，利用时序 Property（time series properties）。

4. 如有需要，使用 backing dataset 或 edits history 来维护完整的历史记录以供审计追踪。

1. Use a single object per real-world entity with properties reflecting the current state.
2. Create a separate linked object type (such as `Contract Amendment` or `Contract History`) to capture historical changes.
3. Leverage time series properties for values that change frequently and need temporal tracking.
4. Use the backing dataset or edits history to maintain full historical records for audit trails if needed.
***
## Anti-pattern: The Misnomer
Misnomer 反模式发生在你为 Object Type、Property 和 Link Type 使用模糊、通用或具有误导性的名称时，这些名称无法清晰地传达其含义，从而在整个 Ontology 中造成混淆和误解。

The Misnomer anti-pattern occurs when you use vague, generic, or misleading names for object types, properties, and link types that do not clearly communicate their meaning, leading to confusion and misinterpretation across the Ontology.
### Common causes
* 使用对你自己有意义但对他人无意义的简写名称
* 名称直接从源系统列名沿用而未进行翻译
* 追求简洁胜过清晰
* 缺乏命名规范或治理标准
* 假设上下文会使含义不言自明

* Using shorthand names that make sense to you but not to others
* Names are carried over directly from source system column names without translation
* Desire for brevity over clarity
* Lack of naming conventions or governance standards
* Assumption that context will make meaning obvious
### Indicators
* 最终用户经常询问 "这个 Property 是什么意思？" 或 "这是什么类型的 `[Object]`？"
* 同一个名称可能合理地指代多个不同的概念

* Property 名称是单一的通用词，如 `value`、`type`、`status`、`date` 或 `name`，没有任何限定

* Link Type 使用通用标签，如 "related to"，而不具体说明关系的性质

* End users frequently ask "What does this property mean?" or "What kind of `[Object]` is this?"
* The same name could reasonably refer to multiple different concepts
* Property names are single generic words like `value`, `type`, `status`, `date`, or `name` without qualification
* Link types use generic labels like "related to" without specifying the nature of the relationship
### Example
你使用含糊不清的名称创建了以下 Ontology 元素：

You create the following Ontology elements with ambiguous names:
* Object Type：`Item`（什么类型的 item？产品？订单明细？库存项目？）

* Property：`value`（货币价值？数量？分数？评级？）

* Property：`type`（什么的类型？有效值是什么？）

* Property：`date`（创建日期？修改日期？截止日期？生效日期？）

* Link Type：`Item` → `Related Item`（它们是如何关联的？父子关系？替代品？配件？）

* Object type: `Item` (What kind of item? Product? Line item? Inventory item?)
* Property: `value` (Monetary value? Quantity? Score? Rating?)
* Property: `type` (Type of what? What are valid values?)
* Property: `date` (Created date? Modified date? Due date? Effective date?)
* Link type: `Item` → `Related Item` (How are they related? Parent-child? Substitute? Accessory?)
遇到这些名称的最终用户必须猜测其含义，或深入查阅文档以理解数据实际代表的内容。

End users encountering these names must guess at their meaning or dig into documentation to understand what the data actually represents.
### Problems
| Problem | Impact |
|---------|--------|
| Misinterpretation | End users cannot understand the Ontology without additional context, leading to incorrect analysis and decisions. |
| Steep learning curve | New team members must spend significant time learning what vague names actually mean. |
| Documentation dependency | Documentation becomes essential rather than supplementary, and falls out of date quickly. |
| Cross-team confusion | Different teams interpret the same vague names differently, leading to inconsistent usage. |
### Solution
为所有 Ontology 元素使用具体、描述性的名称。名称应当是自解释的（self-documenting），以便任何人都能在没有额外上下文的情况下理解其含义。

Use specific, descriptive names for all Ontology elements. Names should be self-documenting so that anyone can understand meaning without additional context.
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Object type: Item                    →     Object type: Product
Object type: Sales Order Line Item
Object type: Warehouse Inventory Record

Property: value                      →     Property: monetary_value
Property: quantity_on_hand
Property: risk_score

Property: type                       →     Property: product_category
Property: service_tier

Property: date                       →     Property: order_placed_date
Property: contract_effective_date

Link: Item → Related Item            →     Link: Product → Purchasing Customer
Link: Employee → Supervisor
Link: Equipment → Manufacturing Facility
```
要实施此原则：

To implement this:
1. 在构建之前建立命名规范，并通过治理审查加以执行。

2. 使用具体、描述性的名称：`Product`、`Sales Order Line Item`、`Warehouse Inventory Record`。

3. 对含义模糊的 Property 加以限定：`monetary_value`、`quantity_on_hand`、`risk_score`。

4. 用解释关系的名称命名 Link：`Purchasing Customers`、`Manufacturing Facility`、`Supervisor`。

5. 为所有 Ontology 元素添加描述，说明其含义和有效值。
6. 与最终用户一起审查名称，确保它们直观且无歧义。

1. Establish naming conventions before building and enforce them through governance reviews.
2. Use specific, descriptive names: `Product`, `Sales Order Line Item`, `Warehouse Inventory Record`.
3. Qualify ambiguous properties: `monetary_value`, `quantity_on_hand`, `risk_score`.
4. Name links explaining the relationship: `Purchasing Customers`, `Manufacturing Facility`, `Supervisor`.
5. Add descriptions to all Ontology elements explaining their meaning and valid values.
6. Review names with end users to ensure they are intuitive and unambiguous.
## Building a successful Ontology
本指南中描述的反模式很常见但完全可以避免。通过专注于基本的最佳实践（对现实进行建模而非对系统进行建模、有意策划 Property、跨团队协作、为每个任务选择合适的工具），你可以构建一个能够随组织需求扩展的 Ontology。

The anti-patterns described in this guide are common but avoidable. By focusing on the fundamental best practices (modeling reality rather than systems, curating properties intentionally, collaborating across teams, and choosing the right tools for each task), you can build an Ontology that scales with your organization's needs.
请记住，有效的 Ontology 设计是迭代的。从清晰的实体定义开始，尽早让利益相关者参与进来，并在你了解什么有效时不断完善你的模型。当你遇到挑战时，重新审视本指南中的原则，以确定是否可能正在出现反模式，并在变得难以改变之前及时修正方向。

Remember that effective Ontology design is iterative. Start with clear entity definitions, involve stakeholders early, and refine your model as you learn what works. When you encounter challenges, revisit the principles in this guide to identify whether an anti-pattern may be emerging and course-correct before it becomes difficult to change.