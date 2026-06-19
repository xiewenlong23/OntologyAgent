<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-getting-started/
---
# Getting started
以下指南提供了实施动态排程 workflow 初始版本的步骤。请查看每个部分中引用的文档以获取更多信息。

The following guide provides the steps to implement a first version of your dynamic scheduling workflow. Review the referenced documentation in each section for more information.
## 1. Create core Ontology objects
您必须创建以下核心 object types 才能构建动态排程 workflow:

You must create the following core object types to build a dynamic scheduling workflow:
* 创建一个 `Schedule` object type。这表示资源所分配到的事件、任务或时段。例如,您的 `Schedule` object type 可以是 `Maintenance Tasks`,这些任务需要分配给 `Technicians`。

* object type 必须包含用于保存外键的 properties,以便与 resource object type(s) 建立关系。

* 此 object type 可以包含一个 `fixed duration` Boolean property,用于强制执行或不强制执行 `Schedule` 的静态持续时间。

* 您必须允许对此对象进行编辑,因为 start/end/duration 以及与 resources 的关系将在整个过程中被编辑。

* 创建一个或多个 resource object types,表示要分配到 schedule 的 resources。例如,需要在任务上工作的人员（即 `Technician`）。

* 在 `Schedule` object type 与不同的 `Resource` object types 之间创建 links。

* 为每个 `Schedule` 创建一个 save handler action。有关更多信息,请参阅 [drag and drop](/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/)。

* save handler 必须修改 `Schedule` 对象上的以下参数。每个参数必须标记为 optional。

* Resource ID（resource 对象的外键）

* Start Time
* End Time
* 您 action 中的 parameter IDs 必须与 schedule object type 中使用的 property IDs 完全匹配（例如,如果您的 property 是 `start_time`,则 parameter ID 也必须为 `start_time`）。

* start time 和 end time action parameters 必须与 schedule object type 上对应 properties 具有相同的 type classes（`schedules:schedulable-start-time` 和 `schedules:schedulable-end-time`）。

* Create a `Schedule` object type. This represents the events, assignments, or slots to which resources are allocated. For example, your `Schedule` object type may be `Maintenance Tasks`, which need to be assigned to `Technicians`.
* The object type must have properties that hold foreign keys to create relations with the resource(s) object types.
* This object type can have a `fixed duration` Boolean property to enforce or not enforce a static duration of the `Schedule`.
* You must enable edits on this object, as the start/end/duration and relations to the resources will be edited throughout this process.
* Create one or more resource object types that represent the resources to allocate to the schedule. For example, the persons that need to work on a task (the `Technician`).
* Create links between the `Schedule` object type and the different `Resource` object types.
* Create a save handler action for each `Schedule`. See [drag and drop](/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/) for more information.
* A save handler must modify the following parameters on the `Schedule` object. Each parameter must be marked as optional.
* Resource ID (the foreign key to the resource object)
* Start Time
* End Time
* The parameter IDs in your action must exactly match the property IDs used in your schedule object type (for example, if your property is `start_time`, the parameter ID must also be `start_time`).
* The start time and end time action parameters must have the same type classes (`schedules:schedulable-start-time` and `schedules:schedulable-end-time`) as the corresponding properties on your schedule object type.
有关每个 object type 架构的更多信息,请查看 [dynamic scheduling Ontology primitives documentation](/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives/)。

Review the [dynamic scheduling Ontology primitives documentation](/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives/) for more information about the schema of each object type.
## 2. Configure the widget in Workshop
创建完核心对象后,您现在可以配置 widget 以在 Workshop 中使用。

With the core objects created, you can now configure the widget for use in Workshop.
至少，scheduling Gantt chart 配置需要：

At minimum, the scheduling Gantt chart configuration requires:
* **Timeline Data（时间轴数据）：** 定义 chart 全局边界的开始和结束时间戳。

* **Row Data（行数据）：** 对应于 chart 每个行的 `Resource` 对象。

* **Input Data (Pucks)（输入数据 Pucks）：** 至少一个 schedule layer，其中包含：

* **Schedule Object Set（Schedule 对象集）：** 该 layer 的 `Schedule` 对象。

* **Save Handler Action（保存处理器 Action）：** 对应于 `Schedule` 对象的 save handler action。

* 您应该使用 dropdown 中 widget 提供的 parameters，在配置 options 中指定默认的 save handler action parameters。

* **Timeline Data:** Start and end timestamps that define the global bounds of the chart.
* **Row Data:** The `Resource` objects corresponding to each row of the chart.
* **Input Data (Pucks):** At least one schedule layer with:
* **Schedule Object Set:** The `Schedule` objects for this layer.
* **Save Handler Action:** The corresponding save handler action for the `Schedule` object.
* You should specify the default save handler action parameters within the configuration options using the widget-provided parameters available in the dropdown.
请查看 [scheduling Gantt chart widget documentation](/docs/foundry/dynamic-scheduling/scheduling-gantt-chart-widget/) 以获取更多信息。

Review the [scheduling Gantt chart widget documentation](/docs/foundry/dynamic-scheduling/scheduling-gantt-chart-widget/) for more information.