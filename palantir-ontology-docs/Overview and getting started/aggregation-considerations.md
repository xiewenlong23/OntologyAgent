<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-backend/aggregation-considerations/
---
# Aggregation considerations
在 Foundry 中,根据您所处理数据的复杂性和数量,由于高基数聚合的性质,应用程序可能无法以完全准确性(也称为"不精确聚合")显示结果。

In Foundry, depending on the complexity and volume of data you are working with, applications may not display results with full accuracy (also known as "inexact aggregations") due to the nature of aggregations with high cardinality.
`object-set-service` API 具有以下与聚合准确性相关的字段,您可以在可用的地方使用这些字段来优化准确性:

The `object-set-service` API has the following fields related to aggregation accuracy that you may use to refine the accuracy wherever available:
* API 调用方可以在请求中添加 `AggregationExecutionMode` 并将其设置为 `PREFER_ACCURACY`。设置后,API 响应速度较慢,但可以提供更准确的结果,而不保证完全准确。

* 聚合响应包含一个 `AggregateResultAccuracy` 字段,用于指示结果是否准确。

* API callers can add `AggregationExecutionMode` in the request and set to `PREFER_ACCURACY`. Where set, the API response is slower but provides more accurate results without full accuracy guarantee.
* The aggregation response contains an `AggregateResultAccuracy` field to indicate whether the result is accurate.
Foundry 中的每个产品在指示聚合可能不精确方面都略有不同的行为表现。请查看以下部分,了解不精确聚合在 Foundry 中可能如何体现的示例,以及用户在达到准确性方面应考虑的事项。

Each product in Foundry has slightly different behaviors that indicate aggregations might be inexact. Review the following section for examples of how inexact aggregations may manifest in Foundry, and the considerations users should have on reaching accuracy.
如需更多指导,请联系 Palantir Support。

For more guidance, contact Palantir Support.
## Object Explorer and Workshop
请参考以下两张直方图截图,它们展示了一个包含 2000 万个对象的数据集中的数据。第一张截图是拉入 Object Explorer 的数据集,第二张是来自 Workshop 中的 Workshop Filter List widget。

Consider the following two histogram screenshots, showing data from a dataset with 20 million objects. The first screenshot is of a dataset pulled into Object Explorer, and the second is Workshop Filter List widget from within Workshop.

> 📷 **[图片: Object Explorer histogram.]**

> 📷 **[图片: Object Explorer histogram.]**

> 📷 **[图片: Workshop Filter List widget histogram.]**

> 📷 **[图片: Workshop Filter List widget histogram.]**

这些直方图是通过两个聚合请求构建的。第一个请求尝试获取按计数排名前 100 的桶,收到一个近似响应。第二个请求再次获取这 100 个桶的计数,但另外过滤到仅这 100 个桶,以确保计数的准确性。

The histogram were constructed using two aggregation requests. The first request tries to get the top 100 buckets by count, receiving an approximate response. The second request gets the counts for the same 100 buckets again, but additionally, filters down to just these 100 buckets to ensure accuracy in the count.
虽然显示的计数是准确的,但第二个直方图在以下意义上仍然是不准确的:显示的桶并不是实际按计数排名前 100 的桶,因为第一个聚合响应并不准确。

While the displayed counts are accurate, the second histogram is still inaccurate in the sense that the buckets that are displayed are not the actual top 100 buckets in terms of count, as the first aggregation response was not accurate.
Object Explorer 和 Workshop 对 OSS 的请求未指定 `AggregationExecutionMode`,OSS 默认使用 `PREFER_SPEED`。

Object Explorer and Workshop requests to OSS do not specify `AggregationExecutionMode`, and OSS defaults to `PREFER_SPEED`.
## Quiver pivot table and Workshop pivot table
在 Quiver 和 Workshop pivot table 中按 count 降序排序列时,顶部的 bucket 无法按正确顺序显示。在这种情况下,不精确的聚合可能会以以下某条错误信息为特征:

When sorting descending columns by count in Quiver and Workshop pivot tables, top buckets are not shown in proper order. In this case, inexact aggregations might be characterized by one of the following error messages:
* "Too many values for `column`, not all are displayed"
* "Showing approximate results due to computational limitations"
* "Only loading first 1,000 values per property. Filter your data for more accurate results."
* "Too many values for `column`, not all are displayed"
* "Showing approximate results due to computational limitations"
* "Only loading first 1,000 values per property. Filter your data for more accurate results."
在下面的示例中,`Example Bucket` 列未按预期降序排列。

In the examples below, the `Example Bucket` column is not ranked by descending as desired.

> 📷 **[图片: Workshop pivot table.]**

> 📷 **[图片: Workshop pivot table.]**

> 📷 **[图片: Quiver pivot table with error message.]**

> 📷 **[图片: Quiver pivot table with error message.]**

> 📷 **[图片: Quiver pivot table with error message 2.]**

> 📷 **[图片: Quiver pivot table with error message 2.]**

这些并不是按 count 排列的真实顶部 bucket,因为 Quiver 和 Workshop 在支撑 pivot table 的聚合请求中没有指定排序。排序是使用返回的 bucket 在前端完成的。

These are not the real top buckets by count as Quiver and Workshop do not specify an ordering in the aggregation request that backs the pivot table. The sorting is completed on the frontend using buckets that are returned.
## Ontology SDK (OSDK)
OSDK 设置为 `PREFER_ACCURACY`,其有限的聚合复杂度意味着每个 query response 都将是 `ACCURATE`。

OSDK is set to `PREFER_ACCURACY` and its limited aggregation complexity means that every query response will be `ACCURATE`.
![OSDK Application documentation.](/docs/resources/foundry/object-backend/inexact-osdk.png)
## Functions
Function 始终使用 `PREFER_ACCURACY`,因此给定 bucket 的值将是正确的。目前在 function 调用期间无法同时执行 `groupBy` 和 `orderBy`。以下代码片段演示了当前在 backend 使用 `groupBy` 并在内存中进行排序的示例。

Functions always use `PREFER_ACCURACY`, so the value for a given bucket will be correct. There is currently no way to `groupBy` and `orderBy` at the same time during a function call. The following code snippet demonstrates a current example of `groupBy` in the backend and order in memory.
```
@Function()
public async aggregateOnMoreBucketsThanAuthorized(): Promise<TwoDimensionalAggregation<string, Double>> {
// Aggregate and sum
const aggregation = await Objects.search()._af20mInstancesObv2()
.groupBy(o => o.exampleBucket.topValues())
.count()

aggregation.buckets.sort((b1, b2) => b2.value - b1.value);
return aggregation;
}
```
Example result:
```
{
"buckets": [
{
"key": {
"string": "10105",
"type": "string"
},
"value": {
"double": 461,
"type": "double"
}
},
{
"key": {
"string": "10163",
"type": "string"
},
"value": {
"double": 454,
"type": "double"
}
},
{
"key": {
"string": "10848",
"type": "string"
},
"value": {
"double": 454,
"type": "double"
}
},
...

```