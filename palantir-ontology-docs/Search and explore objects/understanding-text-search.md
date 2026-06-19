<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/understanding-text-search/
---
# Understanding text search
Foundry 平台中的文本搜索(包括在 Object Explorer、Workshop 和 Functions API 中)依赖于一个底层搜索引擎,该引擎通过称为 **analyzer**(分析器)的机制处理文本。了解分析器的工作方式有助于您编写更有效的搜索查询,并在应用程序中构建更好的搜索体验。

Text search across the Foundry platform, including in Object Explorer, Workshop, and the Functions API, relies on an underlying search engine that processes text through a mechanism called an **analyzer**. Understanding how analyzers work helps you write more effective search queries and build better search experiences in your applications.
## How text analysis works
当字符串 property 被索引用于搜索时,平台会通过 analyzer 处理其值。默认 analyzer 称为 **standard analyzer**(标准分析器)(请参阅 [Lucene StandardAnalyzer ↗](https://lucene.apache.org/core/10_2_0/core/org/apache/lucene/analysis/standard/StandardAnalyzer.html)),其执行以下步骤:

When a string property is indexed for search, the platform processes its value through an analyzer. The default analyzer, called the **standard analyzer** (see [Lucene StandardAnalyzer ↗](https://lucene.apache.org/core/10_2_0/core/org/apache/lucene/analysis/standard/StandardAnalyzer.html)), performs the following steps:
1. 在空白和标点符号边界处将文本拆分为单个单词,称为 **token**(词元)。

2. 将所有 token 转换为小写。

1. Splits the text into individual words, called **tokens**, at whitespace and punctuation boundaries.
2. Converts all tokens to lowercase.
例如,property 值 `The Quick Brown Fox` 被存储为 token `the`、`quick`、`brown` 和 `fox`。当您搜索 `quick` 时,搜索引擎会将此 token 与存储的 token 进行匹配并找到匹配项。

For example, a property value of `The Quick Brown Fox` is stored as the tokens `the`, `quick`, `brown`, and `fox`. When you search for `quick`, the search engine matches this token against the stored tokens and finds a match.
这种基于 token 的方法具有以下重要影响：

This token-based approach has important implications:
* 默认情况下，搜索是 **不区分大小写** 的，因为在索引过程中所有 token 都会被转换为小写。

* 非短语查询会独立匹配 token。例如，搜索 `brown fox` 会分别评估 `brown` 和 `fox` 这两个 token，因此它会匹配包含这两个 token 的任何 Property，无论它们的顺序或位置如何。若要求 token 按顺序一起出现，请使用短语搜索（`"brown fox"`）。

* 搜索 `rown` **不会** 匹配 `brown`，因为 `rown` 不是一个完整的 token。

* Searches are **case-insensitive** by default because all tokens are converted to lowercase during indexing.
* Non-phrase queries match tokens independently. For example, a search for `brown fox` evaluates the `brown` and `fox` tokens separately, so it matches any property containing both tokens regardless of order or proximity. To require the tokens to appear together in order, use a phrase search (`"brown fox"`).
* A search for `rown` does **not** match `brown` because `rown` is not a complete token.
### Analyzer types
字符串 Property 使用的分析器在 Ontology 中进行配置。可用的分析器类型如下：

The analyzer used for a string property is configured in the Ontology. The following analyzer types are available:
| Analyzer | Behavior | Example value | Resulting tokens |
| ----- | ----- | ----- | ----- |
| Standard (default) | Splits on whitespace and punctuation, converts to lowercase | `The Quick-Brown Fox` | `the`, `quick`, `brown`, `fox` |
| Simple | Splits on any non-letter character, converts to lowercase (digits and punctuation are dropped) | `The Quick-Brown Fox 42` | `the`, `quick`, `brown`, `fox` |
| Not analyzed | Stores the entire value as a single token | `The Quick-Brown Fox` | `The Quick-Brown Fox` |
| Whitespace | Splits on whitespace only, preserves case | `The Quick-Brown Fox` | `The`, `Quick-Brown`, `Fox` |
| Language | Applies language-specific tokenization, stemming, and stopword removal | `Running quickly` (English) | `run`, `quick` |
Language 分析器支持以下语言：`english`、`french`、`german`、`japanese`、`korean`、`arabic` 和 `combined_arabic_english`。

The Language analyzer supports the following languages: `english`, `french`, `german`, `japanese`, `korean`, `arabic`, and `combined_arabic_english`.
> **ℹ️ 注意**

> 您可以在 **Ontology Manager** 中查看或更改 Property 的分析器，相关设置位于该 Property 的搜索配置下。Property 必须启用 **Searchable** render hint 才能被搜索。
> **ℹ️ 注意**

> You can check or change the analyzer for a property in the **Ontology Manager** under the property's search configuration. Properties must have the **Searchable** render hint enabled to be searchable.
### Special character handling in tokens
standard 分析器将下划线和句点视为 token 的一部分，而不是分隔符。这意味着：

The standard analyzer treats underscores and periods as part of a token rather than as separators. This means:
* `banana_pudding` 会被存储为单个 token `banana_pudding`，而不是 `banana` 和 `pudding`。

* `user.name` 会被存储为单个 token `user.name`，而不是 `user` 和 `name`。

* `banana_pudding` is stored as a single token `banana_pudding`, not as `banana` and `pudding`.
* `user.name` is stored as a single token `user.name`, not as `user` and `name`.
在使用基于 token 的搜索方法时，搜索 `banana` **不会** 匹配值 `banana_pudding`。如果需要匹配此类值，请使用通配符搜索，例如 `banana*`，或考虑使用 whitespace 分析器。

A search for `banana` will **not** match the value `banana_pudding` when using token-based search methods. If you need to match such values, use a wildcard search like `banana*` or consider using the whitespace analyzer.
## Search in Object Explorer
> **ℹ️ 注意**

> Object Explorer 仍然是 Ontology 发现、全局搜索以及查看单个 Object 的主要 Interface。[Insight](/docs/foundry/insight/overview/) 在 Object Explorer 的基础上构建，提供了扩展的分析功能，并与 Object Explorer 并行提供。
> **ℹ️ 注意**

> Object Explorer remains the primary interface for Ontology discovery, global search, and viewing individual objects. [Insight](/docs/foundry/insight/overview/) builds on Object Explorer to provide expanded analysis features and is available alongside it.
Object Explorer 提供两种搜索 Interface，每种具有不同的匹配行为。

Object Explorer provides two search interfaces, each with different matching behavior.
### Global search bar
Object Explorer 主页和结果页面上的全局搜索栏会跨所有 Object Type 的所有可搜索 Property 执行基于 token 的搜索。默认情况下，查询中的每个词都使用 OR 逻辑独立搜索。例如，搜索 `yellow cab` 会返回匹配 `yellow` 或 `cab` 的 Object。

The global search bar on the Object Explorer home page and results page performs a token-based search across all searchable properties of all object types. By default, each word in your query is searched independently using OR logic. For example, searching for `yellow cab` returns objects matching either `yellow` or `cab`.
您可以使用 [Search syntax](/docs/foundry/object-explorer/search-syntax/) 中描述的搜索语法功能来修改此行为：

You can modify this behavior using the search syntax features described in [Search syntax](/docs/foundry/object-explorer/search-syntax/):
* **短语搜索：** 将搜索词用引号括起来（`"yellow cab"`）以要求精确的短语匹配。

* **逻辑运算符：** 使用 **AND**、**OR** 和 **NOT** 来组合搜索条件。

* **通配符：** 使用 `*` 匹配零个或多个字符，或使用 `?` 匹配单个字符。支持尾部通配符（`term*`）和前置通配符（`*term`）。请注意，不支持同时使用前置和尾部通配符（例如 `*row*`）。
* **模糊搜索：** 在搜索词后附加 `~` 以查找近似匹配。

* **Phrase search:** Wrap terms in quotation marks (`"yellow cab"`) to require an exact phrase match.
* **Logical operators:** Use **AND**, **OR**, and **NOT** to combine search criteria.
* **Wildcards:** Use `*` to match zero or more characters, or `?` to match a single character. Both trailing wildcards (`term*`) and leading wildcards (`*term`) are supported. Note that combined leading-and-trailing wildcards (such as `*row*`) are not supported.
* **Fuzzy search:** Append `~` to a term to find approximate matches.
> **⚠️ 警告**

> 前置通配符搜索（`*term`）仅适用于在 **Ontology Manager** 中启用了 **Enable leading wildcards** render hint 的字符串 Property。还必须选择 **Searchable** render hint。有关配置 render hint 的更多信息，请参阅 [Render hints](/docs/foundry/object-link-types/metadata-render-hints/)。
> **⚠️ 警告**

> Leading wildcard search (`*term`) is only available for string properties that have the **Enable leading wildcards** render hint enabled in the **Ontology Manager**. The **Searchable** render hint must also be selected. For more information on configuring render hints, see [Render hints](/docs/foundry/object-link-types/metadata-render-hints/).
> **ℹ️ 注意**

> 全局搜索栏中 **不支持** 前置通配符搜索。该功能仅在 exploration 中对单个字符串 Property 进行过滤时可用。
> **ℹ️ 注意**

> Leading wildcard search is **not** supported in the global search bar. It is available only when filtering on individual string properties in an exploration.
### Property filters in explorations
在探索特定的 Object Type 时，您可以在各个 string Property 上添加关键词过滤器。这些过滤器提供以下匹配模式：

When exploring a specific object type, you can add keyword filters on individual string properties. These filters offer the following match modes:
| Mode | Behavior |
| ----- | ----- |
| Contains (default) | Matches objects where the property contains all search tokens |
| Starts with | Matches objects where the property contains a token starting with the search term (equivalent to `term*`) |
| Exact | Matches objects where the property value exactly matches the search term |
| Is not | Excludes objects where the property contains the search tokens |
> **ℹ️ 注意**

> Property 关键词过滤器会根据该 Property 的 analyzer 生成的单个 token 进行匹配。如果 Property 使用的是 **not analyzed** analyzer，则整个值会被视为单个 token，必须相应地进行匹配。
> **ℹ️ 注意**

> Property keyword filters match against individual tokens produced by the property's analyzer. If a property uses the **not analyzed** analyzer, the entire value is treated as a single token and must be matched accordingly.
## Leading wildcard search
前导通配符搜索允许您查找 Property 值以特定词结尾的 Object。例如，搜索 `*smith` 可以匹配 `Goldsmith`、`Blacksmith` 和 `smith` 等值。

Leading wildcard search allows you to find objects where a property value ends with a specific term. For example, searching for `*smith` matches values such as `Goldsmith`, `Blacksmith`, and `smith`.
### Enabling leading wildcard search
要使用前导通配符搜索，您必须在相关的 string Property 上启用 **Enable leading wildcards** 渲染提示：

To use leading wildcard search, you must enable the **Enable leading wildcards** render hint on the relevant string properties:
1. 在 **Ontology Manager** 中，导航到该 Object Type 并选择您要配置的 string Property。

2. 在 Property 编辑器中，勾选 **Enable leading wildcards** 渲染提示。

3. 确保同时勾选了 **Searchable** 渲染提示，因为前导通配符功能需要依赖它。

4. 保存更改，并将该 Object Type 备份数据源重新索引到 Object Storage V1 (Phonograph)。您可以等待下一次触发的重新索引，或者从 **Data sources** 选项卡手动启动一次重新索引。

1. In the **Ontology Manager**, navigate to the object type and select the string property you want to configure.
2. In the property editor, select the **Enable leading wildcards** render hint.
3. Ensure the **Searchable** render hint is also selected, as it is required for leading wildcards to function.
4. Save your changes and reindex the object type's backing data sources into Object Storage V1 (Phonograph). You can wait for the next triggered reindex or manually start one from the **Data sources** tab.
有关可用渲染提示的完整列表，请参阅 [Render hints](/docs/foundry/object-link-types/metadata-render-hints/)。

For the full list of available render hints, see [Render hints](/docs/foundry/object-link-types/metadata-render-hints/).
### Using leading wildcard search
启用该渲染提示后，您就可以在 Object Explorer Property 过滤器中使用前导通配符，只需在搜索词前加上 `*` 即可。例如：

Once the render hint is enabled, you can use leading wildcards in Object Explorer property filters by prefixing your search term with `*`. For example:
* `*smith` 匹配 `Goldsmith`、`Blacksmith` 和 `smith`。

* `*ing` 匹配 `running`、`swimming` 和 `ing`。

* `*smith` matches `Goldsmith`, `Blacksmith`, and `smith`.
* `*ing` matches `running`, `swimming`, and `ing`.
> **⚠️ 警告**

> 组合使用前导和尾部通配符（`*term*`）**不**受支持。您可以使用前导通配符（`*term`）或尾部通配符（`term*`），但不能同时使用两者。如果您需要进行部分字符串匹配，请考虑使用 [Contour](/docs/foundry/contour/overview/) 或 Workshop Filter List 中的 Regex 模式。
> **⚠️ 警告**

> Combined leading-and-trailing wildcards (`*term*`) are **not** supported. You can use either a leading wildcard (`*term`) or a trailing wildcard (`term*`), but not both at the same time. If you need partial string matching, consider using [Contour](/docs/foundry/contour/overview/) or the Regex mode in a Workshop Filter List.
## Search in Workshop
Workshop 提供了多种搜索和过滤 Object 的方式，每种方式具备不同的功能。

Workshop provides several ways to search and filter objects, each with different capabilities.
### Filter list keyword search
[Filter List](/docs/foundry/workshop/widgets-filter-list/) 关键词搜索组件支持五种搜索模式，用户可在查询时选择：

The [Filter List](/docs/foundry/workshop/widgets-filter-list/) keyword search component supports five search modes, selectable by the user at query time:
| Mode | Behavior |
| ----- | ----- |
| All | Broadest search. Combines token matching, wildcard matching, and prefix matching to return any results that partially or fully match the query. Wildcard sub-matches compare the query directly against indexed tokens without applying the analyzer to the query, so wildcard queries work most predictably on properties using the **Not analyzed** or **Whitespace** analyzer. |
| Any | Matches objects where the property contains any search tokens |
| Exact | Matches objects where the property contains all search tokens as an exact phrase, in order |
| Advanced | Supports Boolean syntax with **AND**, **OR**, **NOT**, quotation marks, and parentheses for complex queries |
| Regex | Matches objects using a regular expression pattern against the property tokens |
有关高级过滤的更多详细信息，请参阅 [Filter List advanced filtering](/docs/foundry/workshop/widgets-filter-list/#advanced-filtering) 文档。

For more details on advanced filtering, see the [Filter List advanced filtering](/docs/foundry/workshop/widgets-filter-list/#advanced-filtering) documentation.
### Exploration search bar widget
Workshop 中的 **Exploration Search Bar** 组件使用与 Object Explorer 全局搜索栏相同的搜索基础设施。它支持相同的语法，包括用于短语搜索的引号、逻辑运算符、通配符和模糊搜索。

The **Exploration Search Bar** widget in Workshop uses the same search infrastructure as the Object Explorer global search bar. It supports the same syntax including quotation marks for phrase search, logical operators, wildcards, and fuzzy search.
### Object set filter variables
[Object set filter variables](/docs/foundry/workshop/object-set-filter-variables/) 支持一个执行仅前缀匹配的 `CONTAIN` 过滤器。例如，如果 Property 值为 `id000123` 且过滤查询为 `id0001`，则视为匹配。但是，查询 `d0001` **不会**匹配，因为它没有从值的开头开始。

[Object set filter variables](/docs/foundry/workshop/object-set-filter-variables/) support a `CONTAIN` filter that performs prefix-only matching. For example, if a property value is `id000123` and the filter query is `id0001`, this is considered a match. However, the query `d0001` would **not** match because it does not start at the beginning of the value.
## Search in the Functions API
[Functions API](/docs/foundry/functions/api-object-sets/#filtering) 通过其字符串过滤方法提供了对文本搜索行为最细粒度的控制：

The [Functions API](/docs/foundry/functions/api-object-sets/#filtering) provides the most granular control over text search behavior through its string filter methods:
| Method | Behavior |
| ----- | ----- |
| `.exactMatch()` | Matches objects where the property value exactly matches the query string |
| `.phrase()` | Splits the query into tokens and matches values containing all tokens in order with no other tokens between them |
| `.phrasePrefix()` | Same as `.phrase()`, but the last token also matches tokens that start with it |
| `.prefixOnLastToken()` | Splits the query into tokens and matches values containing all tokens in any order, where the last token also matches tokens starting with it |
| `.matchAnyToken()` | Splits the query into tokens and matches values containing any of the tokens |
| `.matchAllTokens()` | Splits the query into tokens and matches values containing all tokens in any order |
| `.fuzzyMatchAnyToken()` | Same as `.matchAnyToken()` but allows approximate matches within an edit distance |
| `.fuzzyMatchAllTokens()` | Same as `.matchAllTokens()` but allows approximate matches within an edit distance |
> **ℹ️ 注意**

> `.phrase()` 和 `.phrasePrefix()` 方法不会跨由下划线或句号创建的 token 边界进行匹配。例如，`.phrase("banana")` 不会匹配值 `banana_pudding`，因为 `banana_pudding` 是一个单一的 token。
> **ℹ️ 注意**

> The `.phrase()` and `.phrasePrefix()` methods do not match across token boundaries created by underscores or periods. For example, `.phrase("banana")` does not match the value `banana_pudding` because `banana_pudding` is a single token.
## Comparison of search capabilities
下表总结了每个上下文中可用的搜索功能：

The table below summarizes which search capabilities are available in each context:
| Capability | Object Explorer (global) | Object Explorer (property filter) | Workshop Filter List | Functions API |
| ----- | ----- | ----- | ----- | ----- |
| Token search | Yes | Yes | Yes | Yes |
| Phrase search | Yes (quotation marks) | No | Yes (Exact mode) | Yes (`.phrase()`) |
| Prefix search | Yes (`term*`) | Yes (Starts with) | Yes (All mode) | Yes (`.phrasePrefix()`, `.prefixOnLastToken()`) |
| Leading wildcard search | No | Yes (requires render hint) | No | No |
| Wildcard search | Yes (`*`, `?`) | No | Yes (All mode) | No |
| Fuzzy search | Yes (`~`) | No | No | Yes (`.fuzzyMatchAnyToken()`, `.fuzzyMatchAllTokens()`) |
| Boolean operators | Yes (AND, OR, NOT) | No | Yes (Advanced mode) | Yes (`Filters.and()`, `Filters.or()`, `Filters.not()`) |
| Regular expressions | No | No | Yes (Regex mode) | No |
## Common pitfalls
* **部分单词搜索不匹配 token：** 搜索 `app` 不会匹配 `application`，除非您使用通配符（`app*`）或前缀搜索方法。这是因为标准分析器生成的 token 是 `application`，而 `app` 不是精确的 token 匹配。

* **下划线和句号会阻止 token 切分：** 标准分析器将 `first_name` 和 `user.name` 视为单一 token。如果您需要在 `first_name` 中搜索 `first`，请使用通配符或考虑更改该 Property 的分析器。

* **在 Object Explorer 中不带引号的多词查询使用 OR 逻辑：** 在 Object Explorer 全局搜索栏中搜索 `New York` 会返回匹配 `new` OR `york` 的对象，其中可能包含您未预期的结果。请使用 `"New York"` 进行精确短语匹配。

* **通配符过滤器不分析查询：** 使用通配符搜索（例如 `Quick*`）时，查询字符串不会经过分析器处理 —— 它会逐字符与已索引的 token 进行比较。这带来两个后果：

* **大小写必须与索引形式匹配。** 在使用标准分析器（会将所有 token 小写化）的 Property 上，包含大写字母的通配符查询将无法匹配，即使原始文本在分析小写化之前包含这些字母。

* **多词通配符查询无法匹配。** 因为每个已索引的 token 都是单个单词，所以包含空格的通配符查询（例如 `a search term*`）会与单个 token 进行比较，无法匹配。因此，通配符搜索实际上仅限于单词查询。对于跨词的部分匹配，请考虑使用 [Contour](/docs/foundry/contour/overview/) 或 Workshop 筛选列表中的 Regex 模式。

* **前导通配符需要 render hint：** 前导通配符搜索（`*term`）仅在 **Ontology Manager** 中启用了 **Enable leading wildcards** render hint 的字符串 Property 上可用。没有此 render hint，前导通配符查询将不会返回结果。

* **不支持组合的前导和尾部通配符：** 您无法在 Object Explorer 或 Workshop 中搜索 `*term*`。如果您需要部分字符串匹配，请考虑使用 [Contour](/docs/foundry/contour/overview/) 或 Workshop 筛选列表中的 Regex 模式。

* **Partial word searches do not match tokens:** Searching for `app` does not match `application` unless you use a wildcard (`app*`) or a prefix search method. This is because the standard analyzer produces the token `application`, and `app` is not an exact token match.
* **Underscores and periods prevent token splitting:** The standard analyzer treats `first_name` and `user.name` as single tokens. If you need to search for `first` within `first_name`, use a wildcard or consider changing the property's analyzer.
* **Multi-word queries without quotation marks use OR logic in Object Explorer:** Searching for `New York` in the Object Explorer global search bar returns objects matching `new` OR `york`, which may include results you did not expect. Use `"New York"` for an exact phrase match.
* **Wildcard filters do not analyze the query:** When using wildcard search (such as `Quick*`), the query string is not run through the analyzer — it is compared character-for-character against indexed tokens. This has two consequences:
* **Case must match the indexed form.** On a property using the standard analyzer (which lowercases all tokens), a wildcard query containing uppercase letters will not match, even though the original text contained those letters before analysis lowercased them.
* **Multi-word wildcard queries do not match.** Because each indexed token is a single word, a wildcard query containing whitespace (such as `a search term*`) is compared against individual tokens and cannot match. Wildcard searches are therefore effectively limited to single-word queries. For partial matching across words, consider [Contour](/docs/foundry/contour/overview/) or the Regex mode in a Workshop Filter List.
* **Leading wildcards require a render hint:** Leading wildcard search (`*term`) is only available on string properties that have the **Enable leading wildcards** render hint enabled in the **Ontology Manager**. Without this render hint, leading wildcard queries do not return results.
* **Combined leading-and-trailing wildcards are not supported:** You cannot search for `*term*` in Object Explorer or Workshop. If you need partial string matching, consider using [Contour](/docs/foundry/contour/overview/) or the Regex mode in a Workshop Filter List.