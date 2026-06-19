<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/function-actions-getting-started/
---
# Getting started
本教程介绍如何创建一个由 [Ontology Edit function](/docs/foundry/functions/edits-overview/) 支持的 action type。

This tutorial explains how to create an action type that is backed by an [Ontology Edit function](/docs/foundry/functions/edits-overview/).
## Prerequisites
在本教程中，我们将使用与 [Actions 入门教程](/docs/foundry/action-types/getting-started/) 相同的 `Demo Ticket` object type 和示例对象。

In this tutorial, we will use the same `Demo Ticket` object type and sample objects as in the [Getting Started with Actions tutorial](/docs/foundry/action-types/getting-started/).
首先，编写一个 Ontology edit function，以执行 action 所需的编辑操作。这需要：

Start by writing an Ontology edit function that performs the desired edits for your action. This requires:
* 使用 functions on objects TypeScript 模板设置 repository，

* 将相关的 object types 导入到您的 repository，以及

* 发布 Ontology edit function 以供 actions 读取。

* Setting up a repository using the functions on objects TypeScript template,
* Importing the relevant object types into your repository, and
* Publishing the Ontology edit function for actions to read.
有关这些步骤的信息，请参阅 functions 文档：

Information on these steps can be found in the functions documentation:
* **[入门](/docs/foundry/functions/getting-started/)：** 按照本教程创建一个基本的 functions repository 并发布一个 function。

* **[Functions on objects](/docs/foundry/functions/functions-on-objects/)：** 按照本教程创建一个使用 object 数据的 function。

* **[Ontology edits](/docs/foundry/functions/api-ontology-edits/)：** 使用此参考来创建 Ontology edit function。

* **[Getting started](/docs/foundry/functions/getting-started/):** Follow this tutorial to create a basic functions repository and publish a function.
* **[Functions on objects](/docs/foundry/functions/functions-on-objects/):** Follow this tutorial to create a function that uses object data.
* **[Ontology edits](/docs/foundry/functions/api-ontology-edits/):** Use this reference to create an Ontology edit function.
编写并发布 Ontology edit function 后，以下步骤将该 function 连接到 action，以便该 function 可用于对 objects 进行编辑。在本教程中，我们已从一个 repository 中编写并发布以下 Ontology edit function：

Once you have written and published an Ontology edit function, the steps below will connect the function to an action so that the function can be used to make edits to objects. For the purposes of this tutorial, we have written and published the following Ontology edit function from a repository:
![Ontology edit function](/docs/resources/foundry/action-types/function_backed_actions_ontology_edit_function.png)
为方便起见，代码可在此处获取：

For convenience, the code is available here:
```typescript
@OntologyEditFunction()
public addPriorityToTitle(ticket: DemoTicket): void {
let newTitle: string = "[" + ticket.ticketPriority + "]" + ticket.ticketTitle;
ticket.ticketTitle = newTitle;
}
```
> **⚠️ 警告**

> 用于 action types 的 functions 必须使用 `@OntologyEditFunction()` 注解，而不是 `@Function()`。更多详细信息可在 [functions on objects](/docs/foundry/functions/api-ontology-edits/#declaring-an-edit-function) 文档中找到。
> **⚠️ 警告**

> Functions for use in action types must be annotated with `@OntologyEditFunction()` instead of `@Function()`. Further details can be found in the documentation for [functions on objects](/docs/foundry/functions/api-ontology-edits/#declaring-an-edit-function).
## Creating a function-backed action
在 **Rules** 部分，添加一个类型为 **Function** 的规则。搜索您作为 [prerequisites](#prerequisites) 的一部分发布的 function，并选择最新版本。配置 inputs 以与 action parameters 匹配，如下所示。请注意，function rule 不能与其他 [Ontology rules](/docs/foundry/action-types/rules/#ontology-rules) 组合使用。

In the **Rules** section, add a single rule of type **Function**. Search for the function you published as part of the [prerequisites](#prerequisites), and pick the latest version. Configure the inputs to match up to the action parameters, as below. Note that a function rule cannot be combined with [other Ontology rules](/docs/foundry/action-types/rules/#ontology-rules).
![Configure inputs](/docs/resources/foundry/action-types/function_backed_actions_configure_inputs.png)
选择 function 时，function 的所有 inputs 将自动作为 parameters 创建并添加到 **Parameters** 选项卡。在这些截图中显示的示例中，已创建一个类型为 **Object reference** 的 `Demo Ticket` parameter。如有需要，现在可以进一步自定义该 parameter。

When selecting the function, all inputs of the function will automatically be created as parameters and added to the **Parameters** tab. In the example shown in these screenshots, a `Demo Ticket` parameter of type **Object reference** has been created. The parameter can now be customized further if needed.
![Demo Ticket](/docs/resources/foundry/action-types/function_backed_actions_demo_ticket.png)
![Demo Ticket Details](/docs/resources/foundry/action-types/function_backed_actions_demo_ticket_details.png)
保存您的 action 并按照[与其他应用程序集成的指南](/docs/foundry/action-types/use-actions/)在整个平台中配置它。

Save your action and configure it across the platform as described in the [guidance for integration with other applications.](/docs/foundry/action-types/use-actions/)
## Changing function version
默认情况下，如果 function 逻辑发生更改，action 不会自动更新以匹配该更改。相反，您必须返回到 action 的 **Rules** 部分并升级该 action 正在引用的 function 版本。例如，如果我们已经发布了 function 的 0.1.2 版本，我们需要在此处进行更新：

By default, if the function logic is changed, the action does not automatically update to match it. Instead, you must return to the **Rules** section of the action and upgrade the version of the function that the action is referencing. For example, if we published version 0.1.2 of the function, we would need to update it here:
![How to update the version of the function](/docs/resources/foundry/action-types/function_backed_actions_update_function_logic.png)
### Auto upgrades
您可以选择性地启用 action 所引用的 function 的自动升级。如果启用，该 action 将在[版本范围](/docs/foundry/functions/version-range-dependencies-for-functions/)内依赖该 function，并在运行时[解析该版本](/docs/foundry/functions/version-range-dependencies-for-functions/#version-range-resolution)。

You can optionally choose to enable auto upgrades for the function that the action is referencing. If enabled, the action will depend on the function at a [version range](/docs/foundry/functions/version-range-dependencies-for-functions/) and [resolve the version](/docs/foundry/functions/version-range-dependencies-for-functions/#version-range-resolution) at runtime.
要为 action 启用自动升级，请导航到 action 的 **Rules** 部分并选择 **Function** 参数。在 **Function** 下拉菜单中，选择您希望运行的 function 的最低版本，并启用 **Auto upgrade** 选项。这将对应于一个版本范围依赖项，其中包含所选最低版本的所有向后兼容的版本，例如 minor 或 patch 升级。

To enable auto upgrades for an action, navigate to the **Rules** section of the action and select the **Function** parameter. In the **Function** dropdown, select the minimum version of the function that you want to be run and enable the **Auto upgrade** option. This will correspond to a version range dependency that comprises all backward compatible versions, such as minor or patch upgrades, of the selected minimum version.
![How to enable auto upgrades for a function-backed action](/docs/resources/foundry/action-types/function_backed_actions_auto_upgrade.png)
> **ℹ️ 注意**

> 对于 `0.y.z` 形式的 function 版本，自动升级是禁用的。这些版本保留用于初始开发阶段，在该阶段 function 的 API 和行为可能会频繁更改，因此不应被视为稳定版本。请参阅有关[选择发布版本](/docs/foundry/functions/functions-versioning/#choosing-a-release-version)的文档。
> **ℹ️ 注意**

> Auto upgrades are disabled for function versions of the form `0.y.z`. These versions are reserved for initial development where function API and behavior may change frequently and should not be considered stable. Refer to the documentation on [choosing a release version](/docs/foundry/functions/functions-versioning/#choosing-a-release-version).
#### Security
如果为 function-backed action 启用了自动升级，那么没有[对 action 的编辑权限](/docs/foundry/object-permissioning/ontology-permissions-legacy/#permissions-for-editing-link-types)的用户可以通过对底层 function 进行更改来修改该 action 的行为。这是因为 function 的编辑权限并未与该 action 的权限相关联。

If auto upgrades are enabled for a function-backed action, users who do not have [edit permissions on the action](/docs/foundry/object-permissioning/ontology-permissions-legacy/#permissions-for-editing-link-types) can modify the action's behavior by making changes to the backing function. This is because edit permissions on the function are not tied to the permissions on the action.
#### Breaking changes
由于[破坏性更改](/docs/foundry/functions/version-range-dependencies-for-functions/#risks)出现在不良的 function 版本中，自动升级可能会导致 action 执行失败。

Auto upgrades can result in action execution failures due to [breaking changes](/docs/foundry/functions/version-range-dependencies-for-functions/#risks) in bad function releases.
#### Provenance
action 的 provenance 根据所选最低 function 版本的 provenance 进行设置。如果 function 的较新版本返回了此 provenance 之外的编辑（例如，额外的 object type），则 action 执行将失败。

The provenance of the action is set according to the provenance of the selected minimum function version. If a newer release of the function returns edits outside of this provenance (for example, an additional object type), action execution will fail.
> **ℹ️ 注意**

> 目前，provenance 仅包含 action 在运行时可能编辑的 object types。
> **ℹ️ 注意**

> Currently, the provenance consists only of the object types that the action may edit at runtime.