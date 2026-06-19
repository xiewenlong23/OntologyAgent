<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/events/
---
# Events
Events 是 [object types](/docs/foundry/object-link-types/object-types-overview/) 或 [timeline geometries](#timeline-geometries)，其中包含关于特定时间点或时间段的时间信息；最常见的是，event object 包含标记时间段开始和结束的 timestamp properties。Event objects 会在 map canvas 上以及屏幕底部的 timeline panel 中作为 timeline geometries 显示为图标，您可以对两者进行样式设置，以帮助用户更好地理解 objects 的 events 与时间的关系。

Events are [object types](/docs/foundry/object-link-types/object-types-overview/) or [timeline geometries](#timeline-geometries) that include temporal information about a specific point or period of time; most commonly this means an event object has timestamp properties that mark the start and end of the time period. Event objects render as icons on the map canvas as well as within the timeline panel at the bottom of the screen as timeline geometries, both of which you can style to help users better understand objects' events in relation to time.
请查看下表，了解 event objects 和 timeline geometries 之间的区别。

Review the table below to learn more about the distinctions between event objects and timeline geometries.

| 功能行为或配置 | Event object | Timeline geometry |
| --- | --- | --- |
| 渲染配置先决条件 | 在 Ontology Manager 中配置，event objects 包含 start 和 end timestamp properties。 | 在地图的 **Layers** 面板中配置，timeline geometries 要求 object 根据其几何形状至少具有一个 timestamp property。任何具有至少一个 timestamp property 的 object 都可以在地图的 timeline 上渲染。 |

| Map canvas 效果 | 用于基于不透明度（opacity）的样式设置。 | 无效果。只会向地图的 timeline 添加 layers。 |

| Map timeline 效果 | Foundry 会自动在地图的 timeline 上显示 event objects。 | 一旦在地图的 **Layers** 面板中配置，Foundry 会将具有 timestamp properties 的 objects 显示为 timeline geometries。Event objects 将覆盖默认的 timeline 样式。 |

| Timeline 样式选项 | 无 timeline 样式选项。Event objects 包含一个显示 object 颜色的条形。 | 提供多种 timeline 样式选项，例如形状和自定义颜色。 |

| 具有多个 timeline layers 时的显示行为 | Event objects 仅显示在 Ontology Manager 中配置的 event time periods。 | 您可以根据 object 上的 timestamp properties，在地图的 **Layers** 面板中配置多个 timeline geometry layers。 |

| Feature behavior or configuration | Event object | Timeline geometry |
| --- | --- | --- |
| Rendering configuration prerequisites | Configured in Ontology Manager, event objects contain start and end timestamp properties. | Configured in a map's **Layers** panel, timeline geometries require an object to have at least one timestamp property depending on the geometry's shape. Any object with at least one timestamp property can render on a map's timeline. |
| Map canvas effects | Used for opacity-based styling. | No effects. Will only add layers to a map's timeline. |
| Map timeline effects | Foundry automatically displays event objects on a map's timeline. | Foundry displays objects with timestamp properties as timeline geometries once configured in the map's **Layers** panel. Event objects will override default timeline styling. |
| Timeline styling options | No timeline styling options. Event objects contain a bar displaying the object's color. | Multiple timeline styling options available, such as those for shape and custom coloring. |
| Display behavior with multiple timeline layers | Event objects only show the event time periods configured in Ontology Manager. | You can configure multiple timeline geometry layers in the **Layers** panel of your map based on the timestamp properties on your object. |

[了解更多有关在 Ontology 中配置 events 的信息。](/docs/foundry/map/integrate-objects/#event-objects)

[Learn more about configuring events in the Ontology.](/docs/foundry/map/integrate-objects/#event-objects)
## Event objects
Event 对象是 [object types](/docs/foundry/object-link-types/object-types-overview/)，其中包含关于特定时间点或时间段的时间信息。最常见的情况是，event 对象具有标记时间段开始和结束的 timestamp properties。[详细了解如何在 Ontology 中配置 events。](/docs/foundry/map/integrate-objects/#event-objects)

Event objects are [object types](/docs/foundry/object-link-types/object-types-overview/) that include temporal information about a specific point or period of time. Most commonly this means an event object has timestamp properties that mark the start and end of the time period. [Learn more about configuring events in the Ontology.](/docs/foundry/map/integrate-objects/#event-objects)
一旦您 [将 event 对象作为图层添加到 map](/docs/foundry/map/add-to-map/)，您就可以应用自定义样式、浏览其链接的 events，并在 [timeline](/docs/foundry/map/timeline/) 中查看 event 时间段。

Once you [add event objects to your map as a layer](/docs/foundry/map/add-to-map/), you can apply custom styles, explore their linked events, and view event time periods in the [timeline](/docs/foundry/map/timeline/).
![Timeline geometry example where a user can see the time properties of the event object 'Earthquakes' on the timeline, noting there is no additional timeline geometry.](/docs/resources/foundry/map/events-object.png)
Event 对象会自动在 timeline 中填充一个 event 图层，并且可以通过添加一个与 event 对象开始和结束时间相同的 timeline geometry 来设置样式。在左侧面板的 **Style** 部分中还有其他可用的显示选项：

Event objects automatically populate an event layer in the timeline and can be styled by adding a timeline geometry with the same start and end time as the event object's start and end time. There are additional display options available in the **Style** section of the left panel:
* **Shape:** 默认情况下使用 start 和 end time property 来绘制条形图。Object type 的 start 和 end time 是在 [Ontology Manager 的 **Capabilities** 选项卡中配置的。](/docs/foundry/map/integrate-objects/#event-objects)

* **Color:** 选择 **Color** 以使用 **Fixed color**、**Function**、**Property** 或 **Linked sensor** 为 event 对象的图标着色。

* **Shape:** Uses a start and end time property to draw a bar by default. An object type's start and end time are configured in [Ontology Manager's **Capabilities** tab.](/docs/foundry/map/integrate-objects/#event-objects)
* **Color:** Select **Color** to shade your event object's icons using a **Fixed color**, **Function**, **Property**, or **Linked sensor**.
如果您在 **Layers** 面板中添加了一个 timeline geometry，它将覆盖此 event 图层在 timeline 中的外观。但是，event 的开始和结束时间仍然可以用于在 map 上进行基于不透明度的样式设置。

If you add a timeline geometry in the **Layers** panel, it will override this event layer's appearance in the timeline. However, the event's start and end time can still be used for opacity-based styling on the map.
### Use event objects for styling
您可以对 map 上的 event 对象进行样式设置，使其仅在当前 [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range) 与 event 的时间段重叠时才可见。使用此功能可以使您的 map 随时间变化而响应，并仅显示当前相关的 event 对象。[详细了解如何使用 event 对象进行样式设置。](/docs/foundry/map/visualize-objects/#opacity-styling)

You can style event objects on your map so they are only visible when the current [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range) overlaps with the time period of the event. Use this to make your map responsive over time and show only the event objects that are currently relevant. [Learn more about using event objects for styling.](/docs/foundry/map/visualize-objects/#opacity-styling)
![Styling events by time.](/docs/resources/foundry/map/events-style-by-time.gif)
### Linked events
Linked event 是链接到另一个对象的 event 对象。在 map 上，您可以通过选择该对象并打开 **Events** 选项卡来查看这些 linked events。如果当前选定的时间位于 event 的开始和结束时间之间，则该 event 将出现在 **Active events** 部分中。否则，该 event 被视为非活动状态，可以通过使用 **Show inactive events** 选项来显示。

A linked event is an event object linked to another object. On the map, you can view those linked events by selecting the object and opening the **Events** tab. If the currently selected time lies between the start and end times of an event, the event will appear in the **Active events** section. Otherwise, the event is considered inactive and can be shown by using the **Show inactive events** option.
![The Events tab is displayed.](/docs/resources/foundry/map/events-selection-events-tab.png)
当 linked events 属于 [geospatial object type](/docs/foundry/map/integrate-objects/) 时，点击 **+** 将其添加到您的 map：

When the linked events are of a [geospatial object type](/docs/foundry/map/integrate-objects/) click **+** to add them to your map:
![Add to map button.](/docs/resources/foundry/map/events-add-to-map.png)
每个 event 都有您可以执行的相应 actions：

Each event has corresponding actions you may take:
* 使用 ![Magnifying glass icon.](/docs/resources/foundry/map/events-magnifying-glass.png) 图标将选定的时间窗口设置为与 event 的时间端点匹配。

* 使用 ![Open in button.](/docs/resources/foundry/map/events-open-in.png) 图标在 Object Explorer 中打开该 event。

* Set the selected time window to match the time endpoints of the event with the ![Magnifying glass icon.](/docs/resources/foundry/map/events-magnifying-glass.png) icon.
* Open the event in Object Explorer with the ![Open in button.](/docs/resources/foundry/map/events-open-in.png) icon.
#### Show on series panel \[Planned deprecation]
右键单击一个对象并选择 **Open linked events**，以打开 linked events 并将其添加到 [series panel](/docs/foundry/map/series-panel/)。在重要时间段的背景下分析您的时间序列数据，并调整 time selection，使 map 反映感兴趣的时间。

Right-click on an object and select **Open linked events** to open and add linked events to the [series panel](/docs/foundry/map/series-panel/). Analyze your time series data in the context of important periods of time, and adjust the time selection so the map reflects a time of interest.
![Add events to series panel.](/docs/resources/foundry/map/events-add-to-series-panel.png)
#### Show counts in labels
如果您为某个图层启用标签，则每个对象的标签中还会显示 active events 的计数。将鼠标悬停在 active event 计数上可查看 active events：

If you enable labels for a layer, a count of active events also displays in the label for each object. Hover over the active event count to view the active events:
![View events from label.](/docs/resources/foundry/map/events-view-from-label.png)
## Timeline geometries
Timeline geometry 由 event 对象的成对 timestamp properties 定义，在 map 的 timeline 中呈现为 event 图层，并且可以通过 object property 进行样式设置。与作为 map 图层渲染的 event 对象相比，timeline geometry 提供了额外的自定义样式选项。

Defined by an event object's paired timestamp properties, timeline geometries render as event layers in a map's timeline and can be styled by an object property. Timeline geometries offer additional custom style options when compared to event objects rendered as a map layer.
[详细了解如何在您的 map 上添加和配置 timeline geometry。](/docs/foundry/map/visualize-timeline/)

[Learn more about adding and configuring timeline geometries on your map.](/docs/foundry/map/visualize-timeline/)