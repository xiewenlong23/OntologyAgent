<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/configure-transforms-pipeline/
---
# Configure transforms pipeline
> **⚠️ 警告**

> 2022 年 7 月之前，Foundry Rules（之前称为 Taurus）要求用户创建自己的 transform 来运行 Foundry Rules。本节内容仅适用于在 2022 年 7 月之前部署 Foundry Rules 的情况。
> **⚠️ 警告**

> Prior to July 2022, Foundry Rules (previously known as Taurus) required users to create their own transform to run Foundry Rules. This section is only relevant if you deployed Foundry Rules prior to July 2022.
规则在 [Workshop 应用程序中编写并审核](/docs/foundry/foundry-rules/author-and-run-a-rule/) 后，编码后的逻辑将作为 transform 的一部分应用。本节介绍 transform 的各个组件以及如何根据您的使用场景进行配置。transform 的大部分内容通过默认部署进行配置；但是，对工作流的扩展可能需要额外的步骤。

Once rules have been [written and reviewed in the Workshop application](/docs/foundry/foundry-rules/author-and-run-a-rule/), the encoded logic is applied as part of a transform. This section explains the various components of the transform and how to configure them for your use case. The majority of the transform is configured by default via the default deployment; however, extensions to the workflow may require additional steps.
## Example transform
在 [部署 Foundry Rules transform](/docs/foundry/foundry-rules/deploy-workflow/) 之后，transform 将类似于以下示例：

After [deploying the Foundry Rules transform](/docs/foundry/foundry-rules/deploy-workflow/), the transform will look similar to the example below:
```java
public final class FoundryRulesTransformExample {
// In addition to replacing the RIDs below, you will also need to import the relevant object types
// and relations into the Project using the "Ontology" section of the 'Settings' tab above
@AdditionalInputs
public static Set<InputSpec> additionalInputs = ImmutableOntologyInputs.builder()
.addObjectRids("ri.ontology.main.object-type.4168ed49-00...") // employee
// .addLinkRids("...") // add all referenced relations
.ontologyRid("ri.ontology.main.ontology.00000000-0000-0000-0000-000000000000")
.ontologyBranchRid("ri.ontology.main.branch.00000000-0000-0000-0000-000000000000")
.build()
.getInputSpecs();

@Compute
public void compute(
@Input("ri.foundry.main.dataset.0000...") FoundryInput source_object_backing_dataset,
@Input("ri.foundry.main.dataset.0000...") FoundryInput rules_input,
@Output("ri.foundry.main.dataset.0000...") FoundryOutput outcome_output,
@Output("REPLACE WITH PATH TO WRITE STATUS DATASET TO") FoundryOutput rule_status_output,
TransformContext transformContext) {

Dataset<Row> source = source_object_backing_dataset.asDataFrame().read();
Dataset<Row> rulesDataset = rules_input.asDataFrame().read();

// Configuring the Taurus Rule Runner
Args ruleRunnerArgs = new TaurusRuleRunner.Args.Builder()
.rules(new Rules.Builder()
.logicColumnName("RuleLogic")
.ruleIdColumnName("RuleId")
.dataset(rulesDataset)
.build())
// Put all sources used in Foundry Rules editor Workshop app here (for datasets the name here
// must match the dataset name in the Foundry Rules app)
.putSources(SourceReference.objectTypeId("employee"), source)
// .putSources(SourceReference.dataset(DatasetName.of("name in Foundry Rules app")), dataset)
// Required if you use many-many ontology join tables:
// .manyToManyJoinTables(ImmutableMap.of(LinkTypeId.of("relation-id"), dataset))
// set to true to ensure the rule execution output matches the rule editor widget's preview (this flag is false by default)
// .shouldMatchContourExecutionBehavior(true)
.context(transformContext)
.build();

// Run the rules using Spark (lazily evaluated)
RuleEffects ruleEffects = TaurusRuleRunner.runRules(ruleRunnerArgs);

// Get the results from all the rules that use the specified actions
Dataset<Row> outcomes = ruleEffects.actionReadyMergedDataset(
ActionTypeRid.valueOf("ri.actions.main.action-type.b6f052c7-f7b1-4b4f-83ee-f81d9e854114"));
outcome_output.getDataFrameWriter(outcomes).write();

rule_status_output.getDataFrameWriter(ruleEffects.statusDataset()).write();
}
}
```
***
## Using `@AdditionalInputs` to add Ontology inputs
```java
@AdditionalInputs
public static Set<InputSpec> additionalInputs = ImmutableOntologyInputs.builder()
.addObjectRids("ri.ontology.main.object-type.4168ed49-00...") // employee
// .addLinkRids("...") // add all referenced relations
.ontologyRid("ri.ontology.main.ontology.00000000-0000-0000-0000-000000000000")
.ontologyBranchRid("ri.ontology.main.branch.00000000-0000-0000-0000-000000000000")
.build()
.getInputSpecs();
```
您可以使用 `@AdditionalInputs` 来提供访问 Foundry Rules 中使用的 Object Type 元数据的权限。Foundry Rules Workshop 应用程序中配置使用的任何 Object Type 都必须在此处添加。第一个 Object Type RID 将默认填写，但在 [部署工作流模板](/docs/foundry/foundry-rules/deploy-workflow/) 部分中添加的任何其他对象必须作为额外的 `.addObjectRids()` 条目添加。

You can use `@AdditionalInputs` to provide the permissions to access metadata about the object types used in Foundry Rules. Any object types configured for use in the Foundry Rules Workshop application must be added here. The first object type RID will be filled out by default, but any additional objects added as part of the [deploy workflow template](/docs/foundry/foundry-rules/deploy-workflow/) section must be added as additional `.addObjectRids()` entries.
此外，Workshop 应用程序中使用的任何 *关系* 都必须作为 `.addLinkRids()` 条目添加在此处。RID 可以分别从 Object Type 和 Link Type 页面通过 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 获取。

In addition, any *relations* that will be used in the Workshop application must be added here as a `.addLinkRids()` entry. The RIDs can be obtained from the [Ontology Manager](/docs/foundry/ontology-manager/overview/) using the object type and relation pages, respectively.
在添加这些条目之后，还需要使用 Code Repository **Settings** 选项卡中的 **Ontology Imports** 帮助程序将 Object Type 和 Link Type 导入到项目中。

After adding these entries, it is also necessary to import the object types and relations into the Project using the **Ontology Imports** helper within the **Settings** tab of the Code Repository.
![Ontology imports settings panel with imported object type](/docs/resources/foundry/foundry-rules/ontology_imports.png)
## Input and output datasets
```java
@Compute
public void compute(
@Input("ri.foundry.main.dataset.0000...") FoundryInput source_object_backing_dataset,
@Input("ri.foundry.main.dataset.0000...") FoundryInput rules_input,
@Output("ri.foundry.main.dataset.0000...") FoundryOutput outcome_output,
@Output("REPLACE WITH PATH TO WRITE STATUS DATASET TO") FoundryOutput rule_status_output,
```
本节提供 Foundry 应用程序中规则使用的所有 [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) 的数据。这包括 Foundry 规则中使用的任何对象的后备数据集以及多对多连接表。默认情况下，其中几个将被预填充。

This section provides the data for all the [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) used by the Foundry rules in your application. This includes the backing datasets for any objects and many-to-many join tables used in Foundry rules. By default, several of these will be pre-filled.
但是，在 [部署工作流模板](/docs/foundry/foundry-rules/deploy-workflow/) 时添加的任何其他对象或数据集必须作为新的 `@Input` 条目添加在此处。这些数据集稍后将作为 [TaurusRuleRunner.Args](#foundry-rules-rule-runner) 的一部分被需要。

However, any additional objects or dataset added in while [deploying the workflow template](/docs/foundry/foundry-rules/deploy-workflow/) must be added as new `@Input` entries here. These datasets will be required later as part of [TaurusRuleRunner.Args](#foundry-rules-rule-runner).
此外，您必须为 `rule_status_output` 的输出提供一个路径。该数据集包含任何未成功运行的规则的详细信息，是一个有用的调试工具。

Additionally, you must provide a path for the output of `rule_status_output`. This dataset contains details of any rules that did not run successfully and is a useful debugging tool.
## Foundry Rules rule runner
```java
// Configuring the Foundry Rules rule runner
Args ruleRunnerArgs = new TaurusRuleRunner.Args.Builder()
.rules(new Rules.Builder()
.logicColumnName("RuleLogic")
.ruleIdColumnName("RuleId")
.dataset(rulesDataset)
.build())
// Put all sources used in Foundry Rules editor Workshop app here (for datasets the name here must
// match the dataset name in the Foundry Rules application)
.putSources(SourceReference.objectTypeId("employee"), source)
// .putSources(SourceReference.dataset(DatasetName.of("name in Foundry Rules app")), dataset)
// Required if you use many-many ontology join tables:
// .manyToManyJoinTables(ImmutableMap.of(LinkTypeId.of("relation-id"), dataset))
// set to true to ensure the rule execution output matches the rule editor widget's preview (this flag is false by default)
// .shouldMatchContourExecutionBehavior(true)
.context(transformContext)
.build();
```
本节配置了最终将运行 `rulesDataset` 中提供的 Foundry 规则的 rule runner（`TaurusRuleRunner`）。本节也大部分由默认预先配置，但是，如 [Input and Output Datasets](#input-and-output-datasets) 中所述，任何额外的 [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) 必须通过添加额外的 `.putSources()` 条目在 `TaurusRuleRunner` 中注册。此外，在使用 Foundry 规则配置的对象之间使用的任何多对多连接表必须使用 `.manyToManyJoinTables()` 在此处注册，如上例所示。

This section configures the rule runner (`TaurusRuleRunner`) that will ultimately run the Foundry rules provided in the `rulesDataset`. This section is also mostly pre-configured by default, but, as described in [Input and Output Datasets](#input-and-output-datasets), any extra [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) must be registered with the `TaurusRuleRunner` by adding additional `.putSources()` entries. Additionally, any many-to-many join tables used between objects configured with Foundry rules must be registered here using `.manyToManyJoinTables()` as shown in the example above.
## Rule Action datasets
```java
RuleEffects ruleEffects = TaurusRuleRunner.runRules(ruleRunnerArgs);

Dataset<Row> outcomes = ruleEffects.actionReadyMergedDataset(
ActionTypeRid.valueOf("ri.actions.main.action-type.b6f052c7-f7b1-4b4f-83ee-f81d9e854114"));
outcome_output.getDataFrameWriter(outcomes).write();
```
**Rule Actions** 充当一组 Foundry 规则的公共输出 schema。在使用 `.runRules()` 运行所有规则之后，可以通过使用所需 Action 的 **Action Type RID** 调用 `.actionReadyMergedDataset()` 来获取特定 Rule Action 的所有结果行。此 RID 可在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 的 Action Type 视图中找到。

**Rule Actions** act as a common output schema for a collection of Foundry rules. Having run all rules using `.runRules()`, it is possible to get all result rows for a particular rule Action by calling `.actionReadyMergedDataset()` with the **Action type RID** of the required Action. This RID can be found in the Action type view of the [Ontology Manager](/docs/foundry/ontology-manager/overview/).
![Ontology App with the Action Type Rid of a particular Action Type](/docs/resources/foundry/foundry-rules/action_type_rid.png)
如上例所示，返回的数据集可以写入 transform 的输出。该数据集将包含每个 Action 的 Action 参数对应的一列，以及一个包含该行来源规则 ID 的 `Foundry Rules_rule_id` 列。

The dataset returned can be written to an output of the transform as shown in the above example. This dataset will contain one column per Action parameter of the Action, plus a `Foundry Rules_rule_id` column containing the ID of the rule that the row originated from.
添加到 Workshop 应用程序中的其他 **rule Actions** 可以通过复制示例，然后替换 Action Type RID 并添加一个新的输出数据集来包含在此处，如 [Input and Output Datasets](#input-and-output-datasets) 部分所述。

Additional **rule Actions** added to the Workshop app can be included here by copying the example, then replacing the Action type RID and adding a new output dataset, as described in the [Input and Output Datasets](#input-and-output-datasets) section.
> **ℹ️ 注意**

> 如果在运行 transform 或 CI 检查时遇到任何错误，请查看 [故障排除参考](/docs/foundry/foundry-rules/common-issues/)。
> **ℹ️ 注意**

> If you encounter any errors when running the transform or CI checks, review the [troubleshooting reference](/docs/foundry/foundry-rules/common-issues/).
### Reference implementation
如果由您的 Palantir 代表进行配置，可能会有上述 transform 的可用参考实现。搜索 `Business Rules with Rules Workflow` 文件夹，或导航至 **Foundry Training and Resources** 项目，然后进入 **Reference Examples → Application Development in Workshop → Business Rules with Rules Workflow**。

If configured by your Palantir representative, there may be an available reference implementation of the above transform. Search for the `Business Rules with Rules Workflow` folder or navigate to the **Foundry Training and Resources** Project, then to **Reference Examples → Application Development in Workshop → Business Rules with Rules Workflow**.
在这里，您将找到一个模板 Workflow application 和 transform pipeline，它们是基于示例 aviation Ontology 实现的。

Here, you will find a template Workflow application and transform pipeline implemented on top of the example aviation Ontology.