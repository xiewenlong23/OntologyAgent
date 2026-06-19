<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/explore-charts/
---
# Explore with charts
一旦选择了要探索的 object type，Explore 视角就会显示用于搜索和过滤的图表。

Once you have selected an object type to explore, the Explore perspective displays charts for search and filtering.
![New Exploration](/docs/resources/foundry/object-explorer/exploration_flights.png)
## Charts
Charts 是用户在 Object Explorer 中进行筛选时的主要交互点。每个 chart 代表对主 object type 或 linked object types 上某个 property 字段的聚合。默认情况下，所选 object type 上的每个突出 property 都会显示一个 chart；但是，用户可以自定义并[保存自己的默认布局](#saving-a-layout)，管理员也可以[为所有用户保存全局默认布局](/docs/foundry/object-explorer/configure/#default-layout-administrative-users)。

Charts are the main point of interaction for users filtering within Object Explorer. Each chart represents an aggregation of a property field on the main object type, or linked object types. By default, there will be one chart shown for each prominent property on the selected object type; however, users can customize and [save their own default layouts](#saving-a-layout), and administrators are able to [save global default layouts for all users](/docs/foundry/object-explorer/configure/#default-layout-administrative-users).
### Adding, Removing, and Ordering Charts
通过点击当前视图底部的 **Add chart** 卡片，可以向您的 exploration 添加一个 chart。这会打开一个搜索栏，用于在所选 object type 和 linked objects 上搜索 properties。选择要聚合的 property 后，chart 将出现在您的 exploration 中，并且 **Add chart** 卡片会向下移动一个位置。

Add a chart to your exploration by clicking the **Add chart** card at the bottom of your current view. This opens a search bar for properties on the selected object type and linked objects. After selecting a property to aggregate, the chart will appear on your exploration and the **Add chart** card shifts one position down.
此外，也可以通过 exploration 搜索栏中的筛选条件来添加 chart。在搜索栏中添加新筛选条件时，会出现一个 **Add chart to view** 按钮。选择此按钮会将 chart 添加到您 exploration 布局的第一个位置。

Alternatively, a chart can be added from filters in the exploration’s search bar. While adding a new filter in the search bar, an **Add chart to view** button will appear. Selecting this adds the chart to the first position in your exploration layout.

> 📷 **[图片: Adding a Chart]**

> 📷 **[图片: Adding a Chart]**

要移除一个 chart，请将鼠标悬停在 exploration 中该 chart 的标题上。会出现一个 **X** 图标：点击它会从您的视图中移除该 chart，但不会从您的搜索中移除任何筛选条件。

To remove a chart, hover over its header in your exploration. An **X** icon appears: clicking this removes the chart from your view but does not remove any filters from your search.

> 📷 **[图片: Removing a Chart]**

> 📷 **[图片: Removing a Chart]**

Charts 可以通过拖放重新排序和调整大小。在 chart 标题的空白处点击并按住，可显示用于重新排序 charts 的 interface。在布局中移动一个 chart 会使其他 charts 移动以填充其原本空出的空间。

Charts can be reordered and resized by dragging and dropping. Click and hold empty space in the chart header to show the interface for reordering charts. Moving a chart in your layout will shift the others to fill its now empty space.

> 📷 **[图片: Reordering Charts]**

> 📷 **[图片: Reordering Charts]**

要水平调整 chart 的大小，请点击并按住其边缘之一，然后拖动以缩小或扩大。每个 chart 可以填充 exploration 布局中一列或两列。

To resize a chart horizontally, click and hold on one of its edges and drag to shrink or expand it. Each chart can fill one or both of the columns in the exploration layout.

> 📷 **[图片: Resizing Horizontally]**

> 📷 **[图片: Resizing Horizontally]**

如果 Listogram chart 的值超过五个，点击 **Show more** 和 **Show less** 将垂直调整 chart 的大小。

If a Listogram chart has more than five values, clicking **Show more** and **Show less** will resize the chart vertically.

> 📷 **[图片: Resizing Vertically]**

> 📷 **[图片: Resizing Vertically]**

### Charts on Linked Objects
要针对 linked objects 的 properties 进行筛选，请从搜索菜单左侧选择一个 linked object type。

To filter on properties of linked objects, select a linked object type from the left hand side of the search menu.

> 📷 **[图片: add_linked_property.png]**

> 📷 **[图片: add_linked_property.png]**

在 exploration 视图中，chart 标题将表明它正在对 linked object 的 properties 进行筛选。在所附示例中，前两个 charts 对所选 type 的 properties 进行筛选，后两个 charts 则对 linked objects 的 properties 进行筛选。

In the exploration view, the chart header will indicate that it is filtering on the properties of a linked object. In the attached example the top two charts filter on the properties of the selected type, and the bottom two filter on properties of linked objects.

> 📷 **[图片: linked_property_charts.png]**

> 📷 **[图片: linked_property_charts.png]**

## Types of Charts
Object Explorer 支持多种图表类型以适配不同的 Property 类型。以下是每种类型的概述和示例。

Object Explorer supports several types of charts for different property types. Below is a summary and example of each type.
### Listogram
Listogram 显示非数值型 Property 的聚合结果。适用于 String、Boolean 和 Array 类型的 Property。在本示例中,图表列出了所有 Employee 的 First Name 以及具有该名字的 Employee 数量。

Listograms display aggregations on non-numeric properties. This applies to String, Boolean, and Array properties. In this example, the chart lists all First Names for Employees alongside the count of Employees with that first name.

> 📷 **[图片: listogram.png]**

> 📷 **[图片: listogram.png]**

Listogram 还可以显示带有数值型 Property 聚合的属性——例如,按州划分的每个业务 franchise 的平均收入。

Listograms can also display properties with aggregations of numeric properties - for example, the average revenue of each franchise of a business by state.
Listogram 的配置包括:

Configuration for a listogram includes:
* Aggregation 类型

* 例如,不是显示每个 airport 的 *flights *数量,而是显示 *flight time* 的 *average*

* Sort 类型和方向

* 例如,按数量升序排序,或按 Property 值按字母顺序排序

* Aggregation type
* For example, instead of showing the number of \*flights \*for each airport, show the \*average \*of *flight time*
* Sort type and direction
* For example, sort by the count ascending, or sort alphabetically by the property values

> 📷 **[图片: listogram_controls.png]**

> 📷 **[图片: listogram_controls.png]**

若要在 listogram 上进行筛选,点击您希望筛选的值。可以使用图表底部的下拉菜单来保留或排除所选的值。

To filter on a listogram, click on the values you would like to filter. Selected values can be kept or excluded by using the dropdown at the bottom of the chart.

> 📷 **[图片: listogram_select.png]**

> 📷 **[图片: listogram_select.png]**

### Pie Chart
非数值型 Property(布尔型和字符串型)也可以使用饼图(Pie Chart)进行展示。使用图表配置选项选择 **Pie Chart** 选项。

Non-numeric properties (booleans and strings) can also be displayed using pie charts. Select the **Pie Chart** option using the chart configuration options.

> 📷 **[图片: pie_chart.png]**

> 📷 **[图片: pie_chart.png]**

> 📷 **[图片: pie_chart_configuration.png]**

> 📷 **[图片: pie_chart_configuration.png]**

### Histogram
Histogram(直方图)显示数值型或日期型 Property 的柱状图聚合。

Histograms display bar chart aggregations on numeric or date properties.

> 📷 **[图片: histogram.png]**

> 📷 **[图片: histogram.png]**

直方图会自动缩放以适配所有相关数据，并自动分桶以便更轻松地进行选择，无需额外配置。要进行筛选，可以选择特定的桶（如左图所示），或点击并拖动以选择自定义范围（如右图所示）。使用图表底部的输入框编辑范围的起始点和结束点。

The histogram chart will scale to fit all relevant data and automatically bucket to allow for easier selection. No additional configuration is needed. To filter, either select a particular bucket (pictured left) or click and drag to select a range of your own choosing (pictured right). Edit the range’s start and end points with the inputs at the bottom of the chart.

> 📷 **[图片: histogram_select.png]**

> 📷 **[图片: histogram_select.png]**

### Grid Plots
网格图（Grid Plot）以颜色图形式展示两个 Property：X 轴上选定的 Property，以及 Y 轴上另一个 **Group By** Property。

Grid plots show color chart of two properties: The selected property on the X-Axis and another **Group By** property on the Y-Axis.

> 📷 **[图片: grid_plot.png]**

> 📷 **[图片: grid_plot.png]**

打开图表的配置以修改坐标轴、排序信息和颜色比例尺。

Open configuration for the chart to modify the axes, sort information, and color scale.

> 📷 **[图片: grid_plot_config.png]**

> 📷 **[图片: grid_plot_config.png]**

使用网格图（Grid Plot）进行筛选时，点击网格中的一个区域。按住 `ctrl` 或 `command` 键可点击连续范围内的多个选项。

To filter with a Grid Plot, click on a segment of the grid. Hold `ctrl` or `command` to click multiple options in a contiguous range.
### Single Statistic
Single Statistic 图表显示一组 Object 的某一个数值型 Property 的聚合值。选择一个 Property 和一种聚合类型（Sum、Average、Min、Max、Count 和 Unique Count）。此图表不可用于筛选。

Single Statistic charts show an aggregate value on one numerical property for a set of objects. Select a property and a type of aggregation (Sum, Average, Min, Max, Count and Unique Count). This chart cannot be used for filtering.

> 📷 **[图片: single_statistic.png]**

> 📷 **[图片: single_statistic.png]**

### Statistics Table
Statistics 表以可排序的表格形式显示按另一个 Property 分组的数值型 Property 的聚合值。可用的聚合包括 Sum、Min、Max、Average 和 Count。

Statistics tables show aggregates for numeric properties grouped by another property in a sortable table. Available aggregates are Sum, Min, Max, Average, and Count.

> 📷 **[图片: summary_statistics.png]**

> 📷 **[图片: summary_statistics.png]**

配置选项包括显示的 Metric、用于分组的 Property，以及在表格底部显示一个汇总行。

Configuration options include the metrics displayed, the property to group by, and displaying a summary row at the bottom of the table.
要进行筛选，请选择所需分组 Property 所在的行。

To filter, select the row of the desired group by property.
### Maps
**Cluster Map**
任何 **geopoint** 类型 Property 的默认图表是 Cluster Map，其中气泡按比例显示 Object 的数量或其他聚合的结果。

The default for any **geopoint** type property is a Cluster Map with scaled bubbles showing the number of objects, or the result of another aggregation.

> 📷 **[图片: Cluster Map]**

> 📷 **[图片: Cluster Map]**

配置选项包括更改执行的聚合类型，以及该聚合所基于的 Property（例如，不显示机场的数量，而是显示每个区域内出发航班的总和）。

Configuration options include the ability to change the type of aggregation performed, and which property that aggregation is on (e.g. instead of the count of airports, show the sum number of the departing flights within each area).

> 📷 **[图片: Cluster Map Options]**

> 📷 **[图片: Cluster Map Options]**

您可以通过点击这些气泡来按地理位置进行筛选，然后点击 3D 地图下方的 **apply filter**。

You can filter geospatially by clicking on these bubbles, and then clicking **apply filter** below the 3map.
**Choropleth Map**
**Choropleth Map**
某些在 Ontology 中已使用 typeclass 进行标注的 text Property 可用于创建如下所示的 choropleth map：

Some text properties that have been annotated with a typeclass in the ontology may be used to create a choropleth map that looks like the one 3below:

> 📷 **[图片: Choropleth Map]**

> 📷 **[图片: Choropleth Map]**

对于任何包含地理区域值（例如国家代码）且可以绘制在地图上的 Property 类型，都可以创建 choropleth。所需的 typeclass 的 `kind` 为 `choropleth_map_config_id`，`name` 则取决于该 Property 包含的区域代码类型。例如：

A choropleth can be created for any property type that contains values for geographic regions (e.g. country codes) that can be plotted on a map. The `kind` of the typeclass necessary is `choropleth_map_config_id`, and the `name` depends on what type of region code the property contains. For instance:
* 对于国家，使用 `countries`

* US States → `us_states`
* US Counties → `us_counties`
* US Zip Codes → `us_zip_codes`
* For countries, use `countries`
* US States → `us_states`
* US Counties → `us_counties`
* US Zip Codes → `us_zip_codes`
如需更多区域边界选项，或在添加此 typeclass 方面需要额外帮助，请联系您的 Palantir 代表。

For additional region boundary options, or additional assistance with adding this typeclass, contact your Palantir representative.
配置选项包括更改聚合类型以及所使用的色阶：

Configuration options include changing the type of aggregation as well as the color scale used:

> 📷 **[图片: Choropleth Map Configuration]**

> 📷 **[图片: Choropleth Map Configuration]**

## Undoing and redoing changes to your exploration
若要撤销或重做对 exploration 的更改，请使用 perspective bar 左侧的按钮。目前，最近 5 个 exploration 状态会被保存以供撤销和重做。可以撤销的操作包括：

To undo or redo a change to your exploration, use the buttons on the left side of the perspective bar. Currently, the last 5 exploration states are saved for undo and redo. Actions that can be undone are:
* 在搜索栏或从 chart 中编辑 filter

* 更改 charts 的布局（添加新 chart 或重新排序现有 chart）

* 更改 exploration perspective

* 将 exploration pivot 到一个 linked object type

* Editing a filter, either in the search bar or from a chart
* Changing the layout of your charts (adding a new one or reordering existing ones)
* Changing the exploration perspective
* Pivoting the exploration to a linked object type

> 📷 **[图片: Undo and Redo]**

> 📷 **[图片: Undo and Redo]**

## Saving a Layout
Layout 允许用户为特定 object type 创建可共享的视图。可共享视图包括已添加的 charts、table 的列配置，以及 table 的任何排序配置。

Layouts allow users to create shareable views for a specific object type. The shareable views include charts that have been added, column configurations for the table, and any sorting configuration for the table.
要保存一个 layout（布局），请点击屏幕左上角的 layout 选择器（**A**），然后选择 **Save current view (e.g. charts, sorts, etc.) as new layout**（**B**）。

To save a layout, open the layout selector in the top-left corner of the screen (**A**) and select **Save current view (e.g. charts, sorts, etc.) as new layout** (**B**).

> 📷 **[图片: Selecting a Layout]**

> 📷 **[图片: Selecting a Layout]**

在弹出的对话框中，设置 **Initial Perspective**（**C**），它控制 layout 初次打开时是显示 Explore tab（图表）还是 Results tab（表格）。你也可以通过勾选 **Set as default layout for** 下的 **For yourself**（**D**）复选框，将该 layout 设为当前 object type 的个人默认 layout，这意味着每当你开始一个新的 object type 探索时，该 layout 将被默认选中。

In the resulting pop-up, set the **Initial Perspective** (**C**), which controls whether the layout will initially open the Explore tab (the charts) or the Results tab (the table). You can also set the layout as your personal default layout for this object type by ticking the **For yourself** (**D**) box under **Set as default layout for**, which means that this layout will be selected by default whenever you start a new exploration on this object type.

> 📷 **[图片: Edit Layout]**

> 📷 **[图片: Edit Layout]**

如果你是一名 [administrative user](/docs/foundry/object-explorer/configure/#default-layout-administrative-users)，通过勾选 **Set as default layout for** 下的 **For all users** 复选框（**E**），你可以将一个 layout 设为所有用户的全局默认 layout。

If you are an [administrative user](/docs/foundry/object-explorer/configure/#default-layout-administrative-users), by ticking the **For all users** checkbox (**E**) under **Set as default layout for** you can set a layout as the global default layout for all users.
请注意，如果某个用户为某个 object type 设置了自己的默认 layout，则该 layout 将优先于任何已设置的全局默认 layout。

Note that if an individual user sets their own default layout for an object type, that layout will take precedence over any global default layout which has been set.
作为用户，你也可以使用下面显示的子菜单（**F**），将一个已有的 layout 设为指定 object type 的个人默认 layout：

As a user, you can also set an existing layout as your default for a specific object type by using the sub-menu shown below (**F**):

> 📷 **[图片: Setting your own default Layout]**

> 📷 **[图片: Setting your own default Layout]**

## Preview Panel
在探索视图的右侧，一个最多包含 20 条结果的列表会展示你当前探索内容的预览。

On the right-hand side of the exploration view, a list of up to 20 results shows a preview of your exploration’s contents.

> 📷 **[图片: Preview Table Sorting]**

> 📷 **[图片: Preview Table Sorting]**

点击预览卡片可以在 Object View tab 中打开该 object。要按单个 property 排序，请使用预览列表子标题中的 **Sort by** 选项。要按多个 property 排序，请将鼠标悬停在表头上并选择齿轮图标，如下图所示。这将打开一个对话框，用于配置按多个 property 排序，排序将按顺序应用。

Click a preview card to open the object in an Object View tab. To sort by a single property, use the **Sort by** option in the preview list subheader. To sort by multiple properties, hover over the header and select the gear icon, pictured here.This opens a dialog to configure sorts by many properties, which are then applied in order.