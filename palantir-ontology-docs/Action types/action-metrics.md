<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/action-metrics/
---
# Action metrics
Action metrics 显示过去 30 天内某 action type 的近实时使用情况。您可以从 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中 action type 的概览页面访问这些 metrics，也可以在 [Workflow Lineage](/docs/foundry/workflow-lineage/overview/) 中通过选择某次执行的 action 节点来访问。可用的 metrics 如下：

Action metrics display the near real-time usage of an action type over the last 30 days. You can access these metrics from the action type's overview page in [Ontology Manager](/docs/foundry/ontology-manager/overview/), or in [Workflow Lineage](/docs/foundry/workflow-lineage/overview/) by selecting the action node for a given execution. The following metrics are available:
* **成功/失败指标：** 通过成功和失败计数监控您操作的当前状态。这有助于快速识别问题并支持主动排查，使您能够在故障发生后立即进行处理。

* **P95 时长指标：** 跟踪每个 Action Type 的第 95 百分位（P95）执行时长。此指标突出显示了执行时长的上限范围，帮助您检测性能瓶颈并优化工作流，以实现稳定高效运行。

* **Success/failure metrics:** Monitor the current status of your actions with success and failure counts. This enables rapid identification of issues and supports proactive troubleshooting, allowing you to address failures as soon as they occur.
* **P95 duration metric:** Track the 95th percentile (P95) execution duration for each action type. This metric highlights the upper range of execution times, helping you detect performance bottlenecks and optimize workflows for consistent and efficient operation.
您还可以访问 [run history](/docs/foundry/aip-observability/run-history/)，该功能提供过去七天内特定 Action 执行情况的完整视图。详细了解 [AIP observability capabilities](/docs/foundry/aip-observability/overview/)。

You are also able to access [run history](/docs/foundry/aip-observability/run-history/), which provides a complete view of a given action's executions over the past seven days. Learn more about [AIP observability capabilities](/docs/foundry/aip-observability/overview/).
![Screenshot of action metrics in the overview section.](/docs/resources/foundry/action-types/action-metrics-failures.png)
所有指标均使用来自 Foundry Telemetry Service (FTS) 的最新数据进行近实时更新。这可确保您能够访问最新的信息，以监控、调试并维护 Action 的健康状况。

All metrics are updated in near real-time using the latest data from the Foundry Telemetry Service (FTS). This ensures you have access to the most current information for monitoring, debugging, and maintaining the health of your actions.
## Action failure types
Action 指标无需启用 Action 日志即可显示。与 Action 日志不同，Action 指标会跟踪失败情况。

Action metrics do not require action logs to be displayed. Unlike action logs, action metrics track failures.
Action 指标具有多种可能显示的失败类别。这些类别包括：

Action metrics have a variety of categories of failures that may be displayed. These categories are:
* **Invalid parameter failure（无效参数失败）：** Action 提交时包含一个或多个在 Action 上下文中无效的参数。

* **Scale limit failure（规模限制失败）：** Action 影响的 Object Type 数量超过了允许的上限（默认通常为 10,000）。

* **Authentication failure（身份验证失败）：** 用户未通过 Action 的安全提交标准。

* **Side effect failure（副作用失败）：** 由于 Webhook 或副作用配置错误导致 Action 失败。

* **Function failure（函数失败）：** 由于底层 Function 失败导致 Action 失败。此失败模式仅适用于 function-backed actions。

* **User-facing function failure（面向用户的函数失败）：** 支持该 Action 的 Function 抛出了意图显示给用户的错误。此失败模式仅适用于 function-backed actions。

* **Conflict failure（冲突失败）：** 由于冲突（例如并发修改）导致 Action 失败。

* **Unclassified failure（未分类失败）：** Action 失败未归入上述任何类别。

* **Invalid parameter failure:** The action was submitted with a parameter or parameters that are not valid within the context of the action.
* **Scale limit failure:** The action affected more than the permitted limit of object types (by default, usually 10,000).
* **Authentication failure:** The user did not pass the security submission criteria for the action.
* **Side effect failure:** The action failed due to a webhook or an incorrectly configured side effect.
* **Function failure:** The action failed because the underlying function failed. This failure mode is only possible for function-backed actions.
* **User-facing function failure:** The function backing the action threw an error intended to be displayed to the user. This failure mode is only possible for function-backed actions.
* **Conflict failure:** The action failed due to a conflict, such as a concurrent modification.
* **Unclassified failure:** The action failure did not fall into any of the above categories.
## Permissions
要查看 Action 指标，您必须是该 Action 的 `viewer`。

To view action metrics, you must be a `viewer` on the action.