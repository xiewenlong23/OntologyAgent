<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/core-concepts/
---
# Core concepts
This page describes major concepts related to the Ontology in Foundry.
This page describes major concepts related to the Ontology in Foundry.
## Ontology
An Ontology is a categorization of the world. In Foundry, the Ontology is the digital twin of an organization, a rich semantic layer that sits on top of the digital assets (datasets and models) integrated into Foundry. The Foundry Ontology creates a complete picture of an organization's world by mapping datasets and models to object types, properties, link types, and action types.
An Ontology is a categorization of the world. In Foundry, the Ontology is the digital twin of an organization, a rich semantic layer that sits on top of the digital assets (datasets and models) integrated into Foundry. The Foundry Ontology creates a complete picture of an organization’s world by mapping datasets and models to object types, properties, link types, and action types.
* An [object type](#object-type) defines an entity or event in an organization.
* A [property](#property) defines the object type's characteristics.
* A [link type](#link-type) defines the relationship between two object types.
* An [action type](#action-type) defines how an object type can be modified.
* An [object type](#object-type) defines an entity or event in an organization.
* A [property](#property) defines the object type’s characteristics.
* A [link type](#link-type) defines the relationship between two object types.
* An [action type](#action-type) defines how an object type can be modified.
The concepts that comprise the Ontology have parallels in the structure of a dataset. You can think of each object type as analogous to a dataset; an object is an instance of an object type, just as a row is one entry in a dataset. The columns in a dataset are analogous to properties of an object, as they provide additional information for a given row. The value in a dataset field (like a cell in a spreadsheet) is akin to the property value of an object. And just as datasets can be joined together in various ways, objects can have links between them based on property values. The table below summarizes this comparison:
The concepts that comprise the Ontology have parallels in the structure of a dataset. You can think of each object type as analogous to a dataset; an object is an instance of an object type, just as a row is one entry in a dataset. The columns in a dataset are analogous to properties of an object, as they provide additional information for a given row. The value in a dataset field (like a cell in a spreadsheet) is akin to the property value of an object. And just as datasets can be joined together in various ways, objects can have links between them based on property values. The table below summarizes this comparison:
|Datasets |Ontology       |
|---    |---            |
|Dataset  |Object type    |
|Row      |Object         |
|Column   |Property       |
|Field    |Property value |
|Join     |Link type      |
The diagram below demonstrates how these concepts can come together to create an Ontology. The content below continues to define the different components of the Ontology in more depth.
The diagram below demonstrates how these concepts can come together to create an Ontology. The content below continues to define the different components of the Ontology in more depth.

> 📷 **[图片: Aviation Ontology]**

> 📷 **[图片: Aviation Ontology]**

## Object type
An **object type** is the schema definition of a real-world entity or event. An **object** refers to a single instance of an object type; an object corresponds to a single real-world entity or event. An **object set** refers to a collection of multiple object instances; that is, an object set represents a group of real-world entities or events.
An **object type** is the schema definition of a real-world entity or event. An **object** refers to a single instance of an object type; an object corresponds to a single real-world entity or event. An **object set** refers to a collection of multiple object instances; that is, an object set represents a group of real-world entities or events.
[Learn more about object types.](/docs/foundry/object-link-types/object-types-overview/)
[Learn more about object types.](/docs/foundry/object-link-types/object-types-overview/)
## Property
A **property** of an object type is the schema definition of a characteristic of a real-world entity or event. A **property value** refers to the value of a property on an object, or a single instance of that real world entity or event.
A **property** of an object type is the schema definition of a characteristic of a real-world entity or event. A **property value** refers to the value of a property on an object, or a single instance of that real world entity or event.
[Learn more about properties.](/docs/foundry/object-link-types/properties-overview/)
[Learn more about properties.](/docs/foundry/object-link-types/properties-overview/)
## Shared property
**shared property（共享属性）** 是一种可在您的 Ontology 中多个 Object Type 上使用的 Property。共享属性允许跨 Object Type 进行一致的数据建模，并对 Property 元数据进行集中管理。

A **shared property** is a property that can be used on multiple object types in your ontology. Shared properties allow for consistent data modeling across object types and centralized management of property metadata.
[详细了解共享属性。](/docs/foundry/object-link-types/shared-property-overview/)

[Learn more about shared properties.](/docs/foundry/object-link-types/shared-property-overview/)
## Link type
**link type（关联类型）** 是两个 Object Type 之间关系的 schema 定义。**link（关联）** 指的是两个 Object 之间该关系的单个实例。

A **link type** is the schema definition of a relationship between two object types. A **link** refers to a single instance of that relationship between two objects.
[详细了解关联类型。](/docs/foundry/object-link-types/link-types-overview/)

[Learn more about link types.](/docs/foundry/object-link-types/link-types-overview/)
## Action type
**action type（操作类型）** 是用户可一次性对 Object、Property 值和 Link 所做的一组更改或编辑的 schema 定义。它还包括操作提交时发生的副作用行为。一旦在 Ontology 中配置了 Action Type，最终用户就可以通过应用 Action 来对 Object 进行更改。

An **action type** is the schema definition of a set of changes or edits to objects, property values, and links that a user can take at once. It also includes the side effect behaviors that occur with action submission. Once an action type is configured in the Ontology, end users can make changes to objects by applying actions.
[详细了解操作类型。](/docs/foundry/action-types/overview/)

[Learn more about action types.](/docs/foundry/action-types/overview/)
## Roles
**Roles（角色）** 是 Ontology 中集中的权限模型。与 Foundry 文件系统中的角色类似，Ontology 角色授予对 Ontology 资源的访问权限。角色可以在 Ontology 级别或各个资源级别授予。

**Roles** are the central permissioning model in the Ontology. Similar to roles in the Foundry filesystem, Ontology roles grant access to ontological resources. Roles can be granted on the Ontology level or the individual resource level.
详细了解 [Ontology 角色](/docs/foundry/object-permissioning/ontology-permissions/) 及其在 Object Type、Link Type 和 Action Type 中的使用方式。

Learn more about [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions/) and how they are used for object types, link types, and action types.
## Functions
**Function（函数）** 是一段基于代码的逻辑，它接收输入参数并返回输出。Function 与 Ontology 原生集成：它们可以接收 Object 和 Object Set 作为输入，读取 Object 的 Property 值，并可用于跨 Action Type 和基于 Ontology 构建的应用程序。

A **function** is a piece of code-based logic that takes in input parameters and returns an output. Functions are natively integrated with the Ontology: they can take objects and object sets as input, read property values of objects, and be used across action types and applications that build on the Ontology.
[详细了解 Function 概述](/docs/foundry/functions/overview/)，或 [详细了解基于 Ontology 的 Function](/docs/foundry/functions/functions-on-objects/)。

[Learn more about Functions in general](/docs/foundry/functions/overview/), or [learn more about Ontology-based Functions](/docs/foundry/functions/functions-on-objects/).
## Interfaces
**Interface（接口）** 是一种 Ontology 类型，用于描述 Object Type 的形状及其功能。Interface 提供 Object Type 多态性，允许对共享通用形状的 Object Type 进行一致的建模和交互。

An **interface** is an Ontology type that describes the shape of an object type and its capabilities. Interfaces provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape.
详细了解 [Interface](/docs/foundry/interfaces/interface-overview/)。

Learn more about [interfaces](/docs/foundry/interfaces/interface-overview/).
## Object Views
**Object Views（对象视图）** 是与特定 Object 相关的所有信息和 Workflow 的中心枢纽。其中包括 Object 的关键信息、任何关联的 Object 和相关的 Metric，以及与该 Object 相关的分析、仪表板和应用程序。

**Object Views** are a central hub for all information and workflows related to a particular object. This includes key information about an object, any linked objects, and related metrics, as well as analyses, dashboards, and applications related to the object.
[详细了解对象视图。](/docs/foundry/object-views/overview/)

[Learn more about Object Views.](/docs/foundry/object-views/overview/)