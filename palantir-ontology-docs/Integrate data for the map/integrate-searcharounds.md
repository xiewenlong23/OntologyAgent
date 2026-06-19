<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/integrate-searcharounds/
---
# Map Search Arounds
Search Around 是基于 Link 或 Function 的搜索，允许用户探索相关的 Object。您可以在 Control Panel 中 [配置 Search Around 的限制](/docs/foundry/map/control-panel/#data-loading)。

Search Arounds are link or function-based searches that allow users to explore related objects. You can [configure search around limits in Control Panel](/docs/foundry/map/control-panel/#data-loading).
## Link Search Arounds
用户可以从任何地理空间 Object 向其链接到的任何地理空间 Object 执行 Search Around。有关更多信息，请参阅 [Create a link type](/docs/foundry/object-link-types/create-link-type/)。

A user can Search Around from any geospatial object to any geospatial objects it is linked to. See [Create a link type](/docs/foundry/object-link-types/create-link-type/) for more information.
## Link merged Search Arounds
Map 应用程序可以运行两步 Search Around，其中一个地理空间 Object 通过一个中间 Object（可以是非地理空间的）链接到另一个地理空间 Object。

The Map application can run two-step Search Arounds, where a geospatial object is linked to another geospatial object via an intermediary object (which could be non-geospatial).
* 中间 Object 可能表示两个 Object 之间的关系。例如，一个 `Factory` Object 和一个 `Supplier` Object 可能通过一个 `Supply Contract` Object 相关联；当运行 Search Around 时，Map 将显示一条从 factory 到 supplier 的弧线，其中该弧线表示 supply contract。

* 中间 Object 也可能是两个 Object 都涉及的一个 event。例如，一个 `Customer` Object 可能通过一个 `Delivery` event 链接到一个 `Distribution Center` Object —— 在这种情况下，delivery event 将显示为沿弧线移动的圆圈。圆圈的位置将根据 event 开始和结束时间以及当前选定的 timestamp 在弧线上进行插值。

* The intermediary object might represent a relationship between the two objects. For example, a `Factory` object and a `Supplier` object might be related via a `Supply Contract` object; when a Search Around is run, the Map will show an arc from factory to supplier, where the arc represents the supply contract.
* The intermediary object might also be an event which both objects are involved with. For example, a `Customer` object might be linked to a `Distribution Center` object via a `Delivery` event - in this case, the delivery events will be shown as circles traveling along the arc. The position of the circle will be interpolated along the arc based on the event start and end time as well as the currently selected timestamp.
![Link merged arc example](/docs/resources/foundry/map/integrate-objects-linkmerge-arc-example.png)
有两种方法可以将 Object 配置为用于 link 合并的 Search Around：

There are two methods for configuring objects to be used for link merged Search Arounds:
* 将中间 Object 指定为 link 合并 Object，这意味着该 Object Type 本身永远不会出现在 Search Around 列表中，但其传递性 link 将会出现。

* 将特定的 link 遍历指定为合并。当只需要将中间 Object 的部分关系进行 link 合并时，可使用此方法。

* Designating the intermediary object as a link merge object, which means that this object type itself will never appear in the Search Around list, but its transitive links will.
* Designating specific link traversals to be merged. Use this approach if only some of the relations of the intermediary object should be link merged.
### Set an intermediary object type to always link merge
若要将中间 Object Type 指定为始终 link 合并，请在中间 Object Type 的 **Capabilities** 选项卡的 **Search Around** 部分中开启 **Link merge always**。这意味着该 Object Type 本身永远不会出现在 Search Around 列表中，但其传递性 link 将会出现。

To designate an intermediary object type to always link merge, turn on **Link merge always** in the **Search Around** section of the intermediary object type's **Capabilities** tab.  This means that the object type itself will never appear in the Search Around list, but its transitive links will.
![Link merge configuration in Ontology Manager.](/docs/resources/foundry/map/oma-capabilities-link-merge.png)
例如，如果中间 Object Type 是 `Delivery`，且两侧的 Object Type 分别是 `Distribution Center` 和 `Customer`，那么当选择一个 `Distribution Center` 进行 Search Around 时，`Delivery` 不会出现在列表中，但 `Customer (via Delivery)` 会出现。示例如下：

For example, if the intermediary object type is `Delivery`, and the object types on either side are `Distribution Center` and `Customer`, then when a `Distribution Center` is selected to Search Around on, `Delivery` will not show up in the list, but `Customer (via Delivery)` will. See below for an example:
![Search Around menu with link merged objects.](/docs/resources/foundry/map/integrate-objects-searcharound-linkmerge-example.png)
### Set specific link traversals to be link merged
若要将特定 link 遍历指定为 link 合并，请在中间 Object Type 的 **Capabilities** 选项卡的 **Search Around** 部分中同时指定 **Incoming links to merge** 和 **Outgoing links to merge**。

To designate specific link traversals to be link merged, specify both the **Incoming links to merge** and **Outgoing links to merge** in the **Search Around** section of the intermediary object type's **Capabilities** tab.
![Incoming/Outgoing link merge configuration in Ontology Manager.](/docs/resources/foundry/map/oma-capabilities-link-merge-incoming-outgoing.png)
例如，如果您希望通过 `Delivery` Object Type 从 `Supplier` Object Type 对 `Distribution Center` Object Type 执行 Search Around，则可以通过将 `Delivery <-> Supplier` link 选择为 **Incoming links to merge**，并将 `Delivery <-> Distribution Center` link 选择为 **Outgoing links to merge**，将 `Delivery` Object Type 配置为中间 Object Type。现在，当选择一个 `Supplier` 进行 Search Around 时，`Distribution Centers (via Delivery)` 将作为选项出现在列表中。

For example, if you want to be able to perform a Search Around from a `Supplier` object type to a `Distribution Center` object type via a `Delivery` object type, you would configure the `Delivery` object type as the intermediary by selecting the `Delivery <-> Supplier` link as **Incoming links to merge** and the `Delivery <-> Distribution Center` link as **Outgoing links to merge**. Now, when a `Supplier` is selected to Search Around on, `Distribution Centers (via Delivery)` will appear as an option in the list.
> **ℹ️ 注意**

> 如果您希望 link 遍历的两个方向都出现在 Search Around 列表中（例如，`Suppliers` 既要包含 `Distribution Centers (via Delivery)`，`Distribution Centers` 也要包含 `Suppliers (via Delivery)`），则需要将这些 link 同时配置为 **Incoming links to merge** 和 **Outgoing links to merge**。
> **ℹ️ 注意**

> If you want both link traversal directions to appear in the Search Around list (for example, for both `Suppliers` to have `Distribution Centers (via Delivery)` and also `Distribution Centers` to have `Suppliers (via Delivery)`), you will need to configure those links as both **Incoming links to merge** and **Outgoing links to merge**.
## Search Around functions
您可以通过编写 **Map Search Around** [functions](/docs/foundry/functions/overview/) 为 Map 创建功能强大的 **Map Search Around**。这允许您编写 TypeScript functions，这些 functions 接收所选 Object，并遍历 Ontology 以带回与正在执行的特定分析相关或有用的所有 Object。

You can create powerful **Map Search Arounds** for the Map by writing **Map Search Around** [functions](/docs/foundry/functions/overview/). This allows you to write TypeScript functions that are given the selected objects and traverse the Ontology to bring back all the objects that are relevant or useful for the specific analysis being undertaken.
**Map Search Around** functions 返回的数据结构可以包括：

**Map Search Around** functions return a data structure that can include:
* `objectRids`：Object，将被添加到 map 中。

* `edges`：边，包括一个源 Object、一个目标 Object，以及可选的中间 Object。源 Object 和目标 Object 将被添加到 map 中，并在它们之间绘制一条弧线，中间 Object 将在选中弧线时列出。

* `measures`：Time Series Measures，将被添加到 [timeline](/docs/foundry/map/timeline/) 中。

* `objectRids`: Objects, which will be added to the map.
* `edges`: Edges, which include a source object, a target object, and optionally intermediary objects.  The source and target objects will be added to the map with an arc drawn between them, and the intermediary objects will be listed when the arc is selected.
* `measures`: Time Series Measures, which will be added to the [timeline](/docs/foundry/map/timeline/).
### Implement a Map Search Around function
**Map Search Around** functions 是在 TypeScript functions 仓库中开发的。有关更多信息，请参阅 [Functions documentation](/docs/foundry/functions/overview/)。

**Map Search Around** functions are developed in a TypeScript functions repository. For more information, see the [Functions documentation](/docs/foundry/functions/overview/).
#### Return type
**Map Search Around** function 必须声明返回类型为 `Promise<IMapSearchAroundResults>`。Map 应用程序将根据 return type 的名称和结构来发现 Search Around functions，因此返回类型必须严格按照以下方式声明：

A **Map Search Around** function must declare a return type of `Promise<IMapSearchAroundResults>`. The Map application will discover Search Around functions using the name and structure of their return type, so the return type must be declared exactly as follows:
```typescript
export interface IMapSearchAroundResults {
objectRids?: string[];
edges?: IMapSearchAroundEdge[];
measures?: IMapSearchAroundMeasure[];
}

export interface IMapSearchAroundEdge {
sourceObjectRid: string;
targetObjectRid: string;
intermediaryObjectRids?: string[];
}

export interface IMapSearchAroundMeasure {
objectRids: string[];
measureId: string;
}

```
#### Parameters
Map Search Around functions 必须包含一个（且只能包含一个）Object 参数，该参数可以是以下类型之一：

Map Search Around functions must include one (and only one) object parameter, which can be one of the following:
* **单个 Object**：当选择指定类型的单个 Object 时，此 Search Around function 将在 Search Around 菜单中可用。例如：

* **A single object:** this Search Around function will be available in the Search Around menu when a single object of the specified type is selected. For example:
```typescript
public exampleSearchAround(object: ExampleObjectType) { ...
```
* **Object 数组**：当选择指定类型的任意数量的 Object 时，此 Search Around function 将在 Search Around 菜单中可用。例如：

* **An object array:** this Search Around function will be available in the Search Around menu when any number of objects of the specified type are selected. For example:
```typescript
public exampleSearchAround(objects: ExampleObjectType[]) { ...
```
* **Object set（对象集）：**当选中指定类型的任意数量的对象时,此 Search Around function 将出现在 Search Around 菜单中。例如：

* **An object set:** this Search Around function will be available in the Search Around menu when any number of objects of the specified type are selected. For example:
```typescript
public exampleSearchAround(objectSet: ObjectSet<ExampleObjectType>) { ...
```
Map Search Around function 可以选择性地包含以下标量类型的任意数量的额外参数：`string`、`boolean`、`Integer`、`Long`、`Float`、`Double`、`LocalDate` 或 `Timestamp`（有关更多详细信息,请参阅 [Scalar types](/docs/foundry/functions/types-reference/#scalar-types)）。当用户使用额外参数执行 Search Around function 时,系统将提示用户输入这些参数的值。例如：

Map Search Around functions can optionally include any number of additional parameters of these scalar types: `string`, `boolean`, `Integer`, `Long`, `Float`, `Double`, `LocalDate`, or `Timestamp` (see [Scalar types](/docs/foundry/functions/types-reference/#scalar-types) for more details). When a user executes a Search Around function with additional parameters, the user will be prompted to enter values for the parameters. For example:
```typescript
public exampleSearchAround(objectSet: ObjectSet<ExampleObjectType>, stringParameter: string, timestampParameter: Timestamp) { ...
```
### Tips & troubleshooting
* 为了最大限度地提高性能,所有代码应尽可能地异步。在您的 function 代码中,加载对象时始终使用 `allAsync()` 和 `getAsync()`,而不是 `all()` 和 `get()`,并尽可能少地使用 `await` 语句。

* Map 应用程序将使用最新发布的 function 版本。要发布您的 Function,您需要使用符合 semver 规范的版本（例如：1.0.0）对您想要的 branch/commit 进行标记。

* 您的代码仓库需要有权访问您要在 function 中使用的所有 Ontology 对象和 Link。这可在代码仓库 **Settings** 的 **Ontology** 部分进行配置。

* 如果 Object Type 及其 backing dataset 在与代码仓库不同的项目中定义,则包含您代码仓库的项目需要引用这些 backing dataset 以及那些 Object Type。

* To maximize performance, all code should be as asynchronous as possible. In your function code, always use `allAsync()` and `getAsync()` instead of `all()` and `get()` when loading objects, and use as few `await` statements as possible.
* The Map application will use the latest published version of a function. To publish your Function, you need to tag the branch/commit you want with a semver-compatible version, for example: 1.0.0.
* Your repository needs access to all the Ontology objects and links you want to use in your function. This is configurable under the **Ontology** section of the Repository's **Settings**.
* If the object types and their backing datasets are defined in a different project than the repository, the project containing your repository will need a reference to the backing datasets and those object types.
### Examples
此示例代码包含三个基于开源示例数据的 Search Around function：

This example code contains three Search Around functions, based on open-source sample data:
* `airportsRelatedObjects`：返回与一组机场相关的各种对象。可在用于机场分析的地图模板中使用。

* `nearbyAirports`：执行地理空间搜索以查找给定距离内的其他机场。该 function 接受一个可选的距离参数,允许用户在执行 function 时提供距离。

* `routesBetweenAirports`：给定一组机场,仅返回这些机场之间的所有路线。

* `airportsRelatedObjects`: Returns various objects related to a set of airports. Could be used in a map template for airport analysis.
* `nearbyAirports`: Performs a geospatial search to find other airports within a given distance. The function takes an optional distance parameter, allowing the user to provide a distance when executing the function.
* `routesBetweenAirports`: Given a set of airports, returns all routes just between those airports.
```typescript
import { Distance, Function, Integer, Filters } from "@foundry/functions-api";
import { ObjectSet, Objects, ExampleDataAirport } from "@foundry/ontology-api";

export interface IMapSearchAroundResults {
objectRids?: string[];
edges?: IMapSearchAroundEdge[];
measures?: IMapSearchAroundMeasure[];
}

export interface IMapSearchAroundEdge {
sourceObjectRid: string;
targetObjectRid: string;
intermediaryObjectRids?: string[];
}

export interface IMapSearchAroundMeasure {
objectRids: string[];
measureId: string;
}

export class MapSearchAroundFunctions {

/**
* Return relevant objects for airports: runways, routes
*/
@Function()
public async airportsRelatedObjects(airportSet: ObjectSet<ExampleDataAirport>): Promise<IMapSearchAroundResults> {
const relatedObjects = (await Promise.all([
airportSet.searchAroundExampleDataRunway().allAsync(),
airportSet.searchAroundRoutes().allAsync(),
])).flat();

const objectRids = relatedObjects.map(o => o.rid!);

return {
objectRids,
};
}

/**
* Return all airports within the specific number of kilometres of the selected airport (defaulting to 50)
*/
@Function()
public async nearbyAirports(airport: ExampleDataAirport, distanceKm?: Integer): Promise<IMapSearchAroundResults> {
const point = airport.airportLocation;
const distance = Distance.ofKilometers(distanceKm ?? 50);

if (point === undefined) {
return {};
}

const nearbyAirports = await Objects.search()
.exampleDataAirport()
.filter(airportFilter => airportFilter.airportLocation.withinDistanceOf(point, distance))
.allAsync();

const objectRids = nearbyAirports.map(o => o.rid!);

return {
objectRids,
};
}

/**
* Return only routes that depart from and arrive in the selected airports
*/
@Function()
public async routesBetweenAirports(airportSet: ObjectSet<ExampleDataAirport>): Promise<IMapSearchAroundResults> {
const airports = await airportSet.allAsync();
const airportCodes = airports.map(airport => airport.airport);
const airportsByCodes = new Map(Array.from(airports, a => [a.airport, a]));

const routes = await Objects.search()
.exampleDataRoute()
.filter(route => Filters.and(
route.origin.exactMatch(...airportCodes),
route.dest.exactMatch(...airportCodes),
))
.allAsync();

const edges = routes.map(route => ({
sourceObjectRid: airportsByCodes.get(route.origin!)!.rid!,
targetObjectRid: airportsByCodes.get(route.dest!)!.rid!,
intermediaryObjectRids: [route.rid!],
}));

return {
edges
};
}

}
```