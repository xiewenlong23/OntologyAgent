<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/search-objects/
---
# Search for objects
从 Object Explorer [home page](/docs/foundry/object-explorer/getting-started/) 使用全局搜索栏进行的搜索结果将显示在搜索结果页面上:

The results of a search with the global search bar from the Object Explorer [home page](/docs/foundry/object-explorer/getting-started/) will be shown on the search result page:
您的查询在搜索栏中可见且可编辑(如下方 A 所示)。

Your query is visible and editable in the search bar (shown as A below).
页面分为多个标签页 **(B)**：

The page is divided into tabs **(B)**:
* **All** 标签页默认显示,包含所有结果。
* 匹配结果可以筛选到不同的标签页中:

* Objects **(C)**,
* Object types **(D)**,以及

* Artifacts **(E)**。
* The **All** tab is displayed by default and contains all results.
* Matching results can be filtered down into separate tabs:
* Objects **(C)**,
* Object types **(D)**, and
* Artifacts **(E)**.
此搜索结果页面还包含一个 [sidebar](#navigate-using-the-sidebar)(下图中的 **F**)。

This search results page also contains a [sidebar](#navigate-using-the-sidebar) (**F** below).
![Searching](/docs/resources/foundry/object-explorer/OE_search_results_general_annotated.png)
## Navigate using the sidebar
这些结果均按其类型进行分类。左侧的导航菜单(如上图中的 **F** 所示)可以帮助您在不同分类之间导航。

These results are all categorized by their type. The navigation menu to the left (shown as **F** in the image above) can help you navigate the different categories.
选择任何分区的标题也会将您筛选到该类型的结果。在 **All results** 视图中,如果某个类型的结果超过默认显示数量(如下图中的 **1** 所示),此操作还会向您显示该类型的所有结果。

Selecting the title of any section will also filter you to results of that type. This will also show you all of the results of that type in the event that there are more than the default number shown when in the **All results** view (indicated by **1** in the image below).

> 📷 **[图片: Sidebar]**

> 📷 **[图片: Sidebar]**

* 第一项 **All results**(如上图中的 **1** 所示)显示每个分类的匹配结果样本。默认情况下,进入页面时此项处于激活状态。

* 接下来是 **"Object type filters" (2)**。点击其中任意一个,将显示特定 object type 的更长匹配列表。点击分区底部的 **"View X other filters >"** 将把标签页从 "All" 切换到 "Objects",您可以在那里浏览完整的 object 结果列表和筛选器。

* **"Object type groups" (3)** 按关联的 group 筛选结果。点击分区底部的 **"View all filters >"** 将把标签页从 "All" 切换到 "Object types",您可以在那里浏览完整的 object types 结果列表。

* 最后是 **"Artifacts" (4)** 的匹配项,分为 "Explorations & Lists"、"Comparison Views" 和 "Modules"。点击分区底部的 **"View all filters >"** 将把标签页从 "All" 切换到 "Artifacts",您可以在那里浏览完整的结果列表。

* The first item, **All results** (shown as **1** in the image above), displays a sample of matches for each category. This is active by default when landing on the page.
* Next are **“Object type filters” (2)**. Clicking on any of them will show a longer list of matches for the specific object type. Clicking on **“View X other filters >”** at the bottom of the section will switch the tab from “All” to “Objects”, where you can explore the full list of object results and filters.
* **“Object type groups” (3)** filters the results by the associated group. Click on **“View all filters >”** at the bottom of the section to switch the tab from “All” to “Object types”, where you can explore the full list of object types results.
* Lastly are matches on **“Artifacts” (4)**, divided into "Explorations & Lists", "Comparison Views", and "Modules". Click on **“View all filters >”** at the bottom of the section to switch the tab from “All” to “Artifacts”, where you can explore the full list of results.
## Types of results
Object Explorer 搜索栏会在平台上的所有 Objects(上图中的 **(C)**)以及与 object 相关的资源(如 Object types **(D)**、保存的 Explorations、Lists、Comparisons 和 Modules **(E)**)中进行搜索。

The Object Explorer search bar searches across all Objects in the platform (**(C)** in the top image), as well as object-related resources such as Object types **(D)**, saved Explorations, Lists, Comparisons, and Modules **(E)**.
### Sorting results
在单个 object 结果分区中,结果按以下方式排序:

Within the individual object results section, the results are sorted as follows:
* 所有 prominent object types 都会显示在 non-prominent object types 之前。

* 在 prominent 和 non-prominent 结果中,object types 按该类型的单个 object 结果数量(升序)进行排序。换言之,结果最少的 prominent object type 最先显示,然后是结果较多的 prominent object types,接着是结果最少的 non-prominent object type(与其他 non-prominent types 相比),以此类推。

* All prominent object types are shown before non-prominent object types.
* Within the prominent and non-prominent results, object types are sorted (in ascending order) by the number of individual object results for that type. In other words, the prominent object type with the least results will display first, then prominent object types with more results, then the non-prominent object type with the least results (compared to other non-prominent types), and so on.
> **ℹ️ 注意**

> 在 Object Explorer 中,此处或其他任何位置都不会显示 hidden object 或 property types。
> **ℹ️ 注意**

> No hidden object or property types will be displayed as search results here or elsewhere in Object Explorer.
### Exploring objects linked to a particular result
对于单个 objects 的匹配项(上图中的 **2**),将鼠标悬停在结果上可为您提供启动 object exploration 的选项,以通过特定 link 探索到该单个结果。

For matches on individual objects (**2** in the image above), hovering over the result gives you options for starting an exploration of objects across a particular link to that individual result.
示例:如果您搜索机场 "SFO",您可以将鼠标悬停在结果上,并启动对抵达该机场的航班的 exploration。

Example: If you search for the airport “SFO”, you can hover over the result and start an exploration on flights arriving at the airport.
![Search Around](/docs/resources/foundry/object-explorer/OE_search_results_search_around.png)