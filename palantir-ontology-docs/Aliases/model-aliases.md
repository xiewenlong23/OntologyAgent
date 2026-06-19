<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/model-aliases/
---
# Model aliases
Model alias 是对语言模型的命名引用，提供了一种在代码中引用语言模型的便捷方式。

Model aliases are named references to language models that provide a convenient way to reference language models in code.
有关在 function 中使用语言模型的完整演练，请参阅 [TypeScript v2 和 Python functions 中的语言模型](/docs/foundry/functions/language-models-python-tsv2/)。

For a full walkthrough of using language models in functions, see [Language models in TypeScript v2 and Python functions](/docs/foundry/functions/language-models-python-tsv2/).
## Define a model alias
要定义 model alias，请打开 TypeScript v2 或 Python 代码仓库，并按照以下步骤操作：

To define a model alias, open a TypeScript v2 or Python code repository and follow the steps below:
1. 在 **Resource imports** 面板中打开 **Platform SDK** 选项卡。

1. Open the **Platform SDK** tab in the **Resource imports** panel.
![The tab to access Platform SDK resources in a TypeScript v2 repository.](/docs/resources/foundry/functions/platform-sdk-tab.png)
2. 要导入新的语言模型，请选择右上角的 **Add > Models**。将打开一个窗口，您可以在其中查看 Palantir 提供的和已注册的可用模型。

2. To import a new language model, select **Add > Models** in the upper right corner. A window will open in which you can view available Palantir-provided and registered models.
![The model import dialog in a TypeScript v2 repository.](/docs/resources/foundry/functions/models-v3-import-dialog.png)
3. 选择要导入的模型，然后选择 **Confirm selection**。将打开一个配置对话框，您可以在其中为每个选定的模型配置 alias。选择 alias 附近的笔图标进行编辑，或选择保留默认值。

3. Select the models to import, then choose **Confirm selection**. A configuration dialog will open in which you can configure aliases for each selected model. Select the pen icon near the alias to make edits, or choose to keep the defaults.
> **ℹ️ 注意**

> Alias 键在仓库内必须唯一。
> **ℹ️ 注意**

> Alias keys must be unique within the repository.
![Configure model aliases after choosing models to import.](/docs/resources/foundry/functions/configure-models-aliases.png)
4. 导入的模型将出现在 **Resource imports** 侧边栏的 **Platform SDK** 选项卡中。您可以通过选择 alias 旁边的笔图标来内联编辑任何 alias。

4. The imported models will appear in the **Platform SDK** tab in the **Resource imports** side panel. You can edit any alias inline by selecting the pen icon next to the alias.
![Configure model aliases inline.](/docs/resources/foundry/functions/inline-models-aliases-edit.png)
## Use a model alias in code
要在 function 中使用 model alias，请导入 alias 工具并按名称引用该 alias。该 alias 将解析为一个 model RID，您可以将其传递给 model client：

To use a model alias in your function, import the alias utility and reference the alias by name. The alias resolves to a model RID that you can pass to a model client:
```typescript tab="TypeScript v2"
import { Aliases } from "@osdk/functions";

const modelRid = Aliases.model("gpt5Nano").rid;
```
```python tab="Python"
from functions.aliases import model

model_rid = model("gpt5Nano").rid
```
有关使用 alias 调用语言模型的完整示例，请参阅 [编写使用语言模型的 function](/docs/foundry/functions/language-models-python-tsv2/#write-a-function-that-uses-a-language-model)。

For a complete example of calling a language model using an alias, see [Write a function that uses a language model](/docs/foundry/functions/language-models-python-tsv2/#write-a-function-that-uses-a-language-model).
> **⚠️ 警告**

> Model alias 在添加到 [Marketplace products](/docs/foundry/functions/marketplace-functions/) 的 function 中有效，但在安装过程中无法重新映射。如果 alias 引用的模型在目标环境中不可用，则该 function 在运行时将无法解析该 alias。
> **⚠️ 警告**

> Model aliases work in functions added to [Marketplace products](/docs/foundry/functions/marketplace-functions/), but cannot be remapped during installation. If the model referenced by an alias is not available in the target environment, the function will fail to resolve the alias at runtime.