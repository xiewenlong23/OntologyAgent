<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/language-models-python-tsv2/
---
# Language models in TypeScript v2 and Python functions
> **ℹ️ 注意: Prerequisites**

> 要使用 Palantir 提供的语言模型，必须[在您的 enrollment 上启用 AIP](/docs/foundry/aip/enable-aip-features/)。您还必须拥有使用 [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities) 的权限。
> **ℹ️ 注意: Prerequisites**

> To use Palantir-provided language models, [AIP must be enabled on your enrollment](/docs/foundry/aip/enable-aip-features/). You must also have permissions to use [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities).
Palantir 提供了一组可在 functions 中使用的语言模型。[了解更多关于 Palantir 提供的 LLMs](/docs/foundry/aip/supported-llms/)。

Palantir provides a set of language models that can be used within functions. [Learn more about Palantir-provided LLMs](/docs/foundry/aip/supported-llms/).
## Import a language model
要开始使用语言模型，您必须按照以下步骤将特定模型导入到您的 functions 代码仓库中：

To begin using a language model, you must import the specific model into your functions code repository by following the steps below:
1. 在 **Resource imports** 面板中打开 **Platform SDK** 选项卡。

1. Open the **Platform SDK** tab in the **Resource imports** panel.
![The tab to access Platform SDK resources in a TypeScript v2 repository.](/docs/resources/foundry/functions/platform-sdk-tab.png)
2. 要导入新的语言模型，请在右上角选择 **Add > Models**。将会打开一个窗口，您可以在其中查看可用的 Palantir 提供和已注册的模型。

2. To import a new language model, select **Add > Models** in the upper right corner. A window will open in which you can view available Palantir-provided and registered models.
![The model import dialog in a TypeScript v2 repository.](/docs/resources/foundry/functions/models-v3-import-dialog.png)
3. 选择要导入的模型，然后选择 **Confirm selection**。将会打开一个配置对话框，您可以在其中为每个选定的模型配置 alias。选择 alias 附近的笔图标进行编辑，或选择保留默认值。

3. Select the models to import, then choose **Confirm selection**. A configuration dialog will open in which you can configure aliases for each selected model. Select the pen icon near the alias to make edits, or choose to keep the defaults.
> **⚠️ 警告**

> 每个模型都必须有一个 alias，并且该 alias 在仓库中必须唯一。
> **⚠️ 警告**

> Each model must have an alias, and the alias must be unique within the repository.
![Configure model aliases after choosing models to import.](/docs/resources/foundry/functions/configure-models-aliases.png)
4. 导入的模型将出现在 **Resource imports** 侧边面板的 **Platform SDK** 选项卡中。您可以通过选择 alias 旁边的笔图标来内联编辑任何 alias。

4. The imported models will appear in the **Platform SDK** tab in the **Resource imports** side panel. You can edit any alias inline by selecting the pen icon next to the alias.
![Configure model aliases inline.](/docs/resources/foundry/functions/inline-models-aliases-edit.png)
## Write a function that uses a language model
TypeScript v2 和 Python functions 中的语言模型使用 proxy endpoints 与模型进行交互。以下示例使用 [OpenAI chat completion proxy endpoint](/docs/foundry/api/v2/llm-apis/models/openai-chat-completions-proxy/)。您可以从文档侧边面板中选择其他 providers。

Language models in TypeScript v2 and Python functions use proxy endpoints to interact with models. The following example uses the [OpenAI chat completion proxy endpoint](/docs/foundry/api/v2/llm-apis/models/openai-chat-completions-proxy/). You can select other providers from the documentation side panel.
> **ℹ️ 注意**

> 第三方库（例如以下示例中的 `openai`）未预安装。请从左侧面板的 **Libraries** 部分安装它们。
> **ℹ️ 注意**

> Third-party libraries, such as `openai` in the example below, are not pre-installed. Install them from the **Libraries** section of the left side panel.
要在您的 function 中使用导入的语言模型，首先导入必要的 utilities：

To use an imported language model in your function, begin by importing the necessary utilities:
```typescript tab="TypeScript v2"
import { PlatformClient } from "@osdk/client";
import OpenAI from "openai";
import { Aliases } from "@osdk/functions";
import { getFoundryToken, getOpenAiBaseUrl, createFetch } from "@osdk/language-models";
```
```python tab="Python"
from openai import OpenAI
from functions.api import function
from functions.aliases import model
from foundry_sdk.v2.language_models import (
get_openai_base_url,
get_foundry_token,
get_http_client,
)
```
使用您配置的 model aliases 以及导入的 utilities 直接调用模型。这种方法比 TypeScript v1 workflow 更简单，并减少了对硬编码 resource identifiers 的需求。

Directly call the model using the model aliases you configured along with the imported utilities. This approach is simpler than the TypeScript v1 workflow and reduces the need to hardcode resource identifiers.
```typescript tab="TypeScript v2"
export default async function callOpenAi(client: PlatformClient, prompt: string): Promise<string> {
const oaiClient = new OpenAI({
apiKey: await getFoundryToken(client),
baseURL: getOpenAiBaseUrl(client),
fetch: createFetch(client),
});

const completion = await oaiClient.chat.completions.create({
model: Aliases.model("{MY_ALIAS}").rid,
messages: [
{ role: 'user', content: prompt },
],
reasoning_effort: "minimal",
max_completion_tokens: 200,
});

return completion.choices[0]?.message.content ?? "";
}
```
```python tab="Python"
@function
def get_chat_completion(prompt: str) -> str:
client = OpenAI(
api_key=get_foundry_token(preview=True),
base_url=get_openai_base_url(preview=True),
http_client=get_http_client(preview=True),
)

completion = client.chat.completions.create(
model=model("{MY_ALIAS}").rid,
messages=[
{
"role": "user",
"content": prompt,
},
],
)

return str(completion.choices[0].message.content)
```