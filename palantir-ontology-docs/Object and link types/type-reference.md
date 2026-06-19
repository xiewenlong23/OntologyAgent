<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/type-reference/
---
# Types reference
在定义 Ontology 时，您可以使用多种类型来表示已引入 Foundry 的数据的真实世界定义。Foundry 中使用的类型分为 *Ontology* 类型或 *data* 类型：

When you define your Ontology, you can use a wide variety of types to represent real-world definitions of the data you brought into Foundry. The types used in Foundry are categorized as *Ontology* types or *data* types:
* **Ontology types** 用于将真实世界领域建模到 Ontology 中。

* **Data** 类型用于表示数据值。Foundry 中的 data 类型灵感来自 [RDF ↗](https://w3c.github.io/rdf-concepts/spec/#section-Datatypes)、[OWL ↗](https://www.w3.org/TR/owl-ref/#Datatype) 和 [XSD ↗](https://www.w3.org/TR/xmlschema-2/#datatype) 中的类似概念。

* **Ontology types** are used to model a real-world domain into an Ontology.
* **Data** types are used to represent data values. Data types in Foundry are inspired by similar concepts in [RDF ↗](https://w3c.github.io/rdf-concepts/spec/#section-Datatypes), [OWL ↗](https://www.w3.org/TR/owl-ref/#Datatype) and [XSD ↗](https://www.w3.org/TR/xmlschema-2/#datatype).
## Ontology resources
以下类型可用于构建和定义您的 Ontology。

The following types are available to build and define your Ontology.
### Object type
**object type** 是真实世界实体或事件的 schema 定义，由各个 objects 组成。例如，`JFK` 和 `LHR` 都可以是 `Airport` object type 的 objects。

An **object type** is a schema definition of a real-world entity or event, comprised of individual objects. For example, both `JFK` and `LHR` can be objects of an `Airport` object type.
[详细了解 object types。](/docs/foundry/object-link-types/object-types-overview/)

[Learn more about object types.](/docs/foundry/object-link-types/object-types-overview/)
#### Property
object type 的 **property** 是描述真实世界实体或事件的特征。例如，如果 `LHR` 是 `Airports` 的 object type，则 `name` 和 `country` 是 `Airports` 的 properties。对于 `LHR` object，property 值如下：

A **property** of an object type is a characteristic that informs a real-world entity or event. For example, if `LHR` is an object type of `Airports`, `name` and `country` are properties of `Airports`. For the `LHR` object, the property values would be the following:
* **name:** LHR
* **country:** United Kingdom
* **name:** LHR
* **country:** United Kingdom
[详细了解 properties。](/docs/foundry/object-link-types/properties-overview/)

[Learn more about properties.](/docs/foundry/object-link-types/properties-overview/)
### Shared property
**shared property** 是可以在 Ontology 中的多个 object types 上使用的 property。Shared properties 允许跨 object types 进行一致的数据建模，并集中管理 property 元数据。

A **shared property** is a property that can be used on multiple object types in your Ontology. Shared properties allow for consistent data modeling across object types and centralized management of property metadata.
[详细了解 shared properties。](/docs/foundry/object-link-types/shared-property-overview/)

[Learn more about shared properties.](/docs/foundry/object-link-types/shared-property-overview/)
### Link type
**Link Type**（链接类型）是两个 Object Type 之间关系的 schema 定义。**Link**（链接）是指两个 Object 之间该关系的单个实例。

A **link type** is the schema definition of a relationship between two object types. A **link** refers to a single instance of that relationship between two objects.
[了解更多关于 Link Type 的信息。](/docs/foundry/object-link-types/link-types-overview/)

[Learn more about link types.](/docs/foundry/object-link-types/link-types-overview/)
### Action type
**Action Type**（操作类型）是一组对 Object、Property 值和 Link 的更改或编辑的 schema 定义，用户可以一次性完成所有这些操作。Action Type 还包括当 Action 发生时执行的副作用行为。一旦在 Ontology 中配置了 Action Type，最终用户就可以通过应用 Action 来对 Object 进行更改。

An **action type** is the schema definition of a set of changes or edits to objects, property values, and links that a user can make all at once. Action types also include the side effect behaviors that happen when an Action occurs. Once an action type is configured in the Ontology, end users can make changes to objects by applying Actions.
[了解更多关于 Action Type 的信息。](/docs/foundry/action-types/overview/)

[Learn more about action types.](/docs/foundry/action-types/overview/)
### Object type groups
Object Type groups 是一种分类原语，可帮助用户更好地搜索和探索其 Ontology。

Object type groups are a classification primitive that helps users better search and explore their ontology.
[了解更多关于 Object Type groups 的信息。](/docs/foundry/object-link-types/type-groups/)

[Learn more about object type groups.](/docs/foundry/object-link-types/type-groups/)
### Interfaces
**Interface**（接口）是一种 Ontology 类型，用于描述 Object Type 的形状及其能力。Interface 提供 Object Type 多态性，允许对共享通用形状的 Object Type 进行一致的建模和交互。

An **interface** is an Ontology type that describes the shape of an object type and its capabilities. Interfaces provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape.
了解更多关于 [Interface](/docs/foundry/interfaces/interface-overview/) 的信息。

Learn more about [interfaces](/docs/foundry/interfaces/interface-overview/).
## Difference between object types and objects
为了阐明 Object Type 和 Object 之间的区别，下面提供了一些示例。请注意，同样的区别也适用于 Link Type 和 Link。

To clarify the difference between object types and objects, examples are provided below. Note that the same distinction applies to link types and links.
### Object type definitions
Object Type 定义（有时简称为 "Object Type"）是指关于 Ontology 实体（如 Object Type、Link Type 和 Action Type）的类型级信息。例如，Object Type 的元数据可以包括显示名称、Property 名称、Property 数据类型和描述。元数据并不指 Object Type 的 Property 或主键的实际数据或值；这些被视为 Ontology 数据。

Object type definitions, sometimes just referred to as "object types", refer to type-level information about ontology entities such as object types, link types, and action types. For example, the metadata for an object type may include display name, property names, property data types, and description. Metadata does not refer to the actual data or values of an object type’s properties or primary key; these are considered ontology data.
### Object instances
Object 实例（有时简称为 "Object"）是 Ontology 实体特定实例的实际主键和 Property 值。例如，一个 `Airplane` Object Type 可以有一个 Object 实例，其 `Plane ID` Property 的值为 `my_plane_id1`，`Maximum Occupancy` Property 的值为 `240`。

Object instances, sometimes just referred to as "objects", are the actual primary key and property values for specific instances of an ontology entity. For example, an `Airplane` object type can have an object instance with a `Plane ID` property having the value `my_plane_id1`, and a `Maximum Occupancy` property having value `240`.
## Value types
**Value Type**（值类型）是围绕 Field Type 的语义包装器，由元数据和约束组成，可以增强类型安全性、提高表达力并提供额外的上下文。Value Type 封装特定领域的数据类型，并以可在整个平台中重用的方式强制执行数据验证。常用的 Value Type 包括电子邮件地址、URL、UUID 和枚举。

**Value types** are semantic wrappers around a field type comprised of metadata and constraints that can enhance type safety, improve expressiveness, and provide additional context. Value types encapsulate domain-specific data types and enforce data validation in a manner reusable across the platform. Commonly used value types include email addresses, URLs, UUIDs, and enumerations.
虽然 Field Type 和 base type 是静态定义的，但 Value Type 是在给定 [space](/docs/foundry/security/orgs-and-spaces/) 的上下文中自定义的。因此，用户无法创建新的 Field Type 或 base type，但可以动态地创建 **Value Type**。

While field types and base types are defined statically, value types are customized within the context of a given [space](/docs/foundry/security/orgs-and-spaces/). As a result, users cannot create new field types or base types but are able to create **value types** dynamically.
[了解更多关于 Value Type 的信息。](/docs/foundry/object-link-types/value-types-overview/)

[Learn more about value types.](/docs/foundry/object-link-types/value-types-overview/)