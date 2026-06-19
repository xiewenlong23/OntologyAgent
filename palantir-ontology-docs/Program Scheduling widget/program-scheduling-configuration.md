<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/program-scheduling-configuration/
---
# Widget configuration
Program Scheduling widget 包含若干必填和可选的配置设置。本节提供了一个概览，必填设置会被特别标记。

The Program Scheduling widget includes several required and optional configuration settings. This section presents an overview, and the required settings are specifically marked as such.
## Timeline
* **Start timestamp \[REQUIRED]:** 设置一个 timestamp 变量以控制 timeline 轴的起点。

* **End timestamp \[REQUIRED]:** 设置一个 timestamp 变量以控制 timeline 轴的终点。

* **Start timestamp \[REQUIRED]:** Set a timestamp variable to control the beginning of the timeline axis.
* **End timestamp \[REQUIRED]:** Set a timestamp variable to control the end of the timeline axis.
## Input data (layers)
您可以使用多个 layers 在单个 timeline 上表示不同的 workstreams 或 object types。例如，一个 layer 可以显示 project tasks，而另一个 layer 叠加显示关键 milestones。每个 layer 都是可独立配置的。

You can use multiple layers to represent different workstreams or object types on a single timeline. For example, one layer could display project tasks while another overlays key milestones. Each layer is independently configurable.
* **Data**
* **Object set \[REQUIRED]:** 提供该 layer 的 tasks 或 events 的 object set。

* **Puck type \[REQUIRED]:** 为该 layer 中的 items 选择视觉类型。可选项为 **Standard**、**Background** 或 **Event**。有关每种类型的描述，请参阅 [puck types](/docs/foundry/dynamic-scheduling/program-scheduling-overview/#puck-types) 部分。

* **Start time property \[REQUIRED]:** 选择一个 date 或 timestamp property 用作 start time。

* **End time property:** 选择一个 date 或 timestamp property 用作 end time。Event pucks 不需要此 property。

* **Dependency property:** 对于 standard pucks，选择一个 array property 来定义 tasks 之间的 dependency relationships。Dependencies 显示为连接 timeline 上相关 pucks 的箭头。有关更多信息，请参阅 [dependencies](/docs/foundry/dynamic-scheduling/program-scheduling-overview/#dependencies) 部分。

* **Data**
* **Object set \[REQUIRED]:** The object set that provides the tasks or events for this layer.
* **Puck type \[REQUIRED]:** Select the visual type for items in this layer. Options are **Standard**, **Background**, or **Event**. See the [puck types](/docs/foundry/dynamic-scheduling/program-scheduling-overview/#puck-types) section for a description of each type.
* **Start time property \[REQUIRED]:** Select a date or timestamp property to use as the start time.
* **End time property:** Select a date or timestamp property to use as the end time. Event pucks do not require this property.
* **Dependency property:** For standard pucks, select an array property that defines dependency relationships between tasks. Dependencies are displayed as arrows connecting related pucks on the timeline. See the [dependencies](/docs/foundry/dynamic-scheduling/program-scheduling-overview/#dependencies) section for more information.
* **Display and formatting**
* **Grouping properties:** 选择一个或多个 properties 以按其组织和嵌套 table rows，例如 project name、team 或 phase。您可以将每个 grouping property 的排序方向配置为升序或降序。

* **Detail properties:** 选择当用户选择一个 puck 时显示在 detail card 中的 properties。

* **Color:** 选择在 timeline 中显示 pucks 时使用的颜色。

* **Static:** 为该 layer 中的所有 pucks 选择单一颜色。

* **Dynamic:** 配置条件格式规则以根据 property 值应用不同的颜色 — 例如，根据 status 或 priority 为 tasks 着色。

* **Display and formatting**
* **Grouping properties:** Select one or more properties to organize and nest the table rows by, such as project name, team, or phase. You can configure the sort direction for each grouping property as ascending or descending.
* **Detail properties:** Select properties to display in the detail card that appears when a user selects a puck.
* **Color:** Select the colors to use when displaying pucks in the timeline.
* **Static:** Select a single color for all pucks in this layer.
* **Dynamic:** Configure conditional formatting rules to apply different colors based on property values — for example, coloring tasks by status or priority.
* **Interactions（交互）**

* **Save handler action（保存处理 Action）：** 对于 standard puck 和 event puck，选择一个 action，以便在用户拖动或调整 puck 大小时触发。该 action 接收更新后的开始和结束时间，从而可以将排程变更写回 Ontology。此 action 必须接受以下参数：

* Schedule object
* Start time
* End time
* **Interactions**
* **Save handler action:** For standard and event pucks, select an action to trigger when a user drags or resizes a puck. The action receives the updated start and end times, allowing you to write scheduling changes back to the Ontology. This action must accept as parameters:
* Schedule object
* Start time
* End time
如果您希望编辑依赖关系箭头，则需要为依赖关系数组属性添加一个参数。

If you would like to edit dependency arrows, you will need to add a parameter for the dependency array property.
* **Right-click menu（右键菜单）：** 配置当用户右键单击 puck 时显示的自定义上下文菜单项。每个菜单项可以触发一个 action 或一个 Workshop event。

* **Right-click menu:** Configure custom context menu items that appear when a user right-clicks a puck. Each menu item can trigger an action or a Workshop event.
## Interface
* **Expand groups by default（默认展开分组）：** 启用后，widget 加载时会展开所有表格分组。禁用时，分组默认处于折叠状态。

* **Hide arrows by default（默认隐藏箭头）：** 启用时，puck 之间的依赖关系箭头在初始状态下是隐藏的。用户可以在运行时切换箭头的可见性。

* **Show current time indicator（显示当前时间指示器）：** 在时间轴上显示一条表示当前日期和时间的垂直线。

* **Expand groups by default:** When enabled, all table groups are expanded when the widget loads. When disabled, groups start collapsed.
* **Hide arrows by default:** When enabled, dependency arrows between pucks are hidden initially. Users can toggle arrow visibility at runtime.
* **Show current time indicator:** Display a vertical line on the timeline representing the current date and time.
## Output
* **Selected object set（已选对象集）：** 一个可变的输出变量，用于捕获当前选中的对象。此对象集可以被当前模块内的其他 Workshop widget 使用。

* **Selected object set:** A mutable output variable that captures the currently selected objects. This object set can be used by other Workshop widgets within the current module.