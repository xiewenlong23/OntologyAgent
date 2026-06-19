<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/branching-functions/
---
# Branching functions
您可以在 global branch 上开发、发布和使用 function。目前支持 TypeScript v1 functions 和 AIP Logic functions。

You can develop, publish, and consume functions on a global branch. This is currently supported for TypeScript v1 functions and AIP Logic functions.
## Developing functions
> **ℹ️ 注意**

> 要将 Global Branching 用于 TypeScript v1，请将您的代码仓库模板版本升级到 `functions-typescript` 子模板的 `0.903.0` 版本或更高版本。请查看[有关代码仓库升级的文档](/docs/foundry/code-repositories/repository-upgrades/#manual-branch-upgrade)以获取操作说明。
> **ℹ️ 注意**

> To use Global Branching for TypeScript v1, upgrade your repository template version to version `0.903.0` of the `functions-typescript` child template or higher. Review [the documentation on repository upgrades](/docs/foundry/code-repositories/repository-upgrades/#manual-branch-upgrade) for instructions.
您可以开发一个依赖于 global branch 上资源更改的 function，例如新创建或修改的 ontology entity。

You can develop a function that depends on changes made to resources on your global branch, such as newly created or modified ontology entities.
![Developing a new function on a branch.](/docs/resources/foundry/functions/branch-function.png)
当您准备就绪后，使用 **version target** 发布您的 function——即 global branch 合并时发布到 `main` 的稳定版本。在您的 branch 上进行开发期间，该 function 将作为不稳定的预览版本发布。

When you are ready, publish your function with a **version target** — the stable version published to `main` when the global branch merges. During development on your branch, the function is published as unstable preview versions.
![Publishing functions on a branch.](/docs/resources/foundry/functions/branch-function-publish.png)
一旦您成功在 branch 上发布了您的 function，您就可以在 Workshop、AIP Logic 和 function-backed action 中使用该 branch 上的新 function 版本。此 function 版本带有 `Branched pre-release` 标签。请注意，在您的 branch 上发布的 function 将无法从其他 branch（包括 `main`）访问。

Once you have successfully published your function on the branch, you can use the new function version on your branch in Workshop, AIP Logic, and function-backed actions. This function version is labeled with the `Branched pre-release` tag. Note that functions published on your branch will not be accessible from other branches, including `main`.
![Using a branched function in Workshop.](/docs/resources/foundry/functions/branch-function-backed-variable.png)
![Using a branched function in actions.](/docs/resources/foundry/functions/branch-function-backed-action.png)
> **ℹ️ 注意**

> 目前无法在 TypeScript v1 代码仓库中依赖 query function 的 branch 版本。
> **ℹ️ 注意**

> It is currently not possible to depend on branched versions of query functions in TypeScript v1 repositories.
当您继续在 branch 上进行开发时，您可以继续将 function 版本发布到同一个 version target。只要您的 version target 保持不变，任何使用您 function 的资源都将自动拉取最新发布的版本。这使您能够快速迭代，而无需在每次发布后手动更新 function 引用。

As you continue developing on your branch, you can continue publishing function versions to the same version target. As long as your version target remains the same, any resource using your function will automatically pull the latest published version. This lets you iterate quickly without manually updating function references after each publish.
如果分支上的版本目标发生变化，你必须更新该 function 所有正在分支上使用旧版本的下游依赖项，以使用新的版本目标。这也会作为 [check](/docs/foundry/global-branching/core-concepts/#checks) 显示。

If the version target on the branch changes, you must update all dependents of the function that were using the old version on the branch to use the new version target. This will also be displayed as a [check](/docs/foundry/global-branching/core-concepts/#checks).
## Conflict resolution and rebasing functions
在分支上进行开发时，你不会自动接收到发布到 `main` 的较新 function 版本。这可以防止 main 上的开发干扰你的分支工作。如果 `main` 上有可用的较新版本，你将在 function 版本选择器和 Ontology Manager 中看到通知。然后你可以 rebase 你的 function 版本以拉取 `main` 上所有较新的版本。

When developing on a branch, you will not automatically receive newer function versions published to `main`. This prevents main development from disrupting your branch work. If newer versions are available on `main`, you will see notifications in function version selectors and Ontology Manager. You can then rebase your function versions to pull in all newer versions from `main`.
![Rebasing functions dialog.](/docs/resources/foundry/functions/rebasing-functions.png)
如果你正在开发时，版本目标已发布到 `main`，则你必须在合并之前选择一个全新的版本目标。完成后，请更新所有下游依赖项以使用新的版本目标。

If your version target gets published to `main` while you are developing, you must select a new version target before merging. Once you do, update any dependents to use the new version target.
## Merging
合并 global branch 时，修改过的 functions 将以稳定版本目标发布到 `main`。使用你分支上发布版本的资源将在合并过程中自动开始使用 `main` 上发布的新稳定版本。

When merging your global branch, modified functions will be published on `main` with the stable version target. Resources using the version published on your branch will automatically start using the new stable version that was published on `main` as part of the merge.
> **⚠️ 警告**

> Foundry 仅将你的版本目标合并到 `main`，而不会合并分支上发布的其他版本。这些版本在你的分支合并后不会存在于 `main` 上。
> **⚠️ 警告**

> Foundry only merges your version target into `main` and does not merge other versions published on the branch. Those versions will not exist on `main` after your branch merges.