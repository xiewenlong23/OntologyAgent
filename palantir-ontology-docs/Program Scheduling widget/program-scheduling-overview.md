<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/program-scheduling-overview/
---
# Program Scheduling widget
**Program Scheduling** widget 是一个 Workshop widget，提供项目（programs）、项目（projects）和任务（tasks）的按时间顺序排列的视图。使用它来跟踪各个工作流的进度，可视化任务之间的相互关系，并识别可能影响下游交付物的阻塞项。该 widget 可与任何具有表示开始和结束时间的日期或时间戳属性的 object type 配合使用。

The **Program Scheduling** widget is a Workshop widget that provides a chronological view of programs, projects, and tasks. Use it to track progress across workstreams, visualize how tasks relate to one another, and identify blockers that may impact downstream deliverables. The widget works with any object type that has date or timestamp properties representing start and end times.
配置 Program Scheduling widget 的模块构建者可以：

Module builders configuring a Program Scheduling widget can:
* 在可交互的时间轴上跟踪项目和任务进度，任务以 puck 的形式显示，反映其计划持续时间。

* 将任务依赖关系可视化为 puck 之间的箭头，使用户能够轻松识别阻塞点，并了解延迟如何在项目中级联传播。
* 将任务组织成可折叠的层级表格分组，与时间轴并排显示 —— 例如，按项目、团队或阶段分组。

* Track project and task progress on an interactive timeline, with tasks displayed as pucks that reflect their scheduled duration.
* Visualize task dependencies as arrows between pucks, making it easy for users to identify blockers and understand how delays cascade through a program.
* Organize tasks into a hierarchical table of collapsible groups alongside the timeline — for example, grouped by project, team, or phase.
在下面的示例中，Program Scheduling widget 显示按项目阶段分组的任务，并使用依赖关系箭头突出显示各交付物之间的关系。

In the example below, the Program Scheduling widget displays tasks grouped by project phase, with dependency arrows highlighting the relationships between deliverables.

> 📷 **[图片: Program Scheduling widget 示例：显示按项目阶段分组且交付物之间带有依赖关系箭头的任务。]**

> 📷 **[图片: Program Scheduling widget example: Displaying tasks grouped by project phase with dependency arrows between deliverables.]**

## Puck types
数据层中的每个任务或事件在时间轴上渲染为一个 **puck**。puck 类型按层配置，决定了项目的可视化方式以及可用的交互。

Each task or event in a data layer is rendered as a **puck** on the timeline. The puck type is configured per layer and determines how items are visualized and what interactions are available.
* **Standard pucks（标准 puck）：** 表示跨时间范围的任务或活动的矩形条。这些支持依赖关系箭头，用于可视化任务之间的依赖关系。

* **Background pucks（背景 puck）：** 表示更广泛时间段的阴影矩形区域，例如项目阶段、规划周期或评审窗口。Background puck 为其前面的任务提供视觉上下文，但是只读的，用户无法编辑。

* **Event pucks（事件 puck）：** 在单一时间点上的细垂直标记。这些可以表示里程碑、截止日期或关键决策点。

* **Standard pucks:** Rectangular bars representing tasks or activities that span a time range. These support dependency arrows to visualize dependencies between tasks.
* **Background pucks:** Shaded rectangular regions representing broader time periods such as project phases, planning cycles, or review windows. Background pucks provide visual context for the tasks in front of them but are read-only and cannot be edited by users.
* **Event pucks:** Thin vertical markers at a single point in time. These can represent milestones, deadlines, or key decision points.
## Dependencies
Program Scheduling widget 可以将任务依赖关系可视化为连接时间轴上相关 puck 的箭头，帮助用户理解顺序约束并识别哪些任务正在阻塞下游工作。依赖关系按层配置，通过在 object type 上选择一个引用同一层中其他对象主键的数组属性来完成。

The Program Scheduling widget can visualize task dependencies as arrows connecting related pucks on the timeline, helping users understand sequencing constraints and identify which tasks are blocking downstream work. Dependencies are configured per layer by selecting an array property on the object type that references the primary keys of other objects in the same layer.
* 依赖关系箭头仅对 standard puck 可用。

* 将鼠标悬停在 puck 上会高亮显示其依赖关系链，便于追踪哪些任务被阻塞以及哪些任务正在阻塞其他任务。

* 您可以使用 **Hide arrows by default** interface 选项默认隐藏箭头。用户可以在运行时切换箭头的可见性。

* Dependency arrows are only available for standard pucks.
* Hovering over a puck highlights its dependency chain, making it easier to trace which tasks are blocked and which are blocking others.
* You can hide arrows by default using the **Hide arrows by default** interface option. Users can toggle arrow visibility at runtime.
## Widget layout
下图提供了完整 widget 布局的概览。

The image below provides an overview of the full widget layout.

> 📷 **[图片: Overview of the Program Scheduling widget layout.]**

> 📷 **[图片: Overview of the Program Scheduling widget layout.]**

1. **Timeline:** 组件主体显示沿水平时间轴排列的任务块，时间轴由可配置的起始和结束时间戳控制。如果进行了编辑，**Save Changes** 按钮将出现在右侧。

2. **Rows:** 主体左侧显示按可配置属性（如项目、团队或阶段）组织的层级行表。分组可以展开或折叠。

3. **Dependencies:** 箭头连接相关任务块，以可视化排序约束并突出显示阻塞项。

4. **Detail card:** 选择一个任务块将打开一个详情卡片，显示所选任务的属性。用户也可以在此视图中编辑和遍历 Link。

1. **Timeline:** The body of the widget displays task pucks positioned along a horizontal time axis controlled by configurable start and end timestamps. If edits have been made, the **Save Changes** button will appear on the right.
2. **Rows:** The left side of the body displays a hierarchical table of rows organized by configurable properties such as project, team, or phase. Groups can be expanded or collapsed.
3. **Dependencies:** Arrows connect related task pucks to visualize sequencing constraints and highlight blockers.
4. **Detail card:** Selecting a puck opens a detail card displaying properties for the selected task. Users can also edit and traverse links in this view.