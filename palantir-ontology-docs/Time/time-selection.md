<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/time-selection/
---
# Time selection
> **⚠️ 警告: Deprecated functionality**

> 地图的 **Time selection** 面板已被弃用，本文档将在未来的版本中删除。该面板的功能现已移至 [timeline](/docs/foundry/map/time-overview/#selected-time-and-time-range)。
> **⚠️ 警告: Deprecated functionality**

> Map's **Time selection** panel has been deprecated, and this documentation will be removed in a future release. The panel's functionality now resides in the [timeline.](/docs/foundry/map/time-overview/#selected-time-and-time-range)
使用 **Time selection** 面板，您可以调整当前选定的时间和 time window。通过滚动 time window，您可以了解数据如何随时间变化。

Using the **Time selection** panel, you can adjust the currently selected time and time window. By scrolling through the time window, you can understand how your data changes over time.
## Change the selected time
使用 time selector 调整您的地图，以在感兴趣的时间点可视化数据。

Adjust your map to visualize data at a time of interest by using the time selector.
> **ℹ️ 注意**

> time selector 仅允许选择在当前 time window 内的时间。
> **ℹ️ 注意**

> The time selector only allows selecting a time that lies within the current time window.
![Time selector](/docs/resources/foundry/map/time-selection-selector.png)
您也可以使用滑块在时间窗口内滚动：

You can also use the slider to scroll through your time window:
![Time slider](/docs/resources/foundry/map/time-selection-slider.png)
### View the latest data
单击 **View latest** 将选定时间设置为当前时间。在 **Latest Data** 视图下，选定时间将自动更新以匹配当前时间。将最新数据模式与 [streaming data](/docs/foundry/building-pipelines/pipeline-types/#streaming) 结合使用，可以实时可视化地图上更新的数据。

Click **View latest** to set the selected time to the current time. When on the **Latest Data** view, the selected time will automatically update to match the current time. Use latest data mode in combination with [streaming data](/docs/foundry/building-pipelines/pipeline-types/#streaming) to visualize data on your map that updates in real time.
## Change the time window
使用时间滑块下方的日期范围选择器调整时间窗口：

Adjust the time window using the date range selector under the time slider:
![Time window](/docs/resources/foundry/map/time-selection-window.png)