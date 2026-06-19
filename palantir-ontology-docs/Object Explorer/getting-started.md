<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/getting-started/
---
# Getting started
下方的主页是打开 Object Explorer 时显示的页面。它是一个导航中心，用户可以从中开始探索对象，无论是有特定问题需要解答，还是希望发现可探索的 Object Type。

The home page below is shown when opening Object Explorer. It is an orientation hub where one can start exploring objects, either with a specific question in mind or to discover possible object types to explore.
从此视图中，用户可以执行以下主要操作：

From this view, user can perform the following primary actions:
* 通过搜索栏 **(A)** 在平台 objects 范围内的所有内容中进行搜索。

* 探索一组 Object Type **(B, C, D)**。

* 预览特定的 Object Type **(E)**。

* 选择特定的 Object Type 进行探索 **(F)**。

* Searching across everything in the objects realm of the platform from the search bar **(A)**.
* Exploring a group of object types **(B, C, D)**.
* Previewing a specific object type **(E)**.
* Selecting a specific object type for exploration **(F)**.

> 📷 **[图片: Object Explorer home page]**

> 📷 **[图片: Object Explorer home page]**

## Global search bar (A)
全局搜索栏可对整个 Ontology 执行搜索。它可用于搜索单个对象、Object Type、保存的探索或 modules（基于 objects 的应用程序）。

The global search bar performs searches across all of the Ontology. It can be used to search for individual objects, object types, saved explorations, or modules (objects-backed applications).
> **⚠️ 警告**

> 如果 Ontology 中包含超过 250 个用户可发现的 Object Type，则关键字搜索将仅限于前 250 个 Object Type。要搜索特定的 Object Type 或一组 Object Type，您必须使用 [下文](#group-exploration-b-c-d) 中描述的功能。
> **⚠️ 警告**

> If the Ontology contains more than 250 object types that a user may discover, the keyword search will be limited to the first 250 object types. To search a specific object type or a group of object types you must leverage the functionality described [below](#group-exploration-b-c-d).

> 📷 **[图片: Global search bar]**

> 📷 **[图片: Global search bar]**

这些搜索会返回搜索词 **(1)** 匹配以下条件的结果：

These searches bring back results where the search terms **(1)** match the following:
* object type、property type、saved exploration 的标题和/或 metadata（例如 name、description 等）。

* 任何单个 object 的 title 或 property。

* The titles and/or metadata (e.g. name, description, etc.) of object types, property types, saved explorations.
* Any title or property of individual objects.
部分匹配项（即 object type 和 property type 结果）会作为 type-ahead 结果 **(3)** 立即显示。若要查看所有匹配项，请点击第一个选项 **Search for...** **(2)**，系统会将您重定向到 [search results page](/docs/foundry/object-explorer/search-objects/)。

Some matches, namely object type and property type results, will be shown immediately as type-ahead results **(3)**. To see all matches, click the first option **Search for...** **(2)** to be redirected to the [search results page](/docs/foundry/object-explorer/search-objects/).
您可以在 [search syntax guide](/docs/foundry/object-explorer/search-syntax/) 中了解更多关于搜索栏 search syntax 的信息。

You can learn more about search syntax for the search bar in the [search syntax guide](/docs/foundry/object-explorer/search-syntax/).
## Group exploration (B, C, D)
用户可访问的所有 object type 都显示在搜索栏下方的 [configurable object groups](/docs/foundry/object-explorer/configure/) 中。使用侧边导航 **(C)** 选择并导航到某个 group。

All object types accessible to a user are displayed under the search bar in [configurable object groups](/docs/foundry/object-explorer/configure/). Use the side navigation **(C)** to select and navigate to a group.
### Search with object type groupings (B)
Object type 分组也会反映在全局搜索栏中。左侧选项卡中提供预配置的 groups，您可以在 **Object types** 下快速配置自定义 groups。在此选择一个 object type group，使您能够在选择某个 object type 进行探索之前，对一组更精细的 object types 执行搜索。

Object type groupings are also reflected in the global search bar. Preconfigured groups are available in the left side tab, and custom groups can be quickly configured under **Object types**. Selecting an object type group here allows you to perform searches on a more refined set of object types before selecting one for exploration.

> 📷 **[图片: Object Type Groups]**

> 📷 **[图片: Object Type Groups]**

### Explore object type groups on a graph (D)
该 graph 旨在帮助用户探索 Ontology 并理解特定 group 内 object types 之间的连接。

The graph is designed to help users explore the Ontology and understand the connections between the object types within a specific group.
点击 **Graph** 图标可查看 group graph，其中显示该 group 内 object types 之间的 links 以及指向其他 object type groups 的 links **(1)**。在此视图中，您还可以移除 object type groups **(2)** 并更改 graph 的布局 **(3)**。

Click on the **Graph** icon to view the group graph, which displays the links within the object types in the group and links to other object type groups **(1)**. In this view, you can also remove the object type groups **(2)** and change the layout of the graph **(3)**.

> 📷 **[图片: Object type group graph]**

> 📷 **[图片: Object type group graph]**

点击 link 符号（<->）可显示 object types 之间 link 的类型 **(4)**。

Click on a link symbol (<->) to show the type of links between the object types **(4)**.

> 📷 **[图片: Object type graph link]**

> 📷 **[图片: Object type graph link]**

选择单个 object 以查看菜单 **(5)**，该菜单允许您探索 [object type preview](#preview-object-types-e) 或开始一次 exploration。

Select a single object to view a menu **(5)** that allows you to explore the [object type preview](#preview-object-types-e) or start an exploration.

> 📷 **[图片: Object type graph menu]**

> 📷 **[图片: Object type graph menu]**

## Preview object types (E)
点击 object preview 可访问 object type 的快速视图（无需进入更全面的 exploration 页面）。在 preview 中，您可以找到有关该 object type 的信息 **(1)**，包括 description、properties 和 linked object types。点击 **Start Exploration** **(2)** 即可开始对该 object type 进行新的 Exploration。

Click on an object preview to access a quick view of an object type (without moving into the more comprehensive exploration page). In the preview, find information about the object type **(1)**, including the description, properties, and linked object types. Click **Start Exploration** **(2)** to start a new Exploration of the object type.

> 📷 **[图片: Object type preview]**

> 📷 **[图片: Object type preview]**

### Add object type as favorite (F)
可以通过点击 Object type 卡片上的星标图标 **(1)** 将其添加为收藏。收藏会显示在侧边导航顶部的一个专门分组中。

Object types can be added as a favorite by clicking the star icon on their card **(1)**. Favorites show up in a dedicated group at the top of the side navigation.
> **ℹ️ 注意**

> 收藏的 Object Type 也会显示在界面底部的 "All object types" 完整列表中。
> **ℹ️ 注意**

> Favorites will also be shown in the full list of “All object types” at the bottom of the interface.

> 📷 **[图片: Explorer]**

> 📷 **[图片: Explorer]**

### Explorations & lists (G)
已保存的探索和列表将显示在 Home 页面顶部，方便访问。它们也可以在 **Artifacts** 选项卡中找到。

Saved explorations and lists will appear at the top of the Home page for easy accessing. They can also be found in the **Artifacts** tab.