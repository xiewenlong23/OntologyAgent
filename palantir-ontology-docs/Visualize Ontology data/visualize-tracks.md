<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-tracks/
---
# Track displays
Maps 包含用于渲染随时间移动的 objects 的 displays。这些 displays 旨在帮助您可视化 objects 移动的路径以及 objects 在地图上移动时出现的模式。

Maps include displays for rendering objects that move over time. These displays are designed to help you visualize the paths that objects take and the patterns that emerge as objects move across the map.
所有 track displays 都具有使用 [time-based opacity styling](/docs/foundry/map/visualize-objects/#opacity-styling) 的能力。除了下面的 track displays 之外,您还可以使用 track geometry source 作为定位 [icons and circles](/docs/foundry/map/visualize-points/) 的方式。[Learn more about configuring tracks in the Ontology.](/docs/foundry/map/integrate-objects/#track-objects)

All track displays have the ability to use [time-based opacity styling](/docs/foundry/map/visualize-objects/#opacity-styling). In addition to the track displays below, you can also use a track geometry source as the way to position [icons and circles](/docs/foundry/map/visualize-points/). [Learn more about configuring tracks in the Ontology.](/docs/foundry/map/integrate-objects/#track-objects)
下面的概念性示例使用 track geometry source 为温哥华市附近移动的 vessel objects 显示 track line、breadcrumbs 以及当前位置的 icon:
![Track displays example showing a track line, breadcrumbs, and icon at the current position for vessel objects moving near the City of Vancouver.](/docs/resources/foundry/map/styling-tracks.png)
The notional example below uses a track geometry source to display a track line, breadcrumbs, and icon at the current position for vessel objects moving near the City of Vancouver:
![Track displays example showing a track line, breadcrumbs, and icon at the current position for vessel objects moving near the City of Vancouver.](/docs/resources/foundry/map/styling-tracks.png)
您还可以在 Control Panel 中配置每个 track 的 time series points 数量,[在 organization-level](/docs/foundry/map/control-panel/#data-loading) 或 [在 settings menu 中 per-map](/docs/foundry/map/settings/#time-series-buckets)。

You can also configure the number of time series points per track in Control Panel [on an organization-level](/docs/foundry/map/control-panel/#data-loading) or [per-map in the settings menu](/docs/foundry/map/settings/#time-series-buckets).
#### Moving geometry interpolation
当使用 tracks 作为 geometry source 时,还有其他选项可用于配置地图如何从 track 解释 point location 以及 [selected time](/docs/foundry/map/time-overview/#adjust-the-selected-time-time-range-and-filtered-time-window)。

When using tracks as a geometry source, there are additional options you can use to configure how the map interprets the point location from the track and the [selected time](/docs/foundry/map/time-overview/#adjust-the-selected-time-time-range-and-filtered-time-window).
* **Interpolation mode**
* **Linear:** 在 track 中的已知点之间平滑插值。

* **Last known:** 在 selected time 之前,将 object 显示在最后记录的位置。

* **Max time gap:** 当两个连续的 track points 之间的时间差大于配置的值时,该 track 在该时间段被视为没有数据。

* **Interpolation mode**
* **Linear:** Smoothly interpolate between known points in the track.
* **Last known:** Show the object at the last recorded position before the selected time.
* **Max time gap:** When two consecutive track points have a time difference greater than the value configured, the track is considered as having no data for that time period.
## Track lines
Track lines 通过将相邻的记录位置用线连接起来，可视化 objects 所经过的路径。如果两个点之间的时间差大于配置的 **Max time gap**，则不会在这两个点之间绘制线段。除此之外，track lines 的样式选项与 [lines](/docs/foundry/map/visualize-polygons-lines/) 相同。

Track lines visualize the paths that objects take by connecting adjacent recorded positions with a line. If two points have a time difference greater than the configured **Max time gap**, the line will not be drawn between those points. Otherwise, track lines have the same styling options as [lines](/docs/foundry/map/visualize-polygons-lines/).
## Track breadcrumbs
Track breadcrumbs 是一种仅可视化 object 精确记录位置的方式。每个 object 的 track 都被渲染为一系列小圆圈（即 breadcrumbs），用于显示 object 在不同时间点的位置。除此之外，breadcrumbs 的样式选项与 [circles](/docs/foundry/map/visualize-points/#circle-configuration) 相同。

Track breadcrumbs are a way to visualize only the exact recorded positions of an object. Each object's track is rendered as a series of small circles, or breadcrumbs, that show the object's location at different times. Otherwise, breadcrumbs have the same styling options as [circles](/docs/foundry/map/visualize-points/#circle-configuration).
Track breadcrumbs 同样会显示在 timeline 中，以便您查看 object 位置被记录的确切时间。本示例可视化了某卫星的地面轨迹（ground trace），并根据卫星在每个点的纬度（latitude）来为线条和 breadcrumbs 着色。Timeline 中的 breadcrumbs 也会反映该颜色样式配置。

Track breadcrumbs also display in the timeline to allow you to see the exact time at which object positions were recorded. This example visualizes a satellite's ground trace, and colors the line and breadcrumbs by the latitude of the satellite at every point. The breadcrumbs in the timeline also reflect that color style configuration.
未在地图视口（map viewport）中可见的 breadcrumbs 会被淡化显示，以帮助您理解 object 随时间变化的路径以及 object 在哪些时间范围内会在地图上可见。

Breadcrumbs that are not visible in the map viewport are faded out to help you to understand the object path over time and at what time ranges the object will be visible on the map.
![Track breadcrumbs example allowing a user to see the exact time at which object positions were recorded.](/docs/resources/foundry/map/styling-track-breadcrumbs.png)
> **ℹ️ 注意**

> 如果当前 [time range](/docs/foundry/map/time-overview/#adjust-the-selected-time-time-range-and-filtered-time-window) 内没有 breadcrumbs，则它们不会出现在地图或 timeline 中。
> **ℹ️ 注意**

> If there are no breadcrumbs in the current [time range](/docs/foundry/map/time-overview/#adjust-the-selected-time-time-range-and-filtered-time-window), they will not appear on the map or timeline.
添加 track breadcrumbs 后，您可以从其 timeline legend 条目访问 geometry 的其他配置操作。

Once you add track breadcrumbs, you can access the geometry's additional configuration actions from the its entry in the timeline legend.
### Styling
要使新的 track breadcrumb geometry 图层出现在 timeline 上，请从 **Layers** 面板添加一个 breadcrumb geometry。

To make a new track breadcrumb geometry layer appear on the timeline, add a breadcrumb geometry from the **Layers** panel.
![The timeline geometry to edit how the Flights object appears on a timeline.](/docs/resources/foundry/map/track-breadcrumb_add-geometry.png)
添加 track breadcrumbs geometry 后，样式菜单中会出现 **Track breadcrumbs** 区块。您可以更改在地图上绘制所选路径时所使用的 properties。

Once the track breadcrumbs geometry is added, a **Track breadcrumbs** section will appear in the style menu. You can change the properties used when drawing the selected path on the map.
在 **Track breadcrumb** geometry 中选择 **Color** 菜单，以配置 timeline 上形状颜色的呈现方式。

Select the **Color** menu in the **Track breadcrumb** geometry to configure how shape colors are represented on your timeline.
您还可以通过在 **Color by** 下拉菜单中更改所选项，使用 properties 和 measures 来配置 track breadcrumbs 的颜色样式。例如，下图配置为使用 `Latitude` property 并采用彩虹色谱进行着色：

You can also use properties and measures to configure track breadcrumbs color styling by changing the selected option in the **Color by** dropdown menu. For example, the image below is configured to color by the `Latitude` property with a rainbow color spectrum:
![Track breadcrumbs example showing the coloring of track breadcrumbs by the 'Latitude' property.](/docs/resources/foundry/map/timeline_track-breadcrumbs.png)