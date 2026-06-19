<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/time-series/
---
# Time series
[Time series](/docs/foundry/time-series/time-series-overview/) 是随时间变化的测量值。您可以在 Ontology 中将 time series 值配置为 [time series properties](/docs/foundry/time-series/time-series-setup/)。地图包含一些功能，可帮助您查看和分析与地理空间对象关联的 time series 数据。

[Time series](/docs/foundry/time-series/time-series-overview/) are measured values that change over time. You can configure time series values in the Ontology as [time series properties](/docs/foundry/time-series/time-series-setup/). The map contains features to help you view and analyze time series data that is associated with geospatial objects.
![Time series data in the timeline and selection panel.](/docs/resources/foundry/map/time-series.png)
## Explore related time series
在地图上选择一个具有关联 time series 数据的对象。您可以在选择面板的 **Series** 标签页中查看任何相关的 time series。time series 旁边显示的值反映的是在当前 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) 时该 time series 的值。

Select an object on your map that has associated time series data. You can see any related time series in the **Series** tab of the selection panel. The value shown next to a series reflects the value of the series at the current [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range).
![Series tab of selection panel.](/docs/resources/foundry/map/time-series-tab.png)
您也可以通过右键单击一个对象并选择 **Add series to series view**，将 [time series](/docs/foundry/time-series/time-series-overview/) 显式添加到 series 面板中。此外，您也可以先选择一个对象以渲染 [**Selection** panel](/docs/foundry/map/selection/#selection-panel)，然后再导航到 **Series** 标签页。在 **Series** 标签页中，将鼠标悬停在 series 行上时会出现省略号图标，单击该图标会打开一个包含与该 time series 相关的其他操作的菜单，您可以在其中选择 **Add to series view**。

You can also add a [time series](/docs/foundry/time-series/time-series-overview/) explicitly to the series-panel by right-clicking an object and selecting **Add series to series view**. Additionally, you can select an object to render the [**Selection** panel](/docs/foundry/map/selection/#selection-panel) before navigating to the **Series** tab. From the **Series** tab, select the ellipsis icon that appears when hovering over a series row to open a menu that contains additional actions related to the time series where you can select **Add to series view**.

| 右键单击以添加 time series | 使用 **Selection** 面板添加 time series |
| --- | --- |
| 
> 📷 **[图片: 从右键菜单将 series 添加到 timeline。]**
 | 
> 📷 **[图片: 从选择面板将 series 添加到 timeline。]**
 |

| Right-click to add a time series | Use the **Selection** panel to add a time series |
| --- | --- |
| 
> 📷 **[图片: Adding a series to the timeline from the right-click menu.]**
 | 
> 📷 **[图片: Adding a series to the timeline from the selection panel.]**
 |

当您将 time series 添加到 timeline 后，该 series 随时间变化的可视化将显示在地图底部。您可以使用 [timeline](/docs/foundry/map/timeline/) 来检查该 series，并通过 timeline 图例中的条目访问更多 time series 操作。

When you add a time series to the timeline, a visualization of the series over time will appear at the bottom of the map. You can use the [timeline](/docs/foundry/map/timeline/) to examine the series and access more time series actions from its entry on the timeline legend.
## Use time series for styling
当您地图上的对象具有关联的 time series 数据时，您可以根据关联的 time series 为对象着色。使用此功能可以使您的地图响应当前的 [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range)，并帮助您了解数据如何随时间变化。有关使用 time series 进行 [value-based styling](/docs/foundry/map/visualize-objects/#value-based-styling) 的更多信息，请参阅相关文档。

When objects on your map have associated time series data, you can color the objects by an associated time series. Use this to make your map responsive to the current [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range) and help you understand how your data is changing over time. Read more about using time series for [value-based styling](/docs/foundry/map/visualize-objects/#value-based-styling).
## Interact with time series in the timeline \[Beta]
> **ℹ️ 注意: Beta**

> 与 Map timeline 中的 time series 进行交互的功能处于开发的 [beta](/docs/foundry/platform-overview/development-life-cycle/) 阶段，可能在您的注册中不可用。在积极开发过程中，功能可能会发生变化。请联系 Palantir Support 以请求访问此功能。
> **ℹ️ 注意: Beta**

> Interacting with a time series in the Map timeline is in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development. Contact Palantir Support to request access to this feature.
您可以通过两种方式将 time series 添加到地图的 timeline 中：

You can add a time series to your map's timeline in two ways:
* **右键单击菜单：** 在地图上右键单击一个对象，选择 **Add series to the timeline**，然后从菜单中选择一个 series。

* **Selection 面板：** 在地图上选择一个对象，[打开 **Selection** 面板](/docs/foundry/map/selection/#selection-panel)，然后导航到 **Series** 标签页。接下来，将鼠标悬停在 series 行上时出现的 **…**，打开包含与所选 time series 相关的其他操作的菜单，然后选择 **Add to timeline**。

* **Right-click menu:** Right-click an object on your map and select **Add series to the timeline** before choosing a series from the menu.
* **Selection panel:** Select an object on your map, [open the **Selection** panel](/docs/foundry/map/selection/#selection-panel), and navigate to the **Series** tab. Next, select the **…** that appears when hovering over a series row to open a menu that contains additional actions related to the selected time series before choosing **Add to timeline**.
将 time series 添加到 timeline 后，您可以通过 timeline 图例配置其渲染样式，并可选择性地切换其可见性。

Once you add a time series to the timeline, you can configure its rendered styles and optionally toggle its visibility using the timeline legend.