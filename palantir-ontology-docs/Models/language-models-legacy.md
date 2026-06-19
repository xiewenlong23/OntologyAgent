<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/language-models-legacy/
---
# Legacy language models within functions
> **🚨 危险: Legacy**

> 这是关于 functions 中 **legacy** 语言模型的文档。[Functions 中更新后的语言模型](/docs/foundry/functions/language-models-python-tsv2/) 提供了更强大的功能，例如视觉和流式传输。[升级您在 functions 中的语言模型](/docs/foundry/functions/language-models/#upgrade-from-legacy-language-models-within-functions) 以利用最新的 AIP offerings。
> **🚨 危险: Legacy**

> This is documentation for the **legacy** language models within functions. The [updated language models in functions](/docs/foundry/functions/language-models-python-tsv2/) offer more robust capabilities, such as vision and streaming. [Upgrade your language models in functions](/docs/foundry/functions/language-models/#upgrade-from-legacy-language-models-within-functions) to take advantage of the latest AIP offerings.
Palantir 提供了一组可在 functions 中使用的语言模型。[详细了解 Palantir 提供的 LLMs](/docs/foundry/aip/supported-llms/)。

Palantir provides a set of language models which can be used within functions. [Read more about Palantir-provided LLMs](/docs/foundry/aip/supported-llms/).
> **ℹ️ 注意: Prerequisites**

> 要使用 Palantir 提供的语言模型，[必须首先在您的 enrollment 上启用 AIP](/docs/foundry/aip/enable-aip-features/)。您还必须拥有使用 [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities) 的权限。
> **ℹ️ 注意: Prerequisites**

> To use Palantir-provided language models, [AIP must first be enabled on your enrollment](/docs/foundry/aip/enable-aip-features/). You also must have permissions to use [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities).
## Import a language model
要开始使用语言模型，您必须按照以下步骤将特定模型导入到您编写 Function 的代码仓库中：

To begin using a language model, you must import the specific model into the code repository where you are writing your functions by following the steps below:
1. 导航并打开 **Model Imports** 侧边栏，以查看所有已导入的现有模型。

1. Navigate and open the **Model Imports** side panel to view all existing imported models.

> 📷 **[图片: Model import sidebar.]**

> 📷 **[图片: Model import sidebar.]**

2. 要导入新的语言模型，请在 **Resource Imports** 面板的右上角选择 **Add**，然后选择 **Models**。这将打开一个新窗口，您可以在其中查看可供使用的 Palantir 提供的模型。

2. To import a new language model, select **Add** in the top-right corner of the **Resource Imports** panel and select **Models**. This will open a new window where you will be able to view the Palantir-provided models that are available to you.

> 📷 **[图片: Model import dialog showing a few Palantir-provided LLMs.]**

> 📷 **[图片: Model import dialog showing a few Palantir-provided LLMs.]**

3. 您还将看到一个标签页，您可以在其中查看通过 Modeling Objectives 应用程序或先前的直接模型部署创建的自定义模型。有关使用这些模型的更多信息，请参阅 [functions on models](/docs/foundry/functions/functions-on-models/) 文档。

3. You will also see a tab where you can view custom models which have been created through the Modeling Objectives app or direct model deployments previously. More information on using those models can be found in the [functions on models](/docs/foundry/functions/functions-on-models/) documentation.
4. 选择您要导入的模型，然后选择 **Confirm selection** 以将这些模型导入到您的仓库中。Task runner 将执行 `localDev` 任务，生成与这些模型交互的代码绑定。

4. Select the models you would like to import, then select **Confirm selection** to import these models into your repository. Task runner will execute the `localDev` task, generating code bindings to interact with these models.
5. 导入语言模型后，您现在可以通过添加以下 import 语句在仓库中使用它们，请将 GPT\_4o 替换为您已导入仓库的语言模型的名称：

5. After importing the language models, you can now use them in your repository by adding the following import statement, replacing GPT\_4o with the name of the language model you have imported into your repository:
```typescript
import { GPT_4o } from "@foundry/models-api/language-models"
```
## Writing a function that uses a language model
在此阶段，我们现在可以编写一个使用我们导入的语言模型的 Function。对于本示例，我们假设已如上所述导入了 GPT\_4o。

At this stage, we can now write a function that uses a language model we imported. For this example, we assume that we have imported GPT\_4o as described above.
我们首先向文件中添加以下 import 语句：

We begin by adding the following import statement to our file:
```typescript
import { GPT_4o } from "@foundry/models-api/language-models"
```
每个语言模型都将生成具有强类型输入和输出的可用方法。例如，GPT\_4o 模型提供了一个 createChatCompletion 方法，允许用户传递一组消息以及额外的参数来修改模型的行为，例如 temperature 或最大 token 数。

Each language model will have generated methods available with strongly typed inputs and outputs. For example, the GPT\_4o model provides a createChatCompletion method which allows the user to pass a set of messages along with additional parameters to modify the model’s behavior, such as the temperature or maximum number of tokens.
在以下示例中，我们使用提供的 GPT\_4o 模型对用户提供的一段文本运行简单的情感分析。该 Function 将把文本分类为"Good"（良好）、"Bad"（糟糕）或"Uncertain"（不确定）。

In the following illustrative example, we use the provided GPT\_4o model to run a simple sentiment analysis on a piece of text provided by a user. The function will classify the text as "Good", "Bad", or "Uncertain".
```typescript
@Function()
public async sentimentAnalysis(userPrompt: string): Promise<string> {
const systemPrompt = "Provide an estimation of the sentiment the text the user has provided. \
You may respond with either Good, Bad, or Uncertain. Only choose Good or Bad if you are overwhelmingly \
sure that the text is either good or bad. If the text is neutral, or you are unable to determine, choose Uncertain."

const systemMessage = { role: "SYSTEM", contents: [{ text: systemPrompt }] };
const userMessage = { role: "USER", contents: [{ text: userPrompt }] };
const gptResponse = await GPT_4o.createChatCompletion({messages: [systemMessage, userMessage], params: { temperature: 0.7 } });
return gptResponse.choices[0].message.content ?? "Uncertain";
}
```
然后可以在整个平台中使用此 Function。

This function can then be used throughout the platform.
## Embeddings
除了生成式语言模型外，Palantir 还提供可用于生成 embeddings 的模型。一个简单的示例如下：

Along with generative language models, Palantir also provides models which can be used to generate embeddings. A simple example is as follows:
```typescript
@Function()
public async generateEmbeddingsForText(inputs: string[]): Promise<Double[][]> {
const response = await TextEmbeddingAda_002.createEmbeddings({ inputs });
return response.embeddings;
}
```
这最常用于执行 [semantic search](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) 工作流。

This is most commonly used to perform [semantic search](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) workflows.
## Performance considerations
某些模型可能会应用速率限制，限制在特定时间段内可以传递的 token 数量。此限制将与适用于 functions 的任何标准限制一起执行。

Certain models may have rate limits applied to them, limiting the number of tokens which may be passed over a certain time period. This will be enforced along with any standard limits that apply to functions.
***
注意：AIP 功能可用性可能会有变化，并且可能因客户而异。

Note: AIP feature availability is subject to change and may differ between customers.