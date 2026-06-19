<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/interface-overview/
---
# Interfaces
**Interface** 是 Ontology 中的一种类型，用于描述 object type 的形状（shape）及其能力。Interface 允许对共享公共形状的 object type 进行一致的建模和交互。例如，`Facility` interface 可能包含 `Facility Name` 和 `Location` properties。`Facility` 可以由 `Airport`、`Manufacturing Plant` 或 `Maintenance Hangar` 等 object type 实现，每个 object type 可以包含额外的、类型特定的 properties。

An **interface** is an Ontology type that describes the shape of an object type and its capabilities. Interfaces allow for consistent modeling of and interaction with object types that share a common shape. For example, a `Facility` interface may include `Facility Name` and `Location` properties. `Facility` could be implemented by object types such as `Airport`, `Manufacturing Plant`, or `Maintenance Hangar`, which could each contain additional type-specific properties.

> 📷 **[图片: `Facility` interface 的示例。]**

> 📷 **[图片: An example of a `Facility` interface.]**

通过使用 `Facility` interface，workflow 可以与 `Airport`、`Manufacturing Plant` 和 `Maintenance Hangar` object type 进行交互，无论是聚合方式还是独立方式，都无需了解这些 object type 的具体细节。此外，如果引入了实现 `Facility` interface 的新 object type，则该 workflow 将立即与新 object type 兼容，无需额外的重构。

By using the `Facility` interface, workflows can interact with `Airport`, `Manufacturing Plant`, and `Maintenance Hangar` object types, either in aggregate or independently, without needing to know specific details about those object types. Additionally, if new object types that implement the `Facility` interface are introduced, the workflow will be immediately compatible with the new object types without additional refactors.
请查看 [current levels of support](/docs/foundry/interfaces/interface-overview/#current-levels-of-support) 以了解有关在平台哪些位置可以使用 interface 的更多信息。

Review the [current levels of support](/docs/foundry/interfaces/interface-overview/#current-levels-of-support) to learn more about where you can use interfaces in the platform.
## Interface features
Interface 由 interface properties、[link type constraints](/docs/foundry/interfaces/interface-link-types-overview/) 以及有关该 interface 的 [metadata](/docs/foundry/interfaces/interface-metadata/) 组成。Interface properties 可以在 interface 上本地定义（推荐方式），也可以使用 [shared properties](/docs/foundry/object-link-types/shared-property-overview/) 进行定义。一个 interface 可以由多个 object type 实现。

An interface is composed of interface properties, [link type constraints](/docs/foundry/interfaces/interface-link-types-overview/), and [metadata](/docs/foundry/interfaces/interface-metadata/) about the interface. Interface properties can be defined locally on the interface (recommended) or using [shared properties](/docs/foundry/object-link-types/shared-property-overview/). An interface can be implemented by multiple object types.
与编程语言中的 interface 非常相似，您可以 [extend an interface](/docs/foundry/interfaces/extend-interface/) 来创建一个继承原始 interface properties 的子 interface，然后向子 interface 添加新的、更具体的 properties。然后，object type 可以 [implement the interface](/docs/foundry/interfaces/implement-interface/) 以表示它们符合该 interface 定义。Object type 可以实现多个 interface，以便在不同的 workflow 中使用。Interface 还可以扩展多个其他 interface，包括那些自身又扩展了其他 interface 的 interface，从而实现通过多层 interface 继承的 properties。

Much like interfaces in programming languages, you can [extend an interface](/docs/foundry/interfaces/extend-interface/) to create a child interface that inherits the properties of the original interface, then add new, more specific properties to the child interface. Object types can then [implement the interface](/docs/foundry/interfaces/implement-interface/) to indicate that they conform to the interface definition. Object types can implement multiple interfaces, for use in different workflows. Interfaces can also extend multiple other interfaces, including interfaces that themselves extend other interfaces, resulting in properties that are inherited through layers of interfaces.
## Differences between interfaces and object types
在 Ontology 中，interface 和 object type 之间在功能和样式上都存在差异。

There are both functional and stylistic differences between interfaces and object types within the Ontology.
Object type 是具体的（concrete）；它们具有由 shared 或 local properties 定义的 schema，由包含 property 值的 datasets 支持，并且可以实例化为 object。

Object types are concrete; they have schemas defined by shared or local properties, are backed by datasets containing property values, and can be instantiated as objects.
相比之下，interface 是抽象的；它们具有由 interface property 定义的 schema，不由数据集支持，不能直接实例化，但必须作为特定的 object type 进行实例化。

By contrast, interfaces are abstract; they have schemas defined by interface properties, are not backed by datasets, and cannot be instantiated directly but must be instantiated as a specific object type.
在样式上，interface 在平台中通过图标周围的虚线与 object type 进行视觉区分。

Stylistically, interfaces are visually distinguished from object types in the platform by having dashed lines around their icons.

> 📷 **[图片: Example interface icon]**

> 📷 **[图片: Example interface icon]**

## Interface permissions
Interface 通过 [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 进行权限管理。

Interfaces are permissioned through [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles).
## Current levels of support
随着对 interface Ontology 类型支持的不断扩展，其可用性在 Palantir 平台的各个应用之间会有所不同。

As support for interface Ontology types expands, availability will vary across the Palantir platform.
Interface 目前在以下应用程序和服务中受支持：

Interfaces are currently supported in the following applications and services:
* **[Ontology Manager](/docs/foundry/ontology-manager/overview/)**：定义、编辑和实现 interface。

* **[Marketplace](/docs/foundry/marketplace/overview/)**：打包和安装 interface。

* **[Functions](/docs/foundry/functions/overview/)**：TypeScript v2 functions。
* **[Ontology Manager](/docs/foundry/ontology-manager/overview/):** Define, edit, and implement interfaces.
* **[Marketplace](/docs/foundry/marketplace/overview/):** Package and install interfaces.
* **[Functions](/docs/foundry/functions/overview/):** TypeScript v2 functions.
Interface 在以下应用程序和服务中部分受支持：

Interfaces are partially supported in the following applications and services:
* **[Actions](/docs/foundry/action-types/overview/)**：定义用于创建、修改或删除实现 interface 的 object 的 action。Action 不能直接引用 interface link type 约束，但可以引用用于实现 interface link type 的具体 link type。

* **[Object Set Service](/docs/foundry/object-backend/overview/#object-set-service-oss)**：按 interface 搜索和排序 object。按 interface 进行聚合的支持正在开发中。对 interface link type 的支持正在开发中。

* **[Ontology SDK](/docs/foundry/ontology-sdk/overview/)**：将 interface 用作与实现 object type 交互的 API 层。支持的成熟度因语言而异；目前支持 TypeScript，Java 和 Python 的支持正在开发中。

* **[Actions](/docs/foundry/action-types/overview/):** Define actions to create, modify, or delete objects implementing an interface. Actions cannot reference interface link type constraints directly, but they can reference the concrete link types used to implement the interface link type.
* **[Object Set Service](/docs/foundry/object-backend/overview/#object-set-service-oss):** Search and sort objects by interfaces. Support for aggregating by interfaces is in development. Support for interface link types is in development.
* **[Ontology SDK](/docs/foundry/ontology-sdk/overview/):** Use interfaces as an API layer for interacting with implementing object types. Support varies by language; TypeScript is currently supported and support for Java and Python is in development.
Interface 正在积极开发中，但尚不支持以下内容：

Interfaces are under active development, but not yet supported in the following:
* **[Workshop](/docs/foundry/workshop/overview/)**
* **[Functions](/docs/foundry/functions/overview/)**：TypeScript v1 和 Python functions

* **[Workshop](/docs/foundry/workshop/overview/)**
* **[Functions](/docs/foundry/functions/overview/):** TypeScript v1 and Python functions
## Get started with interfaces
要将 interface 添加到您的 Ontology，您可以 [创建](/docs/foundry/interfaces/create-interface/) 新的 interface 或 [扩展](/docs/foundry/interfaces/extend-interface/) 现有的 interface。拥有 interface 之后，您可以使用具有适当结构的 object type [实现](/docs/foundry/interfaces/implement-interface/) 该 interface，或者随着 Ontology 的演进 [编辑](/docs/foundry/interfaces/edit-interface-definition/) 该 interface 以更好地适应您的组织。

To add interfaces to your Ontology, you can [create](/docs/foundry/interfaces/create-interface/) new interfaces or [extend](/docs/foundry/interfaces/extend-interface/) existing ones. Once you have an interface, you can then [implement](/docs/foundry/interfaces/implement-interface/) that interface with an object type of the appropriate shape or [edit](/docs/foundry/interfaces/edit-interface-definition/) it to better fit your Organization as your Ontology evolves.