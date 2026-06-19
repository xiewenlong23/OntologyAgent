<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/monitoring/
---
# Function monitoring
Foundry 中的 functions 可以被监控，以跟踪其性能和可靠性。本页说明了可用于 functions 的监控能力。

Functions in Foundry can be monitored to track performance and reliability. This page explains the available monitoring capabilities for functions.
## Available monitoring rules
Foundry 中的 Function 监控支持以下规则类型：

Function monitoring in Foundry supports the following rule types:
1. **Function duration p95（第 95 百分位执行时长）：** 当第 95 百分位执行时间超过阈值时触发告警。

2. **Number of function failures in window（时间窗口内的 Function 失败次数）：** 当在特定时间范围内的总失败次数超过阈值时触发告警。此规则会跟踪所有类型的失败。

3. **Number of user-facing function failures in window（时间窗口内的面向用户的 Function 失败次数）：** 当在特定时间范围内面向用户的失败次数超过阈值时触发告警。此规则仅跟踪由 Function 代码抛出的面向用户的错误。

4. **Number of non-user-facing function failures in window（时间窗口内的非面向用户的 Function 失败次数）：** 当在特定时间范围内非面向用户的失败次数超过阈值时触发告警。此规则排除了面向用户的错误，因此非常适合用于监控基础设施和系统级别的故障。

1. **Function duration p95:** Alerts when the 95th percentile execution time exceeds thresholds.
2. **Number of function failures in window:** Alerts when the total failure count exceeds thresholds within a timeframe. This rule tracks all failure types.
3. **Number of user-facing function failures in window:** Alerts when the count of user-facing failures exceeds thresholds within a timeframe. This rule tracks only user-facing errors thrown by function code.
4. **Number of non-user-facing function failures in window:** Alerts when the count of non-user-facing failures exceeds thresholds within a timeframe. This rule excludes user-facing errors, making it useful for monitoring infrastructure and system-level failures.
有关每种规则类型的详细配置选项和参数，请参阅 [monitoring rules reference documentation](/docs/foundry/monitoring-views/rules-reference/#function-rules)。

For detailed configuration options and parameters for each rule type, review the [monitoring rules reference documentation](/docs/foundry/monitoring-views/rules-reference/#function-rules).
## Set up function monitoring
要为您的 Functions 设置监控，请按照创建监控视图和规则的标准流程进行操作：

To set up monitoring for your functions, follow the standard process for creating monitoring views and rules:
1. 按照 [monitoring views overview documentation](/docs/foundry/monitoring-views/overview/#create-a-new-monitoring-view) 中所述创建一个监控视图。

2. 按照 [adding a monitoring rule](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule) 部分所述，为 Functions 添加一条监控规则。
3. 配置适当的阈值和严重级别。

4. 按照 [alert subscription guide](/docs/foundry/monitoring-views/overview/#subscribe-to-alerts) 设置告警通知。

1. Create a monitoring view as described in the [monitoring views overview documentation](/docs/foundry/monitoring-views/overview/#create-a-new-monitoring-view).
2. Add a monitoring rule for functions as described in the section on [adding a monitoring rule](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule).
3. Configure appropriate thresholds and severity levels.
4. Set up alert notifications following the [alert subscription guide](/docs/foundry/monitoring-views/overview/#subscribe-to-alerts).
![Example monitoring alert setup.](/docs/resources/foundry/functions/monitoring-alerts.png)
### Dynamic scopes
Function 监控器支持 **Workflow Lineage**、**Workshop** 和 **OSDK application** 作为动态作用域。当您选择这些作用域之一时，监控器会自动跟踪该作用域资源所使用的所有 Functions，并在 Functions 添加或移除时自动调整，无需进一步干预。

Function monitors support **Workflow Lineage**, **Workshop**, and **OSDK application** as dynamic scopes. When you select one of these scopes, the monitor automatically tracks all functions the scoped resource uses and adjusts as functions are added or removed without requiring further intervention.
![Select scope dialog showing dynamic scope options for function monitors.](/docs/resources/foundry/functions/functions-app-as-dynamic-scope-monitoring.png)
## Related documentation
* [Monitoring rules reference](/docs/foundry/monitoring-views/rules-reference/#function-rules)
* [Monitoring views overview](/docs/foundry/monitoring-views/overview/)
* [External system integration](/docs/foundry/monitoring-views/external-systems/) 用于告警

* [Monitoring rules reference](/docs/foundry/monitoring-views/rules-reference/#function-rules)
* [Monitoring views overview](/docs/foundry/monitoring-views/overview/)
* [External system integration](/docs/foundry/monitoring-views/external-systems/) for alerts