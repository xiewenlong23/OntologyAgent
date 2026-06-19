<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/widgets-filtering/
---
# Filtering
许多 Object View 要求用户对可视化组件（如图表、表格、聚合 Metric 和 KPI 等）进行过滤。**Filter Widgets（过滤器 widget）** 允许用户应用不同类型的过滤器，以便深入查看该 Object View 上特定子集的 Linked Objects。

Many Object Views require the user to filter on visual components such as charts, tables, aggregative metrics and KPIs, and so on. **Filter Widgets** allow users to apply different types of filters in order to drill-down into a specific subset of Linked Objects on that Object View.
此类别包含多个 Filter Widgets：

This category includes several Filter Widgets:
* 通过使用 [Multiselect Filter](#multiselect-filter)、[Dropdown Filter](#dropdown-filter)、[Button Filter](#button-filter) 或 [Date Range Filter](#date-range-filter)，按预定义 Property（包括字符串、数值和日期）进行过滤。

* 如需更灵活的过滤功能，请使用 [Linked Object Filter Sidebar](#linked-object-filter-sidebar)

* 使用 [Filter Sandbox Container](#filter-sandbox-container) 可使某些过滤器仅应用于当前视图的特定部分。

* 使用 [Filter Container](#filter-container) 可将预定义过滤器仅应用于 Object View 内的部分 widget。

* 使用 [Active Filters](#active-filters) 可汇总当前在 Object View 上应用的所有过滤器。

* Filter by pre-defined properties, including strings, numerical values, and dates by using the [Multiselect Filter](#multiselect-filter), [Dropdown Filter](#dropdown-filter), [Button Filter](#button-filter), or [Date Range Filter](#date-range-filter).
* Use the [Linked Object Filter Sidebar](#linked-object-filter-sidebar) for more flexible filtering functionality
* Use the [Filter Sandbox Container](#filter-sandbox-container) to have certain filters applied only on part of the current view.
* Use the [Filter Container](#filter-container) for pre-defined filters applied only on a subset of widgets within the Object View.
* Use the [Active Filters](#active-filters) for a summary of all filters currently applied on your Object View.
除了这些仅用于过滤的核心过滤 Widgets 之外，还有一些专门用于可视化但也支持部分过滤功能的 widget，例如 Charts。[Conditional Container](/docs/foundry/object-views/widgets-layout/#conditional-container) 支持根据用户交互的过滤器来显示/隐藏内容。

Apart from these core Filtering Widgets, which are dedicated to filtering only, there are additional widgets that are dedicated to visualization, but also allow some filtering, such as Charts. The [Conditional Container](/docs/foundry/object-views/widgets-layout/#conditional-container) enables displaying/hiding content according to filters that the user interacts with.
**常见问题与注意事项：**

**Common Issues and Notes:**
* 为了在 Object View 的单个选项卡上的不同 widget 之间（甚至跨选项卡之间）激活过滤功能，**您必须在右侧栏编辑器的 "Settings" 下勾选 "cross-filtering" 复选框**。未勾选此复选框的选项卡将不会应用过滤器。

> 📷 **[图片: 已启用跨区域过滤]**

* In order to activate filters to apply across different widgets on a single tab of an Object View, or even across tabs, **you have to mark the checkbox of “cross-filtering”** on the right-bar editor, under “Settings”. Filters will not apply in tabs that were not marked with this checkbox.

> 📷 **[图片: Cross-section filtering enabled]**

* 若要使过滤器**跨不同选项卡**应用，请确保选项卡 Settings 下的 "filterSet value" 在您希望进行跨选项卡过滤的所有选项卡中具有完全相同的文本值。该值区分大小写。

* 在这种情况下，使用相同 filterSet value 的过滤器将受到相同活跃过滤器的影响。例如，如果 Tab A 和 Tab B 共享相同的 filterSet value，则在 Tab A 上应用的任何过滤器都会在 Tab B 上生效，反之亦然。

> 📷 **[图片: 跨选项卡过滤]**

* In order to have a filter applied **across different tabs**, make sure that the “filterSet value“ under the tab Settings has an identical text value across all tabs you wish to filter across. This value is case-sensitive.
* In that case, the filters that use the same filterSet value will be affected by the same active filters. For example, if Tab A and Tab B share the same filterSet value, any filters applied on Tab A will be applied on Tab B and vice versa.

> 📷 **[图片: Filter across tabs]**

* 在所有过滤配置中，您需要选择当前所编辑 Object 的 Linked Object，而不是您正在编辑的 Object 本身。

* 示例：如果您正在配置 "Airport" 的 Object View，并且其关联了 "Flights"，则您可能会在 Flights 上显示不同的可视化内容（时间线、图表、所有航班的列表表格），并希望针对 "Flights" 的不同 Property 设置过滤器（例如按航空公司过滤、按日期过滤、按出发城市过滤）。

* 因此，在配置过滤器之前，您当前的 Object 需要链接到另一个 Object。链接的设置在 Ontology Manager 中完成。

* In all filter configurations, you will select a Linked Object to the object that you’re currently editing, and not the object that you are editing itself.
* Example: If you’re configuring the Object View of an “Airport”, with “Flights” connected to it, you would probably have different visuals on flights (timelines, charts, list of all flights in a table), and would want to set your filters on different properties of “Flights” (e.g. filter per airline, filter per date, filter per origin city).
* Therefore, before you configure a filter, your current object needs to be linked to another object. Setting up the links is done in the Ontology Manager.
* 大多数 Filter Widgets 仅添加了一项可选功能，允许用户针对当前正在浏览 Object 的视图在本地应用过滤器。

* 大多数 Filter Widgets 不支持预配置默认激活的过滤器，从而为用户缩小视图范围（Filter Container 除外，它确实支持设置预配置过滤器）。

* 用户可以在当前 Object 的当前视图上激活过滤器，但一旦他们切换到其他 Object 或刷新页面，这些过滤器将不再生效。

* Most Filter Widgets only add an optional functionality that allows the user to apply filters locally for the current view of the object they currently browse.
* Most of the Filter Widgets do not enable you to pre-configure filters to be active by default, such that would narrow down the view for the user (Filter Container is an exception, as it does allow to set up pre-configured filters).
* The user would be able to activate filters on their current view of the current object, but once they move to a different object or refresh, these filters would not apply.
## Multiselect Filter
Multiselect Filter 允许用户通过多个值对 Object View 进行过滤，值之间使用 "OR" 逻辑。它会保留满足所选值中至少一个条件的所有条目。

The multiselect filter allows users to filter the Object View by multiple values, with an “OR” statement between them. It keeps all entries that satisfy at least one of the chosen values.
配置完成后，效果如下：

Once configured, this is how it looks:
![multiselect-filter](/docs/resources/foundry/object-views/widgets_hp-multi-select-filter-1.gif)
### Configuration
注意：每个始终需要配置的设置项旁边都用 (\*) 符号标记。

Note: Each setting that is always required is signed with a (\*) sign next to it.
* \[必填] **Linked Object to Filter（要筛选的 Linked Object）：** 选择此筛选器要应用的 Linked Object。Widget 配置将仅提供与当前配置的 Object 相关联的 Objects（在 Ontology Manager 中定义）。

* 示例：在 *Airport* Object View 中，包含 *Flights* Objects 的视图，涉及两种到 *Airport* 的 Link Type："*Arriving Flights*"（到达航班）和 "*Departing Flights*"（出发航班）。如果将 Multiselect Filter 的 Linked Object 设置为 "*Arriving Flights*"，则它将应用于所有其他同样涉及 "*Arriving Flights*" Object 的 widgets。

* \[必填] **Property to Filter（要筛选的属性）：** 选择要筛选的属性：(1) 首先需要为筛选器选择 Object Type；然后 (2) 选择该 Object 上要按其筛选的属性。

* 选择后，此值列表将在 Object View 中以带多选下拉框的筛选器形式提供给用户。受此筛选器影响且与该筛选器共享 Object 的所有其他 widgets 将被筛选，仅显示具有所选属性值（一个或多个）的 Object 实例。

* 示例：查看一个机场 Object，其到达航班来自 20 个起点，用户有一个额外的 widget 显示来自这些起点的所有到达航班表格。用户为 Object `Arriving flights` 选择一个 multiselect filter，然后为 `Flights` Object 选择 `Origin City` 属性。下拉筛选器将向用户呈现所有 20 个起点。一旦用户选择起点的子集，表格 widget 将仅显示来自该起点子集的到达航班。

* \[可选] **Label For Filter（筛选器标签）：** 将在 Object View 中显示在筛选器框旁边，供用户查看。

* \[可选] **Maximum Number Of Filter Options（筛选选项的最大数量）：** 确定要显示的属性的不同值的数量。默认设置为 100。

* \[Required] **Linked Object to Filter:** Choose the Linked Object for this filter to apply on. The widget configuration would offer you only objects linked to the object you are currently configuring (as defined in the Ontology Manager).
* Example: In an *Airport* Object View, which includes views of *Flights* objects, involving both types of links to the *Airport*: “*Arriving Flights*” and “*Departing Flights*”. If you set up the Multiselect Filter with the Linked Object “*Arriving Flights*”, it would apply to all other widgets that are also involving that same object “*Arriving Flights*”.
* \[Required] **Property to Filter:** Choose the property you want to filter down by: (1) you first need to choose the object type for the filter; and then (2) choose the property of that object by which you want to filter.
* Once selected, this list of values will be available to users in the Object View, in a filter box with a multi-select dropdown. All other widgets affected by this filter and sharing the object with this filter, would be filtered down to only object instances that have the property values (one or many) chosen.
* Example: Looking at an airport object with arriving flights from 20 origins, a user has an additional widget showing a table of all flights arriving from these origins. The user chooses a multiselect filter for the object `Arriving flights`, and then chooses the property `Origin City` for the `Flights` object. The dropdown filter would present to the user all 20 origins. Once the user chooses a subset of origins, the table widget would only show arriving flights from this subset of origins.
* \[Optional] **Label For Filter:** will be displayed to users in the Object View, next to the filter box.
* \[Optional] **Maximum Number Of Filter Options:** determines how many distinct values of the property to filter will be displayed. Set by default to 100.
**常见问题和注意事项：**

**Common Issues and Notes:**
* 配置完成后，您需要在右侧配置编辑器设置中勾选"allow cross-filtering"复选框（详见上文），筛选器才能对 Object View 生效。

* Once configured, you would need to mark the checkbox “allow cross-filtering” in the configuration editor settings on the right side (see details above) in order for the filter to affect the Object View.
## Dropdown Filter
此筛选器支持具有一个或多个带单选下拉框（针对单个属性）的筛选器，允许用户使用值下拉框筛选 Object View 中的其他 widgets。

This filter enables having one or more filters with a single-selection dropdown of a single property, allowing the user to filter other widgets in the Object View using a dropdown of values.
配置完成后，效果如下：

Once configured, this is how it looks:
![Dropdown Filter](/docs/resources/foundry/object-views/widgets_hp-dropdown-filter.gif)
### Configuration
对于您希望配置的每个下拉筛选器选项，您需要先点击"Add Item"。您只需再次点击"Add Item"，即可在单个 widget 下添加多个下拉筛选器（它们将并排显示）。

For each dropdown filter option you would like to configure, you need to first click on “Add Item”. You will be able to add several dropdown filters under a single widget by just clicking “Add Item” again (they will all appear one next to the other).
添加项后，配置菜单提供两种"Filter Type"选项：

Once an item is added, the configuration menu offers two options of "Filter Type":
**选项 1 - Dynamic List（动态列表）：**

**Option 1 - Dynamic List:**
这是更简单的选项，允许像大多数筛选器 widgets 一样轻松选择 Object 和下拉属性：

This is the simpler option, allowing an easy selection of an object and a property for the dropdown like most filter widgets:
* \[必填] **Linked Object to Filter（要筛选的 Linked Object）：** 选择此筛选器要应用的 Linked Object。Widget 配置将仅提供与当前配置的 Object 相关联的 Objects（在 Ontology Manager 中定义）。

* \[必填] **Property to Filter（要筛选的属性）：** 选择要筛选的属性：(I) 首先需要为筛选器选择 Object Type；然后 (II) 选择您希望按其筛选的该 Object 的属性。

* 选择后，受此筛选器影响且与该筛选器关联到相同 Object Type 的所有其他 widgets 将从所有 Linked Objects 筛选至仅显示其属性值与下拉框中所选值相同的那些。

* \[可选] **Label For Filter（筛选器标签）：** 将在 Object View 中显示在筛选器框旁边，供用户查看。

* **Enable 'All' filter option toggle（启用"All"筛选选项开关）：** 如果筛选器为必填项，请保持此开关关闭，以强制用户选择一个值。如果可以选中所有值（不按其中任何一个进行筛选），请打开此开关。如果您希望选择多个值，请改用 Multiselect Filter widget。

* \[Required] **Linked Object to Filter:** Select the Linked Object for this filter to apply on. The widget configuration would offer you only objects linked to the object you are currently configuring (as defined in the Ontology Manager).
* \[Required] **Property to Filter:** Select the property you want to filter down by: (I) you first need to select the object type for the filter; and then (II) select the property of that object that you wish to filter by.
* Once selected, all other widgets affected by this filter and related to the same object type as this filter, would filter down from all Linked Objects to only those where their property has the same value as selected in the dropdown.
* \[Optional] **Label For Filter:** Will be displayed to users in the Object View, next to the filter box.
* **Enable 'All' filter option toggle:** If the filter needs to be mandatory, keep this toggle off, to force users to select one value. If it can have all values selected (do not filter by any of them), turn the toggle on. If you wish to select multiple values, select the Multiselect Filter widget instead.
**选项 2 - Value List（值列表）：**

**Option 2 - Value List:**
这是更复杂的选项，专门用于希望定义精确筛选值列表的情况，该列表将是完整下拉列表的子列表。您需要手动键入希望包含在 Dropdown Filter 中供用户使用的每个值。配置方法如下：

This is the more complex option, specifically for cases where you wish to define an exact list of values to filter from, which would be a sub-list of the full dropdown list. You would need to manually type each and every value you wish to include in the Dropdown Filter for the user. How to configure this:
* \[必填] **Linked Object to Filter（要筛选的 Linked Object）：** 选择此筛选器要应用的 Linked Object。

* \[必填] **Property to Filter（要筛选的属性）：** 选择要筛选的属性：(I) 首先需要为筛选器选择 Object Type；然后 (II) 选择您希望按其筛选的该 Object 的属性。

* 选择后，受此筛选器影响且与该筛选器关联到相同 Object Type 的所有其他 widgets 将从所有 Linked Objects 筛选至仅显示其属性值与下拉框中所选值相同的那些。

* \[必填] **Filter property value(s)（筛选属性值）：** 您需要手动键入希望包含在此下拉筛选器中供用户使用的每个值，然后点击"Create"以添加它。
* 输入的值区分大小写，并按输入顺序显示；一旦输入，值无法重新排序，除非删除值（点击 'X'）后重新输入。
* 显示值的数量限制为 100。

* 默认提供"All"选项。如有需要，您可以移除此选项并重新添加（"All"，区分大小写）。

* \[可选] **Label For Filter（筛选器标签）：** 将在 Object View 中显示在筛选器框旁边，供用户查看。

* \[Required] **Linked Object to Filter:** Select the Linked Object for this filter to apply on.
* \[Required] **Property to Filter:** Select the property you want to filter down by: (I) you first need to select the object type for the filter; and then (II) select the property of that object that you wish to filter by.
* Once selected, all other widgets affected by this filter and related to the same object type as this filter, would filter down from all Linked Objects to only those where their property has the same value as selected in the dropdown.
* \[Required] **Filter property value(s):** You need to manually type down each and every value that you wish to include in this dropdown filter for the user, and click on “Create” to add it.
* Values entered are case-sensitive and will appear in the order they are entered; once entered, values cannot be re-arranged except by removing values (click on the ‘X’) and re-entering them.
* The number of displayed values is limited to 100.
* The ‘All’ option is offered by default. You can remove this option and re-add it if desired (“All”, case-sensitive).
* \[Optional] **Label For Filter:** will be displayed to users in the Object View, next to the filter box.
**常见问题和注意事项：**

**Common Issues and Notes:**
* 如果满足以下条件，请考虑使用 Multiselect 过滤器代替 Dropdown 过滤器：(a) 您希望拥有选择多个选项的功能；(b) 您不需要多个下拉菜单（不过这也可以通过 filter container 来解决）。

* Dropdown widget 与 "Active Widget" 的交互有限。即使切换并启用了 "Enable 'All' filter option"，用户仍然无法 "Clear filter"，除非他们明确地在 Multiselect 过滤器下选择 "All"。

* 配置完成后，您需要在右侧配置编辑器设置中勾选 "allow cross-filtering" 复选框（详见上文），过滤器才能对 Object View 生效。

* 在单个 dropdown filter widget 下，UI 能够呈现的 dropdown filter 框数量有限（约 7-8 个不同的 dropdown）。在极少数情况下，如果单个 Object View 需要更多 dropdown filters，请使用额外的 Dropdown 过滤器或使用 Filter Container。

* Consider using the Multiselect filter instead of the Dropdown filter if (a) you want the functionality of selecting more than a single option; (b) you don’t need multiple dropdowns (though this could also be solved with a filter container).
* The interaction of the Dropdown widget with the “Active Widget” is limited. Even if “Enable 'All' filter option” is toggled and enabled, users will still not be able to “Clear filter”, unless they explicitly select “All” under the Multiselect filter.
* Once configured, you would need to mark the checkbox “allow cross-filtering” in the configuration editor settings on the right side (see details above) in order for the filter to affect the Object View.
* There is a limit to the number of dropdown filter boxes the UI is able to present under a single dropdown filter widget (around 7-8 different dropdowns). In the unlikely event that you need more dropdown filters for a single Object View, use an additional Dropdown filter or use a Filter Container.
## Button Filter
此 widget 创建一个按钮，通过单击即可按预定义的值集进行过滤：可以是文本（字符串）值、数值范围或日期范围。再次单击该按钮可取消过滤选择。

This widget creates a button that with a single click filters to a pre-defined set of values: either text (string) values, a range of numerical values, or a range of dates. A second click on the button un-filters the selection.
这是一个刚性过滤器；一旦由 Object View Editor 配置完成，最终用户将无法进行任何配置选择。

This is a rigid filter; once configured by the Object View Editor, there is no configuration choice available to end users.
请注意，按钮在选中或取消选中时会改变颜色。您可以添加 [Active Filters](#active-filters) 来使状态在视觉上更清晰。

Note that the button changes color as you select or unselect it. You can add an [Active Filters](#active-filters) to make the state visually clear.
配置完成后，其显示效果如下：
![Button Filter](/docs/resources/foundry/object-views/widgets_hp-buttons-filter.gif)
Once configured, this is how it looks:
![Button Filter](/docs/resources/foundry/object-views/widgets_hp-buttons-filter.gif)
### Configuration
首先，选择 button filter 类型：

First, select a button filter type:
* Value List：用于过滤文本 property（字符串）。

* Range：用于过滤数值 property（如 integers 或 doubles）。

* Date Range：用于过滤为日期 property 列表。

* Value List: To filter text properties (strings).
* Range: To filter numerical properties (like integers or doubles).
* Date Range: To filter down to a list of date properties.
对于这 3 种类型的 button filters，您将拥有以下设置：

For all 3 types of button filters, you will have the following:
* \[Required] **Object to Filter：** 选择此过滤器要应用的 Linked Object。

* \[Required] **Object to Filter:** Select the Linked Object for this filter to apply on.
* \[Required] **Property to Filter：** 选择要筛选的 property：(I) 首先需要为过滤器选择 object type；然后 (II) 选择您希望按其过滤的该对象的 property。

* 一旦选中，所有受此过滤器影响且与该过滤器相关的 object type 相同的其他 widgets，将从所有 Linked Objects 过滤为仅包含符合过滤器条件属性值的对象。

* \[Required] **Property to Filter:** select the property you want to filter down by: (I) you first need to select the object type for the filter; and then (II) select the property of that object that you wish to filter by.
* Once selected, all other widgets affected by this filter and related to the same object type as this filter, would filter down from all Linked Objects to only those objects with properties value that the filter condition applies to.
* \[Required] 从此处开始，按钮的设置因按钮类型而异：

* **Value List：** 手动输入要过滤的确切值列表，各值之间用 "OR" 语句连接。请注意，此功能区分大小写，且顺序不能简单地重新排列。重新排列值的方法是删除并重新写入整个值列表。请注意，如果您同时应用 "All" 选项和另一个特定值 X，则过滤器将仅应用于值 X。

* **Range：** 提供数值范围的上下边界。至少在其中一项中输入一个值：
* 下界 = 大于或等于；
* 上界 = 小于或等于；
* 同时填写两者可创建范围过滤器。

* 如果您希望使用 "greater than"，请确保删除 Upperbound 中的 0；反之亦然，适用于 "lower than"。

* **Date Range：** 提供一个具有 2 个选项的 toggle - 精确日期（"from 1\1\2019 to 31\12\2019"）或相对于当前时间（"Last Month" 或 "Between two years ago and one year ago"）。配置本身通过标准的日历日期选择器完成。

* \[Required] From this point, the setting of the button is different per button type:
* **Value List:** manually type in the exact list of values you wish to filter by, with an “OR” statement between them. Note that it is case-sensitive and the order cannot be simply re-arranged. The way to re-arrange values is by deleting and re-writing the entire list of values. Note that if you apply both the “All” option as well as another specific value X, then the filter will only apply on value X.
* **Range:** offers both lower and upper boundary of numerical values. Enter a value to at least one of them:
* Lowerbound = greater or equal to;
* Upperbound = lower or equal to;
* Fill both to have a range filter.
* Make sure to delete the 0 from the Upperbound if you wish to have a “greater than”, and vice versa for “lower than”.
* **Date Range:** offers a toggle with 2 options - exact dates (“from 1\1\2019 to 31\12\2019”) or relative to current time (“Last Month” or “Between two years ago and one year ago”). The configuration itself is done with a standard calendar date picker.
* \[Optional] **Button Label：** 按钮上显示的文本。此项为可选，但最佳实践是创建带有标签的按钮。

* \[Optional] **Button Label:** the text to display on the button. It’s optional, but it's best practice to create a button with a label.
* \[Optional] **Button color：** 默认颜色为灰色。要为按钮选择其他颜色，请使用 Blueprint 标准颜色（参见 https://blueprintjs.com/docs/#core/colors）或使用内部 Palantir Blueprint 库。基础颜色（"Blue"、"Red"、"Yellow" 等）也可以使用。
* 未选中的按钮将显示为淡色。只有在被点击后，它才会变为所选颜色。

* Date Range Button 没有选择 Button Color 的选项。

* \[Optional] **Button color:** The default color is grey. To select a different color for the button, use the Blueprint standard colors (see https://blueprintjs.com/docs/#core/colors) or use the internal Palantir Blueprint library. Basic colors (“Blue”, “Red”, “Yellow”, etc.) would also work.
* An un-selected button would have a faded color. Only once clicked, it would change to the chosen color.
* The Date Range Button does not have an option to pick a Button Color.
**常见问题和注意事项：**

**Common Issues and Notes:**
* 为了让用户获得更高的灵活性，建议使用以下方式：

* 使用 "Date Range Filter" 代替 "Date Range Button Filter"；

* 使用 "Multiselect Filter" 或 "Dropdown Filter" 代替 "Value List Button Filter"。

* 请注意，有 2 种方式可以说明 button filter 的作用：(I) 为按钮设置清晰的标签；(II) 添加一个 "Active Filter" 组件，它会显示所有 filter，包括通过点击 button filter 进行筛选的实际值。

* Button Filter 默认是关闭的，因此需要点击它才能使 filter 生效。

* 配置完成后，您需要在右侧配置编辑器设置中勾选 "allow cross-filtering" 复选框（详见上文），filter 才能作用于 Object View。

* To grant users with more flexibility, consider using:
* “Date Range Filter“ instead of the ”Date Range Button Filter“;
* “Multiselect Filter” or the “Dropdown Filter” instead of the “Value List Button Filter”.
* Note that there are 2 ways to indicate what a button filter does: (I) label the button well; (II) add an “Active Filter” widget, which shows all filters, including the actual values filtered by clicking on the button filters.
* The Button Filter is off by default, so that it has to be clicked for the filter to apply.
* Once configured, you would need to mark the checkbox “allow cross-filtering” in the configuration editor settings on the right side (see details above) in order for the filter to affect the Object View.
## Date Range Filter
Date Range Filter 允许用户基于特定的 date property，将 Object View 筛选限定在一个日期范围内。

配置完成后，一旦用户选择了一个日期范围并点击 **Submit**，Object View 中的所有 widget 都会受到影响。视图将仅显示所选 date property 中的日期落在该范围内的 object instance。

The Date Range Filter allows users to filter down their Object View to a range of dates, based on a specific date property.
Once configured, any widget in the Object View is affected once a date range is chosen and the user selects **Submit**. Views will only display object instances where the date in the chosen date property is within the range.
请注意，您应该插入您希望筛选的 object 的 object ID，该 object 通常是您当前正在配置的 object 的 Linked Object。

Note that you should insert the object ID of the object that you want to filter down, which is usually a Linked Object to the object that you are currently configuring.
配置完成后，其显示效果如下：
![Date Range Filter](/docs/resources/foundry/object-views/widgets_hp-daterange-filter.gif)
Once configured, this is how it looks:
![Date Range Filter](/docs/resources/foundry/object-views/widgets_hp-daterange-filter.gif)
### Configuration
* \[Required] **Object to Filter:** 选择此 filter 要应用的 Linked Object。

* \[Required] **Property to Filter:** 选择您希望用于筛选的 property：(I) 首先需要为该 filter 选择 object type；(II) 然后选择该 object 的您希望用于筛选的 property。

* 选中后，所有受此 filter 影响且与该 filter 属于同一 object type 的其他 widget，将从所有 Linked Objects 筛选限定为所选 date property 落在该日期范围内的那些 Linked Objects。

* \[Optional] **Label For Filter:** 将在 Object View 中显示在 filter 框旁边，供用户查看。

* \[Required] **Object to Filter:** Select the Linked Object for this filter to apply on.
* \[Required] **Property to Filter:** Select the property you want to filter down by: (I) you first need to select the object type for the filter; and then (II) select the property of that object that you wish to filter by.
* Once selected, all other widgets affected by this filter and related to the same object type as this filter, would filter down from all Linked Objects to only those where the chosen date property is within this dates range.
* \[Optional] **Label For Filter:** will be displayed to users in the Object View, next to the filter box.
**常见问题与注意事项：**

**Common Issues and Notes:**
* 配置完成后，您需要在右侧配置编辑器设置中勾选 "allow cross-filtering" 复选框（详见上文），filter 才能作用于 Object View。

* Once configured, you would need to mark the checkbox “allow cross-filtering” in the configuration editor settings on the right side (see details above) in order for the filter to affect the Object View.
## Linked Object Filter Sidebar
该 widget 创建了一种灵活的筛选体验，允许用户从该 Linked Object 的所有 property 中，通过任意特定的值集来筛选当前的 Object View。

This widget creates a flexible filtering experience, allowing the user to filter the current Object View by any specific set of values out of all properties of that Linked Object.
该 widget 提供了高自由度，但同时也对用户来说有更高的复杂度。它要求用户理解并了解 Linked Object 的 property，而所有其他 Filter Widget（例如 Dropdown Filter、Button Filter）则为用户预先配置好了这些选项。

This widget enables a high degree of choice, but also higher complexity for the user. It requires the user to understand and know the properties of the Linked Object, while all other Filter Widgets (e.g. Dropdown Filter, Button Filter) pre-configure them.
配置完成后，其显示效果如下：

Once configured, this is how it looks:
![Linked Object Filter Sidebar.gif](/docs/resources/foundry/object-views/widgets_hp-filter-sidebar.gif)
### Configuration
该 widget 的配置只需要选择您希望 Object View 用来进行筛选的 Linked Object。剩余的配置，即选择具体的 property 和筛选值，完全由用户决定，并且仅在其本地视图上生效。一旦用户刷新页面或切换到其他 object，他们就需要重新配置这些 filter。

Configuration of this widget only requires selecting the Linked Object that you wish the Object View to filter by. The rest of the configuration, i.e. choosing the specific properties and values to filter by, is completely up to the user and would apply locally on their view only. Once the user refreshes the page or turns to a different object, they would need to re-configure these filters again.
**常见问题与注意事项：**

**Common Issues and Notes:**
* 针对同一 property 选择的多个值之间为 "OR" 关系。不同 property 的值之间为 "AND" 关系。

* 示例：在处理 "Airport" object 时，Object View Editor 选择为 Linked Object "Arriving Flights" 添加一个 Linked Object Filter Sidebar。用户可以选择按 property "Month" 进行筛选，并仅选择 January 到 June；同时也可以按 "Carrier Name" 进行筛选，并选择 Delta Airlines 和 United Airlines。视图将被筛选限定为该机场的所有到达航班，这些航班需满足日期在 January 到 June 之间（January 或 February ... 或 June），并且承运商为 United 或 Delta。

* All values chosen for a certain property would have an “OR” statement between them. Values of different properties will have an “AND” statement between them.
* Example: When working with an “Airport” object, the Object View Editor chose to add a Linked Object Filter Sidebar for the Linked Object “Arriving Flights”. A user can select to filter down by Property “Month” and select only January to June; as well as filter by “Carrier Name” and select Delta Airlines and United Airlines. The view would be filtered down to all arriving flights within that airport that are between January and June (January or February ... or June), and are either United or Delta.
## Filter Sandbox Container
Filter Sandbox Container 使您能够将 widget 组织到一个 container 中，使其内部的所有 filter 被沙箱化，即它们只会影响并受该 container 内其他 widget 的影响。

The Filter Sandbox Container enables you to organize widgets into a container such that all filters inside it are sandboxed, meaning they only affect and are affected by other widgets inside this container.
### Configuration
添加 Filter Sandbox Container widget，然后通过点击 "Add Item" 将已有的 widget 添加到 container 中。

从 widget selector 中选择要添加的 widget。

Add the Filter Sandbox Container widget, then add existing widgets into the container by clicking on "Add Item".
Select the widget to add from the widget selector.
另一个配置选项是 filter set identifier（过滤器集标识符）。默认情况下，每个新的 filter sandbox（过滤器沙盒）都会生成一个新的唯一值。如果您希望与以下对象共享过滤器，可以更改该值：

The other configuration option is the filter set identifier. By default, a new unique value is generated for every new filter sandbox. It can be changed if you want to share filters with:
* Filter Sandbox Container（过滤器沙盒容器） - 为两者设置相同的 filter set identifier（过滤器集标识符）值。

* 另一个选项卡上的所有 widgets（小部件） - 在目标选项卡上启用跨区域过滤（cross-section filtering），并为其设置相同的 filter set identifier（过滤器集标识符）值。

* Filter Sandbox Container - set the same value of filter set identifier for both of them.
* All widgets on the other tab - enable cross-section filtering on the target tab and set the same value of filter set identifier for it.
**常见问题与说明：**

**Common Issues and Notes:**
* Cross-filtering（交叉过滤，即容器内的小部件之间相互影响和被影响的过滤）始终为此容器启用。

* 如果容器内的小部件需要 cross-filtering（交叉过滤），请使用此容器而非 Filter Container（小部件）来实现沙盒功能。如果只需让小部件受预定义过滤器影响，请在 Filter Container 中禁用订阅过滤器（subscription to filters）。

* 如果既需要沙盒内的交叉过滤，又需要预定义过滤器，请使用 Filter Sandbox Container，并在其中添加一个同时启用发布过滤器（publishing）和订阅过滤器（subscription）的 Filter Container。

* Cross-filtering (filters affecting and being affected by other widgets inside the container) is always enabled for this container.
* Use this container over Filter Container widget for sandboxing if you need cross-filtering for widgets inside the container. Use the Filter Container with subscription to filters disabled if you need widgets affected only by predefined filters.
* If you need both cross-filtering inside the sandbox and predefined filters, use Filter Sandbox Container and add a Filter
Container inside it with both publishing and subscription to filters enabled.
## Filter Container
此小部件可用于创建一个小部件的封闭子集，并对该子集应用 *预定义的一组过滤器*。

This widget enables creating a contained subset of widgets with a *pre-defined set of filters* applied only on them.
此过滤器子集可以在以下任意属性类型的组合上进行定义：(1) 文本（字符串）值列表；(2) 数值范围；和\或 (3) 日期范围。

This subset of filters can be defined on any combination of the following property types: (1) list of text (string) values; (2) numeric range; and\or (3) date range.
请勿将此小部件用作 filter sandbox（过滤器沙盒），因为它仅为支持预定义过滤器而构建。

Do not use this widget as a filter sandbox, as it was built to only support pre-defined filters.
注意：如需使用 filtering sandbox container（过滤沙盒容器）（即仅在容器内应用过滤器且不受外部过滤器影响），请改用 [Filter Sandbox Container](#filter-sandbox-container)。

Note: To have a filtering sandbox container (that is, to have filters apply only within a container and not be affected by external filters), use the [Filter Sandbox Container](#filter-sandbox-container) instead.
### Configuration
Filter Container 的配置包含两个部分：

The Filter Container configuration has two parts:
**第 1 部分 - 对容器内所有小部件应用预配置的过滤器**

**Part 1 - Apply pre-configured filters on all widgets within the container**
这些预定义过滤器默认情况下 *仅应用于容器内的小部件*。容器中的预定义过滤器可以是以下三种过滤器类型的任意组合：

These pre-defined filters would be applied by default *only to widgets within the container*. Pre-defined filters in the container can be any combination of the following three filter types:
* Value List（值列表） - 用于过滤文本属性（即字符串）

* Range（范围） - 用于过滤数值属性（即整数、双精度数）

* Date Range（日期范围） - 用于过滤到一组日期属性

* Value List - to filter text properties (i.e. string)
* Range - to filter numerical properties (i.e. integer, double)
* Date Range - to filter down to a list of date properties
对于每个默认过滤器，您需要配置以下内容：

For each default filter, you need to configure the following:
* \[必填] **Linked Object to Filter（要过滤的链接对象）：** 选择此过滤器要应用的 Linked Object。小部件配置仅提供链接到当前对象的对象（在 Ontology Manager 中定义）。

* \[必填] **Property to Filter（要过滤的属性）：** 选择您要按其过滤的属性：(I) 首先需要选择过滤器的 object type；然后 (II) 选择您希望按其过滤的该对象的 property。

* 选择后，此容器内与同一 object type 相关的所有其他小部件，将从所有 Linked Objects 过滤为仅包含符合过滤器条件属性值的对象。

* \[必填] 从此处开始，设置因过滤器类型（Text Value List、Numeric Range、Date Range）而异：

* **Value List（值列表）：** 手动输入您希望按其过滤的确切值列表，值与值之间使用 “OR” 关系。请注意，区分大小写，且顺序不能简单地重新排列。重新排列值的方式是删除并重新写入整个值列表。请注意，如果同时应用 “All” 选项和另一个特定值 X，则过滤器将仅应用于值 X。

* **Range（范围）：** 允许您设置数值范围的下边界和上边界。至少在其中一项中输入一个值：
* 下边界 = 大于或等于；
* 上边界 = 小于或等于；
* 同时填写两项以形成范围过滤。

* 如果您希望使用 “大于”，请确保删除 Upperbound 中的 0；“小于” 反之亦然。

* **Date Range（日期范围）：** 提供一个具有 2 个选项的切换 - 精确日期（“从 1\1\2019 到 31\12\2019”）或相对于当前时间（“上个月”或“两年前到一年年前之间”）。配置本身使用标准的日历日期选择器完成。

* \[可选] **Filter Label（过滤器标签）：** 用于文档记录的内部标签，不会出现在面向用户的任何位置。可选。

* \[Required] **Linked Object to Filter:** Select the Linked Object for this filter to apply on. The widget configuration only offers objects linked to the current object (as defined in the Ontology Manager).
* \[Required] **Property to Filter:** Select the property you want to filter down by: (I) you first need to select the object type for the filter; and then (II) select the property of that object that you wish to filter by.
* Once selected, all other widgets within this container, which are related to the same object type, would filter down from all Linked Objects to only those objects with properties value that the filter condition applies to.
* \[Required] From this point, the setting is different per filter type (Text Value List, Numeric Range, Date Range):
* **Value List:** manually type in the exact list of values you wish to filter by, with an “OR” statement between them. Note that it is case-sensitive and the order cannot be simply re-arranged. The way to re-arrange values is by deleting and re-writing the entire list of values. Note that if you apply both the “All” option as well as another specific value X, then the filter will only apply on value X.
* **Range:** This allows you to set both the lower and upper boundary of a range of numerical values. Enter a value to at least one of them:
* Lowerbound = greater or equal to;
* Upperbound = lower or equal to;
* Fill both to have a range filter.
* Make sure to delete the 0 from the Upperbound if you wish to have a “greater than”, and vice versa for “lower than”.
* **Date Range:** offers a toggle with 2 options - exact dates (“from 1\1\2019 to 31\12\2019”) or relative to current time (“Last Month” or “Between two years ago and one year ago”). The configuration itself is done with a standard calendar datepicker.
* \[Optional] **Filter Label:** An internal label for documentation, will not appear anywhere for the user. Optional.

> 📷 **[图片: Configuring Filter Container]**

> 📷 **[图片: Configuring Filter Container]**

**Cross-filtering 设置：**

**Cross-filtering settings:**
* ***Subscribe to filters for nested sections?（订阅嵌套区域的过滤器？）*** 如果希望 Filter Container 受到来自容器外部的过滤器影响——包括来自包含它的 Tab 的过滤器，以及其他与当前 Tab 共享 cross-filtering 的 Tab。这也会让它消费容器内的其他 filter widget，例如选中某根柱子的 Chart widget，或 multiselect filter。

* ***Publish filters from nested sections?（从嵌套区域发布过滤器？）*** 如果希望 Filter Container 内部的过滤器应用到容器外部——既应用到包含它的 Tab，也应用到其他与当前 Tab 共享 cross-filtering 的 Tab。这不适用于 predefined filters，而仅适用于容器内任何其他额外的 filter widget。

* ***Subscribe to filters for nested sections?*** If you wish the Filter Container to be affected by filters applied outside the container - both from the tab containing it, as well as other tabs sharing cross-filtering with the current tab. This would also make it consume other filter widgets within the container, e.g. Chart widget with a bar selected, or a multiselect filter.
* ***Publish filters from nested sections?*** If you wish the filters inside the Filter Container to apply outside the container - both on the tab containing it, as well as on other tabs sharing cross-filtering with the current tab. This does not apply to the predefined filters, but only to any additional filter widgets within the container.
如何使用这些开关？

How to use these toggles?
* 两个开关都关闭 —— predefined filters 仅在容器内生效，且容器既不发布也不消费任何其他过滤器——无论容器内还是容器外。

* 仅 Subscribe 开关开启 —— 容器受外部过滤器影响，但容器内的过滤功能不生效，除非是 predefined filters。

* 仅 Publish 开关开启 —— 容器内的 filter widget 仅作用于容器外部，而不在容器内生效。只有 predefined filters 在容器内生效。

* 两个开关都开启 —— Tab 上的所有过滤器到处生效，但此容器中的 predefined filters 除外。

* Both toggles off - predefined filters apply within the container only, but it neither publishes or consumes any other filters - internal or external to the container.
* Only Subscribe toggle on - the container is affected by external filters, but filtering within the container does not work, unless it is the pre-defined filters.
* Only Publish toggle on - filters widgets within the container apply only outside the container, and not within the container. Only the predefined filters apply within the container.
* Both toggles on - all filters on the tab apply everywhere, except for the pre-defined filters in this container.
**常见问题与注意事项：**

**Common Issues and Notes:**
* Pre-defined filters 仅在容器内生效，不会应用于容器外的任何 widget。这仅适用于这些 predefined filters，而不适用于可能在容器内配置的其他 filter widget。需要 sandbox container 功能？请尝试 [Filter Sandbox Container](#filter-sandbox-container)。

* “Filter Container”中的 predefined filters 在 UI 中对用户不可见，也无法被用户移除，除非按以下步骤操作：

* 在 Filter Container 中添加一个 “Active Filter” widget 以将其显示出来。

* 确保 “Enable removing default filters” 开关已开启（默认开启）。否则，即使使用 “Active Filter” 的移除选项，用户也无法移除这些过滤器。

* 在 filter container 内应用过滤器也会移除 filter widget 中不匹配的选项，例如 [Dropdown Filter](#dropdown-filter)。如果不希望出现此行为，请改用 [Filter Sandbox Container](#filter-sandbox-container)。

* The pre-defined filters are only applied within the container and do not apply on any widget outside the container. This is true only for these pre-defined filters, and not for other filter widgets which could be configured within the container. Looking for a sandbox container capability? Try [Filter Sandbox Container](#filter-sandbox-container).
* The pre-defined filters in the “Filter Container” will not be visible for the user in the UI, and will not be possible to remove by users, unless your follow the following steps:
* Add an “Active Filter” widget within the Filter Container to display it.
* Make sure the toggle of “Enable removing default filters” is switched-on (it is on by default). Otherwise, users cannot remove these filters, even with the “Active Filter“ removal option.
* Applying filters inside a filter container will also remove non-matching options in filter widgets, such as [Dropdown Filter](#dropdown-filter). If this behavior is not desired, use [Filter Sandbox Container](#filter-sandbox-container) instead.
**第二部分 - 作为 widget 容器的 Filter Container**

**Part 2 - Filter Container as a Container of widgets**
像配置其他任何容器一样配置此容器内的视图。您添加的每个 widget 都会订阅 Filter Container 的 predefined filters，以及任何其他被定义为对其生效的过滤器。

Configure views within this container as with any other container. Every widget you add would be subscribed to the pre-defined filters of the Filter Container, as well as any other filter defined to affect it.
点击 “Add Section” 后，您将获得与在主 Object View 上或在其他带有嵌套 Tab 的 widget（例如任何 Container widget）上使用 “Add Section” 时相同的配置体验。

Once you click on “Add Section”, you get the same configuration experience as with any other “Add Section” on the main Object View or on other widgets with nested tabs (e.g. any Container widget).
**Section layout（区域布局）：**

**Section layout:**
这决定了 Filter Container 内的 widget 是垂直堆叠（一个接一个，默认），还是水平排列（一个接一个，从左到右）。

This determines whether widgets within the Filter Container would be stacked vertically (one under the other, this is the default) or horizontally (one next to the other, from left to right).
## Active Filters
该 widget 显示 Object View 上当前应用的所有过滤器的摘要，并允许用户移除单个过滤器或清除所有过滤器。该过滤器无需任何配置。

This widget displays a summary of all filters that are currently applied on the Object View, and allows the user to either remove individual filters or clear all filters. There is no configuration required for this filter.
Active Filter 是一个有用的视觉提示，帮助用户了解其 Object View 上当前哪些过滤器处于激活状态。一旦 Object View 包含多个过滤 widget（包括使用图表进行过滤），特别是当您使用 Filter Container 或 Button Filter 时，可见性强的 active filters 对用户体验至关重要。

Active Filter is a useful visual indication for the user to understand which filters are currently active on their Object View. Once your Object View contains several filtering widgets (filtering using charts included), and especially if you use Filter Container or Button Filter, the visibility of active filters is important for the user experience.
配置完成后，其外观类似于下方可交互的 widget，左侧带有一个 filter icon。在本例中，它受不同 filter widget 的影响：

Once configured, it will look like the interactive widget below, with a filter icon to the left. In this example, it is affected by the different filter widgets:
![filter-summary](/docs/resources/foundry/object-views/widgets_hu-filter-summary-1.gif)
## Configuration
Active Filter widget 无需任何配置，只需将其作为一个新 section 添加即可。

There’s no configuration for the Active Filter widget. Simply add it as a new section.
**常见问题和注意事项：**

**Common Issues and Notes:**
* 此 widget 将显示来自所有共享 cross-section 和 cross-tabs 筛选功能的所有 section 所应用的所有筛选器。

* 某些筛选 widget 可能无法与此 widget 交互。目前，它无法移除由 Dropdown 筛选器应用的筛选器，用户仍需要在 dropdown 中手动更改值。当 Dropdown 默认将您限制为一个值时这是合理的，但即使在启用了 "All" 选项时仍然适用。

* This widget will display all filters applied from all sections sharing a cross-section and cross-tabs filtering.
* Some filter widgets might not interact with this widget. Currently, it will not remove a filter applied by the Dropdown filter, and users would still need to manually change the value in the dropdown. This makes sense when the Dropdown limits you by default to one value, but it still applies even when the “All” option is enabled.