<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-inline-metrics/
---
# Inline metrics
Inline metrics 为 application builders 提供了一种简化的方法，用于直接在 chart 中显示关键数据。

Inline metrics provides application builders with a streamlined method for displaying key data directly in the chart.
* Header metrics 与 widget 的 timeline（x 轴）对齐，提供整个 schedule 的高级聚合。

* Row metrics 与每个行对齐，提供对各个 resource 对象的 scheduling 和 assignment 的洞察。

* Header metrics are aligned with the timeline (x-axis) of the widget, offering high-level aggregations for the entire schedule.
* Row metrics are aligned with each row, providing insights into the scheduling and assignment of individual resource objects.

> 📷 **[图片: 配置了 header 和 row metrics 的 scheduling gantt chart。]**

> 📷 **[图片: Scheduling gantt chart configured with header and row metrics.]**

## Functions signature
Inline metrics 需要返回与以下 shape 匹配的 [custom type](/docs/foundry/functions/types-reference/) 列表的 functions。

Inline metrics require functions that return a list of a [custom type](/docs/foundry/functions/types-reference/) that matches the following shape:
```
interface InlineMetricsBucket {
range: IRange<Timestamp>;
value: Double
}
```
Inline metrics 同样支持其他返回类型。

Inline metrics can support alternative return types as well.
```typescript
// NOTE: The name of the interface is not important - only the names of the keys
interface InlineMetricsBucketInteger {
range: IRange<Timestamp>;
value: Integer
}

interface InlineMetricsBucketString {
range: IRange<LocalDate>;
value: string
}
```
`range` key 支持 `Timestamp`、`LocalDate` 或 `Integer`（数值表示 epoch milliseconds）的 `IRange` 类型。

The `range` key can support `IRange` types of `Timestamp`, `LocalDate`, or `Integer` (with numerical values representing epoch milliseconds).
value key 支持 `string`、`Integer` 或 `Double` 类型的值。

The value key can support `string`, `Integer`, or `Double` values.
## Sample header metric function
```typescript

import { IRange, Double, Timestamp } from "@foundry/functions-api";

interface InlineMetricBucketV1Double {
range: IRange<Timestamp>;
value: Double;
}

// Counts the number of tasks within the given range bucketed by a step in days
@Function()
public getInlineMetricsV1WithObjectCounts(startTime: Timestamp, endTime: Timestamp, step: Double): Array<InlineMetricBucketV1Double> {
const tasks = Objects.search().schedulingMaintenanceTask().filter(x =>
x.startTime.range().gte(startTime).lte(endTime)
).all();
const buckets: InlineMetricBucketV1Double[] = [];

let current = startTime;
let count = 0
while (current < endTime) {
const currentEnd: Timestamp = current.plusDays(step);
const tasksInRange = tasks.filter(x => x.startTime! >= current && x.startTime! <= currentEnd);
buckets.push({
range: {
min: current,
max: currentEnd
},
value: tasksInRange.length
})
current = currentEnd;
count++;
}
return buckets
}

```
由于 header metrics 作为 header 与 x 轴一起显示，因此这些 functions 不一定与任何特定对象绑定作为输入。

Since header metrics are displayed as a header alongside the x-axis, these functions are not necessarily tied to any specific objects as inputs.
## Sample row metric function
```typescript
// Returns the name of the row alongside the number bucket to which it belongs
@Function()
public getInlineMetricsV1StringWithObject(techs: ObjectSet<SchedulingTechnician_1>, startTime: Timestamp, endTime: Timestamp, step: Double): Array<InlineMetricBucketV1String> {
const techName = techs.all()[0].fullName;
const buckets: Array<InlineMetricBucketV1String> = [];

let current = startTime;
let count = 0;
while (current < endTime) {
const currentEnd: Timestamp = current.plusDays(step);
buckets.push({
range: {
min: current,
max: currentEnd
},
value: `${techName}-${count}`,
})
current = currentEnd;
count++;
}
return buckets
}
```
Row metrics 接受对应的 row object 作为 runtime input。在配置中指定您的 function 时，您可以将 object parameter 指定为 runtime input，widget 将自动将对应的 row 传递给 function。

Row metrics accept the corresponding row object as runtime input. When specifying your function in the configuration, you can specify the object parameter as runtime input and the widget will automatically pass the corresponding row through to the function for you.

> 📷 **[图片: Metric 配置的 Runtime input。]**

> 📷 **[图片: Runtime input for metric configuration.]**

## Widget configuration
Scheduling Gantt Chart widget config 包含一个 **Metrics** 部分，其中包括 header-level 和 row-level metrics 的 options。

The Scheduling Gantt Chart widget config has a **Metrics** section which includes options for header-level and row-level metrics.

> 📷 **[图片: Scheduling Gantt Chart config 面板中的 Metrics 部分。]**

> 📷 **[图片: Metrics section in the Scheduling Gantt Chart config panel.]**

在 metric 配置设置中，您可以提供显示标题、选择图标，以及/或者设置条件着色。

Within the metric configuration setup, you can provide a display title, select an icon, and/or set up conditional coloring.

> 📷 **[图片: Individual metric configuration screen.]**

> 📷 **[图片: Individual metric configuration screen.]**

