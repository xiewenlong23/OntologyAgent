<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-calendar-widget/
---
# Widget configuration
## Widget modes
Scheduling Calendar widget 有两种模式：read-only 和 dynamic。默认情况下，widget 以 read-only 模式开始，该模式旨在查看和分析数据而不进行任何更改。切换到 dynamic 模式使您能够直接在 widget 中添加、编辑或删除 schedule objects。

The Scheduling Calendar widget has two modes: read-only and dynamic. By default, the widget begins on read-only mode, which is designed for viewing and analyzing data without making any changes. Switching to dynamic mode enables you to add, edit, or delete schedule objects directly in the widget.
Dynamic 模式需要对 schedule object type 进行特定的 Ontology 设置。您需要为表示开始时间（`schedules:schedulable-start-time`）和结束时间（`schedules:schedulable-end-time`）的 properties 添加 type classes。您可以通过以下方式完成此操作：

Dynamic mode requires specific Ontology settings on your schedule object type. You will need to add type classes to the properties that represent the start (`schedules:schedulable-start-time`) and end time (`schedules:schedulable-end-time`) for your object. You can do this by:
1. 在 Ontology Manager 中导航到您的 schedule object type。

2. 在 **Properties** 选项卡中，选择需要 type class 的 property。

3. 从右侧的 property 详细信息面板中选择 **Interaction** 选项卡。

4. 向下滚动并选择 **Add new type class**，然后在提供的文本框中输入 type class kind 和 value。

1. Navigate to your schedule object type in Ontology Manager.
2. In the **Properties** tab, select the property that needs a type class.
3. Select the **Interaction** tab from the property details panel on the right.
4. Scroll down and select **Add new type class**, then enter the type class kind and value in the provided text boxes.
## Input data (pucks)
* **Schedule Name:** 层的名称，用于在配置过程中区分不同的层。此值不会显示在 widget 本身中。

* **Schedule Name:** The name of the layer to help differentiate between different layers during configuration. This value is not displayed in the widget itself.
* **Schedule Object Set:** 这是 Scheduling Calendar widget 的 input variable，并确定将显示哪些数据。为此 object set 选择的 object type 必须具有表示开始时间和结束时间的 properties。

* **Schedule Object Set:** This is the input variable to the Scheduling Calendar widget and determines what data will be displayed. The object type selected for this object set must have properties that represent a start time and an end time.
* **Start Time (read-only mode):** 选择一个 date 或 timestamp property 用作事件的开始时间。在 dynamic 模式下，如果已应用正确的 Ontology 设置，widget 将推断此值。

* **Start Time (read-only mode):** Select a date or timestamp property to use as the start time of the events. In dynamic mode, the widget will infer this value if the correct Ontology settings have been applied.
* **End Time (read-only mode):** 选择一个 date 或 timestamp property 用作事件的结束时间。在 dynamic 模式下，如果已应用正确的 Ontology 设置，widget 将推断此值。

* **End Time (read-only mode):** Select a date or timestamp property to use as the end time of the events. In dynamic mode, the widget will infer this value if the correct Ontology settings have been applied.
* **Title:** 选择一个 property 用作 widget 中 object pucks 的显示标签值。

* **Title:** Select a property to use as the displayed label value for the object pucks in the widget.
* **Color（颜色）：** 选择在图表中显示事件时要使用的颜色。

* **Static（静态）：** 为所有 puck 选择单一颜色。

* **Segment-by（按段）：** 选择一个 Property，widget 将根据所选 Property 的值自动为 puck 分配颜色。

* **Dynamic（动态）：** 配置应用于图表中 puck 的条件格式规则。

* **Color:** Select the color(s) to use when displaying events in the chart.
* **Static:** Select a single color for all pucks.
* **Segment-by:** Select a property and the widget will automatically color-code pucks based on the values of the selected property.
* **Dynamic:** Configure conditional formatting rules to apply to pucks in the chart.
* **Pop-over Properties（弹出属性）：** 此部分确定当用户的光标悬停在日历上的 puck 上时，将显示在 popover 卡片上的 Property。

* **Pop-over Properties:** This section determines the properties that will be displayed on the popover card when a user’s cursor hovers over a puck on the calendar.
* **Save Handler Action (Dynamic mode)（保存处理程序 Action - 动态模式）：** 选择将用于拖放交互的 Action。该 Action 应为一个 Modify action，用于编辑 schedule object 的 start 和 end time Property。

* 该 Action 必须具有用于修改 schedule object 的 start time 和 end time 的参数。

* Action 中的参数 ID 必须与您为 start time 和 end time 选择的 Property ID 完全匹配。例如：

* 如果您的 start time Property 是 `start_time`，则 Action 参数 ID 也必须为 `start_time`。

* 如果您的 end time Property 是 `end_time`，则 Action 参数 ID 也必须为 `end_time`。

* Action 参数必须具有与对应 Property 相同的 type class（`schedules:schedulable-start-time` 和 `schedules:schedulable-end-time`）。

* 所有参数应标记为 optional。

* **Save Handler Action (Dynamic mode):** Select an action that will be used for drag-and-drop interactions. This action should be a Modify action that edits the schedule objects start and end time properties.
* The action must have parameters for modifying the start time and end time of the schedule object.
* The parameter IDs in your action must exactly match the property IDs you selected for start and end time. For example:
* If your start time property is `start_time`, the action parameter ID must also be `start_time`.
* If your end time property is `end_time`, the action parameter ID must also be `end_time`.
* The action parameters must have the same type classes (`schedules:schedulable-start-time` and `schedules:schedulable-end-time`) as the corresponding properties.
* All parameters should be marked as optional.
![Configuration of data layer](/docs/resources/foundry/dynamic-scheduling/calendar_data_layer_config.png)
### Display configuration
* **Starting Day of Week（每周起始日）：** 此选择确定当您的图表处于 week 或 month 视图时，哪一天将作为一周的开始。

* **Starting Day of Week:** This selection determines which day will serve as the beginning of the week when your chart is in either week or month view.
* **Interval Size (Dynamic only)（间隔大小 - 仅动态模式）：** 默认情况下，用户可以将 object 分配到 Scheduling Calendar widget 上的任何时间，精确到具体的分钟。Snap behavior 允许 builder 设置可分配 object 的固定间隔。一旦 puck 被拖放到图表中的新位置，它将自动对齐到最近间隔的开始位置。

* **Interval Size (Dynamic only):**  By default, users can assign objects to any time on the Scheduling Calendar widget, down to the specific minute. Snap behavior allows builders to set defined intervals of when objects can be assigned. Once a puck is dropped to a new placement in the chart, the puck will snap to the beginning of the closest interval.
* **Starting Hour（开始小时）：** 此选择确定图表在 day 或 week 视图中的开始时间。

* **Starting Hour:** This selection determines when the chart will begin in day or week view.
* **Ending Hour（结束小时）：** 此选择确定图表在 day 或 week 视图中的结束时间。

* **Ending Hour:** This selection determines when the chart will end in day or week view.
![Display configuration panel](/docs/resources/foundry/dynamic-scheduling/calendar_config.png)
## Common configuration issues
### Error: "The action parameter ids must align with the ids of the selected properties"
当 save handler action 的参数 ID 与 widget 配置中使用的 Property ID 不完全匹配时，会发生此错误。

This error occurs when the save handler action's parameter IDs do not exactly match the property IDs used in the widget configuration.
**原因（Cause）：** 该 widget 要求以下内容之间完全匹配：

**Cause:** The widget requires an exact match between:
* 您的 start time 和 end time Property 的 Property ID

* save handler action 中的参数 ID

* The property IDs of your start and end time properties
* The parameter IDs in your save handler action
**Solution:**
1. 在 Ontology Manager 中检查您的 Property ID：

* 导航到您的 schedule object type。

* 记下确切的 Property ID（例如，`start_time`、`end_time`）。

2. 检查您的 Action 参数 ID：

* 在 Ontology Manager 中打开您的 save handler action。

* 在 Action 的参数配置中，验证参数 ID 是否与您的 Property ID 完全匹配。

* 参数名称可以不同，但 *参数 ID* 必须与 Property ID 相同。

3. 验证 type class 已应用于 Property 和 Action 参数：

* Property 应具有 `schedules:schedulable-start-time` 和 `schedules:schedulable-end-time` type class。

* 对应的 Action 参数应具有相同的 type class。

4. 如有必要，编辑 Action 参数 ID 以匹配您的 Property ID。

1. Check your property IDs in Ontology Manager:
* Navigate to your schedule object type.
* Note the exact property IDs (for example, `start_time`, `end_time`).
2. Check your action parameter IDs:
* Open your save handler action in Ontology Manager.
* In the action's parameter configuration, verify that parameter IDs exactly match your property IDs.
* Parameter names can differ, but the *parameter IDs* must be identical to property IDs.
3. Verify type classes are applied to both properties and action parameters:
* Properties should have `schedules:schedulable-start-time` and `schedules:schedulable-end-time` type classes.
* The corresponding action parameters should have the same type classes.
4. If needed, edit the action parameter IDs to match your property IDs.