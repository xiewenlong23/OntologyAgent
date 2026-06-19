<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/platform-sdk/
---
# Use platform APIs with the Foundry platform SDK
Foundry APIs 提供了多种功能，您可以通过 functions 结合 [Foundry platform SDK](/docs/foundry/api/v2/general/overview/sdks/#foundry-platform-software-development-kits) 库加以利用。您可以使用 platform SDK 为管理或治理工作流构建 functions，与 schedules 和 builds 进行交互，访问 media sets 等。

Foundry APIs expose a variety of functionality that you can leverage with the [Foundry platform SDK](/docs/foundry/api/v2/general/overview/sdks/#foundry-platform-software-development-kits) library through functions. You can use the platform SDK to build functions for administrative or governance workflows, interact with schedules and builds, access media sets, and more.
> **⚠️ 警告**

> TypeScript v1 functions 不支持 First-class authentication。我们建议在这些工作流中使用 Python functions 和 TypeScript v2 functions。
> **⚠️ 警告**

> First-class authentication is not supported for TypeScript v1 functions. We recommend using Python functions and TypeScript v2 functions for these workflows.
## Install the SDK
若要安装 Foundry platform SDK，请导航至您代码仓库中的 **Libraries** 侧边栏，并搜索以下 SDK 名称：Python 对应 `foundry-platform-sdk`，TypeScript 对应 `@osdk/foundry`。

To install the Foundry platform SDK, navigate to the **Libraries** side panel in your code repository and search for the SDK name: `foundry-platform-sdk` for Python, or `@osdk/foundry` for TypeScript.

> 📷 **[图片: Libraries 搜索面板，正在搜索 Python platform SDK。]**

> 📷 **[图片: The Libraries search panel, searching for the Python platform SDK.]**

> 📷 **[图片: Libraries 搜索面板，正在搜索 TypeScript platform SDK。]**

> 📷 **[图片: The Libraries search panel, searching for the TypeScript platform SDK.]**

## Initialize your client
您的 function 需要进行身份验证才能与 Foundry APIs 交互。此过程涉及实例化一个经过身份验证的"client"，通过它您可以通过 SDK 向 Foundry APIs 发起请求。在 TypeScript v2 仓库中，这需要使用 `@osdk/client` 库，该库应已预先安装。您可以通过查找绿色图钉来验证这一点：

Your function requires authentication to interact with Foundry APIs. This process involves instantiating an authenticated “client” through which you can make requests to the Foundry APIs through the SDK. In TypeScript v2 repositories, this requires the `@osdk/client` library, which should be pre-installed. You can verify this by looking for the green pin:

> 📷 **[图片: The authentication library for TypeScript.]**

> 📷 **[图片: The authentication library for TypeScript.]**

## Use platform APIs
一旦你的 function 完成认证，就可以开始使用 Foundry APIs。以下示例展示了如何在 Python 和 TypeScript 中调用 language model 或查询 media sets：

Once your function is authenticated, you can start using Foundry APIs. The examples below show how to call a language model or query media sets in both Python and TypeScript:
```typescript tab="TypeScript v2"
import { Client } from "@osdk/client";
import { Functions } from "@osdk/foundry";

export default async function useLlm(
client: Client, // This parameter gets populated by Foundry at runtime
prompt: string
): Promise<string> {

const promptMessage = [
{
role: "USER",
content: prompt
}
];
const result = await Functions.Queries.execute(
client,
"com.foundry.languagemodelservice.models.gpt41.CreateChatCompletion",
{
parameters: {
messages: promptMessage
}
},
{
preview: true, // Required only for unstable endpoints, see API reference
}
);
return result.value["completion"] as string;
}
```
```python tab="Python"
from foundry_sdk import FoundryClient

@function
def media_item_to_base64(media_item_rid: str, media_set_rid: str) -> str:
foundry_client = FoundryClient()

result = foundry_client.media_sets.MediaSet.read(
media_set_rid=media_set_rid,
media_item_rid=media_item_rid,
preview=True  # Required only for unstable endpoints, see API reference
)

# Convert the binary stream to a base64 encoded string
base64_encoded = base64.b64encode(result).decode('utf-8')

return base64_encoded
```
### Client permissions
TypeScript v2 client（在运行时由 Foundry 传递给 function）和在代码中初始化的 Python client 具有以下 permissions scope：

The TypeScript v2 client (passed to the function by Foundry at runtime) and the Python client initialized in code have the following permissions scope:
* `api:admin-read`
* `api:functions-read`
* `api:ontologies-read`
* `api:orchestration-read`
* `api:usage:mediasets-read`
* `api:usage:ontologies-write`
* `api:admin-read`
* `api:functions-read`
* `api:ontologies-read`
* `api:orchestration-read`
* `api:usage:mediasets-read`
* `api:usage:ontologies-write`
每个 platform API endpoint 都需要特定的 scopes 才能访问该 endpoint。有关这些 scopes 的文档可在 [API reference](/docs/foundry/api/v2) 中找到

Each platform API endpoint requires certain scopes to hit the endpoint. Documentation on these scopes can be found in the [API reference](/docs/foundry/api/v2)