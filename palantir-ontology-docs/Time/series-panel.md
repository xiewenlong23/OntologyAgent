<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/series-panel/
---
# Series panel \[Planned deprecation]
> **⚠️ 警告: 计划弃用 (Planned deprecation)**

> Map 中的 series panel 处于 [计划弃用 (planned deprecation)](/docs/foundry/platform-overview/development-life-cycle/) 阶段，将于 2026 年 1 月 31 日后不可用。请使用 [timeline](/docs/foundry/map/timeline/#time-series-beta) 来查看基于时间的数据，并在 Map 中进一步检查基于时间的 object properties。
> 如果您对 Map 的 timeline 功能有疑问，或者在迁移工作流程时需要其他帮助，请联系 Palantir Support。
> **⚠️ 警告: Planned deprecation**

> The series panel in Map is in the [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be unavailable after January 31, 2026. Use the [timeline](/docs/foundry/map/timeline/#time-series-beta) to view time-based data and further inspect time-based object properties in Map.
> Contact Palantir Support if you have questions about Map's timeline feature or require additional help migrating your workflows.
您可以使用 map 的 **Series** 面板来进一步检查与 timeline 所选时间和时间窗口同步的 [time series](/docs/foundry/map/time-series/) 和 [linked events](/docs/foundry/map/events/#linked-events)。

You can use a map's **Series** panel to further inspect [time series](/docs/foundry/map/time-series/) and [linked events](/docs/foundry/map/events/#linked-events) synced with the timeline's selected time and time window.
![Series panel.](/docs/resources/foundry/map/time-series-view.png)
## Time series
[Time series](/docs/foundry/time-series/time-series-overview/) 是随时间变化的测量值。

[Time series](/docs/foundry/time-series/time-series-overview/) are measured values that change over time.
您可以使用以下方法将 time series 添加到 series 面板：

You can add a time series to the series panel using the following methods:
* 右键单击一个 object，然后选择 **Add series to series view**，再从 **Add series to series panel** 菜单中选择一个 series。

* 选择一个 object，[打开 **Selection** 面板](/docs/foundry/map/selection/#selection-panel)，然后导航到 **Series** 选项卡。选择将鼠标悬停在 series 行上时出现的 **…** 图标，以打开包含与所选 time series 相关的其他操作的菜单。然后，选择 **Add to series view**。

* Right-click an object and choose **Add series to series view** before selecting a series from the **Add series to series panel** menu.
* Select an object, [open the **Selection** panel](/docs/foundry/map/selection/#selection-panel), and navigate to the **Series** tab. Select the **…** icon that appears when hovering over a series row to open a menu that contains additional actions related to the selected time series. Then, select **Add to series view**.

| 右键单击以添加 time series | 使用 **Selection** 面板添加 time series |
| --- | --- |
| 
> 📷 **[图片: 从右键菜单向 series 面板添加 series。]**
 | 
> 📷 **[图片: 从 selection 面板向 series 面板添加 series。]**
 |

| Right-click to add a time series | Use the **Selection** panel to add a time series |
| --- | --- |
| 
> 📷 **[图片: Adding a series to the series panel from the right-click menu.]**
 | 
> 📷 **[图片: Adding a series to the series panel from the selection panel.]**
 |

当您将 time series 添加到 **Series** 面板时，series 随时间变化的可视化会出现在 map 的底部。您可以使用 **Series** 面板通过选择您希望查看的时间点来在时间中移动。此外，您可以滚动查看已渲染的时间范围。

When you add a time series to the **Series** panel, a visualization of the series over time appears at the bottom of the map. You can use the **Series** panel to move through time by selecting the point in time you wish to view. Additionally, you can scroll across the rendered time range.