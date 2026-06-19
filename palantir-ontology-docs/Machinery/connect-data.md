<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/machinery/connect-data/
---
# Connect data to Machinery
通过将 process 连接到 datasource，您可以弥合抽象的 process 定义与现实世界观察之间的差距。这些数据可用于进行初步的 [process mining](/docs/foundry/machinery/process-mining/) 或 [监控性能并查找瓶颈](/docs/foundry/machinery/analyze-andonitor/)。

By connecting a process to a datasource, you can bridge the gap between an abstract process definition and real-world observations. This data can be used to conduct initial [process mining](/docs/foundry/machinery/process-mining/) or to [monitor performance and find bottlenecks](/docs/foundry/machinery/analyze-and-monitor/).
Machinery 连接到 ontology 中的两种类型的 object 数据：[process object](#process-objects) 和 [log object](#log-objects)。用于数据配置的面板可通过主工具箱或从 process 容器访问。

Machinery connects to two types of object data in the ontology: [process objects](#process-objects) and [log objects](#log-objects). The side panel for data configuration is accessible through the main toolbox or from process containers.
## Process objects
Process object 是一个经历 process 的实体。

A process object is an entity that goes through a process.
例如，对于入职流程来说，这可能是一个 `Employee`；对于采购到付款流程来说，这可能是一个 `Invoice`。实体的 state 由一个字符串 property 显式跟踪，通常称为 `state`。`state` property 的值（例如 "created" 或 "approved"）由 graph 上的 state 节点表示。

For example, this may be an `Employee` for an onboarding process, or an `Invoice` for a purchase-to-pay process. The state of the entity is explicitly tracked by a string property, typically called `state`. The values of the `state` property (for instance, "created" or "approved") are represented by state nodes on the graph.
> **ℹ️ 注意**

> State value 可能存在依赖项，例如 action 中的提交条件或由特定 state 条件触发的 automations。在 Machinery 中更改 state value 不会更新这些依赖项，也不会更改 ontology data 中的值。
> **ℹ️ 注意**

> A state value may have dependencies, like submission criteria in actions or automations that are triggered by a certain state condition. Changing the state value in Machinery does not update these dependencies, nor does it change the values in the ontology data.
在 multi-process 设置中，每个 process container 恰好捕获 object type 上的一个 state property。

In the multi-process setting, each process container captures exactly one state property on an object type.
![Example of a multiple object type process, showcasing multiple processes, nesting, and hierarchy.](/docs/resources/foundry/machinery/multiple-object-type-processes.png)
如上面的 resource 示例截图所示，一个 object type 可以有多个 state property；例如，一个粗粒度的 state 和一个细粒度的 state。

As in the resource example screenshot above, an object type can have multiple state properties; for instance, a coarse state and a granular state.
Process object type 表示实体的最新 state，因此无法提供有关 state transitions 和时间模式的信息。

The process object type represents the latest state of the entity, and therefore cannot inform on state transitions and temporal patterns.

> 📷 **[图片: Ontology configuration side panel.]**

> 📷 **[图片: Ontology configuration side panel.]**

## Log objects
Log object 表示对实体 state 的单个更改。Log objects 包含对 process entity 的引用、其 previous state、其 new state 以及 transitions 的时间。

A log object represents an individual change to an entity’s state. Log objects contain a reference to the process entity, its previous state, its new state, and the timing of the transitions.
* **Log ID (string) \[required]：** Log object 的 primary key。

* **Process ID (string) \[required]：** 正在被跟踪的 process object 的 primary key。在设置 process object 与 Log object 之间的 Ontology link 时使用。

* **Old state (string) \[required]：** Transition 的起始 state。

* **New state (string) \[required]：** Transition 的结束 state。

* **Timestamp (timestamp) \[required]：** 进入结束 state 的时间戳。

* **isLatest (boolean) \[optional]：** 如果此 log 是 process object 的最新记录，则为 True，否则为 False。

* **Duration (long) \[optional]：** 自进入 old state 以来的持续时间（以毫秒为单位）。

* **Path (string) \[optional]：** 迄今为止遇到的所有 state 的列表，包括当前 state。必须是序列化的 JSON 字符串。

* **Action type RID (string) \[optional]：** 导致 transition 的 action type 的标识符。通常，外部更改为 `NULL`。

* **Owning RID (string) \[optional]：** 执行该 action 的 application 的标识符。允许区分手动和自动化的 Actions。外部更改为 `NULL`。

* **Log ID (string) \[required]:** The primary key of the log object.
* **Process ID (string) \[required]:** The primary key of the process object that is being tracked. Use when setting up an Ontology link between the process object and the Log object.
* **Old state (string) \[required]:** The start state of the transition.
* **New state (string) \[required]:** The end state of the transition.
* **Timestamp (timestamp) \[required]:** Timestamp of entering the end state.
* **isLatest (boolean) \[optional]:** True if this log is the most recent for the process object, otherwise False.
* **Duration (long) \[optional]:** Duration in milliseconds since entering the old state.
* **Path (string) \[optional]:** A list of all states encountered so far, including the current state. Must be a serialized JSON string.
* **Action type RID (string) \[optional]:** An identifier of the action type that caused the transition. Typically, `NULL` for external changes.
* **Owning RID (string) \[optional]:** An identifier of the application from which the action was executed. Allows discrimination between manual and automated Actions. `NULL` for external changes.
维护这样的 log 需要在编辑时进行编排。Machinery 提供了一个标准解决方案，可以从 application 内部进行安装。设置 log object type 需要一个 process object type。

Maintaining such a log requires orchestration when edits are made. Machinery provides a standard solution that can be installed from within the application. Setting up a log object type requires a process object type.

> 📷 **[图片: Ontology configuration side panel.]**

> 📷 **[图片: Ontology configuration side panel.]**

一个 dialog 将指导您完成设置。您可以选择要跟踪的编辑来源：

A dialog will guide you through the setup. You can choose which source of edits you want to track:
* 如果 process object type 接收来自外部 datasource 的更改，您可以选择并配置一个 changelog dataset。

* 如果 process object type 可以在 platform 中进行编辑，您可以选择 [在 process object type 上启用 edit history](/docs/foundry/object-edits/user-edit-history/)，并将那些编辑包含在 log object type 中。Machinery 将自动创建一个 edit history 的 materialization dataset，以便将其用于聚合分析。

* If the process object type receives changes from external datasource, you can select and configure a changelog dataset.
* If the process object type can be edited in the platform, you can choose to [enable edit history on the process object type](/docs/foundry/object-edits/user-edit-history/) and include those edits in the log object type. Machinery will automatically create a materialization dataset of the edit history to make it available for aggregated analysis.
> **ℹ️ 注意**

> 目前不支持对具有多个 datasources 或 row-level permissions 的 object types 跟踪来自 platform 编辑的 logs。
> **ℹ️ 注意**

> Tracking logs from platform edits for object types with multiple datasources or row-level permissions is currently not supported.
如果您想跟踪来自外部 datasources 的更改，您必须选择一个采用标准 changelog 格式的 dataset，这是 Machinery 的 log object type schema 的一个更简单的版本。该 dataset 通常是 object type datasource 的上游，并包含以下列：

If you want to track changes from external datasources, you must select a dataset in standard changelog format, which is a simpler version of Machinery’s log object type schema. That dataset is typically upstream of the object type datasource, and contains the following columns:
* **processId (string) \[required]:** 流程实体的唯一标识符。

* **state (string) \[required]:** 流程进入的新状态。

* **timestamp (timestamp) \[required]:** 发生状态转换时的时间戳。

* **isDeleted (boolean) \[optional]:** 将实体标记为已删除的 Property。如果最新日志的 isDeleted 为 `True`，则该对象不会出现在 ontology 中。

* **processId (string) \[required]:** A unique identifier of the process entity.
* **state (string) \[required]:** The new state the process has entered.
* **timestamp (timestamp) \[required]:** The timestamp at which the transition occurred.
* **isDeleted (boolean) \[optional]:** Property that flags an entity as deleted. If isDeleted of the latest log is `True`, that object will not appear in the ontology.
确认后，Machinery 将把 [Marketplace product](/docs/foundry/marketplace/overview/) 安装到您选择的文件夹中。该产品包含一个 [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) pipeline，用于将配置源中的日志条目计算为正确的格式。该产品还会部署日志 Object Type 本身，并通过 ontology link 链接到您的流程 Object Type。

On confirmation, Machinery will install a [Marketplace product](/docs/foundry/marketplace/overview/) into a folder of your choosing. This product contains a [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) pipeline that computes log entries from the configured sources into the correct format. The product also deploys the log object type itself with an ontology link to your process object type.
安装完成后，pipeline 需要完成初始构建，并且日志 Object Type 需要在数据库中建立索引，之后数据才可用于挖掘和监控。

After the installation is complete, the pipeline needs to complete an initial build, and the log object type needs to be indexed in the databases before the data is available for mining and monitoring.
> **ℹ️ 注意**

> 部署的 pipeline 计划在任一数据源发生更改时运行。因此，日志 Object Type 相比流程 Object Type 会延迟一次构建和一次索引作业，通常约为 2-5 分钟。如果您需要实时更新，则需要维护一个自定义日志 Object Type。
> **ℹ️ 注意**

> The deployed pipeline is scheduled to run on every change to any of its datasources. As a result, the log object type lags behind the process object type by one build and one indexing job, typically about 2-5 minutes. If you require real-time updates, you need to maintain a custom log object type.
如果自定义日志 Object Type 满足最小 schema，您可以手动映射它。

You can manually map a custom log object type if it fulfills the minimal schema.