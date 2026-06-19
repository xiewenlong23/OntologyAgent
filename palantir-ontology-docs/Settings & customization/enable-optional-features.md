<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/enable-optional-features/
---
# Enable optional features
可以通过编辑您的 [Rules Workshop application](/docs/foundry/foundry-rules/workshop-application/) 中 Rule Editor widget 的配置来启用或禁用可选功能，如下方截图所示。

Optional features can be enabled or disabled by editing the configuration of the Rule Editor widget within your [Rules Workshop application](/docs/foundry/foundry-rules/workshop-application/), as shown in the screenshot below.
![Optional Features Configuration](/docs/resources/foundry/foundry-rules/enable_optional_features.png)
Foundry Rules 提供了多种可以启用或禁用的可选 logic boards：

There are a range of optional logic boards that can be enabled or disabled for Foundry Rules:
* **Window board：** 支持 [Window functions ↗](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-window.html)。

* **Aggregation board：** 对分组列计算聚合。

* **Join board：** 联接其他 datasets 或 objects。

* **Expression board：** 执行任意 expressions，用于添加列或过滤。

* **Select columns board：** 选择列的子集以传递到下一个 logic board。

* **Union board：** 联合其他 datasets 或 objects。

* **Window board:** Supports [Window functions ↗](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-window.html).
* **Aggregation board:** Computes aggregates over grouped columns.
* **Join board:** Joins additional datasets or objects.
* **Expression board:** Executes arbitrary expressions for adding columns or filtering.
* **Select columns board:** Selects a subset of columns to carry forward to the next logic board.
* **Union board:** Unions additional datasets or objects.
此外，还有一个选项可以启用或禁用从 Contour 导入 rules。

Additionally, there is an option to enable or disable importing rules from Contour.
* **Contour import：** 导入并转换存储在 [Contour analysis](/docs/foundry/contour/core-concepts/) 中的 logic 为 rule。

* **Contour import:** Imports and converts logic stored in a [Contour analysis](/docs/foundry/contour/core-concepts/) to a rule.
最后，Foundry Rules 支持直接基于 time series 数据编写 rules。

Finally, Foundry Rules supports writing rules directly on top of time series data.
* **Time series:** 添加 [time series boards](/docs/foundry/foundry-rules/timeseries-concepts/#add-timeseries-board)，可作为 rule 的一部分直接操作 time series。

* **Time series:** Add [time series boards](/docs/foundry/foundry-rules/timeseries-concepts/#add-timeseries-board) which can manipulate time series directly as part of a rule.