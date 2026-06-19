<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/object-model/
---
# Object model
有两个与 Foundry Rules 相关的主要 Object Model 概念:

There are two primary object model concepts that are relevant to Foundry Rules:
* [Rules](#rules),即应用于数据的规则,以及

* [Proposals](#proposals),即提供更改规则方式的提案。

* [Rules](#rules), which are applied to data, and
* [Proposals](#proposals), which provide a means by which rules can be changed.
### Rules
Rules 是由以下部分组成的标准对象:

Rules are standard objects consisting of:
* 一组 *rule metadata properties*,例如 name、description、author、rule type 等。

* 一组 *custom properties*,将应用于过滤后的数据集或传递给 transform。

* 对于 "alerting" 模式,这些可能是 `alert_severity`、`alert_assignee` 或 `priority`。

* 对于 "categorization" 模式,这些可能是 `group`、`sub-group` 等。

* 一个包含该规则匹配条件的 *logic property*。

* logic 以压缩的 JSON blob 形式存储,符合特定语法以实现一致的序列化。

* A collection of *rule metadata properties* such as name, description, author, rule type, etc.
* A collection of *custom properties* to be applied to the filtered dataset or passed to the transform.
* For “alerting” patterns, these might be `alert_severity`, `alert_assignee`, or `priority`.
* For “categorization” patterns, these might be `group`, `sub-group`, etc.
* A *logic property* containing the match conditions for that rule.
* The logic is stored as a compressed JSON blob that conforms to a specific grammar for consistent serialization.
![A set of metadata input fields like rule name, workflow-specific input fields like level of suspicion, and logic displaying a simple filter on an object property.](/docs/resources/foundry/foundry-rules/example_rule.png)
了解如何为你的工作流 [customize properties](/docs/foundry/foundry-rules/add-a-custom-property/)。

Learn how to [customize properties](/docs/foundry/foundry-rules/add-a-custom-property/) for your own workflow.
### Proposals
许多 rule management 用例对管理规则创建、编辑和删除的审计和审查流程都有相应的要求。为了满足这些需求,Foundry Rules 支持 **rule proposals**,作为提交、审查和监控规则更改的一种方法。Rule proposals 类似于软件开发中的 ["pull requests" ↗](https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests) 概念,因此每个 rule 在给定时间可以有多个 proposal。

Many rule management use cases have corresponding requirements for an audit and review process governing the creation, editing, and deletion of rules. To service these needs, Foundry Rules supports **rule proposals** as a method of submitting, reviewing, and monitoring changes to rules. Rule proposals are analogous to the software development concept of ["pull requests" ↗](https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests), such that each rule can have multiple proposals at a given time.
> **ℹ️ 注意**

> Proposals 是 Foundry Rules 的一项功能,并非必需。由于 Foundry Rules 使用标准对象和 Action 来创建此审批流程,因此可以根据需要自定义工作流,以匹配任何运营或监管对规则变更管理的要求。
> **ℹ️ 注意**

> Proposals are a feature and not a requirement of Foundry Rules. Since Foundry Rules employs standard objects and Actions to create this approval flow, the workflow can be customized as desired to match any operational or regulatory requirements for rule change management.
Proposals 表示为包含以下内容的对象:

Proposals are represented as objects containing:
* 要编辑、创建或删除的 *rule ID*。

* *Proposal metadata*,例如 proposal author、timestamp、status(open、approved、rejected)和 reviewer。

* Proposal 中 *diff of the changes*(即更改列表),存储在以下属性中:`old_rule_name`、`new_rule_name`、`old_logic`、`new_logic` 等。

* The *rule ID* to be edited, created, or deleted.
* *Proposal metadata* such as the proposal author, timestamp, status (open, approved, rejected), and reviewer.
* The *diff of the changes* in the proposal (i.e. list of the changes), captured in properties: `old_rule_name`, `new_rule_name`, `old_logic`, `new_logic`, etc.
![A diff showing the changes to metadata fields as well as rule logic](/docs/resources/foundry/foundry-rules/example_proposal.png)