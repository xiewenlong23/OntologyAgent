<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/time-overview/
---
# Time and temporal data in the map
地图提供了一系列用于可视化和处理随时间变化的数据的功能。Temporal 数据有多种形式，每种形式都可以以不同的方式使用和可视化。

The map has a collection of features for visualizing and working with data that varies over time. There are a variety of forms that temporal data takes, each of which can be used and visualized in different ways.
## Time-based data types available on a map
### Time series
[Time series](/docs/foundry/map/time-series/) 是随时间变化的测量值。您可以在 Ontology 中将 time series 值配置为 [time series properties](/docs/foundry/time-series/time-series-setup/)。使用 time series 在地图上 [style objects](/docs/foundry/map/visualize-objects/#value-based-styling)，并在 [timeline](/docs/foundry/map/time-series/#explore-related-time-series) 中查看它们。

[Time series](/docs/foundry/map/time-series/) are measured values that change over time. You can configure time series values in the Ontology as [time series properties](/docs/foundry/time-series/time-series-setup/). Use time series to [style objects](/docs/foundry/map/visualize-objects/#value-based-styling) on your map, and view them in the [timeline](/docs/foundry/map/time-series/#explore-related-time-series).
![Time series data in the timeline and selection panel.](/docs/resources/foundry/map/time-series.png)
### Events
[Events objects](/docs/foundry/map/events/) 是具有附加 metadata 的 objects，这些 metadata 将 object 与特定时间或时间范围相关联。Event objects 可用于在地图上 [control the opacity of objects](/docs/foundry/map/visualize-objects/#opacity-styling)，并在 [timeline](/docs/foundry/map/visualize-timeline/) 中进行可视化。

[Events objects](/docs/foundry/map/events/) are objects that have additional metadata that associate the object with a specific time or time range. Event objects can be used to [control the opacity of objects](/docs/foundry/map/visualize-objects/#opacity-styling) on your map and visualized in the [timeline](/docs/foundry/map/visualize-timeline/).
![Styling events by time.](/docs/resources/foundry/map/events-style-by-time.gif)
### Tracks
使用 [tracks](/docs/foundry/map/integrate-objects/#track-objects) 来表示具有随时间变化位置的 objects。[track styling options](/docs/foundry/map/visualize-tracks/) 允许您自定义如何可视化 object 随时间变化的位置。

Use [tracks](/docs/foundry/map/integrate-objects/#track-objects) to represent objects that have a position which changes over time. The [track styling options](/docs/foundry/map/visualize-tracks/) let you customize how you visualize the positions of an object over time.
![Track displays example.](/docs/resources/foundry/map/styling-tracks.png)
## Selected time and time range
地图上显示的所有 temporal data 都遵循当前选定的时间和 time range，使您能够查看数据如何随时间变化并检查过去的特定时间。

All temporal data shown on a map respects the current selected time and time range, enabling you to see how your data changes over time and to inspect specific times in the past.
选择 **View latest** 以启动 **Latest Data** 视图，在该视图中选定的时间将自动更新以匹配当前时间。将 **Latest Data** 视图与 [streaming data](/docs/foundry/building-pipelines/pipeline-types/#streaming) 结合使用，以在地图上可视化实时更新的数据。

Select **View latest** to launch the **Latest Data** view, where the selected time will automatically update to match the current time. Use the **Latest Data** view in combination with [streaming data](/docs/foundry/building-pipelines/pipeline-types/#streaming) to visualize data on your map that updates in real time.
您可以在 [timeline](/docs/foundry/map/timeline/) 中查看地图的选定时间和 time range。

You can view the map's selected time and time range in the [timeline](/docs/foundry/map/timeline/).
例如，根据选定的时间，基于时间的 style 颜色会有所不同。

For example, depending on the selected time, the color of time-based styling will vary.
![An example map showing the icon colors of a weather station changing as the selected time is changed in the timeline.](/docs/resources/foundry/map/time_time-selection-changes.gif)
> **ℹ️ 注意**

> 即使未打开 timeline，选定的时间和 time range 也会影响数据在地图上的显示方式。
> **ℹ️ 注意**

> The select time and time range will affect the way data is shown on the map even if the timeline is not open.
## Adjust the selected time, time range, and filtered time window
使用 [timeline](/docs/foundry/map/timeline/) 来调整以下内容：

Use the [timeline](/docs/foundry/map/timeline/) to adjust the:
* [Selected time](/docs/foundry/map/timeline/#adjust-the-selected-time)
* [Time range](/docs/foundry/map/timeline/#adjust-the-time-range)
* [Filtered time window](/docs/foundry/map/timeline/#filter-the-time-window)
* [Selected time](/docs/foundry/map/timeline/#adjust-the-selected-time)
* [Time range](/docs/foundry/map/timeline/#adjust-the-time-range)
* [Filtered time window](/docs/foundry/map/timeline/#filter-the-time-window)