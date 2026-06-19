<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/branching-ontology/
---
# Branching the ontology
该 Ontology 与 Global Branching 集成，以实现 ontology 资源的安全、隔离开发。本文档介绍如何在 branch 上使用 ontology，包括添加和修改资源、rebase 和 conflict resolution、review 和 merge 流程以及已知限制。

The ontology integrates with Global Branching to enable safe, isolated development of ontology resources. This documentation covers how to work with the ontology on branches, including adding and modifying resources, rebasing and conflict resolution, the review and merge process, and known limitations.
有关 Global Branching 概念和工作流程的一般信息，请参阅 [Global Branching 文档](/docs/foundry/global-branching/overview/)。

For general information on Global Branching concepts and workflows, refer to the [Global Branching documentation](/docs/foundry/global-branching/overview/).
## Definitions
有关 branch、proposal 和 rebase 的一般定义，请参阅 [Global Branching 核心概念](/docs/foundry/global-branching/core-concepts/)。以下术语是 ontology branching 特有的：

For general definitions of branches, proposals, and rebasing, refer to the [Global Branching core concepts](/docs/foundry/global-branching/core-concepts/). The term below is specific to ontology branching:
* **Ontology proposal：** 当您在包含 ontology 更改的 branch 上 [创建 Global Branching proposal](/docs/foundry/global-branching/core-concepts/#create-and-prepare-a-proposal) 时，系统会自动创建一个 ontology proposal 来跟踪 ontology 特定的更改。Ontology proposal 包含元数据，例如 review、要合并到 `main` 中的 ontology 更改的名称和描述。

* **Ontology proposal:** When you [create a Global Branching proposal](/docs/foundry/global-branching/core-concepts/#create-and-prepare-a-proposal) on a branch that includes ontology changes, an ontology proposal is automatically created to track the ontology-specific changes. The ontology proposal contains metadata such as reviews, name, and descriptions of the ontology changes being merged into `main`.
## Adding and modifying resources
要修改 branch 上的 ontology，您可以创建一个新 branch，或者使用 branch selector 访问现有 branch。

To modify the ontology on a branch, you can either create a new branch in Ontology Manager, or access an existing branch using the branch selector.
要创建 branch，请打开 branch selector 并选择 **Create new branch**，打开一个对话框，在其中为您的 branch 添加标题和描述。

To create a branch, open the branch selector and choose **Create new branch** to open a dialog where you can add a title and description for your branch.

> 📷 **[图片: Branch selector.]**

> 📷 **[图片: Branch selector.]**

如果您已有要包含在 branch 中的 ontology 更改，可以从保存对话框中选择 **Save to new branch**，以使用这些更改创建一个单独的 branch。请注意，如果您对任何 [受保护的 ontology 资源](#resource-protection) 进行更改，则需要保存到一个新 branch。

If you already have changes to the ontology that you would like to include in a branch, you can select **Save to new branch** from the save dialog to create a separate branch with those changes. Note that if you make changes to any [protected ontology resources](#resource-protection), you will be required to save to a new branch.

> 📷 **[图片: Save to ontology option.]**

> 📷 **[图片: Save to ontology option.]**

> **ℹ️ 注意**

> 您只能从主 ontology（也称为 `main` branch）创建 branch。
> **ℹ️ 注意**

> You can only branch from the main ontology, also known as `main` branch.
在分支上时，位于界面底部的 [branch taskbar](/docs/foundry/global-branching/branch-taskbar/) 将显示您当前的分支名称以及其他元数据。

While on a branch, a [branch taskbar](/docs/foundry/global-branching/branch-taskbar/) at the bottom of the interface will display your current branch name and additional metadata.
## Resource protection
分支保护支持的 ontology 资源类型包括：

The ontology resource types supported by branch protection include:
* Object types
* Action types
* Link types
* Interface types
* Shared property types
* Object types
* Action types
* Link types
* Interface types
* Shared property types
以下类型不支持资源保护：

Resource protection is not supported on:
* 类型组（Type groups）

* 规则集（修改规则集时，将强制执行包含该规则集的 object type 的保护状态）

* Type groups
* Rule sets (when modifying a rule set, the protection status of the containing object type will be enforced)
此外，ontology 资源必须先迁移到使用项目权限（project permissions）才能被保护。有关更多信息，请参阅 [ontology permissions](/docs/foundry/object-permissioning/ontology-permissions/)。

Additionally, ontology resources must be migrated to use project permissions before they can be protected. For more information, review [ontology permissions](/docs/foundry/object-permissioning/ontology-permissions/).
将 ontology 资源迁移到使用项目权限后，您可以通过父项目的 **Files** 选项卡查看和管理其保护状态。

After migrating an ontology resource to use project permissions, you can view and manage its protection status via the parent project's **Files** tab.
![Protecting an ontology resource.](/docs/resources/foundry/ontologies/protect-from-compass.png)
启用保护后，您必须在单独的分支上进行更改，并创建一个 proposal 以将其合并到主分支（main branch）。

Once protection is enabled, you must make changes on a separate branch and create a proposal to merge them into the main branch.
在 Ontology Manager 的 **Overview** 选项卡中也可以看到保护状态：

The protection status is also visible in Ontology Manager on the **Overview** tab:
![Protected ontology resource in Ontology Manager overview page.](/docs/resources/foundry/ontologies/ontology-overview-tab.png)
您还可以在 **Security** 选项卡下查看适用的策略：

You can also review the applicable policy under the **Security** tab:
![Protected ontology resource in Ontology Manager's Security tab.](/docs/resources/foundry/ontologies/ontology-security-tab.png)
修改受保护的资源时，**Save** 对话框将被替换为 **Create and save to branch**，要求您将更改保存到一个新分支。

When modifying protected resources, the **Save** dialog is replaced with **Create and save to branch**, requiring you to save changes to a new branch.
![Save to new branch option in Ontology Manager.](/docs/resources/foundry/ontologies/modify-protected-object.png)
## Rebasing and conflict resolution
当您在分支上引入更改时，`main` 也可能收到来自其他人的新更改。Rebase 操作会将来自 `main` 的最新更改合并到您当前的分支中，以使您当前的分支保持最新。

While you are introducing changes on your branch, `main` can also receive new changes from others. Rebasing incorporates the latest changes from `main` into your current branch to keep your current branch up to date.
> **ℹ️ 注意: Automatic rebasing**

> 如果您的全局分支（global branch）不包含对 ontology 的更改，则会自动执行 rebase。一旦您向分支引入 ontology 更改（包括为 object type 建立索引），您将需要手动 rebase，以使您的分支与 `main` 保持同步。
> **ℹ️ 注意: Automatic rebasing**

> If your global branch does not contain changes to the ontology, rebasing occurs automatically. Once you introduce ontology changes to your branch, including indexing an object type, you will need to manually rebase to keep your branch up to date with `main`.
### Rebase a branch
当 `main` 有新的更改时，侧边栏的 **Main branch updates** 选项卡上会出现一个蓝色指示符，以提示您查看这些更改。

When there are new changes from `main`, a blue indicator appears on the **Main branch updates** tab in the sidebar to prompt you to review these changes.

> 📷 **[图片: Main branch updates.]**

> 📷 **[图片: Main branch updates.]**

导航至 **Main branch updates** 页面，查看自上次 rebase 以来（或如果是首次手动 rebase，则为自分支创建以来）的传入更改。选择 **Rebase branch** 以使用最新的 `main` 版本更新您的分支。

Navigate to the **Main branch updates** page to view incoming changes since your last rebase — or since branch creation, if this is your first manual rebase. Select **Rebase branch** to update your branch with the latest version of `main`.
![Rebase branch view.](/docs/resources/foundry/ontologies/rebase-branch-view.png)
如果没有冲突或错误，rebase 将自动完成，您的分支将保持最新。

If there are no conflicts or errors, the rebase will complete automatically, and your branch will be up to date.
### Resolve merge conflicts
如果存在冲突，您的 rebase 将保持进行中，并且您将被重定向到 **Conflicts tab** 以解决分支与 `main` 之间的任何冲突更改。如果仅有错误，则会改为重定向到 **Errors tab**。

If there are conflicts, your rebase will remain in progress, and you will be redirected to the **Conflicts tab** to resolve any conflicting changes between your branch and `main`. If there are only errors, you will be redirected to the **Errors tab** instead.
在 rebase 期间，来自 `main` 的更改会加载到您的分支上，而当前分支中之前保存的任何更改则会重新加载回工作状态中，您可以在 **All changes** tab 中查看这些更改。

During rebasing, changes from `main` are loaded onto your branch, while any previously saved changes from your current branch are reloaded back into the working state, which you can see in the **All changes** tab.
此状态允许您查看和访问来自 `main` 和您分支的更改。当某个 ontology resource 同时包含来自两个分支的更改时，默认显示您分支的版本。

This state allows you to view and access changes from both `main` and your branch. When an ontology resource has changes from both branches, it will display your branch version by default.
![Review rebase changes.](/docs/resources/foundry/ontologies/review-rebase-changes.png)
要解决冲突，您可以为每个资源选择 **Use Main branch changes** 或 **Keep current branch changes**。或者，您也可以直接导航到该资源并应用 **custom changes** 来解决其冲突。

To resolve conflicts, you can choose to **Use Main branch changes** or **Keep current branch changes** for each resource. Alternatively, you can navigate directly to that resource and apply **custom changes** to resolve its conflicts.
在此示例中，`Palantir employee` object type 存在冲突，其 display name 在 `main` branch 和您的分支上均被更改。要解决此冲突，请选择保留该 object type 的哪个版本。

In this example, the `Palantir employee` object type has a conflict in which the display name has been changed on both `main` branch and your branch. To resolve this conflict, choose which version of this object type to keep.
![Review object type rebase changes.](/docs/resources/foundry/ontologies/review-object-type-rebase-changes.png)
您也可以通过进行自定义更改来解决此冲突。在该示例中，您可以导航到该 object type 并将其 display name 从 "Palantir employee" 更改为 "Current employee"。由于此自定义更改，冲突将被解决。

You can also resolve this conflict by making a custom change. In the example, you can navigate to the object type and change its display name from "Palantir employee" to "Current employee". The conflict will now be resolved due to this custom change.
![Current employee example.](/docs/resources/foundry/ontologies/current-employee-example.png)
![Current employee example conflicts.](/docs/resources/foundry/ontologies/current-employee-example-conflicts.png)
在解决所有冲突后，请确保在完成 rebase 之前处理所有错误。

After resolving all conflicts, ensure any errors are addressed before finishing your rebase.
### Finish rebase
一旦所有错误和冲突均已解决，您可以选择 **Finish rebase and save**，您的分支将保持最新。

Once all errors and conflicts have been resolved, you can select **Finish rebase and save**, and your branch will be up to date.
![Finish rebase and save option.](/docs/resources/foundry/ontologies/finish-rebase-and-save.png)
您可以继续在您的分支上工作，并定期执行 rebase，以使您的分支与 `main` branch 的最新版本保持一致。

You can continue working on your branch and rebasing regularly to keep your branch current with the latest version of `main` branch.
![Branch is up-to-date.](/docs/resources/foundry/ontologies/branch-is-up-to-date.png)
## Merge requirements
### Prepare your branch for review
在完成更改并准备将分支合并到 `main` 时，请通过在分支任务栏中选择 **Create proposal** 图标来创建 proposal。添加名称和描述以设置您的 proposal。

When you are ready to merge your branch into `main` after making your changes, create a proposal by selecting the **Create proposal** icon in the branch taskbar. Add a name and description to set up your proposal.
![Create proposal from taskbar.](/docs/resources/foundry/ontologies/create-proposal-taskbar.png)
![Create proposal from dialog.](/docs/resources/foundry/ontologies/create-proposal-dialog.png)
创建 proposal 后，将运行 **merge checks** 以验证 global branch 上的资源是否能够合并到 `main` branch。失败的检查可能包括您的分支与 `main` branch 之间的冲突，这需要您对分支进行 rebase。

When a proposal is created, **merge checks** will run to verify whether the resources on a global branch are able to merge into the `main` branch. Failed checks can include conflicts between your branch and the `main` branch, which would require you to rebase your branch.

> 📷 **[图片: Taskbar popover with merge checks.]**

> 📷 **[图片: Taskbar popover with merge checks.]**

### Request a review
您可以通过分支任务栏、Global Branching proposal 页面或 ontology proposal 页面为您的 proposal 添加审阅者。

You can add reviewers to your proposal through the branch taskbar, the Global Branching proposal page, or the ontology proposal page.
在 ontology 提案页面，导航至 **Review changes** 并选择 **Invite reviewers** 以向你的提案添加审阅者。对于已迁移至项目的 ontology 资源，请选择 **View policies** 以查看基于关联项目策略需要哪些审阅者来审核该资源。

On the ontology proposal page, go to **Review changes** and select **Invite reviewers** to add reviewers to your proposal. For ontology resources that have migrated to projects, select **View policies** to see which reviewers are required to review a resource based on the associated project policies.
每个 ontology 资源都被视为一个独立的任务。资源名称旁边的状态标签表示整体审批状态，而右侧的 **Your review** 部分允许你提交审阅意见。

Each ontology resource is considered an individual task. The status tag next to the resource name indicates the overall approval status, while the **Your review** section on the right allows you to submit a review.
> **ℹ️ 注意**

> 虽然 ontology 实体在 Global Branching 中被视为独立的资源，但它们在同一个本地 ontology 提案下进行分组。这意味着向一个 ontology 资源添加审阅者，实际上会为该审阅者添加所有 ontology 资源的审阅权限。
> **ℹ️ 注意**

> While ontology entities are treated as separate resources in Global Branching, they are grouped under a single local ontology proposal. This means adding a reviewer to one ontology resource effectively adds that reviewer across all ontology resources.
![Ontology proposal review changes.](/docs/resources/foundry/ontologies/ontology-proposal-review-tab.png)
> **ℹ️ 提示: 发表评论**

> 你还可以对提案中的各个任务发表评论，以提供有关所提议更改的背景信息。通过选择最右侧的 Comments 侧边栏，访问任务的 Comments 部分。
> **ℹ️ 提示: Leaving comments**

> You may also leave comments on the various tasks in your proposal to give context about the changes proposed. Access the Comments section of your tasks by selecting the Comments sidebar on the far right.
### Review the proposal
在 **Review changes** 选项卡中，审阅者可以批准或拒绝单个任务。没有相关权限的用户仍然可以审核任务，例如表达他们对更改的意见，但这不会影响任务的批准状态。

In the **Review changes** tab, reviewers may approve or reject individual tasks. Users without permissions may still review the task, for example, to convey their opinions on the change, but this will not affect the approved status of the task.
> **⚠️ 警告: 审批权限**

> 具有审批权限的用户即使未被添加为审阅者也可以批准提案。请使用审阅者列表来跟踪应当审阅更改的人员，而不是用于限制审批操作。
> **⚠️ 警告: Approval rights**

> Users with approval rights can approve proposals even if not added as reviewers. Use the reviewers list to track who should review changes, not to restrict approvals.
在 ontology 提案中，审阅者可以查看提案详情，并批准或拒绝对所有已修改资源或特定 ontology 资源的更改。

In the ontology proposal, reviewers can view the proposal details and approve or reject changes to all modified resources or to specific ontology resources.
![Approve ontology change.](/docs/resources/foundry/ontologies/review-protected-object.png)
一旦满足策略要求，已批准资源的状态将从 `In Progress` 变为 `Approved`。如果所有其他检查均已通过，你就可以合并该提案。

Once the policy requirements are met, approved resources change from `In Progress` to `Approved`. You can then merge the proposal if all other checks have passed.
### Merge your branch
当你准备好将更改合并到 `main` 时，你必须合并你的 Global Branching 提案。这将自动启动 ontology 的合并流程。

When you are ready to merge your changes to `main`, you must merge your Global Branching proposal. This will automatically kick off the merge process for the ontology.
![Merge branch option in Global Branching page.](/docs/resources/foundry/ontologies/test-changes-foundry-branching-merge-branch.png)
为此，请在分支任务栏中选择合并图标，或导航到 Global Branching 中的提案页面并选择 **Merge proposal**。

To do so, select the merge icon in the branch taskbar, or navigate to your proposal page in Global Branching and select **Merge proposal**.
## Known limitations
* **Datasource deletion:** 当在一个 object type 上发生冲突，且该 object type 的 backing datasource 在 `main` 分支上已被替换或删除时，选择保留你的分支更改将导致合并失败。在这种情况下，请选择 `main` 分支的更改。

* **Conditional formatting deletion:** 当在一个 property type 上发生冲突，且该 property type 的 conditional formatting rule set 在 `main` 分支上已被替换或删除时，选择保留你的分支更改将导致合并失败。在这种情况下，请选择 `main` 分支的更改。

* **Pipeline Builder object types:** 在 Pipeline Builder 中创建的 object type 无法在分支上的 Ontology Manager 中进行修改。

* **Indexing counts as a modification:** 对 object type 进行索引操作被视为一项修改。如果该资源受到项目策略的保护，你将需要获得策略批准才能合并你的分支。若要绕过此要求，请在合并前移除索引相关的更改。

* **Reviewers apply across all ontology resources:** 由于 ontology 更改是分组在一起的，向一个 ontology 资源添加审阅者会将其添加至整个提案。只有资源项目策略中的用户才需要批准该特定资源。

* **Datasource deletion:** When a conflict occurs on an object type where a backing datasource has been replaced or removed on the `main` branch, choosing to keep your branch changes will lead to a merge failure. In this case, choose the `main` branch changes.
* **Conditional formatting deletion:** When a conflict occurs on a property type where a conditional formatting rule set has been replaced or removed on the `main` branch, choosing to keep your branch changes will lead to a merge failure. In this case, choose the `main` branch changes.
* **Pipeline Builder object types:** Object types created in Pipeline Builder are not modifiable in Ontology Manager on a branch.
* **Indexing counts as a modification:** Indexing an object type is treated as a modification. If the resource is protected by a project policy, you will need policy approval to merge your branch. To bypass this requirement, remove indexing changes before merging.
* **Reviewers apply across all ontology resources:** Adding reviewers to one ontology resource adds them to the entire proposal, as ontology changes are grouped together. Only users in a resource's project policy are required to approve that specific resource.