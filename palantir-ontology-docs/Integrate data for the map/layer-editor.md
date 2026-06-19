<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/layer-editor/
---
# Map Layer Editor
Map Layer Editor 应用程序允许您创建、编辑和预览地图图层（map layer）。地图图层包含地理空间数据,并定义数据的可视化方式。您可以在 [Map Application](/docs/foundry/map/add-to-map/#add-map-overlays) 和 [Workshop map widget](/docs/foundry/workshop/widgets-map/#layers) 中使用地图图层。

The Map Layer Editor application allows you to create, edit, and preview map layers. A map layer contains geospatial data and defines how the data should be visualized. You can use map layers in the [Map Application](/docs/foundry/map/add-to-map/#add-map-overlays) and the [Workshop map widget](/docs/foundry/workshop/widgets-map/#layers).
Map Layer Editor 提供了一个可视化（point-and-click）UI,用于配置包含矢量或栅格数据的地图图层。如果您需要更多控制或希望使用更高级的地图功能,您也可以选择编写 [Mapbox GL JS Style Specification document ↗](https://docs.mapbox.com/mapbox-gl-js/style-spec/)。

The Map Layer Editor provides a point-and-click UI for configuring map layers that contain vector or raster data. If you need more control or want to use more advanced mapping features, you can instead choose to write a [Mapbox GL JS Style Specification document ↗](https://docs.mapbox.com/mapbox-gl-js/style-spec/).
## Create a new map layer
在 Foundry 中,导航到您希望在其中创建地图图层的文件夹,然后从 **New** 菜单中选择 **Map Layer**：

In Foundry, navigate to the folder in which you wish to create the map layer, and select **Map Layer** from the **New** menu:

> 📷 **[图片: New map layer button]**

> 📷 **[图片: New map layer button]**

然后,添加数据源或选择编写 Mapbox JSON 文档以开始配置您的图层。

Then, add a data source or choose to write a Mapbox JSON document to begin configuring your layer.
![Select layer type](/docs/resources/foundry/map/map-layer-editor-select-type.png)
> **⚠️ 警告**

> 我们建议仅在需要矢量或栅格图层不支持的功能时才使用 Mapbox JSON 文档。
> **⚠️ 警告**

> We recommend only using a Mapbox JSON document when you require functionality that is not supported by the vector or raster layers.
您可以在右侧的 **Layer Preview** 面板中实时预览您的地图图层。

You can preview your map layer live in the **Layer Preview** panel on the right.
创建或修改地图图层后,请始终点击 **Save** 以使该图层在 Map 应用程序中可用。

Always click **Save** after creating or modifying a map layer to make the layer available in the Map application.
## Vector layers
矢量图层显示来自 GeoJSON 或矢量切片源的图形数据。有四种方式可以指定数据源：

Vector layers display geometry data from GeoJSON or vector tile sources. There are four ways to specify a data source:
* **GeoJSON File：** 选择一个[手动上传的](/docs/foundry/compass/manually-upload-data/) GeoJSON 文件。

* **Dataset GeoJSON File：** 选择一个 dataset,然后选择该 dataset 中包含的 GeoJSON 文件。

* **GeoJSON URL：** 输入 GeoJSON 文件的 URL。

* **MVT URL：** 输入矢量切片集（vector tileset）的 URL。

* **GeoJSON File:** Select a [manually uploaded](/docs/foundry/compass/manually-upload-data/) GeoJSON file.
* **Dataset GeoJSON File:** Select a dataset, and then choose a GeoJSON file contained in that dataset.
* **GeoJSON URL:** Enter a URL for a GeoJSON file.
* **MVT URL:** Enter a URL for a vector tileset.
添加 source 后,您可以添加一个或多个 display 来配置数据在地图上的可视化方式。

After adding a source, you can add one or more displays to configure how your data is visualized on the map.
![Vector layer](/docs/resources/foundry/map/map-layer-editor-vector.png)
## Raster layers
Raster layer 显示来自 raster tileset 的位图数据。通过指定 tileset 的 URL 来配置 raster data source。

Raster layers display bitmap data from a raster tileset. Configure a raster data source by specifying the URL for the tileset.
![Raster layer](/docs/resources/foundry/map/map-layer-editor-raster.png)
raster layer 的可用 display 选项包括:

The available display options for raster layers are:
* **Opacity(不透明度):** 图层显示的不透明或透明程度。

* **Sampling(采样):** 当地图放大以至于 raster 图像必须被放大时所使用的插值方法。

* **Linear(线性):** 使用最接近的源像素的平均值进行插值,这在过度缩放时会导致模糊的外观。

* **Nearest(最近邻):** 通过选择最近的源像素进行插值,这在过度缩放时会产生清晰但有像素感的外观。

* **Zoom levels(缩放级别):** 显示该图层的最大和最小缩放级别。

* **Opacity:** How opaque or transparent to display the layer.
* **Sampling:** The interpolation method to use when the map is zoomed in such that the raster imagery must be scaled up.
* **Linear:** interpolates values using an average of the closest source pixels, which can result in a blurry appearance when overzoomed.
* **Nearest:** interpolates by selecting the nearest source pixel, which creates a sharp but pixelated appearance when overzoomed.
* **Zoom levels:** The maximum and minimum zoom levels at which to display the layer.
## Object layers
Object layer 直接从您的 Ontology 显示数据。只有同步到 OSS 或 OQL(已弃用)且具有 geopoint 或 geoshape property type 的 object type 才能通过 object layer 显示。

Object layers display data directly from your Ontology. Only object types that are synced to OSS or OQL (deprecated) and have a geopoint or geoshape property type can be displayed via object layers.
![Object layer](/docs/resources/foundry/map/map-layer-editor-objects.png)
> **ℹ️ 注意**

> 虽然 object layer 需要 OSS 或 OQL(已弃用),但并非所有实例都可用。有关更多信息,请联系您的 Palantir 代表。
> **ℹ️ 注意**

> Although OSS or OQL (deprecated) is required for object layers, it is not available on all instances. Contact your Palantir representative for more information.
Object layer 提供两种方式来指定您要渲染的数据:

Object layers provide two ways to specify the data you want to render:
* **Object type:** 选择一个 object type 并可选择性地定义 filters。所有匹配的对象将显示在您的地图 layer 中。

* **Saved object set:** 选择一个 [从 Object Explorer 保存的 exploration](/docs/foundry/object-explorer/save-explorations/)。该 layer 应用将显示保存在您的 exploration 中的所有对象。

* **Object type:** Select an object type and optionally define filters. All matching objects will display in your map layer.
* **Saved object set:** Select an [exploration saved from Object Explorer](/docs/foundry/object-explorer/save-explorations/). The layer app will display all objects that are present in your saved exploration.
Object layer display 的配置选项与 vector layer 相同。

The options for configuring object layer displays are the same as for vector layers.
## Mapbox JSON layers
对于 Mapbox JSON layer,您可以在 Map Layer Editor 中编辑 JSON 文档。编辑器会验证 JSON 并突出显示任何错误。

For Mapbox JSON layers, you can edit the JSON document in the Map Layer Editor. The editor validates the JSON and highlights any errors.
JSON 内容必须符合 [Mapbox GL JS Style Specification ↗](https://docs.mapbox.com/mapbox-gl-js/style-spec/),但仅支持 `sources` 和 `layers` properties(两者都是必需的)。

The JSON content must conform to the [Mapbox GL JS Style Specification ↗](https://docs.mapbox.com/mapbox-gl-js/style-spec/), but only the `sources` and `layers` properties are supported (and both are required).
![JSON layer](/docs/resources/foundry/map/map-layer-editor-json.png)