<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/link-type-metadata/
---
# Metadata reference
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

A link type is represented in the Foundry Ontology by the following metadata:
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

* **ID:** A unique identifier of the link type, primarily used to reference links of this type when configuring an application. For example, `employee-employer` may be the ID of the link type defined between the `Employee` and `Company` object types.
* **RID:** An automatically generated unique identifier for every resource in Foundry. A link type’s RID will be referenced in error messages across the platform.
* **Status:** A signal to users and other Ontology builders about where in the development process the link type stands. It can be `active`, `experimental`, or `deprecated`. By default, the `Employee → Employer` link type will have status `experimental`. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* **Object types:** The object types related through the link type definition. For example, the `Employee → Employer` link type will refer to the `Employee` and `Company` object types.
* **Cardinality:** Indicates to applications if each object type in the link type has one or many objects. For example, The Employee object type in link type `Employee → Employer` has cardinality `many` and the Company object type has cardinality `one`, since many employees are linked to a single employer. The Employee object types in link type `Direct Report ↔ Manager` will each have cardinality `many` if a direct report can have multiple managers and if a manager can have multiple direct reports.
* **Key:** The properties or columns used to create the links.
* In a one-to-one or in a one-to-many cardinality link type, a property of one object type (the foreign key) refers to the primary key property of the other object type. This reference between a foreign key and primary key defines the links between objects. For example, in the `Employee → Employer` link type, the `Employee` object type may have an `employer ID` property (the foreign key) that refers to the `company ID` property (primary key) of the `Company` object type.
* In a many-to-many cardinality link type, a table containing pairs of primary keys defines the links between two objects. These link types require a join table to be specified, along with mapping these keys that tell applications which columns in the join table refer to the primary keys of which object types in the link type. For example, the join table backing the `Direct Report ↔ Manager` link type might contain pairs of `employee numbers`, for which each pair represents a `Direct Report ↔ Manager` link.
* **Display name:** The name shown to anyone accessing a link of this type in user applications. Each side of a link type has a display name. A side of a link type represents the link *to* that object type. For example, In the `Employee → Employer` link type, the display name for the `Employee` object type is `Employee` and the display name for the `Company` object type is `Employer`.
* **Plural display name:** The name shown to anyone accessing a link of this type with many linked object types in user applications. For example, In the `Employee → Employer` link type, the plural display name for the `Employee` object type is `Employees` and there is no plural display name for the `Company` object type, as there can only be one company per employee.
* **API name:** The name used when referring to the link type programmatically in code. The API name on a side of a link type can be used to return objects of that type. For example, if the API name on the Employee side of the `Employee → Employer` link type is `employee`, then calling `Company.employee.get()` will return the `Employee` objects linked to those `Company` objects. Read more about [API names](/docs/foundry/functions/api-objects-links/).
* **Visibility:** An indication to user applications for how prominently to display the side of the link type (referring to links *to* the object type on that side). A `prominent` side of a link type will lead applications to show this side of the link type first to users. A `hidden`  side of a link type will not appear in user applications. By default, the Employee and Company sides of the link type will have visibilities `normal`.
* **Type classes:** Additional metadata that are interpreted by user applications. Read more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

[Learn more about creating and configuring a link type in the Ontology and about validation requirements for link type metadata.](/docs/foundry/object-link-types/create-link-type/)
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

[Learn more about properties (characteristics of an object type).](/docs/foundry/object-link-types/properties-overview/)