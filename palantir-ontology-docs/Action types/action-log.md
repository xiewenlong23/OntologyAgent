<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/action-log/
---
# Action log
Action log 将所有 action 提交建模为 object types，以便在支持 object 的 Foundry 工具中进行分析和展示。可将 action log object type 用作决策工作流的输入，并用于监控 Ontology 的变更。

The action log models all action submissions as object types to be analyzed and displayed in object-aware Foundry tooling. Use an action log object type as an input to decision-making workflows and to monitor changes to your Ontology.
> **ℹ️ 注意**

> Action log 旨在捕获通过提交 actions 所做出的决策，并将这些决策作为 Ontology 中的数据进行提供。对于需要记录某个 object 所有编辑的使用场景，可以为 object type 启用 [edit history](/docs/foundry/object-edits/user-edit-history/)。
> **ℹ️ 注意**

> The action log is designed to capture decisions made by submitting actions and make these decisions available as data in the Ontology. For use cases where
> logging all edits to an object is desired, [edit history](/docs/foundry/object-edits/user-edit-history/) can be enabled for an object type.
## Background
Actions 是修改 Ontology 并触发相关副作用的主要方式。通常，这些 Ontology 修改是某项特定决策的结果，或伴随着数据审计需求。Action log 简化了表示这些决策和数据编辑的 object types 的生成与维护。为便于识别，所有 action log object types 都会以 `[LOG]` 作为前缀。

Actions are the primary way to modify the Ontology and trigger related side effects. Often, these Ontology modifications are the result of a specific decision or are accompanied by data audit requirements. The action log simplifies generation and maintenance of object types that represent these decisions and data edits. For easy identification, all action log object types are prefaced with `[LOG]`.
## Action log Ontology
Action log object types 与 action types 一一对应。提交一个 action 会生成一个对应的 action log object type 的新 object。该新创建的 object 会自动 link 到该已提交 action 所编辑的所有 objects。通过将 log object types 与 action types 进行一对一建模，action log 支持捕获超出特定 object 编辑之外的上下文，例如同时被编辑的其他 objects，以及 action 提交时 Ontology 所代表的世界状态。

Action log object types map one-to-one with action types. Submitting an action generates a single new object of the corresponding action log object type. This newly-created object is automatically linked to all objects edited by the submitted action. By modeling log object types one-to-one with action types, the action log supports capturing context beyond specific object edits, such as which other objects were concurrently edited and the state of the world (as represented by the Ontology) at the time of action submission.
例如，假设存在一个 `Close Alerts` action type，它将多个所选 `Alert` objects 的 "Status" property 修改为 "Closed"。在配置了 action log 的情况下，一次性关闭 10 个 `Alert` objects 将产生一个 `action log` object，并通过外键 links 关联到全部 10 个 `Alert` objects。

For example, imagine a `Close Alerts` action type that modifies the "Status" property of many selected `Alert` objects to "Closed". When configured with an action log, closing 10 `Alert` objects at once will yield a single `action log` object with foreign key links to all 10 `Alert` objects.
> **ℹ️ 注意**

> 要应用由 action log 支持的 action type，用户需要拥有 action log object type 的相应权限，就像他们需要对 action type 通过 rules 和 functions 创建或修改的任何其他 object types 拥有相应权限一样。
> **ℹ️ 注意**

> To apply an action log-backed action type, users need the appropriate permissions for the action log object type, just as they do for any other object types that the action type might create or modify through rules and functions.
### Action log schema
默认情况下，action log object types 会存储以下内容：

By default, action log object types store:
* **Action RID：** 单次 action 提交的唯一标识符

* **Action type RID：** 单个 action type 的唯一标识符

* **Action type version：** Action type 每次更新时自动递增的版本号

* **Timestamp：** Action 提交的 UTC 时间戳

* **UserId：** 提交 action 的用户的 Multipass 用户 ID

* **Edited objects：** Action 所编辑的所有 objects 的主键值。请注意，不支持存储除主键之外的被编辑 objects 的 properties。

* \[可选] **Summary：** 用于描述该 action 的可自定义字符串

* \[可选] **Parameter values**

* \[可选] **Object reference parameters 的 property 值**（当启用 `allow multiple values` 时，不支持 object reference parameters）

* **Action RID:** Unique identifier for a single action submission
* **Action type RID:** Unique identifier for a single action type
* **Action type version:** Version number that auto-increments each time an action type is updated
* **Timestamp:** UTC timestamp of action submission
* **UserId:** Multipass user ID for action submitting user
* **Edited objects:** Primary key values of all objects edited by the action. Note that storing properties of edited objects other than the primary key is not supported.
* \[Optional] **Summary:** A customizable string to describe the action
* \[Optional] **Parameter values**
* \[Optional] **Property values of object reference parameters** (this is not supported for object reference parameters if `allow multiple values` is enabled)
Action log object types 可配置为存储 action 未编辑的 object properties。这允许您存储数据编辑，以及与 Ontology 编辑的上下文或动机相关的信息。

Action log object types can be configured to store object properties that are not edited by the action. This allows you to store data edits as well as relevant information about the context of or motivation for the Ontology edits.
回到 `Close Alerts` action type 的示例，假设 `Alert` objects 还具有 "Priority" property（包含 "High Priority" 和 "Low Priority" 值）、"Created at" 时间戳以及 "Source" 机器。Action log 支持存储这些 properties，即使它们未被 `Close Alerts` 编辑。通过在 "Priority" 上进行聚合（无需编辑该列），我们可以回答诸如 "大多数 'High Priority' alerts 的来源是哪里？" 或 "关闭 'High Priority' alerts 需要多长时间？" 等问题。

Returning to the example of a `Close Alerts` action type, imagine the `Alert` objects also have a "Priority" property containing values "High Priority" and "Low Priority" as well as a "Created at" timestamp and a "Source" machine. The action log supports storing these properties, even if they are not edited by `Close Alerts`. By aggregating on "Priority", without editing the column we can answer questions such as "where is the source of most "High Priority" alerts?" or "how long does it take to close "High Priority" alerts?".
## Action log on function-backed action types
要为 function-backed action type 配置 action log，其对应的 Ontology edit function 必须配置 `Edits` provenance。有关 `Edits` provenance 的更多信息，请参阅 [functions 文档](/docs/foundry/functions/edits-overview/)。

To configure the action log for a function-backed action type, the backing Ontology edit function must have `Edits` provenance configured. See the [functions documentation](/docs/foundry/functions/edits-overview/) for more information on `Edits` provenance.
## Action log timeline
您可以使用自定义 Workshop widget 在时间线中查看 action log object types。使用此 widget，可将时间线配置为支持数据审计，以帮助回答 "什么发生了变更、由谁变更、何时变更？" 等问题。

You can view action log object types in a timeline using a custom Workshop widget. With this widget, the timeline can be configured to support data audits in order to help answer the questions "what changed, by whom, and when?"
在 Workshop 中，可以将多个 action log object types 进行 union，以获得某个使用场景内或整个 Ontology 的编辑的整体视图。

Within Workshop, action log object types can be unioned together for a holistic view of edits within a use case or across an Ontology.
通过选择 edited object type 来配置 action log 时间线。然后选择要显示的 action log object types，以及所需的 action log object type properties。

Configure the action log timeline by selecting the edited object type. Then choose which action log object types to display, along with the desired action log object type properties.