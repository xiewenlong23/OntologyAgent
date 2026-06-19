<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-drag-and-drop/
---
# Drag and drop
scheduling Gantt chart widget 的拖放功能使最终用户能够将"pucks"分配或重新分配到不同的行和/或不同的时间点。拖放是与 widget 中 pucks 交互的主要方式。

The drag-and-drop feature for the scheduling Gantt chart widget enables the end user to assign or re-assign the "pucks" to a different row and/or different point in time. Drag and drop is the primary way to interact with pucks in the widget.
## Set up drag-and-drop behavior
为了配置拖放行为，您必须在 widget configuration options 中提供一个 save action handler。在拖放 puck 时，widget 将调用此 action。下面的步骤将指导您在最常见的 action type 上设置拖放行为：一个修改关联 schedule 对象的开始、结束和所分配行的简单 action。在本示例中，我们将 schedule layer 称为 `Object type A`。

In order to configure the drag-and-drop behavior, you must provide a save action handler in the widget configuration options. On drag and drop of a puck, the widget will call this action. The steps below will guide you through setting up drag-and-drop behavior on the most common action type: a simple action that modifies the start, end, and assigned row of the associated schedule object. In this example, we will refer to the schedule layer as of `Object type A`.
## Set up instructions
1. 在 Ontology Manager 中，导航到 `Object type A` 并创建一个 modify action type。此 action type 应具有以下参数：

* 一个 object，类型为 object type A。

* 该 object reference 的 `Start timestamp` property

* 该 object reference 的 `End timestamp` property

* 该 object reference 的外键 property，对应于该 schedule object 所分配的 `Row ID`。

因此，action type 应配置为：输入 `Start timestamp`、`End timestamp` 和/或更新的外键将调整 object type A 的 object 上的值。

1. In Ontology Manager, navigate to `Object type A` and create a modify action type. This action type should have the following parameters:
* An object, of object type A.
* The `Start timestamp` property of that object reference
* The `End timestamp` property of that object reference
* The foreign key property of that object reference, which corresponds to the `Row ID` that this schedule object is assigned.
As a result, the action type should be configured such that inputting a `Start timestamp`, `End timestamp`, and/or updated foreign key will adjust the values on the object of object type A.
2. 现在，在 Workshop 中，导航到 **Input Data (Pucks) > \[your schedule layer] > Drag & Drop**。

2. Now, in Workshop, navigate to **Input Data (Pucks) > \[your schedule layer] > Drag & Drop**.
3. 在 **Save Handler Action** 下，选择您配置的 action type。

3. Under **Save Handler Action**, select the action type you configured.
4. 在您刚刚输入的 action type 下，选择 **Select parameter to configure** 并选择 object、start timestamp、end timestamp 和 foreign key 参数。您现在应该看到这四个参数列在配置中。现在我们将选择 Scheduling Gantt variables 来预填这些参数值。

1. 对于 `Object` 参数，在 **Local Default Value** 下，在弹出窗口中选择 **SCHEDULE OBJECT**，以确保在拖放时，widget 自动传入您正在拖放的 schedule object。

2. 对于 `Start Timestamp` 参数，在 **Local Default Value** 下，在弹出窗口中选择 **SELECTED START TIMESTAMP**，以确保在拖放时，widget 自动传入您将 schedule object 拖动到的新 start timestamp。

3. 对于 `End Timestamp` 参数，在 **Local Default Value** 下，在弹出窗口中选择 **SELECTED END TIMESTAMP**，以确保在拖放时，widget 自动传入您将 schedule object 拖动到的新 end timestamp。

4. 对于 `foreign key` 参数，在 **Local Default Value** 下，在弹出窗口中选择 **RESOURCE ID**，以确保在拖放时，widget 自动传入您将 schedule object 拖动到的新行（resource）。

4. Under the action type you just inputted, choose **Select parameter to configure** and select the object, start timestamp, end timestamp, and foreign key parameters. You should now see these four parameters listed in the configuration. We will now select Scheduling Gantt variables to pre-fill these parameter values.
1. For the `Object` parameter, under **Local Default Value**, select **SCHEDULE OBJECT** in the popup window to ensure that, on drag and drop, the widget automatically passes in the schedule object you are dragging and dropping.
2. For the `Start Timestamp` parameter, under **Local Default Value**, select **SELECTED START TIMESTAMP** in the popup to ensure that, on drag and drop, the widget automatically passes in the new start timestamp that you have dragged the schedule object to.
3. For the `End Timestamp` parameter, under **Local Default Value**, select **SELECTED END TIMESTAMP** in the popup to ensure that, on drag and drop, the widget automatically passes in the new end timestamp that you have dragged the schedule object to.
4. For the `foreign key` parameter, under **Local Default Value**, select **RESOURCE ID** in the popup to ensure that, on drag and drop, the widget automatically passes in the new row (resource) that you have dragged the schedule object to.
您现在可以将此 schedule layer 中的任何 puck 拖放到新行（resource）和/或新的 start timestamp 和 end timestamp。放下时，此 action type 将以预填的更新参数触发。有关其他自定义设置，请参阅下一节。

You can now drag and drop any puck in this schedule layer to a new row (resource) and/or new start timestamp and end timestamp. On drop, this action type will be triggered with the parameters pre-filled with these updated values. See the next section for additional customizations.

> 📷 **[图片: Setting up Drag and Drop.]**

> 📷 **[图片: Setting up Drag and Drop.]**

## Drag-and-drop behavior customizations
您可以自定义拖放行为，超出上一节中描述的简单配置范围。

You can customize the drag-and-drop behavior beyond the simple configuration described in the previous section.
### Update snap behavior
默认情况下，当配置了拖放功能时，pucks 可以按分钟级别进行拖动。可以使用 snap behavior（吸附行为）来自定义您希望 pucks 拖动的粒度。例如，如果您希望启用拖放 pucks 的功能，使其在视觉上以加减一天的方式移动，而不是以加减一分钟的方式移动。吸附行为同样适用于通过拖动边缘来延长或缩短 puck 的持续时间。要进行设置，请按照以下说明操作：

By default, when drag-and-drop is configured, pucks can be dragged on a minute-by-minute level. Snap behavior can be used to customize the granularity by which you want pucks to be dragged. For example, if you would like to enable the ability to drag and drop pucks such that they visually move plus or minus a day, rather than plus or minus a minute. Snap behavior will also apply when extending or shortening a puck's duration by dragging its edges. To set up, follow the instructions below:
1. 导航到 **Input Data (Pucks) > \[your schedule layer] > Drag & Drop > Snap Behavior**。

2. 为 snap interval size（吸附间隔大小）提供一个数值变量。

3. 选择时间单位。例如，snap interval size 值为 `3`、时间单位为 `Day` 意味着，每当您在此 layer 中拖放 puck 时，它将以 3 天的增量进行移动。

1. Navigate to **Input Data (Pucks) > \[your schedule layer] > Drag & Drop > Snap Behavior**.
2. Provide a numeric variable for snap interval size.
3. Select the unit of time. For example, a value of `3` for snap interval size and `Day` for unit of time would mean that, whenever you drag and drop a puck in this layer, it will move by 3-day increments.

> 📷 **[图片: Setting up Snap Behavior.]**

> 📷 **[图片: Setting up Snap Behavior.]**

### Advanced save handler action type
在拖放时，widget 会使用所提供的参数调用您的 save handler action type。在标准情况下，这是一个直接修改这些属性的简单 action type。但是，只要 widget 能够传入 `Schedule Object`、`Start Timestamp`、`End Timestamp` 和 `Resource ID`，action type 的底层逻辑和结果可以是您想要的任何形式。这意味着，您可以使用一个由 function on object 支持的 action type 来代替简单的编辑操作，例如。您还可以将来自 Workshop 的其他参数或值传递到您的 action type 中。

On drag and drop, the widget calls your save handler action type with the provided parameters. In the standard case, this is a simple action type that modifies these properties directly. However, as long as the widget is able to pass in the `Schedule Object`, `Start Timestamp`, `End Timestamp`, and `Resource ID`, the underlying logic and outcome of the action type can be whatever you want. This means that rather than a simple edit, you could instead have this action type backed by a function on object, for example. You can also pass in additional parameters or values from Workshop into your action type.
在以下场景中，请考虑使用 function-backed action type 来实现拖放功能：

In the following scenarios, consider using a function-backed action type for drag-and-drop usage:
* 您希望编辑 schedule object 并有条件地触发对 ontology 中其他对象的编辑。

* 您希望编辑 schedule object 并在您的 ontology 中创建其他对象。

* 您希望编辑 schedule object 并调用一个 API。

* You want to edit the schedule object and conditionally trigger edits on other objects in your ontology.
* You want to edit the schedule object and create additional objects in your ontology.
* You want to edit the schedule object and call an API.
### Suggestion function
当将 pucks 拖放到另一行和/或时间时，您可能希望为最终用户提供按需推荐。**Custom Suggestions > Suggestion Function** 使您能够定义一个在拖放时触发的 function。该 function —— 根据您的自定义逻辑 —— 可以临时将 Gantt 上的时间段标记为绿色或红色，以指示"良好"或"不良"的放置位置。

When dragging and dropping pucks to another row and/or time, you may want to provide the end user with on-demand recommendations. **Custom Suggestions > Suggestion Function** enables you to define a function that is triggered on drag and drop. This function - by your custom logic - can temporarily color time slots on the Gantt with green or red, to indicate "good" or "bad" drop locations.
查看 [Suggestion functions](/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/) 以获取更多信息。

Review [Suggestion functions](/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/) for more information.

> 📷 **[图片: Setting up snap behavior.]**

> 📷 **[图片: Setting up snap behavior.]**

