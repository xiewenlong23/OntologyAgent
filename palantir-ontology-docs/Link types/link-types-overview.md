<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/link-types-overview/
---
# Link types
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

A **link type** is the schema definition of a relationship between two object types. A **link** refers to a single instance of that relationship between two objects in the same Ontology.
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

For example, in the Ontology Manager, you may create a link type between the `Employee` object type and the `Company` object type that defines the relationship between `Employee` and `Employer`. A link refers to a single instance of the `Employee → Employer` link type, like the relationship between the notional employee “Melissa Chang” and her employer, “Acme, Inc.”
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

Similarly, in the Ontology Manager, you may create a link type between the `Flight` object type and the `Aircraft` object type that defines the relationship between `Scheduled Flight` and `Assigned Aircraft`. A link refers to a single instance of the `Scheduled Flight → Assigned Aircraft` link type, like the relationship between “JFK → SFO 24-02-2021” and its assigned aircraft “Boeing 737-123”.
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

Links can also exist between two objects of the same type. A link type `Direct Report ↔ Manager` can be defined between the `Employee` object type and itself.
注意,不支持跨不同 Ontology 的 Object Type 之间的 link。在这种情况下,您可以考虑使用共享 Ontology。

[PARA_0]

> 📷 **[图片: Delete link type]**

[PARA_1]
您可以更改 backing datasource:

[PARA_2]
1. 导航至 link type 视图的 **Datasources** 页面。

2. 选择现有 datasource 旁边的 ![pen](/docs/resources/foundry/object-link-types/pen.png) **Select** 图标。这将允许您在 Foundry 中浏览并选择可用的 datasource。

[PARA_3]
> **⚠️ 警告: Warning**

> 更改 link type 的 backing datasource 将移除旧 datasource 中列与定义 link type 的 key 之间的任何连接。**只有在**您更改为与旧 datasource **具有相同 schema** 的新 datasource 时,Key 才会自动重新映射。否则,您需要将 key 重新映射到新 datasource。

[PARA_4]

> 📷 **[图片: Edit link type metadata]**

[PARA_5]
1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
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

Note that links between object types across different Ontologies is not supported. In this case, you may prefer to leverage a shared Ontology.
支撑 Ontology 的概念在数据集结构中有类似的概念。Ontology 中 Link Type 的定义类似于两个数据集之间的 join，而 Link 的定义类似于与另一个数据集中同一行的字段进行 join 的一行。例如，您可以将 `Employee` 数据集与 `Company` 数据集进行 join，以探索 `Employees` 与其 `Employers` 之间的关系。在 join 后的数据集中，将 "Melissa Chang" 与其雇主 "Acme, Inc." 进行 join 的单行即表示一个 Link。

The concepts underpinning the Ontology have analogous concepts in the structure of a dataset. The definition of a link type in the Ontology is analogous to that of a join between two datasets, while the definition of a link is analogous to that of a row joined with the fields of the same row in another dataset. For example, you can join the `Employee` dataset with the `Company` dataset to explore the relationship between `Employees` and their `Employers`. In the joined dataset, a single row that joins “Melissa Chang” with her employer “Acme, Inc.” represents a link.
Foundry Ontology 并非一个抽象的数据模型，而是将每个 Ontology 概念映射到组织的实际数据，使该数据资产能够为实际应用程序提供支持。通过在 Ontology Manager 中向 Link Type 中引用的 Object Type 添加 backing datasources，可以在用户应用程序中创建和显示 Links。在 Object Type 以多对多基数关联的 Link Type 的情况下，datasources 则为 Link Type 本身提供 backing。要创建 `Employee → Employer` 类型的 Links，组织将向 `Employee` 和 `Company` Object Type 添加 backing datasources，并将其员工目录及其他企业数据接入 Ontology。

Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. Links are created and displayed in user applications by adding backing datasources to the object types referred to in the link type in the Ontology Manager. In the case of link types where object types are related with a many-to-many cardinality, datasources back the link types themselves. To create links of type `Employee → Employer`, an organization will add backing datasources to the `Employee` and `Company` object types and connect their employee directory and other enterprise data into the Ontology.
首先，请通过学习如何 [create a new link type](/docs/foundry/object-link-types/create-link-type/) 来开始。

Get started by learning how to [create a new link type](/docs/foundry/object-link-types/create-link-type/).