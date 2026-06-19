<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/rule-logic/
---
# Rule logic
每个 Foundry rule 都有与之关联的 logic。该 logic 由三部分组成:

Each Foundry rule has logic associated with it. This logic is formed of three parts:
1. [Inputs:](#inputs) Foundry rule 的数据输入。

2. [Logic blocks:](#logic-blocks) 应用于所选输入的 transformations。

3. [Rule output:](#rule-output) rule 的输出格式。

1. [Inputs:](#inputs) The data inputs to a Foundry rule.
2. [Logic blocks:](#logic-blocks) The transformations to be applied to the selected input(s).
3. [Rule output:](#rule-output) The output format of the rule.
![Foundry Rules logic example with the three parts described above](/docs/resources/foundry/foundry-rules/labeled_foundry_rules_logic.png)
*所有截图均使用虚拟数据。*

*All screenshots use notional data.*
## Inputs
Foundry rule 的 inputs 可以是 datasets 或 objects,具体取决于用例。但是,使用 objects 作为 inputs 提供了更友好的用户界面以及额外功能,例如 filter 值的自动完成下拉列表。

The inputs to a Foundry rule can be either datasets or objects, depending on the use case. However, using objects as inputs provides a more user-friendly interface as well as extra features, such as autocomplete dropdowns for filter values.
rule authors 可用的 datasets 和 objects 由工作流所有者在 [Foundry Rules workflow configuration](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/) 中进行配置。

The datasets and objects available to rule authors are configured by the workflow owner in the [Foundry Rules workflow configuration](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/).
> **⚠️ 警告**

> Foundry Rules 不支持由多个数据源支持、具有多个 materializations 或使用 edit-only properties 的 object types。
> **⚠️ 警告**

> Foundry Rules does not support object types that are either backed by multiple data sources, have multiple materializations, or use edit-only properties.
> **ℹ️ 注意**

> 由 restricted view 支持的 objects 不能直接用作 inputs。请改为将支持 restricted view 的 dataset 配置为 [alternate backing dataset](/docs/foundry/foundry-rules/configure-workflow/#alternate-backing-datasets)。
> **ℹ️ 注意**

> Objects backed by a restricted view cannot be used as inputs directly. Instead, configure the dataset which backs the restricted view as an [alternate backing dataset](/docs/foundry/foundry-rules/configure-workflow/#alternate-backing-datasets).
## Logic blocks
应用于规则输入的 transformations 以一系列 logic block 表示。可用的 transformations 包括 filtering、expressions、aggregates 和 joins。也可以配置哪些 transformations 对最终用户可用。了解更多关于 [enabling optional features](/docs/foundry/foundry-rules/enable-optional-features/) 的信息。

The transformations applied to the rule's inputs are represented as a series of logic blocks. The available transformations include filtering, expressions, aggregates, and joins. It is also possible to configure which of these transformations are made available to the end user. Learn more about [enabling optional features](/docs/foundry/foundry-rules/enable-optional-features/).
每个 logic block 接收来自前一个 block/source 输出的行，并应用该 transformation，输出一组新的行和列。可以通过单击 block 右上角的 **Preview** 按钮查看输出。

Each logic block takes rows output from the previous block/source and applies the transformation, outputting a new set of rows and columns. The output can be viewed by clicking the **Preview** button in the top right of the block.
## Rule output
规则的末端是 rule output。每个 rule output 对应一个 output dataset，其在 [Foundry Rules workflow configuration](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/) 中配置。因此，所选的 output 决定了由 Foundry rule 输出的行的目标和格式。每个字段的 interface 可以根据其接受的 [值的类型进行定制](/docs/foundry/foundry-rules/permitted-and-default-output-values/)。*生成的 output dataset 将包含所有使用该 output 的规则所输出的行*。这种设计旨在使不同规则的输出更容易保持一致性。

At the end of the rule is the rule output. Each rule output corresponds to an output dataset, as configured in the [Foundry Rules workflow configuration](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/). The selected output therefore specifies the destination and format for the rows output by the Foundry rule. The interface for each field may be [tailored to the type of values it accepts](/docs/foundry/foundry-rules/permitted-and-default-output-values/). *The output dataset produced will contain the rows output by all rules which use that output*. This behavior is designed to make it easier to achieve consistency in the output of different rules.
Rule output 允许 workflow owner 强制规定 rule author 必须从其 logic 中输出的确切列和类型。在视觉上，这种强制通过一个表单来表示，其中每个表单输入对应 output dataset 中的一列。

The rule output allows workflow owners to enforce the exact columns and types that rule authors must output from their logic. Visually, this enforcement is represented as a form where each form input corresponds to a column in the output dataset.
如果同一 application 中的不同 Foundry rules 必须输出具有不同 schema 的行，那么可以配置多种不同的 rule outputs 供选择。或者，如果 schema 相似，则可以将某些 Action parameters 配置为可选，而不是创建一个新的 rule Action，这样可能会更简单。

If different Foundry rules within the same application must output rows with different schema, then it is possible to configure a choice of several different rule outputs. Alternatively, if the schemas are similar, then it may be easier to configure some of the Action parameters to be optional, instead of creating a new rule Action.
了解更多关于 [configuring rule outputs](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/#workflow-outputs) 的信息。

Learn more about [configuring rule outputs](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/#workflow-outputs).
![Configured rule Action with corresponding output dataset](/docs/resources/foundry/foundry-rules/rule_action_output_column_mapping.png)