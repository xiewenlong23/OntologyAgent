<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/typescript-v1-getting-started/
---
# Getting started with TypeScript v1 functions
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 Functions。有关更[强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2),包括对 Ontology SDK 和可配置资源请求的支持,我们建议[迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
## Create a TypeScript v1 functions repository
导航到您选择的项目,通过选择 **+ New > Repository** 创建一个新的代码仓库。选择 TypeScript Functions 模板来初始化您的仓库。

Navigate to a project of your choice and create a new code repository by selecting **+ New > Repository**. Select the TypeScript functions template to initialize your repository.
![Create a TypeScript v1 function code repository.](/docs/resources/foundry/functions/tsv1-functions-create-repo.png)
创建仓库后,导航到 `functions-typescript/src/index.ts` 文件。

Once the repository is created, navigate to the `functions-typescript/src/index.ts` file.
## Write a function
此仓库中的 Functions 必须在 TypeScript 类中定义,并且该类必须从 `functions-typescript/src/index.ts` 文件导出。您可以在 `index.ts` 中预填充的示例中编写您的 Function,或者创建一个新文件。如果您创建一个新文件,请确保从 `index.ts` 中导出您的类。

Functions in this repository must be defined within a TypeScript class, and that class must be exported from the `functions-typescript/src/index.ts` file. You can either write your function in the prepopulated examples in `index.ts`, or create a new file. If you create a new file, ensure that you export your class from `index.ts`.
以下是一个基本示例：

Below is a basic example:
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";

export class ExampleFunctions {

@Function()
public addIntegers(a: Integer, b: Integer): Integer {
return a + b;
}
}
```
如果上述代码写在名为 `exampleFunctions.ts` 的文件中,则必须从 index 文件中导出,如下所示：

If the above code is written in a file called `exampleFunctions.ts`, it must be exported from the index file as shown below:
```typescript tab="TypeScript v1"
// in functions-typescript/src/index.ts

export * from "./relative/path/to/exampleFunctions";
```
## Test in live preview
添加新 Function 后,您可以在 Functions 辅助工具中运行它。打开 **Functions** 辅助工具并选择 **Live Preview**。选择 `range` 函数,输入 input 值,然后选择 **Run** 来运行代码。

After you add the new function, you can run it in the functions helper. Open the **Functions** helper and select **Live Preview**. Choose the `range` function, enter input values, and select **Run** to run the code.
![Run your new function in the functions helper.](/docs/resources/foundry/functions/tsv1-functions-helper-preview-run.png)
选择右上角的 **Commit** 将您的更改提交到仓库的 `master` 分支。

Select **Commit** in the upper right to commit your changes onto the `master` branch of your repository.
## Publish a function
提交您的工作后,您将看到 **Tag version** 选项。这将发布您仓库中的所有 Functions。

After committing your work, you will see the **Tag version** option. This will publish all of the functions in your repository.
![The option to tag a branch with a new version.](/docs/resources/foundry/functions/ts-functions-tags.png)
选择 **Tag version** 从 `master` 分支标记一个发布版本。根据您的更改范围设置 tag 名称,然后选择 **Tag and release**。

Select **Tag version** to tag a release off the `master` branch. Set the tag name based on the extent of your changes, then choose **Tag and release**.

> 📷 **[图片: 选择要为新发布标记的版本类型。]**

> 📷 **[图片: Choose the version type to tag for the new release.]**

要查看 Function 在被打 tag 和发布过程中的进度,请选择 **View** 弹出菜单,或导航到 **Tags** 选项卡。**Step 2: Release** 完成后,选择已发布的 Function 以在 Function Registry 中查看它们。

To view the progress as your functions are tagged and released, select the **View** pop-up or navigate to the **Tags** tab. Once **Step 2: Release** is completed, select the published functions to view them in the function registry.
> **⚠️ 警告**

> 在权限传播过程中,Function 可能无法立即通过名称在 Workshop 或 Function Registry 中被搜索到。
> **⚠️ 警告**

> Functions may not be immediately searchable by name in Workshop or the function registry while permissions propagate.
![Both the tag and release checks passed, and the new function is published.](/docs/resources/foundry/functions/tsv1-functions-tags-and-releases.png)
## Use a new function
在 tag 的检查通过后,返回 **Code Repositories** 中的 **Code** 选项卡,选择 **Functions** helper。现在您应该可以在 **Published** 部分下看到您的新 `range` function。选择并运行该 Function。

After the checks for your tag have passed, navigate back to the **Code** tab in **Code Repositories** and select the **Functions** helper. You should now be able to see your new `range` function under the **Published** section. Select and run the function.
![Run the new function in the functions helper.](/docs/resources/foundry/functions/tsv1-functions-helper-run-2.png)
### Next steps
在本教程中,您学习了如何使用 Code Repositories 从一个 Repository 中编写、发布和测试 TypeScript v1 function。接下来,我们建议学习如何编写 [functions on objects](/docs/foundry/functions/foo-getting-started/)。

In this tutorial, you learned how to use Code Repositories to write, publish, and test a TypeScript v1 function from a repository. Next, we recommend learning how to author [functions on objects](/docs/foundry/functions/foo-getting-started/).