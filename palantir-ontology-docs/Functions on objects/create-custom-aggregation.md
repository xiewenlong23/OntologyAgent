<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/create-custom-aggregation/
---
# Create a custom aggregation
Functions 可用于基于 Ontology 中的数据计算自定义聚合，然后可以在 Workshop 的图表 widget 中展示这些数据。本指南将逐步介绍如何编写自定义聚合逻辑：从 Ontology 加载聚合数据，对结果进行处理以生成未来结果的预测，并返回修改后的结果。

Functions can be used to compute custom aggregations based on data in the ontology, which can then be surfaced in a chart widget in Workshop. This guide walks through how to write custom aggregation logic that loads aggregated data from the ontology, manipulates the results to create a projection of future results, and returns the modified results.
在本节操作过程中，以下参考可能对您有所帮助：

These references may be useful while working through this section:
* [Object Set 聚合](/docs/foundry/functions/api-object-sets/#computing-aggregations) 参考

* [聚合类型](/docs/foundry/functions/types-reference/#aggregation-types) 参考

* Reference for [Object Set aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations)
* Reference for [aggregation types](/docs/foundry/functions/types-reference/#aggregation-types)
## Loading an aggregation
在本示例中，假设您拥有一个由费用记录组成的 Ontology，其中每个 `expense` 对象都具有部门名称、费用 `date` 和费用 `amount` 等 Property。如果您希望估算未来六个月各部门每月的支出，可以首先加载每月支出的聚合数据：

In this example, assume you have an ontology consisting of expenses, with each `expense` object having properties for department name, expense `date`, and expense `amount`. If you want to estimate the monthly spend by department over the next six months, you can begin by loading the aggregated data for the monthly spend:
```typescript
const result = await Objects.search()
.expenses()
.groupBy(expense => expense.departmentName.topValues())
.segmentBy(expense => expense.date.byMonth())
.sum(expense => expense.amount);
```
## Manipulating aggregation results
接下来，您可以推算每个部门未来六个月的支出。在本示例中，可以采用一种简单的方法，即将最后一个月的值作为未来六个月的估算值。

Next, you can extrapolate the spend for each department for the next six months. For this example, you can take a simple approach of using the final month's value as the estimate for the next six months.
```typescript
const modifiedBuckets = result.buckets.map(bucket => {
// Find the bucket corresponding to the most recent month
const lastBucket = bucket.value[bucket.value.length - 1];

let nextSixMonths: IBaseBucket<IRange<Timestamp>, Double>[] = [];
let currentMonth = lastBucket.key.max!;
// Loop six times
for (let i = 0; i < 6; i++) {
// Find the end of this range (the following month)
const nextMonth = currentMonth.plusMonths(1);
// Add a new bucket which uses the next month as the date range
// and the most recent month as the value
nextSixMonths.push({
key: {
min: currentMonth,
max: nextMonth,
},
value: lastBucket.value,
});
currentMonth = nextMonth;
}

// Return the modified results
return { key: bucket.key, value: nextSixMonths };
});
```
## Returning the aggregation
现在您已经为未来六个月创建了估算，可以返回这些估算值：

Now that you have created an estimate for the next six months, you can return these estimated values:
```typescript
return { buckets: modifiedBuckets };
```
该 function 的完整示例代码如下：

The full example code for this function is as follows:
```typescript
@Function()
public async estimatedDepartmentExpenses(): Promise<ThreeDimensionalAggregation<string, IRange<Timestamp>>> {
const result = await Objects.search()
.expenses()
.groupBy(expense => expense.departmentName.topValues())
.segmentBy(expense => expense.date.byMonths())
.sum(expense => expense.amount);

const modifiedBuckets = result.buckets.map(bucket => {
// Find the bucket corresponding to the most recent month
const lastBucket = bucket.value[bucket.value.length - 1];

let nextSixMonths: IBaseBucket<IRange<Timestamp>, Double>[] = [];
let currentMonth = lastBucket.key.max!;
// Loop six times
for (let i = 0; i < 6; i++) {
// Find the end of this range (the following month)
const nextMonth = currentMonth.plusMonths(1);
// Add a new bucket which uses the next month as the date range
// and the most recent month as the value
nextSixMonths.push({
key: {
min: currentMonth,
max: nextMonth,
},
value: lastBucket.value,
});
currentMonth = nextMonth;
}

// Return the modified results
return { key: bucket.key, value: nextSixMonths };
});

return { buckets: modifiedBuckets };
}
```
生成的聚合结果可以在 Workshop chart 中使用，以展示未来六个月的每月支出估算。

The resulting aggregation can be used in a Workshop chart to show the monthly spend estimate for the next six months.