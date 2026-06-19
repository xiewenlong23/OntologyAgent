<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/machinery/process-mining/
---
# Process mining
使用 Machinery 应用程序创建 process model 有几种方法：你可以通过 [绘制 states 和 transitions](/docs/foundry/machinery/draw-a-graph/) 手动定义 process，也可以通过 *process mining* 从历史观测中自动推导 process model。

There are several ways to create a model of a process using the Machinery application: you can define a process manually by [drawing states and transitions](/docs/foundry/machinery/draw-a-graph/), or you can derive a process model automatically from historical observations by *process mining*.
Machinery 支持将 Process Mining 作为专用模式。Process Mining workflow 可通过主工具栏访问，前提是已配置 [data connection](/docs/foundry/machinery/connect-data/)。

Process mining is supported as a dedicated mode in Machinery. The process mining workflow is accessible through the main toolbar once a [data connection has been configured](/docs/foundry/machinery/connect-data/).
![Process mining view with filter set.](/docs/resources/foundry/machinery/process-mining.png)
在 mining 模式下，您将看到现有的 process definition 与数据中发生的状态和 transition 相叠加。样式说明如下：

In mining mode, you will see your existing process definition overlaid with states and transitions as they occur in the data. The styling indicates the following:
* **Amber：**Mining 结果。确认后，这些元素将添加到您的 process definition 中。

* **Gray：**这些元素存在于数据中，但已存在于您的 process definition 中。

* **Dashed line：**当前 process definition 中在数据里没有引用的元素。这可能表明您的 process definition 存在问题。

* **Amber:** The mining result. These elements will be added to your process definition once you confirm.
* **Gray:** These elements occur in data but already exist in your process definition.
* **Dashed line:** Elements from the current process definition that have no reference in the data. This may indicate an issue with your process definition.
## Settings
在 mining 侧边面板顶部，您可以配置应使用哪些数据源进行 mining：process object、log object 或两者。虽然可以仅从 process object type 中 mining 最新的 state 值，但建议使用 log object type。

At the top of the mining side panel, you can configure which data source should be used for mining: process objects, log objects, or both. While it is possible to mine only the latest state values from the process object type, a log object type is recommended.
此外，您可以选择要 mining 的元素：state、transition 或两者。通常，在相关数据源可用的情况下，您应该同时 mine state 和 transition。

In addition, you can select what elements should be mined: states, transitions, or both. Typically, you should mine both states and transitions if the relevant datasources are available.

> 📷 **[图片: Mining side panel settings.]**

> 📷 **[图片: Mining side panel settings.]**

## Filtering
收集的数据通常包含噪声和错误。Mining 的原始输出可能过于复杂或包含意外结果。Machinery 允许您从数据中过滤 state 和 transition，以帮助您生成更可用的 process 表示。

Collected data often contains noise and errors. The raw output from mining can be too complex or contain unexpected results. Machinery allows you to filter states and transitions from the data to help you produce a more usable representation of your process.

> 📷 **[图片: Mining filters and exclusions.]**

> 📷 **[图片: Mining filters and exclusions.]**

在 mining 侧边面板底部，您可以配置过滤器。

At the bottom of the mining side panel, you can configure filters.
* **Transition filter：**此过滤器按出现次数对所有 transition 进行排序，出现频率最高的 transition 排在最前面。然后计算所有这些值的累计总和，并保留所有 transition 中排名前 *x*% 的部分。这样可以剔除不常见 transition 的尾部。

* **Excluded elements：**不应被接受到 process definition 中的错误 state 值或 transition 列表。这些排除的值在保存时会持久化，并可随时间进行管理。

* **Transition filter:** This filter sorts all transitions by their occurrence, with the most frequent transitions ranked highest. It then computes a cumulative sum of all those values and keeps the top *x* % of all transitions. This cuts off the tail-end of infrequent transitions.
* **Excluded elements:** A list of erroneous state values or transitions that should not be accepted into the process definition. These excluded values are persisted when saving and can be managed over time.