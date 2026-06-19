<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/ontology-structural-guidance/
---
# Ontology design: Structural guidance
以下各节提供了关于如何在 Ontology 中构建 properties、relationships 和 access control 的指导。

The following sections provide guidance on how to structure properties, relationships, and access control within the Ontology.
## Normalization and derived properties
**每个事实只存储一次。使用 derived properties 以提供便利。**

**Store each fact once. Use derived properties for convenience.**
反规范化数据（将 linked objects 上的值复制到父 object 上）可能存在风险。当数据源发生变化时，每个副本都必须更新。规范化可以保持数据一致性，而 derived properties 则让您在无需维护的情况下获得反规范化的访问便利。

Denormalized data (copying values from linked objects onto a parent object) can be risky. When the data source changes, every copy must be updated. Normalization keeps data consistent, and derived properties give you the convenience of denormalized access without the upkeep.
并非所有计算值都是相同的。正确的方法取决于该值是可以从稳定的输入中安全地预先计算，还是需要与 Ontology 中的动态变化保持同步。

Not all computed values are the same. The right approach depends on whether a value can be safely pre-computed from stable inputs or whether it needs to stay in sync with dynamic Ontology changes.
### Pre-computed vs. dynamically derived values
|Type	|Characteristics	|Recommended tool	|Example|
|-|-|-|-|
|Pre-computed	|Computed from properties on the same object; inputs rarely change or only change due to pipeline ingestion.	|Pipeline transform	|`fullName` = `firstName` + " " + `lastName`

Inputs are stable and updated in the same pipeline, so pre-computing is safe and adds zero runtime overhead.|
|Dynamically derived	|Depends on linked objects or values that change via actions, automations, or other Ontology-level operations.	|Derived property	|`directReportCount`

Employees are reassigned, onboarded, and offboarded through actions. A derived property that counts linked `Employee` objects stays correct automatically.|
> **⚠️ 警告**

> 当某个值依赖于通过 actions 所做的更改时，每个可能影响该值的 action 也必须更新该值。如果有任何 action 未能做到这一点，该值将一直保持错误，直到发现该差异为止。
> **⚠️ 警告**

> When a value depends on changes made through actions, every action that could affect the value must also update the value. If any action fails to do so, the value will remain incorrect until the discrepancy is identified.
### Anti-patterns
* 同一个值作为 property 存储在多个 object types 上

* Properties 因作为其他位置维护值的副本而过时

* 更新单个现实世界的事实需要对多个 objects 进行写入

* Integer 或 count properties 是手动维护的，而不是从 links 计算得出的

* The same value is stored as a property on multiple object types
* Properties go stale because they are copies of values maintained elsewhere
* Updating a single real-world fact requires writes to multiple objects
* Integer or count properties are manually maintained rather than computed from links
### Example
一个 `Manager` object type 需要显示其直接下属的数量：

A `Manager` object type needs to display a count of direct reports:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Manager                                    Manager
- direct_report_count: 5                   - direct_report_count (derived):
(manually maintained integer;                counts linked Employee objects
must be updated every time          →       at query time
an employee joins or leaves)
Employee
Employee                                     - manager (link to Manager)
- manager_name: "Alice"
(copied from the linked Manager;
breaks if the manager's name
changes)
```
### Performance considerations
Derived properties 在运行时进行求值。其性能特征因规模而异：

Derived properties are evaluated at runtime. The performance characteristics vary by scale:
|Scale	|Recommendation|
|-|-|
|Low to moderate (<~10k objects per query)	|Use derived properties freely. Runtime evaluation is sufficiently performant for most workflows.|
|High (>~10k objects per query)	|Derived properties may introduce latency due to higher-overhead query paths. Denormalization may be an appropriate tradeoff, but it should be a conscious, documented decision and not the default.|
### Best practices
1. **将每个事实存储在一个位置**，即在语义上属于该事实的 object 上。

2. **使用 derived properties** 在查询时从 linked objects 计算或聚合值。

3. **监控性能**，随着规模的增长。如果 derived properties 在高规模下引入了不可接受的延迟，请考虑选择性的反规范化。

4. **对任何反规范化进行文档记录**，包括其基本原理、事实来源（source of truth）以及保持副本同步的更新策略。

1. **Store each fact in one place**, on the object where it semantically belongs.
2. **Use derived properties** to compute or aggregate values from linked objects at query time.
3. **Monitor performance** as scale grows. If derived properties introduce unacceptable latency at high scale, consider selective denormalization.
4. **Document any denormalization** with the rationale, the source of truth, and the update strategy for keeping copies in sync.
## Structs
**将语义相关的字段分组到 structs 中。**

**Group semantically related fields into structs.**
当一个 property 天然是多字段的（例如，包含街道、城市、州和邮编的地址）时，请使用 struct 而不是将其拆分为多个独立的 properties。Structs 可以保留语义分组，并支持更丰富的元数据捕获。

When a property is naturally multi-field (for example, an address with street, city, state, and postal code), use a struct rather than flattening into separate properties. Structs preserve semantic grouping and enable richer metadata capture.
### When to use structs
|Scenario	|Example|
|-|-|
|Multi-field values	|Address (street, city, state, postal code), coordinates (latitude, longitude)|
|Values with metadata	|AI-generated outputs with confidence scores, source references, and reasoning|
|Multi-valued properties with selection logic	|Multiple phone numbers where a reducer surfaces the primary one|
### Example
在 `Facility` object type 上对地址进行建模：

Modeling an address on a `Facility` object type:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Facility                                   Facility
- address_street                           - address (struct)
- address_city                                 - street
- address_state                    →           - city
- address_postal_code                          - state
- address_country                              - postal_code
- country
(Five unrelated properties with a
naming convention as the only link         (One semantic concept with a main
between them)                               field and structured sub-fields)
```
### Key benefits
|Benefit	|Details|
|-|-|
|Semantic grouping	|An address is one concept, not five unrelated strings. The Ontology reflects this.|
|Metadata capture	|Structs can carry source, confidence, and timestamp information alongside the primary value.|
|Reducer support	|In multi-valued scenarios, reducers can surface the most relevant value (for example, primary address).|
|Main field behavior	|A struct can designate a main field so it behaves like a simple property in interfaces and queries.|
Structs 在 AI-first 的工作流中尤其有价值，因为大语言模型（LLM）的输出既有主要结果，又包含相关的元数据（推理过程、来源引用、置信度分数）。应将这些信息一起捕获，而不是分散到不相关的 properties 中。

Structs are especially valuable in AI-first workflows where large language model (LLM) outputs have both a primary result and associated metadata (reasoning, source references, confidence scores). Capture these together rather than scattering them across unrelated properties.
### Best practices
1. **识别多字段 properties**，即那些字段在语义上相关且始终一起使用的 properties。

2. **定义 struct**，使用清晰的字段名称和类型。

3. **指定一个主字段**，以便在大多数情况下该 struct 的行为类似于一个简单的 property。

4. **使用 reducers** 来处理多值的 struct properties，以呈现最相关的值。

5. **捕获元数据**（来源、置信度、时间戳）与主要值一起存放在 struct 中，特别是对于 AI 生成的输出。

1. **Identify multi-field properties** where the fields are semantically related and always used together.
2. **Define the struct** with clear field names and types.
3. **Designate a main field** so the struct behaves like a simple property in most contexts.
4. **Use reducers** for multi-valued struct properties to surface the most relevant value.
5. **Capture metadata** (source, confidence, timestamps) in the struct alongside the primary value, especially for AI-generated outputs.
## Interfaces
**使用 interfaces 来构建可重用且面向未来的抽象。**

**Use interfaces to build reusable, future-proof abstractions.**
Interface 是实现 ["Don't repeat yourself" 设计原则](/docs/foundry/ontology/ontology-best-practices/#2-dont-repeat-yourself-rule-of-three) 和 [open/closed extensibility](/docs/foundry/ontology/ontology-best-practices/#3-open-for-extension-closed-for-modification) 的主要工具。它们定义了一个共享的 shape（properties、links、actions），多个 object types 可以实现该 shape，从而使 workflow 能够面向 interface 而非单个 type。

Interfaces are the primary tool for achieving the ["Don't repeat yourself" design principle](/docs/foundry/ontology/ontology-best-practices/#2-dont-repeat-yourself-rule-of-three) and [open/closed extensibility](/docs/foundry/ontology/ontology-best-practices/#3-open-for-extension-closed-for-modification). They define a shared shape (properties, links, actions) that multiple object types can implement, enabling workflows to target the interface rather than individual types.
### When to use interfaces
|Scenario	|Example|
|-|-|
|Common properties across types	|`Inspectable` interface with `lastInspectionDate` and `inspectionStatus`, implemented by `Vehicle`, `Equipment`, `Facility`|
|Shared workflows	|A scheduling workflow targeting `SchedulableResource` works for arenas, conference rooms, and vehicles without modification|
|Taxonomic grouping	|A `MilitaryAsset` interface implemented by `Aircraft`, `Vessel`, `GroundVehicle` for drilldown aggregation workflows|
|Multi-level abstraction	|`SchedulableResource` extends `Trackable`, adding scheduling-specific properties to a broader tracking abstraction|
### Example
多个 object types 需要巡检跟踪：

Multiple object types need inspection tracking:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Vehicle                                    Interface: Inspectable
- lastInspectionDate                       - lastInspectionDate
- inspectionStatus                         - inspectionStatus
- (duplicate action: Schedule              - (shared action: Schedule Inspection)
Vehicle Inspection)
→     Vehicle implements Inspectable
Equipment                                    - make, model, mileage, ...
- lastInspectionDate
- inspectionStatus                       Equipment implements Inspectable
- (duplicate action: Schedule              - serial_number, warranty_expiry, ...
Equipment Inspection)
Facility implements Inspectable
Facility                                     - address, capacity, ...
- lastInspectionDate
- inspectionStatus                       (One interface, one shared action,
- (duplicate action: Schedule             three implementing types)
Facility Inspection)

(Three copies of the same properties
and logic, maintained independently)
```
### Platform considerations
即使当前平台工具未能完全支持 interface-backed workflow，使用 interface 进行设计也奠定了一个基础，随着支持的扩展将带来回报。

Even where current platform tooling does not fully support interface-backed workflows, designing with interfaces establishes a foundation that pays off as support expands.
|Situation	|Guidance|
|-|-|
|The interface is fully supported in your workflow	|Target the interface directly. A single workflow covers all implementing types.|
|The interface is not yet supported in a specific context	|Define the interface now and duplicate the workflow per type as a temporary measure. This approach is no less efficient than working without an interface, and it establishes a clear path to consolidation once support is available.|
请查看我们的 [interface documentation](/docs/foundry/interfaces/interface-overview/) 了解当前支持详情。

Review our [interface documentation](/docs/foundry/interfaces/interface-overview/) for current support details.
### Best practices
1. **识别公共 shape：** 如果多个 object types 共享 properties、links 或 actions，请定义一个 interface 来捕获该共享 shape。

2. **围绕能力或分类体系设计 interface：** 能力型 interface 可以包括 `Inspectable`、`Schedulable` 或 `Billable`。分类型 interface 可以包括 `MilitaryAsset` 或 `MedicalDevice`。

3. **在 workflow 中面向 interface：** 尽可能针对 interface 构建 actions、functions 和 applications。

4. **扩展 interface 以实现多层抽象：** Interface 可以扩展其他 interface，以构建分层的抽象。

5. **现在搭建脚手架，稍后整合：** 即使由于当前平台支持的限制，某些 workflow 必须暂时按 type 重复定义，也可以先定义 interface。

1. **Identify common shapes:** If multiple object types share properties, links, or actions, define an interface that captures the shared shape.
2. **Design interfaces around capabilities or taxonomy:** Capability interfaces may include `Inspectable`, `Schedulable`, or `Billable`. Taxonomic interfaces may include `MilitaryAsset` or `MedicalDevice`.
3. **Target interfaces in workflows:** Build actions, functions, and applications against interfaces where possible.
4. **Extend interfaces for multi-level abstraction:** Interfaces can extend other interfaces to build layered abstractions.
5. **Scaffold now, consolidate later:** Define interfaces even if some workflows must temporarily be duplicated per-type due to current platform support gaps.
## Links and object-backed link types
**Link 应表示语义上有意义的关系。**

**Links should represent semantically meaningful relationships.**
每个 link type 都应回答一个明确的领域问题，例如：

Every link type should answer a clear domain question, such as:
* 该患者就诊了哪个 facility？

* 该 employee 属于哪个 team？

* 该工单使用了哪些 equipment？

* Which facility did this patient visit?
* Which team does this employee belong to?
* Which equipment was used in this work order?
### When to use link types
|Link type	|Use when	|Example|
|-|-|-|
|Direct link	|The relationship is meaningful but carries no metadata of its own.	|`Employee` → `Department`|
|Object-backed link	|The relationship carries its own metadata (dates, roles, status, allocation).	|`Employee` → `VentureStaffing` → `Venture` (with `role`, `startDate`, `allocation`)|
并非每个链接对象在每个场景下都需可见。有些 workflow 关心关联元数据，有些只关心直接连接。Object-backed links 使您能够根据 workflow 暴露相应的视图。

Not every linking object needs to be visible in every context. Some workflows care about the join metadata, others just want the direct connection. Object-backed links let you expose either view depending on the workflow.
### Example
对 employee 与 venture 之间的关系进行建模，其中每次分配都有一个 role 和 start date：

Modeling the relationship between employees and ventures, where each assignment has a role and start date:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Employee → Venture (direct link)           Employee → Venture Staffing → Venture
(no way to capture role,
start date, or allocation         →     Venture Staffing
per assignment)                           - role
- start_date
— OR —                                       - allocation_percentage
- status
Employee
- venture_role                           Workflows can expose either:
- venture_start_date                       - Direct: Employee → Venture
(ambiguous if employee has                 - Detailed: Employee → Staffing → Venture
multiple venture assignments)
```
### Impact of incorrect link design
|Problem	|Impact|
|-|-|
|Lost metadata	|Direct links cannot capture when, why, or in what capacity a relationship exists.|
|Ambiguous multi-links	|Properties like `venture_role` on the source object become ambiguous when an entity participates in multiple relationships.|
|Meaningless links	|Links that exist only because two datasets share a foreign key add noise to the Ontology and confuse navigation.|
### Best practices
1. **验证语义含义：** 避免仅因两个数据集共享一个外键而存在的 link。需考量该关系在领域中是否有意义。

2. **评估关系是否承载元数据：** 如果承载（如 dates、roles、status），请使用 object-backed link type 来捕获这些元数据。

3. **暴露恰当的详细程度：** 设计 workflow 时，根据上下文使用直接关系或通过链接对象访问的详细关系。

4. **清晰命名 link：** Link 名称应描述两个方向的关系。更多信息请查看 [naming conventions](#naming-conventions) 部分。

1. **Validate semantic meaning:** Avoid links that exist only because two datasets share a foreign key. Ask if the relationship is meaningful in the domain.
2. **Evaluate whether the relationship carries metadata:** If it does (dates, roles, status), use an object-backed link type to capture that metadata.
3. **Expose the right level of detail:** Design workflows to use either the direct relationship or the detailed relationship through the linking object, depending on the context.
4. **Name links for clarity:** Link names should describe the relationship from each direction. Review the section on [naming conventions](#naming-conventions) for more information.
## Naming conventions
**优化人类可读性与 agent 可导航性。**

**Optimize for human readability and agent navigability.**
一致且具有描述性的命名是您对 Ontology 质量最有价值的投资之一。清晰的命名使 Ontology 对人类和 AI agents 都更易于浏览，并且一旦 Ontology 投入使用，更正命名将十分困难。

Consistent, descriptive naming is one of the most impactful investments you can make in Ontology quality. Clear names make the Ontology easier for both humans and AI agents to navigate, and they are far harder to correct once the Ontology is in use.
### Naming rules
|Element	|Convention	|Good examples	|Bad examples|
|-|-|-|-|
|Object types	|Singular, concrete nouns a domain expert would recognize	|`Patient`, `WorkOrder`, `FlightSegment`	|`Data`, `Item`, `Record`|
|Properties	|Concise, self-evident; no encoded type info or implementation details	|`age`, `status`, `lastInspectionDate`	|`dtLastInspMod`, `nVAL_01`, `field_x`|
|Links	|Read naturally from each direction	|`department` (Employee → Dept), `employees` (Dept → Employee)	|`related_items`, `link_1`|
|Dates	|Follow a single convention consistently across the Ontology	|`createdDate`, `updatedDate`, `effectiveDate`	|Mixing `createdDate` and `dateOfCreation`|
|Ambiguous terms	|Qualify with specific meaning	|`monetaryValue`, `quantityOnHand`, `riskScore`	|`value`, `quantity`, `score`|
### Example
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
Object type: Item                    →     Object type: Product

Property: dtLastInspMod              →     Property: lastInspectionDate

Property: value                      →     Property: monetaryValue
Property: quantityOnHand

Link: Item → Related Item            →     Link: Product → Supplier
Link: Employee → Supervisor
```
### Best practices
1. **在构建前建立命名约定：** 提前就 dates、statuses、identifiers 和 links 的模式达成一致。

2. **遵循 Ontology 既定的约定：** 如果 Ontology 已使用 `createdDate`，请勿引入 `dateOfCreation`。

3. **限定有歧义的 properties：** 使用 `monetaryValue`、`quantityOnHand` 和 `riskScore`。请勿使用 `value`、`quantity` 和 `score`。

4. **按关系命名 link：** 从 `Employee` 到 `Department` 的 link 应为 `department`（从 employee 视角）和 `employees`（从 department 视角）。

5. **与最终用户一起审查命名：** 对构建者而言清晰的名称，对使用者可能存在歧义。请与每天使用 Ontology 的人员一起验证。

1. **Establish naming conventions before building:** Agree on patterns for dates, statuses, identifiers, and links up front.
2. **Follow the Ontology's established conventions:** If the Ontology already uses `createdDate`, do not introduce `dateOfCreation`.
3. **Qualify ambiguous properties:** Use `monetaryValue`, `quantityOnHand`, and `riskScore`. Do not use `value`, `quantity`, and `score`.
4. **Name links by relationship:** A link from `Employee` to `Department` should be `department` (from the employee's perspective) and `employees` (from the department's perspective).
5. **Review names with end users:** Names that seem clear to the builder may be ambiguous to consumers. Validate with the people who will use the Ontology every day.
## Security design
**按照最小权限原则语义化地设计安全性。**

**Design security semantically, following the principle of least privilege.**
Ontology 中的安全性应该使用在领域中合理的术语来表达，而不是使用数据基础设施相关的术语。用户应该能够查看安全配置并理解受保护的内容及其原因。

Security in the Ontology should be expressed in terms that make sense in the domain, not in terms of data infrastructure. Users should be able to look at a security configuration and understand what is protected and why.
### Security model
结合行级和列级安全，以实现细粒度的单元格级访问控制：

Combine row-level and column-level security for fine-grained cell-level access control:
|Security layer |Controls	|Example |
|-|-|-|
|Row-level	|The objects a user can view	|VIP patients are restricted to senior staff|
|Column-level	|The properties a user can view on visible objects	|Clinical notes are restricted to the care team|
|Cell-level (combined)	|The intersection of row and column restrictions	|VIP patients' clinical notes are visible only to the senior care team|
### Example
控制对敏感患者数据的访问：

Controlling access to sensitive patient data:
```
✗ Avoid                                    ✓ Prefer
────────────────────────────────────────   ────────────────────────────────────────
PublicPatient (object type)                Patient (single object type)
- name                                     - name
- dob                                      - dob
- diagnosis                                - diagnosis (column-restricted:
care team only)
RestrictedPatient (object type)      →       - clinical_notes (column-restricted:
- name                                         care team only)
- dob                                      - mental_health_records (column-
- diagnosis                                    restricted: psychiatry team only)
- clinical_notes
- mental_health_records                  Row-level security:
- VIP patients: senior staff only
(Duplicated schemas; security
achieved by splitting types.              Column-level security:
Properties added to one type are            - clinical_notes: care team only
easily forgotten on the other.)             - mental_health_records: psychiatry only

(One type; security achieved by policy.
Domain boundaries drive access rules.)
```
### Impact of incorrect security design
|Problem	|Impact|
|-|-|
|Duplicated types for security	|Schemas drift out of sync; properties added to one type are easily forgotten on the other. Violates the ["Don't repeat yourself" design principle](/docs/foundry/ontology/ontology-best-practices/#2-dont-repeat-yourself-rule-of-three).|
|Over-permissive defaults	|Starting with broad access and restricting later risks exposing sensitive data before lockdown is complete.|
|Ad-hoc filtering instead of policy	|Security logic scattered through application code rather than enforced at the Ontology layer is fragile and difficult to audit.|
|Misaligned boundaries	|Security boundaries that do not follow domain boundaries are harder to reason about and more likely to have gaps.|
### Best practices
1. **从严格的权限开始，有计划地开放：** 默认采用最小访问权限并根据需要逐步扩展，而不是从开放开始后再进行限制。
2. **同时使用行级和列级安全** 以实现细粒度的单元格级访问控制。

3. **使安全与领域边界保持一致：** 如果您的领域具有自然的访问边界（例如区域经理只能查看其区域的数据；护理团队只能查看其患者的数据），请使用 Ontology 关系和安全策略来对这些边界进行建模，而不是使用临时的数据过滤方式。

4. **避免为安全目的而重复创建 Object Type：** 使用带有精心设计的安全策略的单一 Object Type 优于使用具有重复 schema 的多个 Object Type。

5. **审查新的 ontology 路径以确保访问控制的一致性：** 确保新增的 link、type 或 property 能够保持对受限数据的预期保护。

1. **Start restrictive, open up deliberately:** Default to minimal access and widen as needed, rather than starting open and restricting later.
2. **Use row-level and column-level security together** for fine-grained cell-level access control.
3. **Align security with domain boundaries:** If your domain has natural access boundaries (a regional manager sees their region's data; a care team sees their patients), model those boundaries using Ontology relationships and security policies rather than ad-hoc data filtering.
4. **Avoid duplicating object types for security:** A single type with well-designed security policies is better than multiple types with duplicated schemas.
5. **Review new ontology paths for access-control consistency:** Ensure added links, types, or properties preserve the intended protections around restricted data.
使用本页面的指导确保安全边界与领域边界保持一致，然后参考我们的 [安全与治理文档](/docs/foundry/security/overview/) 以获取配置详细信息。

Use the guidance on this page to ensure security boundaries align with domain boundaries, then refer to our [security and governance documentation](/docs/foundry/security/overview/) for configuration details.