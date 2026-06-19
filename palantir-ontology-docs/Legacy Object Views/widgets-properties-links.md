<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/widgets-properties-links/
---
# Properties and links
本页讨论了所有展示 object 数据模型和 ontology 简单表格视图的 widget，重点展示当前 object 的 properties 以及该 object 与其他 objects 之间的 links。

This page discusses all widgets displaying simple tabular views of an object’s data model and ontology, highlighting the properties of the current object, and the links that the object has to other objects.
该类别还包括用于展示统计、metrics 或 KPI 的 widget，这些指标要么是预先在 object 的 pipeline 中计算好并作为 object 的 property 可用，要么需要对当前 object 的 Linked Objects 进行聚合计算。

This category also includes widgets to present statistics, metrics or KPIs that are either pre-calculated in the object’s pipeline and available as a property of the object, or that require aggregations over Linked Objects to the current object.
## Properties widget
**Properties** widget 展示一个 object 或 linked object 的 properties。包含该 widget 的 tab 会作为任何新定义 object type 的默认 Object View 被创建。

The **Properties** widget displays properties of an object or a linked object. A tab containing this widget is created as the default Object View for any newly defined object type.
![Properties widget](/docs/resources/foundry/object-views/widgets_hu-properties.png)
### Properties widget configuration
#### Properties definition in the Ontology Manager
Properties widget 的配置与 Ontology Manager 中的 properties 定义密切相关。当你点击 "Edit Properties and Backing Dataset" 时，每个 Property 都有一个独立的面板，允许你定义它在 Object View 中的显示方式。

The Properties widget configuration is closely related to the properties definition in the Ontology Manager. As you “Edit Properties and Backing Dataset”, each Property has a separate settings panel, which allows you to define how it will be displayed in the Object View.
有多个设置会影响 Properties Widget 中的显示效果：

There are several settings that affect the display in the Properties Widget:
* Property 可见性

* Prominent：该 property 将显示在 Properties widget 中，并且 widget 中有一个配置选项用于仅显示 prominent properties。此选项用于 object 最重要的核心 properties。

* Normal：该 property 将显示在 Properties widget 中。此选项用于大多数 properties。

* Hidden：该 property 不会显示在 Properties widget 中（也不会显示在 Object View 或 Object Explorer 的任何位置）。此选项用于内部 ID、与其他 objects 链接的关系列等 properties。

* Render Hints
* Long text：此选项将一个 property 标记为长文本（通常用于长字符串，例如描述、评论等），可以在 Properties widget 的单独 section 中显示文本。

* Keywords：将 property 渲染为 keyword，这会改变其在 Properties widget 中的查看方式，并允许在 widget 内的单独 section 中显示。

* Type classes：这允许你为 properties 定义 type classes，这会影响它们的功能。

* 将 property 设为可编辑：如果你希望使 property 可编辑，请设置一个 [action type](/docs/foundry/action-types/overview/) 或 [inline action](/docs/foundry/action-types/inline-edits/)。

* Property visibility
* Prominent: The property will be displayed in the Properties widget, and there is a configuration option in the widget to only display prominent properties. This option is used for the most important core properties of an object.
* Normal: The property will be displayed in the Properties widget. This option is used for most properties.
* Hidden: The property will not be displayed in the Properties widget (or anywhere in the Object View or Object Explorer). This option is used for properties such as internal IDs, relation-columns for links to other objects, and so on.
* Render Hints
* Long text: This option, marking a property as a long text (usually for long strings, such as descriptions, comments, etc.), enables displaying texts in a separate section of the Properties widget.
* Keywords: Render a property as a keyword, which changes the way it is viewed in the Properties widget, and also allows to display it in a separate section within the widget.
* Type classes: This allows you to define type classes to properties, which would affect their functionality.
* Make a property editable: If you wish to make a property editable, set up an [action type](/docs/foundry/action-types/overview/) or an [inline action](/docs/foundry/action-types/inline-edits/).

> 📷 **[图片: Properties in Ontology Manager]**

> 📷 **[图片: Properties in Ontology Manager]**

#### Configuration of the Properties widget itself
在 widget 配置中，首先选择您希望显示 Current Object 的 properties，还是 Linked Object 的 properties：

In the widget configuration, first select if you wish to display properties of the Current Object, or properties of a Linked Object:
* 如果显示 Linked Object，首先选择您希望显示的 link。

* 只有当 Current Object 仅链接到一个 object 时，才能显示 Linked Object 的 properties。这在以下情况下是可能的：(1) 一对一关系；(2) 多对一关系，其中 Current Object 定义为“多”的一方。

* 示例：配置一个 Flight object 时，可以显示链接到该 flight 的 Aircraft 的 properties（Flights 与 Aircraft 之间是多对一关系）。但是，从 Aircraft object 的角度来看，则无法显示链接的 Flight 的 properties，因为任何单个 Aircraft 都链接到多个 Flight object。

* In case of displaying a Linked Object, first select the link that you wish to display.
* Displaying properties of a Linked Object is possible only if the Current Object is linked to only one object, which is possible either (1) in a one-to-one relationship; (2) in a many-to-one relationship, with the Current Object defined as the “many”.
* Example: Configuring a Flight object, it is possible to display the properties of the Aircraft linked to this flight (Flights to Aircraft has a many-to-one relationship). However, looking at the Aircraft object, it would not be possible to display properties of the linked Flight, as there are many Flight objects linked to any single Aircraft.
选择 Current Object / Linked Object 之后，有 3 个组件需要配置：Data、Sections、View Options。

After choosing Current Object / Linked Object, there are 3 components to configure: Data, Sections, View Options.
##### Data
* 选择您希望显示的 properties：

* All Properties：显示所有定义为 Prominent 或 Normal 的 properties，但不显示 Hidden 的 properties。允许使用 `Properties to Exclude` 选择器排除一组特定的 properties（见下文）。

* Prominent Properties：仅显示在 Ontology Manager 中定义为 Prominent 的 properties。允许使用 `properties to exclude` 选择器排除一组特定的 properties（见下文）。

* Specific Properties：打开一个多选下拉菜单，其中包含该 Linked Object 的所有 properties，可供选择。

* No Properties：不显示任何 property。

* Properties to Exclude：选择您希望从显示中排除的 properties - 仅适用于前两个选项 - All Properties 和 Prominent Properties。

* Select what properties you wish to display:
* All Properties: Display all properties that are defined as Prominent or Normal, but no Hidden properties. Allows exclusion of a specific set of properties using the `Properties to Exclude` selector (see below).
* Prominent Properties: Display only the properties defined as Prominent in the Ontology Manager. Allows exclusion of a specific set of properties using the `properties to exclude` selector (see below).
* Specific Properties: Opens a multi-select dropdown with all properties of that Linked Object, to select between.
* No Properties: Do not display any property.
* Properties to Exclude: Select which properties you wish to exclude from display - only available for the first two options - of All Properties and Prominent Properties.
##### Sections
默认情况下，有三个 property sections，分别是：

By default, there are three sections of properties, which are:
* Normal properties：所有 Normal 和 prominent；

* Long text properties：仅包含 long text properties，这些在 Ontology Manager 中被定义为 long text（详见上文）；

* Keyword properties：将 object 的 keyword properties 显示为 tags。仅显示在 Ontology Manager 的“Edit Properties and Backing Dataset”中被标记为 keyword 的 properties。

* Normal properties: All Normal and prominent;
* Long text properties: Only long text properties, which are defined as such in the Ontology Manager (see details above);
* Keyword properties: Displays keyword properties of object as tags. Only properties that were marked as keywords in the Ontology Manager, under “Edit Properties and Backing Dataset” would be displayed here.
您可以删除这些 sections 或更改其顺序。除了这三种类型之外，没有其他类型的 sections。

You can remove or change the order of these sections. There are no additional types of sections to these three.
##### View options
* **User Editable：** 是否允许用户编辑 properties。这需要事先在 Ontology Manager 中进行两项设置（详见上文）：

* Dataset level：必须在 object type 上启用编辑。

* Property level：必须有一个 [inline edit action](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits) 附加到该 property 上。

* **Hide Undefined Values：** 隐藏所有值未定义（null）的 properties。如果此开关关闭，property 将以灰色的“no value”文本显示。

* **Include link to 'More properties'：** 此选项将渲染一个 **View all** 按钮，使用户进入同一 object 视图中的 **Properties** 标签页。

* **User Editable:** Whether to allow users to edit properties. This requires two settings in the Ontology Manager in advance (see more details above):
* Dataset level: Edits must be enabled on the object type.
* Property level: There must be an [inline edit action](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits) attached to the property.
* **Hide Undefined Values:** Hide all properties with undefined (null) values. If this toggle is off, the property will be displayed with “no value” text greyed out.
* **Include link to 'More properties':** This option will render a **View all** button that takes the user to a **Properties** tab within the same object view.
#### Common issues and notes
* properties 显示的顺序是按字母排序的。以其他方式对 properties 进行排序的主要方法是使用上述 widget 配置中的 "Sections"。

* 有关如何将 properties 设置为 Prominent、将 properties 设置为 Long Text 或 Keyword，或使其可由用户编辑的更多详细信息，请参阅 [documentation on editing properties](/docs/foundry/object-link-types/edit-properties/)。

* The order in which properties are displayed is alphabetical. The main way to order properties in a different way is by using the "Sections" mentioned above, under the widget configuration.
* For more details on how to setup properties as Prominent, set properties as a Long Text or a Keyword, or making them user editable, see the [documentation on editing properties](/docs/foundry/object-link-types/edit-properties/).
## Property Cards
**Property Cards** widget 使您能够可视化包含 properties 和 linked objects 聚合的卡片。

The **Property Cards** widget lets you visualize cards with properties and aggregations over linked objects.
使用 Property Cards widget 显示重要的 properties（数值、时间戳、日期、字符串等）、aggregations、统计、metrics、KPI，以及当前 object 或与其链接的 object 的任何其他关键信息。

Use the Property Cards widget to display important properties (numeric, timestamps, dates, strings, etc.), aggregations, statistics, metrics, KPIs, and any other key information for the current object or for objects linked to it.
![Property cards](/docs/resources/foundry/object-views/widgets_property-cards.png)
* 此 widget 受 filters 影响，这些 filters 适用于 linked objects 的任何 aggregations。

* Property Cards widget 支持丰富的 UI 用于 [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/) 和 [value formatting](/docs/foundry/object-link-types/value-formatting/)，包括全局（基于 ontology editor 中的 ontology 级配置）和本地覆盖选项。

* This widget is affected by filters, which apply to any aggregations of linked objects.
* The Property Cards widget supports a rich UI for [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/) and [value formatting](/docs/foundry/object-link-types/value-formatting/), including both global (based on ontology-level configurations in the ontology editor) and local override options.
### Property Card configuration
首先为每个 property / linked object aggregation 的可视化添加一个新卡片。然后，配置 widget 中所有卡片的整体布局。

Start by adding a new card for each visualization of a property / linked object aggregation. Then, configure the
overall layout of all cards within the widget.
#### Configuration per card
* Property cards 可以显示 **a property** 或 **an aggregation of linked properties**。

* 显示 property 时，卡片可以显示 current object 的 properties，也可以显示具有一对一关系或多对一关系的 linked object 的 properties（例如，如果 current object 是 Flight，并且与 Aircraft 是多对一关系，则可以显示 Aircraft object 的 properties）。

* 显示 linked object 时，卡片可以显示与 current object 存在一对多或多对多关系链接的任何 object 的 aggregations。

* 对于 aggregations，选择 aggregation 的类型 - count、unique count / cardinality、average、min、max、sum。

* 添加将显示在卡片上的 label，以及 icon 和 icon color。

* **Conditional formatting and value formatting：** 默认情况下，widget 使用在该特定 object 和 property 的 ontology 级别定义的全局 ontology 格式化规则。

* 此 widget 支持 conditional formatting（例如，根据预定义规则将 value 颜色设置为红色/绿色）。支持的选项是全局格式化（在 Ontology Manager 中配置的，参见 [conditional formatting documentation](/docs/foundry/object-link-types/conditional-formatting/)）和可选的本地覆盖。请注意，这仅适用于 properties，不适用于 aggregations。

* Property Cards widget 支持 value formatting（例如，`$3.6M` 而不是 `3,625,329`）。支持的选项是全局 value formatting（在 Ontology Manager 中配置的；参见 [value formatting documentation](/docs/foundry/object-link-types/value-formatting/)）和本地覆盖。请注意，这适用于 properties 和 linked properties 的 aggregations。

* 对于本地覆盖，value 和 conditional formatting 使用与 ontology 级别格式化相同的 UI，请查看 ontology 文档（链接如上）以获取更多详细信息。

* Property cards can either display **a property** or an **aggregation of linked properties**.
* When displaying a property, a card can show both properties of the current object, as well as properties of a linked object with a one-to-one relation or a many-to-one (e.g. if the current object is Flight, with a many-to-one relation to Aircraft, it would be possible to show the properties of the Aircraft object).
* When displaying a linked object, the card can show aggregations of any object linked to the current object in a one-to-many or many-to-many relation.
* In case of an aggregations, select the type of aggregation - count, unique count / cardinality, average, min, max, sum.
* Add a label which will be displayed on the card, as well as an icon and icon color.
* **Conditional formatting and value formatting:** By default, the widget uses the global ontology formatting rules defined at the ontology level for that specific object and property.
* This widget supports conditional formatting (e.g. color value to red/green according to predefined rules). Supported options are global formatting (as configured in Ontology Manager (see [conditional formatting documentation](/docs/foundry/object-link-types/conditional-formatting/)) and an optional local override. Note that this applies only for properties, not for aggregations.
* The Property Cards widget supports value formatting (e.g. `$3.6M` instead of `3,625,329`). Supported options are global value formatting (as configured in Ontology Manager; see [value formatting documentation](/docs/foundry/object-link-types/value-formatting/)) and a local override. Note that this applies to properties and to aggregations of linked properties.
* For local overrides, both value and conditional formatting use the same UI as the ontology level formatting, check the ontology documentation (linked above) for further details.
#### Configuration for all cards on a Property Cards widget
* 一旦所有 Property 和 aggregation cards 配置完成，可以使用 layout configuration 来确定 cards 显示时的背景、尺寸、样式、对齐方式和图标样式的样式设置。

* 如果希望对不同的 cards 使用不同类型的可视化配置，可以考虑为每种不同的配置添加一个新的 widget instance。

* Once all property and aggregation cards are configured, use the layout configuration to determine styling of background, size, style, alignment and icon style of cards in display.
* If you wish to use different types of visual configurations for different cards, consider adding a new widget instance for each different configuration.

> 📷 **[图片: Property cards config]**

> 📷 **[图片: Property cards config]**

#### Common issues and notes
* Property Cards 是用于可视化当前 object 和 linked objects 的显著 properties、aggregations、statistics、metrics、KPI 以及任何其他关键信息的受支持 widget。

* 在可视化单个关键 properties 和 aggregations 方面，此 widget 是优于任何其他 widget 的首选解决方案。建议使用 Property Cards widget 来替代以下 widgets：Statistics、Context Stat Section、Linked Statistics、Advanced Statistics 或 Property Plus。

* Property Cards widget 不支持 [Functions on Objects](/docs/foundry/functions/functions-on-objects/)。如果需要此支持，请考虑使用 Workshop 或 Quiver，并通过专用 widgets 将其嵌入到 Object View 中。

* Property Cards is the supported widget for visualizing prominent properties, aggregations, statistics, metrics, KPIs and any other key information for the current object and linked objects.
* This widget is the preferred solution over any other widget for purposes of visualizing single key properties and aggregations. Consider using the Property Cards widget instead of the following widgets: Statistics, Context Stat Section, Linked Statistics, Advanced Statistics, or Property Plus.
* The Property Cards widget does not support [Functions on Objects](/docs/foundry/functions/functions-on-objects/). If this support is required, consider using Workshop or Quiver and embedding it in the Object View using the dedicated widgets.
## Links
**Links** widget 以树状视图显示一个 object 的 links，并具有遍历 Links 和导航到 Linked Objects 的能力。包括：

The **Links** widget displays an object's links in a tree view, with the ability to traverse through Links and navigate to Linked Objects. This includes:
* 显示所有 Linked Objects 的树状结构，能够展开每个 Linked Objects 的视图，以显示与其链接的所有 Objects，并继续通过 Links 进行跳转（"嵌套链接"）；

* 悬停任何 Object 可以看到一个包含该 Object 所有显著 properties 的 tooltip；

* 点击任何 object 可以跳转到其 Object View。

* Display a tree of all Linked Objects, with the ability to expand the view for each Linked Objects, to display all Objects Linked to it, and continue hopping through Links (“nested links”);
* Hover over any Object to see a tooltip with all prominent properties of that Object;
* Click on any object to jump to its Object View.
请参见以下示例，其中包含 3 个步骤：

See an example below, which includes 3 steps:
* 从一个 Airport object 开始；

* 转到所有 Linked Flights；

* 转到其中一个 Flight 的所有 Linked Objects：Aircraft、Destination Airport 以及所有相关的 Post-Flight Reviews。

* Starting with an Airport object;
* Moving to all Linked Flights;
* Moving to all Linked Objects of one of these Flights: Aircraft, Destination Airport, all related Post-Flight Reviews.
![Links widget](/docs/resources/foundry/object-views/widgets_hu-links.png)
### Links widget configuration
* Link types (first links only) - 允许您确定 widget 上将显示哪些类型的 links。用户可以遍历 links 并跳转到其他 linked objects（例如，从 Airport → 到所有 Flights → 到承载这些 Flights 的 Aircraft → 到拥有这些 Aircraft 的 Airlines，等等）

* Filter Nested Links by Type - 此设置允许您仅显示在 "Link types (first links only)" 下选择的 Linked Objects。

* Link types (first links only) - allows you to determine which types of links will be displayed on the widget. Users can traverse through links and hop to other linked objects (e.g. from an Airport → to all Flights → to the Aircraft carrying these Flights → to the Airlines owning these Aircraft, etc.)
* Filter Nested Links by Type - this setting allows you to only display Linked Objects that are chosen under the “Link types (first links only)”.
#### Common issues and notes
* 目前无法对以下内容进行排序或确定顺序

* Linked Objects 的 values 列表（例如，按字母顺序显示所有 Linked Flights）。

* 此 widget 下 Linked Objects 的 *types*（例如，先显示 Linked Flights，再显示 Linked Aircraft）。

* 此 widget 目前不受 filters 的影响。显示的 Links 始终是链接到当前 Object 的*所有* Objects。

* It is currently not possible to sort or determine the order of
* The list of values of Linked Objects (e.g. show all Linked Flights alphabetically).
* The *types* of Linked Objects under this widget (e.g. show Linked Flights first and Linked Aircraft second).
* This widget is currently not affected by filters. Links displayed are always *all* Objects linked to the current Object.
## Edit History
**Edit History** widget 以列表视图显示当前查看 object 的所有编辑历史。如果 object 从未被编辑，或者所选 columns 的子集（详见下文）没有编辑记录，则此 widget 将显示 `No Edits` 消息。

The **Edit History** widget displays a list view with the history of all edits made for the current object in view. If the object has never been edited or the subset of selected columns (more below) has no edits, this widget will display a `No Edits` message.

> 📷 **[图片: Edit history]**

> 📷 **[图片: Edit history]**

### Edit History configuration
|Option |Description    |
|---    |---    |
|All Properties |Displays edits for all properties on the given object type.  |
|Specific Properties    |Specific Properties, Only displays edits for properties selected in the `Properties to Include` selector in the widget config. |
#### Common issues and notes
* Edit History 中仅显示通过 Actions 对 object 所做的更改。在 backing dataset 或上游 pipeline 中所做的更改不会反映在此 widget 中。

* Edit History 只会反映在 Ontology Manager 中启用 [**Track user edit history**](/docs/foundry/object-edits/user-edit-history/) 切换开关之后，索引到 Object Storage V2 中的 objects 的更改。

* 目前不支持对带有 marking properties 的 object types 进行 user edits 跟踪。

* 每个提交的值都会作为一次编辑被记录，即使它来自 action parameter 中配置的默认值。

* Only changes made via Actions to the object will be shown in Edit History. Changes made in the backing dataset or in the pipeline upstream will not be reflected on this widget.
* Edit History will only reflect the changes made to objects indexed into Object Storage V2 after the [**Track user edit history**](/docs/foundry/object-edits/user-edit-history/) toggle is enabled within Ontology Manager.
* Tracking user edits for object types with marking properties is not supported at this time.
* Each submitted value is logged as an edit, even if it is coming from a default value configured in an action parameter.