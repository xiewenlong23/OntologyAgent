<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/timeline/
---
# View and filter events on a timeline
时间线 (Timeline) 可用于检查对象的时间属性，并按给定时间范围内的特定事件进行过滤。

The timeline can be used to inspect the time properties of objects and filter to specific events in a given time range.
![overview-expanded](/docs/resources/foundry/vertex/timeline_overview-expanded.png)
## View time events
界面左下方的 **时间线 (Timeline)** 按钮可用于显示或隐藏时间线。

The **Timeline** button in the lower-left of the interface can be used to show or hide the timeline.
![timeline-button](/docs/resources/foundry/vertex/timeline_timeline-button.png)
如果时间线上没有可见内容，**缩放至合适大小 (Zoom to fit)** 按钮有助于在时间线的 **时间范围 (Time range)** 内显示图上的时间事件。

If nothing is visible on the timeline, the **Zoom to fit** button can be helpful to show time events on the graph in the timeline's **Time range**.
![zoom-to-fit](/docs/resources/foundry/vertex/timeline_zoom-to-fit.png)
当可见时，时间线将显示对象时间属性的线条以及对象属性中时间范围的条形。

When visible, the timeline will show lines for an object's time properties and bars for time ranges in an object's properties.
![event-lines](/docs/resources/foundry/vertex/timeline_event-lines.png)
![bar-events](/docs/resources/foundry/vertex/timeline_bar-events.png)
## Filter time events
可以通过按住 Shift 键并在时间线上左键拖动以创建时间过滤窗口，或使用时间线控制栏中的 **时间过滤 (Time filter)** 按钮来在图上过滤事件。

Events can be filtered on the graph by either holding Shift and left-click dragging on the timeline to create a time filter window, or by using the **Time filter** button in the control bar of the timeline.
**时间过滤 (Time filter)** 也可在应用程序顶部使用。图中与过滤条件匹配的节点完全不透明，而不匹配时间过滤条件的节点则会淡化显示。

The **Time filter** is also available on the top of the application. Nodes on the graph that match the filter are fully opaque, while nodes that do not match the time filter are faded out.
![time-filter](/docs/resources/foundry/vertex/timeline_graph-time-filter.png)
## Change cursor position
可以通过在时间线上双击左键、将光标拖动到新位置，或使用控制栏中间的输入框来更改时间线上的光标位置。

The cursor position on the timeline can be changed by double-left-clicking on the timeline, dragging the cursor to a new position, or by using the input in the middle of the control bar.
![cursor-pos](/docs/resources/foundry/vertex/timeline_cursor-pos.png)
要为光标获取更具体的日期，您可以单击光标表单以输入特定的日期和时间。

To get a more specific date for the cursor, you can click the cursor form to input a specific date and time.
![cursor-edit](/docs/resources/foundry/vertex/timeline_cursor-edit.png)
## Expand the timeline
若要将每个对象类型 (Object Type) 显示在其自己的时间线行上，请单击时间线控制栏中的"展开"按钮 (![双雪佛龙向上图标](/docs/resources/foundry/vertex/double-chevron.png))。

To show each object type on its own timeline row, click the "expand" button (![double chevron icon pointing upward](/docs/resources/foundry/vertex/double-chevron.png)) in the control bar of the timeline.
![by-object-type](/docs/resources/foundry/vertex/timeline_by-object-type.png)
## Style the timeline
若要更改对象在时间线上的显示方式，请在屏幕左侧的 **图层 (Layers)** 面板中选择对象节点旁边的画笔图标。然后，展开 **时间线形状 (Timeline shape)** 部分。

To change how objects appear on the timeline, select the brush icon next to the object node in the **Layers** panel to the left of your screen. Then, expand the **Timeline shape** section.
![The Timeline shape style configuration section for the F1 Race object node. The shape is set to Bar, and there are options to select a start property and end property](/docs/resources/foundry/vertex/timeline_shape-menu.png)
您可以更改在时间线上绘制所选形状时使用的属性；对于使用两个时间属性的形状，请选择 **起始属性 (Start property)** 和 **结束属性 (End property)** 下拉菜单；对于使用单个属性的形状，请选择 **时间属性 (Time property)**。

You can change the properties used when drawing the selected shape on the timeline; select the **Start property** and **End property** dropdown menus for shapes that use two time properties, or select **Time property** for shapes that use a single property.
![The style configuration section for the F1 Race object node. The shape is set to Diamond, and there is an option to select a time property.](/docs/resources/foundry/vertex/timeline_diamond-select-time-property.png)
在时间线样式配置中选择的形状将出现在时间线中该对象类型的每个实例上。

The shape chosen in the timeline style configuration will appear for every instance of the object type in the timeline.
选择 **时间线颜色 (Timeline Color)** 菜单以配置时间线上形状颜色的表示方式。

Select the **Timeline Color** menu to configure how shape colors are represented on your timeline.
![The timeline color configuration window, currently set to a fixed color.](/docs/resources/foundry/vertex/timeline_color-menu.png)
您还可以使用属性和度量 (measures) 通过更改 **按颜色区分 (Color by)** 下拉菜单中的所选选项来配置时间线 [颜色样式](/docs/foundry/vertex/graphs-display-options/#color-by)。例如，下面的图像配置为使用 `Year` 属性以彩虹色谱进行着色：

You can also use properties and measures to configure timeline [color styling](/docs/foundry/vertex/graphs-display-options/#color-by) by changing the selected option in the **Color by** dropdown menu. For example, the image below is configured to color by the `Year` property with a rainbow color spectrum:
![The timeline color configuration window set to color by a property using a rainbow color spectrum. The objects that appear on the map and timeline use a rainbow of colors based on a linear interpolation.](/docs/resources/foundry/vertex/timeline_color-by-property.png)
## Timeline playback
您可以使用播放按钮 (⏵) 来自动移动时间光标；播放速度可以通过速度预设（1x、2x、5x、10x、100x 等）进行调整。

You can use the play button (⏵) to move the time cursor automatically; playback speed can be adjusted with the speed presets (1x, 2x, 5x, 10x, 100x, and so on).
![The timeline playback controls showing the speed presets and the play/pause button](/docs/resources/foundry/vertex/timeline_playback_controls.png)
光标将在时间线上的时间窗口或时间过滤器（如果存在）中自动循环。

The cursor will loop automatically through the time window on the timeline or a time filter if it exists.
![The timeline filter showing that the time cursor stays within that range when using the playback controls](/docs/resources/foundry/vertex/timeline_playback_with_filter.png)