<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/search-syntax/
---
# Search syntax
Object Explorer 支持跨所有 objects 及其 properties 的搜索。为了帮助您找到所需内容,此页面描述了 [global search bar](/docs/foundry/object-explorer/getting-started/#global-search-bar-a) 的搜索语法。

Object Explorer supports search across all objects and their properties. To help you find what you need, this page describes search syntax for the [global search bar](/docs/foundry/object-explorer/getting-started/#global-search-bar-a).
### Quotation marks
默认情况下,在搜索栏中输入的各个单词将彼此独立地进行搜索。例如,搜索 `yellow cab` 将返回所有 property 值匹配 `yellow` 或 `cab` 的 objects。

By default, individual words entered into the search bar will be searched for independently of each other. For example, searching `yellow cab` will return all objects with property values that match either `yellow` or `cab`.
此行为可以使用引号进行更改。在 Object Explorer 中搜索 `"yellow cab"` 将返回所有在一个或多个 property 值中包含确切短语 `yellow cab` 的对象。与搜索单个词相比,此类短语搜索通常返回的结果更少。

This behavior can be altered using quotation marks. Searching Object Explorer for `"yellow cab"` will return all objects that have the exact phrase `yellow cab` in one or more property values. Searching for phrases like this will typically yield fewer results than searching for individual words.
### Logical operators (not/and/or)
**NOT**、**AND** 和 **OR** 运算符可用于增强 Object Explorer 中的文本搜索。

The operators **NOT**, **AND**, and **OR** can be used to enhance text search in Object Explorer.
#### Join operators
使用 **AND** 和 **OR** 作为连接运算符来组合两个不同的搜索条件。具体来说,可以使用 **AND** 来搜索同时满足两个条件的项,而 **OR** 用于搜索满足至少一个条件的项。例如,要搜索涉及 Manhattan 和 Brooklyn 的出租车行程,可以搜索 `Manhattan AND Brooklyn`。类似地,要搜索涉及 Manhattan 或 Brooklyn 的出租车行程,请搜索 `Manhattan OR Brooklyn`。

Use **AND** and **OR** as join operators to compound two different search criteria. Specifically, you can use **AND** to search for an item that satisfies both criteria, while **OR** searches for those that satisfy at least one criterion. For example, to search for taxi rides that involve both Manhattan and Brooklyn, you can search for `Manhattan AND Brooklyn`. Similarly, to search for taxi rides that involve either Manhattan or Brooklyn, search for `Manhattan OR Brooklyn`.
#### Negation operators
与同时应用于多个条件的连接运算符(如 `dogs AND cats` 或 `vanilla OR chocolate`)不同,**NOT** 运算符应用于单个条件,用于搜索*不*满足该条件的元素。

Unlike the join operators applied to multiple criteria at once (such as `dogs AND cats` or `vanilla OR chocolate`), the **NOT** operator applies to a single criteria to search for elements that do *not* satisfy the criteria.
例如,如果搜索 `NOT Brooklyn`,则 Object Explorer 会返回所有搜索结果,*除了*提及 Brooklyn 的结果。**NOT** 运算符也可以应用于复合条件。另外,搜索 `NOT (Manhattan OR Brooklyn)` 会返回所有搜索结果,*除了*提及 Brooklyn 或 Manhattan 的结果。

For example, if you search for `NOT Brooklyn`, then Object Explorer returns results for all searches *except* those that mention Brooklyn. The **NOT** operator can also be applied to compounded criteria. Alternatively, searching for `NOT (Manhattan OR Brooklyn)` returns all search results *except* those that mention Brooklyn or Manhattan.
#### Combining operators
使用引号创建的短语也可以纳入搜索中。例如,`"yellow cab" AND Manhattan` 是一个有效的表达式。

Phrases created using quotation marks can also be incorporated into a search. For example, `"yellow cab" AND Manhattan` is a valid expression.
逻辑运算符也可以使用括号构建为更复杂的表达式。例如,以下搜索会返回不引用 Manhattan 但引用 yellow 或 green cabs 的对象:`("yellow cab" OR "green cab") AND (NOT Manhattan)`。

Logical operators can also be structured into more complex expressions using parentheses. For example, this search returns objects which do not reference Manhattan but do reference either yellow or green cabs: `("yellow cab" OR "green cab") AND (NOT Manhattan)`.
### Wildcards
* `?`:问号可用于替换单个字符

* 搜索 `qu?ck` 将返回 `quick`、`quack`、`qu4ck` 等结果
* `*`:星号可用于替换零个或多个字符

* 搜索 `bro*` 将返回 `bro`、`brother`、`broadcasting` 等结果

* 也支持前导通配符:搜索 `*smith` 将返回 `smith`、`Goldsmith`、`Blacksmith` 等结果。前导通配符需要在 **Ontology Manager** 中字符串 property 上启用 **Enable leading wildcards** render hint。有关更多信息,请参阅 [Render hints](/docs/foundry/object-link-types/metadata-render-hints/)。

* `?`:  A question mark can be used to replace a single character
* Searching for `qu?ck` would return results for `quick`, `quack`, `qu4ck`, and so on
* `*`: An asterisk can be used to replace zero or more characters
* Searching for `bro*` would return results for `bro`, `brother`, `broadcasting`, and so on
* Leading wildcards are also supported: searching for `*smith` would return results for `smith`, `Goldsmith`, `Blacksmith`, and so on. Leading wildcards require the **Enable leading wildcards** render hint to be enabled on the string property in the **Ontology Manager**. For more information, see [Render hints](/docs/foundry/object-link-types/metadata-render-hints/).
> **ℹ️ 注意**

> 不支持同时使用前导和尾部通配符(`*term*`)。您可以使用前导通配符(`*term`)或尾部通配符(`term*`),但不能同时使用两者。如果需要执行此类查询,请考虑使用替代工具,例如 [Contour](/docs/foundry/contour/overview/)。
> **ℹ️ 注意**

> Combined leading-and-trailing wildcards (`*term*`) are not supported. You can use either a leading wildcard (`*term`) or a trailing wildcard (`term*`), but not both at the same time. If you need to perform queries of this kind, consider using an alternative tool such as [Contour](/docs/foundry/contour/overview/).
有关平台中文本搜索工作原理的详细说明,包括分析器行为以及 Workshop 和 Functions API 中的搜索功能,请参阅 [Understanding text search](/docs/foundry/object-explorer/understanding-text-search/)。

For a detailed explanation of how text search works across the platform, including analyzer behavior and search capabilities in Workshop and the Functions API, see [Understanding text search](/docs/foundry/object-explorer/understanding-text-search/).
### Fuzzy searching
在搜索词末尾使用 `~` 运算符可对相似词及精确匹配执行"模糊"匹配。例如,`quikc~` 将返回 `quick` 和 `quack` 的结果。

Use the `~` operator at the end of a search term to perform a "fuzzy" match for similar terms and also exact matches. For example, `quikc~` would return results for `quick` and `quack`.