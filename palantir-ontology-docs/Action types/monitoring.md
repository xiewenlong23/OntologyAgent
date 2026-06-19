<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/monitoring/
---
# Action monitoring
Foundry 中的 Actions 可以被监控以跟踪性能和可靠性。本页说明了 actions 可用的监控功能。

Actions in Foundry can be monitored to track performance and reliability. This page explains the available monitoring capabilities for actions.
## Available monitoring rules
Foundry 中的 Action 监控支持两种关键规则类型：

Action monitoring in Foundry supports two key rule types:
1. **Action duration p95：**当第 95 百分位执行时间超过阈值时发出警报。

2. **Number of action failures in window：**在时间窗口内失败次数超过阈值时发出警报。

1. **Action duration p95:** Alerts when the 95th percentile execution time exceeds thresholds.
2. **Number of action failures in window:** Alerts when failure count exceeds thresholds within a timeframe.
有关详细的配置选项和参数，请查看我们的[监控规则参考文档。](/docs/foundry/monitoring-views/rules-reference/#action-rules)

For detailed configuration options and parameters, review our [monitoring rules reference documentation.](/docs/foundry/monitoring-views/rules-reference/#action-rules).
## Set up action monitoring
要为您的 actions 设置监控，请按照创建 monitoring views 和 rules 的标准流程进行操作：

To set up monitoring for your actions, follow the standard process for creating monitoring views and rules:
1. 按照 [monitoring views 概述文档](/docs/foundry/monitoring-views/overview/#create-a-new-monitoring-view) 中的说明创建一个 monitoring view。

2. 按照 [adding a monitoring rule](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule) 部分中的说明，为某个 action 或 action type 添加一条 monitoring rule。
3. 配置适当的阈值和严重级别。

4. 按照 [alert subscription guide](/docs/foundry/monitoring-views/overview/#subscribe-to-alerts) 设置警报通知。

1. Create a monitoring view as described in the [monitoring views overview documentation](/docs/foundry/monitoring-views/overview/#create-a-new-monitoring-view).
2. Add a monitoring rule for an action or action type as described in the section on [adding a monitoring rule](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule).
3. Configure appropriate thresholds and severity levels.
4. Set up alert notifications following the [alert subscription guide](/docs/foundry/monitoring-views/overview/#subscribe-to-alerts).
![Example monitoring alert setup.](/docs/resources/foundry/action-types/monitoring-alerts.png)
### Dynamic scopes
Action monitors 支持 **Workflow Lineage**、**Workshop** 和 **OSDK application** 作为动态作用域（dynamic scopes）。当您选择其中之一作为 scope 时，监控器会自动跟踪该 scoped resource 使用的所有 actions，并随着 actions 的添加或删除进行调整，无需进一步人工干预。

Action monitors support **Workflow Lineage**, **Workshop**, and **OSDK application** as dynamic scopes. When you select one of these scopes, the monitor automatically tracks all actions the scoped resource uses and adjusts as actions are added or removed without further intervention.
![Select scope dialog showing dynamic scope options for action type monitors, including Workshop module, Workflow Lineage, and Developer Console application.](/docs/resources/foundry/action-types/app-as-dynamic-scope-monitoring.png)
## Related documentation
* [Monitoring rules reference](/docs/foundry/monitoring-views/rules-reference/#action-rules)
* [Monitoring views overview](/docs/foundry/monitoring-views/overview/)
* [Monitoring rules reference](/docs/foundry/monitoring-views/rules-reference/#action-rules)
* [Monitoring views overview](/docs/foundry/monitoring-views/overview/)