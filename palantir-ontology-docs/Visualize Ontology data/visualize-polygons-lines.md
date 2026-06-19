<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-polygons-lines/
---
# Polygon and line displays
Maps 可以根据您的 ontology 对象渲染 polygons 和 lines。可以通过以下两种方式指定要绘制的 line 或 polygon geometry:

Maps can render polygons and lines based on your ontology objects. There are two ways to specify the line or polygon geometry to draw:
* **Geoshape 属性:** 显示存储在对象 geoshape 属性中的 GeoJSON line 和 polygon geometries。

* **Line segment:** 显示对象上两个 geopoint 属性之间的 lines。

* **Geoshape properties:** Display GeoJSON line and polygon geometries stored in a geoshape property on your objects.
* **Line segment:** Display lines between two geopoint properties on objects.
有关如何配置 styling 规则以及 color 和 opacity styling 配置的更多信息,请参阅 [value-based styling](/docs/foundry/map/visualize-objects/#value-based-styling)。Polygons 和 lines 可以使用以下其他属性进行样式设置。

See [value-based styling](/docs/foundry/map/visualize-objects/#value-based-styling) for more information on how styling rules are configured, as well as color and opacity styling configuration. Polygons and lines can be styled with the following additional attributes.
## Stroke width
使用 **Stroke width** 部分来控制渲染 lines 时使用的宽度,或未填充 polygons 的 stroke。

Use the **Stroke width** section to control the width used when rendering lines, or the stroke of polygons that are not filled.
![Styling line width.](/docs/resources/foundry/map/styling-line-width.png)
## Stroke style
使用 **Stroke style** 部分来控制渲染 lines 时使用的虚线模式,或未填充 polygons 的 stroke。可用选项包括:

Use the **Stroke style** section to control the dash pattern used when rendering lines, or the stroke of polygons that are not filled. The available options are:
| Solid                                           | Dashed                                            | Dotted                                            |
| ----------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| ![Solid line.](/docs/resources/foundry/map/styling-stroke-solid.png) | ![Dashed line.](/docs/resources/foundry/map/styling-stroke-dashed.png) | ![Dotted line.](/docs/resources/foundry/map/styling-stroke-dotted.png) |
对于 line segments,您还可以配置箭头以指示 line 的方向。

For line segments, you can also configure arrows to indicate the direction of the line.
![Line segment with arrows.](/docs/resources/foundry/map/styling-arrows.png)
## Fill polygons
启用 **Fill polygons** 时,polygons 将以最简 stroke 渲染,并在其内部填充指定的 color。禁用时,polygon 将仅使用 **Stroke width** 和 **Stroke style** 中的样式配置进行 stroke。

When **Fill polygons** is enabled, polygons render with a minimal stroke and their interior filled with the specified color. When disabled, the polygon is instead only stroked, using the styling configuration in **Stroke width** and **Stroke style**.
| Fill enabled                                        | Fill disabled                                         |
| --------------------------------------------------- | ----------------------------------------------------- |
| ![Filled polygon.](/docs/resources/foundry/map/styling-fill-enabled.png) | ![Stroked polygon.](/docs/resources/foundry/map/styling-fill-disabled.png) |
## Loading methods
当显示大量对象时,polygon 和 line geometries 也支持基于 tile 的 [loading methods](/docs/foundry/map/objects-loading-methods/)。

When displaying a large number of objects, polygon and line geometries can also support tile-based [loading methods](/docs/foundry/map/objects-loading-methods/).