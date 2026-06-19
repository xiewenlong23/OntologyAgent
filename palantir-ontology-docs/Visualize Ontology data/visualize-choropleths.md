<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-choropleths/
---
# Choropleths
分级统计地图（Choropleth map）通过计算每个区域内所有 Object 的聚合来为区域着色。分级统计图对于可视化大型数据集中的空间模式非常有用。该示例地图展示了一个由 3100 万个交通事故 Object 生成的分级统计地图，其中每个美国州根据其境内发生的交通事故的平均严重程度进行着色。

A choropleth map displays regions colored by an aggregation computed across all objects in each region. Choropleths are useful for visualizing spatial patterns in large datasets. This example map shows a choropleth map generated from 31 million traffic accident objects, where each US state is colored by the average severity of accidents that occurred within it.
![Choropleth map showing severity of traffic accidents by US State.](/docs/resources/foundry/map/choropleth-traffic-severity.png)
要配置分级统计地图，请将您要计算聚合的 Object 添加到地图中，然后从 **Styling** 面板中的 **Add display** 菜单中添加一个分级统计样式器。

To configure a choropleth map, add the objects you want to compute aggregations over to the map, and add a choropleth styler from the **Add display** menu in the **Styling** panel.
![Add choropleth option in display menu.](/docs/resources/foundry/map/choropleth-add-display.png)
然后您需要指定如何将 Object 分组到各个区域中，以及如何显示每个区域。分级统计区域的样式选项与 [polygon displays](/docs/foundry/map/visualize-polygons-lines/) 相同，唯一的区别在于所有值都是基于每个区域内所有 Object 计算出的聚合。

You then need to specify how to group objects into regions, as well as how each region should be displayed. A choropleth region has the same styling options as [polygon displays](/docs/foundry/map/visualize-polygons-lines/), with the only difference that all the values are based on aggregations computed over all objects in each region.
## Grouping objects into regions
分级统计图的 **Regions** 样式部分允许您指定如何将 Object 分组到区域中，每个区域将在地图上显示为单个 polygon。您可以通过具有 Map 应用支持的 boundary identifier 类型的 Property，或者链接到图层中 Object 的 Object Type 来将 Object 分组。

The **Regions** section of styling for choropleths lets you specify how to group objects into regions, where each region will show as a single polygon on the map. You can group objects together by a property that has a boundary identifier type supported by the Map application, or an object type linked to the objects in your layer.
### Group by boundary identifiers
Map 应用支持为配置了某些常见 identifier 类型的 Object 渲染分级统计图。这些 boundary 类型的 polygon geometry 已内置于 Map 应用中，如果您的数据已经附加了这些 identifier 类型之一，则可以更轻松地进行数据集成。

The map application supports rendering choropleths for objects that are configured with some common identifier types. The polygon geometry for these boundary types is built in to the Map application, making your data integration easier if your data already has one of these identifier types attached.
Map 支持的 identifier 类型的一些示例包括：

Some examples of identifier types that the map supports are:
* ISO 3166 国家代码

* US State 缩写（CA、TX、OR 等）

* US County FIPS 代码

* ISO 3166 country codes
* US State abbreviations (CA, TX, OR, …)
* US County FIPS codes
有关支持的完整 identifier 范围以及如何配置 Property Type 以引用它们以用于地图的更多信息，请参阅 [Map 的 Ontology objects](/docs/foundry/map/integrate-objects/#boundary-identifiers) 页面。

See the [Ontology objects for the map](/docs/foundry/map/integrate-objects/#boundary-identifiers) page for more information on the full range of identifiers supported, and how to configure property types to reference them for use in maps.
要配置 boundary identifier，请在 **Group by** 下拉菜单中选择 **Property** 选项，然后从配置了 identifier 的 Property 中的 **Property** 下拉菜单中进行选择。只有在 Ontology 中配置为 boundary identifier 的 Property 才会显示。

To configure a boundary identifier, select the **Property** option in the **Group by** dropdown menu, and then choose from the properties that have an identifier configured in the **Property** dropdown menu. Only properties that are configured in the Ontology as a boundary identifier will be shown.
选择 boundary Property 后，在计算样式聚合时，所有具有相同 Property 值的 Object 将被分组在一起。

After selecting a boundary property, all objects with the same value for that property type will be grouped together when computing aggregations for styling.
### Group by linked objects
如果您需要为区域提供自己的 geometry，可以通过选择 ontology link 将 Object 分组在一起。然后，Map 应用将链接到同一 Object 的 Object 分组在一起。[了解有关自定义区域 geometry 的 ontology 配置](/docs/foundry/map/integrate-objects/#linked-objects) 的更多信息。

If you need to provide your own geometry for regions, you can group objects together by selecting an ontology link. The Map application will then group together objects that are linked to the same object. [Learn more about the ontology configuration](/docs/foundry/map/integrate-objects/#linked-objects) for custom region geometry.
## Styling by aggregation
在分级统计地图中，基于值的样式有所不同，因为每个区域的颜色都是基于其内部 Object 计算的聚合。定义分级统计聚合有两种方式，**standard** 和 **expression**。

Value-based styling is different in choropleth maps, since each region is colored based on an aggregation computed over the objects within. There are two ways to define aggregations for a choropleth, **standard**, and **expression**.
### Standard aggregations
标准 aggregation 是一种简单的方式，用于在某个区域内对对象的 property 进行 aggregation。要配置标准 aggregation，请打开 **Property** 菜单，然后选择您要使用的 property 和 aggregation function（sum、mean、max、min）。

A standard aggregation is a simply way to define an aggregation over a property of the objects in a region. To configure a standard aggregation, open the **Property** menu and select the property and aggregation function (sum, mean, max, min) you want to use.
![Standard aggregation configuration.](/docs/resources/foundry/map/choropleth-standard-aggregation.png)
## Expression aggregations
expression aggregation 允许您对区域内的对象定义自定义 aggregation。通过添加多个 expression reference 来构建 expression aggregation，列表中的最后一个 reference 提供的值将用于为该区域上色。每个 reference 可以是以下之一：

An expression aggregation lets you define a custom aggregation over the objects in a region. Build an expression aggregation by adding multiple expression references, and the last reference in the list provides the value that will be used to color the region. Each reference can be one of:
* 对归入该区域的对象的 property 进行简单的 aggregation

* 来自该区域本身的 property（仅在使用 linked objects 进行分组时可用）

* 将其他两个 reference 进行组合的 operation

* A simple aggregation over a property of the objects grouped into a region
* A property from the region itself (only available when grouping by linked objects)
* An operation that combines two other references
例如，此地图使用 expression aggregation，根据每个区域的步道密度为美国林务局护林区 (US Forest Service Ranger Districts) 着色。

For example, this map uses an expression aggregation to color US Forest Service Ranger Districts by the density of trails in each district.
![Choropleth map showing trail density by US Forest Service Ranger District.](/docs/resources/foundry/map/choropleth-trail-density.png)
它使用三个 expression 来计算步道密度：

It uses three expressions to compute the trail density:
* 第一个计算每个美国林务局护林区内步道的总长度。
* 第二个引用该区域的总面积。

* 第三个是一个 operation，通过将第一个 reference 除以第二个 reference 来计算每英亩的平均步道长度。

* The first computes the total length of trails within each US Forest Service Ranger District.
* The second references the total area of the region.
* The third is an operation that computes the average trail length per acre, by dividing the first reference by the second.