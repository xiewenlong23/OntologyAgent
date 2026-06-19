<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/integrate-actions/
---
# Ontology Actions
您可以在 Ontology 中配置用户可在 Map 应用程序中对地理空间 Objects 应用的 [Actions](/docs/foundry/action-types/overview/)。例如,这些 Actions 可以是根据在地图上选择的点、绘制的多边形或线来创建或编辑 objects。

You can configure [Actions](/docs/foundry/action-types/overview/) in the Ontology that users can apply to geospatial Objects in the Map application. For example, these Actions might be to create or edit objects based on points selected, polygons, or lines drawn on the map.
## Point Actions
当用户在地图上或某个 point object 上右键单击时,Actions 菜单将显示所有适用于地理空间 points 的 Ontology Actions。要定义一个适用于 points 的 Action,它需要具有以下任一条件:

When a user right-clicks on the map or on a point object, the Actions menu will show all Ontology Actions that apply to geospatial points. To define an Action that applies to points, it needs to have either:
* 一个 `String` 参数,其 type class 为:Kind: `geo` Value: `geopoint`(数据将是 `latitude,longitude` 形式的字符串),或者

* A `String` parameter with the type class: Kind: `geo` Value: `geopoint` (the data will be a string of `latitude,longitude`), or
![Geopoint Action parameter in the Ontology Manager](/docs/resources/foundry/map/integrate-actions-geopoint-param.png)
* 两个 `Double` 参数:

* 一个将传入 latitude,其 type class 为:Kind: `geo` Value: `latitude`,

* 另一个将传入 longitude,其 type class 为:Kind: `geo` Value: `longitude`。

* Two `Double` parameters:
* One that will be passed the latitude, with the type class: Kind: `geo` Value: `latitude`, and
* One that will be passed the longitude, with the type class: Kind: `geo` Value: `longitude`.
![Latitude Action parameter in the Ontology Manager](/docs/resources/foundry/map/integrate-actions-latitude-param.png)
![Longitude Action parameter in the Ontology Manager](/docs/resources/foundry/map/integrate-actions-longitude-param.png)
## Shape Actions
当用户选择多边形对象或在地图上绘制形状时,**Actions** 菜单将显示所有适用于地理空间形状的 Ontology Actions。若要定义一个适用于形状的 Action,该 Action 需要具有一个 `String` 参数,其 type class 为:Kind: `geo`,Value: `geojson`,其中数据将是一个 GeoJSON geometry 字符串。

When a user selects a polygon object or draws a shape on the map, the **Actions** menu will show all Ontology Actions that apply to geospatial shapes. To define an Action that applies to shapes, the Action needs to have a `String` parameter with the type class: Kind: `geo` and Value: `geojson`, where the data will be a GeoJSON geometry string.
![Geojson Action parameter in the Ontology Manager](/docs/resources/foundry/map/integrate-actions-geojson-param.png)
## Use actions to edit object `geoshape` properties
Actions 可以被配置为允许用户在地图上编辑对象的 `geoshape` property。用户可以选择对象,从 **Actions** 菜单中选择相关的 action,然后根据需要修改形状(例如,通过添加或移动点、进行缓冲区处理或平移形状)。

Actions can be configured to allow users to edit a `geoshape` property of an object on the map. A user can select the object, choose the relevant action from the **Actions** menu, and then modify the shape as necessary (for example, by adding or moving points, buffering, or translating the shape).
![Using a shape update action](/docs/resources/foundry/map/integrate-actions-applying-shape-update.gif)
若要配置一个 action 以允许用户在地图上编辑对象的 `geoshape` property,请为所需 Object Type 创建一个 "Modify object" action,并设置一个满足以下要求的参数:

To configure an action to allow users to edit a `geoshape` property of an object on the map, create a "Modify object" action for the desired object type with a parameter that fulfills the following requirements:
* 是一个 `String` 参数

* 映射到您希望更新的对象上的 `geoshape` property
* 默认值已禁用

* Type class 为:Kind: `geo`,Value: `geojson`

* Type class 为:Kind: `geo`,Value: `prefill`

* Is a `String` parameter
* Is mapped to the `geoshape` property on the object that you wish to update
* Has default value disabled
* With the type class: Kind: `geo`, Value: `geojson`
* With the type class: Kind: `geo`, Value: `prefill`
![Update shape action parameter in the Ontology Manager](/docs/resources/foundry/map/integrate-actions-oma-shape-param.png)
![Update shape action parameter typeclasses in the Ontology Manager](/docs/resources/foundry/map/integrate-actions-oma-shape-param-details.png)