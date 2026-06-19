<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/core-concepts/
---
# Core concepts
## Layers
**Layer** 是用于构建地图的地理数据集合。Foundry Map 应用程序支持多种 layer，这些 layer 可以组合在一起，形成强大的地理空间可视化：

A **layer** is a collection of geographic data that are used to build a map. The Foundry Map application supports a variety of layers that can be combined to form powerful geospatial visualizations:
* **Base layer：**Base layer 通过渲染包括道路、城市、边界、地名等在内的世界地理特征，为地图提供基础。可用的 base layer 包括浅色主题、深色主题和卫星图像等。使用 **Layers** 面板中的选择器来切换 base layer。

* **Base layer:** A base layer provides the foundation of a map by rendering geographic features of the world including roads, cities, borders, place names, and more. Available base layers include a light theme, a dark theme, and satellite imagery, amongst others. Change base layers by using the selector in the **Layers** panel.
![Base layer selector](/docs/resources/foundry/map/core-concepts-base-layer.png)
您还可以选择使用以下不同类型的 layer：

You also have the option of using different types of layers as follows:
* **Object layer：**用于利用来自您的 Ontology 中 object 的 [geospatial data](/docs/foundry/map/integrate-objects/)。

* **Link layer：**在执行 Search Around 之后，显示 object 之间的关系。

* **Overlay layer：**使用 [Map Layer Editor](/docs/foundry/map/layer-editor/) 一次性创建高质量可视化，以导入到一个或多个地图中。

* **Annotation layer：**绘制用于突出显示并提供有关地图特定区域上下文信息的形状。阅读有关 [creating annotations](/docs/foundry/map/annotations/) 的更多信息。

* **Object layer:** Use to leverage [geospatial data on objects](/docs/foundry/map/integrate-objects/) from your Ontology.
* **Link layer:** Show the relationships between objects after executing a Search Around.
* **Overlay layer:** Create high-quality visualizations using the [Map Layer Editor](/docs/foundry/map/layer-editor/) just once for import into one or many maps.
* **Annotation layer:** Draw shapes that highlight and provide contextual information about specific areas of your map. Read more about [creating annotations](/docs/foundry/map/annotations/).
## Object styling
您应用于 object 的 [style](/docs/foundry/map/visualize-objects/) 决定了它们在地图上的外观。

The [style](/docs/foundry/map/visualize-objects/) you apply to your objects defines their appearance on a map.
## Time selection
每张地图都有一个 **selected time**,它始终位于当前选定的 **time window** 之内。Time window 决定了地图加载和显示 [time series](/docs/foundry/map/time-series/) 数据的时间段。[Time-based styling](/docs/foundry/map/visualize-objects/#opacity-styling) 可以利用 time selection 来有选择地控制带有时间数据的对象的透明度。阅读更多关于操作 [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range) 的信息。

Every map has a **selected time**, which is always within the currently selected **time window**. The time window determines the period of time for which the map loads and shows [time series](/docs/foundry/map/time-series/) data. [Time-based styling](/docs/foundry/map/visualize-objects/#opacity-styling) can use the time selection to selectively control the opacity of objects with temporal data. Read more about manipulating [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range).