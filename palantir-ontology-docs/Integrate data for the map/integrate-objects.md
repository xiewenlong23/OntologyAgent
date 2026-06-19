<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/integrate-objects/
---
# Ontology objects
Map 应用程序支持附加了地理空间数据的 Ontology 对象。

The Map application supports Ontology objects with geospatial data attached.
## Ontology-native representation
点、线和多边形 geometry 可以使用 `geopoint` 或 `geoshape` property 类型在 ontology 中指定。有关更多详细信息,请参阅 [geospatial 文档中的 ontology 部分](/docs/foundry/geospatial/ontology/)。

Point, line, and polygon geometries can be specified in the ontology using the `geopoint` or `geoshape` property types. See the [ontology section of the geospatial docs](/docs/foundry/geospatial/ontology/) for more details.
## Circles
可以通过在 Object Type 的 **Capabilities** 选项卡的 **Geospatial** 部分中选择一个 **Radius** property 来指定 circle geometry。Radius property 可以是任何以米为单位计量的 numeric property。

A circle geometry can be specified on an object type by selecting a **Radius** property in the **Geospatial** section of the object type's **Capabilities** tab. The radius property can be any numeric property measured in meters.
![Radius property configuration in the Ontology Manager](/docs/resources/foundry/map/oma-capabilities-radius-earthquake.png)
> **⚠️ 警告**

> Circle geometry 仅在地图上渲染,不会被索引用于搜索。如果您需要根据 circle geometry 对对象进行地理空间搜索,则需要使用 [polygon](#ontology-native-representation) 来近似表示一个 circle。
> **⚠️ 警告**

> The circle geometry is only rendered on the map, not indexed for searching.  If you need objects to be geospatially searchable based on a circle geometry, you will need to approximate a circle using a [polygon](#ontology-native-representation).
## Choropleths
要渲染 [choropleth visualizations](/docs/foundry/map/visualize-choropleths/)，您需要配置您的 ontology，以便将 objects 分组到 regions 中。有两种方法可以做到这一点：**boundary identifiers** 和 **linked objects**。

To render [choropleth visualizations](/docs/foundry/map/visualize-choropleths/), you will need to configure your ontology so that objects can be grouped together into regions. There are two ways to do so, **boundary identifiers** and **linked objects**.
### Boundary identifiers
Maps 支持为配置了某些常见 region identifier 类型的 objects 渲染 choropleths——包括 ISO 3166 国家代码、US State 缩写等。这些 boundary 类型的 polygon geometry 内置于 map application 中，如果您的数据已经附加了这些 identifier 类型之一，则可以更轻松地进行数据集成。这些 identifiers 是通过将特定的 [Value Type](/docs/foundry/object-link-types/value-types-overview/) 附加到您要映射的 object type 的 property 来配置的。

Maps support rendering choropleths for objects that are configured with some common region identifier types -- including ISO 3166 country codes, US State abbrevations, and more. The polygon geometry for these boundary types is built into the map application, making your data integration easier if your data already has one of these identifier types attached. These identifiers are configured by attaching a specific [Value Type](/docs/foundry/object-link-types/value-types-overview/) to a property on the object type you want to map.
要配置 boundary identifiers，首先在 Marketplace 中搜索并安装 "Choropleth Value Types" product。该 product 包含 map application 知道如何渲染为 choropleths 的 ontology value types。

To configure boundary identifiers, first search for and install the "Choropleth Value Types" product in Marketplace. This product contains the ontology value types that the map application knows how to render as choropleths.
![Image of the choropleth value types product in Marketplace](/docs/resources/foundry/map/marketplace-choropleth-value-types.png)
当前支持的 region 类型及其识别方式包括：

The current supported region types and ways of identifying them are:
* Admin 0（全球 administrative level 0 boundaries）

* ISO 3166 alpha-2 国家代码

* ISO 3166 alpha-3 国家代码

* US States
* FIPS 代码

* USPS 缩写

* US Counties
* FIPS 代码

* ANSI 代码

* Admin 0 (global administrative level 0 boundaries)
* ISO 3166 alpha-2 country codes
* ISO 3166 alpha-3 country codes
* US States
* FIPS codes
* USPS abbrevations
* US Counties
* FIPS codes
* ANSI codes
如果您的 object type 已经有一个包含这些 identifiers 之一的 property，请在 Ontology Manager 中该 property 的 **Value Type** 下拉菜单中选择相应的 value type。

If your object type already has a property the contains one of these identifiers, select the corresponding value type in the **Value Type** dropdown menu for that property in Ontology Manager.
![Image of the Value Type dropdown menu in the Ontology Manager](/docs/resources/foundry/map/oma-choropleth-value-type.png)
如果您想为上述 region 类型之一显示 choropleths，但您的数据具有 latitude/longitude points 而不是受支持的 identifiers 之一，请使用来自 Marketplace 的 "Choropleth Boundary Datasets" product 来附加 region identifiers。该 product 包含包含 regions 的实际 geometries 和其他元数据的 datasets。使用 Pipeline Builder 的 [Geometry intersection join](/docs/foundry/pipeline-builder/transforms-geospatial/#geometry-intersection-joins) 查找每个 point 所在的 region 并附加相应的 region identifier，然后在 ontology manager 中配置相应的 value type。

If you want to display choropleths for one of the region types above, but your data has latitude/longitude points instead of one of the supported identifiers, use the "Choropleth Boundary Datasets" product from Marketplace to attach the region identifiers. This product contains datasets that contain the actual geometries and other metadata for the regions. Use Pipeline Builder's [Geometry intersection join](/docs/foundry/pipeline-builder/transforms-geospatial/#geometry-intersection-joins) to find the region that each point lies within and attach the corresponding region identifier, then configure the corresponding value type in ontology manager.
### Linked objects
如果您想显示包含上述未包含的 region 类型的 choropleth，或者希望更好地控制 region geometries 和 regions 上的 properties，您可以创建一个包含您选择的 region geometry 的 object type。然后从您要聚合的 object type 到该 region object type 创建一个 many-one link。

If you want to display a choropleth with a region type is not included above, or otherwise want more control over the region geometries and properties on the regions, you can create an object type with region geometry of your choice. Then create a many-one link from the object type you want to aggregate over to that region object type.
例如，假设您想显示一个 choropleth，显示每个 sales region 的 orders 总价值。为此配置 ontology 的一种简单方法是：

For example, imagine you want to display a choropleth that shows the total value of orders placed for each sales region. A simple way to configure the ontology for this is to have:
* 一个 "Sales region" object type，带有一个包含每个 sales region geometry 的 geoshape property。

* 一个 "Order" object type，具有以下 properties：

* "Sales region"，包含每个 order 所下达到的 region 的 primary key

* 一个 "Value"，包含该 order 的总价值

* 一个从 "Order" 到 "Sales region" 的 many-one

* A "Sales region" object type with a geoshape property containing the geometry of each sales region.
* An "Order" object type, with the properties:
* "Sales region" that contains the primary key of the region each order was placed in
* A "Value" that contains the total value of the order
* A many-one from "Order" to "Sales region"
要显示 choropleth：

To display the choropleth:
1. 使用 [search dialog](/docs/foundry/map/add-to-map/#add-ontology-objects) 将您的 "Order" objects 添加到 map

2. [添加一个 **Choropleth** display](/docs/foundry/map/visualize-objects/#displays) 用于 "Order" layer

3. 在 [**Regions** section](/docs/foundry/map/visualize-choropleths/#grouping-objects-into-regions) 中选择 **Linked object** 选项，并选择从 "Order" object 链接到其关联的 "Sales region" 的 link type。

4. 使用 "Value" property 在 [styling aggregations](/docs/foundry/map/visualize-choropleths/#styling-by-aggregation) 中控制每个 region 的颜色

1. Use the [search dialog](/docs/foundry/map/add-to-map/#add-ontology-objects) to add your "Order" objects to the map
2. [Add a **Choropleth** display](/docs/foundry/map/visualize-objects/#displays) for the "Order" layer
3. Choose the **Linked object** option in the [**Regions** section](/docs/foundry/map/visualize-choropleths/#grouping-objects-into-regions), and select the link type that links from an "Order" object to its associated "Sales region".
4. Use the "Value" property in [styling aggregations](/docs/foundry/map/visualize-choropleths/#styling-by-aggregation) to control the color of each region
## H3 hexagons
Objects 可以包含包含来自 [H3 geospatial indexing system ↗](https://h3geo.org/docs/) 的 H3 cell IDs 的 string properties。这些将在 map 上呈现为相关的 hexagons。

Objects can include string properties containing H3 cell IDs from the [H3 geospatial indexing system ↗](https://h3geo.org/docs/). These will render as relevant hexagons on the map.
要指定 string property 包含 H3 cell IDs，请在 object type 的 **Capabilities** 选项卡的 Geospatial 部分中的 **H3 cell** 下选择该 property。

To specify that a string property contains H3 cell IDs, select that property under **H3 cell** in the Geospatial section of the object type's **Capabilities** tab.
![H3 property configuration in the Ontology Manager](/docs/resources/foundry/map/oma-capabilities-h3-tree.png)
> **⚠️ 警告**

> H3 hexagon 仅在 Map 上呈现，不被 indexing 用于搜索。如果您需要 objects 基于 H3 hexagon 进行 geospatial 搜索，您将需要将 H3 cell IDs 转换为 GeoJSON Polygons，并将它们包含在如上所述的 `geoshape` property 中。
> **⚠️ 警告**

> The H3 hexagon is only rendered on the Map, not indexed for searching. If you need objects to be geospatially searchable based on a H3 hexagon, you will need to convert the H3 cell IDs into GeoJSON Polygons and include them in a `geoshape` property as described above.
## Georectified images
一个 Object 可以附加地理校正图像，例如卫星照片、航空影像或物理地图的扫描件。地理校正图像需要两个 Property：

An object can have georectified images attached, such as a satellite photo, aerial imagery, or a scan of a physical map. Two properties are required for the georectified image:
* 一个 image URL `String` Property，包含要渲染的图像的 URL。支持的图像文件扩展名包括 `.png`、`.jpg`、`.jpeg`、`.gif`、`.webp`、`.bmp`、`.ico` 和 `.svg`。image URL Property 的 ID 用于配置 image bounds Property。

* 一个 image bounds `geoshape` Property，包含一个 GeoJSON Polygon，表示该图像的地理校正边界。Polygon 必须按顺时针顺序指定其顶点，从左下角开始。

* image bounds Property 必须具有一个 type class，用于指示 image URL Property 的 ID，格式如下：

* Kind：`geo`
* Value：`bounds.<image URL property ID>`，其中 `<image URL property ID>` 是 image URL Property 的 ID。

* 例如，如果 image URL Property ID 为 `image_url`，则 typeclass 应为：Kind：`geo`，Value：`bounds.image_url`

* An image URL `String` property containing the URL of the image to render. Supported image file extensions include `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`, `.ico`, and `.svg`. The ID of the image URL property is used to configure the image bounds property.
* An image bounds `geoshape` property containing a GeoJSON Polygon of a quadrilateral representing the georectified bounds of the image. The polygon must specify its vertices in clockwise order, beginning with the bottom left corner.
* The image bounds property must have a type class indicating the ID of the image URL property, in the following format:
* Kind: `geo`
* Value: `bounds.<image URL property ID>` where `<image URL property ID>` is the ID of the image URL property.
* For example, if the image URL property ID is `image_url` then the typeclass would be: Kind: `geo`, Value: `bounds.image_url`
![Georectified image property configuration in the Ontology Manager](/docs/resources/foundry/map/oma-geo-bounds-typeclass.png)
具有地理校正图像的 Object 与所有 `geoshape` Property 一样，会被索引以用于地理空间搜索。

Objects with georectified images are indexed for geospatial search, as with all `geoshape` properties.
## Tiled imagery from media sets \[Beta]
> **ℹ️ 注意: Beta**

> 在 Maps 中使用 media references 处于 [beta](/docs/foundry/platform-overview/development-life-cycle/) 开发阶段，可能在您的注册中不可用。在积极开发过程中，功能可能会发生变化。
> **ℹ️ 注意: Beta**

> Using media references in Maps is in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.
地理参考的栅格影像也可以通过将 GeoTIFF 影像（`.tiff`、`.tif`）上传到 [media set](/docs/foundry/data-integration/media-sets/) 来以 tile 形式显示。然后，具有 [media reference property](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) 的 Object Type 可以添加到地图中，并且随着用户在 Map 上平移或缩放，仅会加载影像的可见部分。

Georeferenced raster imagery can also be displayed in tiles by uploading GeoTIFF imagery in a  (`.tiff`, `.tif`) to a [media set](/docs/foundry/data-integration/media-sets/). From there, object types with a [media reference property](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) can be added to the map and only the visible portions of the imagery will be loaded as the user pans or zooms around the Map.
## Track objects
Object 可以具有数字类型的 [time series properties](/docs/foundry/time-series/time-series-overview/)，表示 Object 随时间变化的经度和纬度，使用户能够查看 Object 随时间移动的路径以及其在任何时间点的位置。

Objects can have numeric [time series properties](/docs/foundry/time-series/time-series-overview/) representing an object's latitude and longitude over time, allowing users to see the path the object traveled over time as well as its location at any point in time.
要为 Object Type 配置 track，请在 Object Type 的 **Capabilities** 选项卡的 **Geospatial** 部分中选择 **Track Latitude** 和 **Track Longitude** Property。这两个 Property 都必须是数字类型的 time series Property，表示 Object 随时间变化的位置。有关配置 time series 的更多信息，请参阅 [Time series setup](/docs/foundry/time-series/time-series-setup/)；有关在地图中可视化 track 选项的更多信息，请参阅 [track displays](/docs/foundry/map/visualize-tracks/)。

To configure the track for the object type, select the **Track Latitude** and **Track Longitude** properties in the **Geospatial** section of the object type's **Capabilities** tab. Both properties must be numeric time series properties representing the object's location over time. See [Time series setup](/docs/foundry/time-series/time-series-setup/) for more information on configuration time series, and [track displays](/docs/foundry/map/visualize-tracks/) for more information on the options in maps for visualizing tracks.
![Track latitude and longitude configuration in the Ontology Manager](/docs/resources/foundry/map/oma-capabilities-track-lat-lon.png)
## Event objects
Event Object 是发生在某个时间点或时间段内的 Ontology Object。通过在 Object Type 的 **Capabilities** 选项卡的 **Event** 部分中指定 **Event start time** 和 **Event end time** timestamp Property，可以将 Object Type 配置为 event。

Event objects are Ontology objects that occur at a point or period of time. Object types can be configured as events by specifying **Event start time** and **Event end time** timestamp properties in the **Event** section of the object type's **Capabilities** tab.
![Event configuration in the Ontology Manager](/docs/resources/foundry/map/oma-capabilities-event.png)
### Event objects on the map
如果将 event Object 添加到 Map，则可以将它们配置为仅在当前（也就是说，当所选 timestamp 处于 event 时间段内时）显示。

If event objects are added to the Map, they can be configured to only display when current (that is, when the selected timestamp is within the event period).
### Event objects linked to objects on the map
如果地图上的 Object 具有链接到它们的 event Object，则可以将 event Object 添加到 **Series** 面板中以进行时间分析，并且可以将当前 event 计数指标添加到 Object 标签。例如，一个 `road` Object 可以在地图上表示为线条，并且一个 `road` Object 可能具有链接的 `traffic accident` event；然后，用户可以使用这些指标查看每条 road 在任何时间点的交通 event 计数。

If objects on the map have event objects linked to them, the event objects can be added to the **Series** panel for temporal analysis, and current event count indicators can be added to object labels. For example, a `road` object could be represented as lines on the map, and a `road` object may have linked `traffic accident` events; a user could then use the indicators to see traffic event counts for each road at any point in time.
为此，event Object Type 必须在 Object Type 的 **Capabilities** 选项卡的 **Event** 部分中配置一个 **Event intent**，以指示 event 的严重程度。

For this to be possible, the event object type must be configured with an **Event intent** indicating the severity of the event in the **Event** section of the object type's **Capabilities** tab.