<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-concepts/
---
# Core concepts
Dynamic scheduling 基于以下核心概念构建：

Dynamic scheduling is built on the following core concepts:
## Schedule object
Schedule object 是 Ontology 对任务或活动的表示，应包括事件发生时的开始和结束时间以及/或其预期持续时间。

A schedule object is the Ontology's representation of a task or activity, and should include a start and end time of when that event is occurring and/or its expected duration.
## Resource object
Resource object 表示 schedule object 被分配或调度的任何实体（例如人员、地点、项目等）。

A resource object represents any entity (such as person, location, project, etc.) that the schedule object is being assigned to or scheduled against.
## Scheduling widgets
### Scheduling Gantt chart
Scheduling Gantt chart 渲染一个用于调度或资源分配工作流的交互式图表，由两个核心元素组成：

The scheduling Gantt chart renders an interactive chart for scheduling or resource allocation workflows and consists of two core elements:
* **Schedule objects：** Schedule objects（例如，飞机维护任务）在 scheduling Gantt chart 上以 pucks（块）的形式渲染。用户可以拖放 pucks 来更新 schedule object 的开始时间、结束时间和/或 linked resource object。

* **Resource objects：** Resource objects（例如，飞机维修技师）在 scheduling Gantt chart 中以行的形式渲染。当用户将光标悬停在某一行上时，卡片将显示 resource object 的 title、module builder 选择的 properties，以及指向 object view 的链接。

* **Schedule objects:** Schedule objects (for example, aircraft maintenance tasks) are rendered as pucks (blocks) on the scheduling Gantt chart. Users can drag and drop pucks to update a schedule object's start time, end time, and/or linked resource object.
* **Resource objects:** Resource objects (for example, an aircraft mechanic) are rendered as rows in the scheduling Gantt chart. When a user hovers over a row, cards will display the resource object's title, properties selected by the module builder, and a link to the object view.
Scheduling Gantt chart widget 为 module builders 提供了灵活性，可选择 interface 颜色和交互行为，例如 schedule object pucks 的 puck allocation behavior 和 snap behavior。

The scheduling Gantt chart widget provides module builders with the flexibility to choose interface colors and interactions such as puck allocation behavior and snap behavior for schedule object pucks.
有关更多信息，请参阅 [scheduling Gantt chart widget](/docs/foundry/dynamic-scheduling/scheduling-gantt-chart-widget/) 文档。

For more information, see the [scheduling Gantt chart widget](/docs/foundry/dynamic-scheduling/scheduling-gantt-chart-widget/) documentation.
### Calendar
Calendar 以日、周、月或自定义视图渲染 `Schedule` objects。

The calendar renders `Schedule` objects over day, week, month, or custom views.
## Scenarios
[Scenarios](/docs/foundry/workshop/scenarios-overview/) 支持创建和比较 what-if 分析。通过使用 scenarios，在 widget 中所做的编辑不会直接写入 Ontology。相反，它们作为 proposed changes 创建，可以被执行。

[Scenarios](/docs/foundry/workshop/scenarios-overview/) enable the creation and comparison of what-if analyses. By using scenarios, edits made in the widget are not directly written to the Ontology. Instead, they are created as proposed changes that can be actioned.
## Schedule save action handler
Schedule save action handler 用于在 scheduling Gantt chart widget 中执行 Ontology 编辑。此 action 是必需的，以便用户可以通过拖放来编辑 pucks，并将这些更改暂存（stage）到 Ontology 中。大多数用例可以使用简单的 Ontology modify action，但可以使用 [function-backed custom save action](/docs/foundry/action-types/function-actions-overview/) 来处理高级工作流。Function-backed action 必须至少接受以下可选参数：

A schedule save action handler is used to execute Ontology edits in the scheduling Gantt chart widget. This action is required so users can edit pucks by dragging and dropping, and stage those changes in the Ontology. Most use cases can use a simple Ontology modify action, but a [function-backed custom save action](/docs/foundry/action-types/function-actions-overview/) can be used for advanced workflows. A function-backed action must accept at least the following optional parameters:
* Resource ID（到 resource object 的外键）

* Start time
* End time
* Resource ID (the foreign key to the resource object)
* Start time
* End time
## Suggestion function
[Suggestion functions](/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/) 根据您组织定义的逻辑，指示潜在 schedule object placement 的适用性。当用户选择 schedule object puck 时，用户界面会高亮显示 schedule 中满足规则逻辑所定义条件的区域。规则逻辑的输出可用于高亮显示可以进行分配的区域，或者相反地，高亮显示无法进行分配的区域。Application builders 可以通过 Workshop widget configuration 中的一个设置来强制执行这些规则。开启后，此功能将强制将 puck 放置到最近的高亮显示区域。

[Suggestion functions](/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/) indicate the suitability of a potential schedule object placement based on logic defined by your organization. When a user selects a schedule object puck, the user interface highlights regions in the schedule that meet the conditions defined in the rule logic. The output of the rule logic can be used to highlight areas where an assignment can be made or, by contrast, areas where assignments cannot be made. Application builders have the option to enforce these rules through a setting in the Workshop widget configuration. When turned on, this feature will force placement of the puck to the closest highlighted region.
## Search function
[Search functions](/docs/foundry/dynamic-scheduling/scheduling-search-functions/) 充当您的"问题解决者"，提供根据您的特定需求和标准量身定制的 scheduling recommendations。该 function 根据用途和需求返回一组 schedule objects 或 time slots。通过在 scheduling Gantt chart widget 中右键单击来执行 search function。Recommendation function 始终考虑当前的世界状态，确保 recommendations 考虑用户在活动场景中所做的任何 scheduling 更改。

[Search functions](/docs/foundry/dynamic-scheduling/scheduling-search-functions/) act as your "problem solver," providing scheduling recommendations tailored to your specific needs and criteria. The function returns a set of schedule objects or time slots, depending on the purpose and requirements. Execute a search function by right-clicking in the scheduling Gantt chart widget. The recommendation function always takes the current state of the world into consideration, ensuring that recommendations take into account any scheduling changes users have made in the active scenario.
### Validation rule
[Validation rules](/docs/foundry/dynamic-scheduling/scheduling-validation-rules/) 允许您将 scheduling constraints 编码化，使终端用户能够在了解定义其工作流的限制和约束的情况下构建或修改 schedule。每个 validation rule 都由一个 function 支持，该 function 评估 assignment object 的当前状态是否满足 function 逻辑中定义的某个条件。

[Validation rules](/docs/foundry/dynamic-scheduling/scheduling-validation-rules/) allow you to codify scheduling constraints, enabling end users to build or modify schedules with an understanding of the limitations and restrictions that define their workflows. Each validation rule is backed by a function that evaluates whether the current state of an assignment object meets a certain condition as defined in the function logic.