<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/timeline/
---
# Timeline
您可以使用 timeline 来查看基于时间的数据，以及配置时间窗口和 [selected time](/docs/foundry/map/time-overview/#adjust-the-selected-time-time-range-and-filtered-time-window)。您可以设置 [selected time 和 time range](/docs/foundry/map/time-overview/#selected-time-and-time-range)，进一步检查 object 的基于时间的属性，并筛选特定时间范围内的特定 object。

You can use the timeline to view time-based data as well as configure the time window and [selected time](/docs/foundry/map/time-overview/#adjust-the-selected-time-time-range-and-filtered-time-window). You can set the [selected time and time range](/docs/foundry/map/time-overview/#selected-time-and-time-range), further inspect the time-based properties of objects, and filter to specific objects in a given time range.
![A .gif of the maps application that shows the timeline displaying events, track breadcrumbs and series.](/docs/resources/foundry/map/timeline-overview.gif)
Timeline 可用于查看 [events](#events)，例如 [event objects](/docs/foundry/map/events/#event-objects) 和 [timeline geometries](/docs/foundry/map/events/#timeline-geometries)、[track breadcrumbs](#track-breadcrumbs) 以及 [time series](#time-series-beta)。

The timeline can be used to view [events](#events), such as [event objects](/docs/foundry/map/events/#event-objects) and [timeline geometries](/docs/foundry/map/events/#timeline-geometries), [track breadcrumbs](#track-breadcrumbs), and [time series](#time-series-beta).
即使 timeline 未打开，timeline 的 time range 和 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) 也会影响 map 上可见的任何基于时间的数据。

Even when the timeline is not open, the timeline's time range and [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) can affect any time-based data that is visible on the map.
## Basic controls
### Open and enable the timeline
选择 map canvas 左下角的 **Timeline** 以显示或隐藏 timeline。

Select **Timeline** in the lower-left of the map canvas to show or hide the timeline.
![The timeline open button.](/docs/resources/foundry/map/timeline_timeline-button.png)
在 [Workshop](/docs/foundry/workshop/overview/) 中使用 [Map widget](/docs/foundry/workshop/widgets-map/) 嵌入 map 时，您可以配置 timeline 默认为打开状态。

When embedding a map in [Workshop](/docs/foundry/workshop/overview/) using the [Map widget](/docs/foundry/workshop/widgets-map/), you can configure the timeline to open by default.
![The timeline enable button in the Map workshop widget configuration panel.](/docs/resources/foundry/map/timeline_workshop-enable.png)
### Adjust the selected time
Timeline 上的 cursor 位置表示 map 的 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range)。您可以通过以下方式调整 selected time：

The cursor position on the timeline represents the map's [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range). You can adjust the selected time by:
* 在 timeline 上双击或右键单击。

* 将 cursor 拖动到新位置。

* 选择 timeline 头中间的日期或时间戳以呈现日期和时间选择器。

* Double-clicking or right-clicking on the timeline.
* Dragging the cursor to a new position.
* Selecting the date or timestamp in the middle of the timeline header to render a date and time picker.
![The cursor position on the timeline.](/docs/resources/foundry/map/timeline_cursor-pos.gif)
要获得 cursor 的更具体日期，您可以单击 cursor 表单以输入特定的日期和时间。

To get a more specific date for the cursor, you can click the cursor form to input a specific date and time.
![The input in the middle of the timeline header being used to change the cursor position.](/docs/resources/foundry/map/timeline_cursor-edit-map.png)
选择 **View latest** 将 selected time 设置为当前时间。在 **Latest Data** 视图下，selected time 将自动更新以匹配当前时间。结合使用 **Latest Data** 模式和 [streaming data](/docs/foundry/building-pipelines/pipeline-types/#streaming) 来可视化 map 上实时更新的数据。

Select **View latest** to set the selected time to the current time. When on the **Latest Data** view, the selected time will automatically update to match the current time. Use **Latest Data** mode in combination with [streaming data](/docs/foundry/building-pipelines/pipeline-types/#streaming) to visualize data on your map that updates in real time.
> **ℹ️ 注意**

> 使用日期和时间选择器时，您只能选择位于 object layer 当前时间范围内的时间。
> **ℹ️ 注意**

> When using the date and time selector, you can only select a time that lies within your object layer's current time range.
您可以在 [Control Panel](/docs/foundry/map/control-panel/) 中为所有地图的 **View latest** 模式配置默认时间选择和轮询间隔。此外，您还可以在 [settings panel](/docs/foundry/map/settings/#polling-interval) 中配置每个地图的轮询间隔、时区和时间格式。

You can [configure the default time selection and polling interval when in **View latest** mode for time series for all maps in Control Panel](/docs/foundry/map/control-panel/). Additionally, you can configure [per-map polling interval, time zone, and time format in the settings panel](/docs/foundry/map/settings/#polling-interval).
### Adjust the time range
您可以在 timeline 右上角的 header 中查看 [time range](/docs/foundry/map/time-overview/#selected-time-and-time-range)，也可以从 timeline 视图的开始和结束时间查看。您可以按照以下指南使用鼠标或触控板调整时间范围。

You can view the [time range](/docs/foundry/map/time-overview/#selected-time-and-time-range) in the top right header of the timeline as well as from the start and end time of the timeline's view. You can adjust the time range with a mouse or trackpad by following the guidelines below.
滚动控件：

Scroll controls:
* 使用鼠标的滚轮在 timeline 上放大或缩小，在滚动前按 `Cmd`（macOS）/`Ctrl`（Windows）可平移时间范围。

* 使用触控板通过垂直滑动或捏合来放大或缩小 timeline。

* Use your mouse's scroll wheel to zoom in our out on the timeline, and press `Cmd` (macOS)/`Ctrl` (Windows) before scrolling to pan the time range.
* Use your trackpad to zoom in our out on the timeline by vertically swiping or pinching in or out.
在 timeline header 右上角的 ribbon 中选择 **Time range**，以为 timeline 输入特定的日期和时间范围。

Select **Time range** in the top right ribbon of the timeline header to input a specific date and time range for the timeline.
![The input in the right of the timeline header being used to change the time window.](/docs/resources/foundry/map/timeline_time-window.png)
要根据 timeline 中的数据获取自动时间窗口，请选择由双向箭头标记的 **Zoom to fit** 按钮。

To get an automatic time window based on the data in the timeline, select the **Zoom to fit** button, marked by bidirectional arrows.
![The zoom-to-fit button on the right header of the timeline.](/docs/resources/foundry/map/timeline_zoom-to-fit.png)
### Filter the time window
您可以通过以下方式筛选地图上的事件：

You can filter events on a map by:
* 按住 `Shift`，在 timeline 中选择一个点，然后在 timeline 上拖动光标以创建时间筛选窗口。

* 使用 timeline 控制栏中的 **Time filter** 按钮。

* Holding `Shift`, selecting a point in the timeline, and dragging your cursor on the timeline to create a time filter window.
* Using the **Time filter** button in the control bar of the timeline.
![The time window filter on the timeline.](/docs/resources/foundry/map/timeline_map-filter-close.png)
**Time filter** 也可在地图 canvas 的顶部使用。地图上符合筛选条件的 objects 完全显示，而不匹配时间筛选条件的 objects 则会淡出。

The **Time filter** is also available at the top of your map canvas. Objects on the map that match the filter are fully opaque, while objects that do not match the time filter are faded out.
![The time filter shown at the top of the maps application.](/docs/resources/foundry/map/timeline_map-filter.png)
### Timeline playback
您可以使用播放按钮（⏵）自动移动时间光标；播放速度可以通过速度预设（1x、2x、5x、10x、100x 等）进行调整。

You can use the play button (⏵) to move the time cursor automatically; playback speed can be adjusted with the speed presets (1x, 2x, 5x, 10x, 100x, and so on).
![The timeline playback controls showing the speed presets and the play/pause button.](/docs/resources/foundry/map/timeline_playback_controls.png)
光标将自动循环遍历 timeline 上的时间窗口或时间筛选条件（如果存在）。

The cursor will loop automatically through the time window on the timeline or a time filter if it exists.
![The timeline filter showing that the time cursor stays within that range when using the playback controls.](/docs/resources/foundry/map/timeline_playback_with_filter.png)
### Expand the timeline
当 timeline 折叠时，添加到 timeline 的数据不可见。但是，您仍然可以更改时间范围、筛选时间窗口和 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range)。

When the timeline is collapsed, data added to the timeline is not visible. However, you can still change the time range, filtered time window, and [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range).
要将每个 object type 显示在各自的 timeline 行上，请选择 timeline 控制栏中的 **Expand**（![Double chevron icon pointing upward button.](/docs/resources/foundry/map/double-chevron.png)）。

To show each object type on its own timeline row, select the **Expand** (![Double chevron icon pointing upward button.](/docs/resources/foundry/map/double-chevron.png)) in the control bar of the timeline.
## Add data to the timeline
添加到 timeline 的所有数据均按 object type 进行分组。

All data added to the timeline is grouped by object type.
### Events
#### Event objects
[Event objects](/docs/foundry/map/events/#event-objects) 将自动在时间轴上添加一个 event layer。

[Event objects](/docs/foundry/map/events/#event-objects) will automatically add an event layer to the timeline.
![Event object example where a user can see the time properties of the event object 'Earthquakes' on the timeline, noting there is no additional timeline geometry.](/docs/resources/foundry/map/events-object.png)
#### Timeline geometries
若要使新的 timeline event geometry layer 出现在时间轴上，请从 **Layers** 面板中添加一个 [timeline geometry](/docs/foundry/map/visualize-timeline/)。[详细了解如何对 timeline geometries 应用自定义样式。](/docs/foundry/map/visualize-timeline/#styling)

To make a new timeline event geometry layer appear on the timeline, add a [timeline geometry](/docs/foundry/map/visualize-timeline/) from the **Layers** panel. [Learn more about applying custom styling to timeline geometries.](/docs/foundry/map/visualize-timeline/#styling)
![The timeline geometry to edit how the Flights object appears on a timeline.](/docs/resources/foundry/map/timeline_add-geometry.png)
### Track breadcrumbs
具有 breadcrumb geometry 的 tracks 也会根据 [time range](#adjust-the-time-range) 和地图视口在时间轴上进行渲染。

Tracks with a breadcrumb geometry also render on the timeline depending on the [time range](#adjust-the-time-range) and the map viewport.
您可以通过将所选时间移动到其他点来对对象在其 track 上的路径进行动画展示。

You can animate the paths of objects on their track by moving the selected time to other points.
若要使新的 track breadcrumbs layer 在时间轴上渲染，请从 **Layers** 面板中添加一个 [track breadcrumbs geometry](/docs/foundry/map/visualize-tracks/#track-breadcrumbs)。

To make a new track breadcrumbs layer render on the timeline, add a [track breadcrumbs geometry](/docs/foundry/map/visualize-tracks/#track-breadcrumbs) from the **Layers** panel.
![Track breadcrumbs example allowing a user to see the exact time at which object positions were recorded.](/docs/resources/foundry/map/timeline_track-breadcrumbs.png)
在时间轴上添加 track breadcrumbs layer 后，您可以从该 layer 在时间轴图例中的条目访问更多 timeline geometry 操作，例如在 **Layers** 面板中进行 [进一步样式设置](/docs/foundry/map/visualize-tracks/#styling)。

Once you add a track breadcrumbs layer on the timeline, you can access more timeline geometry actions from the layer's entry in the timeline legend, such as [further styling](/docs/foundry/map/visualize-tracks/#styling) in the **Layers** panel.
### Time series \[Beta]
请参阅 [time series 文档](/docs/foundry/map/time-series/#interact-with-time-series-in-the-timeline-beta)，了解如何在地图的时间轴中添加和配置 time series。

Review the [time series documentation](/docs/foundry/map/time-series/#interact-with-time-series-in-the-timeline-beta) to learn about adding and configuring a time series in your map's timeline.
## FAQs
### Will time-based data be visible on the map or timeline for large object sets?
如果您添加一个大型（超过 1,000 个对象）object set，则您的地图会通过 [tile-based loading](/docs/foundry/map/objects-loading-methods/) 自动在地图上加载对象。

If you add a large (greater than 1,000 objects) object set, then your map automatically loads objects on your map through [tile-based loading](/docs/foundry/map/objects-loading-methods/).
对于 tile-based loading，[timeline events](#events)、基于时间的样式以及 [filtered time window](#filter-the-time-window) 将不可用。若要解决此问题，请切换到 **Object-based** loading。这也可能需要减少对象数量以提升性能。

For tile-based loading, [timeline events](#events), time-based styling, and [filtered time window](#filter-the-time-window) will not be available. To fix, switch to **Object-based** loading. This also may require reducing the number of objects to enhance performance.
### Why am I unable to see time series styling on my map?
如果来自 time series properties 的样式不可见，这意味着 Map 无法从 temporal property 派生颜色。您应验证 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) 是否包含您的数据。

If styling from time series properties are not visible, this means that Map is unable to derive color from a temporal property. You should verify the [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) contains your data.
### Why am I unable to see time-based opacity on my objects on my map?
选择一个不可见的特定对象，并检查该对象上的 timestamp 或 date property 是否与 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) 匹配。

您只能在 [event object](/docs/foundry/map/events/#use-event-objects-for-styling) 上配置基于时间的对象不透明度。

Select a specific object that is not visible and check if the timestamp or date property on the object matches the [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range).
You can only configure time-based object opacity on an [event object](/docs/foundry/map/events/#use-event-objects-for-styling).
### Why am I unable to see any track breadcrumbs on my map?
具有 breadcrumb geometry 的 tracks 也会根据 [time range](#adjust-the-time-range) 在时间轴上进行渲染。

Tracks with a breadcrumb geometry also render on the timeline depending on the [time range](#adjust-the-time-range).
### Why am I unable to see any time-based data in my timeline?
如果时间轴上没有任何可见内容，请使用 **Zoom to fit** 按钮在时间轴的 **Time range** 中显示地图上的时间事件。

If nothing is visible on the timeline, use the **Zoom to fit** button to show time events on the map in the timeline's **Time range**.
当可见时，时间轴会显示对象 time properties 的线条。

When visible, the timeline displays lines for an object's time properties.
![The timeline with event-lines.](/docs/resources/foundry/map/timeline_event-lines.png)
此外，时间轴会显示对象 properties 中 time ranges 的条形。

Additionally, the timeline displays bars for time ranges in an object's properties.
![The timeline with bar-events.](/docs/resources/foundry/map/timeline_bar-events.png)