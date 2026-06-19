<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/ontology-branches-legacy/
---
# Ontology proposals \[Legacy]
> **⚠️ 警告**

> Ontology branches（原称为 ontology proposals）即将停用。在已启用 Global Branching 的 enrollment 上，你无法再创建 ontology branches。请改用 [global branches](/docs/foundry/ontologies/branching-ontology/) 来修改 ontology，并访问扩展功能，包括 branching datasources、在支持的应用程序中下游测试更改，以及在统一工作流中管理数据和 ontology 的修改。
> **⚠️ 警告**

> Ontology branches (formerly known as ontology proposals) are being sunset. On enrollments with Global Branching enabled, you can no longer create ontology branches. Instead, use [global branches](/docs/foundry/ontologies/branching-ontology/) to modify the ontology and access expanded capabilities including branching datasources, testing changes downstream in supported applications, and managing both data and ontology modifications within a unified workflow.
Ontology branches 允许你在一个分支上对 Ontology 进行更改，该分支基于该 ontology 的 `Main` 版本。此过程可确保所有修改在被纳入主 Ontology 之前都经过审阅和批准。

Ontology branches allow you to make changes to an Ontology on a branch, which is based on the `Main` version of that ontology. This process ensures that all modifications are reviewed and approved before being incorporated into the main Ontology.
要创建一个分支，你需要对包含相关资源的项目拥有 editor 权限。

To create a branch, you need editor permission on the project containing the resources.
## Definitions
* **Branch:** Ontology 上的一个 *branch* 是该 Ontology 的一个独立版本，派生自主版本，旨在支持实验和更改，而不会影响主分支。这使用户能够在隔离的环境中对 Ontology 的调整进行测试和完善，然后再将其合并回主分支。

* **Branch:** A *branch* on the Ontology is a separate version of that Ontology, derived from the main version, designed to enable experimentation and changes without impacting the main branch. This allows users to test and refine adjustments to the Ontology in an isolated environment before merging them back into the main branch.
* **Proposal（提案）：** *Proposal* 类似于版本控制系统中的 Pull Request，是专为 Ontology 分支量身定制的。Proposal 会随分支的创建自动生成，并包含 reviews、name 以及即将合并到主分支的更改描述等元数据。Proposal 是一种在独立分支中所做的更改被集成到主 Ontology 之前对其进行审查和批准的机制。

* **Proposal:** A *proposal* is analogous to a Pull Request in a version control system, specifically tailored for Ontology branches. A proposal is automatically created alongside a branch and contains metadata such as reviews, name, and descriptions of the changes being merged into the main branch. Proposals serve as a mechanism for reviewing and approving changes made in a separate branch before they are integrated into the main Ontology.
## Ontology branching workflow
通用的 ontology 分支工作流包含五个步骤：

The general ontology branching workflow has five steps:
1. [创建你的分支](#1-create-your-branch)

2. [准备你的 proposal 以供审查](#2-prepare-your-proposal-for-review)

3. [请求审查](#3-request-a-review)

4. [审查 proposal](#4-review-the-proposal)

5. [发布 proposal](#5-release-the-proposal)

1. [Create your branch](#1-create-your-branch)
2. [Prepare your proposal for review](#2-prepare-your-proposal-for-review)
3. [Request a review](#3-request-a-review)
4. [Review the proposal](#4-review-the-proposal)
5. [Release the proposal](#5-release-the-proposal)
每个步骤将在以下章节中详细说明。

Each step is outlined in the following sections.
### 1. Create your branch
你可以通过选择 **Create Branch** 来创建一个分支，这会打开一个对话框，你可以在其中为你的 proposal 选择 title 和 description。

You can create a branch by selecting **Create Branch** to open a dialog where you can choose a title and description for your proposal.
或者，如果你已经对 Ontology 进行了一些希望纳入 proposal 的更改，你可以在保存对话框中选择 save 并切换 **Propose your changes**。

Alternatively, if you already have changes to the Ontology that you would like to include in your proposal, you can select save and toggle **Propose your changes** from the save dialog.
![Propose your changes.](/docs/resources/foundry/ontologies/propose-changes.png)
如果你当前位于 Ontology 的主分支上，并且没有任何更改，你也可以通过选择分支选择组件并为新分支输入一个名称来创建一个分支。

If you are on the main branch of your Ontology, and you have no changes, you can also create a branch by choosing the branch select component and typing a name for the new branch.
Proposal 分支只能在主 Ontology configuration 上创建。你不能基于另一个 proposal 创建新分支。

Proposal branches can only be created on the main Ontology configuration. You cannot create a new branch based on another proposal.
在分支上时，位于 workspace interface 上方的分支导航 top bar 会显示你当前所在的分支。

While on a branch, a branch navigation top bar located above the workspace interface reflects your current branch.
![Branch navigation top bar.](/docs/resources/foundry/ontologies/topbar.png)
### 2. Prepare your proposal for review
此时，根据你创建 proposal 的方式，你的分支上可能已经有一些更改。在你的分支上，你可以继续对 Ontological resources 进行更改，包括创建和删除。

At this point, depending on how you created your proposal, you may already have some changes on your branch. While on your branch, you can continue making changes to Ontological resources, including creation and deletion.
每个被修改的 Ontological entity 都将在你的 proposal 中构成一个独立的 **Task**，并可供审查。

Every modified Ontological entity will constitute a separate **Task** in your proposal and made available for review.
对于已迁移使用 [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 的资源，viewers 可以在 proposal 中对资源进行更改。如果资源使用的是 datasource derived permissions，则只有 editors 或 owners 才能在 proposal 中对其进行更改。

For resources that have migrated to use [Ontology roles](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles), viewers can make changes to resources in a proposal. If the resource is on datasource derived permissions, only editors or owners can make changes to them on a proposal.
> **ℹ️ 注意**

> 在分支上，当你持有 editor 或 owner 权限时，可以编辑资源。
> **ℹ️ 注意**

> On a branch, you may edit resources when holding editor or owner permissions.
### 3. Request a review
在对分支进行更改之后，你可以向你的 proposal 添加 reviewers。为此，请导航到你的 [Proposal view](#2-prepare-your-proposal-for-review)，方法是在 top bar 中选择 **Open proposal details**。

After making changes to the branch, you may add reviewers to your proposal. To do so, navigate to your [Proposal view](#2-prepare-your-proposal-for-review), by selecting **Open proposal details** located in the top bar.
如果你已经退出了分支，你可以通过以下两种方式进入你的 proposal overview：导航到 **Proposals** 选项卡并选择你的 proposal，或者使用 branch select 组件。

If you exited your branch, you can go to your proposal overview either by navigating to the **Proposals** tab and selecting your proposal, or by using the branch select component.
从那里，从 **Reviewers（审查者）** 部分分配审查者。

From there, assign reviewers from the **Reviewers** section.
在 proposal 进入 `In review（审查中）` 阶段之前，审查者不会收到通知。

Reviewers are not notified until the proposal is in the `In review` stage.
> **ℹ️ 注意**

> 您也可以对 proposal 中的各个任务添加评论，以提供有关所提议更改的背景信息。通过选择 **Reviews（审查）** 选项卡，然后选择最右侧的 **Comments（评论）** 侧边栏，访问任务的 **Comments（评论）** 部分。
> **ℹ️ 注意**

> You may also leave comments on the various tasks in your proposal to give context about the changes proposed. Access the **Comments** section of your tasks by choosing the **Reviews** tab, and then selecting the **Comments** sidebar on the far right.
### 4. Review the proposal
审查者可以在 **Reviews（审查）** 选项卡中批准或拒绝单个任务，并可以添加评论以支持其审查。

Reviewers may approve or reject individual tasks in the **Reviews** tab, and may add comments to support their review.
审查者必须具有 owner 或 edit 权限才能批准更改。

Reviewers must have owner or edit permissions to be able to approve a change.
没有权限的用户仍然可以审查任务，例如表达他们对更改的意见，但这不会影响任务的 approved 状态。

Users without permissions may still review the task, for example, to convey their opinions on the change, but this will not affect the approved status of the task.
如果 proposal 的创建者对所有已编辑的资源具有 owner 或 editor 权限，他们将能够批准自己的更改。

If the creator of the proposal has owner or editor permissions on all the edited resources, they will be able to approve their own changes.
> **⚠️ 警告**

> 即使 editor 或 owner 未被明确添加为审查者，他们仍然可以批准您的 proposals。我们建议将审查者列表用作跟踪谁应该审查更改的方式，而不是用作保护 Ontology 的方式。相反，通过仔细分配角色和权限来保护 Ontology。
> **⚠️ 警告**

> Even if an editor or owner is not explicitly added as a reviewer, they can still approve your proposals. We recommend using the reviewers list as a way to keep track of who should review changes, but not as a way of safeguarding the Ontology. Instead, protect the Ontology by carefully assigning roles and permissions.
### 5. Release the proposal
一旦您的更改经过审查并获得批准，proposal 就可以合并到 Ontology 中。

Once your changes have been reviewed and approved, the proposal can be merged into the Ontology.
> **ℹ️ 注意**

> 将更改合并到 Ontology 不需要特殊权限。proposal 获得批准后，任何可以编辑该分支的人都可以将 proposal 合并到 Ontology 中。
> **ℹ️ 注意**

> Merging changes into the Ontology does not require special permissions. After a proposal is approved, anyone who can edit the branch can merge the proposal into the Ontology.
proposal 合并后，它会从侧边栏的 **In Review（审查中）** 部分移至 **Merged（已合并）** 部分。

After a proposal is merged, it is moved from the **In Review** section to the **Merged** section in the sidebar.
在您合并 proposal 之前的任何时间，您都可以通过从侧边栏中选择 **delete（删除）** 来关闭该 proposal。

At any point of time before you merge the proposal, you can close the proposal by selecting **delete** from the sidebar.
Proposals 只能合并到主 ontology 配置中。

Proposals can only be merged into the main ontology configuration.
Proposals 无法自动恢复。要撤销一个 proposal，您必须撤销其中的不同更改。

Proposals cannot be reverted automatically. To undo a proposal, you must undo the different changes within it.
> **⚠️ 警告**

> 一旦 proposal 被关闭，它就无法被重新打开。
> **⚠️ 警告**

> Once a proposal is closed, it cannot be reopened.