<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/getting-started/
---
# Getting started
本指南演示了如何将 **Foundry Training and Resources** 项目中的资源与 Map 应用程序配合使用。在本示例中,我们将对一些航空公司航线数据进行地理空间分析。

This guide demonstrates how to use the Map application with resources from the **Foundry Training and Resources** project. In this example, we will analyze some airline route data geospatially.
## Create a new map
要创建地图,请展开左侧的 Foundry 导航栏,然后在 Apps 部分点击 **View all**。你将在 **Operational Applications** 部分下找到 **Map** 应用程序。

To create a map, expand the left-hand side Foundry navigation bar, then click on **View all** in the Apps section. You will find the **Map** application under the **Operational Applications** section.

> 📷 **[图片: Map application in the Foundry navigation bar]**

> 📷 **[图片: Map application in the Foundry navigation bar]**

## Map application interface overview
当 Map 应用程序加载时,你将看到一张空白地图:

When the Map application loads, you are presented with a blank map:
![Map application](/docs/resources/foundry/map/map-interface-overview.png)
屏幕左侧有以下面板:

On the left side of the screen are the following panels:
* **Layers:** 添加、管理和设置 object 及 overlay layer 的样式;设置 base layer。

* **Find:** 查找 object 和位置;导航到特定的地理空间坐标。

* **Histogram:** 基于 property 和 time series 值分析和筛选 object。

* **Info:** 显示地图的整体摘要。

* **Layers:** Add, manage, and style object and overlay layers; set the base layer.
* **Find:** Find objects and locations; navigate to specific geospatial coordinates.
* **Histogram:** Analyze and filter objects based on property and time series values.
* **Info:** Display an overall summary of the map.
屏幕顶部是一个工具栏,具有以下功能:

At the top of the screen is a toolbar with the following functionality:
* **Select:** 选择地图上的所有项目,反转选择,或选择与绘制形状相交的项目。

* **Search Around:** 探索 object 关系。

* **Draw:** 在地图上绘制和交互形状,包括多边形、圆形、矩形、线条、点。

* **Capture:** 捕获当前地图状态的截图。

* **Measure:** 测量地图上的物理距离。

* **Annotate:** 向地图添加文本或多边形注释。

* **Delete:** 从地图中移除项目。

* **Select:** Select all items on the map, invert selection, or select items intersecting with a drawn shape.
* **Search Around:** Explore object relations.
* **Draw:** Draw and interact with shapes on the map, including polygons, circles, rectangles, lines, points.
* **Capture:** Capture a screenshot of the current map state.
* **Measure:** Measure physical distances on the map.
* **Annotate:** Add text or polygon annotations to the map.
* **Delete:** Remove items from the map.
屏幕右侧有以下面板:

On the right side of the screen are the following panels:
* **Selection:** 分析详细信息并对所选项目执行 actions。

* **Time Selection:** 设置应用于地图和 time series 视图的时间范围和当前时间戳。

* **Selection:** Analyze details and take actions on selected items.
* **Time Selection:** Set the time range and current timestamp to apply to the map and time series views.
屏幕右下角是用于 time series 和 event data 时序分析的 **Series** 面板。

At the bottom right of the screen is the **Series** panel for the temporal analysis of time series and event data.
## Add an object to the map
在本示例中,我们将搜索底特律大都会机场 (DTW) 并将其添加到地图中。

In this example, we will search for the Detroit Metro Airport (DTW) and add it to the map.
首先,点击 **Layers** 面板中的 **Add to Map**:

First, click **Add to Map** in the **Layers** panel:

> 📷 **[图片: Add to Map button]**

> 📷 **[图片: Add to Map button]**

然后,搜索 `DTW` 以找到 Detroit Metro Airport;您可能需要在右侧列表中选择 object type `[Example Data] Airport`。选择 DTW airport 对象并点击 **Add selected**。

Then, search for `DTW` to find Detroit Metro Airport; you may need to select the object type `[Example Data] Airport` in the list on the right. Select the DTW airport object and click **Add selected**.
![Searching for Detroit Metro Airport](/docs/resources/foundry/map/tutorial-add-dialog-dtw-airport.png)
现在您应该会看到地图已放大到 DTW airport;该对象的地理空间数据是一个点,因此该对象由一个表示坐标的地图图钉表示。左侧的 **Layers** 面板现在显示您有一个 `[Example Data] Airports` layer,右侧的 **Selection** 面板显示所选对象的详细信息,如下图所示。

You should now see the map zoomed in on DTW airport; the object's geospatial data is a point, so the object is represented by a map pin indicating the coordinates. The **Layers** panel on the left now shows that you have an `[Example Data] Airports` layer, and the **Selection** panel on the right displays details about the selected object as shown below.
![Map with Detroit Metro Airport](/docs/resources/foundry/map/tutorial-dtw-on-map.png)
尝试在地图上导航:

Try navigating around the map:
* 点击并拖动以平移地图
* 通过以下任一方式放大和缩小:
* 滚动鼠标滚轮
* 点击界面左下角的缩放按钮
* 按键盘上的 **+** 和 **-** 键

* Click and drag to pan the map around
* Zoom in and out by doing any of the following:
* Scrolling the mouse wheel
* Clicking the zoom buttons in the bottom-left corner of the interface
* Pressing the **+** and **-** keys on your keyboard
## Search Around for linked objects
在本例中,我们将针对 Detroit Metro Airport (DTW) 进行探索性分析。首先,通过右键单击地图上的 DTW 对象图标,选择 **Search Around**,然后选择 `[Example Data] Runway`,将 DTW 的跑道添加到地图中。

In this example, we will perform exploratory analysis regarding Detroit Metro Airport (DTW). First, add DTW's runways to the map by right-clicking the DTW object icon on the map, selecting **Search Around**, and then choosing `[Example Data] Runway`.

> 📷 **[图片: Detroit Metro Airport Search Around menu]**

> 📷 **[图片: Detroit Metro Airport Search Around menu]**

然后您应该会看到跑道对象也已添加到地图。这些跑道对象在地图上以线条表示。您可以将鼠标悬停在跑道线条上以查看跑道 ID。您还可以单击跑道以选择它,并在 **Selection** 面板中查看更多详细信息。

You should then see the runway objects added to the map as well. These runway objects are represented by lines on the map. You can hover the mouse over a runway line to see the runway ID. You can also click on a runway to select it and see more details in the **Selection** panel.
![Runways added to the map](/docs/resources/foundry/map/tutorial-added-runways.png)
## Geospatial search
在本例中,我们将查找距 Detroit Metro Airport (DTW) 200 公里以内的其他机场。

In this example, we will find other airports within 200 kilometers of Detroit Metro Airport (DTW).
首先,点击 **Draw** 以调出形状绘制工具:

First, click **Draw** to bring up the shape drawing tool:
![Draw button on toolbar](/docs/resources/foundry/map/toolbar-draw-button.png)
然后,选择 **Circle** 工具:

Then, select the **Circle** tool:

> 📷 **[图片: Circle tool]**

> 📷 **[图片: Circle tool]**

最后,从地图上点击 DTW airport 以选择中心点,输入 "200",然后选择 **km**。

Finally, from the map, click on DTW airport to choose the center point, enter "200", and select **km**.
![200 km radius search](/docs/resources/foundry/map/tutorial-200km-radius-search.png)
这将打开 Object Search 对话框,过滤出与该圆相交的对象。从 **Object Type** 列表中选择 **\[Example Data] Airports**,然后点击 **Add all**。这将向地图添加另外六个机场。

This opens the Object Search dialog, filtered to objects that intersect with that circle. Choose **\[Example Data] Airports** from the **Object Type** list, and click **Add all**. This will add six additional airports to the map.