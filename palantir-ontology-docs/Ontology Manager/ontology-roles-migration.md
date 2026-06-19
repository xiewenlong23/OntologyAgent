<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/ontology-roles-migration/
---
# Ontology roles migration \[Legacy]
> **ℹ️ 注意: Legacy**

> 本页描述的是一个已不再是最新的 ontology 资源权限配置方法的旧版流程。Ontology 资源现在可以通过 [使用 Compass 文件系统进行权限配置](/docs/foundry/object-permissioning/ontology-permissions/)。要进行迁移，请 [查看迁移指南。](/docs/foundry/ontology-manager/migrate-to-project-based-permissions/)
> **ℹ️ 注意: Legacy**

> This page describes a legacy process that is no longer the most up-to-date method for ontology resource permissioning. Ontology resources can now be [permissioned using the Compass filesystem](/docs/foundry/object-permissioning/ontology-permissions/). To migrate over, [review the migration guide.](/docs/foundry/ontology-manager/migrate-to-project-based-permissions/)
[Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 是一种针对 ontology 资源的旧版授权模型，取代了 [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#datasource-derived-permissions)。Ontology roles 适用于 object types、link types 和 action types，这些统称为 "ontology 资源"。要使用 ontology 的最新功能（包括 shared property types、interfaces 等）必须配置 ontology roles。默认情况下，自 2023 年 9 月以来创建的所有新 enrollment 都已使用 ontology roles。

[Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) is a legacy authorization model for ontology resources, replacing [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#datasource-derived-permissions). Ontology roles apply to object types, link types, and action types, which are referred to as “ontology resources”. Ontology roles are required to use the most recent features of the ontology, including shared property types, interfaces, and more. By default, ontology roles have been used on all new enrollments created since September 2023.
Ontology roles 允许你直接在每个 Ontology 资源及其元数据上授予角色。所有元数据权限均在 Ontology Manager 中进行管理。Ontology roles 允许你将 Ontology 资源（例如 `Aircraft` object type）与其*数据*（例如 [object instances](/docs/foundry/object-link-types/object-types-overview/)（如表示为 Ontology object 的特定飞机）和 link instances）解耦；这些数据实例仍由其输入 datasource 权限进行管理。详细了解 [Ontology permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/)。

Ontology roles allow you to grant roles *directly* on each Ontology resource and to their metadata. All metadata permissions are managed in Ontology Manager. Ontology roles allow you to decouple Ontology resources (like an `Aircraft` object type) from the *data* of these resources, such as [object instances](/docs/foundry/object-link-types/object-types-overview/) (like a specific plane represented as an Ontology object) and link instances; these data instances remain governed by their input datasource permissions. Learn more about [Ontology permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/).
每个 Ontology 都链接到一个或多个 [Foundry organizations](/docs/foundry/security/orgs-and-spaces/#organizations)。

Each Ontology is linked to one or multiple [Foundry organizations](/docs/foundry/security/orgs-and-spaces/#organizations).
角色权限的详细说明请参阅 [Ontology roles 文档](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles)。

Roles permissions are detailed in the [Ontology roles documentation](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles).
> **ℹ️ 注意**

> 每个迁移到 ontology roles 的 object type、link type 和 action type 都将对该特定 ontology 具有访问权限的所有用户开放查看权限。因此，ontology 资源信息对该 ontology 的所有用户都可访问。
> **ℹ️ 注意**

> Every object type, link type, and action type migrated to ontology roles will have view permission for all users that have access to that particular ontology. Therefore, ontology resource information is accessible for all users of that ontology.
迁移 ontology 资源到 ontology roles 没有明确的顺序要求，因此可以混合使用采用 [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#datasource-derived-permissions) 的 object types 和采用 ontology roles 的 object types。因此，为了本次迁移的目的，我们将"能够编辑 object type"定义如下：

There is no explicit ordering required for migrating ontology resources to ontology roles, making it possible to have a mix of object types using [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#datasource-derived-permissions), and others using ontology roles. Therefore, for the purpose of this migration, we define `able to edit an object type` as follows:
* **使用 datasource-derived permissions 的 object types：** 用户在该 object type 的输入 datasources 上具有 `Editor` 权限。

* **使用 Ontology roles 的 object types：** 用户在该 object type 上具有 `Ontology Editor` 权限，并且不需要对输入 datasource 具有任何权限。用户应注意，这仅允许编辑 Ontology 资源及其元数据，并不授予对数据/datasource 本身的任何权限。对 object *数据*（而非*元数据*）的访问仍由输入 datasources 上授予的权限管理。

* **Object types using datasource-derived permissions:** Users have `Editor` permission on the input datasources for that object type.
* **Object types using Ontology roles:** Users have `Ontology Editor` permission on the object type and do not require any permissions on the input datasource. Users should note that this only allows editing Ontology resources and their metadata and does not grant any permission on the data/datasource itself. Access to object *data* (not *metadata*) is still governed by the permissions granted on input datasources.
## Migrate to ontology roles
如果您的注册启用了 Ontology 角色，但您尚未将您拥有的 Ontology 资源迁移到角色授权模型，您将在 Ontology Manager 中看到一个提示您进行迁移的横幅。

或者，在查看 Ontology 资源表时，您可以筛选出您拥有的、仍在使用 "Same permissions as backing datasource" 的资源。

If Ontology roles are enabled on your enrollment, but you have not yet migrated the Ontology resources that you own to the roles authorization model, you will see a banner in Ontology Manager that prompts you to do so.
Alternatively, when looking at the tables of Ontology resources, you can filter to the ones you own that are still using the "Same permissions as backing datasource".
> **ℹ️ 注意**

> Ontology 角色尚未对所有 Foundry 注册可用。如果您无法访问 Ontology 角色，请联系 Palantir Support。
> **ℹ️ 注意**

> Ontology roles are not yet available for all Foundry enrollments. If you do not have access to Ontology roles, contact Palantir Support.
### Prerequisites
要执行迁移，用户必须具有以下权限：

To perform the migration, users must have the following permissions:
1. 在 Foundry Ontology 中进行更改的权限。

1. Permissions to make changes in the Foundry Ontology.
2. 每个单独资源所需的以下权限：

2. The following permissions for each individual resource:
* 对于 object types，用户必须对输入 datasource 具有 `Owner` 权限。

* 对于 one-to-many link types，用户无需其他权限。只需对 link type 中引用的两个 object types 具有 `Viewer` 权限，并且用户必须是该 link type 本身或 Ontology 级别的 `Owner`。

* 对于 many-to-many link types，用户还必须对 link type 的输入 datasource 具有 `Owner` 权限。

* 对于 action types，无需其他权限。

* For object types, users must have `Owner` permission on the input datasource.
* For one-to-many link types, users do not need additional permissions. Only `Viewer` permissions on both object types referenced in the link type are required, and the user must be an `Owner` on the link type itself or at the Ontology level.
* For many-to-many link types, users must also have `Owner` permission on the input datasource of the link type.
* No additional permission is needed for action types.
> **ℹ️ 注意**

> 迁移到 Ontology 角色后，[修改 action types](/docs/foundry/object-permissioning/ontology-permissions-legacy/#permissions-for-editing-action-types) 需要额外的权限。您需要对 action type 编辑的任何 object types 以及 action type 本身具有权限，才能使用角色修改 action types。
> **ℹ️ 注意**

> Additional permissions are required for [modifying action types](/docs/foundry/object-permissioning/ontology-permissions-legacy/#permissions-for-editing-action-types) after migrating to Ontology roles. You will need permissions on any object types the action type edits, and on the action type itself, to modify action types with roles.
### Notification to migrate
迁移到 Ontology 角色是通过 [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) 管理的。一个专用的 Upgrade Assistant 任务会显示必须迁移的 Ontology 资源列表，以及具有执行迁移权限的被分派人。从 Upgrade Assistant 打开资源会将用户引导至资源的 **Security** 选项卡，以便在 Ontology Manager 应用程序中完成迁移。

Migration to Ontology roles is managed through [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/). A dedicated Upgrade Assistant task displays the list of Ontology resources that must be migrated, along with assignees that have permission to perform the migration. Opening a resource from Upgrade Assistant directs the user to the **Security** tab of the resource to migrate it within the Ontology Manager application.
如果用户具有设置 Ontology 角色的权限，尚未迁移的 Ontology 资源将出现在 **Security** 选项卡的迁移界面中，以便首次设置 Ontology 角色。在 Ontology 资源迁移完成后，Ontology 角色选择器会显示在 **Security** 选项卡下，并可由 `Ontology Owners` 进行更新。

If a user has permission to set Ontology roles, Ontology resources that have not yet migrated will appear in the migration interface in the **Security** tab to set Ontology roles for the first time. After the Ontology resource is migrated, the Ontology role picker is displayed under the **Security** tab and can be updated by `Ontology Owners`.
### Migrate using Ontology Manager
有两种方式可以将 Ontology 资源（object types、action types、link types）迁移到 Roles：[批量迁移](#bulk-migration-of-ontology-resources) Ontology 资源，或[逐个迁移](#one-by-one-migration-for-all-ontology-resources) 所有 Ontology 资源。

There are two ways to migrate Ontology resources (object types, action types, link types) to Roles: [bulk migration](#bulk-migration-of-ontology-resources) of Ontology resources or [one-by-one migration](#one-by-one-migration-for-all-ontology-resources) for all Ontology resources.
#### Bulk migration of Ontology resources
您可以将 Ontology 资源批量迁移到 Roles。在继续操作之前，请参阅[先决条件](#prerequisites)列表。您一次最多只能迁移 500 个资源。

You can bulk-migrate Ontology resources to Roles. Refer to the list of [prerequisites](#prerequisites) before proceeding. You can only migrate 500 resources at a time.
要进行批量迁移，请前往 Ontology Manager 中的 **Advanced**，然后在 Migrations 部分选择 **continue with migration assistant**。

To bulk-migrate, go to **Advanced** in the Ontology Manager and select **continue with migration assistant** in the Migrations section.
迁移向导将按以下步骤显示。

The migration wizard will appear with the following steps.
1. **Choose resources:** 选择您希望应用相同角色的所有 object types、link types 或 action types。下图显示了迁移向导中选择资源的界面：

1. **Choose resources:** Choose all the object types, link types, or action types on which you wish to apply the same roles. The image below displays the interface for choosing resources in the migration wizard:
![Bulk migration.](/docs/resources/foundry/ontology-manager/oma-migration-wizard-choose-resources.png)
2. **Related resources:** 仅当存在可以迁移的相关资源（link types 或 action types）时，才会显示此步骤。

3. **Assign roles:** 您可以手动设置要分配给这些 Object types 的 groups/users 和默认角色。roles migrator 目前无法批量建议角色。我们强烈建议在授予角色时使用 **user groups** 而不是 **users**。

4. **Summary:** 查看摘要，确认迁移的影响，并完成迁移以应用角色。

2. **Related resources:** This step is shown only if there are related resources (link types or action types) that can be migrated.
3. **Assign roles:** You can manually set the groups/users and the default role you want to assign to these Object types. The roles migrator cannot suggest roles in bulk for now. We strongly recommend using **user groups** over **users** when granting roles.
4. **Summary:** View the summary, acknowledge the implications of the migration, and complete the migration to apply the roles.
> **⚠️ 警告**

> 当你确认迁移的影响时，即表示你承认原先从 backing datasource 派生的 permissions 将会被新分配的 role grants 覆盖，且该迁移是不可逆的。
> **⚠️ 警告**

> When you acknowledge the implications of the migration, you are acknowledging that the permissions previously derived from backing datasources will be overwritten by the newly assigned role grants and that the migration is irreversible.
##### Exceptions to bulk migration
某些 action types 在进行批量迁移之前需要执行额外的步骤。

Some action types cannot be bulk-migrated without further steps.
在以下情况下，action types 无法迁移到 roles：

Action types cannot be migrated to roles if:
* 该 action type 没有检查当前用户 permissions 的 submission criteria。

* 解决方案：在 Ontology Manager 中该 action type 的 **Security & Submission criteria** 标签页（**Submission criteria** 区域）添加一个基于当前用户的 condition，然后保存到 Ontology，再重新尝试迁移。

* 该 action type 由 function 支持（backed by a function），必须在迁移前使用 `@edits decorators` 重新发布。

* 解决方案：请参阅 [decorators](/docs/foundry/functions/decorators/#decorators) 文档中的相关步骤。

* The action type has no submission criteria that checks the current user’s permissions.
* Solution: Add a condition based on the current user in the **Security & Submission criteria** tab of the Action type in the Ontology Manager (in the **Submission criteria** section) and save to the Ontology before re-attempting the migration.
* The action type is backed by a function and must be republished with `@edits decorators` before the migration.
* Solution: Refer to the steps in the [decorators](/docs/foundry/functions/decorators/#decorators) documentation.
要解决这些问题，请进入 **Action Types** 页面，并筛选出 **Same permissions as backing datasource**，这将显示因存在问题而尚未迁移的 action types。解决所有未处理的问题后，再对任何剩余的 action types 继续执行批量迁移。

To address these issues, go to the **Action Types** page and filter down to **Same permissions as backing datasource**, which will display the action types that have not been migrated because of issues. Resolve all outstanding issues and then proceed with bulk migration again for any remaining action types.
> **⚠️ 警告: Warning**

> 在迁移 action types 时，请确保仅将 permissions 授予那些在所引用的 object types 以及 action type 部署的所有 use cases 上都具备充分上下文的用户。
> **⚠️ 警告: Warning**

> When migrating action types, ensure that permissions are only granted to users with sufficient context on both the referenced object types and all use cases where the action type is deployed.
#### One-by-one migration for all Ontology resources
在 Ontology Manager 主页中，选择要迁移的 Ontology resources（object type、link type 或 action type），并将 `Security setup` 筛选为 `Same permissions as backing datasource`，将 `permissions` 筛选为 `owner`。

From the Ontology Manager home page, select the Ontology resources that you want to migrate (object type, link type, or action type) and filter by `Security setup` to `Same permissions as backing datasource` and by `permissions` = `owner`.
选择要迁移的实体，然后在页眉中选择 **Migrate to roles**，或在 Security 标签页中选择 **Start using roles**。

Select the entity to migrate, then choose either **Migrate to roles** on the header or **Start using roles** on the Security tab.
迁移向导将出现，并提供两个建议的 role 选项：**Datasource roles** 和 **Ontology admins and datasource roles**。这些选项允许用户使用并配置与其现有 Ontology 设置一致的角色。选择其中一个选项将预填建议的 roles 列表；这些 roles 之后可以更改。

The migration wizard will appear with two suggested role options: **Datasource roles** and **Ontology admins and datasource roles**. These options allow users to use and configure roles that align with their existing Ontology setups. Selecting one of the options pre-fills the list of suggested roles; these roles can be changed later.
* **Datasource roles：** 此选项将添加 input datasource 上具有 `Editor` 或 `Owner` role 的所有 users 和 user groups。

* **Ontology admins and datasource roles：** 此选项将添加当前能够根据 [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#type-specific-edit-permissions) 修改给定 Ontology resource 的所有 users。这些 users 属于 `Ontology Administrators` user group，并在 input datasource 上具有 Editor 或 Owner role。

* **Datasource roles:** This option adds all users and user groups with an `Editor` or `Owner` role on the input datasource.
* **Ontology admins and datasource roles:** This option adds all users that can currently modify the given Ontology resource based on [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#type-specific-edit-permissions). These users belong to the `Ontology Administrators` user group and have an Editor or Owner role on the input datasource.
下图显示了迁移向导中的 roles 建议：

The image below shows the roles suggestion in the migration wizard:
![Migrating one resource roles suggestion.](/docs/resources/foundry/ontology-manager/oma-migrating-one-resource-roles-suggestions.png)
选择所需的 role 建议，查看建议的 [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 以及 object type 的默认 role，必要时进行修改。接下来，查看摘要，确认影响，并完成迁移以应用这些 roles。

Choose the desired role suggestions, review the suggested [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) and the default role for the object type, then make modifications if necessary. Next, view the summary, acknowledge the implication, and complete the migration to apply the roles.
下图显示了如何在迁移向导中分配 roles：

The image below shows how to assign roles in the migration wizard:
![Migrating one resource assign roles.](/docs/resources/foundry/ontology-manager/oma-migrating-one-resource-assign-roles.png)
##### Exceptions
在以下情况下，你可能无法尝试将 action type 迁移到 Roles：

You may be prevented from attempting the migration of an action type to Roles if:
* 该 action type 没有检查当前用户 permissions 的 submission criteria。

* 解决方案：在 Ontology Manager 中该 action type 的 **Security & Submission criteria** 标签页（**Submission criteria** 区域）添加一个基于当前用户的 condition，然后保存到 Ontology，再重新尝试迁移。

* 该 action type 由 function 支持（backed by a function），必须在迁移前使用 `@edits decorators` 重新发布。

* 解决方案：请参阅 [decorators](/docs/foundry/functions/decorators/#decorators) 文档中的相关步骤。

* The action type has no submission criteria that checks the current user’s permissions.
* Solution: Add a condition based on the current user in the **Security & Submission criteria** tab of the action type in the Ontology Manager (in the **Submission criteria** section) and save to the Ontology before re-attempting the migration.
* The action type is backed by a function and must be republished with `@edits decorators` before the migration.
* Solution: Refer to the steps in the [decorators](/docs/foundry/functions/decorators/#decorators) documentation.
当这些问题解决后，您将能够将 action type 迁移到 Roles。

When these issues have been resolved, you will be able to migrate the action types to Roles.
#### What if some ontology resources are no longer needed
如果您不再需要一个需要 action 的 ontology 资源，您可以使用 [Ontology cleanup tool](/docs/foundry/ontology-manager/cleanup/) 删除该资源。该工具可帮助您根据一组标准识别哪些 object type 可以安全删除（例如，datasource 是否已移入回收站、弃用日期是否已过、index 是否失败、是否正在使用 Ontology roles 等）。

If you no longer need an ontology resource that requires an action, you can delete the resource using the [Ontology cleanup tool](/docs/foundry/ontology-manager/cleanup/). This tool helps you identify which object types are safe to delete based on a set of criteria (for example, if the datasource is trashed, the deprecation date has passed, the index is failing, whether they are using Ontology roles or not, and so on.)
#### Migrating function-backed action types
Function-backed action type 需要将支撑的 Function 一同迁移。Foundry 将尝试自动迁移 Function，从而允许您迁移 action type。然而，某些 Function 可能无法自动迁移，需要在 Function 中手动声明已编辑的 object type。如果在将 action type 迁移到 Ontology roles 后看到 Function-backed action 出现失败，请查看 [FAQ](#how-can-i-resolve-a-function-backed-action-that-is-failing-post-migration) 部分。

Function-backed action types require the backing Function to be migrated. Foundry will attempt to migrate Functions automatically, allowing you to migrate the action type as well. Some Functions, however, might not be migrated automatically and require manually declaration of the edited object types in the Functions. Check the [FAQ](#how-can-i-resolve-a-function-backed-action-that-is-failing-post-migration) section if you see failures in your Function-backed actions after migrating an action type to Ontology roles.
### Migration frequently asked questions
#### Will there be any changes in object-aware applications?
用户可能可以访问 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中 object type 和 link type 的 metadata，而这些 metadata 之前由于他们没有输入 datasource 的 `Viewer` 权限是无法查看的。这并不意味着他们将获得输入 datasource 中数据的访问权限——数据访问始终由这些 datasource 上的 roles 控制。他们可以查看哪些具体 metadata 由其 [Ontology role](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 决定。

Users may have access to metadata on object types and link types in the [Ontology Manager](/docs/foundry/ontology-manager/overview/) that they could not previously view because they did not have `Viewer` access to the input datasources. This does not mean they will get access to the data in the input datasources which is always governed by the roles on those datasources. The specifics of what metadata they will be able to see is determined by their [Ontology role](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles).
Object Explorer 还将更新在 object type 迁移后编辑 Object View 的权限检查。在 object type 迁移之前，用户需要属于 `Object View Administrators` 组并具有输入 datasource 的 `Editor` 权限才能编辑 Object View。在 object type 迁移之后，Object Explorer 将仅检查用户是否对该 object type 本身具有 `Ontology Editor` 权限。

Object Explorer will also update the permission checks for editing Object Views when an object type is migrated. Before an object type is migrated, a user needs to be in the `Object View Administrators` group and have `Editor` access to the input datasources to edit Object Views. After an object type has been migrated, Object Explorer will only check that the user has `Ontology Editor` permissions on the object type itself.
#### How can I resolve a function-backed action that is failing post migration?
如果 Foundry 无法自动检测 Ontology Edit Function 正在编辑的 object type，则该 action 将在提交后失败，并出现以下错误。

If Foundry failed to automatically detect the object types an Ontology Edit Function is editing, the action will fail after submission with the following error.
![Functions provenance error.](/docs/resources/foundry/ontology-manager/functions-provenance-error.png)
要解决此错误，请按照 [Functions 文档](/docs/foundry/functions/edits-overview/) 中解释的步骤操作。

To resolve this error, follow the steps explained in the [Functions documentation](/docs/foundry/functions/edits-overview/).