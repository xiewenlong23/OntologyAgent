<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-functions-create-custom-aggregation/
---
# Create a custom aggregation
Function 可用于基于 ontology 中的数据计算自定义聚合，然后可以在 Workshop 的 chart widget 中展示。本指南将逐步介绍如何编写自定义聚合逻辑，从 ontology 加载聚合数据，操作结果以创建未来结果的预测，并返回修改后的结果。

Functions can be used to compute custom aggregations based on data in the ontology, which can then be surfaced in a chart widget in Workshop. This guide walks through how to write custom aggregation logic that loads aggregated data from the ontology, manipulates the results to create a projection of future results, and returns the modified results.
在学习本节时，以下参考资料可能会对您有所帮助：

These references may be useful while working through this section:
* 参考 [Python aggregation types](/docs/foundry/functions/types-reference/#aggregation-types)

* Reference for [Python aggregation types](/docs/foundry/functions/types-reference/#aggregation-types)
> **⚠️ 警告**

> `TwoDimensionalAggregation` 和 `ThreeDimensionalAggregation` 中的 `.from_osdk()` 仅在使用 Python OSDK v2 时受支持。
> **⚠️ 警告**

> `.from_osdk()` in `TwoDimensionalAggregation` and `ThreeDimensionalAggregation` are only supported when using v2 of the Python OSDK.
## Loading an aggregation
在本示例中，假设您有一个由支出 (expense) 组成的 ontology，每个 `expense` object 都具有部门名称、支出 `date` 和支出 `amount` 等 property。如果您想估算未来六个月内各部门的每月支出，可以首先加载每月支出的聚合数据：

In this example, assume you have an ontology consisting of expenses, with each `expense` object having properties for department name, expense `date`, and expense `amount`. If you want to estimate the monthly spend by department over the next six months, you can begin by loading the aggregated data for the monthly spend:
```python
client = FoundryClient()
result: AggregateObjectsResponse = (
client.ontology.objects.Expense
.group_by(Expense.object_type.department_name.exact())
.group_by(Expense.object_type.date.exact())
.sum(Expense.object_type.amount)
.compute()
)
```
## Manipulating aggregation results
接下来，您可以为每个部门推断未来六个月的支出。在本示例中，您可以采用一种简单的方法，即使用最后一个月的值作为未来六个月的估算值。

Next, you can extrapolate the spend for each department for the next six months. For this example, you can take a simple approach of using the final month's value as the estimate for the next six months.
```python
current_buckets = ThreeDimensionalAggregation.from_osdk(result, "departmentName", "date")
modified_buckets: list[NestedBucket[str, Range[Date], Double]] = []
date_format = "%Y-%m-%d"
for bucket in current_buckets.buckets:
# Find the bucket corresponding to the most recent month
last_bucket: SingleBucket[Date, Double] = bucket[-1].value

next_six_months: list[SingleBucket[Range[Date], Double]] = []
# The `date` field has been converted to a string formatted YYYY-MM-DD.
# Convert to type `Date` from the string. Convert back to a string when
# creating a SingleBucket object for each month
current_month: Date = datetime.strptime(last_bucket.key, date_format).date()

# Loop six times
for _ in range(6):
# Construct the next month from the current month
next_month = current_month + relativedelta(months=1)
# Add a new bucket which uses the next month as the date range
# and the most recent months amount as the value
next_six_months.append(SingleBucket(Range(min=current_month, max=next_month), last_bucket.value))
current_month = next_month

# Append the modified results as a NestedBucket
modified_buckets.append(NestedBucket(bucket.key, next_six_months))
```
## Returning the aggregation
现在您已经创建了未来六个月的估算值，可以将这些估算值作为 `ThreeDimensionalAggregation` 返回：

Now that you have created an estimate for the next six months, you can return these estimated values as a `ThreeDimensionalAggregation`:
```python
return ThreeDimensionalAggregation(modified_buckets)
```
此 function 的完整示例代码如下：

The full example code for this function is as follows:
```python
from dateutil.relativedelta import relativedelta
from datetime import datetime

from functions.api import (
Date,
Double,
NestedBucket,
SingleBucket,
String,
Range,
ThreeDimensionalAggregation,
function,
)
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Expense

@function
def estimated_department_expenses() -> ThreeDimensionalAggregation[str, Date, Double]:
client = FoundryClient()
result = (
client.ontology.objects.Expense
.group_by(Expense.object_type.department_name.exact())
.group_by(Expense.object_type.date.exact())
.sum(Expense.object_type.amount)
.compute()
)

current_buckets = ThreeDimensionalAggregation.from_osdk(result, "departmentName", "date")
modified_buckets: list[NestedBucket[str, Range[Date], Double]] = []
date_format = "%Y-%m-%d"
for bucket in current_buckets.buckets:
# Find the bucket corresponding to the most recent month
last_bucket: SingleBucket[Date, Double] = bucket.buckets[-1]

next_six_months: list[SingleBucket[Range[Date], Double]] = []
# The `date` field has been converted to a string formatted YYYY-MM-DD.
# Convert to type `Date` from the string.
current_month: Date = datetime.strptime(last_bucket.key, date_format).date()

# Loop six times
for _ in range(6):
# Construct the next month from the current month
next_month = current_month + relativedelta(months=1)
# Add a new bucket which uses the next month as the date range
# and the most recent months amount as the value
next_six_months.append(SingleBucket(Range(min=current_month, max=next_month), last_bucket.value))
current_month = next_month

# Append the modified results as a NestedBucket
modified_buckets.append(NestedBucket(bucket.key, next_six_months))

return ThreeDimensionalAggregation(modified_buckets)
```
生成的聚合可用于 Workshop chart 中，以展示未来六个月的每月支出估算值。

The resulting aggregation can be used in a Workshop chart to show the monthly spend estimate for the next six months.