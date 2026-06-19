<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/author-and-run-a-rule/
---
# Author and run a rule
以下步骤将指导您完成在 Workshop application 中编写和运行规则的整个过程。

The following steps will guide you through the process of authoring and running a rule in a Workshop application.
1. **找到 Workshop Rule 应用：** 在 workflow 配置页面中，选择文件夹并选择 Workshop 应用。

![Screenshot of path shown in the workshop configuration page](/docs/resources/foundry/foundry-rules/fr-workflow-path.png)

![Screenshot of Workshop application](/docs/resources/foundry/foundry-rules/fr-manual-open.png)

1. **Find the Workshop Rule application:** From the workflow configuration screen, select the folder and choose the Workshop application.

![Screenshot of path shown in the workshop configuration page](/docs/resources/foundry/foundry-rules/fr-workflow-path.png)

![Screenshot of Workshop application](/docs/resources/foundry/foundry-rules/fr-manual-open.png)

2. **编写规则：** 在上一步创建的 Workshop 应用中，点击 **Create New** 按钮以开始创建规则。
* (a) 在规则顶部的表单中填写名称、描述以及其他信息。

* (b) 编写希望规则执行的逻辑。例如，这可以是一个简单的 filter。

* (c) 点击 **Submit changes** 以为此新规则创建一个 proposal。

![Authoring a Foundry rule](/docs/resources/foundry/foundry-rules/author_a_foundry_rule.png)

2. **Author a rule:** Within the Workshop application created in the previous step, click the **Create New** button to begin creating a rule.
* (a) Fill out the form at the top of the rule with a name, description, and other information.
* (b) Author logic that you want the rule to execute. For example, this could be a simple filter.
* (c) Click **Submit changes** to create a proposal for this new rule.

![Authoring a Foundry rule](/docs/resources/foundry/foundry-rules/author_a_foundry_rule.png)

3. **批准 proposal：** 在 Workshop 应用的 **Proposals** 标签页中，在左侧选择新创建的 proposal。

* 选择 **Approve** 以将其激活为规则。

![Approving a Foundry rule proposal](/docs/resources/foundry/foundry-rules/approve_rule_proposal.png)

3. **Approve the proposal:** Within the **Proposals** tab of the Workshop application, select the newly created proposal on the left side.
* Select **Approve** to activate it as a rule.

![Approving a Foundry rule proposal](/docs/resources/foundry/foundry-rules/approve_rule_proposal.png)

4. **构建规则回写和规则输出 dataset：** 导航到在 [configuring the workflow](/docs/foundry/foundry-rules/configure-workflow/) 时创建的输出 dataset。

* 选择 **Actions**，然后选择 **Explore data lineage** 以查看输入 dataset。

![Navigate to Data Lineage for output dataset](/docs/resources/foundry/foundry-rules/navigate_to_data_lineage.png)

4. **Build the rule writeback and rules output datasets:** Navigate to the output dataset that was created while [configuring the workflow](/docs/foundry/foundry-rules/configure-workflow/).
* Choose **Actions**, then **Explore data lineage** to view the input datasets.

![Navigate to Data Lineage for output dataset](/docs/resources/foundry/foundry-rules/navigate_to_data_lineage.png)

* 同时选择 rules writeback dataset（d）和输出 dataset（e）。

* Select both the rules writeback dataset (d) and the output dataset (e).
* 在选中两个 dataset 的情况下右键单击，然后选择 **Build**。

![Build the rules writeback and Foundry rules output datasets](/docs/resources/foundry/foundry-rules/run_rules.png)

* Right-click with both datasets selected and choose **Build**.

![Build the rules writeback and Foundry rules output datasets](/docs/resources/foundry/foundry-rules/run_rules.png)

* 构建完成后，输出 dataset 将包含新规则的结果。未来，可以将这两个 dataset 放在 [schedule](/docs/foundry/data-lineage/manage-schedules/) 上以保持输出的最新状态。

* Once the build has completed, the output dataset will contain the results of your new rule. In the future, these two datasets can be placed on a [schedule](/docs/foundry/data-lineage/manage-schedules/) to keep the outputs up to date.