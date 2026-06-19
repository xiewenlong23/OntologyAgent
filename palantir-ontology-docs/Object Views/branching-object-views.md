<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/branching-object-views/
---
# Branching object views
## Overview
Object Views 与 Global Branching 集成，以实现 object view 配置的安全、隔离开发。本文档介绍了如何在分支上使用 object views，包括添加和修改资源、跨应用程序兼容性、合并要求、rebase 以及已知限制。

Object Views integrates with Global Branching to enable safe, isolated development of object view configurations. This documentation covers how to work with object views on branches, including adding and modifying resources, cross-application compatibility, merge requirements, rebasing, and known limitations.
有关 Global Branching 概念和工作流程的一般信息，请参阅 [Global Branching 文档](/docs/foundry/global-branching/overview/)。

For general information on Global Branching concepts and workflows, refer to the [Global Branching documentation](/docs/foundry/global-branching/overview/).
## Adding, removing, and modifying resources
要将 object view 添加到分支，请在 [Object View 编辑器](/docs/foundry/object-views/config-object-views/#use-the-object-view-editor) 中处于分支状态时保存一个 object view 版本。

To add an object view to a branch, save an object view version while on a branch in the [Object View editor](/docs/foundry/object-views/config-object-views/#use-the-object-view-editor).
Object views 支持两种类型的分支兼容资源：

Object views support two types of branch-compatible resources:
* **OV-managed modules：** 捕获对分支上 object view 所做的 Workshop 内容更改。每个完整的 object view tab、object instance panel 和 object set panel 都会创建一个单独的 OV-managed module。Workshop 应用程序中所有 branch-aware 功能在 object views 内也可用。

* **Full object view tabs：** 捕获 object view tabs 的结构更改，包括添加、删除、重命名、profile 更改以及可见性条件修改。

* **OV-managed modules:** Capture Workshop content changes made to an object view on a branch. A separate OV-managed module is created for each full object view tab, the object instance panel, and the object set panel. All branch-aware features available in Workshop applications are also available inside object views.
* **Full object view tabs:** Capture structural changes to object view tabs, including additions, deletions, renames, profile changes, and visibility condition modifications.
以下示例显示了 `Museum` object type 在分支上的不同资源。从上到下依次为：full object view tabs 资源、`Museum` object type 本身、full object view 的 **Museum History** tab，以及 [panel object view](/docs/foundry/object-views/config-panel-views/#object-instance-panels)。

The example below shows different resources on a branch for the `Museum` object type. From top to bottom: the full object view tabs resource, the `Museum` object type itself, the **Museum History** tab of the full object view, and the [panel object view](/docs/foundry/object-views/config-panel-views/#object-instance-panels).
![A screenshot showing different branch resources for the Museum object type in the branch taskbar.](/docs/resources/foundry/object-views/object-view-branch-resources.png)
您可以使用分支任务栏从分支中单独移除任何 object view 资源。移除 full object view tabs 资源会自动将其所有关联的 tabs 从分支中移除。

You can remove any object view resource from a branch individually using the branch taskbar. Removing a full object view tabs resource automatically removes all of its associated tabs from the branch.
![A screenshot showing the option to remove an Object View branch resource from the branch taskbar.](/docs/resources/foundry/object-views/removing-object-view-branch-resource.png)
## Cross-application compatibility
Object views 可以针对分支上 ontology 的最新状态进行编辑，包括在分支上创建的 object types 和 action types。Object View widget 还可用于将 branched object view 嵌入到独立的 Workshop 应用程序中。可以在 Ontology Manager 的 **Object views** tab 中预览分支上的 object view。

Object views can be edited for the latest state of the ontology on a branch, including object types and action types created on a branch. The Object View widget can also be used to embed a branched object view inside a standalone Workshop application. An object view can be previewed on a branch within the **Object views** tab in Ontology Manager.
## Merge requirements
### Deployability checks
在将 object view 从分支部署到 `main` 之前，必须通过以下可部署性检查：

Before deploying an object view to `main` from a branch, the following deployability checks must succeed:
* **用户具有发布权限：** 需要[编辑 object view 的权限](/docs/foundry/object-views/config-overview/#permissions)。此权限检查与在 `main` 上发布新 object view 版本时进行的检查相同。

* **User has publish permissions:** [Permissions to edit the object view](/docs/foundry/object-views/config-overview/#permissions) is required. This is the same permission check that is done when publishing a new object view version on `main`.
* **Object view 必须与 main 进行 rebase：** 在合并之前，将分支上每个 object view 资源与 `main` 上的最新更改进行 rebase。

* **Object view must be rebased with main:** Before merging, rebase each object view resource on the branch with the latest changes on `main`.
* **未修改 Legacy 字段：** 验证分支上未修改任何新 Object View 编辑器不支持的功能。此检查应始终通过。如果失败，请联系 Palantir Support。

* **No Legacy fields modified:** Verifies that no features unsupported by the new Object View editor have been modified on the branch. This check should always pass. If it fails, contact Palantir Support.
### Approvals checks
Object views 使用 [approvals](/docs/foundry/global-branching/resource-protection-and-approval-policies/) 来确定在分支上进行更改的用户是否具有合并这些更改所需的权限。所需的具体权限取决于 object view 所链接到的 object type 的 [permission model](/docs/foundry/object-permissioning/ontology-permissions/)。

Object views use [approvals](/docs/foundry/global-branching/resource-protection-and-approval-policies/) to determine whether the user making changes on a branch has the permissions required to merge those changes. The specific permissions required depend on the [permission model](/docs/foundry/object-permissioning/ontology-permissions/) of the object type that the object view is linked to.
#### Object type uses datasource-derived permissions
当 object type 使用 [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#datasource-derived-permissions) 时，contributor 或 approving reviewer 必须具备：

When the object type uses [datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/#datasource-derived-permissions), the contributor or an approving reviewer must have:
* 对 object type 具有 `View` 访问权限，并对其**所有** backing datasources 具有 `Editor` 访问权限。

* 在 [Control Panel](/docs/foundry/administration/enrollments-and-organizations-permissions/) 中具有 `Object View Admin` 应用程序权限，该权限是在 Object Explorer 中发布 object views 所必需的。这与在 `main` 上[发布新 object view 版本](/docs/foundry/object-views/config-overview/#permissions)时所需的应用程序权限相同。

* `View` access on the object type and `Editor` access on **all** of its backing datasources.
* The `Object View Admin` application permission in [Control Panel](/docs/foundry/administration/enrollments-and-organizations-permissions/), which is required to publish object views in Object Explorer. This is the same application permission required when [publishing a new object view version](/docs/foundry/object-views/config-overview/#permissions) on `main`.
> **ℹ️ 注意: 合并时 Datasource 权限更为严格**

> 上述 datasource 权限要求比 branching 之外使用的标准编辑权限检查更为严格。在 `main` 上编辑 object view 只需 object type 的**任意一个** backing datasource 上的 `Editor` 角色。而从 branch 合并更改则需要在**每个** backing datasource 上都具有 `Editor` 角色。
> **ℹ️ 注意: Datasource permissions are stricter at merge time**

> The datasource permission requirement above is stricter than the standard edit-permissions check used outside of branching. Editing an object view on `main` only requires the `Editor` role on **any** of the object type's backing datasources. Merging changes from a branch requires the `Editor` role on **every** backing datasource.
#### Object type uses ontology roles or project-based permissions
当 object type 使用 [ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 或 [project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/) 时，contributor 或审批 reviewer 仅需具备 object type 的编辑权限即可。这通常通过 ontology roles 下的 `Ontology Editor` 角色授予，或通过 project-based permissions 下的 `Editor` 项目角色授予。Object type 的编辑权限已涵盖在 Object Explorer 中发布 object view 的权限，因此无需单独的 `Object View Admin` 应用程序权限。

When the object type uses [ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) or [project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/), the contributor or an approving reviewer only needs edit access on the object type. This is typically granted through the `Ontology Editor` role under ontology roles, or through the `Editor` project role under project-based permissions. Edit access on the object type already covers publishing object views in Object Explorer, so no separate `Object View Admin` application permission is required.
#### Inherited project approval policies
Object view 以及构成 object view tabs 和 panels 的 Workshop 模块是父 object type 的逻辑子资源。如果该 object type 被 [protected](/docs/foundry/global-branching/resource-protection-and-approval-policies/#resource-protection)，且位于具有 [project approval policy](/docs/foundry/global-branching/resource-protection-and-approval-policies/#project-approval-policies) 的项目中，则该 policy 同样适用于 object view 及其模块。两者的审批请求必须满足该 policy 后，proposal 才能被合并。

Object views and the Workshop modules that make up object view tabs and panels are logical children of the parent object type. If the object type is [protected](/docs/foundry/global-branching/resource-protection-and-approval-policies/#resource-protection) and lives in a project with a [project approval policy](/docs/foundry/global-branching/resource-protection-and-approval-policies/#project-approval-policies), that policy applies to the object view and its modules. Approval requests for both must satisfy the policy before the proposal can be merged.
> **ℹ️ 注意: 从父 object type 继承 protection**

> 继承式 resource protection 正在开发中，即将发布。正式上线后，只要父 object type 处于 protected 状态，将禁止对 object view 及其模块直接在 `main` 上进行编辑。在此之前，即使父 object type 已被 protected，object view 以及构成其 tabs 和 panels 的模块仍可在 `main` 上直接编辑。
> **ℹ️ 注意: Inherited protection from the parent object type**

> Inherited resource protection is under development and will be released soon. Once available, it will prevent direct edits to `main` for an object view or its modules whenever the parent object type is protected. Until then, an object view and the modules that make up its tabs and panels can still be edited directly on `main` even if the parent object type is protected.
## Rebasing and conflict resolution
Branch 上的每个 object view 资源在部署前必须与 main 进行 rebase。Object view module 资源可通过 [Workshop rebasing](/docs/foundry/workshop/branching-integration/#rebasing-and-conflict-resolution) 进行 rebase。[Full object view tabs resource](/docs/foundry/object-views/use-full-views-in-platform/) 上的 tab 配置更改必须与 tab 内容更改分开 rebase。当 full object view 需要 rebase 时，通知消息将显示在 [Object View editor](/docs/foundry/object-views/config-object-views/#edit-object-view-tabs) 中 object view 区域的下方。

Each object view resource on a branch must be rebased with main before being deployed. Object view module resources can be rebased using [Workshop rebasing](/docs/foundry/workshop/branching-integration/#rebasing-and-conflict-resolution). Tab configuration changes on a [full object view tabs resource](/docs/foundry/object-views/use-full-views-in-platform/) must be rebased separately from tab content changes. When rebasing is required for full object view, a notification message will appear below the object view section in the [Object View editor](/docs/foundry/object-views/config-object-views/#edit-object-view-tabs).
Object view rebase 对话框显示三列：

The object view rebase dialog displays three columns:
* Main branch 状态

* 您的 branch 状态

* 建议的 rebase 结果

* The main branch state
* Your branch state
* The proposed rebase result
`main` 与您 branch 之间无冲突的更改将被自动接受并纳入结果。如果存在冲突，您必须针对每个受影响的 tab 选择保留 `main` 版本还是 branch 版本。结果列显示 rebase 之后最终状态的预览。您可以在完成 rebase 之前修改任何自动接受的更改。

Non-conflicting changes between `main` and your branch are automatically accepted and included in the result. If there is a conflict, you must choose whether to keep the version from `main` or from your branch for each affected tab. The result column shows a preview of the final state after rebasing. You can modify any auto-accepted changes before completing the rebase.
以下是 object view rebase 对话框的示例。该示例展示了两个已自动接受的无冲突更改。检测到 `Louvre` tab 的两次编辑之间存在冲突。

Below is an example of the object view rebase dialog. The example demonstrates two non-conflicting changes that have been auto-accepted. A conflict was detected between the two edits of the `Louvre` tab.
![Example of object view rebase dialog.](/docs/resources/foundry/object-views/object-view-rebase-example.png)
若要解决冲突，请选择 branch 版本或 `main` 版本。这样即可成功完成 rebase。您可以展开冲突行以查看可见性详情。

To resolve the conflict, choose either the branch or `main` version. This enables a successful rebase. You can expand the conflicting row to view visibility details.
![Example of resolving a conflict in the object view rebase dialog.](/docs/resources/foundry/object-views/object-view-rebase-conflict-resolution.png)
## Known limitations
[Legacy object view tabs](/docs/foundry/object-views/config-legacy-object-views/) 无法在 branch 上进行编辑。

[Legacy object view tabs](/docs/foundry/object-views/config-legacy-object-views/) cannot be edited on a branch.