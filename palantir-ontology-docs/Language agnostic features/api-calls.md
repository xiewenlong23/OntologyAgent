<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/api-calls/
---
# Make API calls from functions
可以从 TypeScript v1、TypeScript v2 和 Python function 中对外部源进行 API 调用，但这样做需要额外的配置。下文将详细介绍此配置和外部源的使用方法。

It is possible to make API calls to external sources from TypeScript v1, TypeScript v2 and Python functions, but doing so requires additional configuration. This configuration and external source usage are detailed below.
## Configure access to external APIs
默认情况下，不允许 function 调用外部 API。要启用从您的 function 调用外部系统，您必须在 [Data Connection](/docs/foundry/data-connection/overview/) 中 [配置一个 source](/docs/foundry/data-connection/set-up-source/)，以允许 Foundry 与外部系统连接。

By default, functions are not allowed to call external APIs. To enable calling external systems from your function, you must [configure a source](/docs/foundry/data-connection/set-up-source/) in [Data Connection](/docs/foundry/data-connection/overview/) to allow Foundry to connect with an external system.
为了使 function 能够安全地连接到您 source 的外部系统，您的 source 必须配置为 [启用 export](/docs/foundry/data-connection/export-overview/#enable-exports-for-source)，并允许 [将您的 source 导入到 Code Repositories](/docs/foundry/data-connection/external-transforms/#prerequisite-import-a-source-into-code)。可以通过在 Data Connection 中导航到该 source 并打开 **Connection settings** 部分来配置这两项。在那里您可以找到 **Code import configuration** 选项卡，如果您的 source 还没有 API name，您还可以在此处进行配置。此 API name 将用于在代码中引用您的 source。

For functions to connect to your source's external system securely, your source must be configured to [enable exports](/docs/foundry/data-connection/export-overview/#enable-exports-for-source) and allow the [import of your source into Code Repositories](/docs/foundry/data-connection/external-transforms/#prerequisite-import-a-source-into-code). Both of these can be configured by navigating to the source in Data Connection and opening the **Connection settings** section. Here you will find the **Code import configuration** tab, where you can also configure an API name if your source does not yet have one. This API name will be used to reference your source in code.
> **ℹ️ 注意**

> 请确保在您的 source 中完整配置证书链。
> Webhook 和 function 的运行时环境并不完全相同。
> 有时，webhook 可以正常工作，而来自 function 的 API 调用可能会遇到 `UNABLE_TO_GET_ISSUER_CERT` 错误。
> 请参考我们关于 [source 终端中 `openssl` 命令](/docs/foundry/data-connection/troubleshooting/#openssl) 的文档以验证证书。
> **ℹ️ 注意**

> Make sure to fully configure the certificate chain in your source.
> Webhook and function runtime environments are not identical.
> Sometimes, a webhook will work correctly while the API call from a function might encounter an `UNABLE_TO_GET_ISSUER_CERT` error.
> Refer to our documentation on the [`openssl` command in the source terminal](/docs/foundry/data-connection/troubleshooting/#openssl) to verify certificates.
## Use an external source in a function
要从 function 进行 API 调用，您必须首先在 function 仓库中使用 [resource imports 侧边栏](/docs/foundry/functions/resource-imports-sidebar/) 导入您的 source。然后您必须声明您的 function 正在使用该 source。

To make API calls from a function, you must first import your source using the [resource imports sidebar](/docs/foundry/functions/resource-imports-sidebar/) in a functions repository. You must then declare that your function uses the source.
示例如下所示：

Examples of this are shown below:
```typescript tab="TypeScript v1"
import { ExternalSystems } from "@foundry/functions-api";
import { MySource } from "@foundry/external-systems/sources";

export class MyExternalFunctions {
@ExternalSystems({ sources: [MySource] })
@Function()
public async myExternalFunction(): Promise<string> {
const { url } = MySource.getHttpsConnection();
const response = await MySource.fetch(url);

return response.text();
}
}
```
```typescript tab="TypeScript v2"
import { getSource, getHttpsConnection, getFetch } from "@palantir/functions-sources";

export const config = {
sources: ["MySource"]
}

async function MyExternalFunction(): Promise<string> {
const source = await getSource("MySource");
const { url } = getHttpsConnection(source);
const fetch = await getFetch(source);

const response = await fetch(url);

return response.text();
}
```
```python tab="Python"
from functions.api import function
from functions.sources import get_source

@function(sources=["MySource"])
def my_external_function() -> str:
source = get_source("MySource")
url = source.get_https_connection().url
client = source.get_https_connection().get_client()
response = client.get(url)
return response.text
```
您可以在实时预览中测试您的 function，并在发布后使用它进行外部调用。

You can test your function in live preview and use it to make external calls once published.
> **⚠️ 警告**

> **第三方客户端尚不支持无服务器执行或实时预览，除非覆盖 fetch function 或 HTTP agent。** 为确保您的 API 调用在所有环境中正常运行，您必须使用相关的 library 方法以正确的配置发出请求。在所有环境中，直接对外部源或内部 Foundry URL 的 API 调用不保证有效。
> **⚠️ 警告**

> **Third-party clients are not yet supported for serverless execution or live preview without overriding the fetch function or HTTP agent.** To ensure your API calls function properly across all environments, you must use the relevant library methods to make requests with the correct configuration. Direct API calls to external sources or internal Foundry URLs are not guaranteed to work in all environments.
## Access source attributes and credentials
您可以访问由每种 function 类型对应的 library 提供的 source 属性。

You can access source attributes provided by each function type's corresponding library.
下面的示例展示了如何在上面的示例中获取 source 的基本 URL。

The example below shows how to obtain the base URL of the source in the example above.
```typescript tab="TypeScript v1"
const { url } = MySource.getHttpsConnection();
```
```typescript tab="TypeScript v2"
const { url } = getHttpsConnection(source);
```
```python tab="Python"
url = get_source("MySource").get_https_connection().url
```
您还可以使用以下语法访问源上存储的其他 secrets 或 credentials：

You can also access additional secrets or credentials stored on the source by using the following syntax to access secrets:
```typescript tab="TypeScript v1"
const secret = MySource.getSecret("MySecret");
```
```typescript tab="TypeScript v2"
const secret = source.secrets["MySecret"];
```
```python tab="Python"
secret = get_source("MySource").get_secret("MySecret")
```
## Use the pre-configured clients
对于提供 REST API 的源，源对象允许您检索一个 client。该 client 将使用源上指定的 server 和 client certificates 进行预配置。它还将包含额外的 proxy configurations，允许从执行 functions 的环境中进行 egress。如果可能，您应始终使用此 client，以确保您的 function 能够从所有环境中 egress 到源。

For sources that provide a REST API, the source object allows you to retrieve a client. This client will be pre-configured with the server and client certificates specified on the source. It will also include additional proxy configurations which allow egress from the environment functions are executed in. You should always use this client, if possible, to guarantee your function can egress to the source from all environments.
```typescript tab="TypeScript v1"
const fetch = MySource.fetch;
```
```typescript tab="TypeScript v2"
const fetch = await getFetch(source);
```
```python tab="Python"
client = source.get_https_connection().get_client()
```
或者，您可以使用自己的 client 或发出外部请求的第三方库，并使用源对象来 [retrieve attributes and credentials](#access-source-attributes-and-credentials)。

Alternatively, you can use your own client or third-party libraries which make external requests, and use the source object to [retrieve attributes and credentials](#access-source-attributes-and-credentials).
TypeScript v2 functions 提供了一个预配置的 HTTP agent，作为与接受自定义 HTTP agent 的第三方库一起使用的额外集成点。

TypeScript v2 functions provide a pre-configured HTTP agent as an additional integration point for usage with third party libraries which accept a custom HTTP agent.
以下示例演示了如何检索此 agent 并将其与 [axios ↗](https://github.com/axios/axios) 一起使用。

The following example demonstrates retrieving this agent and using it with [axios ↗](https://github.com/axios/axios).
```typescript tab="TypeScript v2"
import { getHttpAgent, getHttpsConnection } from "@palantir/functions-sources";
import axios from 'axios';

const agent = await getHttpAgent(source);
const { url } = getHttpsConnection(source);

const response = await axios.get(url, {
httpsAgent: agent,
});

```
> **ℹ️ 注意**

> 目前，除非源提供 HTTPS client，否则无法访问非 credentials 的源 attributes。例如，您将无法访问 [PostgreSQL source](/docs/foundry/available-connectors/postgresql/) 上的 `hostname` 或其他非 secret attributes。
> **ℹ️ 注意**

> Currently, it is impossible to access source attributes that are not credentials unless the source provides an HTTPS client. For example, you will not be able to access the `hostname` or other non-secret attributes on a [PostgreSQL source](/docs/foundry/available-connectors/postgresql/).
## Use OAuth 2.0 with outbound applications
如果您的外部 API 需要 OAuth 2.0 authorization，您可以在 Control Panel 中配置一个 [outbound application](/docs/foundry/administration/configure-outbound-applications/)，并将其用作 REST API source 的 authentication method。当您的 function 运行时，源会将调用用户的 OAuth access token 公开为 session credentials。然后，您的 function 可以使用该 token 代表用户调用外部 API。

If your external API requires OAuth 2.0 authorization, you can configure an [outbound application](/docs/foundry/administration/configure-outbound-applications/) in Control Panel and use it as the authentication method for a REST API source. When your function runs, the source exposes the calling user's OAuth access token as session credentials. Your function can then use the token to call the external API on the user's behalf.
此模式在 Python 和 TypeScript v2 functions 中受支持。有关代码示例，请参阅下面的 [Use the source's pre-configured client](#use-the-sources-pre-configured-client)。

This pattern is supported in Python and TypeScript v2 functions. See [Use the source's pre-configured client](#use-the-sources-pre-configured-client) below for code examples.
### Limitations
* **TypeScript v1：** TypeScript v1 functions 无法直接从源中检索 OAuth tokens。要从 TypeScript v1 function 中通过 OAuth 2.0 API 进行身份验证，请在配置了 outbound application 的 REST API source 上的 [webhook](/docs/foundry/functions/webhooks/) 中包装该调用。请考虑 [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/) 以获得直接的 token 访问。

* **Deployed mode：** 当 function 在 [deployed mode](/docs/foundry/functions/functions-deployed/) 下运行时，OAuth token 刷新不可用。如果调用用户的 access token 在执行期间过期，function 将无法自动刷新它。在 [serverless mode](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) 下运行您的 function 以使用 OAuth-backed outbound applications。

* **Direct function usage in Workshop：** 在 [Workshop](/docs/foundry/workshop/overview/) 模块中直接使用的 functions，例如 [function-backed variables](/docs/foundry/workshop/functions-use/#function-backed-variables-in-workshop) 或填充 widget 内容的 functions，无法触发 OAuth 2.0 交互式 authorization 提示。如果用户尚未授权 outbound application，则 function 将失败而不会显示提示。要从 Workshop 使用 OAuth-backed function，请将其包装在 [function-backed action](/docs/foundry/action-types/function-actions-overview/) 中。或者，确保用户在 function 在 Workshop 中被直接调用之前，从其他交互式 interface（例如针对同一 outbound application 的 function-backed action）完成 authorization 流程。

* **TypeScript v1:** TypeScript v1 functions cannot retrieve OAuth tokens directly from a source. To authenticate with an OAuth 2.0 API from a TypeScript v1 function, wrap the call in a [webhook](/docs/foundry/functions/webhooks/) on a REST API source configured with the outbound application. Consider [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/) for direct token access.
* **Deployed mode:** OAuth token refreshing is not available when the function is running in [deployed mode](/docs/foundry/functions/functions-deployed/). If the calling user's access token expires during execution, the function cannot refresh it automatically. Run your function in [serverless mode](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) to use OAuth-backed outbound applications.
* **Direct function usage in Workshop:** Functions used directly in a [Workshop](/docs/foundry/workshop/overview/) module, such as [function-backed variables](/docs/foundry/workshop/functions-use/#function-backed-variables-in-workshop) or functions that populate widget content, cannot trigger the OAuth 2.0 interactive authorization prompt. If a user has not already authorized the outbound application, the function will fail rather than display the prompt. To use an OAuth-backed function from Workshop, wrap it in a [function-backed action](/docs/foundry/action-types/function-actions-overview/). Alternatively, ensure the user completes the authorization flow from another interactive interface (such as a function-backed action against the same outbound application) before the function is invoked directly in Workshop.
### Use the source's pre-configured client
最简单的方法是使用源提供的 HTTP client。`Authorization` header 会被自动注入。

The simplest approach is to use the HTTP client provided by the source. The `Authorization` header is injected automatically.
```python tab="Python"
from functions.api import function
from functions.sources import get_source

@function(sources=["MyOAuthSource"])
def call_external_api() -> str:
source = get_source("MyOAuthSource")
url = source.get_https_connection().url
client = source.get_https_connection().get_client()

response = client.get(url + "/api/v1/resource", timeout=10)
return response.text
```
```typescript tab="TypeScript v2"
import { getSource, getHttpsConnection, getFetch } from "@palantir/functions-sources";

export const config = {
sources: ["MyOAuthSource"]
};

export default async function callExternalApi(): Promise<string> {
const source = await getSource("MyOAuthSource");
const { url } = getHttpsConnection(source);
const fetch = await getFetch(source);

const response = await fetch(url + "/api/v1/resource");

return response.text();
}
```
### Use a native HTTP client with manual token injection
如果您需要使用自己的 HTTP client 而不是源提供的 client，请从 session credentials 中检索 OAuth token 并手动设置 `Authorization` header。

If you need to use your own HTTP client instead of the source-provided one, retrieve the OAuth token from session credentials and set the `Authorization` header manually.
```python tab="Python"
import requests
from functions.api import function
from functions.sources import get_source
from external_systems.sources import OauthCredentials, Refreshable, SourceCredentials

@function(sources=["MyOAuthSource"])
def call_external_api() -> str:
source = get_source("MyOAuthSource")
url = source.get_https_connection().url

refreshable_credentials: Refreshable[SourceCredentials] = source.get_session_credentials()
session_credentials: SourceCredentials = refreshable_credentials.get()

if not isinstance(session_credentials, OauthCredentials):
raise ValueError("Expected OAuth credentials")

access_token: str = session_credentials.access_token

response = requests.get(
url + "/api/v1/resource",
headers={"Authorization": f"Bearer {access_token}"},
timeout=10,
)
return response.text
```
```typescript tab="TypeScript v2"
import { getSource, getHttpsConnection } from "@palantir/functions-sources";

export const config = {
sources: ["MyOAuthSource"]
};

export default async function callExternalApi(): Promise<string> {
const source = await getSource("MyOAuthSource");
const credentials = await source.sessionCredentials?.get();

if (!credentials || credentials.type !== "oauth") {
throw new Error("Expected OAuth credentials");
}

const accessToken: string = credentials.accessToken;
const { url } = getHttpsConnection(source);

const response = await fetch(url + "/api/v1/resource", {
headers: { Authorization: `Bearer ${accessToken}` },
});

return response.text();
}
```
### Use OAuth-backed functions in actions
一种常见的模式是调用 OAuth-backed 外部 API 并将结果输入到 [Ontology edit](/docs/foundry/functions/edits-overview/) 中。然后，您可以通过 [function-backed action](/docs/foundry/action-types/function-actions-overview/) 公开该 function。当用户从 Workshop 或 AIP Studio 运行该 action 时，将使用他们的 OAuth token 进行 API 调用，并且所产生的 object edits 将归属于他们。

A common pattern is to call an OAuth-backed external API and feed the result into an [Ontology edit](/docs/foundry/functions/edits-overview/). You can then expose that function through a [function-backed action](/docs/foundry/action-types/function-actions-overview/). When a user runs the action from Workshop or AIP Studio, their OAuth token is used to make the API call, and the resulting object edits are attributed to them.
例如，下面的 function 使用 OAuth token 从第三方身份服务获取调用用户的 profile。然后，它使用该信息创建一个新的 ontology object：

For example, the function below uses an OAuth token to fetch the calling user's profile from a third-party identity service. It then creates a new ontology object with that information:
```python tab="Python"
from functions.api import function, OntologyEdit
from functions.sources import get_source
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import UserProfile

@function(sources=["MyOAuthSource"], edits=[UserProfile])
def link_user_profile() -> list[OntologyEdit]:
source = get_source("MyOAuthSource")
url = source.get_https_connection().url
client = source.get_https_connection().get_client()

response = client.get(url + "/v1/me", timeout=10)
response.raise_for_status()
profile = response.json()

ontology_edits = FoundryClient().ontology.edits()
ontology_edits.objects.UserProfile.create(
profile["id"],
display_name=profile["display_name"],
)
return ontology_edits.get_edits()
```
```typescript tab="TypeScript v2"
import { getSource, getHttpsConnection, getFetch } from "@palantir/functions-sources";
import { UserProfile } from "@ontology/sdk";
import { Client } from "@osdk/client";
import { createEditBatch, Edits } from "@osdk/functions";

type OntologyEdit = Edits.Object<UserProfile>;

export const config = {
sources: ["MyOAuthSource"],
edits: [UserProfile],
};

export default async function linkUserProfile(client: Client): Promise<OntologyEdit[]> {
const source = await getSource("MyOAuthSource");
const { url } = getHttpsConnection(source);
const fetch = await getFetch(source);

const response = await fetch(url + "/v1/me");
if (!response.ok) {
throw new Error(`Failed to fetch profile: ${response.status}`);
}
const profile = await response.json();

const batch = createEditBatch<OntologyEdit>(client);
batch.create(UserProfile, {
userProfileId: profile.id,
displayName: profile.display_name,
});
return batch.getEdits();
}
```
## Troubleshoot common errors
对于 OAuth authorization 错误，例如 `HTTP 401: Unauthorized`、`Credentials expired and no refresh handler provided` 或 `Resolved source credentials are not present on the Source`，请参阅 Data Connection 故障排除参考中的 [OAuth and outbound applications](/docs/foundry/data-connection/troubleshooting/#oauth-and-outbound-applications)。

For OAuth authorization errors, such as `HTTP 401: Unauthorized`, `Credentials expired and no refresh handler provided`, or `Resolved source credentials are not present on the Source`, see [OAuth and outbound applications](/docs/foundry/data-connection/troubleshooting/#oauth-and-outbound-applications) in the Data Connection troubleshooting reference.
### HTTP 407: Proxy authentication required
Function 的网络请求必须由您源的 [egress policies](/docs/foundry/administration/configure-egress/) 覆盖。如果目标 hostname 与允许的 policy 不匹配，则请求可能会返回 `HTTP 407: Proxy Authentication Required`。

Function network requests must be covered by your source's [egress policies](/docs/foundry/administration/configure-egress/). If the destination hostname does not match an allowed policy, the request may return `HTTP 407: Proxy Authentication Required`.
如果你的 egress policies 看起来正确,请检查请求 URL 是如何构建的。`getHttpsConnection()` 返回的 URL 没有尾部斜杠,因此附加路径时如果省略开头的 `/`,就会与主机名拼接在一起:

If your egress policies look correct, check how the request URL is built. The URL from `getHttpsConnection()` has no trailing slash, so an appended path that omits the leading `/` is fused to the hostname:
```text
"https://example.com" + "api/v1"
→ "https://example.comapi/v1"
```
生成的主机名(`example.comapi`)不被任何 egress policy 覆盖,因此请求被拒绝。请在路径前加上 `/`(例如,`url + "/api/v1"`)。

The resulting hostname (`example.comapi`) is not covered by any egress policy, so the request is rejected. Prefix the path with `/` (for example, `url + "/api/v1"`).