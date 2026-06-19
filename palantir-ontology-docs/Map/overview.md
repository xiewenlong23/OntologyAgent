<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/overview/
---
# Map
**Map** 应用程序提供强大的地理空间和时间分析与可视化功能，允许您将来自 Foundry 各处的数据整合到统一的地理空间体验中：

The **Map** application provides powerful geospatial and temporal analysis and visualization capabilities, allowing you to integrate data from across Foundry into a cohesive geospatial experience:
* 探索地理空间对象之间的连接，遍历物理网络。
* 使用边界框和多边形相交查询，对点和多边形数据进行地理空间搜索。
* 可视化来自各种来源的上下文地理空间数据，包括大规模矢量数据和卫星影像，以及时间数据（例如对象随时间移动的路径和事件）。
* 通过绘制形状和执行地理空间操作进行交互。
* 使用地图模板构建地理空间应用程序。

* Explore connections between geospatial objects, traverse physical networks.
* Search geospatially for point and polygon data, using bounding box and polygon intersection queries.
* Visualize contextual geospatial data from a variety of sources, including high-scale vector data and satellite imagery, and temporal data such as paths of object movements over time, and events.
* Interact by drawing shapes and performing geospatial actions.
* Build geospatial applications using map templates.
![Map Application](/docs/resources/foundry/map/map-overview.png)
## Geospatial data on the Map
Map 应用程序使用 [Web Mercator Projection ↗](https://en.wikipedia.org/wiki/Web_Mercator_projection)（EPSG:3857）渲染地图，并期望以 WGS 84 度（EPSG:4326）格式的经纬度坐标作为输入。有关在 Foundry 中转换地理空间数据的更多信息，请参阅 [Foundry 中的地理空间数据](/docs/foundry/geospatial/overview/)。

The Map application renders maps using the [Web Mercator Projection ↗](https://en.wikipedia.org/wiki/Web_Mercator_projection) (EPSG:3857), and expects latitude/longitude coordinates in WGS 84 degrees (EPSG:4326). See [Geospatial data in Foundry](/docs/foundry/geospatial/overview/) for more information on transforming geospatial data in Foundry.