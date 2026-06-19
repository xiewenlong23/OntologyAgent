<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-drag-to-create/
---
# Drag to create
使用 drag to create（拖动创建）使最终用户能够按需创建新的 schedule object。Drag to create 允许您使用 "dragged from" 和 "dragged to" 的开始和结束时间戳，在特定行上初始化一个新的 schedule object。

Enable end users to create new schedule objects on demand using drag to create. Drag to create allows you to initialize a new schedule object on a particular row, at a "dragged from" and "dragged to" start and end timestamp.
为了配置 drag to create，您必须提供一个 `Create Action Type`。在拖放 puck 时，widget 将调用此 action。

In order to configure drag to create, you must provide a `Create Action Type`. On drag and drop of a puck, the widget will call this action.
在下面的示例中，我们将把 schedule layer 称为 `Object type A`。

In the example below, we will refer to the schedule layer as `Object type A`.
## Set up drag-to-create behavior
1. 在 Ontology Manager 中，导航到 `Object type A` 并创建一个 `Create Action Type`。此 action type 应具有以下参数：
* 新对象的主键

* `Start Timestamp` property
* `End Timestamp` property
* `foreign key` property
* （可选）添加您希望在对象创建时填写的 properties。

* 最后，action type 应配置为：输入 `Start Timestamp`、`End Timestamp` 和 `foreign key` 即可创建一个具有这些值的 `object type A` 对象。

2. 现在，在 Workshop 中，导航到 **Input Data (Pucks) > \[your schedule layer] > Interactions > Drag Cursor to Create Action**。

3. 在 **Drag to Create Action** 下，选择您配置的 action type。

4. 在您刚刚输入的 action type 下，选择 **Select parameter to configure** 并选择 start timestamp、end timestamp 和 foreign key 参数。您现在应该能在配置中看到列出的这三个参数。接下来，我们将选择 scheduling Gantt 变量来预填这些参数值。

* 对于 **Start Timestamp** 参数，在 **Local Default Value** 下，在弹出框中选择 **SELECTED START TIMESTAMP**，以确保在 drag to create 时，widget 会自动传入您拖动开始的时间戳。

* 对于 **End Timestamp** 参数，在 **Local Default Value** 下，在弹出框中选择 **SELECTED END TIMESTAMP**。这将确保在 drag to create 时，widget 会自动传入您拖动结束的时间戳。

* 对于 **foreign key** 参数，在 **Local Default Value** 下，在弹出框中选择 **RESOURCE ID**，以确保在 drag to create 时，widget 会自动传入您触发 drag to create 的行（资源）。

1. In Ontology Manager, navigate to `Object type A` and create a `Create Action Type`. This action type should have the following parameters:
* The primary key for your new object
* The `Start Timestamp` property
* The `End Timestamp` property
* The `foreign key` property
* Optionally, add properties that you want to be filled out on object creation.
* In the end, the action type should be configured such that inputting a `Start Timestamp`, `End Timestamp`, and `foreign key` will create an object of `object type A` with those values.
2. Now, in Workshop, navigate to **Input Data (Pucks) > \[your schedule layer] > Interactions > Drag Cursor to Create Action**.
3. Under **Drag to Create Action**, select the action type you configured.
4. Under the action type you just inputted, choose **Select parameter to configure** and select the start timestamp, end timestamp, and foreign key parameters. You should now see these three parameters listed in the configuration. We will now select scheduling Gantt variables to pre-fill these parameter values.
* For the **Start Timestamp** parameter, under **Local Default Value**, select **SELECTED START TIMESTAMP** in the popup to ensure that, on drag to create, the widget automatically passes in the timestamp that you have dragged from.
* For the **End Timestamp** parameter, under **Local Default Value**, select **SELECTED END TIMESTAMP** in the popup. This will ensure that, on drag to create, the widget automatically passes in the timestamp that you have dragged to.
* For the **foreign key** parameter, under **Local Default Value**, select **RESOURCE ID** in the popup to ensure that, on drag to create, the widget automatically passes in the row (resource) that you have triggered drag to create on.
## Use
设置完成后，在某一行上从开始时间到结束时间使用 `Shift + Drag`。这将触发一个弹出窗口，显示您的拖动以创建 action 的表单。提交后，将为指定行创建一个新的 schedule object，其中包含从"拖动来源"和"拖动目标" actions 获取的开始和结束时间戳。

Once set up, `Shift + Drag` on a given row from a start and end time. This will trigger a popup of your drag to create action form. Upon submission, a new schedule object will be created for the specified row, incorporating the start and end timestamps from the "dragged from" and "dragged to" actions.

> 📷 **[图片: Setting up Drag to Create.]**

> 📷 **[图片: Setting up Drag to Create.]**

