<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/function-metrics/
---
# Function metrics
Function metrics 显示过去 30 天内 function type 的近实时使用情况。您可以从 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中 [function type 的概览](/docs/foundry/ontology-manager/overview/#function-type-view) 页面访问这些 metrics，或者在 [Workflow Lineage](/docs/foundry/workflow-lineage/overview/) 中选择给定执行的 function 节点来访问。可用的 metrics 如下：

Function metrics display the near real-time usage of a function type over the last 30 days. You can access these metrics from a [function type's overview](/docs/foundry/ontology-manager/overview/#function-type-view) page in [Ontology Manager](/docs/foundry/ontology-manager/overview/), or in [Workflow Lineage](/docs/foundry/workflow-lineage/overview/) by selecting the function node for a given execution. The following metrics are available:
* **成功/失败 metrics：** 通过成功和失败次数监控您 function 的当前状态。这有助于快速识别问题并支持主动 troubleshooting，使您能够在失败发生时立即处理。

* **P95 duration metric：** 跟踪每个 function type 的第 95 百分位（P95）执行时长。此 metric 突出显示执行时间的上限范围，帮助您检测性能瓶颈并优化 workflows，以实现一致且高效的运行。

* **Success/failure metrics:** Monitor the current status of your functions with success and failure counts. This enables rapid identification of issues and supports proactive troubleshooting, allowing you to address failures as soon as they occur.
* **P95 duration metric:** Track the 95th percentile (P95) execution duration for each function type. This metric highlights the upper range of execution times, helping you detect performance bottlenecks and optimize workflows for consistent and efficient operation.
您还可以访问 [run history](/docs/foundry/aip-observability/run-history/)，它提供了过去七天内给定 function 执行的完整视图。了解更多关于 [AIP observability](/docs/foundry/aip-observability/overview/) 的信息。

You are also able to access [run history](/docs/foundry/aip-observability/run-history/), which provides a complete view of a given function's executions over the past seven days. Learn more about [AIP observability](/docs/foundry/aip-observability/overview/).
![Screenshot of function metrics in the overview section.](/docs/resources/foundry/functions/function-metrics.png)
所有 metrics 均使用来自 Foundry Telemetry Service (FTS) 的最新数据进行近实时更新。这确保您能够访问最新信息以监控、调试和维护 function 的健康状态。

All metrics are updated in near real-time using the latest data from the Foundry Telemetry Service (FTS). This ensures you have access to the most current information for monitoring, debugging, and maintaining the health of your functions.
## Function failure types
Function metrics 有多种类别的失败可能会显示。这些类别包括：

Function metrics have a variety of categories of failures that may be displayed. These categories are:
* **Runtime failure：** 在执行 function 时发生了意外错误，通常是由于 function 代码中的 bug 或未处理的情况所致。

* **Resource limit exceeded：** 该 function 影响的 object type 超过了允许的限制（默认情况下通常为 10,000）。

* **User facing error：** 发生了一个专门打算显示给用户的错误，通常提供有关出错原因或如何修复的指导。

* **Invalid inputs error：** 提供给 function 的一个或多个 inputs 无效或不符合所需条件。

* **Invalid output error：** function 生成的 output 无效或不符合预期的格式或规则。

* **Data loading not allowed error：** function 执行尝试加载数据（包括 objects、object sets、users 或 groups），但不允许这样做。

* **Undeclared object types edited error：** function 执行尝试更新、创建或删除其 object type 未在 function spec 中声明的 object。

* **Structured error：** function 执行遇到其 spec 上定义的 structured error。

* **Deployment error：** function 执行因 function 部署错误而失败。

* **Consistent snapshot error：** function 由于 consistent snapshot 错误而无法执行。

* **Runtime failure:** An unexpected error occurred while executing the function, often due to a bug or unhandled situation in the function's code.
* **Resource limit exceeded:** The function affected more than the permitted limit of object types (by default, usually 10,000).
* **User facing error:** An error occurred that is specifically intended to be shown to the user, often providing guidance on what went wrong or how to fix it.
* **Invalid inputs error:** One or more of the inputs provided to the function were not valid or did not meet the required criteria.
* **Invalid output error:** The function produced output that was not valid or did not conform to the expected format or rules.
* **Data loading not allowed error:** The function execution attempts to load data, including objects, object sets, users, or groups, but is not allowed to do so.
* **Undeclared object types edited error:** The function execution attempts to update, create or delete an object whose object type is not declared in the function spec.
* **Structured error:** The function execution encounters a structured error as defined on its spec.
* **Deployment error:** The function execution failed due to an error with the function's deployment.
* **Consistent snapshot error:** The function failed to execute due to a consistent snapshot error.
## Permissions
要查看 function metrics，您必须是该 function 的 `viewer`。

To view function metrics, you must be a `viewer` on the function.