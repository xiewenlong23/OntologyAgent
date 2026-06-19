<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions-legacy/
---
# Ontology permissions \[Legacy]
> **⚠️ 警告: Ontology 资源现在通过 Compass 进行权限管理**

> Ontology 资源（object types、action types、link types、shared properties 和 interfaces）可以是 [通过 Compass 文件系统管理的常规项目资源。](/docs/foundry/object-permissioning/ontology-permissions/)这取代了之前的 ontology roles 和源自数据源的权限模型。有关更多信息，请 [查阅关于 Ontology 权限的更新文档。](/docs/foundry/object-permissioning/ontology-permissions/)
> **⚠️ 警告: Ontology resources now permissioned via Compass**

> Ontology resources (object types, action types, link types, shared properties, and interfaces) can be [regular project resources managed through the Compass filesystem.](/docs/foundry/object-permissioning/ontology-permissions/). This replaces the previous ontology roles and datasource-derived permission models. For more information, [review the updated documentation on Ontology permissions.](/docs/foundry/object-permissioning/ontology-permissions/)
Ontology 资源指的是 object types、link types 和 action types 及其元数据（schema）。

Ontology resources refer to object types, link types, and action types along with their metadata (schema).
您可能会遇到适用于您注册账户的两种旧版权限模型中的一种：

You may encounter one of two legacy permission models applicable to your enrollment:
1. **[Ontology roles](#ontology-roles)** 是授权 Ontology 资源的默认方法。Ontology roles 支持将 [roles](#ontology-roles) 直接应用于每个 Ontology 资源，而与其底层 datasource 无关。

1. **[Ontology roles](#ontology-roles)** are the default method for authorizing Ontology resources. Ontology roles enable the direct application of [roles](#ontology-roles) onto each Ontology resource, independent of its backing datasource.
* 例如，用户仅需要在 object type 上具有 `Ontology Editor` 角色，而无需在底层 datasource 上具有任何权限，即可编辑 Ontology 中的 object type。

* `Ontology Editor` 角色仅允许编辑 Ontology 资源及其元数据，并不授予对数据或 datasource 本身的任何权限。对 object data（非元数据）的访问仍由底层 datasource 上授予的权限控制。

* For example, a user only requires the `Ontology Editor` role on the object type and does not require any permissions on the backing datasource to edit an object type in the Ontology.
* The `Ontology Editor` role only allows editing Ontology resources and their metadata and does not grant any permission on the data or datasource itself. Access to object data (not metadata) is still governed by the permissions granted on backing datasources.
2. **[Datasource-derived permissions](#datasource-derived-permissions)** 是授权 Ontology 资源的旧版解决方案。Datasource-derived permissions 依赖于每个 object type 的底层 datasource 上定义的权限，在 Ontology 中的 object type 与底层 datasource 之间创建直接的 1:1 依赖关系。因此，具有 datasource-derived permissions 的 object type 需要一个底层 dataset。

2. **[Datasource-derived permissions](#datasource-derived-permissions)** are the legacy solution for authorizing Ontology resources. Datasource-derived permissions rely on the permissions defined on the backing datasource for each object type, creating a direct 1:1 dependency between object types in the Ontology and the backing datasource. For this reason, object types with datasource-derived permissions require a backing dataset.
* 例如，用户必须具有对底层 datasource 的 `Editor` 访问权限，并且是 [`Ontology Administrators` group](/docs/foundry/platform-security-management/manage-groups/) 的成员（在 Ontology 级别），才能编辑 Ontology 中的 object type。

* For example, a user must have `Editor` access to the backing datasource and be a member of the [`Ontology Administrators` group](/docs/foundry/platform-security-management/manage-groups/) (at the Ontology level) to edit an object type in the Ontology.
## Ontology roles
Ontology roles 定义如下：

Ontology roles are defined as:
* `Ontology Owner`：可以编辑 Ontology 资源并完全控制其安全性和共享

* `Ontology Editor`：可以编辑 Ontology 资源

* `Ontology Viewer`：可以查看 Ontology 资源，但不能编辑它们

* `Ontology Discoverer`：仅可查看 Ontology 资源的名称和元数据，不包括 schema

* `Ontology Owner`: Can edit Ontology resources and has full control over their security and sharing
* `Ontology Editor`: Can edit Ontology resources
* `Ontology Viewer`: Can view Ontology resources, but cannot edit them
* `Ontology Discoverer`: Can only see Ontology resource names and metadata, excluding schema
除了直接在 Ontology 资源上授予上述角色外，您还可以在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 应用程序中导航到 Ontology 的 **Ontology Configuration** 选项卡，在 Ontology 级别授予这些角色。只有在 Ontology 级别授予的 `Ontology owner` 角色会被该 Ontology 中的所有资源继承；`Ontology editor` 角色仅与 Ontology 级别的权限相关。

In addition to directly granting the above roles on Ontology resources, you can also grant these roles at the Ontology level by navigating to the **Ontology Configuration** tab of an Ontology in the [Ontology Manager](/docs/foundry/ontology-manager/overview/) application. Only the `Ontology owner` role, granted at the Ontology level, is inherited by all the resources in that Ontology; the `Ontology editor` role is only relevant for Ontology-level permissions.
作为最佳实践，我们强烈建议定义一个负责整个 Ontology 的可信用户组（也称为 Ontology Governance Board），并授予该用户组对整个 Ontology 的 `Ontology Owner` 角色。

As a best practice, we strongly recommended defining a trusted group of users that would be responsible for the Ontology as a whole (also referred to as the Ontology Governance Board) and grant that user group the `Ontology Owner` role for the entire ontology.
> **⚠️ 警告**

> 可以根据不同用户组的具体需求，自定义默认 Ontology 角色中包含的操作或配置其他自定义角色。有关角色及其自定义方式的更多信息，请参阅 [documentation on roles](/docs/foundry/security/projects-and-roles/#roles)。
> **⚠️ 警告**

> It is possible to customize the operations included in a default Ontology role or configure additional custom roles depending on the specific needs of different user groups. For more information on roles and how they can be customized, refer to the [documentation on roles](/docs/foundry/security/projects-and-roles/#roles).
### Create new resources with Ontology roles
Ontology 中的资源创建仅限于在 Ontology 级别具有 `Ontology Owner` 或 `Ontology Editor` 角色的用户。新创建的 object type、link type、shared property 和 Action types with roles 将默认显示创建用户为该资源上的 `Ontology Owner`，而所有其他用户默认为 `Ontology Viewer`。资源创建后，创建用户可以向该资源应用其他角色。

Resource creation in the Ontology is restricted to users with `Ontology Owner` or `Ontology Editor` roles at the Ontology level. Newly created object types, link types, shared properties, and Action types with roles will show the creating user as an `Ontology Owner` on that resource and all other users as an `Ontology Viewer` by default. Once the resource is created, the creating user can apply further roles to the resource.
> **ℹ️ 注意**

> 默认情况下，每个用户都被授予 Ontology 级别的 `Ontology Editor` 角色，并可以为其工作流创建新的 Ontology 资源。要自定义允许哪些用户组添加新的 Ontology 资源，`Ontology Owner` 可以导航到 Ontology Manager 中的 **Ontology configuration** 选项卡，并调整 Ontology 级别的角色授予。
> **ℹ️ 注意**

> By default, every user is granted the `Ontology Editor` role at the Ontology level and can create new Ontology resources for their workflows. To customize which user groups are allowed to add new Ontology resources, an `Ontology Owner` can navigate to the **Ontology configuration** tab in Ontology Manager and adjust the Ontology-level role grants.
### Type-specific edit permissions with Ontology roles
#### Permissions for editing object types and their properties
要对 object type 及其 properties 进行更改，用户必须对该 object type 具有 `Ontology Editor` 权限。如果用户希望将 datasources/columns 映射到 object type properties，则还需要对被映射的 datasource 具有 `Viewer` 权限。

To make changes to an object type and its properties, a user must have `Ontology Editor` permission on the object type. If the user would like to map datasources/columns to object type properties, then `Viewer` permissions to the datasource that is being mapped is also required.
#### Permissions for shared properties
要对 [shared property](/docs/foundry/object-link-types/shared-property-overview/) 进行更改，用户必须对该 shared property 具有 `Ontology Editor` 权限。用户必须对希望添加该 shared property 的任何 object type 具有 `Ontology Editor` 权限。

To make changes to a [shared property](/docs/foundry/object-link-types/shared-property-overview/), a user must have `Ontology Editor` permissions on the shared property. The user must have `Ontology Editor` on any object types to which the user wishes to add the shared property.
#### Permissions for editing link types
要对 link type 进行更改（创建、删除、更新等），用户必须具有以下权限：

To make changes to a link type (create, delete, update, and so on), a user must have the following permissions:
* 在 link type 两端引用的 object type 上具有 `Ontology viewer` 权限。

* 在 link type 本身具有 `Ontology editor` 权限。

* `Ontology viewer` permission on the object types referenced on both sides of the link type.
* `Ontology editor` permission on the link type itself.
如果 link type 使用 join table（关联表），并且所做的修改涉及对 join table 的更改，则还需要对支撑该 link type 的 join table datasource 具有 `Viewer` 权限。

If the link type uses a join table and the modification made involves changes to the join table, then `Viewer` permissions to the join table datasource backing the link type is also required.
#### Permissions for editing action types
要修改 action type（创建、删除、更新等），用户必须具有以下权限：

To make changes to an action type (create, delete, update, and so on), a user must have the following permissions:
* 至少具有该 action type 的 `Editor` 权限，无论是直接拥有还是通过 [ontology 层级](#ontology-roles) 的继承获得

* 对该 action type 在执行期间可能生成编辑的所有 object type 具有 `Ontology Editor` 权限。

* At least `Editor` permissions of the action type, either directly or through inheritance from the [ontology level](#ontology-roles)
* `Ontology Editor` on all object types for which the action type can generate edits during execution.
Action type 可能生成编辑的 object type 包括以下内容：

The object types for which an action type can generate edits include the following:
* 在 create、modify 和 delete object rules 中引用的 object type。

* 与 create 和 delete link rules 中引用的 link type 相关联的 object type。

* 在 function-backed Action 的 function 中被编辑的 object type。

* [Action Log](/docs/foundry/action-types/action-log/#action-log) object type（如果已配置）。

* Object types referenced in create, modify, and delete object rules.
* Object types connected to link types referenced in create and delete link rules.
* Object types edited in functions of function-backed Actions.
* The [Action Log](/docs/foundry/action-types/action-log/#action-log) object type (if one is configured).
### Read-only views
当用户无权编辑某个 object type、link type、shared property 或 action type 时，编辑视图将被禁用，并且会通过横幅向用户说明其拥有和不拥有的权限。

When a user does not have access to edit an object type, link type, shared properties, or action type, the edit views will be disabled and a banner will explain to the user what permissions they do and do not have.
![The view permission banner displays access information for users with viewer role.](/docs/resources/foundry/object-permissioning/oma-user-interface-view-permission.png)
![The discover permission banner shows limited access for users with discoverer role.](/docs/resources/foundry/object-permissioning/oma-user-interface-discover-permission.png)
## Datasource derived permissions
* [查看权限](#view-permissions)

* [类型特定的编辑权限](#type-specific-edit-permissions)

* [编辑 object type 及其 property 的权限](#permissions-for-editing-object-types-and-their-properties)

* [Shared property 的权限](#permissions-for-shared-properties)

* [编辑 link type 的权限](#permissions-for-editing-link-types)

* [编辑 action type 的权限](#permissions-for-editing-action-types)

* [只读视图](#read-only-views)

* [View permissions](#view-permissions)
* [Type-specific edit permissions](#type-specific-edit-permissions)
* [Permissions for editing object types and their properties](#permissions-for-editing-object-types-and-their-properties)
* [Permissions for shared properties](#permissions-for-shared-properties)
* [Permissions for editing link types](#permissions-for-editing-link-types)
* [Permissions for editing action types](#permissions-for-editing-action-types)
* [Read-only views](#read-only-views)
### View permissions
对支撑 object type 或 link type 的 datasource 具有 `Viewer` 权限，使用户能够查看与该特定 datasource 相关联的 object type 或 link type。

Having `Viewer` permissions on the datasource backing an object type or link type allows users to see the object type or link type associated with that specific datasource.
默认情况下，***action type 对所有有权访问 Ontology 的用户可见***。在 datasource-derived 权限模型下，所有用户都将能够查看所有 action type 的标题、描述和 rules。

By default, ***action types are visible to all the users*** who have access to the Ontology. All users will be able to see the title, description, and rules of all action types with the datasource-derived permissions model.
### Type-specific edit permissions
要在 Ontology Manager 中进行任何更改，用户必须是 `Ontology Administrators` 用户组的成员。阅读更多关于 [组和平台安全性](/docs/foundry/platform-security-management/manage-groups/) 的信息。

To make any changes in the Ontology Manager, a user must be a member of the `Ontology Administrators` user group. Read more about [groups and platform security](/docs/foundry/platform-security-management/manage-groups/).
当使用 datasource-derived 权限时，用户可能需要额外的类型特定权限才能成功地在 Foundry Ontology 中进行更改。

A user may need additional type-specific permissions to successfully make changes in the Foundry Ontology when datasource-derived permissions are used.
#### Permissions for editing object types and their properties
要对 object type 及其 property 进行任何更改，用户必须对支撑该 object type 的 datasource 具有 `Editor` 权限。

In order to make any changes to an object type and its properties, a user must have `Editor` permissions to the datasources backing the object type.
#### Permissions for shared properties
要创建或编辑 [shared property](/docs/foundry/object-link-types/shared-property-overview/)，或将 shared property 添加到 object type，用户必须是 `Ontology Administrators` 组的成员。

To create or edit a [shared property](/docs/foundry/object-link-types/shared-property-overview/) or add a shared property to an object type, a user must be a member of the `Ontology Administrators` group.
#### Permissions for editing link types
要对 link type 进行任何更改，用户必须对支撑该 link type 的 datasource 具有 `Editor` 权限，并且对 link type 中引用的两个 object type 所支撑的 datasource 具有 `Viewer` 权限。

In order to make any changes to a link type, a user must have `Editor` permissions to the datasources backing the link type and `Viewer` permissions on the datasources backing both object types referenced in the link type.
#### Permissions for editing action types
* 所有拥有 Ontology 访问权限的用户都可以查看完整的 action types（例如可编辑属性、名称或用户权限）。

* 要对 Ontology 中的 action type 进行更改（创建、删除、更新等），用户必须是 `Ontology Administrators` 组的成员。

* 要运行该 action，用户必须在所有被编辑的 object types 上具有 `Viewer` 权限。

* 如果用户创建的 action 会修改或添加某个 object type，则必须为该 object type 启用 `Edits` 选项。

* All users with access to an Ontology can view the complete action types (editable properties, name, or user permissions, for example).
* To make changes to an action type in an Ontology (create, delete, update, and so on), a user must be a member of the `Ontology Administrators` group.
* To run the action, the user must be a `Viewer` on all the edited object types.
* If a user creates an action that modifies or adds to an object type, the `Edits` option must be enabled for that object type.
有关 action types 权限的更多信息，请参阅[文档](/docs/foundry/action-types/permissions/#permissions)。

For more information on action types permissions, review the [documentation](/docs/foundry/action-types/permissions/#permissions).
### Read-only views
当用户没有编辑 object type、link type 或 action type 的权限时，编辑视图将被禁用，并且会向用户显示一个横幅，说明他们拥有和不拥有的权限。

When a user does not have access to edit an object type, link type, or action type, the edit views will be disabled and a banner will explain to the user what permissions they do and do not have.
### Deleting the backing dataset
如果具有 datasource-derived permissions 的 object type 的 backing dataset 已从回收站中永久删除，则该 object type 被视为孤立（orphaned）。由于权限源自 backing dataset，而该 dataset 已无法被访问，因此用户将无法再修改该 object type，因为所有编辑者权限都已丢失。Ontology 会自动删除孤立的 object types。

If the backing dataset of an object type with datasource-derived permissions has been permanently deleted from the trash, the object type is considered orphaned. Since permissions are derived from the backing dataset, which can no longer be accessed, users can no longer modify the object type as all editor permissions have been lost. The ontology automatically deletes orphaned object types.
> **⚠️ 警告: Warning**

> 对于 datasource-derived permissions，所有 object types 必须具有一个 backing dataset。为防止不可编辑的 ontology types 不断累积，具有 datasource-derived permissions 但没有 backing dataset 的 object types 将在 24 小时后被移除。
> **⚠️ 警告: Warning**

> For datasource-derived permissions, all object types must have a backing dataset. To prevent an accumulation of non-editable ontology types, object types with datasource-derived permissions but no backing dataset will be removed after 24 hours.