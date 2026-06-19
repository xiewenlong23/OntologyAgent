<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/typescript-v2-getting-started/
---
# Getting started with TypeScript v2 functions
TypeScript v2 allows users to take advantage of several key [improvements over TypeScript v1](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including a Node.js runtime and first-class OSDK support. Review the sections below to get started.
TypeScript v2 allows users to take advantage of several key [improvements over TypeScript v1](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including a Node.js runtime and first-class OSDK support. Review the sections below to get started.
## Create a TypeScript v2 functions repository
Navigate to a project of your choice and create a new code repository by selecting **+ New > Repository**. Select the TypeScript v2 functions template to initialize your repository.
Navigate to a project of your choice and create a new code repository by selecting **+ New > Repository**. Select the TypeScript v2 functions template to initialize your repository.
![Create a TypeScript v2 function code repository.](/docs/resources/foundry/functions/tsv2-functions-create-repo.png)
Once the repository has been created, navigate to the `typescript-functions/src/functions/helloWorld.ts` file.
Once the repository has been created, navigate to the `typescript-functions/src/functions/helloWorld.ts` file.
## Write a function
要编写新的 function，请在仓库的 `typescript-functions/src/functions` 目录中创建一个新文件，并为其指定一个描述性名称，例如 `helloWorld.ts`。编写 function 时必须使用 `export default`，以便 Foundry 能够检测到它。

To write a new function, create a new file in the `typescript-functions/src/functions` directory of your repository and give it a descriptive name, for example, `helloWorld.ts`. Write your function using `export default` for Foundry to detect it.
```typescript tab="TypeScript v2"
export default function helloWorld(): string {
return "Hello World!";
}
```
要将 function 发布到 Foundry，您必须满足以下条件：

You must satisfy the following conditions for your function to be published to Foundry:
1. 在 `typescript-functions/src/functions` 目录中的 `.ts` 文件里定义您的 function。在此目录中，您还可以将相关的 function 分组到子目录中。

2. 文件名必须与 function 的名称匹配。要发布名为 `myFunction` 的 function，它必须定义在 `typescript-functions/src/functions` 目录中名为 `myFunction.ts` 的文件里。

3. TypeScript function 必须是该文件的默认导出 (default export)。

4. 您的 function 的输入和输出类型必须遵循支持的 function 类型，详情请参阅 [类型参考](/docs/foundry/functions/types-reference/)。

1. Define your function in a `.ts` file in the `typescript-functions/src/functions` directory. In this directory, you can also group related functions in subdirectories.
2. The name of your file must match the name of your function. For a function called `myFunction` to be published, it must be defined in a file called `myFunction.ts` within the `typescript-functions/src/functions` directory.
3. The TypeScript function must be the default export of your file.
4. Your function's input and output types must follow the supported function types, as detailed in the [type reference](/docs/foundry/functions/types-reference/).
function 的文件路径用于唯一标识从该文件发布的 function。请注意，function 文件路径的更改将导致发布一个新的 function。

Your function's file path is used to uniquely identify the function that gets published from it. Note that a change in your function's file path will therefore result in a new function being published.
## Test in live preview
要在 live preview 中测试您的 function，请打开 **Functions** 辅助工具并选择 **Live preview**。选择您的 function，然后选择 **Run** 来执行。

To test your function in live preview, open the **Functions** helper and select **Live preview**. Choose your function and select **Run** to execute.

> 📷 **[图片: 在 functions 辅助工具中运行您的新 function。]**

> 📷 **[图片: Run your new function in the functions helper.]**

## Commit and publish a function
在窗口右上角选择 **Commit**，将您的更改提交到仓库的 `master` 分支。要查看 function 的 checks（检查），请打开页面顶部的 **Checks** 选项卡。在这里，在进行 commit 之后，您应该会看到一个正在运行的 check。

Select **Commit** at the upper right corner of the window to commit your changes to the `master` branch of your repository. To view your function's checks, open the **Checks** tab at the top of the page. Here, after making a commit, you should see a running check.

> 📷 **[图片: 选择该 check 以查看进度。]**

> 📷 **[图片: Select the check to view progress.]**

提交您的工作后，您将看到 **Tag version** 选项。这将发布您仓库中的所有 function。

After committing your work, you will see the **Tag version** option. This will publish all of the functions in your repository.
![The available tag options.](/docs/resources/foundry/functions/ts-functions-tags.png)
选择 **Tag version** 以从 `master` 分支标记一个发布版本 (release)。根据您更改的范围设置 tag 名称，然后选择 **Tag and release**。

Select **Tag version** to tag a release off of the `master` branch. Set the tag name based on the extent of your changes, and then select **Tag and release**.

> 📷 **[图片: 选择用于标记新发布版本的版本类型。]**

> 📷 **[图片: Choose the version type to tag for the new release.]**

要在 function 被标记和发布时查看进度，请选择 **View** 弹出窗口或导航到 **Tags** 选项卡。一旦 **Step 2: Release** 完成，请选择已发布的 function 以在 function registry 中查看它们。

To view the progress as your functions are tagged and released, select the **View** pop-up or navigate to the **Tags** tab. Once **Step 2: Release** is completed, select the published functions to view them in the function registry.
> **⚠️ 警告**

> 在权限传播完成之前，function 可能无法在 Workshop 或 function registry 中通过名称立即搜索到。
> **⚠️ 警告**

> Functions may not be immediately searchable by name in Workshop or the function registry while permissions propagate.
![Both the tag and release checks passed, and the new function is published.](/docs/resources/foundry/functions/tsv2-functions-tags-and-releases.png)
## Use a new function
在您 tag 的 checks 通过后，导航回 **Code Repositories** 中的 **Code** 选项卡，然后选择 **Functions** 辅助工具。您现在应该能够在 **Published** 部分下看到您的 function。选择它并运行新的 function：

After the checks for your tag have passed, navigate back to the **Code** tab in **Code Repositories** and select the **Functions** helper. You should now be able to see your functions under the **Published** section. Select it and run the new function:
![Run the new function in the functions helper.](/docs/resources/foundry/functions/tsv2-functions-helper-run.png)