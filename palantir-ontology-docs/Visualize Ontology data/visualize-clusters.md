<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-clusters/
---
# Clusters
cluster display 非常适合基于 geopoint location property 的较大对象集。cluster 类似于点，但它不是为每个对象绘制一个标记，而是根据对象与 cluster 的地理邻近度进行聚合。可以配置 cluster 的大小和/或颜色，以表示特定区域内对象的数量，或其他 aggregation metric（例如区域内对象某 property 的 sum 或 average）。当用户放大、缩小或平移以引入新数据时，每个 cluster 区域的内容将自动更新。

Cluster displays are ideal for larger object sets based on a geopoint location property. Clusters are similar to points, but instead of plotting a single marker per object, the objects being plotted are aggregated based on their geographic proximity to clusters. The size and/or color of the cluster can be configured to represent the number of objects within a given area, or some other aggregation metric such as the sum or average of a property across the objects within a region. The contents of each cluster region will update automatically as the user zooms in, zooms out, or pans to introduce new data.
![Cluster map showing total departing flights.](/docs/resources/foundry/map/cluster-example.png)
cluster display 可以使用 **Add geometry** 选项添加到 object layer。cluster display 的 **Center** 配置仅接受 **Geopoint** property。

Cluster displays can be added to object layers using the **Add geometry** option. The **Center** configuration of a cluster display accepts only **Geopoint** properties.
## Styling by aggregation
cluster display 大致具有与 [circle geometries](/docs/foundry/map/visualize-points/#circle-configuration) 相同的样式选项，但其颜色和半径配置是作为单个 cluster 中所有对象的 aggregate value 来计算的。要了解有关通过 aggregate value 进行样式的更多信息，请参阅 choropleth display 的 [styling by aggregation](/docs/foundry/map/visualize-choropleths/#styling-by-aggregation) 部分。

Cluster displays have the roughly the same styling options as [circle geometries](/docs/foundry/map/visualize-points/#circle-configuration), but the color and radius configurations are computed as aggregate values over all objects in a singular cluster. To learn more about styling via aggregate values, see the [styling by aggregation](/docs/foundry/map/visualize-choropleths/#styling-by-aggregation) section for choropleth displays.
## Cluster text labels
在 cluster display 仍处于 beta 阶段时，文本标签的内容将反映用于颜色配置的 aggregate value，或在颜色样式为固定值时反映用于半径配置的 aggregate value。

While cluster displays are in the beta phase of development, the content of the text labels will reflect either the aggregate value used in the color configuration, or the aggregate value used in the radius configuration if the color style is fixed.