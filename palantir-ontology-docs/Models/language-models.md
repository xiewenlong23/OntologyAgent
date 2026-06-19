<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/language-models/
---
# Language models in TypeScript v1 functions
> **⚠️ 警告**

> 以下文档专门针对 TypeScript v1 函数。对于更[强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2),包括对 Ontology SDK 和可配置资源请求的支持,我们建议[migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
> **ℹ️ 注意: Prerequisites**

> 要使用 Palantir 提供的语言模型,必须先[在您的 enrollment 上启用 AIP](/docs/foundry/aip/enable-aip-features/)。您还必须拥有使用 [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities) 的权限。
> **ℹ️ 注意: Prerequisites**

> To use Palantir-provided language models, [AIP must first be enabled on your enrollment](/docs/foundry/aip/enable-aip-features/). You must also have permissions to use [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities).
Palantir 提供了一组可在函数中使用的语言模型。[了解更多关于 Palantir 提供的 LLM](/docs/foundry/aip/supported-llms/) 的信息。

Palantir provides a set of language models which can be used within functions. [Read more about Palantir-provided LLMs](/docs/foundry/aip/supported-llms/).
## Import a language model
要开始使用语言模型,你必须按照以下步骤将特定模型导入到正在编写函数的代码仓库中:

To begin using a language model, you must import the specific model into the code repository where you are writing your functions by following the steps below:
1. 导航并打开 **Model Imports** 侧边面板,以查看所有已导入的模型。

1. Navigate and open the **Model Imports** side panel to see all existing imported models.

> 📷 **[图片: Model import sidebar.]**

> 📷 **[图片: Model import sidebar.]**

2. 要导入新的语言模型，请在 **Resource Imports** 面板的右上角选择 **Add**，然后选择 **Models**。这将打开一个新窗口，您可以在其中查看 Palantir 提供的可用模型。

2. To import a new language model, select **Add** in the upper right corner of the **Resource Imports** panel, then select **Models**. This will open a new window where you will be able to see Palantir-provided models that are available to you.

> 📷 **[图片: Model import dialog showing a few Palantir-provided LLMs.]**

> 📷 **[图片: Model import dialog showing a few Palantir-provided LLMs.]**

3. 您还会看到一个标签页，可以查看通过 Modeling Objectives 应用程序或先前直接部署的自定义模型。有关使用这些模型的更多信息，请参阅 [functions on models](/docs/foundry/functions/functions-on-models/) 文档。

3. You will also see a tab where you can view custom models created through the Modeling Objectives application or direct model deployments previously. More information on using those models can be found in the [functions on models](/docs/foundry/functions/functions-on-models/) documentation.
4. 选择您要导入的模型，然后选择 **Confirm selection** 将这些模型导入到您的 repository 中。Task runner 将执行 `localDev` 任务，生成与这些模型交互的代码绑定。

4. Choose the models you would like to import, then select **Confirm selection** to import these models into your repository. Task runner will execute the `localDev` task, generating code bindings to interact with these models.
5. 导入语言模型后，在侧边栏中选择该模型以查看该模型提供的详细功能。您还可以复制代码片段，以帮助您使用该模型导入和编写 functions。

5. After importing the language models, select the model in the sidebar to view the detailed capabilities offered by this model. You can also copy code snippets to help you import and author functions with the model.

> 📷 **[图片: Model details in sidebar.]**

> 📷 **[图片: Model details in sidebar.]**

## Write a function that uses a language model
在此阶段，您现在可以编写一个使用您导入的语言模型的 function。在本示例中，假设您导入了 GPT-4.1。

At this stage, you can now write a function that uses the language model you imported. For this example, assume that you imported GPT-4.1.
首先，将以下 import 语句添加到您的文件中：

Begin by adding the following import statement to your file:
```typescript
import { Function } from "@foundry/functions-api";
import { Gpt41 } from "@foundry/languagemodelservice/models";
```
每个语言模型都将生成具有强类型输入和输出的可用方法。例如，GPT-4.1 模型提供 `createChatCompletion`、`createChatVisionCompletion` 和 `createChatCompletionStreamed` 作为与模型交互的不同 API。可用功能列表可能会在导入模型的更高版本中扩展。

Each language model will have generated methods available with strongly typed inputs and outputs. For example, the GPT-4.1 model provides `createChatCompletion`, `createChatVisionCompletion`, and `createChatCompletionStreamed` as different APIs to interact with the model. The list of capabilities could expand in later versions of the imported model.
在以下示例中，提供的 GPT\_4o 模型用于对用户提供的文本或图像运行简单的情感分析。该 function 将文本分类为 "Good"、"Bad" 或 "Uncertain"。

In the following illustrative example, the provided GPT\_4o model is used to run a simple sentiment analysis on a piece of text or image provided by a user. The function will classify the text as "Good", "Bad", or "Uncertain".
```typescript

const SYSTEM_PROMPT =
"Provide an estimation of the sentiment the text the user has provided. \
You may respond with either Good, Bad, or Uncertain. Only choose Good or Bad if you are overwhelmingly \
sure that the text is either good or bad. If the text is neutral, or you are unable to determine, choose Uncertain.";

export class MyFunctions {
@Function()
public async llmFunction_createChatCompletion(userPrompt: string): Promise<string | undefined> {
const response = await Gpt41.createChatCompletion({
messages: [
{
role: "SYSTEM",
content: SYSTEM_PROMPT,
},
{
role: "USER",
content: userPrompt,
},
],
params: {
temperature: 0,
},
});
return response.type === "ok" ? response.value.completion : "error";
}

@Function()
public async llmFunction_createChatVisionCompletion(
userPrompt: string,
pngBase64String: string,
): Promise<string | undefined> {
const response = await Gpt41.createChatVisionCompletion({
messages: [
{
role: "USER",
content: [
{ type: "text", text: userPrompt },
{
type: "genericMedia",
genericMedia: {
mimeType: "IMAGE_PNG",
// Base64 encoded PNG String
content: pngBase64String,
},
},
],
},
],
params: {
temperature: 0,
},
});
return response.type === "ok" ? response.value.completion : "error";
}
}
```
此 function 随后可在整个平台中使用。

This function can then be used throughout the platform.
## Embeddings
除了生成式语言模型外，Palantir 还提供可用于生成 embeddings 的模型。一个简单的示例如下：

Along with generative language models, Palantir also provides models that can be used to generate embeddings. A simple example is as follows:
```typescript
@Function()
public async llmFunction_embeddings(inputs: string[]): Promise<Double[][]> {
const response = await Textembedding3large.createEmbeddings({ inputs });
return response.type === "ok" ? response.value.embeddings : [[]];
}
```
这最常用于执行 [semantic search](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) 工作流。

This is most commonly used to perform [semantic search](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) workflows.
## Upgrade from legacy language models within functions
> **ℹ️ 注意**

> 如果您是从一个没有导入任何 [legacy language models](/docs/foundry/functions/language-models-legacy/) 的新 repository 开始的，请跳过此步骤。
> **ℹ️ 注意**

> Skip this step if you are starting from a new repository with no [legacy language models](/docs/foundry/functions/language-models-legacy/) imported.
> **⚠️ 警告**

> 以下流程将导致您的代码仓库在编译时中断，因为代码语法将被更新。请参考侧边栏中每个更新模型的代码片段来更新您的代码。
> **⚠️ 警告**

> The following process will result in a compile-time break in your code repository, as the code syntax will be updated. Refer to the code snippets in the sidebar for each updated model to update your code.
Functions 中更新后的语言模型提供了更高级的功能，例如对视觉和流式传输的更好支持。我们强烈建议升级您的仓库，以利用最新的 AIP  offerings。

The updated language models in functions offer more advanced capabilities, such as better support for vision and streaming. We highly recommend upgrading your repository to take advantage of the latest AIP offerings.
1. 如果您已导入现有的 [legacy language models](/docs/foundry/functions/language-models-legacy/)，侧边栏中会出现一个升级警告图标。选择 **Select imports** 以打开模型导入对话框。

1. If you have existing [legacy language models](/docs/foundry/functions/language-models-legacy/) imported, a warning icon to upgrade will appear in the sidebar. Choose **Select imports** to open the model import dialog.

> 📷 **[图片: Model imports warning in sidebar.]**

> 📷 **[图片: Model imports warning in sidebar.]**

2. 在模型导入对话框中，选择 **Fix** 以移除任何已弃用的 legacy language models。

2. In the model import dialog, select **Fix** to remove any deprecated legacy language models.

> 📷 **[图片: Model import dialog with warning.]**

> 📷 **[图片: Model import dialog with warning.]**

3. 重新选择要迁移到更新后语言模型版本的模型。您可以在对话框中央的详细信息面板中查看此版本支持的附加功能。

3. Reselect the models to migrate to the updated language model versions. You can view additional capabilities supported by this version in the details panel in the center of the dialog.

> 📷 **[图片: Model import dialog shows removed models.]**

> 📷 **[图片: Model import dialog shows removed models.]**

4. 现在，您可以在侧边栏中查看更新后的模型导入。选择一个模型将显示一个包含代码片段的详细信息面板，以帮助您更新代码，从而利用附加功能。

4. Now, you can view the updated model imports in the sidebar. Selecting a model will show you a details panel with code snippets to help you update your code to take advantage of the additional capabilities.

> 📷 **[图片: Model details and code snippet in sidebar.]**

> 📷 **[图片: Model details and code snippet in sidebar.]**

## Performance considerations
某些模型可能会应用 rate limits，限制在特定时间段内可以传递的 tokens 数量。这将与适用于 functions 的任何标准限制一起强制执行。

Certain models may have rate limits applied, limiting the number of tokens that may be passed over a certain time period. This will be enforced along with any standard limits that apply to functions.
***
注意：AIP 功能的可用性可能会发生变化，并且可能因客户而异。

Note: AIP feature availability is subject to change and may differ between customers.