<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/ontology-best-practices/
---
# Ontology design: Best practices
设计良好的 Ontology 创建了一个统一、直观的组织表示，能够实现无缝的数据集成、跨职能协作和强大的分析功能。本节既提供了一套快速参考的设计指南，也对支撑这些指南的核心设计原则进行了更深入的阐述。

A well-designed Ontology creates a unified, intuitive representation of your organization that enables seamless data integration, cross-functional collaboration, and powerful analytics. This section provides both a quick-reference set of design guidelines and a deeper treatment of the core design principles that underpin them.
## Design guidelines
以下指南是 Ontology 设计的实用清单。在适用的情况下，每一条都基于一个[核心设计原则](#core-design-principles)、[反模式](/docs/foundry/ontology/ontology-anti-patterns/)或[结构建议](/docs/foundry/ontology/ontology-structural-guidance/)。

The following guidelines are a practical checklist for Ontology design. Where applicable, each one is grounded in a [core design principle](#core-design-principles), [anti-pattern](/docs/foundry/ontology/ontology-anti-patterns/), or [structural recommendation](/docs/foundry/ontology/ontology-structural-guidance/).
1. **对现实建模，而非对系统建模：** Object Type 应代表真实世界的实体，而非单个源系统或部门的表示。

* **设计原则：** [领域驱动设计](#1-domain-driven-design)

2. **有意策划：** 每个 Property 都应具有明确的业务或技术价值。

* **结构建议：** [规范化和派生 Property](/docs/foundry/ontology/ontology-structural-guidance/#normalization-and-derived-properties)

3. **跨团队协作：** Ontology 设计应让多个部门或团队的利益相关者参与。孤立的团队是导致重复的主要原因。

* **设计原则：** [不要重复你自己](#2-dont-repeat-yourself-rule-of-three)

4. **保持 Object Type 的专注：** 每个 Object Type 应代表一个不同的实体。

* **设计原则：** [领域驱动设计](#1-domain-driven-design)

5. **选择合适的工具：** 使用 Action Type 来处理人工或代理决策，使用 Pipeline 进行自动化转换。

* **反模式：** [The Golden Hammer](/docs/foundry/ontology/ontology-anti-patterns/#anti-pattern-the-golden-hammer)

6. **使用 Interface 进行抽象：** 当实体共享共同特征时，使用 Interface 对抽象进行建模，而不是创建宽泛而稀疏的 Object Type。

* **设计原则：** [组合优于深层继承层次结构](#4-composition-over-deep-hierarchies)

7. **记录你的决策：** 在 Ontology Manager 中记录 Object Type、Property 和 Link。

1. **Model reality, not systems:** Object types should represent real-world entities, not individual source system or department representations.
* **Design principle:** [Domain-driven design](#1-domain-driven-design)
2. **Curate intentionally:** Every property should have clear business or technical value.
* **Structural recommendation:** [Normalization and derived properties](/docs/foundry/ontology/ontology-structural-guidance/#normalization-and-derived-properties)
3. **Collaborate across teams:** Ontology design should involve stakeholders from multiple departments or teams. Siloed teams are a leading cause of duplication.
* **Design principle:** [Don't repeat yourself](#2-dont-repeat-yourself-rule-of-three)
4. **Keep object types focused:** Each object type should represent one distinct entity.
* **Design principle:** [Domain-driven design](#1-domain-driven-design)
5. **Choose the right tool:** Use action types for human or agentic decisions and pipelines for automated transformations.
* **Anti-pattern:** [The Golden Hammer](/docs/foundry/ontology/ontology-anti-patterns/#anti-pattern-the-golden-hammer)
6. **Use interfaces for abstraction:** When entities share common characteristics, model the abstraction with interfaces rather than creating wide, sparse object types.
* **Design principle:** [Composition over deep hierarchies](#4-composition-over-deep-hierarchies)
7. **Document your decisions:** Document object types, properties, and links in Ontology Manager.
## Core design principles
这四条原则源自政府和商业实施中广泛的现场经验。它们按优先级顺序呈现。在发生冲突的情况下，优先级更高的原则优先。

These four principles are derived from extensive field experience across government and commercial implementations. They are presented in priority order. In cases of conflict, higher-priority principles take precedence.
| Priority | Principle | Core idea |
|-------------|-------------|----------|
|1	|[Domain-driven design](#1-domain-driven-design)	|Model the real world, not the source data.|
|2	|[Don't repeat yourself](#2-dont-repeat-yourself-rule-of-three)	|If you built the same thing three times, refactor.|
|3	|[Open for extension, closed for modification](#3-open-for-extension-closed-for-modification)	|Protect core models. Enable builders to extend them.|
|4	|[Composition over deep hierarchies](#4-composition-over-deep-hierarchies)	|Favor multiple inheritance via interfaces. Keep things pluggable.|
实际考量应始终纳入任何决策。请参阅 [务实与权衡](#pragmatism-and-tradeoffs) 部分以获取更多信息。

Practical considerations should always factor into any decision. Review the section on [pragmatism and tradeoffs](#pragmatism-and-tradeoffs) for more information.
### 1. Domain-driven design

> 📷 **[图片: 1-Domain Design]**

> 📷 **[图片: 1-Domain Design]**

**Ontology 建模的是现实世界，而不是源数据。**

**The Ontology models the real world, not the source data.**
Object 应该表示语义上有意义的现实世界概念（例如 `Patient`、`WorkOrder` 或 `Vessel`），而不是数据库表、API 响应或电子表格标签页。Link 应该表示真实的关系（"该患者访问过该机构"），而不是连接键或外键产物。

Objects should represent semantically meaningful real-world concepts (such as a `Patient`, a `WorkOrder`, or a `Vessel`) not database tables, API responses, or spreadsheet tabs. Links should represent real relationships ("this patient visited this facility"), not join keys or foreign key artifacts.
当被要求"将数据集本体化"时，要抵制将列 1:1 映射到 Property 并认为工作完成的冲动。[Kitchen Sink](/docs/foundry/ontology/ontology-anti-patterns/#anti-pattern-the-kitchen-sink) 反模式会产生一个镜像源系统 schema 怪癖而非有用语义的 Ontology。一个设计良好的 Ontology 应该使用起来直观；用户或 AI agent 应该能够毫无摩擦地浏览它，因为该结构匹配他们已经思考其领域的方式。

When asked to "ontologize a dataset", resist the urge to map columns 1:1 to properties and consider the work complete. The [Kitchen Sink](/docs/foundry/ontology/ontology-anti-patterns/#anti-pattern-the-kitchen-sink) anti-pattern produces an Ontology that mirrors source system schema quirks rather than useful semantics. A well-designed Ontology should feel intuitive to use; a user, or an AI agent, should be able to navigate it without friction, because the structure matches how they already think about their domain.
#### Anti-patterns
* Object Type 镜像源系统表而非领域实体

* Property 从源列进行 1:1 映射而未经策展

* 名称来自源系统约定（`dtLastInspMod`）而非业务语言（`lastInspectionDate`）

* Object Model 是通过查看数据而非理解领域来设计的

* 包含多个实体的单个源行被建模为单个 Object Type

* Object types mirror source system tables rather than domain entities
* Properties are mapped 1:1 from source columns without curation
* Names come from source system conventions (`dtLastInspMod`) rather than business language (`lastInspectionDate`)
* The object model was designed by looking at the data rather than understanding the domain
* A single source row containing multiple entities is modeled as a single object type
#### Example
一个包含列 `order_id`、`customer_name`、`customer_email`、`product_sku` 和 `quantity` 的 CSV 描述了至少三个现实世界实体，而不是一个：

A CSV with columns `order_id`, `customer_name`, `customer_email`, `product_sku`, and `quantity` describes at least three real-world entities, not one:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
OrderData                                  Order
- order_id                                 - order_id
- customer_name                            - quantity
- customer_email                →          - Links to → Customer, Product
- product_sku
- quantity                               Customer
- name
(One object type mirroring the CSV)          - email

Product
- sku

(Three object types modeling the domain)
```
#### Impact of anti-patterns
|Problem	|Impact|
|-|-|
|Unintuitive model	|Users and AI agents cannot navigate the Ontology naturally because the structure does not match how they think about the domain.|
|Fragile coupling to source	|Schema changes in source systems break Ontology consumers because the Ontology mirrors source structure rather than abstracting over it.|
|Missed relationships	|Entities embedded as columns (like `customer_name` on an order) cannot be linked, searched, or reasoned about independently.|
|Poor reuse	|Object types shaped by one system's schema are difficult for other teams or use cases to adopt.|
#### Best practices
1. **在查看源 schema 之前识别现实世界实体：** 与领域利益相关方合作定义哪些概念是重要的。单个数据集通常描述多个实体。

2. **将标识与观察分离：** 如果一行表示对某个实体的测量或事件，则该实体和该观察可能是不同的 Object Type。

3. **以人类友好的方式命名：** API 名称应该直观且自文档化。优先使用 `person.children` 而非 `person.linkedChildPersonObjects`。优先使用 `equipment.lastInspectionDate` 而非 `equipment.dtLastInspMod`。

4. **先建模领域，再映射数据：** 理解领域，然后设计 Object Model，然后将源数据映射到该模型中。不要试图查看数据并复制其形状。

5. **将非语义 Type 标记为 hidden：** 当特定工作流需要非语义 Type（用于技术目的而非对现实世界领域实体建模的 Type）时，将它们标记为 hidden，以保持 Ontology 的默认视图整洁。它们仍然可供 Builder 在构建应用程序时使用。

1. **Identify real-world entities before looking at source schemas:** Work with domain stakeholders to define what concepts matter. A single dataset often describes multiple entities.
2. **Separate identity from observation:** If a row represents a measurement or event about an entity, the entity and the observation are likely different object types.
3. **Name things for humans:** API names should be intuitive and self-documenting. Prefer `person.children` over `person.linkedChildPersonObjects`. Prefer `equipment.lastInspectionDate` over `equipment.dtLastInspMod`.
4. **Model the domain, then map the data:** Understand the domain, then design the object model, then map source data into that model. Do not attempt to look at the data and replicate its shape.
5. **Mark non-semantic types as hidden:** When non-semantic types (types that serve a technical purpose rather than modeling real-world domain entities) are necessary for specific workflows, mark them as hidden to keep default views of the Ontology clean. They remain available for builders to leverage when building applications.
### 2. Don't repeat yourself (rule of three)

> 📷 **[图片: 3-Don't Repeat]**

> 📷 **[图片: 3-Don't Repeat]**

**如果你构建了三次相同的东西，就重构它。**

**If you built the same thing three times, refactor.**
重复的 Object Type、多余的 Property 以及复制粘贴的工作流是一种维护负担和上下文管理问题，对于需要推理 Ontology 的人类和 AI agent 皆是如此。目标是每个概念都有一个规范的表示，每个针对该概念的操作都有一个规范的工作流。三次规则是应用此原则的实际触发条件：一次是巧合，两次是模式，三次意味着是时候重构了。

Duplicated object types, redundant properties, and copy-pasted workflows are a maintenance burden and a context-management problem, for both humans and AI agents that need to reason about the Ontology. The goal is a single canonical representation for each concept, with a single canonical workflow for each operation on that concept. The rule of three is a practical trigger for applying this principle: one instance is a coincidence, two is a pattern, and three means it is time to refactor.
#### Anti-patterns
* 多个 Object Type 共享相同的 Property 集和类似的 Link

* 相同的派生 Property 逻辑或 Action 逻辑出现在多个 Type 上

* 不同团队为略有不同的目的创建了几乎相同的 Object Type

* 复制粘贴的工作流跨 Type 存在微小变体

* Multiple object types share the same set of properties and similar links
* The same derived property logic or action logic appears across multiple types
* Different teams have created near-identical object types for slightly different purposes
* Copy-pasted workflows exist with minor variations across types
#### Example
三个团队独立创建了具有重叠 schema 的客户相关 Object Type：

Three teams have independently created customer-related object types with overlapping schemas:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Sales Customer                             Customer (single canonical type)
- name                                     - name
- email                                    - email
- phone                                    - phone
- sales_status
Support Customer                   →         - support_tier
- name                                     - billing_account_id
- email
- phone                                 — OR, if shapes are genuinely distinct —

Billing Customer                           Interface: CustomerBase
- name                                     - name
- email                                    - email
- phone                                    - phone

(Three types, three sets of actions,       Implemented by: SalesLead, SupportContact,
three maintenance burdens)                BillingAccount
```
#### Impact of anti-patterns
|Problem	|Impact|
|-|-|
|Maintenance burden	|Changes must be replicated across every duplicate. Missed updates cause drift between copies.|
|Ambiguous context	|Users and AI agents cannot determine which of several near-identical types is canonical.|
|Inconsistent behavior	|Duplicated action or derived property logic diverges over time, producing conflicting results.|
|Wasted development effort	|Teams re-build the same thing in slightly different forms instead of collaborating on one shared model.|
#### Best practices
1. **审计重复项：** 如果多个 Object Type 共享通用形状（相同的 Property、相似的 Link、相似的 Action），评估它们是否应该成为具有区分 Property 的单一 Type，或者应该实现共享 Interface。

2. **整合共享逻辑：** 如果相同的派生 Property 或 Action 逻辑出现在多个 Type 上，请将其提取到 Interface 或共享 Function 中。

3. **统一团队特定的副本：** 当不同组创建了几乎相同的 Object Type 时，将它们统一为具有适当安全性或过滤的单一规范表示。
4. **应用三次规则：** 一个重复项可以接受。两次是一个警告信号。三次意味着是时候重构了。

1. **Audit for duplicates:** If multiple object types share a common shape (same properties, similar links, similar actions), evaluate whether they should be a single type with a distinguishing property or should implement a shared interface.
2. **Consolidate shared logic:** If the same derived property or action logic appears across multiple types, extract it into an interface or shared function.
3. **Unify team-specific copies:** When different groups have created near-identical object types, unify them into a single canonical representation with appropriate security or filtering.
4. **Apply the rule of three:** One duplicate can be acceptable. Two is a warning sign. Three means it is time to refactor.
### 3. Open for extension, closed for modification

> 📷 **[图片: 2-Open Closed]**

> 📷 **[图片: 2-Open Closed]**

**保护核心模型。让构建者能够对其进行扩展。**

**Protect core models. Enable builders to extend them.**
一旦一个 Object Type、Interface 或工作流经过实战检验并投入生产，其核心结构应当保持稳定。组织中的其他开发者和团队应当能够在此基础上进行构建，添加实现 Interface 的新 Object Type 或消费现有 Object 的新工作流，而无需修改核心模型。

Once an object type, interface, or workflow is field-tested and in production, its core structure should be stable. Other developers and teams in the organization should be able to build on top of it, adding new object types that implement an interface or new workflows that consume existing objects, without needing to modify the core model.
#### Anti-patterns
* 对已确立的 Object Type 进行频繁的破坏性更改，波及所有依赖的应用程序
* 新的用例需要修改现有的核心类型，而非对其进行扩展

* 团队需要编辑共享的 Interface 或 Action 以满足团队特定需求
* 针对某个团队扩展所做的安全更改意外影响到其他使用者

* Frequent breaking changes to established object types that cascade across dependent applications
* New use cases require modifying existing core types rather than extending them
* Teams need to edit shared interfaces or actions to accommodate team-specific needs
* Security changes for one team's extension inadvertently affect other consumers
#### Example
一个核心的 `Equipment` Object Type 和 `Inspectable` Interface 已投入生产。一个新团队需要为某些设备跟踪认证数据：

A core `Equipment` object type and `Inspectable` interface are in production. A new team needs to track certification data for some equipment:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Modify the core Equipment type:            Extend without modifying core:

Equipment                                  Equipment (unchanged)
- serial_number                            - serial_number
- manufacturer                             - manufacturer
- certification_authority  (new)   →       - Links to → Equipment Certification
- certification_expiry     (new)
- certification_status     (new)         Equipment Certification (new linked type)
- last_cert_audit          (new)           - certification_authority
- certification_expiry
(Four new properties, null for all           - certification_status
non-certified equipment, existing           - last_certification_audit
consumers must handle the change)
New interface: Certifiable
- certification_status
- certification_expiry

(Core type untouched, new capability
added via linked type and interface)
```
#### Impact of anti-patterns
|Problem	|Impact|
|-|-|
|Breaking changes	|Modifications to core types can break dependent applications, actions, and workflows across the organization.|
|Scope creep	|Core types accumulate properties and logic for every new use case, trending toward a [God Object](/docs/foundry/ontology/ontology-anti-patterns/#anti-pattern-the-god-object).|
|Entangled ownership	|Multiple teams modify the same core type, creating merge conflicts and unclear accountability.|
|Security leakage	|Extending a core type without clean boundaries can inadvertently widen data access.|
#### Best practices
1. **确定什么是核心要素：** 确定哪些 Property 和 Link 对实体而言是真正根本的，将这些锁定下来。

2. **为扩展而设计：** 在创建核心类型和 Interface 时，预期他人将基于它们进行构建，为链接的扩展类型和新的 Interface 实现留出空间。

3. **扩展而非修改：** 在向现有模型添加内容时，考虑该新增内容是属于核心类型，还是属于扩展（一个新的链接 Object Type、一个新的 Interface 实现或一个新的 Property namespace）。

4. **强制安全边界：** 核心数据模型应具有明确的安全边界，以便对 Ontology 的扩展不会意外扩大访问权限。

1. **Identify what is essential:** Determine which properties and links are truly fundamental to the entity. Lock those down.
2. **Design for extension:** When creating core types and interfaces, anticipate that others will build on them. Leave room for linked extension types and new interface implementations.
3. **Extend rather than modify:** When adding to an existing model, consider if the addition belongs on the core type, or on an extension (a new linked object type, a new interface implementation, or a new property namespace).
4. **Enforce security boundaries:** Core data models should have well-defined security boundaries so that extending the Ontology does not inadvertently widen access.
### 4. Composition over deep hierarchies

> 📷 **[图片: 4-Composition]**

> 📷 **[图片: 4-Composition]**

**通过 Interface 优先采用多重继承。保持可插拔性。**

**Favor multiple inheritance via interfaces. Keep things pluggable.**
Foundry 的 Ontology 通过 Interface 支持多重继承，因此实体可以从多个聚焦的抽象中组合行为，而不是采用单一继承链。

Foundry's Ontology supports multiple inheritance through interfaces, so an entity can compose behavior from multiple focused abstractions instead of a single-inheritance chain.
#### Anti-patterns
* 深度单一继承链中的子类型仅仅是为了组合父类型的能力而存在

* 像 `SchedulableBuilding` 或 `InspectableVehicle` 这类"组合型"类型将两个不相关的概念合并为一个类型

* 工作流与特定 Object Type 紧密耦合，而它们本可以在共享的 Interface 上运行
* 为实体添加新能力需要重构继承链

* Deep single-inheritance chains where child types exist solely to combine parent capabilities
* "Combination" types like `SchedulableBuilding` or `InspectableVehicle` that merge two unrelated concepts into one type
* Workflows are tightly coupled to specific object types when they could operate on a shared interface
* Adding a new capability to an entity requires restructuring the inheritance chain
#### Example
一个 `Arena` 需要同时作为一个建筑和一个可调度资源：

An `Arena` needs to be both a building and a schedulable resource:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Deep single-inheritance:                   Composed interfaces:

Asset                                      Interface: Building
└── PhysicalAsset                          - address
└── Building                         - square_footage
└── SchedulableBuilding
└── Arena              Interface: SchedulableResource
- scheduling_calendar
(Every new combination of capabilities       - booking_policy
requires a new intermediate type.
A SchedulableWarehouse would need         Arena implements both:
yet another branch.)                        Building + SchedulableResource
- arena_name
- seating_capacity

(Adding SchedulableWarehouse only
requires implementing the same two
interfaces — no new hierarchy needed.)
```
#### Impact of anti-patterns
|Problem	|Impact|
|-|-|
|Combinatorial explosion	|Every new combination of capabilities requires a new intermediate type in the hierarchy.|
|Brittle hierarchies	|Changes to a parent type cascade unpredictably through all descendants.|
|Limited reuse	|Workflows built on a specific type deep in the chain cannot be reused for other types that share the same capability.|
|Semantic distortion	|Contrived parent types (like `SchedulableBuilding`) do not represent real-world concepts, violating the [domain-driven design principle](#1-domain-driven-design).|
#### Best practices
1. **围绕能力或角色设计 Interface：** 使用聚焦的 Interface，例如 `Inspectable`、`Schedulable`、`Billable` 或 `Depreciable`，以捕获特定的行为或 Property 集合。

2. **使用分类学 Interface 进行聚合：** 分类学身份 Interface（例如，由 `Aircraft`、`Vessel`、`GroundVehicle` 实现的 `MilitaryAsset`）对于下钻调查或类似的聚合工作流特别有用。

3. **在工作流中以 Interface 为目标：** 在构建 Action、Function 和应用程序时，尽可能以 Interface 为目标。基于 `SchedulableResource` Interface 构建的工作流可以适用于 Arena、会议室和车辆，无需修改。

4. **组合而非继承：** 当实体需要多种能力时，应实现多个 Interface，而不是将其插入深度单一继承链中。

1. **Design interfaces around capabilities or roles:** Use focused interfaces like `Inspectable`, `Schedulable`, `Billable`, or `Depreciable` that capture a specific behavior or property set.
2. **Use taxonomic interfaces for aggregation:** Taxonomic identity interfaces (for example, `MilitaryAsset` implemented by `Aircraft`, `Vessel`, `GroundVehicle`) are particularly useful for drilldown investigations or similar aggregation workflows.
3. **Target interfaces in workflows:** When building actions, functions, and applications, target interfaces where possible. A workflow built on the `SchedulableResource` interface works for arenas, conference rooms, and vehicles without modification.
4. **Compose rather than inherit:** When an entity needs multiple capabilities, implement multiple interfaces rather than inserting it into a deep single-inheritance chain.
## Pragmatism and tradeoffs
**这些原则是指导，而非法则。**

**These principles are guides, not laws.**
现实世界的约束（包括 deadline、遗留系统、平台的部分支持以及用户技能水平）意味着理想的 Ontology 设计并不总是能够立即实现。使用以下指导方针来权衡取舍：

Real-world constraints, including deadlines, legacy systems, partial platform support, and user skill levels, mean that the ideal Ontology design is not always immediately achievable. Use the following guidelines to navigate tradeoffs:
|Guideline	|Detail|
|-|-|
|Steer toward good design without being a roadblock	|If something needs to be working within a tight deadline, build something reasonable now with a clear path to improvement.|
|Name the tradeoffs explicitly	|When recommending a shortcut, explain what is being traded away and when it might matter. For example, a denormalization could work fine at your current scale, but if you grow past 10k objects, you may want to revisit.|
|Prefer incremental improvement over big-bang refactors	|A slightly imperfect Ontology that is in use and generating value is better than a theoretically perfect one that is still being designed.|
|Defend the critical invariants	|Naming quality, semantic clarity, and security design are hard to fix later. Cut corners on implementation details, not on these.|
Ontology 是驱动您组织的软件。请以对待生产代码库同样的审慎态度来对待它，但将业务价值置于完美之上。

The Ontology is the software that powers your organization. Treat it with the same care you would give to a production codebase, but prioritize business value over perfection.