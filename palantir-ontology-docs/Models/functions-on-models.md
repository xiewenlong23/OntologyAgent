<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/functions-on-models/
---
# Functions on models
您可以在 Ontology 的上下文中部署 model，方法是在其运行时使用调用 model 的 function。Model function 是围绕实时 model 部署自动生成的包装器，可以导入到 functions repository 中并从您的代码中调用。这使您能够围绕 model 预测添加自定义业务逻辑、将 model 与 Ontology objects 集成，或编排多个 model 调用。

You can deploy models in the context of the Ontology by using functions that invoke models during their runtime. Model functions are automatically generated wrappers around live model deployments that can be imported into a functions repository and called from your code. This enables you to add custom business logic around model predictions, integrate models with Ontology objects, or orchestrate multiple model calls.
## Overview
可以从两种类型的部署中发布 model function：

Model functions can be published from two types of deployments:
* **[直接 model 部署](/docs/foundry/manage-models/create-a-model-deployment/)：**直接从 model 页面发布。

* **[Modeling Objective live 部署](/docs/foundry/manage-models/set-up-live/)：**从 Modeling Objective 中的部署详情页面发布。

* **[Direct model deployments](/docs/foundry/manage-models/create-a-model-deployment/):** Published directly from the model page.
* **[Modeling Objective live deployments](/docs/foundry/manage-models/set-up-live/):** Published from the deployment details page in a Modeling Objective.
这两种方法都会创建一个具有与您的 model 相同 input 和 output API 的 function。有关 function 行为、版本升级和配置选项的详细信息，请参阅 [Model functions developer guide](/docs/foundry/model-integration/model-functions-guide/)。

Both methods create a function with the same input and output API as your model. For details on function behavior, version upgrades, and configuration options, see the [Model functions developer guide](/docs/foundry/model-integration/model-functions-guide/).
Model function 在 TypeScript v1、TypeScript v2 和 Python functions 中均得到完全支持。

Model functions are fully supported in TypeScript v1, TypeScript v2, and Python functions.
## Import a live deployment in a repository
一旦为实时部署创建了 function——无论是在 [model 本身](/docs/foundry/manage-models/create-a-model-deployment/#3-publish-a-function-for-the-deployment) 上还是在 [modeling objective](/docs/foundry/manage-models/set-up-live/#publish-function) 中——都必须将其导入到特定 repository 中才能使用。在 repository 左侧边栏的 **Resource Imports** 菜单中选择 **Add** 和 **Query Functions**。Models 可按发布时选择的 function 名称进行搜索。请注意，Python 和 TypeScript v2 repositories 仅支持绑定到 ontology 的 model function，如下文所述。

Once a function for a live deployment has been created either [on the model itself](/docs/foundry/manage-models/create-a-model-deployment/#3-publish-a-function-for-the-deployment) or in a [modeling objective](/docs/foundry/manage-models/set-up-live/#publish-function), it must be imported for usage in a specific repository. Select **Add** and **Query Functions** in the **Resource Imports** menu on the left side bar in the repository. Models are searchable by the function name that was chosen during publishing. Note that Python and TypeScript v2 repositories only support model functions that are tied to an ontology, as described in the section below.
> **ℹ️ 注意: Notes**

> 对于 TypeScript v1 repositories，也可以通过选择 **Models** 来导入 model function，这在功能上等同于在 **Query Functions** 下导入它。
> **ℹ️ 注意: Notes**

> For TypeScript v1 repositories, it is also possible to import a model function by selecting **Models**, which is functionally equivalent to importing it under **Query Functions**.
> 使用 Modeling Objectives 中 **API Name** 卡片（而非首选的 [model publication 对话框](/docs/foundry/manage-models/set-up-live/#publish-function)）的 model 上的旧版 function 仍可在 **Modeling Objectives** 部分下导入，但正在被弃用。
> Legacy function on models that use the **API Name** card in Modeling Objectives instead of the preferred [model publication dialog](/docs/foundry/manage-models/set-up-live/#publish-function) can still be imported under the **Modeling Objectives** section, but are being sunset.
## Ontology or space-bound functions
从 2026 年 2 月开始，所有新 model function 将绑定到 ontology。这是用于 [TypeScript v2 和 Python functions](/docs/foundry/functions/language-models-python-tsv2/) 的前提条件，这些 functions 仅允许 ontology 资源导入。在此日期之前，model function 绑定的是 model 的 [space](/docs/foundry/security/orgs-and-spaces/)。TypeScript v1 允许导入这两种类型的 model function，但导入和使用语义略有不同，详见 [下文](#if-the-function-is-registered-to-an-ontology)。

Starting from February 2026 onwards, all new model functions will be tied to an ontology. This is a prerequisite for usage in [TypeScript v2 and Python functions](/docs/foundry/functions/language-models-python-tsv2/), which only allow ontology resource imports. Prior to this date, model functions were tied to the model's [space](/docs/foundry/security/orgs-and-spaces/). TypeScript v1 allows importing both types of model functions, but the import and usage semantics vary slightly as [detailed below](#if-the-function-is-registered-to-an-ontology).
若要检查 function 是否绑定到 ontology，请导航至您的 model：未绑定到 ontology 的 model function 将提示可以进行迁移。[详细了解如何将您的 function 迁移为 ontology 绑定](#migrating-model-functions-to-ontology-bound-functions)。

To check if a function is bound to an ontology, navigate to your model: model functions that are not bound to an ontology will indicate that a migration is available. [Learn more on migrating your function to be ontology-bound](#migrating-model-functions-to-ontology-bound-functions).
## Call a model function from Python or TypeScript v2 functions
一旦为实时部署创建了 function，就必须将其导入到特定 repository 中才能使用。然后可以像 [任何 query function 一样](/docs/foundry/functions/query-functions/#call-a-query-function) 对其进行查询。

Once a function for a live deployment has been created, it must be imported for usage in a specific repository. It can then be queried [like any query function](/docs/foundry/functions/query-functions/#call-a-query-function).
### Example code: Python
```python
from functions.api import function, Double
from foundry_sdk_runtime import AllowBetaFeatures
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Flight

@function(beta=True)
def predict_flight_delays(flight: Flight) -> Double:
# Prepare the input to match the model function's API.
model_output = FoundryClient().ontology.queries.flight_model_deployment(
df_in=[
{
"lastArrivalTime": flight.last_arrival_time,
"lastExpectedArrivalTime": flight.last_expected_arrival_time,
},
]
)
return model_output.df_out[0].prediction
```
### Example code: TypeScript v2
```typescript
import { Client } from "@osdk/client";
import { Double } from "@osdk/functions";
import { flightModelDeployment, Flight } from "@ontology/sdk";

async function predictFlightDelays(client: Client, flight: Flight): Promise<Double> {
// Prepare the input to match the model function's API.
const modelOutput = await client(flightModelDeployment).executeFunction({
"df_in": [
{
"lastArrivalTime": flight.lastArrivalTime,
"lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
},
]
});
return modelOutput.df_out[0].prediction;
}

export default predictFlightDelays;
```
## Write a model-backed TypeScript v1 function
### If the model function is registered to a space
我们首先需要导入该 function：

We first need to import the function:
```typescript
// If the model function is tied to a space and not to an ontology,
// copy the import snippet from the Resource imports sidebar.
```
然后,编写一个函数,该函数接收一个航班,为模型准备数据,并解释模型执行的结果。该模型作为一个异步函数导入,该异步函数遵循[模型的输入和输出规范或 API](/docs/foundry/integrate-models/model-adapter-api/)。基于此,TypeScript 可以在编译时确保将正确的数据结构发送至模型部署,并从模型部署接收正确的数据结构。

Then, write a function that takes a flight, prepares data for the model, and interprets the result of the model execution. The model is imported as an asynchronous function that respects the [model's input and output specification or API](/docs/foundry/integrate-models/model-adapter-api/). From this, TypeScript can ensure, at compile time, that the correct data structure is sent to and received from the model deployment.
请注意,如果你的模型 API 期望单个表格输入和输出,则当启用了[**Enable row-wise processing** 选项](/docs/foundry/model-integration/model-functions-guide/#row-wise-publishing)(默认启用)时,相关的函数将接受单个 TypeScript 对象,其属性对应于为输入指定的列。下面的 `predictFlightDelaysRowWise` 函数演示了这种模式。或者,考虑[在模型 API 中直接使用 Object 或 ObjectSet](/docs/foundry/integrate-models/model-adapter-reference/#for-object-inputs),以便在函数中更方便地与对象一起使用你的模型。

Note that if your model's API expects a single tabular input and output, the associated function will accept single TypeScript objects with properties corresponding to the columns specified for the input if the [**Enable row-wise processing** option](/docs/foundry/model-integration/model-functions-guide/#row-wise-publishing) is enabled, which is the default. The `predictFlightDelaysRowWise` function below demonstrates this pattern. Alternatively, consider [using an Object or ObjectSet directly in the model API](/docs/foundry/integrate-models/model-adapter-reference/#for-object-inputs) to facilitate use of your model with objects in functions.
下面的 `predictFlightDelays` 函数返回一个 [`FunctionsMap`](/docs/foundry/functions/types-reference/#map),这是 TypeScript v1 中用于返回以对象或标量值为键的映射的类型。在本示例中,它将每个 `Flight` 对象映射到其预测的延误值。

The `predictFlightDelays` function below returns a [`FunctionsMap`](/docs/foundry/functions/types-reference/#map), which is the TypeScript v1 type used to return a map keyed by objects or scalar values. In this example, it maps each `Flight` object to its predicted delay value.
```typescript
import { Function, Double, FunctionsMap } from "@foundry/functions-api";
import { Flight } from "@foundry/ontology-api";

@Function()
public async predictFlightDelaysRowWise(flight: Flight): Promise<Double> {
// Prepare the input to match the model function's API.
// This model function expects a single flight.
// If you'd like to process multiple flights at a time,
// edit your model function and uncheck "Enable row-wise processing".

// Note you can also use an Object directly in the model API
// to avoid tedious mapping between a model API and an object type's properties.
const modelInput = {
"lastArrivalTime": flight.lastArrivalTime,
"lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
};
// Call the Live deployment.
const modelOutput = await FlightModelDeploymentRowWise(modelInput);
return modelOutput.prediction;
}

@Function()
public async predictFlightDelays(flights: Flight): Promise<FunctionsMap<Flight, Double>> {
let functionsMap = new FunctionsMap();
// Prepare the input to match the model function's API,
// for the case where row-wise processing is not enabled.

// Note you can also use an ObjectSet directly in the model API
// to avoid tedious mapping between a model API and an object type's properties.
const dfIn = flights.map(flight => ({
"lastArrivalTime": flight.lastArrivalTime,
"lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
}));
// Call the Live deployment.
const modelOutput = await FlightModelDeployment(
{"df_in": dfIn}
);
for (let i = 0; i < flights.length; i++) {
functionsMap.set(flights[i], modelOutput.df_out[i].prediction);
}
return functionsMap;
}
```
请注意,上面的示例假设了以下 Model API:

Note the above example assumes the following Model API:
```python
import palantir_models as pm

class ExampleModelAdapter(pm.ModelAdapter):
...

@classmethod
def api(cls):
inputs = {
"df_in": pm.Pandas(columns=[("lastArrivalTime", datetime.datetime), ("lastExpectedArrivalTime", datetime.datetime)])
}
outputs = {
"df_out": pm.Pandas(columns=[("prediction", float)])
}
return inputs, outputs
...

```
### If the function is registered to an ontology
在这种情况下,导入和查询语法都需要按照下方代码片段中的注释进行更新:

In this case, both the import and the query syntax need to be updated as detailed by the comments in the snippet below:
```typescript
import { Function, Double } from "@foundry/functions-api";
// Add the Queries import to use an ontology-bound model function
import { Queries, Flight } from "@foundry/ontology-api";

export class MyFunctions {
@Function()
public async predictFlightDelays(flight: Flight): Promise<Double> {
// Call your model by API Name from Queries
const modelOutput = await Queries.flightModelDeployment({
"df_in": [
{
"lastArrivalTime": flight.lastArrivalTime,
"lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
},
]
});
return modelOutput.df_out[0].prediction;
}
}
```
### Migrating model functions to ontology-bound functions
当你通过用户界面将 space-bound 的模型函数迁移到 ontology-bound 函数时,使用该模型的 TypeScript v1 函数的现有已发布版本将继续工作。但是,导入语法将不再被识别,这意味着预览和为使用该模型函数的仓库标记新版本将无法继续工作。

When you migrate a space-bound model function to an ontology-bound function from the user interface, existing published versions of TypeScript v1 functions that use the model will continue to work. However, the import syntax will no longer be recognized, meaning preview and tagging new releases of the repository consuming the model function will no longer work.
要在迁移后更新你的 TypeScript v1 函数,请执行以下操作:

To update your TypeScript v1 function after migration:
1. 打开你的代码仓库,并选择 **Resource imports** 侧边栏。

2. 通过将 resources.json 文件更新到新版本,选择新创建的模型函数版本。

3. 按照上文详述的方法,将你的函数代码更新为使用查询函数语法,或参阅[调用 query function](/docs/foundry/functions/query-functions/#call-a-query-function) 的专门文档以了解更多详细信息。

1. Open your code repository and select the **Resource imports** sidebar.
2. Select the newly created version of the model function, by updating the resources.json file to the new version.
3. Update your function code to use the query function syntax as detailed above, or see the dedicated documentation on [calling a query function](/docs/foundry/functions/query-functions/#call-a-query-function) for more details.
> **⚠️ 警告**

> 通过 [Foundry Platform SDK](/docs/foundry/dev-toolchain/overview/#platform-sdks) 和 [Functions.Query ↗](https://github.com/palantir/foundry-platform-python/blob/develop/docs/v2/Functions/Query.md) 方法直接使用模型函数将在迁移时立即失效。这是因为此使用模式通过其 API 名称引用该函数,而该 API 名称会在所有模型函数版本中全局同时迁移。要修复这些消费者,请在迁移后将 API 名称更新为其新值。
> **⚠️ 警告**

> Direct model function usage through the [Foundry Platform SDK](/docs/foundry/dev-toolchain/overview/#platform-sdks) and the [Functions.Query ↗](https://github.com/palantir/foundry-platform-python/blob/develop/docs/v2/Functions/Query.md) method will break immediately upon migration. This is because this consumption pattern refers to the function by its API name, which is migrated globally across all model function versions at once. To remediate these consumers, update the API name to its new value after the migration.
## Performance considerations
模型作为函数运行时的一部分执行,因此所有标准 [limits](/docs/foundry/functions/manage-functions/#enforced-limits) 均适用。如果你的函数 backing 一个 Action,那么对结果 edits 的数量还有[further limits](/docs/foundry/action-types/scale-property-limits/#edit-limits)。在调用实时部署时,模型输入和输出数据通过网络发送的上限为 50 MB。包含该额外吞吐量在内,函数的总执行时间不能超过 30 秒。如果希望按函数提高此超时限制,请联系你的 Palantir 代表。

Models are executed as part of the runtime of the function, therefore all standard [limits](/docs/foundry/functions/manage-functions/#enforced-limits) apply.
If your function backs an Action, there are [further limits](/docs/foundry/action-types/scale-property-limits/#edit-limits) on the number of resulting edits.
When calling live deployments, model input and output data is sent through the network with an upper limit of 50 MB. Including that additional throughput, the total execution time of the function cannot exceed 30 seconds. If you wish to increase this timeout limit per function, contact your Palantir representative.