<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-gantt-chart-widget/
---
# Scheduling Gantt Chart widget
Scheduling Gantt Chart 是一个 Workshop widget，可为 scheduling 或 resource allocation workflows 呈现交互式 Gantt chart。在设置 widget 之前，请确保您已配置好 [dynamic scheduling Ontology](/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives/)。

The Scheduling Gantt Chart is a Workshop widget that renders an interactive Gantt chart for scheduling or resource allocation workflows. Before setting up the widget, ensure you have configured your [dynamic scheduling Ontology](/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives/).
配置 Scheduling Gantt Chart widget 的 Module builders 可以：

Module builders configuring a Scheduling Gantt Chart widget can:
* 为 resource object 行设置 title 和 sub-title properties（包括 icons 和 function backed properties）。

* 选择出现在右键菜单中的 actions、events 和 recommendations。

* 选择 [puck style](/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/) 并自定义 pucks 的颜色和交互（allocation behavior、snap behavior）。

* Set title and sub-title properties for resource object rows (including icons and function backed properties).
* Select actions, events, and recommendations that appear in right-click menus.
* Choose a [puck style](/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/) and customize colors and interactions (allocation behavior, snap behavior) for pucks.
在下面的示例中，Scheduling Gantt Chart 将 pilots 分配给 flights。

In the example below, the Scheduling Gantt Chart assigns pilots to flights.

> 📷 **[图片: Scheduling Gantt chart 示例：将 pilots 分配给 flights。]**

> 📷 **[图片: Scheduling Gantt chart example: Assigning pilots to flights.]**

## Widget layout
下图提供了 widget 布局的概览。

The image below provides an overview of the widget layout.

> 📷 **[图片: Widget 布局示例。]**

> 📷 **[图片: Sample widget layout.]**

1. **Schedule objects (pucks):** 每个 schedule object 在 Scheduling Gantt Chart 上呈现为一个 puck。用户可以拖放这些 pucks 以更新 object 的 start time、end time 和/或 linked resource object。Pucks 还支持两项附加功能：

* **Schedule object details:** 当光标悬停在 puck 上时显示为卡片。默认情况下，卡片将显示 start/end time、schedule object type 上配置的任何 rules 的状态，以及指向 object view 的 link。Builders 还可以添加他们希望显示的 properties。

* **Right-click menu:** 当用户右键单击 puck 时触发。Builders 可以配置 actions、events 和 recommendations。

2. **Resource object or rows:** 每个 resource object 在 Scheduling Gantt Chart 中呈现为一行。

* **Resource object details:** 当光标悬停在行上时显示为卡片。卡片显示 object title、application builder 选择的 properties 以及指向 object view 的 link。

3. **Search bar:** Scheduling Gantt Chart widget 包含一个 widget 内置的 search bar。当用户输入搜索词时，结果将以黄色边框高亮显示。按下 `Enter` 键将创建一个包含结果的新 search group。

4. **Violation rules filter:** Violation rules filter 用于聚焦 schedule 中需要注意的方面。您可以打开/关闭要在其 schedule 中进行评估的 rules，并筛选出违反所选 rules 的 objects。

5. **User preferences (deprecated):** 用户可以定义并保存其首选设置。可自定义的选项包括：

* **Timezone:** 默认情况下，Foundry 中的所有时间戳均为 UTC。此功能将处理用户选择的时区偏移。

* **Collapse pucks:** Widget 将自动将重叠的 pucks 合并为单个 puck，以节省屏幕空间。此 toggle 允许用户打开和关闭此功能。

* **Show time now line:** 当前时间将以红色垂直线表示。

* **Expand legend:** 确定 legend 默认是展开还是折叠。

* **Expand unscheduled:** 确定 unscheduled drawer 默认是展开还是折叠。

* **Expand all nested pucks:** 确定 nested pucks 默认是展开还是折叠。

* **Scroll to pucks on external selection:** 如果启用，当用户在 widget 外部选择 schedule object 时，timeline 将滚动到所选 object 的位置。

* **Persist row widths:** 用户可以通过拖动行边框来调整 resource object 行的宽度。可以保存宽度首选项，以便在重新加载 application 时宽度不会重置为默认值。

* **Persist row/grouping order:** 用户可以通过拖放手动重新排序 resource object 行。可以保存顺序首选项，以便在重新加载 application 时顺序不会重置为默认值。

6. **Unscheduled drawer:** 如果 schedule objects 同时缺少 start/end time 和 linked resource object，则被视为 unscheduled。如果这些 properties 中的任何一个或全部为 null，则 schedule object pucks 将出现在 unscheduled drawer 中。

7. **Change log:** Change log 跟踪用户对其 schedule 所做的所有编辑。

8. **Review changes:** 使用 scenarios 时将显示此选项。选择它会生成一个弹出窗口，其中汇总了在活动场景中所做的所有 Ontology edits 以及任何剩余的 validation rule violations。确认以执行 Ontology edits。

1. **Schedule objects (pucks):** Each schedule object is rendered as a puck on the Scheduling Gantt Chart. Users can drag and drop these pucks to update the object’s start time, end time, and/or linked resource object. Pucks are backed by two additional capabilities:
* **Schedule object details:** Appear as a card when the cursor hovers over a puck. By default the card will show the start/end time, the status of any rules configured on the schedule object type, and a link to the object view. Builders can also add properties they would like displayed.
* **Right-click menu:** Triggered when a user right-clicks on a puck. Builders can configure actions, events, and recommendations.
2. **Resource object or rows:** Each resource object is rendered as a row in the Scheduling Gantt Chart.
* **Resource object details:** Appear as a card when the cursor hovers over a row. Cards display the object title, properties selected by the application builder and a link to the object view.
3. **Search bar:** The Scheduling Gantt Chart widget includes an in-widget search bar. Results will be highlighted with a yellow border as users enter search terms. Pressing the `Enter` key will create a new search group with the results.
4. **Violation rules filter:** The violation rules filter is used to focus on aspects of the schedule that need attention. You can toggle on/off the rules to be evaluated for their schedule and filter down to objects that are violating selected rules.
5. **User preferences (deprecated):** Users can define and save their preferred setup. Customizable options include:
* **Timezone:** By default, all timestamps in Foundry are in UTC. This feature will handle the timezone offset for user selections.
* **Collapse pucks:** The widget will automatically consolidate overlapping pucks into a single puck to preserve screen real-estate. This toggle allows users to turn this feature on and off.
* **Show time now line:** Current time will be represented by a red vertical line.
* **Expand legend:** Determine if the legend is to be expanded or collapsed by default.
* **Expand unscheduled:** Determine if the unscheduled drawer is to expanded or collapsed by default.
* **Expand all nested pucks:** Determine if nested pucks are to be expanded or collapsed by default.
* **Scroll to pucks on external selection:** If enabled, when users select a schedule object outside of the widget, the timeline will scroll to the location of the selected object.
* **Persist row widths:** Users are able to resize the width of resource object rows by dragging the row border. The width preference may be saved so that width does not reset to default when the application is reloaded.
* **Persist row/grouping order:** Users are able to manually reorder resource object rows by dragging and dropping them. The order preference may be saved so that the order does not reset to default when the application is reloaded.
6. **Unscheduled drawer:** Schedule objects are considered unscheduled if they do not have both a start/end time and a linked resource object. If any or all of these properties are null, schedule object pucks will appear in the unscheduled drawer.
7. **Change log:** The change log keeps track of all edits a user has made to their schedule.
8. **Review changes:** This option will be displayed when using scenarios. Selecting it generates a pop-up with a summary of all Ontology edits made in the active scenario and any remaining validation rule violations. Confirm to execute the Ontology edits.
## Widget setup
Scheduling Gantt Chart widget 包含若干必需和可选的 configuration 设置。本节提供概览，required settings 会明确标记。

The Scheduling Gantt Chart widget includes several required and optional configuration settings. This section presents an overview, and the required settings are specifically marked as such.
### Timeline data
* **Start Timestamp \[REQUIRED]:** Timeline 的开始时间。

* **End Timestamp \[REQUIRED]:** Timeline 的结束时间。

* **Start Timestamp \[REQUIRED]:** The beginning of the timeline.
* **End Timestamp \[REQUIRED]:** The end of the timeline.
### Timeline configuration
* **Custom Display Range:** 配置用户首次打开 Workshop module 时 timeline 中显示的时间段。除非在其他地方另有指定，否则用户将能够滚动 Scheduling Gantt Chart 的全长。

* **Custom Timeline Grid Precision:** 选择一个时间单位作为 Gantt chart 网格线，将覆盖默认的网格线。

* **Disable timeline zoom and scroll:** 禁用用户使用 timeline 滚动或缩放功能的能力。

* **Operating Hours:** 将 chart 中的范围划分为"Operating/non-operating"。这些区域将以不同颜色阴影显示。您可以配置 daily schedules、custom time ranges 或 weekday-based schedules。可选择启用 **Collapse by default**，以便在 Gantt chart 首次渲染时折叠 non-operating hours。

* **Timeline Date-Time Formatting:** 自定义不同缩放级别下 timeline 的日期和时间格式。您可以为 minute、hour、day、week、month、quarter 和 year milestones 配置格式字符串。如果未提供格式，则将使用默认格式。

* **Custom Display Range:** Configure the time period that is displayed in the timeline when users initially open the Workshop module. Users will be able to scroll the full length of the Scheduling Gantt Chart, unless specified elsewhere.
* **Custom Timeline Grid Precision:** Select a unit of time for Gantt chart grid lines that will override default grid lines.
* **Disable timeline zoom and scroll:** Disable users' ability to use the timeline scroll or zoom features.
* **Operating Hours:** Delineate ranges in the chart as "Operating/non-operating". These regions will be shaded in different colors. You can configure daily schedules, custom time ranges, or weekday-based schedules. Optionally, enable **Collapse by default** to collapse non-operating hours when the Gantt chart initially renders.
* **Timeline Date-Time Formatting:** Customize the date and time formatting for the timeline at different zoom levels. You can configure format strings for minute, hour, day, week, month, quarter, and year milestones. If no format is provided, a default will be used.
### Row data
* **Fixed Resource Object Set \[REQUIRED]:** 在界面中呈现为 Scheduling Gantt Chart widget 的行。Set 中的每个 object 将对应一行。

* **Fixed Resource Object Set \[REQUIRED]:** Rendered in the interface as the rows of the Scheduling Gantt Chart widget. Each object within the set will correspond to one row.
### Row configuration
* **Title Icon（标题图标）：** 选择一个图标，显示在每行标题 Property 旁边。

* **Row Title（行标题）：** 选择一个 Property 来覆盖默认的行标题。还可以切换当 Property 值为 null 时是否显示行标题。

* **Sub-Titles（副标题）：** 选择 resource object set 中一个或多个将显示在 object 标题下方的 Property。此外，为每个副标题选择一个图标，如下图所示。

> 📷 **[图片: 配置了副标题的 Scheduling Gantt Chart widget。]**

* **Group-By Property（分组 Property）：** 选择一个 fixed resource object set 的 Property，用于将 fixed resource（行）划分为子组。定义的组可以通过图表中的开关进行打开或关闭。在下面的示例中，resource 已被划分为 "Garden City"、"Garza" 和 "Hoople" 组。

> 📷 **[图片: Scheduling Gantt Chart widget 分组配置。]**

> 📷 **[图片: Scheduling Gantt Chart widget 分组配置。]**

* **Default Sorts（默认排序）：** 允许对图表中行的顺序应用一个或多个默认排序。

* **Right Click Menu（右键菜单）：** 有关更多信息，请参阅 [在行上触发 actions 和 events](/docs/foundry/dynamic-scheduling/scheduling-row-level-triggering-actions-and-events/)。

* **Action configuration（Action 配置）：** 配置与 resource object type 相关的 Action。这些 Action 可以是标准的 Ontology create、modify 或 delete Action，也可以是自定义的 [FoO-backed action](/docs/foundry/functions/functions-on-objects/)。

* **Search function（搜索 Function）：** 配置行级推荐 Function。当用户在图表中未排定任何内容的某个时间点右键单击时，将启动此 Function。光标的位置对应于特定的时间和 resource object，然后这些信息可用作 Function 的输入。

* **On Row Select Event（行选中事件）：** 配置当图表中的行被选中时触发的 Workshop 事件。例如，触发一个包含更详细 object 视图的 drawer。

* **Popover Actions（弹出框 Action）：** 配置用于替换悬停在行上时出现的默认弹出框的 Action。

* **Title Icon:** Select an icon that appears alongside the title property of each row.
* **Row Title:** Select a property to override the default row title. You can also toggle whether the row title is displayed when the property value is null.
* **Sub-Titles:** Select one or more properties of the resource object set that will appear underneath the object title. Additionally, select an icon for each sub-title, as demonstrated in the image below.

> 📷 **[图片: Scheduling Gantt Chart widget with subtitles configured.]**

* **Group-By Property:** Select a property of a fixed resource object set that divides fixed resources (rows) into subgroups. The defined groups can be opened or closed via a toggle in chart. In the below example, the resources have been divided into the groups "Garden City," "Garza," and "Hoople."

> 📷 **[图片: Scheduling Gantt Chart widget grouping configuration.]**

> 📷 **[图片: Scheduling Gantt Chart widget grouping configuration.]**

* **Default Sorts:** Allow one or more default sorts to be applied to the ordering of rows in the chart.
* **Right Click Menu:** See [triggering actions and events on a row](/docs/foundry/dynamic-scheduling/scheduling-row-level-triggering-actions-and-events/) for more information.
* **Action configuration:** Configure actions related to resource object type. These actions can be standard Ontology create, modify, or delete actions, or a custom [FoO-backed action](/docs/foundry/functions/functions-on-objects/).
* **Search function:** Configure row-level recommendation function. This function is initiated when the user right-clicks a time in the chart where there is nothing scheduled. The placement of cursor corresponds to a specific time and resource object which can then be used as inputs to the function.
* **On Row Select Event:** Configure Workshop events to trigger when a row is selected in the chart. For example, cause a drawer with a more detailed object view to appear.
* **Popover Actions:** Configure actions to replace the default popover that appears when hovering over a row.
### Input data (pucks)
每个 schedule layer 都在 **Input Data (Pucks)** 部分中独立配置。Schedule layer 表示一组在 Gantt 图上显示为 puck 的 `Schedule` 对象。每个 layer 都有其自己的数据、拖放行为、外观、交互和规则子部分。

Each schedule layer is configured independently within the **Input Data (Pucks)** section. A schedule layer represents a set of `Schedule` objects displayed as pucks on the Gantt chart. Each layer has its own sub-sections for data, drag-and-drop behavior, appearance, interactions, and rules.
对于每个 schedule layer，您可以选择一个 [puck 样式](/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/) 来更改视觉表示。有关 puck 样式、着色和 Property 的更多信息，请参阅 [schedule layer (puck) 样式设置](/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/)。

For each schedule layer, you can select a [puck style](/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/) to change the visual representation. See [schedule layer (puck) styling](/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/) for more information on puck styles, coloring, and properties.
#### Data
* **Schedule Object Set \[必填]：** 要在图表中渲染的 `Schedule` 对象。

* **Linked Resource Property \[必填]：** `Schedule` 对象中链接到 `Resource` 对象的 Property。

* **Start Time Property \[必填]：** 用作开始时间的 `Schedule` 对象的 Property。

* **End Time Property \[必填]：** 用作结束时间的 `Schedule` 对象的 Property。

* **Object set filter for unallocated pucks（用于未分配 puck 的对象集过滤器）：** 仅适用于未分配 puck 的可选 object 过滤器。

* **Schedule Object Set \[REQUIRED]:** The `Schedule` objects to be rendered in the chart.
* **Linked Resource Property \[REQUIRED]:** The property from the `Schedule` object that links to the `Resource` object.
* **Start Time Property \[REQUIRED]:** The property from the `Schedule` object to use as the start time.
* **End Time Property \[REQUIRED]:** The property from the `Schedule` object to use as the end time.
* **Object set filter for unallocated pucks:** An optional object filter that only applies to unallocated pucks.
#### Drag & drop
**Drag & Drop** 子部分用于配置如何在图表中移动 puck。有关详细设置说明，请参阅 [拖放文档](/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/)。

The **Drag & Drop** sub-section configures how pucks can be moved within the chart. See the [drag-and-drop documentation](/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/) for detailed setup instructions.
* **Allocation Behavior（分配行为）：** 确定 Scheduling Gantt Chart 中 puck 的放置方式。预定义的选项包括：

* **Allocate（分配）：** 将 puck 拖放到图表中的任何位置。多个 puck 可以在同一时间分配给同一个 resource。

> 📷 **[图片: Puck 行为示例：Allocate。]**

* **Allocate (no overlaps)（分配（不允许重叠））：** 与 **Allocate** 类似，此选项确保相同 object type 的 puck 不重叠。当一个 puck 被拖放到另一个 puck 上时，已存在的 puck 以及在更晚时间段排定的所有内容将自动移动以防止重叠并保持顺序。

> 📷 **[图片: Puck 行为示例：Allocate no overlap。]**

* **Allocate (resource only)（仅分配 resource）：** 此选项启用内置支持，用于 schedule 对象只能移动到不同 resource 的场景。

* **Allocate (time only)（仅分配时间）：** 此选项启用内置支持，用于 schedule 对象只能在时间上移动的场景。

* **Simple swap（简单交换）：** 与 **Allocate (no overlaps)** 类似，只是当一个 puck 被拖放到另一个 puck 上时，两个 puck 会互换位置。

> 📷 **[图片: Puck 行为示例：Swap。]**

* **Swap with downstream（与下游交换）：** 与 **Simple swap** 类似，此选项允许选定的 puck 互换位置。但是，在这种情况下，所有在已交换 puck 之后分配的 puck 也将跟随其各自的前置 puck，从而有效地将整个序列向下游移动。

> 📷 **[图片: Puck 行为示例：Swap with downstream。]**

* **Snap to previous（吸附到前一个）：** Puck 将自动吸附到给定行上最近 puck 的末尾。

> 📷 **[图片: Puck 行为示例：Snap to previous。]**

* **Allocation Behavior:** Determine how the placement of pucks will occur in the Scheduling Gantt Chart. The predefined options include:
* **Allocate:** Drag-and-drop pucks anywhere in the chart. Multiple pucks can be assigned to the same resource at the same time.

> 📷 **[图片: Puck behavior example: Allocate.]**

* **Allocate (no overlaps):** Similar to **Allocate**, this option ensures that pucks of the same object type do not overlap. When a puck is dropped on top of another puck, the existing puck, along with everything scheduled at a later time period, will automatically shift to prevent overlaps and maintain the sequence.

> 📷 **[图片: Puck behavior example: Allocate no overlap.]**

* **Allocate (resource only):** This option enables built-in support for when schedule objects can only be moved to different resources.
* **Allocate (time only):** This option enables built-in support for when schedule objects can only be moved in time.
* **Simple swap:** Similar to **Allocate (no overlaps)** with the exception that when a puck is dropped on top of another puck, the pucks will switch places with one another.

> 📷 **[图片: Puck behavior example: Swap.]**

* **Swap with downstream:** Similar to **Simple swap**, this option allows the selected pucks to switch places. However, in this case, all subsequent pucks assigned after the swapped pucks will also follow their respective predecessors, effectively shifting the entire sequence downstream.

> 📷 **[图片: Puck behavior example: Swap with downstream.]**

* **Snap to previous:** Pucks will automatically snap to the end of the closest existing puck on a given row.

> 📷 **[图片: Puck behavior example: Snap to previous.]**

* **Snap Behavior（吸附行为）：** 默认情况下，用户可以将对象分配到 Scheduling Gantt Chart widget 上的任何时间，精确到具体的分钟。吸附行为允许构建者设置对象可分配时间的定义间隔。一旦 puck 被拖放到图表中的新位置，它将吸附到最近间隔的开始处。

* **Snap Behavior:** By default, users are able to assign objects to any time on the Scheduling Gantt Chart widget, down to the specific minute. Snap behavior allows builders to set defined intervals of when objects can be assigned. Once a puck is dropped to a new placement in the chart, the puck will snap to the beginning of the closest interval.
例如，配置支持医生预约 schedule 的用户可能会确定所有分配（预约）都需要在整点（:00）或半点（:30）开始。

For example, a user configuring a schedule to support doctors' appointments may determine that all assignments (appointments) need to begin on the hour (:00) or half past the hour (:30).
* **Snap Interval Size（吸附间隔大小）** 应该是确定每个间隔持续时间的整数。在下面的示例中，间隔设置为 8 小时。

> 📷 **[图片: 吸附行为示例。]**

* **Start Timestamp（开始时间戳）** 选项指的是吸附间隔开始的时间。默认情况下，吸附间隔从 Scheduling Gantt Chart widget 的开始时间戳开始。配置后，此变量将覆盖默认的开始时间，并将 puck 吸附到所配置的时间位置上。

* The **Snap Interval Size** should be the integer that determines the duration of each interval. In the example below, the interval is set to 8 hours.

> 📷 **[图片: Snap behavior example.]**

* The **Start Timestamp** option refers to the time at which the snap interval begins. By default, snap intervals begin at the start timestamp for the Scheduling Gantt Chart widget. When configured, this variable will override the default start and snap the puck into place at the configured time.
* **Save Handler Action（保存处理 Action）：** 当 puck 被拖放或调整大小时调用的 Action。

* Save handler 必须修改 `Schedule` 对象上的以下参数。每个参数都必须标记为可选。

* Resource ID（指向 resource 对象的外键）

* Start time（开始时间）

* End time（结束时间）

* 配置 save handler Action 时，应提供 widget 提供的参数作为默认值。有关更多信息，请参阅 scheduling [拖放文档](/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/)。

* **Save Handler Action:** The action that is called when a puck is dragged and dropped or resized.
* A save handler must modify the following parameters on the `Schedule` object. Each parameter must be marked as optional.
* Resource ID (the foreign key to the resource object)
* Start time
* End time
* When configuring a save handler action, you should supply widget provided parameters as the defaults. Refer to the scheduling [drag-and-drop documentation](/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/) for more information.
#### Appearance
* **Color Config（颜色配置）：** 选择将用于此 schedule layer 中所有 puck 的颜色。您可以从以下颜色选项中进行选择：

* **Static（静态）：** 选择此项后，所有 puck 将为相同颜色，使用下拉颜色选择器选择。静态着色的 puck 如下图所示。

> 📷 **[图片: 未配置的 puck 格式。]**

* **Segmented by（分段着色）：** Gantt 将循环使用一组默认颜色为图表上的 puck 着色。

* **Conditional coloring（条件着色）：** 配置基于 Property 值确定 puck 颜色的条件着色规则。

* **Puck Title（Puck 标题）：** 选择一个 Property 来覆盖默认的 puck 标题。

* **Puck Properties（Puck Property）：** 选择要直接显示在每个 puck 上的 Property。Property 将按照 widget 配置中的顺序显示在 puck 上。

* **Popover Properties（弹出框 Property）：** 选择悬停在每个 puck 上时显示的 Property。Property 将按照配置中声明的顺序显示。

* **Puck Sort Order（Puck 排序顺序）：** 当 layer 内的 puck 重叠时，对 puck 应用排序。这不适用于背景 puck。

* **Color Config:** Select the colors that will be used for all pucks in this schedule layer. You can choose from the following color options:
* **Static:** When this is selected, all pucks will be the same color, chosen with a dropdown color picker. Statically colored pucks look like the image below.

> 📷 **[图片: Non-configured puck formatting.]**

* **Segmented by:** The Gantt will rotate through a set of default colors to color pucks on the chart.

* **Conditional coloring:** Configure conditional coloring rules that determine puck colors based on property values.
* **Puck Title:** Select a property to override the default puck title.
* **Puck Properties:** Select properties to appear directly on each puck. Properties will appear on the puck in the same order as in the widget configuration.
* **Popover Properties:** Select properties to display when hovering over each puck. Properties will display in the same order as declared in the configuration.
* **Puck Sort Order:** Apply a sort on pucks when they are overlapping within a layer. This does not apply to background pucks.
#### Interactions
* **Custom Suggestions（自定义建议）：** 为您的 schedule 对象选择建议 Function。当用户拿起 puck 时，Function 结果将作为高亮区域渲染在图表上。这可用于指示用户可以或应该放置 puck 的位置。当启用 **Enforce Suggestions（强制建议）** 时，用户只能在高亮区域中放下 puck（按住 Shift 可覆盖）。有关更多信息，请参阅 [建议 Function](/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/)。

* **Drag Cursor to Create Action（拖动光标以创建 Action）：** 启用跨 interface 的拖动 Action，以为可调度 object type 创建新对象。用户通过按住 Shift 并在 widget 内拖动光标来启动 Action。有关更多信息，请参阅 [拖动创建文档](/docs/foundry/dynamic-scheduling/scheduling-drag-to-create/)。

> 📷 **[图片: 拖动光标以创建 Action 示例。]**

* **Right Click Menu（右键菜单）：**

* **Action configuration（Action 配置）：** 配置与 schedule object type 相关的 Action。这些 Action 可以是标准的 Ontology create、modify 或 delete Action，也可以是自定义的 Function-on-Objects-backed Action。

* **Search function（搜索 Function）：** 配置 puck 级推荐 Function。当用户右键单击 puck 时，将启动此 Function。Schedule 对象的开始/结束时间以及对象本身可以用作 Function 的输入。

* **Events（事件）：** 配置可在 widget 内触发的标准 Workshop 事件的组合。

* **Popover Actions（弹出框 Action）：** 配置显示在 puck 弹出框选项卡中的 Action，以替换默认的弹出框视图。

* **Enable Cross Widget Drops（启用跨 Widget 拖放）：** 允许用户将对象从其他 widget 拖到此 schedule layer。启用后，配置一个 drop Action 以确定如何处理拖放的对象。

* **On Puck Select Event（Puck 选中事件）：** 配置当图表中的 puck 被选中时触发的 Workshop 事件。

* **Custom Suggestions:** Select the suggestion function for your schedule object. The function results will be rendered as highlighted areas on the chart when users pick up a puck. This can be used to indicate where users can or should place pucks. When **Enforce Suggestions** is enabled, users can only drop pucks in highlighted regions (hold Shift to override). See [suggestion functions](/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/) for more information.
* **Drag Cursor to Create Action:** Enables a drag action across the interface to create a new object for the schedulable object type. The user initiates action by holding Shift and dragging their cursor within the widget. See the [drag to create documentation](/docs/foundry/dynamic-scheduling/scheduling-drag-to-create/) for more information.

> 📷 **[图片: Drag cursor to create action example.]**

* **Right Click Menu:**
* **Action configuration:** Configure actions related to the schedule object type. These may be standard Ontology create, modify, or delete actions, or a custom Function-on-Objects-backed action.
* **Search function:** Configure puck-level recommendation function. This function is initiated when the user right-clicks a puck. The start/end time of the schedule object and the object itself can then be used as inputs to the function.
* **Events:** Configure combinations of standard Workshop events that can be triggered within the widget.
* **Popover Actions:** Configure actions that appear in tabs on the puck popover, replacing the default popover view.
* **Enable Cross Widget Drops:** Allow users to drag objects from other widgets into this schedule layer. When enabled, configure a drop action that determines how the dropped object is processed.
* **On Puck Select Event:** Configure Workshop events to trigger when a puck is selected in the chart.
#### Rules
应用于 schedule layer 的可选验证规则。有关更多信息，请参阅 [验证规则](/docs/foundry/dynamic-scheduling/scheduling-validation-rules/)。

Optional validation rules to apply to the schedule layer. See [validation rules](/docs/foundry/dynamic-scheduling/scheduling-validation-rules/) for more information.
> **ℹ️ 注意**

> Background 和 Event puck 样式不支持 Rules。
> **ℹ️ 注意**

> Background and Event puck styles do not support Rules.
### Layout
**Layout** 部分组织为四个子部分，用于控制 widget 的视觉呈现。

The **Layout** section is organized into four sub-sections that control the visual presentation of the widget.
#### Timeline
* **Timeline Location（时间轴位置）：** 将时间轴放置在图表的顶部或底部。

* **Display Cursor Time Flag（显示光标时间标记）：** 开启后,会在时间轴上对应光标位置处渲染一条带标记的垂直线。您可以配置该标记的时间显示格式。

> 📷 **[图片: Display cursor time flag in schedule interface example.]**

* **Timezone（时区）：** 配置 widget 中用于显示时间的时区。可以设置为静态值,也可以由 Workshop 变量支持,以允许动态时区选择。

* **Expand Legend（展开图例）：** 确定图例默认是展开还是折叠状态。

* **Timeline Location:** Places the timeline at either the top or bottom of the chart.
* **Display Cursor Time Flag:** When toggled on, a vertical line with a flag will be rendered on the timeline corresponding to the placement of the cursor. You can configure the time display format for the flag.

> 📷 **[图片: Display cursor time flag in schedule interface example.]**

* **Timezone:** Configure the timezone used for displaying times throughout the widget. This can be set to a static value or backed by a Workshop variable to allow dynamic timezone selection.
* **Expand Legend:** Determine if the legend is expanded or collapsed by default.
#### Top bar
* **Hide Header（隐藏头部）：** 隐藏头部,包括搜索栏、validation rule 过滤器以及用户偏好设置。

* **Custom Header Date/Time Formatting（自定义头部日期/时间格式）：** 为头部日期范围显示配置自定义的日期和时间格式字符串。

* **Hide Header:** Hides the header, including the search bar, validation rule filters, and user preferences.
* **Custom Header Date/Time Formatting:** Configure a custom date and time format string for the header date range display.
#### Bottom bar
* **Hide Footer（隐藏底部）：** 隐藏底部,包括未排程抽屉、变更日志和 review 选项。

* **Hide Unscheduled（隐藏未排程）：** 开启后,未排程切换按钮将被隐藏。

* **Expand Unscheduled（展开未排程）：** 开启后,未排程 pucks 抽屉将默认展开。

* **Standard Unallocated Puck Size（标准未分配 Puck 尺寸）：** 默认情况下,puck 的尺寸与时间时长成比例,如下图所示。

> 📷 **[图片: Example: Standard unallocated puck size.]**

当 **Standard Unallocated Puck Size** 开启后,未分配区域中的 puck 尺寸将被标准化,如下图所示。

> 📷 **[图片: Example: Standardized puck size.]**

* **Hide Footer:** Hides the footer, including the unscheduled drawer, change log, and review option.
* **Hide Unscheduled:** When toggled on, the unscheduled toggle button will be hidden.
* **Expand Unscheduled:** When toggled on, the unscheduled pucks drawer will be expanded by default.
* **Standard Unallocated Puck Size:** By default, the size of the puck is proportional to time duration, as in the image below.

> 📷 **[图片: Example: Standard unallocated puck size.]**

When the **Standard Unallocated Puck Size** is toggled on, the puck size is standardized in the unallocated area, as in the image below.

> 📷 **[图片: Example: Standardized puck size.]**

#### Puck display
* **Split Rows by Schedule Layer（按 Schedule Layer 拆分行）：** 每个 schedule layer 在给定的 fixed resource 上包含一个子行。Schedule layer 的顺序和标签在 **Input Data (Pucks)** 设置中确定,并在悬停对象时显示。该设置默认关闭,仅当 application 配置了多个 schedule layers 时适用。

> 📷 **[图片: Example: split rows by schedule layer.]**

* **Expand All Nested Pucks（展开所有嵌套 Pucks）：** 启用后,带有嵌套子项的 pucks 将默认展开。

* **Collapse overlapping pucks（折叠重叠的 Pucks）：** widget 将把重叠的 pucks 合并为一个 puck,以节省屏幕空间。

* **Disable Popovers（禁用 Popovers）：** 开启后,popovers 将被禁用。

* **Split Rows by Schedule Layer:** Each schedule layer contains a sub-row on a given fixed resource. The order of schedule layers and labels are determined in the **Input Data (Pucks)** setting and will appear when hovering over the object. This setting is toggled off by default and is only applicable when the application is configured with multiple schedule layers.

> 📷 **[图片: Example: split rows by schedule layer.]**

* **Expand All Nested Pucks:** When enabled, pucks with nested children will be expanded by default.
* **Collapse overlapping pucks:** The widget will consolidate overlapping pucks into a single puck to preserve screen real estate.
* **Disable Popovers:** When toggled on, popovers are disabled.
### Metrics
**Metrics** 部分允许您提供自定义 functions 来向 Gantt 图表添加 metrics。您可以配置两种类型的 metrics:

The **Metrics** section allows you to supply custom functions to add metrics to the Gantt chart. You can configure two types of metrics:
* **Header Metrics（头部 Metrics）：** 与图表时间轴对齐的 metrics。

* **Row Metrics（行 Metrics）：** 与图表中每一行对齐的 metrics。

* **Header Metrics:** Metrics that are aligned to the time axis of the chart.
* **Row Metrics:** Metrics that are aligned to each row within the chart.
有关更多信息,请参阅 [inline metrics](/docs/foundry/dynamic-scheduling/scheduling-inline-metrics/)。

See [inline metrics](/docs/foundry/dynamic-scheduling/scheduling-inline-metrics/) for more information.
### Output
Scheduling Gantt Chart widget 会生成可被其他 Workshop widgets 使用的 output variables,以增强您的 application。这些 output variables 包括:

The Scheduling Gantt Chart widget generates output variables that can be used by other Workshop widgets to enhance your application. These output variables include:
* **Selected Objects（已选对象）：** widget 中所选对象的 object set。

* **Search Results Output（搜索结果输出）：** 由最近一次搜索/推荐所返回对象的 object set。此输出仅在 function 返回对象时填充。

* **User Preferences (deprecated)（用户偏好设置（已弃用））：** 一个序列化的字符串,可与 module interface 或 state saving 一起使用,以持久化保存的用户偏好设置。

* **Selected Objects:** An object set of objects selected in the widget.
* **Search Results Output:** An object set of the objects returned by the most recent search/recommendation. This output will only populate if the function returns objects.
* **User Preferences (deprecated):** A serialized string that can be used with the module interface or state saving to persist saved user preferences.
### Scenarios
* **Enable Scenarios（启用 Scenarios）：** 开启后,允许指定一个 scenario variable,该变量可在所有其他 scenario-aware workflows 中使用。在 widget 中执行的操作将首先写入 scenario。关闭后,在 widget 中执行的操作将直接写入 Ontology。

* **Disable Scenario（禁用 Scenario）：** 一个 boolean variable,用于控制是否禁用 scenarios。当设置为 true 时,操作将直接写入 Ontology。

* **Enable Scenarios:** When toggled on, allows the specification of a scenario variable that can be used in all other scenario-aware workflows. Actions made in the widget will first be written to the scenario. When toggled off, actions made in the widget will be written directly to the Ontology.
* **Disable Scenario:** A boolean variable that controls whether scenarios are disabled. When set to true, actions are written directly to the Ontology.