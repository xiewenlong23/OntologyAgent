<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/control-panel/
---
# Control Panel
可以使用 [Control Panel](/docs/foundry/administration/control-panel/) 配置各种组织范围内的 Map 设置。要修改 Map 设置，您需要具有 `Map Admin` 角色。

Various organization-wide Map settings can be configured using the [Control Panel](/docs/foundry/administration/control-panel/). To modify Map settings, you will need the `Map Admin` role.
![Map section in Control Panel.](/docs/resources/foundry/map/control-panel-map-defaults.png)
某些组织级别的设置，用户可以在 [settings menu](/docs/foundry/map/settings/) 中按用户或 Map 级别进行覆盖。

Some organization-level settings users will be able to override on a user or map level in the [settings menu](/docs/foundry/map/settings/).
## Map Defaults
* **Default viewport**（默认视口）定义了用户创建新地图时将看到的初始视图，包括中心点（纬度和经度）和缩放级别。

* **Default time selection**（默认时间选择）定义了在选择时间范围时将向用户显示的日期选项范围。

* **Default unit system**（默认单位制）为所有用户和/或特定用户组设置不同的单位制（公制、英制或航海制）。用户可以在 [map settings](/docs/foundry/map/settings/) 中覆盖此默认设置。

* **Default viewport** defines the initial view, in terms of the center point (latitude and longitude) and zoom level, that a user will see when creating a new map.
* **Default time selection** defines the range of date options that will be shown to users when selecting the time range.
* **Default unit system** sets the different units system (metric, imperial, or nautical), for all users and/or specific users groups. Users can override this default in the [map settings](/docs/foundry/map/settings/).
## Data loading
* **Time series polling interval**（时间序列轮询间隔）：定义在 ["View Latest" mode](/docs/foundry/map/time-overview/#selected-time-and-time-range) 下，地图检查时间序列数据更新的频率。

* **Default polling interval**（默认轮询间隔）：为新地图设置默认轮询间隔（以秒为单位）。用户可以在地图内覆盖此设置。

* **Minimum allowed polling interval**（允许的最小轮询间隔）：设置可覆盖的最小轮询间隔（以秒为单位）。用户无法在单个地图上设置小于此值的轮询间隔。

* **Time series points**（时间序列点）：定义每个轨道要加载的点数。

* **Default time series point count**（默认时间序列点数）：要加载的默认点数。

* **Maximum number of points**（最大点数）：用户在单个地图上覆盖默认计数时可指定加载的最大点数。

* **Object search limits**（对象搜索限制）：控制用户从搜索对话框添加到地图的最大对象数量。

* **Search around limits**（Search Around 限制）：控制用户通过单次 Search Around 添加到地图的最大对象数量。

* **Automatic object search**（自动对象搜索）：控制对象搜索结果是在输入时自动加载，还是需要手动触发。

* **Time series polling interval:** Define how frequently the map will check for updated time series data when in ["View Latest" mode](/docs/foundry/map/time-overview/#selected-time-and-time-range).
* **Default polling interval:** Set the default polling interval (in seconds) for new maps. Users can override this setting within the map.
* **Minimum allowed polling interval:** Set the minimum allowable polling interval override (in seconds). Users are prevented from setting a polling interval smaller than this value for individual maps.
* **Time series points:** Define how many points to load for each track.
* **Default time series point count:** The default number of points to load.
* **Maximum number of points:** The highest number of points a user can specify to load when overriding the default count on an individual map.
* **Object search limits:** Control the maximum number of objects a user can add to a map from the search dialog.
* **Search around limits:** Control the maximum number of objects a user can add to a map as the result of a single Search Around.
* **Automatic object search:** Controls whether object search results load automatically as you type or require manual triggering.
## API Keys
### Mapbox: Enable Find Locations on map
[Find Locations](/docs/foundry/map/navigation/#find-locations) 功能使用 Mapbox 的专有地理编码服务。要为您的组织启用此功能，您需要配置一个特定于组织的 Mapbox API key，该 key 需包含对 Mapbox Geocoding API 的访问权限。

The [Find Locations](/docs/foundry/map/navigation/#find-locations) feature uses a proprietary geocoding service from Mapbox. To enable this feature for your organization, you will need to configure an organization-specific Mapbox API key that includes access to the Mapbox Geocoding API.
### Bing Maps: Enable Bing Maps base layers
要使用 Bing Maps 底图代替默认的 Mapbox 底图，请输入 Bing Maps API key。

To use Bing Maps base layers, instead of the default Mapbox base layers, enter a Bing Maps API key.
## Base maps
### Enable Mapbox base maps
当 Mapbox styles 被禁用时，Foundry 平台中的地图应用和 widget 将默认使用第一个自定义底图。

When Mapbox styles are disabled, map applications and widgets in the Foundry platform will use the first custom base map by default.
### Custom base map
使用 Raster tiles 或 Mapbox JSON 添加自定义底图。

Add a custom base map using either Raster tiles or Mapbox JSON.
![Custom base map configuration panel.](/docs/resources/foundry/map/control-panel-custom-base-map.png)
### Watermark configurations
Watermarks 可以配置为默认设置或按组配置。Watermark 将叠加在底图之上。

Watermarks can be configured as a default or per group. The watermark will overlay on the base map.
![An example map with a watermark reading "demo".](/docs/resources/foundry/map/control-panel-watermark.png)