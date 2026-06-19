<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/derive-property-functions/
---
# Derive properties using Functions
[Functions](/docs/foundry/functions/overview/) 可用于在 object 上创建 **derived properties（派生属性）**。这些属性可以显示在 object 视图中，显示在扩展节点标签中，并用于在图层样式选项中为节点着色。

[Functions](/docs/foundry/functions/overview/) can be used to create **derived properties** on objects. These can be displayed in the object view, shown in extended node labels and used to color nodes in the layer styling options.
任何满足以下条件的 Function 都可以用作 **derived property（派生属性）**：

Any function that meets the following criteria can be used as a **derived property**:
* 该方法是 `public`。

* 该方法使用 `@Functions()` 装饰器。

* 该方法返回一个 FunctionsMap。

* `FunctionMap` 中的所有键都是 object。

* `FunctionsMap` 中的所有值都是 primitive 类型或每个字段都是 primitive 类型的自定义类型。
* 该方法已被标记为发布。

* 该方法对 object set（例如 `ExampleDataRoute[]`）进行操作，而不是对单个 object（例如 `ExampleDataRoute`）进行操作。这确保该 Function 不会针对图中的每个 object 单独调用，从而避免在大型图上出现性能极慢的问题。

* 该方法除 object set 外没有其他输入参数。

* The method is `public`.
* The method uses the `@Functions()` decorator.
* The method returns a FunctionsMap.
* All keys in the `FunctionMap` are objects.
* All values in the `FunctionsMap` are primitives or a custom type with primitives for each field.
* The method has been tagged for release.
* The method operates on object sets (`ExampleDataRoute[]`, for example) and not a single object (such as `ExampleDataRoute`). This ensures the function isn't called for every object on the graph individually, which can be cause very slow performance for large graphs.
* The method has no other inputs besides the object set.
For example:
```typescript
import { Function, FunctionsMap, Double } from "@foundry/functions-api";
import { ExampleDataRoute } from "@foundry/ontology-api";

export class VertexDerivedPropertyFunctions {
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