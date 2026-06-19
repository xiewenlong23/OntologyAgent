<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/configure-rule-actions/
---
# Configure rule Actions
> **⚠️ 警告**

> 在 2022 年 7 月之前，Foundry Rules（以前称为 Taurus）使用 Foundry Actions 作为规则输出。如果您是在 2022 年 7 月之前部署的 Foundry Rules，则本节内容仅与您相关。
> **⚠️ 警告**

> Prior to July 2022, Foundry Rules (previously known as Taurus) used Foundry Actions as rule outputs. This section is only relevant if you deployed Foundry Rules prior to July 2022.
Rule Actions 是 Foundry Rules 中一种用于对规则输出强制实施输出 schema 的方法。这是通过使用 Foundry Actions 作为指定列名和类型的机制来实现的。Rule Action 是一种将在 Foundry Rules 中使用的 Foundry Action。

Rule Actions are a means within Foundry Rules to enforce an output schema on a rule's output. This is accomplished by using Foundry Actions as the mechanism for specifying the column names and types. A rule Action is a Foundry Action that will be used in Foundry Rules.

> 📷 **[图片: 为在 Foundry Rules 中使用而配置 Foundry Action]**

> 📷 **[图片: Configuring a Foundry Action for use in Foundry Rules]**

上图中显示的 Action 仅 [在 transform 内部使用](/docs/foundry/foundry-rules/configure-transforms-pipeline/#rule-action-datasets)，不会单独运行。最好不为该 Action 配置任何 Action 规则（上图中的 **1**），这样即使该 Action 被运行，也不会产生任何影响。

The Action in the screenshot above is only [used within the transform](/docs/foundry/foundry-rules/configure-transforms-pipeline/#rule-action-datasets) and will not be run on its own. It is convenient to have no Action rules configured for the Action (**1** in the screenshot above) so if the Action were to be run, it would have no effect.
Action 的参数将展示给 Foundry Rules Workshop 应用程序中的最终用户，并可用于映射到规则逻辑输出的列（上图中的 **2**）。

The parameters of the Action will be presented to end users in the Foundry Rules Workshop application and made available to map to columns output by the rule logic (**2** in the screenshot above).
* 参数类型将用于强制约束正确的列类型。例如，如果使用 date 类型参数，则只有 date 和 timestamp 类型的列可以映射到该参数。此外，如果参数 ID 与规则中的列名或 object property ID 匹配，则将使用该列/property 预填参数。

* 标记为 required 的参数在 Foundry Rules Workshop 应用中也将是必填项。类似地，可选参数可以留空而不映射任何列，这等同于向参数提供 `null` 值。

* 参数名称将用作 Foundry Rules Workshop 应用中的标签，参数 ID 将用作 [transform 中生成的数据集](/docs/foundry/foundry-rules/configure-transforms-pipeline/#rule-action-datasets) 的列名。

* 除了参数 ID 之外，输出数据集还将包含一个 `taurus_rule_id` 列，用于指示该行来源的规则的 rule ID。

* The parameter types will be used to enforce the correct column types. For example, if a date type parameter is used, then only date and timestamp type columns will be available to map to this parameter. Furthermore, if the parameter ID matches a column name or an object property ID from your rule, it will be used to pre-fill the parameter with this column/property.
* Any parameters that are marked as required will also be required in the Foundry Rules Workshop application. Similarly, optional parameters may be left blank with no column mapped to them, which is equivalent to providing the `null` value to the parameter.
* The parameter names will be used as labels in the Foundry Rules Workshop application, and the parameter IDs will be used as the column names in [the resulting dataset in the transform](/docs/foundry/foundry-rules/configure-transforms-pipeline/#rule-action-datasets).
* In addition to the parameter IDs, the output dataset will also contain a `taurus_rule_id` column to indicate the rule ID of the rule the row originated from.
定义 **Submission Criteria**（**3**）是保存 Action 的必要条件。rule actions 最常见的 submission criterion 是检查 **Current User** 是否属于具有编辑 Foundry Rules workflow 权限的用户组。此验证将在 Foundry Rules App 中编辑规则时应用。

Defining **Submission Criteria** (**3**) is a requirement for saving an Action. The most common submission criterion for rule actions is checking that the **Current User** belongs to a user group with permissions to edit the Foundry Rules workflow. This validation will be applied when editing a rule in the Foundry Rules App.