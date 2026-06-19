<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/integrate-functions/
---
# Function-based styling
[Functions](/docs/foundry/functions/overview/) 可用于在地图中为对象生成动态值。这些值可以显示在 **Selection** 面板中,并通过 [value-based styling](/docs/foundry/map/visualize-objects/#value-based-styling) 应用于地图上对象的颜色。

[Functions](/docs/foundry/functions/overview/) can be used in maps to generate dynamic values for objects. These values can be displayed in the **Selection** panel and applied to color objects on the map through [value-based styling](/docs/foundry/map/visualize-objects/#value-based-styling).
## Define a function for styling
Function 必须满足以下条件才能在地图中用于样式设置:

A function must meet the following conditions to be used for styling in maps:
* 它必须具有单个参数,该参数可以是 array 或 object set。

* 它必须返回一个 map,其中键是来自输入参数的对象,值是 string 或 numeric 类型。

* 在 [TypeScript v1](/docs/foundry/functions/typescript-v1-getting-started/) 中,使用 `FunctionsMap` 来返回 map。

* 在 [TypeScript v2](/docs/foundry/functions/typescript-v2-getting-started/) 中,使用 `Record` 与 `ObjectSpecifier` 键来返回 map。

* It must have a single argument that is either an array or an object set.
* It must return a map where the keys are objects from the input argument, and the values are a string or numeric type.
* In [TypeScript v1](/docs/foundry/functions/typescript-v1-getting-started/), use `FunctionsMap` to return the map.
* In [TypeScript v2](/docs/foundry/functions/typescript-v2-getting-started/), use `Record` with `ObjectSpecifier` keys to return the map.
For example:
```typescript tab="TypeScript v1"
import { Function, FunctionsMap, Double } from "@foundry/functions-api";
import { ExampleDataRoute } from "@foundry/ontology-api";

export class DerivedPropertyFunctions {
@Function()
public async flightCancellationPercentage(routes: ExampleDataRoute[]): Promise<FunctionsMap<ExampleDataRoute, Double>> {
const routeMap = new FunctionsMap<ExampleDataRoute, Double>();

const allFlights = await Promise.all(routes.map(route => route.flights.allAsync()));

for (let i = 0; i < routes.length; i++) {
const route = routes[i];
const flights = allFlights[i];
const cancelledFlights = flights.filter(flight => flight.cancelled);
const cancellationPercentage = (cancelledFlights.length / flights.length) * 100;
routeMap.set(route, cancellationPercentage);
}

return routeMap;
}
}
```
```typescript tab="TypeScript v2"
import { ObjectSpecifier, Osdk } from "@osdk/client";
import { Double } from "@osdk/functions";
import { ExampleDataRoute } from "@ontology/sdk";

async function flightCancellationPercentage(routes: Osdk.Instance<ExampleDataRoute>[]): Promise<Record<ObjectSpecifier<ExampleDataRoute>, Double>> {
const routeMap: Record<ObjectSpecifier<ExampleDataRoute>, Double> = {};

const allFlights = await Promise.all(routes.map(route => route.flights.allAsync()));

for (let i = 0; i < routes.length; i++) {
const route = routes[i];
const flights = allFlights[i];
const cancelledFlights = flights.filter(flight => flight.cancelled);
const cancellationPercentage = (cancelledFlights.length / flights.length) * 100;
routeMap[route.$objectSpecifier] = cancellationPercentage;
}

return routeMap;
}

export default flightCancellationPercentage;
```
> **ℹ️ 注意**

> Map 应用程序将对象分批传递给您的 function,并期望为该批次中的所有对象返回值。Layer 中的所有对象在第一次参数调用中*不会*被全部提供。您的 function 应产生一致的结果,而与对象的批处理方式无关。这意味着对于任何给定的对象,无论同一批次中包含哪些对象,该 function 都应返回相同的值。
> **ℹ️ 注意**

> The Map application passes objects to your function in batches, and expects values to be returned for all objects in the batch. All objects in a layer will *not* be provided in a single function call in the first argument. Your function should produce consistent results regardless of how objects are batched. This means that for any given object, the function should return the same value regardless of which objects are included in the same batch.
## Pass additional arguments to functions
在 Workshop Map widget 中将 function 用于样式设置时,您的 function 除了主要的 objects 输入外,还可以接受其他参数。

When using a function for styling in the Workshop Map widget, your function can accept arguments in addition to the primary objects input.
在使用其他参数时,第一个参数仍将始终指定需要为其计算并返回值的对象。Widget 会自动为此第一个参数提供值,但仅显示其他参数。Widget 配置允许您通过选择变量来为其他参数指定值。

When working with additional arguments, the first argument will still always specify the objects for which you need to compute and return values. The widget automatically provides values for this first argument, but only the additional arguments will be shown. The widget configuration allows you to specify values for additional arguments by selecting variables.

> 📷 **[图片: Workshop Map widget 中 styling function 的其他参数。]**

> 📷 **[图片: Additional arguments to a styling function in the Workshop Map widget.]**

