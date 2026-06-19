<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/getting-started/
---
# Getting started with functions
在 Foundry 中开始使用 functions 有三种语言选项：TypeScript v1、TypeScript v2 和 Python。有关每种语言支持功能的更多信息，请参阅 [language feature support](/docs/foundry/functions/language-feature-support/) 规范。

There are three language options for getting started with functions in Foundry; TypeScript v1, TypeScript v2, and Python. For more information on supported features for each language, review the [language feature support](/docs/foundry/functions/language-feature-support/) specifications.
尽管每种语言具有不同的支持功能集，但你将能够访问每种语言的相同基本平台功能，包括运行、测试和发布 functions。本页提供了这些功能的概述，以帮助你了解如何使用 functions 仓库，无论你将使用哪种语言。

Although each language has a different set of supported features, you will be able to access the same basic platform functionality for each language, including running, testing, and publishing functions. This page provides an overview of these features to help you understand how to use functions repositories, regardless of which language you will be working with.
有关使用特定语言入门的更详细说明，请参阅以下教程：

For more detailed instructions on getting started with a specific language, refer to the tutorials below:
* [Getting started with TypeScript v1 functions](/docs/foundry/functions/typescript-v1-getting-started/)
* [Getting started with TypeScript v2 functions](/docs/foundry/functions/typescript-v2-getting-started/)
* [Getting started with Python functions](/docs/foundry/functions/python-getting-started/)
* [Getting started with TypeScript v1 functions](/docs/foundry/functions/typescript-v1-getting-started/)
* [Getting started with TypeScript v2 functions](/docs/foundry/functions/typescript-v2-getting-started/)
* [Getting started with Python functions](/docs/foundry/functions/python-getting-started/)
请查看以下章节，获取有关 functions 仓库创建和使用的一般信息。

Review the sections below for general information on functions repository creation and usage.
## Create a functions repository
创建 functions 仓库时，你将能够选择最适合你需求的语言。你可以通过选择 **+ New > Repository** 直接从你选择的项目中初始化 functions 仓库，或者通过在右上角选择 **+ New repository** 从 Code Repositories 应用中进行初始化。仓库初始化后，你可以添加并运行 functions。

When creating a functions repository, you will be able to choose the language that best suits your needs. You can initialize functions repositories directly from a project of your choice by selecting **+ New > Repository**, or from the Code Repositories application by selecting **+ New repository** in the top right. Once the repository has been initialized, you can add and run functions.
![Create a functions code repository.](/docs/resources/foundry/functions/functions-create-repo.png)
有关如何为特定语言创建 functions 仓库的详细说明，请参阅以下教程章节：

For detailed instructions on how to create a functions repository for a specific language, refer to the tutorial sections below:
* [Create a TypeScript v1 functions repository](/docs/foundry/functions/typescript-v1-getting-started/#create-a-typescript-v1-functions-repository)
* [Create a TypeScript v2 functions repository](/docs/foundry/functions/typescript-v2-getting-started/#create-a-typescript-v2-functions-repository)
* [Create a Python functions repository](/docs/foundry/functions/python-getting-started/#create-a-python-functions-repository)
* [Create a TypeScript v1 functions repository](/docs/foundry/functions/typescript-v1-getting-started/#create-a-typescript-v1-functions-repository)
* [Create a TypeScript v2 functions repository](/docs/foundry/functions/typescript-v2-getting-started/#create-a-typescript-v2-functions-repository)
* [Create a Python functions repository](/docs/foundry/functions/python-getting-started/#create-a-python-functions-repository)
## Test in live preview
functions 实时预览（live preview）允许你在将 functions 提交到仓库之前对其进行测试。你可以将 function 添加到仓库后，在实时预览中运行该 function。为此，请打开底部工具栏上的 **Functions**，然后选择 **Live Preview**。选择一个 function，输入输入值，然后选择 **Run** 来运行该 function。

The functions live preview allows you to test your functions before committing them to your repository. You can run a function in live preview after adding it to your repository. To do so, open **Functions** on the bottom toolbar and select **Live Preview**. Choose a function, enter input values, and select **Run** to run the function.
![Run your new function in the functions live preview.](/docs/resources/foundry/functions/tsv2-functions-helper-preview-run.png)
> **⚠️ 警告**

> 实时预览在不同于已发布 functions 的运行时环境中运行。差异包括 CPU 资源、可用内存以及 function 在超时之前可以运行的时间。
> [管理已发布 functions 的运行时环境。](/docs/foundry/functions/manage-functions/)
> **⚠️ 警告**

> Live preview runs in a different runtime environment than published functions. Differences include CPU resources, available memory, and how long a function can run before timing out.
> [Manage the runtime environment for published functions.](/docs/foundry/functions/manage-functions/)
在右上角选择 **Commit（提交）**，将你的更改提交到仓库的 `master` 分支。

Select **Commit** in the upper right to commit your changes to the `master` branch of your repository.
## Publish your functions
提交工作后，你将看到 **Tag version（标记版本）** 选项。这将把你仓库中的所有 functions 发布到 functions registry，使它们在整个平台中可被访问（[making them accessible across the platform](/docs/foundry/functions/use-functions/)）。

Once you commit your work, you will see the option to **Tag version**. This will publish all of the functions in your repository to the functions registry, [making them accessible across the platform](/docs/foundry/functions/use-functions/).
![The "Tag version" option.](/docs/resources/foundry/functions/ts-functions-tags.png)
选择 **Tag version（标记版本）** 以从 `master` 分支标记一个发布版本。根据更改的范围设置 tag 名称，然后选择 **Tag and release（标记并发布）**。

Select **Tag version** to tag a release off of the `master` branch. Set the tag name based on the extent of your changes, then choose **Tag and release**.

> 📷 **[图片: Choose the version type to tag for the new release.]**

> 📷 **[图片: Choose the version type to tag for the new release.]**

要在你的 functions 被标记和发布时查看进度，请选择 **View（查看）** 弹出窗口或导航到 **Tags（标记）** 选项卡。一旦 **Step 2: Release（步骤 2：发布）** 完成，请选择已发布的 functions 以在 functions registry 中查看它们。

To view progress as your functions are tagged and released, select the **View** pop-up or navigate to the **Tags** tab. Once **Step 2: Release** is completed, select the published functions to view them in the functions registry.
> **⚠️ 警告**

> 在权限传播过程中，functions 在 Workshop 或 functions registry 中可能无法立即通过名称搜索到。
> **⚠️ 警告**

> Functions may not be immediately searchable by name in Workshop or the functions registry while permissions propagate.
![Both the tag and release checks passed, and the new function is published.](/docs/resources/foundry/functions/tsv1-functions-tags-and-releases.png)
## Run your function
在为你的 tag 的检查通过后，导航回 Code Repositories 中的 **Code（代码）** 选项卡，并从底部工具栏中选择 **Functions（函数）**。你应该在 **Published（已发布）** 部分下看到你新的 function。选择它，并尝试运行这个新的 function：

After the checks for your tag have passed, navigate back to the **Code** tab in Code Repositories and select **Functions** from the bottom toolbar. You should see your new function under the **Published** section. Select it, and try running the new function:
![Run the new function in the functions helper.](/docs/resources/foundry/functions/tsv1-functions-helper-run.png)
[Learn more about leveraging functions across the platform.](/docs/foundry/functions/use-functions/)
[Learn more about leveraging functions across the platform.](/docs/foundry/functions/use-functions/)