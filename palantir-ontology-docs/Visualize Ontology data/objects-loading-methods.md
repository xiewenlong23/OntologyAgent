<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/objects-loading-methods/
---
# Loading methods
默认情况下，Map 应用程序会加载图层中的所有 Object 以在地图上渲染它们。这本质上会产生一个规模限制，因为您只能渲染从 Ontology 加载到浏览器中的数据量。**Loading method** 配置通过限制应用程序仅加载显示地图可见范围所需的必要数据，便于呈现大规模 Object 集。

By default, the Map application loads all objects in a layer to render them on the map. This inherently creates a scale limitation, as you can only render as much data as you can load from the Ontology into your browser. The **Loading method** configuration facilitates the presentation of high-scale object sets by restricting the application to load only the necessary data required to display the visible extent of the map.
## Configure loading methods
您可以使用样式面板中的 **Loading method** 下拉菜单为 display 配置加载方法。

You can configure loading methods for a display with the **Loading method** dropdown menu in the style panel.
![The loading methods configuration option in the style menu.](/docs/resources/foundry/map/objects-loading-methods.png)
加载方法选项如下：

The loading method options are as follows:
* **Auto（自动）：** 默认情况下，应用程序将根据图层内容在基于瓦片和基于 Object 的加载之间推断最佳选择。

* **Tile（瓦片）：** 加载地图视口范围内的简化几何数据。此选项最适合大型 Object 集，并优先考虑性能。

* **Object（Object）：** 加载单个 Object 的完整详细信息。此选项最适合复杂的样式设置。

* **Auto:** By default, the application will use the contents of the layer to infer the optimal choice between tile-based and object-based loading.
* **Tile:** Loads simplified geometry data within the bounds of the map viewport. This option is best suited for large object sets and prioritizing performance.
* **Object:** Loads full details for individual objects. This option is best suited for complex styling settings.
仅当满足以下条件时，您才能为 display 选择加载方法：

You will only be able to select a loading method selection for a display if the following is true:
* 该图层的 Object Type 至少具有一个 [geopoint 或 geoshape Property](/docs/foundry/geospatial/ontology/)。

* 该几何 Property 在 Ontology Manager 中已启用 **Searchable** [render hint](/docs/foundry/object-link-types/metadata-render-hints/)。如果未启用 **Searchable**，瓦片将为空，地图上将不会显示任何 Object。

* 该 display 类型支持基于瓦片的渲染。目前仅支持 icon、circle 和基于 geoshape 的 display。

* The object type for the layer has at least one [geopoint or geoshape property](/docs/foundry/geospatial/ontology/).
* The geometry property has the **Searchable** [render hint](/docs/foundry/object-link-types/metadata-render-hints/) enabled in Ontology Manager. If **Searchable** is not enabled, tiles will be empty and no objects will be visible on the map.
* Tile-based rendering is supported for the display type. Only icon, circle, and geoshape-based displays are currently supported.
## Add objects with tile-based loading methods
对于支持基于瓦片加载方法的 Object Type，搜索对话框将不限制可添加到地图的 Object 数量。因此，**Add all** 选项将始终启用。

For object types that support tile-based loading methods, the search dialog will not limit how many objects can be added to the map. As such, the **Add all** option will always be enabled.
## Tile-based loading method compatibility
在基于瓦片渲染的 display 中渲染的 Object 无法与许多其他 Map 应用程序功能正确配合使用。许多不兼容的功能需要从无法支持基于瓦片图层中所渲染数据规模的服务加载数据。

Objects rendered in a tile-backed display do not work correctly with a number of other Map application features. Many incompatible features require loading data from services that cannot support the scale of data rendered in tile-based layers.
以下章节列出了与基于瓦片加载方法不兼容的 Map 功能。

The following sections list the Map capabilities that are not compatible with tile-based loading methods.
### Styling
Geopoint 和 geoshape Property 是 [Object 图层 display](/docs/foundry/map/visualize-objects/#displays) 唯一支持的几何源，而对于所有 [基于值的样式选项](/docs/foundry/map/visualize-objects/#value-based-styling)，仅支持 Property 值。

Geopoint and geoshape properties are the only geometry sources supported for [object layer displays](/docs/foundry/map/visualize-objects/#displays), and only property values are supported for all [value-based styling options.](/docs/foundry/map/visualize-objects/#value-based-styling)
因此，以下选项*不*受支持：

As such, the following options are *not* supported:
* 基于时间序列的样式（measures 和 TSPs）

* Functions
* [按时间设置不透明度](/docs/foundry/map/visualize-objects/#opacity-styling)

* [Labels](/docs/foundry/map/visualize-objects/#labels)
* [Timeline geometries](/docs/foundry/map/visualize-timeline/)
* [Search Arounds](/docs/foundry/map/integrate-searcharounds/)
* Time series-based styling (measures and TSPs)
* Functions
* [Opacity by time](/docs/foundry/map/visualize-objects/#opacity-styling)
* [Labels](/docs/foundry/map/visualize-objects/#labels)
* [Timeline geometries](/docs/foundry/map/visualize-timeline/)
* [Search Arounds](/docs/foundry/map/integrate-searcharounds/)
### Filtering
在 tile-based display 中显示的 Objects 不受在 [histogram](/docs/foundry/map/histogram/#filtering) 或 [timeline](/docs/foundry/map/timeline/#filter-the-time-window) 中应用的过滤影响。

Objects displayed in a tile-based display do not respect filtering applied in the [histogram](/docs/foundry/map/histogram/#filtering) or the [timeline](/docs/foundry/map/timeline/#filter-the-time-window).
### Shapes
在 tile-based display 中显示的 Objects 不会包含在 [从活动选区创建 shapes](/docs/foundry/map/shapes/#from-selection) 时。

Objects displayed in a tile-based display will not be included when [creating shapes from the active selection](/docs/foundry/map/shapes/#from-selection).