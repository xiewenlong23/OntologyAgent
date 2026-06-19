<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/rule-permissions/
---
# Permissions for editing rules
在某些 workflows 中，您可能希望限制可以编辑或修改 rule 的 users 集合。以下示例展示了如何设置 permissions，以使 rule 的 author 对影响其 rule 的任何更改拥有最终审批权。

In some workflows, you may want to restrict the set of users that can edit or modify a rule. The following example shows how you can set up permissions so that a rule's author has final approval for any changes affecting their rule.
Permissioning 设置如下：

The permissioning setup is as follows:
* 只有规则作者（以及超级用户）才能批准编辑其规则的提案。
* 只有规则作者（以及超级用户）才能批准删除其规则的提案。
* 只有规则作者和提案创建者（以及超级用户）才能拒绝规则所有者的规则上的提案。
* 为了减轻意外提案的问题，提案创建者也可以拒绝提案。例如，如果用户 A 意外地在用户 B 的规则上创建了提案，用户 A 能够拒绝（即撤销）该提案。

* Only rule authors (and superusers) can approve proposals that edit their rules.
* Only rule authors (and superusers) can approve proposals that delete their rules.
* Only rule authors and proposal creators (and superusers) can reject proposals on the rule owner's rules.
* To mitigate the issue of accidental proposals, proposal creators can also reject proposals. For example, if User A accidentally creates a proposal on User B's rule, User A is able to reject (effectively rescinding) that proposal.
按照以下步骤操作以实现此权限设置：

Follow the steps below to achieve this permissioning setup:
1. 配置 *approve a proposal to edit a rule* Action，使用户必须是与该提案关联的规则作者或超级用户。

![Action validation where you must first be in a users or superusers group AND either the rule author or a superuser](/docs/resources/foundry/foundry-rules/proposal_edit_validation.png)

1. Configure the *approve a proposal to edit a rule* Action so that users must either be the rule author associated with the proposal or a superuser.

![Action validation where you must first be in a users or superusers group AND either the rule author or a superuser](/docs/resources/foundry/foundry-rules/proposal_edit_validation.png)

2. 配置 *approve a proposal to delete a rule* Action，使用户必须是与该提案关联的规则作者或超级用户。

2. Configure the *approve a proposal to delete a rule* Action so that users must either be the rule author associated with the proposal or a superuser.
3. 配置 *reject a proposal* Action，使用户必须是与该提案关联的规则作者、提案作者或超级用户。

![Action validation where you must be either the rule author, the proposal author, or a superuser](/docs/resources/foundry/foundry-rules/proposal_reject_validation.png)

3. Configure the *reject a proposal* Action so that users must either be the rule author associated with the proposal, the proposal author, or a superuser.

![Action validation where you must be either the rule author, the proposal author, or a superuser](/docs/resources/foundry/foundry-rules/proposal_reject_validation.png)

> **ℹ️ 注意**

> 如果您没有看到基于规则对象进行验证的选项，则很可能是您没有将规则对象作为参数添加到该 Action。请向 *reject a proposal* Action 添加一个新的规则对象参数，就像为其他 Foundry Rules 操作的规则对象参数添加方式一样。
> **ℹ️ 注意**

> If you do not see an option to validate based on a rule object, you likely do not have the rule object added as a parameter to the Action. Add a new rule object parameter to the *reject a proposal* Action, just as you would add rule object parameters of other Foundry Rules actions.