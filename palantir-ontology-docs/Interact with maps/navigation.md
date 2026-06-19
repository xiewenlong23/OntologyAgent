<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/navigation/
---
# Navigation
Map 应用程序允许您对地图进行平移、缩放、旋转或倾斜，以便于查看和分析。您还可以使用快捷键快速居中地图，或使用 **Find（查找）** 面板在地图上定位 object、位置和坐标。

The Map application allows you to pan, zoom, rotate, or tilt maps to facilitate viewing and analysis. You can also use shortcuts to quickly center the map or use the **Find** panel to locate objects, locations, and coordinates on a map.
## Basic map controls
* 要平移，可在地图视口上单击并拖动，或使用键盘上的箭头键。
* 要缩放，可使用以下方法之一：

* 左下角的 **Zoom in（放大）** 和 **Zoom out（缩小）** 按钮
* 鼠标滚轮
* 键盘上的 **+** 和 **-** 键

* 要旋转和倾斜地图，可在按住 Ctrl（Windows）或 Cmd（macOS）的同时单击并拖动。

* To pan, click and drag on the map viewport, or use the arrow keys on your keyboard.
* To zoom, use one of the following:
* The **Zoom in** and **Zoom out** buttons in the bottom left
* The mouse wheel
* The **+** and **-** keys on your keyboard
* To rotate and tilt the map, click and drag while holding Ctrl (Windows) or Cmd (macOS).
## Center the map on items
按键盘上的 **0** 键，地图将导航以显示您所选的对象。如果您没有所选对象，**0** 将导航地图以显示地图上的所有对象。

Press **0** on your keyboard to navigate the map to display your selected objects. If you have no selected objects, **0** will navigate the map such that all objects on the map can be displayed.
## Use the Find panel
**Find（查找）** 面板允许您导航至已添加到地图的 object，以及位置和坐标。

The **Find** panel allows you to navigate to objects that have been added to your map, as well as locations and coordinates.
### Find objects on map
选择 **Objects on map（地图上的对象）** 选项卡，并输入搜索查询以按标题或 property 值查找 object。选择某个结果后，地图将导航至该 object。

Select the **Objects on map** tab, and enter a search query to find objects by title or property values. Selecting a result
will navigate the map to that object.

> 📷 **[图片: Object results.]**

> 📷 **[图片: Object results.]**

### Find locations
> **ℹ️ 注意: 需要 API 密钥**

> 您的组织必须已在 [Control Panel 中的 Mapbox API 密钥](/docs/foundry/map/control-panel/#api-keys) 中进行配置，才能使用此功能。
> **ℹ️ 注意: API Key Required**

> Your organization must have configured a [Mapbox API Key in Control Panel](/docs/foundry/map/control-panel/#api-keys) for this feature to be available.
选择 **Locations（位置）** 选项卡，并输入查询以按地址或名称查找位置。选择某个结果后，地图将导航至该位置，并显示一个带有该位置地址的标记。您可以通过单击结果列表中地址旁边的 **eye（眼睛）** 图标来隐藏该标记。

Select the **Locations** tab and enter a query to find locations by their address or name. Selecting a result will navigate the map to that location and show a marker with the location's address. You can hide the marker by clicking the **eye** icon next to the address in the results list.
![Location results](/docs/resources/foundry/map/navigation-location-results.png)
### Navigate to Coordinates
在选中 **Objects on map（地图上的对象）** 或 **Locations（位置）** 选项卡的情况下，您可以在搜索输入框中输入坐标，并通过选择结果将地图导航至该坐标。使用 **Show coordinates（显示坐标）** 按钮将在您指定的坐标处添加一个文本标注。

With either the **Objects on map** or **Locations** tab selected, you can enter coordinates in the search input and navigate your map to them by selecting the result. Using the **Show coordinates** button will add a text annotation at your specified coordinates.
![Go to coordinates](/docs/resources/foundry/map/navigation-coordinates.png)