<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/inline-edits/
---
# Inline edits
Action-backed inline edits are validated and submitted differently than standard [actions](/docs/foundry/action-types/getting-started/). For standard actions, multiple parameters need to be set in order for the action to be valid. However, for action-backed inline edits, every parameter is optional and defaults to the existing value of the object, so a user can make individual changes to properties one at a time.
本文档讨论了在使用内联编辑时如何避免意外结果。内联编辑在 Workshop 和 Object Explorer 中均可用。内联编辑 action 的配置取决于 action 的使用位置。

This documentation discusses how to avoid unexpected results when using inline edits. Inline edits are available in both Workshop and Object Explorer. The configuration of the inline edit action depends on where the action is used.
## Object Explorer inline edits
内联编辑允许用户在 [Object Explorer results view](/docs/foundry/object-explorer/view-results/) 或原生 Object View widgets（如 property 或 metric cards widget）中快速编辑对象的值。

Inline edits allow users to quickly edit values of an object in the [Object Explorer results view](/docs/foundry/object-explorer/view-results/) or native Object View widgets, like the property or metric cards widget.
### Configuration
![Inline edit action configuration](/docs/resources/foundry/action-types/inline-action-configuration.png)
要设置内联编辑 action,请在 Ontology Manager 中导航到 object type 的 **Properties** 选项卡,然后进入 **Interaction** 选项卡。选择一个 property,然后在侧边栏中导航到 **Inline edit**。在下拉菜单中,选择可用的 action type 之一或创建一个新的。创建新的 action type 将触发 action type 创建工作流。每个 property 只能有一个 inline edit action type。

To set up an inline edit action, navigate to the **Properties** tab of your object type and then to the **Interaction** tab in Ontology Manager. Select a property and navigate to **Inline edit** in the sidebar. In the dropdown menu, select one of the available action types or create a new one. Creating a new one will trigger the action type creation workflow. Each property can have only one inline edit action type.
您可以将同一个 action type 用作多个 property 的 inline edit,也可以为不同的 property 设置单独的 action type。

You can use the same action type as an inline edit for multiple properties, or you can have separate action types for different properties.
#### Action type requirements for inline edits
并非所有 action type 都可以用作 inline edit action type。要被接受,action type 必须满足以下要求:

Not all action types can be used as inline edit action types. To be accepted, the action type must meet the following requirements:
* 只能修改单个 object type 的单个 object。
* 必须启用默认值。

* 默认值必须来自定义 inline action 的 object reference parameter。因此,action 中被更改的 properties 不能映射到 static values 或 special values(例如 "Current User" 或 "Current Time")。

* 可以设置 visibility status 和 overrides;但是,如果 inline edit 在 Object Explorer 和 Object Views 中使用,则这些设置将被忽略。

* 不能启用 [Side effect webhooks](/docs/foundry/action-types/webhooks/#webhooks-writeback-vs-side-effect) 或 [side effect notifications](/docs/foundry/action-types/notifications/)。

* May only modify a single object of a single object type.
* Default values must be enabled.
* Default values must come from the object reference parameter on which the inline action is defined. As a result, properties that are being changed in the action cannot be mapped to static values or special values like "Current User" or "Current Time".
* Visibility status and overrides can be set; however, they will be ignored if the inline edit is used in Object Explorer and Object Views.
* [Side effect webhooks](/docs/foundry/action-types/webhooks/#webhooks-writeback-vs-side-effect) or [side effect notifications](/docs/foundry/action-types/notifications/) cannot be enabled.
## Workshop inline edits
在 Workshop 中将 action type 用作 inline edit 不需要额外的配置,但并非所有 actions 都适合用于 cell-level editing。有关如何配置 inline edits 的信息,请参阅 [Workshop documentation](/docs/foundry/workshop/widgets-object-table/#inline-edits-cell-level-writeback)。

No additional configuration is required to use an action type as an inline edit in Workshop, but not all actions are suitable for cell-level editing. For information on how to configure inline edits, see the [Workshop documentation](/docs/foundry/workshop/widgets-object-table/#inline-edits-cell-level-writeback).
### Background
在运行单个 action 时,编辑会逐个(按顺序)进行验证和提交。而 inline edits 则不同,它们以批量方式进行验证和提交。因此,并非所有 actions 都适合用作 inline edits。由于 inline edits 可能失败或产生意外结果,这些 actions 包括:

When running a single action, edits are validated and submitted one at a time (sequentially). Inline edits differ in that they are validated and submitted in bulk. Because of this, not all actions are suitable for inline edits. Actions that may fail or have unexpected results due to inline edits include:
* 任何尝试读取另一个 action 可能已写入的数据的 action,或

* 两个尝试写入同一 object 的 actions。

* Any action that attempts to read data to which another action could have written, or
* Two actions that try to write to the same object.
> **ℹ️ 注意**

> 当 inline edits 应用于 [Scenario](/docs/foundry/workshop/scenarios-overview/) 时,提交的 actions 将按顺序应用(以非确定性顺序),而不是像 inline edits 通常那样同时应用。因此,通常因多个 actions 尝试写入同一 object 而失败的 inline edit actions,在应用于 scenario 时可能会成功,但我们不建议构建依赖于此行为差异的应用程序。
> **ℹ️ 注意**

> When inline edits are applied to a [Scenario](/docs/foundry/workshop/scenarios-overview/), the submitted actions are applied sequentially (in a non-deterministic order) rather than simultaneously (as is normally the case with inline edits). As a result, inline edit actions that ordinarily fail due to multiple actions trying to write to the same object may succeed when applied to a scenario, though we do not recommend building applications that depend upon this difference in behavior.
### Valid inline Actions
Actions 必须提交不冲突的编辑,才能作为 Action-backed inline edits 有效发挥作用。实际上,这意味着在同一 table edit widget 中配置的多个 Actions 不得:

Actions must submit non-conflicting edits to be effective as Action-backed inline edits. In practice, this means multiple Actions configured in the same table edit widget must not:
* 写入同一 object,

* 创建相同的 link,或
* 尝试保持聚合值的一致性。

* Write to the same object,
* Create the same link, or
* Attempt to keep aggregate values consistent.
### Invalid inline Actions
**如果 inline edit 尝试编辑同一 object 两次,Actions 将返回错误。** 此外,inline edits 不支持添加或删除 join table links,否则将导致用户可见的错误消息。

**Actions will return an error if an inline edit attempts to edit the same object twice.** Also, adding or deleting join table links is not supported by inline edits and will result in a user-facing error message.
当用户应用 inline edits 时,[submission criteria](/docs/foundry/action-types/submission-criteria/) 将应用于每次编辑,但编辑将以批量方式提交。对于每个编辑后的 object,都会评估 parameter 和 global submission criteria,但引用共享对象或 linked objects 的 submission criteria 与 inline edits 不兼容。这是因为在应用 inline edits 时,累积的 submission criteria 会将编辑后的值与该列未编辑的值进行比较。在最终提交时,编辑将一次性全部提交,并且如果它们都通过相应 object 的 parameter 和 global submission criteria,则提交将成功。

As users apply inline edits, [submission criteria](/docs/foundry/action-types/submission-criteria/) will be applied to each edit, but the edits will be submitted in bulk. Both parameter and global submission criteria will be evaluated for each edited object, but submission criteria that reference shared or linked objects are not compatible with inline edits. This is because when applying inline edits, cumulative submission criteria compare the edited value to the unedited values for the column. At final submission, the edits will be submitted all at once and will succeed if they all pass parameter and global submission criteria for the corresponding object.
因此,在多个 Action types 之间共享的对象或 linked objects 上的 Submission criteria 会在每次编辑时评估一次,先于任何编辑的进行。

Submission criteria on objects shared between multiple Action types or linked objects are therefore evaluated once per edit, before any edits are made.
> **⚠️ 警告**

> 引用共享 Action 类型或链接对象的提交标准与内联编辑不兼容，并且批量更新对象可能违反提交标准规则——这些规则在按顺序（一次一个）应用时按预期工作。
> **⚠️ 警告**

> Submission criteria that reference shared Action types or linked objects are not compatible with inline edits, and bulk updating objects could violate submission criteria rules that work as expected when applied sequentially (one at a time).
#### Example: Invalid inline Actions
设想一个 `Delay Flight` Action，它可以在一个机场将单次航班最多延迟 20 分钟，而该机场可以将所有航班总共最多延迟 50 分钟。

Imagine a `Delay Flight` Action that can delay a single flight by a maximum of 20 minutes at an airport that can delay all flights by a maximum of 50 minutes.
* 两个提交标准——20 分钟的要求和 50 分钟的总和——将在每次更新单元格时进行评估。
* 由于尚未提交任何编辑，50 分钟的总和会将新的延迟与列中未编辑的延迟（即内联编辑开始之前的延迟）之和进行比较。
* 第二个提交标准（机场所有延迟之和必须小于 50 分钟）依赖于一个聚合值，并由列中的所有对象共享。
* 由于内联编辑是批量提交的，因此第二个提交标准在限制给定机场航班延迟的总持续时间方面将无法有效发挥作用；最终编辑的总和可能超过第二个提交标准所允许的 50 分钟。

* 此 Action 不适合用于表格编辑，因为与针对每个单元格单独运行该 Action 相比，它会导致结果不一致。

* Both submission criteria – the 20 minute requirement and the 50 minute total –  will be evaluated each time a cell is updated.
* Because no edits are yet submitted, the 50 minute total will compare the new delays to the sum of unedited delays in the column (the delays from before inline editing began).
* The second submission criteria (that all the delays at the airport sum to less than 50 minutes) relies on an aggregated value and is shared by all the objects in the column.
* Since inline edits are submitted in bulk, this second submission criteria will not be effective in limiting the total duration of flight delays at a given airport; the resulting edits could sum to greater than the 50 allowed by the second submission criteria.
* This Action would not be suitable for table editing as it would cause inconsistent results compared to running the Action individually for each cell.