<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/condition/
---
# Condition
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品,为平台中所有的业务自动化提供了统一的入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
Object monitor conditions 定义了何时会检测并记录新的被监控的 Activity。**Threshold** conditions 会产生连续的 true 或 false 状态,而 **event** conditions 会产生离散的事件。Conditions 可以包含多个子条件,并可以引用多个 [input](/docs/foundry/object-monitors/input/) object sets。Object monitors 支持以下 condition 类型:

Object monitor conditions define when new monitored activity will be detected and recorded. **Threshold** conditions result in a continuous true or false status, while **event** conditions produce discrete events. Conditions may include several sub-conditions and may reference multiple [input](/docs/foundry/object-monitors/input/) object sets. Object monitors support the following condition types:
## Event
Event conditions 是最常见的 condition 类型。Event conditions 包括 input 中对象的添加或移除,以及 Metric 的增加或减少条件。每个事件都发生在特定的时间点,并且是一个离散事件。因此,它们在 Activity graph 中显示为点:

Event conditions are the most common condition type. Event conditions include objects added or removed from the input and metric increase or decrease conditions. Each event takes place at a specific time and is a discrete event. As such, they display as dots in the activity graph:
![Activity history tab in Object Monitors app](/docs/resources/foundry/object-monitors/activity-history-graph.png)
在下面的示例中,event condition 使用了一个 input exploration,并检查何时在该 exploration 中使用了新对象。对象可能因为新创建或更改为匹配用于定义 input 的 filter 而被添加。

In the example below, the event condition uses a single input exploration and checks for when new objects are used in that exploration. Objects may be added because they were newly created or changed to match the filters used to define the input.
![Example Sales Opportunity added event condition](/docs/resources/foundry/object-monitors/monitor_event_condition_example.png)
某些 event conditions 可能需要 threshold 子条件。在这些情况下,主条件和子条件都必须为 true,才能检测到事件。例如,可以使用 threshold 子条件来检测 input 对象数量的增加,但前提是必须满足主条件,即 input set 中至少已有 `N` 个对象。

Some event conditions may require a threshold sub-condition. In these cases, both the primary condition and sub-condition must be true for an event to be detected. For example, a threshold sub-condition may be used to detect when the count of input objects increases, but only if the primary condition of having at least `N` objects already in the input set is met.
## Threshold
Threshold conditions 在 inputs 上运行,以产生随时间变化的 `true` 或 `false` 状态。当 threshold 在任一方向被跨越时,都会记录 Activity。使用 threshold 的 Conditions 可以包含任意数量的嵌套子条件。

Threshold conditions are run on the inputs to produce a status of `true` or `false` over time. Activity is recorded when the threshold is crossed in either direction. Conditions using a threshold may include any number of nested sub-conditions.
Object Monitors 应用中 threshold condition 的示例如下所示。在此示例中,该 condition 检查自定义 Sales Opportunities cohort 中 `amount` 的总和是否大于 `10,000`。

An example threshold condition in the Object Monitors application is shown below. In this example, the condition checks for when the sum of `amount` across a custom cohort of Sales Opportunities is greater than `10,000`.
![Example Sales Opportunities threshold condition](/docs/resources/foundry/object-monitors/monitor_threshold_condition_example.png)
> **ℹ️ 注意**

> Threshold conditions 不支持 [realtime evaluation](/docs/foundry/object-monitors/evaluation/#realtime-evaluation)。
> **ℹ️ 注意**

> Threshold conditions do not support [realtime evaluation](/docs/foundry/object-monitors/evaluation/#realtime-evaluation).
## Function-backed
Function-backed conditions 旨在支持更复杂的 condition 定义，包括 event 或 threshold rule 选项不支持的所有内容。Function-backed conditions 的工作原理是定义并发布一个返回 `true` 或 `false` 布尔值的 Function。该 Function 将在 monitor 被评估时被调用，响应必须指示该次执行的结果。如果状态发生变化，将记录一个 event。

Function-backed conditions are designed to allow more complex condition definitions, including anything not supported by the event or threshold rule options. Function-backed conditions work by defining and publishing a function that returns a Boolean value of `true` or `false`. The function will be called when the monitor is evaluated, and the response must indicate the result for that execution. If the status has changed, an event will be recorded.
该 Function 应接受一个被监控 object type 的 `ObjectSet<>`，并返回一个布尔值以指示 condition 是否满足。了解更多关于[为 Object Monitors 编写 Function](/docs/foundry/functions/use-functions/) 的信息。

The Function should take an `ObjectSet<>` of the object type being monitored and return a Boolean value indicating if the condition is met. Learn more about [authoring a Function](/docs/foundry/functions/use-functions/) to use with Object Monitors.
以下示例使用一个 Function 来计算当一组输入的 Sales Opportunity objects 的 `realized_amount` 之和小于 `expected_amount` 之和时的条件。

The example below uses a Function to compute when the sum of `realized_amount` is less than the sum of `expected_amount` for an input set of Sales Opportunity objects.
![Example Function-backed Sales Opportunity condition](/docs/resources/foundry/object-monitors/monitor_function_backed_condition_example.png)
```
@Function()
/**
* This function calculates if the realized amount for a set of sales opportunities is smaller than
* the sum of all the opportunity amounts.
*/
public async calculateOpportunityUnderRealized(opportunities: ObjectSet<SalesOpportunity>): Promise<boolean> {
let amount = await opportunities.sum(o => o.amount)
let amountRealized = await opportunities.sum(o => o.amountRealized)
if (amount !== null && amountRealized !== null && amountRealized < amount) {
return true
} else {
return false
}
}
```
> **ℹ️ 注意**

> Function-backed conditions 不支持 [realtime evaluation](/docs/foundry/object-monitors/evaluation/#realtime-evaluation)。此外，Function-backed conditions 只能与 threshold conditions 一起使用，并且只能通过输出单个布尔值来实现。
> **ℹ️ 注意**

> Function-backed conditions do not support [realtime evaluation](/docs/foundry/object-monitors/evaluation/#realtime-evaluation). Additionally, Function-backed conditions may only be used with threshold conditions and only by outputting a single Boolean value.