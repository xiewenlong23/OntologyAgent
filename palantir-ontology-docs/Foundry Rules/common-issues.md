<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/common-issues/
---
# Troubleshooting reference
此页面描述了 Foundry Rules 的一些常见问题及其调试步骤。

This page describes several common issues with Foundry Rules and steps to debug.
## Error messages
### `ReadonlyObjectError`
确保您创建的每个 object 都关联了 writeback dataset。请查看 [authoring and running a rule](/docs/foundry/foundry-rules/author-and-run-a-rule/) 中的 build writeback datasets 步骤以获取更多信息。

Make sure that each object you created has a writeback dataset associated. Review the build writeback datasets step of [authoring and running a rule](/docs/foundry/foundry-rules/author-and-run-a-rule/) for more information.
### 400: `Actions:InvalidParametersForApply`
Action 请求中未提供某些必需参数。请验证 Actions 是否配置正确。

Some required parameters were not provided in the Action request. Verify that the Actions are configured properly.
## Proposal diff not displayed correctly for custom property
要使 proposal widget 正确显示 diffs，请按照以下步骤操作：

To get the proposal widget to display diffs correctly, follow these steps:
1. 在 Workshop app 中，将 `new_<PROPERTY>` property 添加到 Proposal Reviewer widget 配置中的 **Properties grouped by section**。这里无需选择 "current" 值。

1. In the Workshop app, add the `new_<PROPERTY>` property to the **Properties grouped by section** in the Proposal Reviewer widget configuration. It is not necessary to select the "current" value here.
2. 如果需要，可以编辑 property 名称以删除 "new" 前缀。

2. If desired, edit the property name to remove the ”new“ prefix.

> 📷 **[图片: Alert Recipient property added to the proposal reviewer configuration sidebar with the 'New' prefix highlighted to indicate it can be removed]**

> 📷 **[图片: Alert Recipient property added to the proposal reviewer configuration sidebar with the 'New' prefix highlighted to indicate it can be removed]**

3. 将 `foundry-rules.property-diff-for:ID_OF_NEW_PROPERTY` type class 添加到 **proposal object** 的 **current** property。请注意，type classes 由 *kind* 和 *name* 组成，写作 `kind.name`。对于 `foundry-rules.property-diff-for:new_<PROPERTY>`，kind 是 `foundry-rules`，name 是 `property-diff-for:new_<PROPERTY>`。

3. Add the `foundry-rules.property-diff-for:ID_OF_NEW_PROPERTY` type class to the **current** property of the **proposal object**. Note that type classes are characterized by a *kind* and a *name*, written out as `kind.name`. In the case of `foundry-rules.property-diff-for:new_<PROPERTY>`, the kind is `foundry-rules` and the name is `property-diff-for:new_<PROPERTY>`.

> 📷 **[图片: Example type class name and kind added to a property in ontology app]**

> 📷 **[图片: Example type class name and kind added to a property in ontology app]**

## Older errors
在 2022 年 7 月之前，Foundry Rules（之前称为 Taurus）需要额外的配置，并使用略有不同的概念。以下错误与该流程相关。如果您在 2022 年 7 月之后部署了 Foundry Rules 并遇到以下问题之一，请尝试导航到 [Workflow Configuration Editor](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/) 以查看工作流中是否存在任何错误。

Prior to July 2022, Foundry Rules (previously known as Taurus) required additional configuration and used slightly different concepts. The following errors are associated with that process. If you deployed Foundry Rules after July 2022 and you encounter one of the issues below, try navigating to the [Workflow Configuration Editor](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/) to see if there are any errors in the workflow.
### `Taurus:MissingOntologyInformation`
此错误表明，错误信息中标识的所请求的 Ontology 信息不存在，或者 transform 没有访问该信息的权限。请检查以下步骤以修复该错误：

This error indicates that the requested Ontology information, as identified in the error message, either does not exist or the transform does not have permissions to access it. Check the following steps to remediate the error:
1. 验证消息中的 RID 或 ID 是否存在于 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中。

2. 验证 Foundry Rules Workshop 应用程序中使用的所有 Object Type *和* Relation 是否已通过 Code Repository **Settings** 选项卡中的 **Ontology Imports** 助手导入到 Project 中。

3. 验证 Foundry Rules Workshop 应用程序中使用的所有 Object Type *和* Relation 的 RID 是否列在 transform 代码顶部的 `@AdditionalInputs` 部分中。了解更多关于[使用 `@AdditionalInputs`](/docs/foundry/foundry-rules/configure-transforms-pipeline/#using-additionalinputs-to-add-ontology-inputs) 的信息。

4. 确保 Foundry Rules Workshop 应用程序中使用的 Object Type 和多对多 Relation 的所有 backing datasets 已通过 Project 视图中的 **Project References** 部分[导入](/docs/foundry/compass/move-and-share-resources/) 到 Project 中。这包括由 Restricted Views 支持的任何 objects 或 relations。

1. Verify that the RID or ID in the message exists in the [Ontology Manager](/docs/foundry/ontology-manager/overview/).
2. Verify that all object types *and* relations used in the Foundry Rules Workshop application are imported into the Project using the **Ontology Imports** helper within the **Settings** tab of the Code Repository.
3. Verify that the RIDs of all object types *and* relations used in the Foundry Rules Workshop application are listed in the `@AdditionalInputs` section at the top of the transform code. Learn more about [using `@AdditionalInputs`](/docs/foundry/foundry-rules/configure-transforms-pipeline/#using-additionalinputs-to-add-ontology-inputs).
4. Make sure all the backing datasets for the object types and many-to-many relations used in the Foundry Rules Workshop application are [imported](/docs/foundry/compass/move-and-share-resources/) into the Project using the **Project References** section of the Project view. This includes any objects or relations backed by Restricted Views.
### `TransformsGradlePlugin:StaticTaurusDependencyDisallowed`
此错误表明，不再允许对 `tau-execution-core` 声明静态版本号依赖关系。要修复此错误，请将声明的版本更改为版本范围 `[0,1[`，而不是静态版本号：

This error indicates that declaring a static version number dependency on `tau-execution-core` is no longer allowed. To remediate this error, change the declared version to be the version range `[0,1[` instead of the static version number:
1. 首先，导航到包含 Foundry Rules transform 的 [**Code Repository**](/docs/foundry/code-repositories/overview/)。

2. 开启 **Show hidden files and folders**。

3. 在 Project 级别的 `build.gradle` 文件中，将以下行

`compile "com.palantir.tau-execution:tau-execution-core:0.x.x"`
更改为 `compile "com.palantir.tau-execution:tau-execution-core:[0,1["`。

* 如果存在另一行 `compile "com.palantir.tau-grammar:tau-grammar-api-objects:0.x.x"`，则*删除此行*。

4. 提交结果后，checks 应通过。

1. First, navigate to the [**Code Repository**](/docs/foundry/code-repositories/overview/) that contains the Foundry Rules transform.
2. Turn on **Show hidden files and folders**.
3. Within the Project level `build.gradle` file, change the line
`compile "com.palantir.tau-execution:tau-execution-core:0.x.x"`
to `compile "com.palantir.tau-execution:tau-execution-core:[0,1["`.
* If there is another line, `compile "com.palantir.tau-grammar:tau-grammar-api-objects:0.x.x"`, then *delete this line*.
4. Commit the result and the checks should pass.
### The Rule Editor preview does not match the output from the Foundry Rules transform
1. 验证 Foundry Rules transform 的输入 datasets 是否与 Rule Editor 预览中用于支持 objects 的 datasets 相对应。

2. 验证 Foundry Rules transform 中是否将标志 `.shouldMatchContourExecutionBehavior(true)` 设置为 `true`（如下例所示）。此标志确保 Foundry Rules transform 执行的逻辑与 Rule Editor 预览中的执行相同。

1. Verify that the input datasets of the Foundry Rules transform correspond to the ones used to back your objects in the Rule Editor preview.
2. Verify that the flag `.shouldMatchContourExecutionBehavior(true)` is set to `true` in the Foundry Rules transform (example below). This flag ensures that the execution of the logic performed by the Foundry Rules transform is the same as in the Rule Editor preview.
```java
// Configuring the Foundry Rules Rule Runner
Args ruleRunnerArgs = new TaurusRuleRunner.Args.Builder()
.rules(new Rules.Builder()
.logicColumnName("RuleLogic")
.ruleIdColumnName("RuleId")
.dataset(rulesDataset)
.build())
.putSources(SourceReference.objectTypeId("employee"), source)
// set to true to ensure the rule execution output matches the rule editor widget's preview
.shouldMatchContourExecutionBehavior(true)
.context(transformContext)
.build();
```
### `Taurus:UnknownMeasureName`
当 sensor object 缺失或 transform 没有正确的权限时，可能会发生此错误。请检查以下内容以修复该错误：

This error can occur when a sensor object is either missing or the transform does not have the correct permissions. Check the following to remediate the error:
* 检查 root object 与 sensor object 之间 link 的 RID 是否已通过 Code Repository **Settings** 选项卡中的 Ontology Imports 助手导入到 Project 中。

* 检查 root 与 sensor object 之间 link 的 RID 是否列在 transform 代码顶部的 `@AdditionalInputs` 部分中。

* 检查 sensor object 的 backing dataset 是否列在 transform 代码顶部的 `@AdditionalInputs` 部分中。

* 检查 sensor object 的 backing dataset 是否已通过 Project 视图中的 **Project References** 部分[导入](/docs/foundry/compass/move-and-share-resources/) 到 Project 中。

* Check that the RID of the link between the root object and the sensor object is imported into the Project using the Ontology Imports helper within the **Settings** tab of the Code Repository.
* Check that the RID of the link between the root and sensor object is listed in the `@AdditionalInputs` section at the top of the transform code.
* Check that the backing dataset of the sensor object is listed in the `@AdditionalInputs` section at the top of the transform code.
* Check that the backing dataset of the sensor object is [imported](/docs/foundry/compass/move-and-share-resources/) into the Project using the **Project References** section of the Project view.
验证您是否已遵循[部署指南](/docs/foundry/foundry-rules/configure-transforms-pipeline/)中的所有步骤。

Verify that you have followed all the steps in [the deployment guide](/docs/foundry/foundry-rules/configure-transforms-pipeline/).