<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-points/
---
# Point displays
Maps 包含两种可视化点 displays 的方式：图标和圆圈。要显示图标或圆圈，您需要一个为每个对象提供位置的 geometry source。支持的几何来源包括 [geopoint properties](/docs/foundry/geospatial/ontology/) 和 [tracks](/docs/foundry/map/integrate-objects/#track-objects)。

Maps contain two ways to visualize point displays: icons and circles. To display an icon or circle, you need a geometry source that provides a location for each object. The supported geometry sources are [geopoint properties](/docs/foundry/geospatial/ontology/) and [tracks](/docs/foundry/map/integrate-objects/#track-objects).
当使用 track 作为点 geometry source 时，地图将从 track 中提取与当前 [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range) 对应的位置。有一些配置选项可控制该位置的插值方式，相关内容在 [tracks](/docs/foundry/map/visualize-tracks/) 页面中介绍。

When using a track as a point geometry source, the map will extract a location from the track that corresponds to the current [selected time](/docs/foundry/map/time-overview/#selected-time-and-time-range). There are configuration options that control how that location is interpolated, which are covered on the [tracks](/docs/foundry/map/visualize-tracks/) page.
## Icon configuration
图标是可视化点数据的最常见方式之一。每个图标都放置在 geometry source 提供的位置，并且可以以多种方式进行样式设置，以生成适合您工作流的可视化效果。

Icons are one of the most common ways to visualize point data. Each icon is placed at the location provided by the geometry source, and can be styled in a variety of ways to generate a visualization that suits your workflow.
### Icon
**Icon** 部分允许您控制将为每个对象显示的图标。指定所显示图标的选项包括：

The **Icon** section allows you to control the icon that will be displayed for each object. The options for specifying the icon that is displayed are:
* **Object default：** 图标将是 object type 的默认图标，在 Ontology Management 应用程序中配置。

* **Media image：** 选择一个图像 media item 以显示图层中的所有对象。

* **Fixed icon：** 选择一个特定图标以显示图层中的所有对象。

* **Property：** 每个对象使用由对象上的 property 确定的图标进行显示。

* **Object default:** The icon will be the default icon for the object type, as configured in the Ontology Management application.
* **Media image:** Choose an image media item to display for all objects in the layer.
* **Fixed icon:** Choose a specific icon to display for all objects in the layer.
* **Property:** Each object is displayed with an icon that is determined by a property on the object.
下面的示例使用带有颜色和图标样式的 rain status time series 来可视化太平洋西北地区在选定日期观测到降雨的气象站。

The example below uses a rain status time series with both color and icon styling to visualize which weather stations across the Pacific Northwest observed rain on the selected day.
![A map displaying sun and rain icons to indicate the weather conditions of the region.](/docs/resources/foundry/map/styling-icon-type.png)
### Image media items
属性选项支持 [media reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) 类型的 object 属性,并会将底层 media 显示为图标。Image 类型的 media reference 是图标唯一支持的 media 格式。

The property option supports [media reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) type object properties and will display underlying media as icons. Image media references are the only supported media format for icons.
### Rotation
您可以通过任意 [value-based styling](/docs/foundry/map/visualize-objects/#value-based) 选项来控制图标的旋转。对于 track geometry 来源,还有一个 **Automatic** 选项,可以根据 track 将图标沿对象的移动方向进行旋转。

You can control the rotation of the icon by any of the [value-based styling](/docs/foundry/map/visualize-objects/#value-based) options. For track geometry sources, there is also an **Automatic** option which rotates the icon in the direction of the object's movement according to the track.
下面的示例使用固定的箭头图标和旋转样式来显示 vessel 对象(船只对象)的移动方向。

The example below uses a fixed arrow icon and rotation styling to display the direction of movement for vessel objects.
![Vessel direction.](/docs/resources/foundry/map/styling-icon-rotation.png)
### Marker shape
您可以为图标配置三种样式的 markers:

There are three styles of markers that you can configure for icons:
| Circle                                              | Pin                                           | None                                          |
| --------------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| ![Circle marker.](/docs/resources/foundry/map/styling-marker-circle.png) | ![Pin marker.](/docs/resources/foundry/map/styling-marker-pin.png) | ![No marker.](/docs/resources/foundry/map/styling-marker-none.png) |
## Circle configuration
每个 circle 以所提供的 location 为中心绘制,并使用可在样式的 **radius** 部分进行配置的 radius 值。

Each circle is centered on the location provided and drawn with a radius value that you can configure in the **radius** section of styling.
![Airports with different circle sizes.](/docs/resources/foundry/map/styling-circle-radius.png)
其他 circle 样式选项与 [polygon 显示的选项](/docs/foundry/map/visualize-polygons-lines/) 相同。

The other circle style options are the same as [the options for polygon displays](/docs/foundry/map/visualize-polygons-lines/).
## Loading methods
当显示大量对象时,icon 和 circle 显示也支持基于 tile 的 [loading methods](/docs/foundry/map/objects-loading-methods/)。

When displaying a large number of objects, icon and circle displays can also support tile-based [loading methods](/docs/foundry/map/objects-loading-methods/).