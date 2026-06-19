<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/timeseries-concepts/
---
# Time series rules \[Sunset]
> **⚠️ 警告: Sunset**

> Foundry Rules 中的时间序列功能处于开发周期的 [sunset](/docs/foundry/platform-overview/development-life-cycle/) 阶段，将在未来的某个日期被弃用。仍提供全面支持。我们建议您将工作流迁移到 [time series alerting automations](/docs/foundry/time-series/alerting-overview/) 以满足任何新的时间序列规则需求。
> **⚠️ 警告: Sunset**

> Time series capabilities in Foundry Rules are in the [sunset](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be deprecated at a future date. Full support remains available. We recommend migrating your workflows to [time series alerting automations](/docs/foundry/time-series/alerting-overview/) for any new time series rules requirements.
除了对 datasets 和 objects 进行操作外，Foundry Rules 还使用户能够管理使用时间序列数据的规则。通过 Foundry Rules，用户可以编写规则来识别数据中的感兴趣时间段。这些时间间隔作为行由 Foundry rules 输出，并可在下游使用，无论是用于告警还是其他用例。Foundry Rules 目前支持转换现有时间序列；例如，使用 aggregates、formulas 和 derivatives，以及基于多个条件识别 intervals。

In addition to operating on datasets and objects, Foundry Rules enables users to manage rules that use time series data. With Foundry Rules, users can write rules that identify time periods of interest within the data. These time intervals are output as rows by the Foundry rules and can be consumed downstream, either for alerting or other use cases. Foundry Rules currently supports transforming existing time series; for example, using aggregates, formulas, and derivatives, as well as identifying intervals based on multiple criteria.
Foundry Rules 构建在 Foundry 的 [time series](/docs/foundry/time-series/time-series-overview/) 之上，并支持 [time series properties](/docs/foundry/time-series/time-series-concepts-glossary/#time-series-property-tsp) 和 measures。

Foundry Rules builds on top of [time series](/docs/foundry/time-series/time-series-overview/) in Foundry and supports [time series properties](/docs/foundry/time-series/time-series-concepts-glossary/#time-series-property-tsp) and measures.
要将时间序列与 Foundry Rules 一起使用，请遵循 [deployment instructions](/docs/foundry/foundry-rules/deploy-timeseries-foundry-rules/)。

To use time series with Foundry Rules, follow the [deployment instructions](/docs/foundry/foundry-rules/deploy-timeseries-foundry-rules/).
## Time series boards
规则可以包含所有标准的 Foundry Rules [logic](/docs/foundry/foundry-rules/rule-logic/)，以及两种类型的时间序列 boards：**Add Timeseries** 和 **Timeseries Search**。

Rules can contain all the standard Foundry Rules [logic](/docs/foundry/foundry-rules/rule-logic/), as well as two types of time series boards: **Add Timeseries** and **Timeseries Search**.
### Add Timeseries board
Add Timeseries board 将一个 series 作为输入，并生成一个修改后的 series，然后该 series 可供后续 boards 使用。转换后的 series 是使用名称 (1) 和 operation (2) 以及该 operation 所需的配置来定义的。例如，下图所示的 board 添加了一个新的 series `$baseline`，该 series 是使用 1000 天的 rolling aggregate 创建的。可以使用 "Preview Timeseries" 按钮 (3) 预览生成的时间序列。

The Add Timeseries board takes a series as input and produces a modified series which can then be consumed by later boards. A transformed series is defined using a name (1) and an operation (2), with the necessary configuration for that operation. For example, the board depicted below adds a new series `$baseline`, created using a rolling aggregate over 1000 days. The resulting time series can be previewed using the ‘Preview Timeseries’ button (3).
![add timeseries](/docs/resources/foundry/foundry-rules/add_timeseries.png)
### Timeseries Search board
Timeseries Search board 根据指定的条件为输入集合中的每个 object 生成 intervals。这些条件可以引用链接到原始 root object 的 series 以及由先前的 **Add Timeseries** boards 创建的任何 series。object 上现有的 measures 以 `@` 为前缀，而作为规则一部分添加的任何 series 以 `$` 为前缀。匹配条件的 intervals 也可以使用 "Preview Intervals" 按钮进行预览。

The Timeseries Search board produces intervals for every object in the input set based on the conditions specified. The conditions may reference both series linked to the original root object as well as any series created by previous **Add Timeseries** boards. Measures existing on the object are prefixed with `@`, while any series added as part of the rule are prefixed with `$`. The intervals matching the conditions can also be previewed using the ‘Preview Intervals’ button.
对于输入中的每个 root object，输出 dataset 中将存在一组匹配的 intervals，作为包含 interval data 的列序列：start time、end time 和 duration。

For every root object in the input, a set of matching intervals will be present in the output dataset as a series of columns containing the interval data: start time, end time, and duration.
![timeseries search](/docs/resources/foundry/foundry-rules/timeseries_search.png)