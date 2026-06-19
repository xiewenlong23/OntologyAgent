<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/widgets-visualization/
---
# Visualization
**Visualization widgets** 以图表、pivot tables、timelines、maps 和其他可视化形式（包括简单的文本和 metrics）显示与当前 object 相关的数据。在其他 Foundry apps 中创建的可视化也可以嵌入 - 请参阅 [Apps and Files](/docs/foundry/object-views/widgets-apps-files/) 类别以了解有关嵌入 Slate applications、Contour boards、Foundry reports、Fusion spreadsheets 以及 Quiver time series 或 charts 的更多信息。

**Visualization widgets** display data related to the current object in charts, pivot tables, timelines, maps, and other visualizations, including simple text and metrics.
Visualizations created in other Foundry apps can be embedded as well - see the [Apps and Files](/docs/foundry/object-views/widgets-apps-files/) category to learn more about embedding Slate applications, Contour boards, Foundry reports, Fusion spreadsheets, and Quiver time series or charts.
## Linked Object View
此 widget 主要用于显示某种类型的所有 Linked Objects 的 *table* 视图及其相关 properties。该 table 还支持选择 linked objects 的子集以在其他 Foundry apps 中打开或执行已配置的 Object Actions。

除了 table 视图之外，还提供简单的 list 视图和 card 视图。

This widget is mainly used to display a *table* view of all Linked Objects of a certain type along with their relevant properties. The table also supports selection of subset of linked objects to open in other Foundry apps or perform configured Object Actions.
In addition to a table view, a simple list view and a card view are also available.
Linked Object View (Table) 不带 Filter Sidebar 和带 Filter Sidebar 的示例：

Example for Linked Object View (Table) without a Filter Sidebar, and with a Filter Sidebar:
![Linked Object View Table without filter sidebar](/docs/resources/foundry/object-views/widgets_linked-object-view-without-sidebar.png)
![Linked Object View Table with Filter sidebar](/docs/resources/foundry/object-views/widgets_linked-object-view-with-sidebar.png)
### Configuration
#### Settings tab
该配置包含 3 个部分：

The configuration has 3 parts:
* Data
* *Linked Object to display*：选择您希望显示的 Linked Object。该 widget 配置提供与当前对象链接的对象，这些对象在 [Ontology configuration](/docs/foundry/object-link-types/create-link-type/) 中定义。通过直接链接或通过中间对象类型的传递性链接来选择对象类型。

* *Properties to display*：
* All Properties - 显示所有定义为 Prominent 或 Normal 的 Property，但不显示 Hidden 的 Property。允许使用 `Properties to Exclude` 选择器（见下文）排除特定的一组 Property。

* Prominent Properties - 仅显示在 Ontology Manager 中定义为 Prominent 的 Property。允许使用 `properties to exclude` 选择器（见下文）排除特定的一组 Property。

* Specific Properties - 打开一个多选下拉菜单，其中包含该 Linked Object 的所有 Property，以供选择。

* No Properties - 不显示任何 Property。

* *Properties to Exclude*：选择您希望从显示中排除的 Property。适用于 **All Properties** 和 **Prominent Properties** 选项。

* View Options - 选择默认显示给最终用户的视图类型。最终用户仍可以在 UI 中（在 widget 标题栏上）切换到其他 2 个视图。

* Table view - 最常用的视图，显示包含所有值的表格，并带有快速筛选搜索功能。

* Card view - 每个 Linked Object 的精简卡片视图，包含 Property（如 1b 中所选）。此选项不具备 Table view 的全部功能。例如，它不支持选择或 Object Actions。

* 注意：对于 Card 显示选项，有一个名为 "Card Width" 的次级配置，用于确定这些卡片的视觉密度。它对 Table 或 List view 选项没有影响。

* List view - 所选 Linked Object 的所有实例的简单列表视图，没有任何选择选项或链接 Property 的显示。

* Search and Filtering - 为 Table view 添加搜索和筛选功能

* Results limit - 限制显示的最大结果数。您希望显示的结果越多，视图加载所需的时间就越长。这与最小/最大高度配置（见下文 Format 选项卡）一起决定此 widget 将占用整个视图的多少空间。

* Enable search and filtering - 打开以在 widget 上启用搜索和筛选功能。这包括基本或高级搜索功能：

* Basic - 在 widget 标题栏上提供一个用于自由文本搜索的简单搜索栏。

* Advanced - 提供一个完整的筛选侧边栏，包含详细的筛选选项，包括一个切换按钮，用于设置默认向最终用户展开或折叠侧边栏。与基本的自由文本搜索不同，此搜索允许根据 Property 类型进行更复杂的筛选（字符串的自由文本和多选、时间戳的日期范围、双精度/整数的数值）。此搜索栏基于旧版 Object Explorer 功能和 UI。

* Data
* *Linked Object to display*: Select the Linked Object you wish to display. The widget configuration offers objects that are linked to the current object as defined in the [Ontology configuration](/docs/foundry/object-link-types/create-link-type/). Choose either an object type either via a direct link or through a transitive link using an intermediate object type.
* *Properties to display*:
* All Properties - display all properties that are defined as Prominent or Normal, but no Hidden properties. Allows excluding a specific set of properties using the `Properties to Exclude` selector (see below).
* Prominent Properties - display only the properties defined as Prominent in the Ontology Manager. Allows exclusion of a specific set of properties using the `properties to exclude` selector (see below).
* Specific Properties - opens a multi-select dropdown with all properties of that Linked Object, to select between.
* No Properties - do not display any property.
* *Properties to Exclude*: select which properties you wish to exclude from display. Available for **All Properties** and **Prominent Properties** options.
* View Options - choose which view type will be displayed to the end-user by default. The end-user can still change to the other 2 views in the UI (on the widget header).
* Table view - the most commonly used view, displays a table of all values, with quick filter search.
* Card view - a condensed cards view of each Linked Object, with properties (as selected on 1b). This option does not have the full functionality of the table view. For example, it does not support selection or Object Actions.
* Note: For the Card display option, there is a secondary configuration called “Card Width” which determines the visual density of these cards. It has no effect for the Table or List view options.
* List view - a simple list view of all instances of the chosen Linked Object, without any option of selection or any display of linked properties.
* Search and Filtering - add search and filtering capabilities to the table view
* Results limit - limit the maximum number of results to be shown. The more results you wish to display, the longer it would take the view to load. This, together with the minimum/maximum height configuration (see below on the Format tab) determine how much of the entire view this widget would take.
* Enable search and filtering - toggle on to have search and filtering functionality on the widget. This includes either basic or advanced search functionality:
* Basic - have a simple search bar for free text searches at widget header.
* Advanced - have a full filter sidebar with detailed filtering options, including a toggle to expand or collapse the sidebar by default to end-users. Unlike the basic free-text search, this search allows more complex filtering based on property type (free-text and multi-select for strings, date range for timestamps, numeric for double/integer). This search bar is based on the legacy Object Explorer functionality and UI.
**Format tab:**
在 widget 配置中的 Format 选项卡下，除了 Title、Icon、Info 和 Layout 的默认值之外，您还可以控制该部分的最小和最大高度（可选）。

Under the format tab within the widget configuration, aside from defaults of Title, Icon, Info and Layout, you can control the minimum and maximum height of the section (optional).
**常见问题和注意事项：**

**Common Issues and Notes:**
* 此 widget 受其他 widget 的 *filters 影响*（如果切换开关打开），但 *不会向与其共享交叉筛选的其他 widget 发布 filter*，即使筛选侧边栏处于打开状态。实际上，内部 filter 仅限于 object table widget 的上下文内。

* Conditional Formatting 和 Value Renderers - 表格中的值可以使用 Conditional Formatting 和 Value Renderer 进行渲染。

* This widget is *affected by filters* from other widgets - if the toggle is on - but *does not publish filters* to other widgets sharing cross-filtering with it, even if the filter sidebar is open. In effect, internal filters are limited to the context of the object table widget.
* Conditional Formatting and Value Renderers - Values in the table can be rendered with conditional formatting and value renderers.
## Timeline
创建一个按时间顺序排列的事件列表，自上而下显示，按日期和时间排序。此时间线由必须至少具有一个 timestamp 的 Linked Object 组成，通常是事件，即具有定义某个持续时间的开始和结束 timestamp 的对象。

此 widget 可以包含直接链接到当前对象或通过 Linked Object 链接到当前对象的一种或多种对象类型。它还可以按不同的日期 Property 显示同一事件，如下例所示。

Create a chronological list of events, displayed top-down, sorted by date and time. This timeline is built of linked objects that must have at least one timestamp, and are usually events, that is an object with a start and end timestamp that define some duration.
This widget can include one or more types of objects linked to the current object directly, or through a linked object. It can also display the same event by different date properties as in the examples below.
对于图形时间线，请使用 [Grouped Events Timeline and Table](#grouped-events-timeline-and-table) widget。

For a graph timeline, use the [Grouped Events Timeline and Table](#grouped-events-timeline-and-table) widget.
![Timeline](/docs/resources/foundry/object-views/widgets_timeline.png)
### Configuration
#### Settings tab
* **添加一个或多个 Linked Object（事件）** - 首先，通过单击 "Add Event Type" 添加至少一个您希望显示在时间线上的 Linked object type。您可以添加多种 Linked Object 类型：

* 在时间线上显示完全不同的不同事件的对象类型。示例：链接到 Aircraft 的 Linked Object，既包括 Flights 事件，也包括 Aircraft Maintenance 事件。

* 显示同一 Linked Object 类型的事件，但通过不同的日期 Property 或不同类型的 Link 定义来显示。示例：

* 链接到 Airport 对象的 Flights 事件，通过不同的日期 Property 显示在同一时间线上：(1) "Planned Arrival Time"，(2) "Actual Arrival Time"，(3) "Expected Departure Time"。在这种情况下，时间线将按时间顺序显示所有航班，每个航班最多出现 3 次。

* 一个 Airport 对象可以同时具有链接到它的 Arriving Flights 和 Departing Flights，并显示在同一时间线上。
* **选择您希望添加的事件对象的类型** - 对于您希望添加的每个事件对象，配置该对象类型的详细信息：

* 选择 Linked Object 类型 - 直接 Linked Object 或 Extended Link。

* 直接 Linked Object 的示例：当前对象是 Airport，您希望显示 Arriving Flights 和 Departing Flights 的时间线。

* Extended object（二级）的示例：当前对象是 Airport，您希望显示一个时间线，其中包含链接到 Airport 的 Arriving Flights 所链接的所有 Aircraft 对象。

* **定义用于在时间线上对事件进行排序的日期 Property** - 选择您希望用于在时间线上对事件进行排序的 Linked Object 的 Property。此 Property 必须是 timestamp/date，因此配置仅建议此类 Property。

* **选择要从 Linked Object 显示的 Property**。

* 选择您希望显示的 Property：

* All Properties - 如果 Linked Object 具有许多 Property，则不建议使用，因为它会使时间线变得拥挤且难以浏览。

* Prominent Properties - 仅显示在 Ontology Manager 中定义为 Prominent 的 Property。

* Specific Properties - 打开一个多选下拉菜单，其中包含该 Linked Object 的所有 Property，以供选择。

* No Properties - 时间线上将仅显示 Linked Object 的标题。

* 选择您希望排除的 Property - 仅适用于 All Properties 和 Prominent Properties 的前两个选项。
* **选择要为时间线上的每个事件显示的标题**。有三个选项：

* **Object Name** 作为标题（例如，事件的名称） - 这是最常用的选项，也是默认选项。

* **Date Property name** 作为标题 - 如果您希望使用多个 Property 显示 Linked Object 的事件（例如 "Planned Arrival Time"、"Actual Arrival Time"、"Expected Departure Time" 等），此选项非常有用。提醒：在这种情况下，基于不同 Property 的每个 link 应在 Timeline widget 内单独配置 - 请参阅上文要点 1）。

* **Custom Name** - 为该类型的所有 Linked Object 添加自由文本描述的选项。例如，如果您在同一时间线中链接 Arriving Flights 和 Departing Flights，则可能希望使用标题 "Arrival" 描述所有 Arriving Flights，并使用 "Departure" 描述所有 Departing Flights。

* **Add one or more Linked Objects (event)** - First, add at least one Linked object type that you wish to display on the timeline by clicking on “Add Event Type”. You can add many types of Linked Objects:
* Display different object types on the timeline, that are completely different events. Example: Linked Objects to an Aircraft that are both Flights events and Aircraft Maintenance events.
* Display events of the same Linked Object type, but by different date properties, or with different types of Links defined. Examples:
* Flight events linked to an Airport object displayed on the same timeline by different date properties: (1) “Planned Arrival Time”, (2) “Actual Arrival Time”, (3) “Expected Departure Time”. The timeline will display a chronological list of all flights, and each flight will appear up to 3 times in this case.
* An Airport object can have both Arriving Flights as well as Departing Flights that are linked to it displayed on the same timeline.
* **Select the type of event object you wish to add** - for each event object you wish to add, configure the details of that object type:
* Select a linked object type - either directly Linked Object or an Extended Link.
* Example of a directly Linked Object: current object is an Airport and you want to display a timeline of Arriving Flights and Departing Flights.
* Example of an Extended object (2nd degree): current object is an Airport, and you want to display a timeline with all Aircraft objects that are linked to Arriving Flights linked to the Airport.
* **Define the date property used to sort events on the timeline** - select the property of the Linked Object you wish to sort the events on your timeline by. This property has to be a timestamp / date, so the configuration only suggests such properties.
* **Select which properties to display from the Linked Object**.
* Select what properties you wish to display:
* All Properties - not recommended if the Linked Object has many properties, as it would be crowded and hard to navigate through the timeline.
* Prominent Properties - only the properties defined as Prominent in the Ontology Manager.
* Specific Properties - opens a multi-select dropdown with all properties of that Linked Object, to select between.
* No Properties - only the title of the Linked Object would be displayed on the timeline.
* Select which properties you wish to exclude - only available for the first two options of All Properties and Prominent Properties.
* **Select which title would be displayed** for each event on your timeline. There are three options:
* **Object Name** as title (e.g. name of the event) - this is the most commonly used option and the default.
* **Date Property name** as title - this is useful if you wish to display events from a Linked Object using more than one property (e.g. “Planned Arrival Time”, “Actual Arrival Time”, “Expected Departure Time”, etc.). Reminder: in such a case, each link based on a different property, should be configured separately within the Timeline widget - see bullet 1 above).
* **Custom Name** - an option to add a free-text description for all Linked Objects of that type. E.g. if you link both Arriving Flights and Departing Flights under the same timeline, you may want to describe all Arriving Flights with the title “Arrival” and all Departing Flights with “Departure”.
#### Format tab
在 widget 配置中的 Format 选项卡下，除了 Title、Icon、Info 和 Layout 的默认值之外，您还可以控制该部分的最小和最大高度（可选）。

Under the format tab within the widget configuration, aside from defaults of Title, Icon, Info and Layout, you can control the minimum and maximum height of the section (optional).
### Common issues and notes
* 此 widget 可搜索和排序（从最早到最新）。但是，它不支持 filtering，因此不受 filter 影响。对于 filtering 功能，请考虑使用 [Grouped Events Timeline and Table](#grouped-events-timeline-and-table) widget。

* 如果您希望在图形时间线上显示事件（而不仅仅是按时间顺序排列的列表），请考虑使用 [Grouped Events Timeline and Table](#grouped-events-timeline-and-table) widget。

* 如果您希望显示甘特图样式的时间线，则有一个 "Linked Objects Gantt Chart" widget。如果此 widget 不可用，请联系您的 Palantir 代表以获取更多详细信息。这对于显示数量较少、具有明确开始和结束日期的事件（例如项目时间线）是相关的。

* 对于 Timeseries 可视化，请联系您的 Palantir 团队以获取有关 Quiver 的更多详细信息，它可以嵌入到 Object View 中。您还可以使用 Charts widget（或嵌入来自 Contour 或 Quiver 的图表），在 X 轴上使用日期/时间 Property。
* 缺少日期的事件将不会显示在事件列表中。将出现一条消息，提醒用户有关缺失事件的信息。

* 出于性能原因，默认情况下仅显示 50 个 Linked Object。当用户向下滚动列表时，将每批 100 个显示更多对象。

* This widget is searchable and sortable (oldest first, newest first). However, it doesn't support filtering, so it is not affected by filters. For filtering functionality, consider using the [Grouped Events Timeline and Table](#grouped-events-timeline-and-table) widget.
* If you wish to display events on a graphic timeline (and not just be a chronological list), consider using the [Grouped Events Timeline and Table](#grouped-events-timeline-and-table) widget.
* If you wish to display a Gantt chart style timeline, there is a “Linked Objects Gantt Chart” widget. If this is not available, contact your Palantir representative for more details. This is relevant for displaying a smaller number of events, with distinct start and end dates, such as a project timeline.
* For Timeseries visualizations, contact your Palantir team for more details about Quiver, which can be embedded in an Object View. You can also use Charts widgets (or embed charts from Contour or Quiver charts), with a date/time property on the X-axis.
* Events with missing dates will not be displayed on the events list. There will be a message alerting the user about missing events.
* For performance reasons, only 50 Linked Objects are displayed by default. As the user scrolls down through the list, additional objects will appear, 100 at a time.
## Grouped Events Timeline and Table
此 widget 包括两个组件：(1) Linked Object 的时间线，以及 (2) 下方列出的 Linked Object 表格。Linked object 可以按 Property 分组，并按文本、日期范围和外部 filter 进行筛选。

This widget includes two components: (1) a timeline of Linked Objects, and (2) a table listing the Linked Objects underneath. Linked objects can be grouped by properties and filtered by text, date range and external filters.
分组事件绘制在不同的平行线上，每条线仅包含具有某个 Property 特定值的事件，类似于 pivot table。在下面的示例中，每个城市都有一条不同的线，该线上包含该城市的所有到达（红色）或出发（蓝色）的航班。

Grouped events are plotted on separate parallel lines, with each line including only events that have a property with a certain value, similar to a pivot table. In the example below, each city has a different line, with all flights that are arriving (red) or departing (blue) from that city on that line.
此 widget 可以包含直接链接到当前对象或通过 Linked Object 链接到当前对象的一种或多种对象类型。它还可以按不同的日期 Property 显示同一事件（示例如下）。

This widget can include one or more types of objects linked to the current object directly, or through a linked object. It can also display the same event by different date properties (examples below).
![Grouped Events Timeline and Table](/docs/resources/foundry/object-views/widgets_hu-grouped-events-table.gif)
### Configuration
#### Settings
* **添加一个或多个 Linked Object（事件）** - 首先，通过单击 "Add Item" 添加至少一个您希望显示在时间线上的 Linked Object Type。您可以添加多种 Linked Object 类型：

* 在时间线上显示完全不同的不同事件的对象类型。示例：链接到 Aircraft 的 Linked Object，既包括 Flights 事件，也包括 Maintenance 事件。

* 显示同一 Linked Object 类型的事件，但通过不同的日期 Property 或不同类型的 Link 定义来显示。示例：

* 链接到 Airport 对象的 Flights 事件，通过不同的日期 Property 显示在同一时间线上：(1) "Planned Arrival Time"，(2) "Actual Arrival Time"，(3) "Expected Departure Time"。在这种情况下，每个航班最多出现 3 次。

* 一个 Airport 对象可以同时具有链接到它的 Arriving Flights 和 Departing Flights，并显示在同一时间线上。
* **选择您希望添加的事件对象的类型** - 对于您希望添加的每个事件对象，配置该对象类型的详细信息：

* 选择 Linked Object - 直接 Linked Object 或 Extended Link。

* 直接 Linked Object 的示例：当前对象是 Airport，您希望显示 Arriving Flights 和 Departing Flights 的时间线。

* Extended object（二级）的示例：当前对象是 Airport，您希望显示一个时间线，其中包含链接到 Airport 的 Arriving Flights 所链接的所有 Aircraft 对象。
* **配置可视化格式选项**

* Max Number of Events - 此选项当前不起作用。

* Color - 为此 item 配置下的所有事件选择颜色。使用 [Blueprint standard colors ↗](https://blueprintjs.com/docs/#core/colors) 或基本颜色名称 - "Blue"、"Red"、"Yellow" 等。

* Series Name - 此时间线下所有事件的描述，将显示在图形时间线的图例上。

* **定义用于在时间线上对事件进行排序的日期 Property** - 选择要用于在时间线上显示事件的 Linked Object 的 Property。此 Property 必须是 timestamp/date，因此配置仅建议此类 Property。

* **Group Events By** - 选择如何在图形时间线上对事件进行分组。每个分组将作为图形时间线中单独的一条水平事件线显示，并依次堆叠在一起。有两个选项：

* Constant - 当前 item 将分组在单个时间线上，标题定义为自由文本值。在这种情况下，如果您希望添加其他时间线作为单独的线，则必须定义其他 item。

* Property - 将事件拆分为多个单独的时间线，每个时间线上的事件根据该 Property 的不同值进行分组。

* 示例：显示 Airport 对象的所有 Arriving Flights 的时间线，可以选择 "Airline Name" Property，并为每个 Airline 创建一个单独的时间线，其中该 Airline 的所有航班都位于其专用时间线上。下面的列表将包含来自所有 Airline 的所有 Flights 事件的按时间顺序排列的列表。

* **Properties Displayed in List** - 选择您希望显示在 widget 第二部分（List）中的 Property：

* 选择您希望显示的 Property：

* All Properties - 如果 Linked Object 具有许多 Property，则不建议使用，因为它会使时间线变得拥挤且难以浏览。

* Prominent Properties - 仅显示在 Ontology Manager 中定义为 Prominent 的 Property。

* Specific Properties - 打开一个多选下拉菜单，其中包含该 Linked Object 的所有 Property。选择要显示的特定 Property。

* No Properties - 时间线上仅显示 Linked Object 的标题。

* Property Filter - 一个可选的切换开关，用于添加基于单个 Property 的 filter，以仅包含特定的值。这些值必须显式输入为区分大小写的自由文本字符串。
* 图形时间线的其他配置（这些仅适用于时间线组件，对表格组件没有影响）

* **Groups Displayed by Default** - 应该作为时间线中的单独线条显示的时间线数量或具体线条。在这两种情况下，用户都可以使用包含所有其他分组的 multi-select helper。

* Max Number - 图形时间线中显示的不同分组和不同时间线的最大数量，以数字（Value）表示。

* Explicit List - 编写要显示的分组的精确值列表（文本，区分大小写）。

* **Sort Groups By** - 时间线可以具有多条水平线，这允许您通过以下 3 种方式之一对这些线进行排序：

* Configuration Order - 您配置不同 item 的顺序

* Name - 所有分组的字母顺序，从顶部的 A 到底部的 Z

* Most Recent Event - 最新事件所在的分组位于顶部

* **Max Graph Height** - 设置 widget 中图形时间线的最大高度（以像素为单位）。要设置整个 widget 的高度，请参阅配置中 Format 选项卡下的 Sizing 选项。

* **Add one or more Linked Objects (event)** - First, add at least one Linked Object Type that you wish to display on the timeline by clicking on “Add Item”. You can add many types of Linked Object:
* Display different object types on the timeline, that are completely different events. Example: Linked Objects to an Aircraft that are both Flights events and Maintenance events.
* Display events of the same Linked Object type, but by different date properties, or with different types of Links defined. Examples:
* Flights events linked to an Airport object displayed on the same timeline by different date properties: (1) “Planned Arrival Time”, (2) “Actual Arrival Time”, (3) “Expected Departure Time”. Each flight will appear up to 3 times in this case.
* An Airport object can have both Arriving Flights as well as Departing Flights that are linked to it displayed on the same timeline.
* **Select the type of event object you wish to add** - for each event object you wish to add, configure the details of that object type:
* Select Linked Object - either directly Linked Object or an Extended Link.
* Example of a directly Linked Object: current object is an Airport and you want to display a timeline of Arriving Flights and Departing Flights.
* Example of an Extended object (2nd degree): current object is an Airport, and you want to display a timeline of all Aircraft objects that are linked to Arriving Flights linked to the Airport.
* **Configure visual format options**
* Max Number of Events - this option is currently not functional.
* Color - select the color for the all events under this item’s configuration. Use the [Blueprint standard colors ↗](https://blueprintjs.com/docs/#core/colors) or basic color names - “Blue”, “Red”, “Yellow”, etc.
* Series Name - the description of all events under this timeline, which will be displayed on the legend of the graphic timeline.
* **Define the date property used to sort events on the timeline** - select by which property of the Linked Object you wish to use to display the events on your timeline. This property has to be a timestamp / date, so the configuration only suggests such properties.
* **Group Events By** - select how to group the events on the graphic timeline. Each group would be displayed as a separate horizontal line of events in the graphic timeline, stacked one on top of the other. There are two options:
* Constant - current item would be grouped on a single timeline, with a title defined as a free-text value. In this case, if you wish to add other timelines as separate lines, you must define additional items.
* Property - split the events to a number of separate timelines, with events grouped on each timeline according to the different values of that property.
* Example: displaying a timeline of all Arriving Flights of an Airport object, one could select the “Airline Name” property and have a separate timeline for each Airline with all flights of that Airline on its dedicated timeline. The list below would include a chronological list of all Flights events from all Airlines.
* **Properties Displayed in List** - select the properties you wish to display on the second part of the widget, the List:
* Select what properties you wish to display:
* All Properties - not recommended if the Linked Object has many properties, as it would be crowded and hard to navigate through the timeline.
* Prominent Properties - only the properties defined as Prominent in the Ontology Manager.
* Specific Properties - opens a multi-select dropdown with all properties of that Linked Object. Choose specific properties to display.
* No Properties - only the title of the Linked Object is displayed on the timeline.
* Property Filter - an optional toggle to add a filter based on a single property, to include only specific values. These values must be explicitly typed as case-sensitive free-text strings.
* Additional configurations for the graphic timeline (these only apply to the timeline component and have no effect on
the table component)
* **Groups Displayed by Default** - how many timelines, or which ones exactly, should be displayed as separate lines in the timeline. In both cases, the user would have a multi-select helper with all other groups on it.
* Max Number - the maximal number of different groups and different timelines would be displayed in the graphic timeline, as a number (Value).
* Explicit List - write the exact list of values of the groups you wish to display (text, case sensitive).
* **Sort Groups By** - the timeline can have multiple horizontal lines, and this allows you to sort these lines by 1 of 3 ways:
* Configuration Order - the order in which you configured the different items
* Name - alphabetical order of all groups, from A at the top - to Z at the bottom
* Most Recent Event - the group with the most recent event at the top
* **Max Graph Height** - set the maximum height of the graphic timeline in the widget (in pixels). To set the height of the entire widget, see the Sizing options under the Format tab in the configuration.
#### Format
在 Format 选项卡下，除了 Title、Icon、Info 和 Layout 的默认值之外，您还可以控制该部分的最小和最大高度。设置其中任何一个都是可选的。

Under the format tab, aside from defaults of Title, Icon, Info and Layout, you can control the minimum and maximum height of the section. Setting either is optional.
### Common Issues and Notes
* 最终用户可以使用自由文本筛选器或日期范围来筛选时间轴。请注意,这些筛选器未发布,且*不会*影响其他 widgets。

* 如果启用了交叉筛选,则此 widget 会受其他筛选 widgets 的影响。

* The end use can filter the timeline using a free-text filter or a date range. Note that these filters are not published and do *not* affect other widgets.
* This widget is affected by other filtering widgets, if cross-section filtering is enabled.