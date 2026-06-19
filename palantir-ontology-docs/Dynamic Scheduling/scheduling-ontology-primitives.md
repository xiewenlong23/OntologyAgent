<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives/
---
# Ontology primitives and data model configuration
用于动态调度的 Ontology 原语由一个 `Schedule` object 和一个或多个 `Resource` object 组成。首先在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中创建您的 object。至少，Workshop widget 需要两种 object type：一个 `Schedule` object 和一个 `Resource` object。

The Ontology primitives for dynamic scheduling are comprised of one `Schedule` object and one or more `Resource` objects. Begin by creating your objects in the [Ontology Manager](/docs/foundry/ontology-manager/overview/). At a minimum, the Workshop widget requires two object types: a `Schedule` object and a `Resource` object.
| Object Type | Description |
| --- | --- |
| Schedule object | A schedule object represents the task or activity of interest and should include a start and end time of when that event is occurring and/or the expected duration. |
| Resource object | A resource object represents any entity (such as a person, location, project, etc.) that the schedule object is being assigned to or scheduled against.  |
## Ontology requirements
`Schedule` object 必须满足下文概述的 property 和 link 要求。

The `Schedule` object must meet the property and link requirements outlined below.
### Required schedule object properties
| Object property | Type |
| --- | --- |
| Foreign key to resource | String |
| Start time | Timestamp |
| End time | Timestamp |
### Required Ontology links
Schedule object type 应链接到每个 resource object type。支持多对一和多对多关系。例如，在上面的示例中，许多任务可以分配给一架飞机。Widget 配置中的 **Resource Link Type** 决定了关系是多对一还是多对多。

The schedule object type should be linked to each resource object type. Both many-to-one and many-to-many relationships are supported. For instance, in the example above, many tasks can be assigned to one aircraft. The **Resource Link Type** in the widget configuration determines whether the relationship is many-to-one or many-to-many.
## Example: Aircraft maintenance schedule
以下示例演示了为飞机安排维护任务的过程。

The example below demonstrates the process of scheduling maintenance tasks for aircraft.
### Simple configuration
下面展示了 Dynamic Scheduling Workshop widget 最低要求的两种 object type 配置。

The two-object-type configuration, the minimum requirement for the Dynamic Scheduling Workshop widget, is illustrated below.
* **Schedule object type：** 在下面的示例中，维护任务是一项有时间限制的活动。

* **Resource object type：** 飞机是执行任务的 object/地点。

* **Schedule object type:** In the example below, maintenance tasks are a time-bound activity.
* **Resource object type:** Aircraft are the object/place where the tasks are conducted.

> 📷 **[图片: Schedule object type.]**

> 📷 **[图片: Schedule object type.]**

### Advanced configuration
动态调度数据支持除两种 object type 模型之外的各种其他配置，允许 application builder 创建复杂的、先进的工作流。

The dynamic scheduling data supports a variety of additional configurations beyond the two-object-type model, allowing application builders to create complex, advanced workflows.
在上述两种 object type 模型的基础上，除了调度维护任务在已分配的飞机上执行的时间之外，用户还可以通过将任务分配给特定的机械师来确定*谁*将执行维护任务。在如下图所示的新 Ontology 中，机械师 object 充当 **第二个 resource object type**，其数量可以不受限制。

Building on the two-object-type model above, in addition to scheduling *when* maintenance tasks will occur on an assigned aircraft, users can also determine *who* will carry out the maintenance task by assigning the task to a specific mechanic. In this new Ontology, as pictured below, the mechanic object acts as a **second resource object type**, which can be unlimited in number.
* **Schedule object type：** 维护任务是一项有时间限制的活动。

* **Resource object type 1：** 飞机是执行任务的 object/地点。

* **Resource object type 2：** 将执行已分配维护任务的机械师。

* **Schedule object type:** Maintenance tasks are a time-bound activity.
* **Resource object type 1:** Aircraft are the object/place where the tasks are conducted.
* **Resource object type 2:** Mechanic who will carry out the assigned maintenance task.

> 📷 **[图片: Advanced schedule object type.]**

> 📷 **[图片: Advanced schedule object type.]**

