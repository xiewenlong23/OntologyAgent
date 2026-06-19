<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/workshop-application/
---
# Workshop application
一个标准的 Foundry Rules application 是一个 Workshop application，通常包含两个页面：Rule Editor 页面和 Proposal Reviewer 页面。

A standard Foundry Rules application is a Workshop application that usually comprises two pages: the Rule Editor page and the Proposal Reviewer page.
* **[Rule Editor](#rule-editor)** 页面用于创建、编辑和删除规则。

* **[Proposal Reviewer](#proposal-reviewer)** 页面用于审核和批准/拒绝 rule proposals。

* The **[Rule Editor](#rule-editor)** page is used for creating, editing, and deleting rules.
* The **[Proposal Reviewer](#proposal-reviewer)** page is used for reviewing and approving/rejecting rule proposals.
还提供了一个额外的 **Rule Viewer** widget，用于创建只读的 rule logic 查看器。

An additional **Rule Viewer** widget is available for creating a read-only rule logic viewer.
## Rule Editor
Rule Editor 页面的目的是允许创建和维护规则。下面的截图显示了一个示例 Rule Editor 页面，由以下 widget 组成（编号用于标识）：

The purpose of the Rule Editor page is to allow for the creation and maintenance of rules. The following screenshot shows an example Rule Editor page consisting of the following widgets (numbered for identification):
1. **Filter list:** 用于筛选显示规则的一组过滤器。

2. **Object list:** 现有规则的列表，由 filter list (1) 筛选，可选择以填充 Rule Editor (3)。

3. **Rule Editor:** 一个接受 Foundry Action 以创建 proposal 并根据 parameters 自动生成所需字段的 widget。Rule Editor 中显示的表单元素由 Ontology 中配置的用于创建新规则的 Action 决定。

![Rules editor Workshop module page with the three panes described above](/docs/resources/foundry/foundry-rules/rules_editor_annotated.png)

1. **Filter list:** A selection of filters to filter the rules shown.
2. **Object list:** A list of existing rules that are filtered by the filter list (1) and can be selected to populate the Rule Editor (3).
3. **Rule Editor:** A widget that accepts a Foundry Action to create a proposal and auto-generates the required fields from parameters. The form elements displayed in the Rule Editor are determined by the Action configured in the Ontology for creating a new rule.

![Rules editor Workshop module page with the three panes described above](/docs/resources/foundry/foundry-rules/rules_editor_annotated.png)

在创建或编辑一条 *rule* 之后，使用 **Submit changes** 按钮来创建一个新的 *proposal*。该 proposal 可以在 Proposal Reviewer 页面进行查看和审核。

After creating or editing a *rule*, the **Submit changes** button is used to create a new *proposal*. This proposal can be viewed and reviewed on the Proposal Reviewer page.
## Proposal Reviewer
Proposal Reviewer 页面允许对 rule proposals 进行审核以及批准/拒绝操作。与 Rule Editor 类似，它包含三个部分（在下方截图中以数字标识）：

The Proposal Reviewer page allows for the review and approval/rejection of rule proposals. Like the Rule Editor, it contains three sections (identified by number in the screenshot below):
1. **Filter list:** 用于更改显示哪些 proposals 的一组过滤器 (1)。

2. **Object list:** proposals 的列表 (2)，由 filter list 筛选，可选择以填充 Proposal Reviewer (3)。

3. **Proposal Reviewer:** 一个接受 Foundry Actions 以批准或拒绝 proposals 的 widget。该 widget 显示已编辑 properties 的 diff，更改后的值以黄色显示，先前的值以淡灰色显示。当用户批准一个 proposal 时，所做的编辑将被应用，并且该 proposal 将根据其类型被创建、编辑或删除。

![Proposal reviewer Workshop module page with the three panes described above](/docs/resources/foundry/foundry-rules/proposal_reviewer_annotated.png)

1. **Filter list:** A selection of filters that change which proposals are shown (1).
2. **Object list:** A list of proposals (2) that are filtered by the filter list and can be selected to populate the Proposal Reviewer (3).
3. **Proposal Reviewer:** A widget that accepts Foundry Actions to approve or reject proposals. The widget shows a diff of the properties that have been edited, with changed values appearing in yellow and prior values in faded grey. When a user approves a proposal, the edits will be applied and the proposal will be either created, edited, or deleted (depending on the proposal).

![Proposal reviewer Workshop module page with the three panes described above](/docs/resources/foundry/foundry-rules/proposal_reviewer_annotated.png)

