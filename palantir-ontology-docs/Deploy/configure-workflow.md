<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/configure-workflow/
---
# Configure workflow
完成 [deploying the workflow template](/docs/foundry/foundry-rules/deploy-workflow/) 后，以下步骤将指导您完成 [configuring your workflow](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/) 的过程。

Once you finish [deploying the workflow template](/docs/foundry/foundry-rules/deploy-workflow/), the following steps will guide you through the process of [configuring your workflow](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/).
1. **访问现有规则：** 在 Foundry Rules 主页中，通过选择相应项从现有规则列表中进行选择。或者，您也可以通过 **Files** 中找到的相应项目导航并选择它。

![List of existing rules in Foundry Rules](/docs/resources/foundry/foundry-rules/overview@2x.png)

1. **Access existing rule:** From the Foundry Rules home page, choose from a list of existing rules by selecting the item. Alternatively, you may also navigate and select it from its respective project found in **Files**.

![List of existing rules in Foundry Rules](/docs/resources/foundry/foundry-rules/overview@2x.png)

2. **添加 workflow 输入：** 在规则视图中，选择 **Add Input** 按钮以向 workflow 添加 object 或 dataset 输入。这将可用作下一节中编写的规则的输入。

* 您可以根据需要添加任意数量的输入，但所有 workflow 必须至少包含一个输入。

* 添加 object type 输入时，link types 部分将出现在每个 object type 下方。任何被选中的 link 都将在 [Rules Management application](/docs/foundry/foundry-rules/workshop-application/) 中可用，用于将不同的 object 连接在一起。

![Button to add a new Workflow Input](/docs/resources/foundry/foundry-rules/add_workflow_input.png)

2. **Add workflow inputs:** With the rule in view, select the **Add Input** button to add an object or dataset input to the workflow. This will become usable as an input to the rule authored in the next section.
* You can add as many inputs here as you wish, but all workflows must contain at least one input.
* When adding object type inputs, the link types section will appear below each object type. Any links selected will become usable in the [Rules Management application](/docs/foundry/foundry-rules/workshop-application/) for joining together different objects.

![Button to add a new Workflow Input](/docs/resources/foundry/foundry-rules/add_workflow_input.png)

> **ℹ️ 注意**

> 由 restricted view 支持的 object 不能直接用作输入。请将支持 restricted view 的 dataset 配置为 [alternate backing dataset](/docs/foundry/foundry-rules/configure-workflow/#alternate-backing-datasets)。
> **ℹ️ 注意**

> Objects backed by a restricted view cannot be used as inputs directly. Instead, configure the dataset which backs the restricted view as an [alternate backing dataset](/docs/foundry/foundry-rules/configure-workflow/#alternate-backing-datasets).
3. **添加 workflow 输出：** 在编辑器的第三部分中，点击 **Add Dataset Output** 并为存储规则结果的 dataset 提供名称和位置。

![Button to add a new Workflow Output](/docs/resources/foundry/foundry-rules/add_workflow_output.png)

3. **Add workflow outputs:** In the third section of the editor, click **Add Dataset Output** and provide a name and location for the dataset where the rule results will be output.

![Button to add a new Workflow Output](/docs/resources/foundry/foundry-rules/add_workflow_output.png)

* 为输出提供一个名称，该名称将显示给 **Rules Management application** 中的规则作者（a）。

* 点击 **Add column** 以为输出添加至少一列（b）。为此列提供一个在 dataset 中使用的名称，以及一个在 rules application 中向规则作者显示的 display name。您可以配置 column 的类型，并确定在编写规则时是否需要提供该列。详细了解 [permitted and default output values](/docs/foundry/foundry-rules/permitted-and-default-output-values/)。

* 为希望从规则结果中捕获的每一条信息添加一列。例如，alerting workflow 可能包含 `Alert ID`、`Severity` 和 `Assignee` 列，以及一列用于捕获触发 alert 的 object 的标识符（例如 `Machine ID`）。

![Configuring the Workflow Output](/docs/resources/foundry/foundry-rules/workflow_output_configuration.png)

* Provide a name for the output that will be displayed to rule authors in the **Rules Management application** (a).
* Click **Add column** to add at least one column to the output (b). Give this column a name to be used in the dataset and a display name to show to rule authors in the rules application. You can configure the type of column and determine whether it is required to provide this column when authoring a rule. Learn more about [permitted and default output values](/docs/foundry/foundry-rules/permitted-and-default-output-values/).
* Add a column for each piece of information you wish to capture from the results of your rule. For example, an alerting workflow may have columns for `Alert ID`, `Severity`, and `Assignee` as well as a column to capture an identifier for the object that triggered the alert (e.g. `Machine ID`).

![Configuring the Workflow Output](/docs/resources/foundry/foundry-rules/workflow_output_configuration.png)

4. **保存 workflow：** 在配置编辑器的右上角，点击 save 按钮。

* 保存 workflow 后，您应该会在编辑器顶部看到一个绿色横幅出现，表示 [transforms pipeline](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/#rule-execution) 已成功创建。

![Banner showing that the transforms pipeline has been created successfully](/docs/resources/foundry/foundry-rules/transforms-pipeline-success-banner.png)

4. **Save the workflow:** In the top right of the configuration editor, click the save button.
* After saving the workflow, you should see a green banner appear at the top of the editor, signifying that the [transforms pipeline](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/#rule-execution) has been created successfully.

![Banner showing that the transforms pipeline has been created successfully](/docs/resources/foundry/foundry-rules/transforms-pipeline-success-banner.png)

完成上述步骤后，请了解如何 [author and run a rule](/docs/foundry/foundry-rules/author-and-run-a-rule/)。

After completing the above steps, learn how to [author and run a rule](/docs/foundry/foundry-rules/author-and-run-a-rule/).
## Advanced configurations
### Alternate backing datasets
您可以使用备用 backing dataset 来配置 object input。这意味着您的规则将根据提供的备用 backing dataset 进行评估，而不是 Ontology 中配置的 writeback（或 backing）dataset。

You can configure an object input with an alternate backing dataset. This means your rules are evaluated against the supplied alternate backing dataset instead of the writeback (or backing) dataset configured in the Ontology.
以下情况特别适用：

This is useful when:
* 在 restricted view-backed objects 上编写规则

* 在 Object 的 backing data 的子集上运行规则

> 📷 **[图片: 配置备用 backing dataset]**

* Writing rules on restricted view-backed objects
* Running rules on a subset of the Object's backing data

> 📷 **[图片: Configuring an alternate backing dataset]**

