<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-timeline/
---
# Timeline geometries
要在 timeline 上可视化图层中所有对象的基于时间的属性,可以配置一个 timeline geometry 以显示在 [timeline](/docs/foundry/map/timeline/) 上。

To visualize time-based properties of all objects in a layer on the timeline, you can configure a timeline geometry to appear on the [timeline](/docs/foundry/map/timeline/).
![Timeline geometry example where a user can see the time properties of the '\[Example\] Airports' object on the timeline.](/docs/resources/foundry/map/styling-timeline-event.png)
Timeline geometries 与 [event objects](/docs/foundry/map/events/#event-objects) 不同,因为您可以为每个 object layer 配置多个 timeline geometries,并应用其他样式选项,例如基于属性的颜色着色。

Timeline geometries differ from [event objects](/docs/foundry/map/events/#event-objects), as you can configure multiple timeline geometries per object layer and apply additional styling options, such as property-based color shading.
添加 timeline geometry 后,您可以从 timeline 图例中该 geometry 的条目访问其其他配置操作。

Once you add a timeline geometry, you can access its additional configuration actions from the geometry's entry in the timeline legend.
## Styling
要使新的 timeline event geometry layer 出现在 timeline 上,请从 **Layers** 面板中添加一个 **Timeline** geometry。

To make a new timeline event geometry layer appear on the timeline, add a **Timeline** geometry from the **Layers** panel.
![The timeline geometry to edit how the Flights object appears on a timeline.](/docs/resources/foundry/map/timeline_add-geometry.png)
添加 timeline geometry 后,样式菜单中会出现一个 **Timeline** 部分,您可以在其中更改在 timeline 上绘制所选形状时使用的属性。对于使用两个时间属性的形状,请选择 **Start property** 和 **End property** 下拉菜单;对于使用单个属性的形状,请选择 **Time property**。

A **Timeline** section appears in the style menu once you add the timeline geometry, where you can change the properties used when drawing the selected shape on the timeline. Select the **Start property** and **End property** dropdown menus for shapes that use two time properties, or select **Time property** for shapes that use a single property.
![The Timeline style configuration section for the Flights object. The shape is set to Bar, and there are options to select a start property and end property.](/docs/resources/foundry/map/timeline_bar-select-time-properties.png)
除非所有属性都已设置,否则 timeline geometry 不会出现在 timeline 中。

The timeline geometry will not appear in the timeline unless all its properties have been set.
![The Timeline style configuration section for the Flights object. The shape is set to Diamond, and there is an option to select a time property.](/docs/resources/foundry/map/timeline_diamond-select-time-property.png)
您在 **Timeline** 样式配置部分中选择的 **Shape** 会在 timeline 上为 object type 的每个实例呈现。例如,下图显示了用菱形表示 timeline 上的 `Flights` object type。

The **Shape** you choose in the **Timeline** style configuration section renders for every instance of the object type in the timeline. For example, the image below shows diamond shapes to represent the `Flights` object type on the timeline.
![The Flights object type, represented as diamonds on the map timeline.](/docs/resources/foundry/map/timeline_diamond-on-timeline.png)
选择 **Geometry** 部分中的 **Color** 菜单,以配置形状颜色在地图 timeline 上的呈现方式。

Select the **Color** menu in the **Geometry** section to configure how shape colors render on your map's timeline.
![The timeline color configuration window, currently set to a fixed color.](/docs/resources/foundry/map/timeline_color-menu.png)
您还可以使用 properties 和 measures 通过更改 **Color by** 下拉菜单中的所选选项来配置 timeline 颜色样式。例如,下图显示了一个 timeline geometry 配置为使用 `Arrival Latitude` property 和彩虹色谱进行着色。

You can also use properties and measures to configure timeline color styling by changing the selected option in the **Color by** dropdown menu. For example, the image below shows a timeline geometry configured to color by the `Arrival Latitude` property with a rainbow color spectrum.
![The timeline color configuration window set to color by a property using a rainbow color spectrum. The objects that appear on the map and timeline use a rainbow of colors based on a linear interpolation.](/docs/resources/foundry/map/timeline_color-by-property.png)