<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/metadata-statuses/
---
# Statuses
Ontology 中的每个 object type、property、link type、action 或 interface 都有一个 **status**，用于表示其开发状态。本体资源的 status 可以是 active、experimental、deprecated 或 example；object types 还可以被分类为 [promoted](#promoted-status-object-types-only)。Status 元数据有助于 Ontology 编辑用户了解哪些资源正被用户应用程序主动依赖。这些 status 可以在 [**Object Explorer**](/docs/foundry/object-explorer/overview/)、[**Object Views**](/docs/foundry/object-views/overview/) 和 [**Workshop**](/docs/foundry/workshop/overview/) 中查看，以提供有关哪些 object types 预期用于用户应用程序的更多信息。

Every object type, property, link type, action, or interface in the Ontology has a **status** that indicates developmental state. An ontological resource's status can be either active, experimental, deprecated, or example; object types can also be classified as [promoted](#promoted-status-object-types-only). Status metadata helps Ontology-editing users to know what resources are being actively relied on by user applications. These statuses are viewable in [**Object Explorer**](/docs/foundry/object-explorer/overview/), [**Object Views**](/docs/foundry/object-views/overview/), and [**Workshop**](/docs/foundry/workshop/overview/) to provide more information about which object types are intended for use in user applications.

> 📷 **[图片: Active status]**

> 📷 **[图片: Active status]**

该 status 可以取以下五个值之一：

The status can take on one of five values:
## Available Status Values
* **Promoted (object types only)：** 表示该 object type 是核心的、可信赖的资源，已通过 ontology 负责人的审核。`Promoted` object types 在 API 命名方面继承与 `active` object types 类似的保护机制。

* **Active：** 表示该资源正在用户面向的应用程序中积极使用，并且不会在 Ontology Manager 中进行重大破坏性更改。

* **Experimental：** 表示该资源仍在开发中。可能会进行某些更改，导致实验性项在用户面向的应用程序中不可用。

* **Deprecated：** 表示该资源将很快被删除。在用户面向的应用程序中不应依赖已弃用的项。
* 已弃用的资源还具有包含以下信息的元数据：
* 说明其被弃用的原因；
* 预计从系统中删除的截止日期；以及
* 旨在替代已弃用资源的对象。

* **Example：** 表示该资源已作为示例安装。示例资源是概念性的，仅适用于培训或早期探索性使用。Examples *不* 预期用于生产工作流。

* **Promoted (object types only):** Indicates that the object type is a core, trusted resource that has been vetted by an ontology owner. `Promoted` object types inherit similar protections as `active` object types for API names.
* **Active:** Indicates that the resource is actively in use in user-facing applications and major breaking changes will not be made in the Ontology Manager.
* **Experimental:** Indicates that the resource is still under development. Changes may be made that make the experimental item unavailable in user facing applications.
* **Deprecated:** Indicates that the resource will soon be deleted. The deprecated item should not be relied on in user facing applications.
* A deprecated resource also has metadata that includes:
* A description for why it is being deprecated;
* A deadline for when it is expected to be deleted from the system; and
* The resource that is meant to replace the one that is deprecated.
* **Example:** Indicates that the resource has been installed as an example. Example resources are notional and are only suitable for trainings or early-stage, exploratory use. Examples are *not* intended for use in production workflows.
### `Promoted` status (object types only)
Object types 支持一种特殊的 `promoted` status，以表示其在 ontology 中具有更高级别的可信度和官方地位。该 status 由一个新的紫色对勾图标表示，有助于用户区分核心的可复用 object types 与更特定于用例的或实验性的 object types。

Object types support a special `promoted` status to signify a higher level of trust and official standing within the ontology. This status, represented by a new purple checkmark icon, helps users differentiate core, reusable object types from more use-case-specific or experimental ones.
`promoted` status 提供了超越标准 `active` status 的突出地位。具有该 status 的 object type 旨在被视为"核心"资源，遵循高标准并由中央团队管理。`Promoted` object types 继承与 `active` status 相似的运营保护机制，例如对删除操作的限制。

The `promoted` status provides prominence beyond the standard `active` status. An object type with this status is meant to be considered a "core" resource, held to high standards and managed by a central team. `Promoted` object types inherit similar operational protections of the `active` status, such as restrictions on deletion.
`promoted` 状态的主要特征包括:

Key characteristics of the `promoted` status include:
* **作用域:** `promoted` 状态仅适用于 object types,不适用于 properties、link types、action types 或 interfaces。

* **可见性:** 将 object type 的状态设置为 `promoted` 将自动将其可见性设置为 `prominent`,从而提高其在整个平台上的可发现性。用户可以选择性地将 object type 的所有 properties 移至 `active` 状态。
* **权限:**

* 只有在 ontology 级别具有 `Ontology Owner` 角色的用户才能直接应用 `promoted` 状态。

* 其他用户必须提交提案,由 ontology 级别的 `Ontology Owner` 审核批准后才能应用该状态。

* **Scope:** The `promoted` status applies only to object types. It is not available for properties, link types, action types or interfaces.
* **Visibility:** Setting an object type's status to `promoted` will automatically set its visibility to `prominent`, increasing its discoverability across the platform. Users can optionally move all properties of the object type to `active` status.
* **Permissions:**
* Only users with the `Ontology Owner` role on the ontology level can directly apply the `promoted` status.
* Other users must submit a proposal for review and approval by an `Ontology Owner` on the ontology level to apply the status.

> 📷 **[图片: Promoted Object Type Example]**

> 📷 **[图片: Promoted Object Type Example]**

## Operations that are not allowed
鉴于应用程序依赖 ontology 资源,当资源的状态为 `active` 时,存在若干可能具有破坏性的操作是不被允许的:

Given that applications rely on ontological resources, there are several potentially destructive operations that are not allowed when a resource has the status `active`:
* 资源无法被删除。资源的状态必须为 `experimental` 或 `deprecated` 才能被删除。

* 处于 active 状态的资源的 API 名称无法被更改。只有标记为 `experimental` 的资源才能更改 API 名称。

* It cannot be deleted. A resource’s status must be `experimental` or `deprecated` before it can be deleted.
* The API name of an active resource cannot be changed. Changing an API name is only possible for those marked as `experimental`.
## Edit a status
默认情况下,任何新的 ontology 资源都将被赋予 `experimental` 状态。要更改状态:

By default, any new ontological resource will be given the `experimental` status. To change the status:
1. 选择当前状态旁边的下拉菜单。
2. 选择新状态。

1. Select the dropdown next to the current status.
2. Select the new status.
当将资源更改为 `deprecated` 状态时,系统将提示您:

When changing a resource to the `deprecated` status, you will be prompted to:
* 填写描述说明其被弃用的原因,
* 输入预计从系统中删除的截止日期,以及
* (可选)选择用于替代您正在弃用的资源的资源。

* Fill out a description for why it is being deprecated,
* Input a deadline for when you expect it to be deleted from the system, and
* Optionally, select a resource that is meant to replace the one you are deprecating.
这些状态可在 Object Explorer、Object Views 和 Workshop 中查看,以提供有关哪些 object types 旨在用于用户应用程序的更多信息。

These statuses are viewable in Object Explorer, Object Views, and Workshop to provide more information about which object types are intended for use in user applications.

> 📷 **[图片: Change status]**

> 📷 **[图片: Change status]**

Ontology Manager 确保 object type 与其相关 properties 或 link types 之间的状态一致性。例如,如果一个 object type 从 `active` 更改为 `experimental`,则其所有 properties 也将被标记为 `experimental`。

The Ontology Manager ensures status consistency between an object type and its related properties or link types. For example, if an object type is changed from `active` to `experimental`, all of its properties will be marked `experimental` as well.
下表指明了 link type 在不同状态 object types 之间的可用状态。一般来说:

The table below indicates available statuses for a link type between object types of different statuses. In general:
* 如果 link type 中的至少一个 object type 更改为 `experimental`,则该 link type 将自动更改为 `experimental`。

* 如果 link type 中的至少一个 object type 更改为 `example`,则该 link type 将自动更改为 `example`。

* 如果 link type 中的至少一个 object type 更改为 `deprecated`,则该 link type 将自动更改为 `deprecated`。

* If at least one object type in a link type is changed to `experimental`, the link type will automatically be changed to `experimental`.
* If at least one object type in a link type is changed to `example`, the link type will automatically be changed to `example`.
* If at least one object type in a link type is changed to `deprecated`, the link type will automatically be changed to `deprecated`.
|*If object type A is…* |and object type B is…  |
|---    |---    |
| |EXPERIMENTAL |ACTIVE |DEPRECATED |
|*EXPERIMENTAL* |experimental only  |experimental only  |deprecated only    |
|*ACTIVE*   |experimental only  |can be experimental, active, or deprecated |deprecated only    |
|*DEPRECATED*   |deprecated only    |deprecated only    |deprecated only    |
link type 的外键也适用相同的要求。应用程序在更改 property 时将更改 link type 的状态:

The same requirements are true of foreign keys of a link type. The application will change the status of a link type when changing a property:
* 如果将一个外键 property 改为 `experimental`,其 link type 将被改为 `experimental`。

* 如果将一个外键 property 改为 `example`,其 link type 将被改为 `example`。

* 如果将一个外键 property 改为 `deprecated`,其 link type 将被改为 `deprecated`。

* If a foreign key property is changed to `experimental`, its link type will be changed to `experimental`.
* If a foreign key property is changed to `example`, its link type will be changed to `example`.
* If a foreign key property is changed to `deprecated`, its link type will be changed to `deprecated`.
应用程序会更改 status 以防止出现无效状态。如果一个外键 property 是 `experimental` 且仍在开发中,其 link type 不应被标记为 `active` 并在生产环境中被依赖。相比之下,当将一个 property 标记为 `active` 时,应用程序不会将以该 property 作为外键引用的 link type 更改为 `active`,因为外键 property 在生产环境中有效,而 link type 及其支持的数据源可能仍在开发中。

The application changes statuses in order to prevent invalid states. If a foreign key property is `experimental` and still being developed, its link type shouldn't be marked `active` and be relied on in production. In contrast, when marking a property `active`, the application won't change a link type referencing the property as its foreign key to `active`, as it is valid for a foreign key property to be in production, while the link type and its backing datasource are still in development.
## Bulk edit statuses
### Properties
当将一个 object type 从 `experimental` 更改为 `active` 时,可以选择同时将 `active` 状态应用于该 object type 上的所有 properties:

When changing an object type from `experimental` to `active`, there is the option to also apply the `active` status to all properties on the object type:

> 📷 **[图片: Apply active status]**

> 📷 **[图片: Apply active status]**

当您将一个 object type 更改为 `example` 时,其所有 properties 也会自动变为 `example`。

When you change an object type to `example`, all of its properties will automatically become `example` also.
也可以从 object type 的 **Properties** 页面批量编辑该 object type properties 的 status。[阅读有关批量编辑 properties 的更多信息。](/docs/foundry/object-link-types/edit-properties/#bulk-edit-multiple-properties)

Statuses across properties of an object type can also be edited in bulk from the **Properties** page of the object type. [Read more about bulk editing properties.](/docs/foundry/object-link-types/edit-properties/#bulk-edit-multiple-properties)
### Object types
也可以从主页 object 视图页面批量编辑 object types 的 status,方法是选中要编辑的 object types 的复选框,然后点击表格右上角的 **Edit status** 按钮。

Statuses across object types can also be edited in bulk from the home page object view page by selecting the checkboxes of the object types to edit and selecting the **Edit status** button at the top right of the table.

> 📷 **[图片: Bulk edit object types]**

> 📷 **[图片: Bulk edit object types]**

## Troubleshooting
### Conflicts between property status and link type status
如果您收到错误 `OntologyMetadata:ConflictBetweenLinkTypeStatusAndPropertyTypeStatus`,则表示 link type 的 status 与 property 的 status 存在冲突。例如,如果一个外键是 `deprecated`,引用该外键的 link types 也应为 `deprecated`。

If you receive the error `OntologyMetadata:ConflictBetweenLinkTypeStatusAndPropertyTypeStatus`, there is a conflict between the status on a link type and the status on a property. For example, if a foreign key is `deprecated`, link types that reference that foreign key should also be `deprecated`.
### Conflicts between object type status and link type status
如果您收到错误 `OntologyMetadata:ConflictBetweenLinkTypeStatusAndObjectTypeStatus`,则表示 link type 的 status 与其关联的某个 object type 的 status 之间存在冲突。根据上表,当存在无效的 object type-link type 组合时,可能会发生这种情况。例如,一个 `experimental` object type 不能有一个 `active` link type。

If you receive the error `OntologyMetadata:ConflictBetweenLinkTypeStatusAndObjectTypeStatus`, there is a conflict between the status on a link type and the status of one of its associated object types. This can happen when there is an invalid object type-link type case according to the table above. For example, an `experimental` object type cannot have an `active` link type.