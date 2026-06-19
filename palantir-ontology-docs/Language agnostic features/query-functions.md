<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/query-functions/
---
# Queries
Query 是 function 中只读的子集，可以通过 [API gateway](/docs/foundry/api/general/overview/introduction/) 可选地暴露。Query 不能有任何副作用，例如修改 Ontology 或更改外部系统。如果你需要通过 API gateway 使用这些编辑功能，应该使用 [Action](/docs/foundry/api/ontology-resources/actions/apply-action/)。

Queries are the read-only subsets of functions that may be optionally exposed through the [API gateway](/docs/foundry/api/general/overview/introduction/). They cannot have any side effects, such as modifying the Ontology or altering external systems. You should use an [Action](/docs/foundry/api/ontology-resources/actions/apply-action/) if you need those additional editing capabilities through the API gateway.
## Query decorator
使用以下语法来定义一个 query function。

Use the following syntax to define a query function.
```typescript tab="TypeScript v1"
import { Query } from "@foundry/functions-api";

@Query({ apiName: "myTypeScriptV1Function" })
```
```typescript tab="TypeScript v2"
// Export a config object with an apiName parameter from the file containing the function
export const config = {
apiName: "myTypeScriptV2Function"
};
```
```python tab="Python"
from functions.api import function

@function(api_name="myPythonFunction")
```
对于 Python 和 TypeScript v1 functions，装饰器接受一个类型为 `string` 的 API name 参数，这是定义 API name 所必需的。当使用 TypeScript v1 时，如果未定义 `apiName` 参数，query 的行为将与现有的 [`@Function` decorator](/docs/foundry/functions/decorators/) 类似。请注意，对应的 Python 语法是 `api_name`。

For Python and TypeScript v1 functions, the decorator accepts an API name parameter of type `string`, which is required to define an API name. When using TypeScript v1, the query will behave similarly to the existing [`@Function` decorator](/docs/foundry/functions/decorators/) if the `apiName` parameter is not defined. Note that the corresponding Python syntax is `api_name`.
### Example: API-named query
以下示例演示了如何通过 [API gateway](/docs/foundry/api/general/overview/introduction/) 暴露一个 query：

The example below demonstrates how to expose a query through the [API gateway](/docs/foundry/api/general/overview/introduction/):
```typescript tab="TypeScript v1"
import { Query, Double } from "@foundry/functions-api";
import { Objects, Aircraft } from "@foundry/ontology-api";

export class PublishedQueries {
@Query({ apiName: "getReschedulableAircraftCount" })
public async countAircraftTakingOffAfter(minimumTimeInMinutes: Double): Promise<Double> {
const aircaftCount = await Objects.search().aircraft()
.filter(aircraft => aircraft.timeUntilNextFlight.range().gt(minimumTimeInMinutes))
.count();

return aircaftCount!;
}
}
```
```typescript tab="TypeScript v2"
import { Client } from "@osdk/client";
import { Double } from "@osdk/functions";
import { Aircraft } from "@ontology/sdk";

export const config = {
apiName: "getReschedulableAircraftCount"
};

async function countAircraftTakingOffAfter(client: Client, minimumTimeInMinutes: Double): Promise<Double> {
const { $count } = await client(Aircraft).where({
timeUntilNextFlight: {
$gt: minimumTimeInMinutes
}
}).aggregate({ $select: { $count: "unordered" } })

return $count;
}

export default countAircraftTakingOffAfter;

```
```python tab="Python"
from functions.api import Double, function
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Aircraft

@function(api_name="getReschedulableAircraftCount")
def count_aircraft_taking_off_after(minimum_time_in_minutes: Double) -> Double:
client = FoundryClient()
aircraft_count = client.ontology.objects.Aircraft.where(
Aircraft.time_until_next_flight > minimum_time_in_minutes
).count().compute()

return aircraft_count
```
## API name validations
Query 的 `apiName` 必须是一个满足以下要求的字符串：

The `apiName` of a query must be a string that meets the following requirements:
* 采用 `lowerCamelCase` 格式。
* 长度不超过 100 个字符。
* 不以数字开头。

* 在导入到该仓库的所有 Ontology 中是唯一的。

* 如果 `apiName` 不唯一，[tagging process](/docs/foundry/functions/getting-started/#publish-your-functions) 将失败，需要你更改名称。

* Be in `lowerCamelCase`.
* Be under 100 characters.
* Not contain leading numbers.
* Be unique among all Ontologies imported into the repository.
* The [tagging process](/docs/foundry/functions/getting-started/#publish-your-functions) will fail if the `apiName` is not unique, requiring you to change the name.
此外，包含 API-named queries 的仓库必须从至少一个 ontology 中导入实体。

Additionally, a repository containing API-named queries must import entities from at least one ontology.
## Version and update API-named queries
API-named queries 始终使用已发布 query 的 **latest tagged version**，并且不遵循与其他 Foundry functions 相同的语义化版本控制范式。

API-named queries will always use the **latest tagged version** of the published query and do not follow the same semantic versioning paradigm as other Foundry functions.
要解除 API name 与 query 的关联并在 API gateway 中中断它，必须从 query decorator 中移除 API name，并从仓库发布一个新的 tag。

To disassociate the API name from the query and break it in the API gateway, you must remove the API name from the query decorator and release a new tag from the repository.
> **ℹ️ 注意**

> 更改 decorator 中的 API name 并发布新 tag 将破坏 consumer。仅支持 query 的最新已发布版本。
> **ℹ️ 注意**

> Changing the API name in the decorator and publishing a new tag will break the consumer. Only the latest published version of the query is supported.
> 为了允许消费者在方便时进行升级而不会出现破坏性更改，您可以支持同一 API 名称的多个版本。为此，您必须复制仓库中的查询代码，并为其指定不同的 API 名称，例如 `getReschedulableAircraftCountV2`。
> To allow consumers to upgrade at their convenience without breaking changes, you can support multiple versions of the same API name. To do this, you must make a copy of the query code in your repository and give it a different API name, for example `getReschedulableAircraftCountV2`.
## Search and view queries
与其他 Function 一样，您可以在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中搜索并管理您的查询。您可以搜索查询名称或 API 名称。在 [上方](#example-api-named-query) 的示例中，API 名称对应的查询为 `getReschedulableAircraftCount`，查询名称对应的查询为 `countAircraftTakingOffAfter`。

As with other functions, you can search for and manage your queries in [Ontology Manager](/docs/foundry/ontology-manager/overview/). You can search for the query name or the API name. In the example [above](#example-api-named-query), the queries are `getReschedulableAircraftCount` for the API name and `countAircraftTakingOffAfter` for the query name, respectively.
![Search for queries in the Ontology Manager](/docs/resources/foundry/functions/query-in-oma.png)
> **ℹ️ 注意**

> 使用 TypeScript v1 Function 时，您可能需要更新仓库中的 `functions.json` 文件，通过将 `enableQueries` Property 设置为 true 来启用查询：
> **ℹ️ 注意**
