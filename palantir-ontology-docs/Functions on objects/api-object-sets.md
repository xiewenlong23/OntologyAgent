<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/api-object-sets/
---
# API: Object sets
**Object Set（对象集）**表示单一类型对象的无序集合。您可以使用 functions API 对对象集进行过滤、基于已定义的 link types 对其他 object types 执行 Search Around，以及计算聚合值或检索具体对象。除了将单个对象作为输入传递给 function 之外，您还可以随时使用对象搜索 API 搜索对象集。

An **object set** represents an unordered collection of objects of a single type. You can use the functions APIs to filter object sets, perform Search Arounds to other object types based on defined link types, and compute aggregated values or retrieve the concrete objects. In addition to passing individual objects as inputs into a function, you can search for object sets at any time using the object search APIs.
> **ℹ️ 注意**

> 过滤、排序和聚合仅适用于在 Ontology app 中启用了 `Searchable` render hint 的 property。这些 property 已建立搜索索引。[了解如何启用 `Searchable` render hint。](/docs/foundry/object-link-types/metadata-render-hints/)
> **ℹ️ 注意**

> Filtering, ordering, and aggregations only work on properties that have the `Searchable` render hint enabled in the Ontology app. These properties have been indexed for search. [Learn how to enable the `Searchable` render hint.](/docs/foundry/object-link-types/metadata-render-hints/)
> **ℹ️ 提示**

> 对于 function 输入而言，对象集比对象数组更高效，因为它们会延迟加载直到需要时。有关高效使用对象集的最佳实践，请参阅 [Optimize performance](/docs/foundry/functions/optimize-performance/)。
> **ℹ️ 提示**

> Object sets are more efficient than object arrays for function inputs because they defer loading until needed. For best practices on using object sets efficiently, see [Optimize performance](/docs/foundry/functions/optimize-performance/).
## Object search
`Objects.search()` interface 允许您对导入到项目中的任何 object type 启动搜索。在此示例中，function 使用给定的 `airportCode` 查找所有从该机场起飞的航班。然后，它会查找这些航班的所有不同目的地并将其返回。

The `Objects.search()` interface allows you to initiate a search for any of the object types imported into your project. In this example, the function uses the given `airportCode` to find all flights that departed from that airport. Then, it finds all the distinct destinations of those flights and returns them.
```typescript

import { Function } from "@foundry/functions-api";
import { Objects } from "@foundry/ontology-api";

export class FlightFunctions {
@Function()
public currentFlightDestinations(airportCode: string): Set<string> {
const flightsFromAirport = Objects.search()
.flights()
.filter(flight => flight.departureAirportCode.exactMatch(airportCode))
.all();

const destinations = flightsFromAirport.map(flight => flight.arrivalAirportCode!);

return new Set(destinations);
}
}
```
对象集也可以通过将对象列表、对象资源标识符列表或对象集资源标识符作为参数传递给被搜索的 object type 来创建。例如：`Objects.search().flights([flight])`。

Object sets can also be created from a list of objects, list of object resource identifiers or an object set resource identifier by passing them as an argument to the searched object type. For example: `Objects.search().flights([flight])`.
一旦获得了给定类型的对象集，您就可以对该集执行下面文档中描述的各种操作。

Once you have an object set of a given type, you can perform various operations on the set as documented below.
## Filtering
`.filter()` 方法允许您根据对象的 searchable properties 对对象集进行过滤。filter 方法接受一个 filter definition，该定义基于您要过滤的 property 的类型。

The `.filter()` method on an object set allows you to filter the object set based on the searchable properties of the objects. The filter method takes a filter definition, which is based on the type of the property you are filtering on.
* 所有 property 类型都支持 `.exactMatch()` filter，它会过滤出在该 property 值上完全匹配的对象。这对于过滤字符串的精确匹配（如上例所示）或过滤对象的主键（例如 `.filter(object => object.primaryKey.exactMatch(PrimaryKey))`）非常有用。

* 若要检查 property 是否为 `null` 或 `undefined`，请使用 `hasProperty()` 方法。

* 若要传递多个值，请使用 spread operator `.exactMatch(...listVariable)`。如果传入空数组，则该 filter 将被忽略。

* 字符串 property 支持多种关键字 filter。有关每个方法的完整详细信息，请参阅 Code Assist 中的文档。

* `.phrase()` 将搜索查询拆分为 tokens（通常是单个词），然后根据值是否按顺序包含所有给定的 tokens 且中间没有其他 tokens 来进行过滤。请注意，由下划线或句点分隔的字符串值将被视为单个 token。例如，当搜索 "banana" 时，property 值为 "banana\_pudding" 或 "banana.pudding" 的对象将不会被返回。

* `.phrasePrefix()` 与 `phrase()` 几乎相同，但最后一个 token 也会匹配以该 token 开头的 token。例如，对 `fresh banana` 进行 `.phrasePrefix()` 搜索将匹配 property 值 `fresh banana_pudding`，但不会匹配 property 值 `banana_pudding fresh`。对 `pudding` 进行 `.phrasePrefix()` 搜索将不会匹配 property 值 `banana_pudding`。

* `.prefixOnLastToken()` 将搜索查询拆分为 tokens，然后根据值是否包含所有给定的 tokens 来进行过滤，其中最后一个 token 也会匹配以该 token 开头的 token。例如，`big app` 将匹配 `big apples` 以及 `apples from the big tree`，但不会匹配 `apples from the biggest tree`。

* `.matchAnyToken()`、`.fuzzyMatchAnyToken()` 将搜索查询拆分为 tokens，然后根据值是否包含任何给定的 tokens 来进行过滤。`fuzzy` 版本允许近似值匹配。

* `.matchAllTokens()`、`.fuzzyMatchAllTokens()` 将搜索查询拆分为 tokens，然后根据值是否包含所有给定的 tokens 来进行过滤。`fuzzy` 版本允许近似值匹配。

* Fuzzy filters 可以接受从 `@foundry/functions-api` 导入的可选 `Fuzziness` 参数。

* 有关可用 `Fuzziness` 选项的说明，请参阅 [ElasticSearch 文档 ↗](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness)。更多信息也可以在下面找到。

* 数字、日期和 timestamp property 支持 `.range()` filters。

* Range filters 具有一组 `.lt()`、`.lte()`、`.gt()` 和 `gte()` 方法，用于执行小于 / 小于等于 / 大于 / 大于等于（分别）的比较。

* 布尔 property 支持 `.isTrue()` 和 `.isFalse()` filters。

* Geopoint property 支持 `.withinDistanceOf()`、`.withinPolygon()` 和 `.withinBoundingBox()` filters。

* GeoShape property 支持 `.withinBoundingBox()`、`.intersectsBoundingBox()`、`.doesNotIntersectBoundingBox()`、`.withinPolygon()`、`.intersectsPolygon()` 和 `doesNotIntersectPolygon()` filters。

* Link filters 可用于使用 `.isPresent()` 方法过滤具有或不具有特定类型的已链接对象的对象。

* 数组 property 支持 `.contains()` filter，它会过滤出其数组 property 值包含 *任何* 给定值的对象。

* All property types support the `.exactMatch()` filter, which filters to objects with an exact match on that property value. This is useful to filter for exact matches on strings (as in the example above), or to filter on the primary key of an object (for example,`.filter(object => object.primaryKey.exactMatch(PrimaryKey))`).
* To check whether a property is `null` or `undefined`, use the `hasProperty()` method.
* To pass multiple values, use the spread operator `.exactMatch(...listVariable)`. If an empty array is passed in, the filter will be ignored.
* String properties support several keyword filters. See the documentation on each method in Code Assist for full details.
* `.phrase()` splits the search query into tokens (usually individual words) and then filters values based on whether they contain all of the given tokens in order with no other tokens in between. Note that string values that are separated by underscores or periods will be treated as one token. For example, when searching for "banana", an object with the property value "banana\_pudding" or "banana.pudding" will not be returned.
* `.phrasePrefix()` is almost identical to `phrase()`, but the last token will also match tokens starting with that token. For example, a `.phrasePrefix()` search for `fresh banana` would match the property value `fresh banana_pudding`, but not the property value `banana_pudding fresh`. A `.phrasePrefix()` search for `pudding` would not match the property value `banana_pudding`.
* `.prefixOnLastToken()` splits the search query into tokens and then filters values based on whether they contain all of the given tokens, where the last token will also match tokens starting with that token. For example, `big app` would match `big apples` as well as `apples from the big tree`, though it would not match `apples from the biggest tree`.
* `.matchAnyToken()`, `.fuzzyMatchAnyToken()` split the search query into tokens and then filter values based on whether they contain any of the given tokens. The `fuzzy` version allows approximate values to match.
* `.matchAllTokens()`, `.fuzzyMatchAllTokens()` split the search query into tokens and then filter values based on whether they contain all of the given tokens. The `fuzzy` version allows approximate values to match.
* Fuzzy filters can take an optional `Fuzziness` parameter imported from `@foundry/functions-api`.
* Explanations of the available `Fuzziness` options can be found in the [ElasticSearch documentation ↗](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness). More information can also be found below.
* Numbers, dates, and timestamp properties support `.range()` filters.
* Range filters have a set of `.lt()`, `.lte()`, `.gt()` and `gte()` methods for performing less than / less than or equal to / greater than / greater than or equal to (respectively) comparisons.
* Boolean properties support `.isTrue()` and `.isFalse()` filters.
* Geopoint properties support `.withinDistanceOf()`, `.withinPolygon()`, and `.withinBoundingBox()` filters.
* GeoShape properties support `.withinBoundingBox()`, `.intersectsBoundingBox()`, `.doesNotIntersectBoundingBox()`, `.withinPolygon()`, `.intersectsPolygon()`, and `doesNotIntersectPolygon()` filters.
* Link filters can be used to filter objects that do or do not have any linked objects of a specific type using the `.isPresent()` method.
* Array properties support the `.contains()` filter, which filters to objects whose array property values contain *any* of the given values.
### Combining filters
您可以使用从 `@foundry/functions-api` 导出的 `Filters` API 将 filter 组合在一起。可用方法包括：

You can compose filters together using the `Filters` API exported from `@foundry/functions-api`. The available methods are:
* `and()` 将对象集过滤为通过所有给定 filter 的对象

* `or()` 将对象集过滤为通过任何给定 filter 的对象

* `not()` 对给定的 filter 取反

* `and()` filters the object set to objects that pass all the given filters
* `or()` filters the object set to objects that pass any of the given filters
* `not()` negates the given filter
在下面的示例中，我们可以使用 `and()` 按航班目的地过滤航班对象集：

In the example below, we can filter an object set of flights by flight destination using `and()`:
```typescript
import { Filters } from "@foundry/functions-api";

Objects.search()
.flights()
.filter(flight => Filters.or(
Filters.and(flight.destination.exactMatch("SFO"), flight.passengerCount.gt(100)),
Filters.and(flight.destination.exactMatch("LAX"), flight.passengerCount.gt(300)),
))
```
上述代码将过滤出抵达 SFO 且乘客数超过 100 人，或抵达 LAX 且乘客数超过 300 人的航班。

The above code would filter to flights that either arrived at SFO with more than 100 passengers or arrived at LAX with more than 300 passengers.
> **⚠️ 警告: Warning**

> 对象集上的 `.filter()` 方法不使用运算符 `&&` 或 `||`。若要应用多个 filter，您必须使用上面列出的 `Filters` 中的方法之一（或多次调用 `.filter()` 以实现 `and` 条件）。
> **⚠️ 警告: Warning**

> The `.filter()` method on an object set does not use the operators `&&` or `||`. To apply multiple filters, you must use one of the methods on `Filters` listed above (or call `.filter()` multiple times to achieve an `and` condition).
### Filtering on string properties with fuzzy search
指定可选的 `fuzziness` 参数可以提供对 Fuzzy 匹配行为的更精细控制。如果您不指定 fuzziness，则会根据所搜索 token 的长度自动允许一个编辑距离。您需要从 `@foundry/functions-api` 导入 `Fuzziness` 才能指定编辑距离。

Specifying the optional `fuzziness` parameter can provide more fine-tuned control over Fuzzy matching behavior. If you do not specify fuzziness, then an automatic edit distance is allowed based on the length of the token you are searching for. You will need to import `Fuzziness` from `@foundry/functions-api` in order to specify edit distance.
#### Fuzzy match any token
```
Objects.search().employee().filter(employee => employee.firstName.fuzzyMatchAnyToken("Michael", { fuzziness: Fuzziness.LEVENSHTEIN_TWO })).all();
```
上述代码返回名字与所提供的搜索词在两次编辑距离内（Levenshtein 距离为 2）的任何员工。在此示例中，将包括 `Michael`、`Micheal`、`Mikhael`、`Michel`、`Mikhail`、`Mihail`（但不包括 `Miguel`）。如果您对搜索词的准确性更有把握，则可以使用更小的编辑距离（具有不同的 Levenshtein 距离）进行搜索，从而进一步细化搜索结果。

The code above returns any employees with a first name within two edits of the provided search term (with Levenshtein distance of two). In this example, that would include `Michael`, `Micheal`, `Mikhael`, `Michel`, `Mikhail`, `Mihail` (but not `Miguel` for example). If you have more certainty in the accuracy of your search term, you can search with a smaller edit distance (with different Levenshtein distances), refining your search results a little more.
#### Fuzzy match all tokens
```
Objects.search().employee().filter(employee => employee.fullName.fuzzyMatchAllTokens("Michael Smith", { fuzziness: Fuzziness.LEVENSHTEIN_ONE })).all();
```
您也可以在多 token 短语上使用模糊过滤器。上述代码会匹配那些全名中**同时**包含 `Michael` 和 `Smith`（每个 token 最多允许一个编辑距离）的员工——例如 `Mikhael Smitt`（即每个 token 的 Levenshtein 距离均为 1）。在使用 `fuzzyMatchAllTokens` 或 `fuzzyMatchesAllTokens` 过滤器时，token 的顺序不会被考虑。

You can also use fuzzy filters on a multiple token phrase. The code above would match on employees whose full name contains **both** `Michael` and `Smith` with up to one edit in each token - for example, `Mikhael Smitt` (that is, each with a Levenshtein distance of one each). The ordering of tokens is not taken into account with a `fuzzyMatchAllTokens` or `fuzzyMatchesAllTokens` filter.
#### Fuzzy match on string array properties
所有基于数组类型的 property 过滤器都可以使用其底层类型可用的方法。例如，字符串数组 property 可以基于字符串 property 任何可用的方法进行过滤，但方法的命名可能略有不同。对数组 property 进行过滤时，数组元素中只要有一个匹配，该对象即会被返回。

All filters on array-based properties can use the methods available to their underlying type. For example, string array properties can be filtered based on any methods available to string properties, though the naming of the methods may differ slightly. Filtering on array properties requires a single match among the array elements in order for that object to be returned.
## Search Around
> **ℹ️ 注意: Search around 限制**

> 通过 `.all()` 或 `.allAsync()` 加载到内存中的 object set 最多允许 **3 个 search around**。如果使用超过 3 个 search around，将抛出错误。在 Object Storage V2 中从 object set A 对 object set B 执行 search around 时，得到的 object set B 包含的 object instance 数量不能超过 1000 万，否则将抛出错误。对于 Object Storage V1，限制为 100,000 个 object instance。
> **ℹ️ 注意: Search around limits**

> Object sets loaded into memory `.all()` or `.allAsync()` are allowed to have a **maximum of 3 search arounds**. If more than 3 search arounds are used, an error is thrown. When performing a search around from object set A to object set B in Object Storage V2, the resulting object set B cannot have more than 10 million object instances, or an error will be thrown. For Object Storage V1, the limit is 100,000 object instances.
根据 object set 的 object type，会生成 *Search Around* 方法，以便基于 object set 的 object type 来遍历 [link](/docs/foundry/object-link-types/link-types-overview/)。在下面的示例中，我们根据出发代码筛选出一个 Flight 的 object set，然后 Search Around 到这些航班上的乘客。这样会得到一个 Passenger 的 object set，可以进一步对其执行过滤或 search around。

Based on the object type of your object set, *Search Around* methods are generated to enable traversing [links](/docs/foundry/object-link-types/link-types-overview/) based on the object type of your object set. In the below example, we filter to an object set of Flights based on the departure code, then Search Around to the passengers on those flights. This results in an object set of Passengers, which can be further filtered or searched around on.
```typescript
const passengersDepartingFromAirport = Objects.search()
.flights()
.filter(flight => flight.departureAirportCode.exactMatch(airportCode))
.searchAroundPassengers();
```
Search Around 方法只会为已导入到您项目中的 link type 生成。有关如何导入 link type 的详细信息，请参阅 [the tutorial](/docs/foundry/functions/foo-getting-started/#import-ontology-types)。

Search Around methods will only be generated for link types that are imported into your project. Refer to [the tutorial](/docs/foundry/functions/foo-getting-started/#import-ontology-types) for details on how to import link types.
请注意，出于性能方面的考虑，在单次搜索中可以执行的 Search Around 操作数量当前限制为 3 个。如果您尝试运行 search around 深度超过三层的搜索，该搜索将在运行时失败。

Note that for performance reasons, the number of Search Around operations you can conduct in a single search is currently limited to 3. If you attempt to run a search with more than three levels of Search Around depth, the search will fail at runtime.
## K-nearest neighbors (KNN)
> **ℹ️ 注意: KNN 限制**

> KNN 仅支持已索引到 [OSv2](/docs/foundry/object-backend/overview/) 的 object type。k 值的范围限制为 0 < K <= 100。此外，搜索向量的维度必须与用于索引的向量大小相同，并且维度上限为 2048。如果超过上述任何限制，将抛出错误。
> **ℹ️ 注意: KNN Limits**

> KNN is only supported on object types indexed into [OSv2](/docs/foundry/object-backend/overview/). The k value is limited to the range 0 < K <= 100. Also, the search vector must be the same size as the one used for indexing and has a 2048 dimension limit. An error will be thrown if any of these limits are exceeded.
具有 embedding property 的 object type 将可用于 KNN 搜索。这些搜索会返回 k 个与所提供的 embedding 参数最接近的具有 embedding property 的对象。以下示例返回与所提供的电影剧本最相似的电影。Embedding 可以在 transformation 工具中生成，例如 [Pipeline Builder](/docs/foundry/pipeline-builder/pipeline-builder-aip/#text-to-embeddings)；也可以在 function query 时 [使用 Palantir 提供的 embedding 模型](language-models.md#embeddings) 或 [在 function 中使用您自己的模型](/docs/foundry/functions/functions-on-models/) 来生成。

Object types with embedding properties will be available for KNN searches. These searches will return the k value objects that have an embedding property nearest to the provided embedding parameter. The following example returns the most similar movies to a provided movie script. Embeddings can be generated in transformation tools such as [Pipeline Builder](/docs/foundry/pipeline-builder/pipeline-builder-aip/#text-to-embeddings) ; or at function query time [using a Palantir-provided embedding model](language-models.md#embeddings) or [your own model in a function](/docs/foundry/functions/functions-on-models/).
请确保您 functions 仓库的 `functions.json` 配置文件中的 `enableVectorProperties` 条目设置为 `true`。

Make sure that your functions repository's `functions.json` configuration file has the `enableVectorProperties` entry set to  `true`.
```typescript
import { Objects } from "@foundry/ontology-api";

const kValue: number = 2;
// Vector can be generated from FML Live or come from an existing object
const vector: Double[] = [0.7, 0.1, 0.3];
const movies: Movies[] = Objects.search()
.movies()
.nearestNeighbors(obj => obj.vectorProperty.near(vector, { kValue }))
.orderByRelevance()
.take(kValue);
```
有关完整 semantic search 工作流的示例，请参阅 [semantic search workflow guide](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/)。

For an example of a full semantic search workflow, review the [semantic search workflow guide](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/).
## Set operations
相同 object type 的 object set 可以使用集合运算以多种方式进行组合：

Object sets of the same object type can be combined in various ways using set operations:
* `.union()` 创建一个由给定 object set 中任意一个所包含的对象组成的新 object set。

* `.intersect()` 创建一个由给定 object set 中所有共同包含的对象组成的新 object set。

* `.subtract()` 移除给定 object set 中存在的任何对象。

* `.union()` creates a new object set composed of objects present in any of the given object sets.
* `.intersect()` creates a new object set composed of objects present in all of the given object sets.
* `.subtract()` removes any objects present in the given object sets.
## Retrieving all objects
`.all()` 和 `.allAsync()` 方法用于检索 object set 中的所有对象。请注意，如果您尝试一次性加载过多对象，您的 function 将无法执行。目前，您可以加载的最大对象数量为 100,000。但是，加载超过 10,000 个对象也可能导致 function 执行超时。[详细了解 functions 中的时间和空间限制。](/docs/foundry/functions/manage-functions/#enforced-limits)

The `.all()` and `.allAsync()` methods retrieve all objects in the object set. Note that if you attempt to load too many objects at once, your function will fail to execute. Currently, the maximum number of objects you can load is 100,000. However, loading more than 10,000 objects may also cause your function execution to time out. [Learn more about time and space limits in functions.](/docs/foundry/functions/manage-functions/#enforced-limits)
您可以使用 `.allAsync()` 方法来检索一个 Promise，该 Promise 解析为 object set 中的所有对象。这对于并行从多个 object set 加载数据非常有用。

You can use the `.allAsync()` method to retrieve a Promise that resolves to all the objects in the object set. This can be useful for loading data from multiple object sets in parallel.
## Ordering and limiting
您也可以不检索所有对象，而是通过对 object set 应用排序子句来加载限定数量的对象。为此，您可以使用以下方法：

Instead of retrieving all objects, you can load a limited number by applying an ordering clause to your object set, then specifying a specific number of objects to load. To do this, you can use the following methods:
* `.orderBy()` specifies a searchable property to order by, and allows you to specify an ordering direction. Only properties whose types can be ordered (numbers, dates, and strings) are available for selection in this method. You can call `.orderBy()` multiple times to sort by multiple properties.
* `.orderByRelevance()` specifies that the objects should be returned in order of how well they match the provided filters, with the most relevant listed first. Relevance for a query term against a property value on a given object is a complex determination that takes into account the frequency of the term appearing in the property value, the frequency of the term appearing across all objects, and more. Relevance is less appropriate when performing only `.exactMatch()` filters or filtering on non-string properties. Note that only one of `.orderBy()` and `.orderByRelevance()` may be used in a single search.
* `.take()` and `.takeAsync()` enable you to retrieve a specified number of objects from the set. These methods are only available after you have specified an ordering.
For example, the following code would retrieve the ten employees with the earliest start dates:
```typescript
Objects.search()
.employees()
.orderBy(e => e.startDate.asc())
.take(10)
```
As another example, imagine an object type `claims` which contains text of accident claims for an insurance company. We'd like to find a specific claim involving a red car and a deer. Without the `.orderByRelevance()` line, any results containing any of the words `red`, `car`, `collision`, `with`, or `deer` may have been returned in the top 10 results. With the `.orderByRelevance()` line, the first 10 results will be the claims that contain the most search terms, so that the most relevant claims will appear first.
```typescript
const results = Objects.search()
.claims()
.filter(doc => doc.text.matchAnyToken("red car collision with deer"))
.orderByRelevance()
.take(10)
```
## Computing aggregations
> **ℹ️ 注意: Aggregation limits**

> Aggregations returned from the Objects API are limited to **10,000 total buckets**. An error will be thrown if this limit is exceeded.
> When bucketing using `.topValues()`, results will be approximate if the data has more than 1,000 distinct values. The list of top values may not be accurate in that case.
### Grouping objects by properties
In many cases, it's unnecessary to load all of the objects in your object set. Instead, you can simply load a bucketed aggregation of values to conduct further analysis.
To begin computing an aggregation, call the `.groupBy()` method on an object set. This allows you to specify bucketing on one of the searchable properties of the object type in the object set. For example, this code groups employees by their start date:
```typescript
Objects.search()
.employees()
.groupBy(e => e.startDate.byDays())
```
When specifying which property to bucket by, you will have to provide additional information about how the bucketing should be done depending on the property type:
* For `boolean` properties, the only option is `.topValues()`. This returns two buckets, one for `true` and one for `false`.
* For string properties, there are two options:
* `.topValues()`: For rapid response times and properties with a smaller cardinality. This buckets by the top 1,000 values for the string property. This limit is to ensure that the returned aggregation is not excessively large.
* `.exactValues()`: For more exact aggregations and the possibility to consider up to 10,000 buckets for high cardinality properties. The amount of considered buckets can be specified via `.exactValues({"maxBuckets": numBuckets})` where `numBuckets` must be an integer value between 0 and 10,000. The response time for this method can take longer, as more results have to be considered.
* For numeric properties (e.g. `Integer`, `Long`, `Float`, `Double`), the two bucketing options are:
* `.byRanges()` allows you to specify the exact ranges that should be used. For example, you could use `.byRanges({ min: 0, max: 50 }, { min: 50, max: 100 })` to bucket objects into the two ranges of \[0, 50] and \[50, 100] that you specify here. The `min` of the range is inclusive and the `max` is exclusive. You may omit either `min` or `max` to represent a bucket containing values from -∞ to `max` or `min` to ∞ respectively.
* `.byFixedWidth()` specifies the width of each bucket. For example, you could use `.byFixedWidth(50)` to bucket objects into ranges that each have a width of 50.
* For `LocalDate` properties, various convenience methods are provided for easy bucketing:
* `.byYear()`
* `.byQuarter()`
* `.byMonth()`
* `.byWeek()`
* `.byDays()` buckets values into days. You may pass in a number of days to use for bucket widths.
* For `Timestamp` properties, the same bucketing options apply as for `LocalDate`, as well as the following additions:
* `.byHours()` buckets values by hours. You may pass in a number of hours to use for bucket widths.
* `.byMinutes()` buckets values by minutes. You may pass in a number of minutes to use for bucket widths.
* `.bySeconds()` buckets values by seconds. You may pass in a number of seconds to use for bucket widths.
* For `Array` properties, the bucketing options are determined by the type of the elements in the array. In particular, you get the same bucketing methods for `Array<PropertyType>` as you would get for the `PropertyType` (for example, `Array<boolean>` gets the same bucketing methods as `boolean`).
* For example, if you have an `Array<string>` called `employeeSet` consisting of Alice and Bob who have respectively worked in `["US", "UK"]` and `["US"]`. Then `employeeSet.groupBy(e => e.pastCountries.exactValue()).count()` will return `{ "US": 2, "UK": 1 }`.
After grouping by one property, you may optionally call the `.segmentBy()` method to perform further bucketing. This allows you to compute a three-dimensional aggregation bucketed by two searchable properties. For example, you could group employees by their start date as well as their role as follows:
```typescript
Objects.search()
.employees()
.groupBy(e => e.startDate.byDays())
.segmentBy(e => e.role.topValues())
```
### Choosing an aggregation metric
After grouping your object set, you can call various aggregation methods to compute aggregation metrics on each bucket. Methods that require a property only accept properties marked searchable. Possible aggregation methods are:
* `.count()` simply returns the number of objects in each bucket
* `.average()` returns the average number for the given numeric, timestamp, date property
* `.max()` returns the maximum value for the given numeric, timestamp, date property
* `.min()` returns the minimum value for the given numeric, timestamp, date property
* `.sum()` returns the sum of values for the given numeric property
* `.cardinality()` returns the approximate number of distinct values for the given property
Calling one of these methods returns either a `TwoDimensionalAggregation` or `ThreeDimensionalAggregation`. A `ThreeDimensionalAggregation` is returned if you called `.segmentBy()` before calling one of the final aggregation methods.
[Learn more about the structure of these aggregation types, including **valid bucketing types**.](/docs/foundry/functions/types-reference/#aggregation-types)
请注意，返回的聚合结果会被包装在 `Promise` 中，因为计算聚合需要从远程服务加载数据。您可以使用 [async/await ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) 语法来解开 `Promise` 的结果。

Note that the resulting aggregations are wrapped in a `Promise`, as computing the aggregation requires loading data from a remote service. You can use the [async/await ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) syntax to unwrap the `Promise` result.
以下是加载 aggregation 并将其作为结果返回的完整示例。

Below is a full example of loading an aggregation and returning it as a result.
```typescript
import { Function, ThreeDimensionalAggregation } from "@foundry/functions-api";
import { Objects } from "@foundry/ontology-api";

export class AggregationFunctions {
@Function()
public async employeesByRoleAndOffice(): Promise<ThreeDimensionalAggregation<string, string>> {
return Objects.search()
.employee()
.groupBy(e => e.title.topValues())
.segmentBy(e => e.office.topValues())
.count();
}
}
```
以下是不使用 groupBy 语句进行 aggregation 的完整示例：

Below is a full example of aggregating without groupBy statements:
```typescript
import { Function } from "@foundry/functions-api";
import { Objects } from "@foundry/ontology-api";

export class AggregationFunctions {
@Function()
public async employeesStats(): Promise<Double> {
// Count of all employees, default to zero if count() returns undefined
return Objects.search().employee().count() ?? 0;
}
}
```
您也可以通过替换上述代码示例中的相应行，在不使用 groupBy 的情况下执行其他 aggregation，例如：

You can also perform other aggregations without groupBy by replacing the appropriate line in the code example above, such as:
* 所有员工的数量：`Objects.search().employee().count();`（如上例所示）

* 员工的平均任期：`Objects.search().employee().average(e => e.tenure);`

* 员工的最长任期：`Objects.search().employee().max(e => e.tenure);`

* 员工的最短任期：`Objects.search().employee().min(e => e.tenure);`

* 所有员工薪资的总和：`Objects.search().employee().sum(e => e.salary);`

* 办公室的数量：`Objects.search().employee().cardinality(e => e.office);`

* Count of all employees: `Objects.search().employee().count();` (as seen in example above)
* Average tenure of employees: `Objects.search().employee().average(e => e.tenure);`
* Maximum tenure of employees: `Objects.search().employee().max(e => e.tenure);`
* Minimum tenure of employees: `Objects.search().employee().min(e => e.tenure);`
* Sum of all employee salaries: `Objects.search().employee().sum(e => e.salary);`
* Number of offices: `Objects.search().employee().cardinality(e => e.office);`
有关在内存中处理 aggregation 结果的示例，请参阅[创建自定义 aggregation](/docs/foundry/functions/create-custom-aggregation/) 的指南。

For an example of manipulating aggregation results in memory, try the guide for [creating custom aggregations](/docs/foundry/functions/create-custom-aggregation/).