<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/vertex-settings-control-panel/
---
# Configure Vertex settings in Control Panel
可以使用 [Control Panel](/docs/foundry/administration/control-panel/) 配置各种组织范围的 Vertex 设置。要修改 Vertex 设置,您需要具有 `Vertex Admin` 角色。

Various organization-wide Vertex settings can be configured using [Control Panel](/docs/foundry/administration/control-panel/). To modify Vertex settings, you will need the `Vertex Admin` role.
![Vertex section in Control Panel](/docs/resources/foundry/vertex/control-panel-vertex.png)
## Graph defaults
* **Default time selection:** 默认时间选择跨越的天数。

* **Default graph mode:** 控制新创建的图表是使用 diagram mode \[beta] 还是 graph mode。

* **Active icon categories:** 控制 diagram mode \[beta] 中可访问的图标类别。

* **Default time selection:** The number of days that the default time selection spans.
* **Default graph mode:** Controls whether new graphs are created in diagram mode \[beta] or graph mode.
* **Active icon categories:** Controls which icon categories are accessible in diagram mode \[beta].
> **ℹ️ 注意: Beta**

> Diagram mode 处于 [beta](/docs/foundry/platform-overview/development-life-cycle/) 开发阶段,您的注册账户可能无法使用。功能在积极开发过程中可能会发生变化。要启用 diagram mode,请联系您的平台管理员在 Control Panel 中 [修改应用程序访问权限](/docs/foundry/administration/configure-application-access/)。
> **ℹ️ 注意: Beta**

> Diagram mode is in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development. To enable diagram mode, contact your platform administrator to [modify application access](/docs/foundry/administration/configure-application-access/) in Control Panel.
## Data loading
* **Time series polling interval:** Vertex 在实时模式下检查更新的时间序列值的频率（以秒为单位）。

* **Time series missing data warning:** 当时间序列没有最近的观测值时,Vertex 将显示警告。此设置控制显示警告之前,所选时间与最近的时间序列值之间允许的最长时间间隔（以小时为单位）。

* **Object search limits:** 控制用户从搜索对话框中可添加到图表的对象的最大数量。

* **Search around limits:** 控制通过 search around 将对象添加到图表的行为。

* **Maximum number of objects:** Vertex 作为单个 Search Around 结果加载的最大对象数。

* **Maximum number of ungrouped objects:** Vertex 将 search around 结果作为单个节点（而非组）添加到图表中的最大对象数。如果要添加到图表的对象超过此限制,则对象将被自动分组。

* **Template search around max depth:** 创建 template 时允许的嵌套 Search Around 的最大数量。

* **Time series polling interval:** How frequently (in seconds) Vertex will check for updated time series values when in live mode.
* **Time series missing data warning:** Vertex will display warnings when time series do not have recent observations. This setting controls the maximum period of time allowed (in hours) between the selected time and the nearest time series value before the warning will appear.
* **Object search limits:** Controls the maximum number of objects a user can add to a graph from the search dialog.
* **Search around limits:** Controls the behavior of adding objects to a graph via search arounds.
* **Maximum number of objects:** The maximum number of objects Vertex will load as a result of a single Search Around.
* **Maximum number of ungrouped objects:** The maximum number of objects resulting from a search around that Vertex will add to the graph as individual nodes, rather than groups. If more objects than this limit would be added to the graph, the objects will be automatically grouped.
* **Template search around max depth:** The maximum number of nested Search Arounds allowed when creating a template.
## Model configurations
* **Legacy model configuration:** 通过 Modeling objectives 应用程序可获得更新的模型配置体验。虽然仍将支持通过 Vertex 直接配置的模型,但不再建议在 Vertex 配置面板中配置新模型。

* **Model configuration mappings:** 选择模型配置者可用的数据类型映射。

* **Legacy model configuration:** An updated model configuration experience is available through the Modeling objectives application. While support for models configured directly through Vertex will remain, configuring new models in the Vertex configuration panel is now discouraged.
* **Model configuration mappings:** Select which types of data mappings are available to model configurers.