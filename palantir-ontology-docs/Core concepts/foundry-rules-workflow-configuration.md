<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/
---
# Foundry Rules workflow configuration
**workflow configuration editor** 用于修改整个 Foundry Rules workflow 的配置方式；例如，在添加新的 [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) 以便 rule author 使用时，或在修改 [workflow outputs](#workflow-outputs) 时。Workflow configuration editor 可以从 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中访问，前提是 Foundry Rules workflow 已被 [deployed](/docs/foundry/foundry-rules/deploy-foundry-rules/)。Foundry Rules workflow 与一个 Project 关联，并作为资源显示在您的 Project 文件夹中。这控制了对 workflow configuration 的权限，并允许用户重命名、移动或删除该 workflow。

The **workflow configuration editor** is used when making changes to how the entire Foundry Rules workflow is configured; for example, when adding new [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) so that they may be used by rule authors, or when modifying [workflow outputs](#workflow-outputs). The workflow configuration editor can be accessed from the [Ontology Manager](/docs/foundry/ontology-manager/overview/) once a Foundry Rules workflow has been [deployed](/docs/foundry/foundry-rules/deploy-foundry-rules/). The Foundry Rules workflow is tied to a Project and shows as a resource in your Project folder. This controls permissions to the workflow configuration and allows users to rename, move, or delete the workflow.
## Workflow inputs
如 [rule logic inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) 部分所述，configuration editor 的 **Inputs** 面板是 workflow owner 可以添加供 rule author 使用的额外 inputs 的地方。在添加 object inputs 时，owner 还可以选择希望提供哪些关联的 link types。

As explained in the [rule logic inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) section, the **Inputs** pane of the configuration editor is where workflow owners may add additional inputs for use by rule authors. When adding object inputs, the owner may also select which associated link types they wish to make available.
![Foundry Rules workflow inputs](/docs/resources/foundry/foundry-rules/workflow_inputs.png)
## Workflow outputs
Workflow outputs 指定所有 Foundry rules 的输出的目标和格式。每个 output 对应一个不同的 **Foundry dataset**，当构建时，该 dataset 将包含所有引用它的 Foundry rules 的结果。在每个 output 中，可以配置 output column 的名称和类型。您还可以限制 output column [permits and takes as default](/docs/foundry/foundry-rules/permitted-and-default-output-values/) 的值。

Workflow outputs specify the destination and format for the output of all the Foundry rules in the workflow. Each output corresponds to a different **Foundry dataset** which, when built, will contain the results from all Foundry rules that reference it. Within each output, the name and type of the output columns can be configured. You can also restrict what values the output column [permits and takes as default](/docs/foundry/foundry-rules/permitted-and-default-output-values/).
![Foundry Rules workflow output](/docs/resources/foundry/foundry-rules/workflow_outputs.png)
## Transform configuration
本部分包含用于配置生成 Foundry rules 结果的 **Transform** 的其他信息。它包括 rule status dataset 的位置以及应用于该 transform 的任何 **Spark profiles**。本部分代表高级配置，在首次设置 Foundry Rules workflow 时可以忽略。

This section contains additional information for configuring the **Transform** that generates the results of the Foundry rules. It includes the location of the rule status dataset as well as any **Spark profiles** applied to the transform. This section represents advanced configuration and can be ignored when first setting up a Foundry Rules workflow.
![Foundry Rules transform configuration](/docs/resources/foundry/foundry-rules/transform_config.png)
## Rule execution
Foundry Rules workflow configuration 还会生成一个 transforms pipeline 来应用这些 rules。Transforms pipeline 是 rules 生效的地方；例如，通过创建 alerts 或对数据进行分类/打标签。[Data Lineage](/docs/foundry/data-lineage/overview/) 图表下方概述了一个 Foundry Rules pipeline 的示例；pipeline 的确切结构取决于用例，并可能根据需求和情况有显著差异。

The Foundry Rules workflow configuration also generates a transforms pipeline to apply the rules. The transforms pipeline is where the rules take effect; for instance, by creating alerts or categorizing/tagging data. The [Data Lineage](/docs/foundry/data-lineage/overview/) graph below outlines an example Foundry Rules pipeline; the exact structure of a pipeline depends on the use case and may vary significantly based on need and circumstance.
![Data Lineage graph showing the objects backing & writeback datasets, datasets to write rules against, and outputs of rules](/docs/resources/foundry/foundry-rules/foundry_rules_data_lineage.png)
Pipeline 获取支持 [workflow inputs](#workflow-inputs) 的 datasets 以及 rules 的 writeback dataset，并将这些 rules 应用于 inputs。然后，它使用 rules 输出的行填充 [workflow outputs](#workflow-outputs) 中指定的 output datasets。

The pipeline takes the datasets backing the [workflow inputs](#workflow-inputs) together with the writeback dataset of rules and applies these rules to the inputs. It then populates the output datasets specified by the [workflow outputs](#workflow-outputs) with the rows output by the rules.