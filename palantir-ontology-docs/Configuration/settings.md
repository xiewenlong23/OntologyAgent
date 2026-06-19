<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/settings/
---
# Settings
选择 Map 屏幕右上角的设置齿轮图标 (![Gear icon](/docs/resources/foundry/map/settings-icon.png)) 打开设置菜单：

Choose the settings gear icon (![Gear icon](/docs/resources/foundry/map/settings-icon.png)) in the top right corner of the Map screen to open the settings menu:
![Map settings menu](/docs/resources/foundry/map/settings.png)
某些设置将受到通过 [Control Panel](/docs/foundry/map/control-panel/) 在组织范围内配置的内容的限制。

Some settings will be limited by what is configured organization-wide via [Control Panel](/docs/foundry/map/control-panel/).
## User settings
与您的用户相关联并适用于您打开的所有地图的设置。

Settings that are associated with your user and apply to all maps you open.
### Units
您可以指定显示距离所使用的单位。这是一项 per-user 设置，在您使用 Map 应用程序时将适用于您。单位选项包括：

You can specify the units in which distances are displayed. This is a per-user setting and is applied for you whenever you are using the Map application. The options for units are:
* Metric（公制）

* Imperial（英制）

* Nautical（航海制）

* Metric
* Imperial
* Nautical
### Enable GeoJSON panel
您可以在屏幕右下角启用一个额外的 GeoJSON 面板，该面板允许您输入和编辑 GeoJSON 数据，并根据 GeoJSON 几何图形创建 annotations。这是一项 per-user 设置，在您使用 Map 应用程序时将适用于您。

You can enable an additional GeoJSON panel in the bottom-right corner of the screen that allows you to enter and edit GeoJSON data, and create annotations based on the GeoJSON geometries. This is a per-user setting and is applied for you whenever you are using the Map application.
![GeoJSON panel](/docs/resources/foundry/map/geojson-panel.png)
## Map settings
按地图存储的设置。这些设置将在使用此特定保存的地图时应用于所有用户。

Settings that are stored per-map. These settings will apply for all users when using this specific saved map.
### Polling interval
您可以指定在 ["View Latest" 模式](/docs/foundry/map/time-overview/#selected-time-and-time-range) 下加载新时间序列和时间序列属性值的频率。

You can specify the frequency at which new time series and time series property values will be loaded when in ["View Latest" mode](/docs/foundry/map/time-overview/#selected-time-and-time-range).
### Time series buckets
您可以为每个轨迹指定要加载的点数。

You can specify the number of points to load for each track.
### Time zone
您可以指定用于显示地图的时区。时区选项包括：

You can specify the time zone in which to display the map. The options for time zone are:
* Local（将使用查看者计算机的时区）

* UTC
* Local (this will use the time zone of the viewer's computer)
* UTC
### Time format
用于显示地图的时间格式。

Time format in which to display the map.
* 12-hour
* 24-hour
* Local
* 12-hour
* 24-hour
* Local
请注意,如果时区设置为 UTC,则 24-hour 是唯一可用的时间格式。

Note that 24-hour is the only time format available if the time zone is set to UTC.
### Theme
在地图应用的 **Light** 和 **Dark** 模式之间切换。此设置不会更改底图为浅色或深色,仅更改地图应用程序的 UI。

Switch between **Light** and **Dark** mode for the map app. This setting does not change the base map to be light or dark, only the UI of the map application.
![Map with dark mode enabled.](/docs/resources/foundry/map/settings-dark-mode.png)
### Enable experimental labels
您可以启用一种用于在地图上显示和定位 [对象标签](/docs/foundry/map/visualize-objects/#labels) 的实验性方法。此方法应用一种定位算法,旨在尽量减少标签相互重叠或遮挡对象的情况。然而,在某些情况下（例如存在大量标签时）,最终的标签定位可能不理想,或者标签可能会以不理想或分散注意力的方式重新定位。这是按地图存储的设置,在使用此特定保存的地图时对所有用户生效。

You can enable an experimental method for displaying and positioning [objects labels](/docs/foundry/map/visualize-objects/#labels) on the map. This method applies a positioning algorithm that attempts to minimize instances of labels overlapping each other, or obscuring objects.  However, in some circumstances (such as with large numbers of labels) the resulting label positioning could be undesirable, or labels could reposition in undesirable or distracting ways. This is a per-map setting that applies for all users when using this specific saved map.