<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/trigger-schedule-build/
---
# Trigger schedule build
[schedule](/docs/foundry/data-integration/schedules/) 定义了一组 Foundry 作为 [build](/docs/foundry/data-integration/builds/) 的一部分重新计算的资源。通过在 action type 上配置 **schedule rule**，您可以在应用该 action 时触发该 schedule 的 build。这使得 Ontology 中的最终用户工作流能够重新计算数据集，而无需用户导航到 [Data Lineage](/docs/foundry/data-lineage/overview/) 或 [Builds application](/docs/foundry/data-integration/application-reference/#builds)。

A [schedule](/docs/foundry/data-integration/schedules/) defines a set of resources Foundry recomputes as part of a [build](/docs/foundry/data-integration/builds/). By configuring a **schedule rule** on an action type, you can trigger a build of that schedule whenever the action is applied. This enables end-user workflows in the Ontology to recompute datasets without users having to navigate to [Data Lineage](/docs/foundry/data-lineage/overview/) or the [Builds application](/docs/foundry/data-integration/application-reference/#builds).
当 action type 包含 schedule rule 时，action 的 Ontology 编辑会在 build 启动 *之后* 应用。编辑不会等待 build 完成。相反，action 触发 build，捕获 schedule run RID，并立即应用其余规则，包括 Ontology 编辑。

When an action type contains a schedule rule, the action's Ontology edits are applied *after* the build begins. Edits do not wait for the build to finish. Instead, the action triggers the build, captures the schedule run RID, and immediately applies the rest of the rules, including the Ontology edits.
## Configure a schedule rule
向 action type 添加 schedule rule 并选择一个 schedule。该 schedule 必须处于 [project-scoped mode](/docs/foundry/data-integration/schedules/#project-scope)。

Add a schedule rule to an action type and select a schedule. The schedule must be in [project-scoped mode](/docs/foundry/data-integration/schedules/#project-scope).
![Action type configuration page in Ontology Manager. A schedule rule is being added.](/docs/resources/foundry/action-types/advanced-schedule-action-type-rule.png)
如果所选 schedule 是 [parameterized](/docs/foundry/building-pipelines/parameterization/)，您必须为每个 schedule 参数提供一个值。当应用 action 时，已解析的参数值将传递给 schedule，并转发到 build 内部底层的参数化 transforms。

If the selected schedule is [parameterized](/docs/foundry/building-pipelines/parameterization/), you must provide a value for each schedule parameter. When the action is applied, the resolved parameter values are passed to the schedule and forwarded to the underlying parameterized transforms inside the build.
Schedule rules 与 [parallelized parameterized schedules](/docs/foundry/building-pipelines/parameterization/#parallelized-mode-advanced) 配合使用时尤其有用。请参阅 [parameterization documentation](/docs/foundry/building-pipelines/parameterization/#use-action-types-for-parallelized-schedules) 以了解有关在 Ontology 中使用 actions 处理并行化 schedule 的更多信息。

Schedule rules are particularly useful when paired with [parallelized parameterized schedules](/docs/foundry/building-pipelines/parameterization/#parallelized-mode-advanced). Review the [parameterization documentation](/docs/foundry/building-pipelines/parameterization/#use-action-types-for-parallelized-schedules) to learn more about using actions in the Ontology for parallelized schedules.
## Permissions
Action 的 [submission criteria](/docs/foundry/action-types/submission-criteria/) 管理通过 action 触发 schedule 所需的权限。如果用户满足 action 提交条件，他们可以在不直接拥有 schedule 任何权限的情况下运行该 schedule。

The action's [submission criteria](/docs/foundry/action-types/submission-criteria/) manage the permissions needed to trigger a schedule through the action. If users satisfy the action submission criteria, they can run the schedule without any direct permissions on the schedule.
> **ℹ️ 注意**

> Foundry 会在首次引用 schedule 时以及每次编辑 schedule rule 时检查用户是否拥有运行该 schedule 的权限。从 action type 引用 schedule 会将运行 schedule 的控制权从 schedule 委托给 action type。任何可以管理 action type 上 actions 的人员都可以控制谁可以触发该 schedule。
> **ℹ️ 注意**

> Foundry checks whether a user has permission to run the schedule the first time it is referenced and whenever the schedule rule is edited. Referencing a schedule from an action type delegates control over running it from the schedule to the action type. Anyone who can manage actions on the action type then controls who can trigger the schedule.
## Track build progress
当 schedule rule 被触发时，生成的 schedule run 由 **schedule run RID** 标识。该 RID 作为值公开，可从 action type 的 Ontology 编辑规则中引用，允许您将其写入所编辑对象的 string property 中。当您希望在对象上保留由 action 触发的 build 的记录时，这非常有用。

When a schedule rule is triggered, the resulting schedule run is identified by a **schedule run RID**. This RID is exposed as a value that can be referenced from the action type's Ontology edit rules, allowing you to write it into a string property of an edited object. This is useful when you want to keep a record on the object of the build that was triggered by the action.
要捕获 schedule run RID，请在同一 action type 上配置 **Modify object** 或 **Create object** 规则，并将目标对象的 string property 映射到 schedule rule 提供的 schedule run RID 值。

To capture the schedule run RID, configure a **Modify object** or **Create object** rule on the same action type and map a string property of the target object to the schedule run RID value provided by the schedule rule.
![Action type configuration page in Ontology Manager. A schedule rule is added, and the schedule run RID is written to a string property through a Create object rule.](/docs/resources/foundry/action-types/build-schedule-run-rid-property.png)
要将存储的 RID 呈现为实时 build 状态指示器，请对该 property 应用 [resource RID formatting](/docs/foundry/object-link-types/value-formatting/#supported-value-formatting)。启用格式化后，Foundry 会将 RID 值显示为带有图标和文本的链接，反映 build 的当前状态：`Running`、`Ignored`、`Failed` 或 `Succeeded`。

To render the stored RID as a live build status indicator, apply [resource RID formatting](/docs/foundry/object-link-types/value-formatting/#supported-value-formatting) to the property. With formatting enabled, Foundry displays the RID value as a link with an icon and text that reflects the current status of the build: `Running`, `Ignored`, `Failed`, or `Succeeded`.