<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/graphs-explore/
---
# Explore existing graphs
## Object exploration
如果您在图中选择了一个感兴趣的对象，您将在侧边栏的 **Selection** 选项卡中看到其属性。

If you select an object of interest on the graph, you will see its properties in the **Selection** tab of the sidebar.
对象还可以在节点标签中显示关键信息或指标。下面的示例显示了航班的出发和到达时间。

Objects may also have key information or metrics shown in the node labels. The example below shows the departure and arrival times of the flights.
![Object Exploration](/docs/resources/foundry/vertex/explore-existing-1.jpg)
## Associated events
如果一个对象具有关联的事件，该事件可以配置为以 *徽章* 的形式显示在受影响的对象上。如果您点击一个具有相关事件的对象节点，您可以在 **object selection** 侧边栏的 **Events** 选项卡中查看详细信息。

If an object has an associated event, the event can be configured to show as a *badge* against the impacted object. If you click on an object node with related events, you can see the details in the **Events** tab of the **object selection** sidebar.
![Events](/docs/resources/foundry/vertex/explore-existing-2.jpg)
### Understand current state and changes over time
对象可以按对象类型（Object Type）、属性值（Property value）、时间序列（time series）或事件进行样式设置。在下面的示例中，应用了以下样式：

Objects can be styled by object type, property value, time series, or events. In the example below, the following styling is applied:
* Airport 对象被着色为深蓝色

* 航班被着色为浅蓝色，如果 `Cancelled Status` 为 `True` 则显示为红色

* Flight Delay 事件被着色为红色

* Flight Delay 事件在 **Flight object** 节点上显示为红色徽章

* Airport objects are colored dark blue
* Flights are colored light blue, and will show red if the `Cancelled Status` is `True`.
* Flight Delay events are colored red
* Flight Delay events are shown as a red badge on the **Flight object** node.
使用时间选择面板，您可以通过"滑动"（拖动光标）来动态查看属性如何随时间变化。下方的截图显示，事件徽章仅在事件进行中（即事件的开始和结束时间之间）出现。

Using the time selection panel, you can "scrub" (drag the cursor) through to see, with dynamic styling, how properties change. The screenshot below shows that the event badge only appears when the event is in progress (that is, between the start and end time of the event).
![Changes Over Time](/docs/resources/foundry/vertex/explore-existing-3.jpg)
### Filter and explore object properties
在只读模式下，您可以使用侧边栏中的 **Histogram** 选项卡按对象类型（Object Type）和属性（Property）过滤图视图。

Within read-only mode, you can use the **Histogram** tab in the sidebar to filter the graph view by object type and properties.
![Object Properties](/docs/resources/foundry/vertex/explore-existing-4.jpg)
选择感兴趣的对象后，您可以选择 **Filter to** 或 **Filter out** 将直方图选择应用于图。图画布顶部显示已应用的过滤器；您可以通过点击特定参数旁边的 **x** 符号来移除单个对象过滤器，也可以通过选择 **Clear filters** 来移除所有过滤器。

Once you have selected the objects of interest, you can select **Filter to** or **Filter out** to apply the histogram selections to the graph. The top of the graph canvas displays the applied filters; you can remove individual object filters by clicking on the **x** symbol next to the specific parameter, or you can remove all filters by selecting **Clear filters**.
![Filters](/docs/resources/foundry/vertex/explore-existing-5.jpg)
## Exploring object relationships
对于更具探索性的工作流程，您可能希望与图视图交互以了解更广泛的关系和不同的指标（Metric）。在这些可编辑的对象图视图中，您可以执行完整 Vertex 应用程序中可用的许多操作，包括 Search Arounds、样式设置和布局更改。

For more exploratory workflows, you may want to interact with the graph view to understand wider relationships and different metrics. In these editable views of an object graph, you can take many actions available in the full Vertex application, including Search Arounds, styling, and layout changes.
> **ℹ️ 注意**

> 在 Workshop 模块中对 graph 所做的更改不会更新用于生成该 graph 的底层 template。如果您希望永久更改 Workshop 中的视图，则需要更新底层 template。
> **ℹ️ 注意**

> Changes made to a graph within a Workshop module will not update the underlying template used to generate the graph. If you wish to permanently change a view within Workshop, you will need to update the underlying template.
在 Graph 画布的顶部，您可以看到如下图所示的额外浏览工具栏。

At the top of the Graph canvas, you can see the additional exploration toolbar as shown below.
![Object Relationships](/docs/resources/foundry/vertex/explore-existing-6.jpg)
### Explore relationships
选择一个 object 并右键单击以打开 **Actions** 菜单。此菜单允许您使用 Search Around 来查找相关的 objects 和 events，以向 graph 视图中添加其他节点。

Select an object and right-click to open the **Actions** menu. This menu lets you Search Around to find related objects and events to add additional nodes to the graph view.
![Search Around](/docs/resources/foundry/vertex/explore-existing-7.jpg)
### Object and edge node styling
选择您感兴趣的 object 节点或边后，您可以在侧边栏的 **Layers** 选项卡中更新和更改样式。

Once you have selected an object node or edge of interest, you can update and change the styling in the **Layers** tab of the sidebar.
> **ℹ️ 注意**

> 在 Workshop 模块中对样式所做的更改不会被持久化。但是，您可以在底层 template 中配置多个 *saved styles*。
> **ℹ️ 注意**

> Changes made to styling within a Workshop module are not persisted. You can, however, configure multiple *saved styles* within the underlying template.
![Styling](/docs/resources/foundry/vertex/explore-existing-8.jpg)