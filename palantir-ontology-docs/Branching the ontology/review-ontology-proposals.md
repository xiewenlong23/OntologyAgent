<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/review-ontology-proposals/
---
# Review ontology proposals
Ontology 提案类似于版本控制系统中的 Pull Request。提案作为一种机制，用于在来自单独分支的更改被集成到 `main` 之前对其进行审查和批准。

An ontology proposal is analogous to a Pull Request in a version control system. Proposals serve as a mechanism for reviewing and approving changes made in a separate branch before they are integrated into `main`.
对于 global branch，当创建 [Global Branching 提案](/docs/foundry/global-branching/core-concepts/#create-and-prepare-a-proposal) 时会自动创建一个 ontology 提案，其中包含诸如 reviews、name 和合并到 `main` 的更改描述等元数据。对于 legacy ontology branch，ontology 提案在分支创建时创建。

For global branches, an ontology proposal is automatically created when a [Global Branching proposal](/docs/foundry/global-branching/core-concepts/#create-and-prepare-a-proposal) is created and contains metadata such as reviews, name, and descriptions of the changes being merged into `main`. For legacy ontology branches, an ontology proposal is created when the branch is created.
本页介绍如何审查 ontology 提案，包括检查 resource 状态、审查 task 以及查看分支上所做的更改。

This page explains how to review ontology proposals, including checking resource statuses, reviewing tasks, and viewing the changes made on a branch.
## Proposals tab
通过侧边选项卡导航到 **Proposals** 页面，您可以在其中选择查看所有 ontology 提案。提案分为以下选项卡：

Navigate to the **Proposals** page through the side tab, where you can choose to view all ontology proposals. The proposals are grouped into the following tabs:
* **My proposals:** 由您撰写的提案。

* **Assigned to me:** 您被指定为 reviewer 的提案。

* **In review:** 正在进行中或已批准的提案。

* **Merged proposals:** 已合并到 `Main` ontology 的提案。

* **Closed proposals:** 已关闭且未合并的提案。

* **My proposals:** Proposals authored by you.
* **Assigned to me:** Proposals where you have been assigned as a reviewer.
* **In review:** Proposals that are in progress or approved.
* **Merged proposals:** Proposals that have been merged to `Main` ontology.
* **Closed proposals:** Proposals that have been closed out, and were not merged.
![Ontology Manager's My proposals overview page.](/docs/resources/foundry/ontologies/ontology-proposals-page.png)
## Proposal view
访问 **Proposal overview**、**Preview status**、**Review changes** 和 **Changelog** 选项卡以获取有关您个人提案的更多信息。

Access the **Proposal overview**, **Preview status**, **Review changes**, and **Changelog** tabs for more information about your individual proposal.
### Proposal overview page
要在 Global Branch 上访问单个提案，请从分支任务栏中选择任何 ontology resource，然后选择 **View ontology proposal**。如果您在 `Main` 上，请导航到 **Proposals** 选项卡并选择您希望查看的提案。如果您在一个 ontology branch 上，请从导航顶部栏中选择 **Open proposal details** 以直接访问该提案。

To access an individual proposal while on a Global Branch, choose any ontology resource from the branch taskbar and select **View ontology proposal**. If you are on `Main`, navigate to the **Proposals** tab and select the proposal you wish to view. If you are on an ontology branch, select **Open proposal details** from the navigation top bar to access the proposal directly.
在提案中，您将看到 **Proposal overview**、**Preview status**、**Review changes** 和 **Changelog** 选项卡以获取更多信息。

Within a proposal, you will see the **Proposal overview**, **Preview status**, **Review changes**, and **Changelog** tabs for more information.
提案概览页面集中显示了您提案的 stage、更改、需要审查的 task 以及选定的 reviewer。

The proposal overview page centralizes your proposal's stage, changes, tasks requiring review, and selected reviewers.
* **View changes on your branch:** 编辑显示在概览页面的底部。编辑按作者和 task 进行分类，其中 task 对应于一个 ontology resource。您可以查看更改、导航到该 resource，或从分支中移除这些更改。更改历史也可以通过 **Changelog** 选项卡访问，其中还显示了更改的确切时间。

* **View and add reviewers:** 分配特定的同事来审查您的提案。

* **View tasks that require attention:** 此部分将显示 Review stage 中所有被拒绝的 task。

* 使用 **Share** 选项复制提案链接。

* **View changes on your branch:** Edits are displayed at the bottom of the overview page. Edits are categorized by author and by task, where a task corresponds to an ontology resource. You may view the change, navigate to the resource, or remove the changes from the branch. The history of changes is also accessible through the **Changelog** tab, where the exact timings of changes are also displayed.
* **View and add reviewers:** Assign specific colleagues to review your proposal.
* **View tasks that require attention:** This section will display all rejected tasks in the Review stage.
* Copy the proposal link by using the **Share** option.
![Proposal overview for a specific Global Branch.](/docs/resources/foundry/ontologies/ontology-proposal-overview.png)
### Preview status
**Preview status** 选项卡显示哪些 object type 已被索引、正在索引中或无法在您的分支上进行索引。一旦 object type 被索引，它将准备好进行预览，这意味着其数据在您的分支上可进行查看和测试。

The **Preview status** tab shows which object types have been indexed, are in progress, or cannot be indexed on your branch. Once an object type is indexed, it will be ready for preview, meaning its data is available on your branch for viewing and testing.
![Preview status tab.](/docs/resources/foundry/ontologies/ontology-proposal-preview-status-tab.png)
### Review changes
**Review changes** 选项卡显示提案中的所有 task。从这里，您可以执行以下操作：

The **Review changes** tab shows all tasks in the proposal. From here, you can perform the following actions:
* 邀请其他 reviewer

* 查看已迁移到项目的 resource 的 approval policies

* 单独或批量批准或拒绝所有符合条件的 task

* 在 task 级别留下评论，并与您的同事协作

* Invite additional reviewers
* View the approval policies of resources that have migrated to projects
* Approve or reject each task individually or in bulk for all eligible tasks
* Leave comments at the level of a task, and collaborate with your colleagues
![Review changes page.](/docs/resources/foundry/ontologies/ontology-proposal-review-changes.png)
### Changelog
Changelog 选项卡显示分支上更改的详细历史。可以展开 task 以揭示特定用户在特定时间点所做的编辑。您还可以直接导航到相关的 ontology resource。

The Changelog tab shows a detailed history of changes on a branch. Tasks can be expanded to reveal edits made by a certain user at a given point in time. You may also directly navigate to the relevant ontology resource.
![Changelog tab.](/docs/resources/foundry/ontologies/ontology-proposal-changelog-tab.png)
## Proposal permissions
* **Viewing a proposal:** 提案的 title 和 description 可被所有有权访问该 ontology 的人发现。任何对提案中某些 resource 至少具有 `Viewer` 权限的用户都可以查看与这些 resource 相关的更改。

* **Modifying Ontology resources:** 对 resource 具有编辑权限的用户可以在分支上对其进行编辑。对于使用 [ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/)（而不是 [project permissions](/docs/foundry/object-permissioning/ontology-permissions/)）的 resource，viewer 可以在分支上建议更改。

* **Accepting or rejecting tasks in a proposal:** 要批准一个 task，审批者默认必须是底层 resource 的 editor 或 owner。如果该 resource 已迁移到项目并受到保护，则审批者必须根据项目 policies 拥有审批权限。

* **Merging an Ontology proposal:** Ontology 提案通过合并 Global Branching 提案来合并。但是，对于 legacy ontology branch，只要获得所有必需的批准，任何可以查看该分支的用户都可以合并该提案。

* **Viewing a proposal:** A proposal's title and description are discoverable by everyone who has access to the ontology. Any user with at least `Viewer` access to some resources in the proposal can see the changes related to those resources.
* **Modifying Ontology resources:** Users with edit permissions on a resource can edit it on a branch. For resources using [ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/) (rather than [project permissions](/docs/foundry/object-permissioning/ontology-permissions/)), viewers can suggest changes on a branch.
* **Accepting or rejecting tasks in a proposal:** For a task to be approved, the approver must be either an editor or owner of the underlying resource by default. If the resource has been migrated to a project and is protected, the approver must have approval rights based on the project policies instead.
* **Merging an Ontology proposal:** Ontology proposals are merged through merging a Global Branching proposal. However, for legacy ontology branches, anyone who can view the branch can merge the proposal as long as all the required approvals are obtained.