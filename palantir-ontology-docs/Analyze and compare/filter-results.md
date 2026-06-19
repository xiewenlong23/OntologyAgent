<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/filter-results/
---
# Filter results
一旦你开始一次 [search](/docs/foundry/object-explorer/search-objects/)，你将进入一个探索视图，在该视图中你可以进行进一步的筛选。

Once you have started a [search](/docs/foundry/object-explorer/search-objects/), you are taken to an exploration view where you can conduct further filtering.
## Search bar
搜索栏是筛选当前 object 集合的核心枢纽。点击搜索栏以展开搜索菜单。在那里，你可以使用一些筛选选项：

The search bar is the central hub for filtering the current set of objects. Click into the search bar to expose the search menu. From there, a few filtering options are available:
![Search](/docs/resources/foundry/object-explorer/explore_search.png)
### Filtering by properties (of the main object type)
→ 你知道要按哪个 property 进行筛选吗？

→ You know what property you want to filter on?
> Example: “I want to filter on the language of my employees”
在搜索菜单中，你可以找到按字母顺序排列的所有 properties 列表 **（B）**（以及可选的描述信息）。

In the search menu, you can find a list of all properties **(B)** (and optionally their descriptions) sorted alphabetically.
![Search](/docs/resources/foundry/object-explorer/explore_search_filtered.png)
在搜索栏 **(A)** 中输入内容以搜索特定的 property 类型。选择所需的 property 后，弹窗将允许您为该 property 选择要筛选的值。输入体验因 property 类型（数值、文本、日期等）而异。对于文本 property（例如 language），可以通过在标签中输入内容来筛选选项。

Type in the search bar **(A)** to search for specific property types. When the desired property is selected, a pop-over will you allow to chose values to filter on for that property. The input experience varies based on the type of the property (numeric, text, date, etc.). For text properties (e.g. language), options can be filtered by typing in the pill.
→ 您知道值但不知道它属于哪个 property？

→ You know the value but not which property it belongs to?
> Example: “I want to filter for flights to Los Angeles“
在搜索栏中输入值（例如 "Los Angeles"）。如果该值存在于当前 object set 中，筛选条件 "where Destination City Name is Los Angeles" 将出现在搜索菜单的右侧。

Type the value (e.g. “Los Angeles”) in the search bar. If the value exists in the current object set, the option to filter “where Destination City Name is Los Angeles” will be available in the right hand side of the search menu.
### Filtering by keywords
关键字搜索在 object type 的所有 property 或特定 property 上均受支持。要对包含您搜索词的 **任意** property 执行关键字搜索，请在搜索栏中输入并使用 Enter 键。通过单击筛选标签 "Has keywords" 来修改生成的筛选条件。

Keyword searches are supported across all of an object type's properties or a specific property. To perform a keyword search across **any** properties that contain your search term, type in the search bar and use the Enter key. Modify the resulting filter by clicking on the filter pill "Has keywords".
要对某个 property 执行关键字搜索，请选择一个文本 property，输入您的查询，然后使用 Enter 键或在筛选图表中切换到 "Keyword" 选项卡。

To perform a keyword search on a property, select a text property, type your query, and use the Enter key or switch to the "Keyword" tab in the filter chart.
![Keyword](/docs/resources/foundry/object-explorer/explore_keyword_property.png)
默认情况下，关键字搜索精确匹配整个词或短语，不匹配前缀或后缀。要执行前缀搜索，请参阅下面的 **"Starts with"** 修饰符。

By default, keyword searches match on the exact word or phrase and do not match on prefixes or suffixes. To perform a prefix search, see the **"Starts with"** modifier below.
#### Adding Term Modifiers
对于给定的搜索词，有三个选项可用于修改查询。为了保持一致性，请使用开关来控制这些修饰符，而不是在此下拉列表中编辑术语。

For a given search term, three options are available to modify the query. For consistency, use the toggles to control these modifiers rather than editing the terms in this dropdown.
* **"Is not"**：对当前搜索词取反，仅查找其 property 中不包含该搜索词的 object。等同于输入 `NOT term`。

* **"Starts with"**：执行通配符搜索，查找其 property 以当前搜索词开头的 object。等同于输入 `term*`，将匹配 "term" 以及像 "terminal" 这样的单词。要进行后缀匹配（前导通配符搜索），必须在 property 上启用 **Enable leading wildcards** 渲染提示。有关通配符搜索的详细信息和限制（包括为什么多词通配符查询不匹配），请参阅 [Understanding text search](/docs/foundry/object-explorer/understanding-text-search/#common-pitfalls)。

* **"Exact"**：执行对整个搜索词的搜索，包括按其确切位置的空格。对 "my search term" 执行 Exact 搜索将仅查找 "my search term" 这一短语，而不会查找像 "my search for a term" 这样的短语。

* **"Is not":** Negates the current search term, looking only for objects whose properties do not contain it. Equivalent to typing `NOT term`.
* **"Starts with":** Performs a wildcard search, looking for objects with properties that start with the current search term. Equivalent to typing `term*`, and will match on both "term" and words like "terminal". For suffix matching (leading wildcard search), the **Enable leading wildcards** render hint must be enabled on the property. For details and limitations of wildcard search (including why multi-word wildcard queries do not match), see [Understanding text search](/docs/foundry/object-explorer/understanding-text-search/#common-pitfalls).
* **"Exact":** Performs a search for the entire search term, including spaces in their exact position. Performing an Exact search for "my search term" will look only for the phrase "my search term", not phrases like "my search for a term".
#### Adding Logical Operators (AND/OR)
选择 "And" 或 "Or" 将向您现有的查询添加一个新的搜索词，并通过相应的逻辑运算符连接。添加新词后，单击某个词以对其进行编辑。

Selecting “And” or “Or” will add a new search term to your existing query connected by the corresponding logical operator. After adding a new term, click on a term to edit it.
![Adding a new term](/docs/resources/foundry/object-explorer/new_search_term.png)
搜索词和逻辑运算符可以嵌套，以执行更复杂的查询。请参阅下面的示例，了解 OR 中嵌套的 AND。另请注意，未编辑时，给定搜索词的修饰符以紧凑视图显示。

Search terms and logical operators can be nested to perform more complicated queries. See below for an example of a nested AND within an OR. Also note that modifiers for a given search term display in a compact view when not being edited.
![Nested Keywords](/docs/resources/foundry/object-explorer/nested_search_terms.png)
单击 "And"/"Or" 标签以切换运算符。请注意，如果两个相邻层级上的运算符变得相同，则筛选条件将简化为单层嵌套。

Click on an “And”/“Or" tag to flip the operator. Note that if operators on two adjacent levels become the same, the filter will simplify to a single level of nesting.
### Filtering on links
与可以直接对当前 object property 应用筛选器的方式一样，也可以基于 object 的关系对其进行筛选。要选择用于筛选的关系，请在搜索菜单的左侧面板中进行选择。

In the same way that filters can be applied directly on current object properties, one can filter objects based on their relations. To choose a relation for filtering, select in the left panel of the search menu.
要搜索具有特定 link 的 object，请选择 "Has Link" 选项，如下高亮显示的 "Has Flight Delay Event"。此筛选器可用于显示具有关联 link 的 object，或不具有关联 link 的 object。

To search for objects that have a particular link, select the "Has Link" option, highlighted below as "Has Flight Delay Event". This filter can be used to show either objects that have the associated link, or objects that do not have the associated link.
> Example: “Flights with an associated delay event.”
![Flights with a delay](/docs/resources/foundry/object-explorer/has_link.png)
要搜索其关联 object 具有特定 property 的 object，请在搜索菜单面板的左侧选择该关系。然后，选择要筛选的 property 类型。

To search for objects whose linked objects have a specific property, select the relation in the left side of the search menu panel. From there, choose a property type to filter.
> Example: “Flights on an Aircraft that were manufactured in 2018.”
![Flights property search](/docs/resources/foundry/object-explorer/linked_to_property.png)
还可以搜索链接到其他特定 object 的 object。例如，在选择一个 link 后，选择选项 "Filter by Airline"。这将打开一个针对到特定 object 的 link 的筛选器。关联的 object 在生成的 listogram 中按其 title 显示。

It is also possible to search for objects that have links to other specific objects. For example, after selecting a link choose the option "Filter by Airline". This opens a filter for links to specific objects. Linked objects are displayed by their title in the resulting listogram.
> Example: "Flights operated by a particular airline."
![Flights linked to airline](/docs/resources/foundry/object-explorer/linked_to_object.png)