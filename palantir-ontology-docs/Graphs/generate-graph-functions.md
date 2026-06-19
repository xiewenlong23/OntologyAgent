<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/generate-graph-functions/
---
# Generate graphs using Functions
[Functions](/docs/foundry/functions/overview/) 可用于编写复杂的 **Search Around** 函数，从一个或多个 object 出发，返回一个结果图。这些函数可以通过 **Search Around** 工具栏菜单、右键菜单执行，或者在[通过 URL 参数创建图时](/docs/foundry/vertex/generate-graph-apps/)执行。每个函数必须包含恰好一个参数，该参数为 Ontology object type 或 Ontology object 列表，并且函数必须具有返回类型 `IGraphSearchAroundResultV1`，详细说明如下。

[Functions](/docs/foundry/functions/overview/) can be used to write complex **Search Around** functions, starting from one or more objects, and returning a graph of results. These functions can be executed from the **Search Around** toolbar menu, the right click menu, or [when creating a graph using URL parameters](/docs/foundry/vertex/generate-graph-apps/). Each function must have exactly one argument that is an Ontology object type or a list of Ontology objects, and the function must have the return type `IGraphSearchAroundResultV1`, as detailed below.
![UI](/docs/resources/foundry/vertex/graph_generation_and_search_around-ui.jpg)
当通过工具栏或右键菜单使用时，函数可以包含类型为 `Integer`、`Double`、`Float`、`string`、`boolean`、`Timestamp` 或 `Date` 的额外参数。在运行这些 Search Arounds 时，将为用户生成一个表单以输入这些参数。

When used through the toolbar or right click menus, functions may have additional arguments of type `Integer`, `Double`, `Float`, `string`, `boolean`, `Timestamp` or `Date`. When running these Search Arounds, a form will be generated for the user to input those parameters.

> 📷 **[图片: Parameters]**

> 📷 **[图片: Parameters]**

### Search Around functions
**Search Around** 函数在 TypeScript functions 仓库中编写。有关更多信息，请参阅 [Functions 文档](/docs/foundry/functions/overview/)。

**Search Around** functions are written in a TypeScript functions repository. For more information, see the [Functions documentation](/docs/foundry/functions/overview/).
**Search Around** 函数必须声明返回类型为 `IGraphSearchAroundResultV1` 或 `Promise<IGraphSearchAroundResultV1>`。Vertex 将通过函数名称及其返回类型的结构来发现 Search Around 函数，因此必须严格按照以下方式声明：

A **Search Around** function must declare a return type of `IGraphSearchAroundResultV1` or `Promise<IGraphSearchAroundResultV1>`. Vertex will discover the Search Around function using the name and structure of its return type, so it must be declared exactly as follows:
```typescript
export interface IGraphSearchAroundResultV1 {
directEdges?: IGraphSearchAroundResultDirectEdgeV1[];
intermediateEdges?: IGraphSearchAroundResultIntermediateEdgeV1[];
orphanObjectRids?: string[];
objectRidsToGroup?: string[][];
layout?: string;
}

export interface IGraphSearchAroundResultDirectEdgeV1 {
sourceObjectRid: string;
targetObjectRid: string;
linkTypeRid?: string;
label?: string;
direction?: string;
}

export interface IGraphSearchAroundResultIntermediateEdgeV1 {
sourceObjectRid: string;
sourceToIntermediateLinkTypeRid?: string;
intermediateObjectRid: string;
intermediateToTargetLinkTypeRid?: string;
targetObjectRid: string;
label?: string;
direction?: string;
}
```
* `directEdges` 将在图中表示为两个 object 之间的直接边。如果该边基于某个 link，则可以提供在 Ontology 中找到的 `linkTypeRid`，以沿该边显示 link type 的 display name，并使 Vertex 感知边的方向。

* `intermediateEdges` 允许您基于事件或其他中间 object 创建两个 object 之间的边。中间边将表示为两个 object 之间的边，中间 object 会被归入该边中。如果在相同的两个 object 之间返回多个中间边，则所有中间 object 将被归入同一条边中。与直接边一样，如果所表示的关系基于一对 link（一条从源 object 到中间 object，另一条从中间 object 到目标 object），则可以提供这些 link type RID。

* `orphanObjectRids` 允许您返回响应中未与其他 object 建立任何 link 的 object。任何参与了 `directEdges` 或 `intermediateEdges` 中边的 object 都无需在此处返回。

* `objectRidsToGroup` 允许您通过返回一个分组数组来将 object 分组到单个节点，其中每个分组是 object RID 的数组。注意：如果将相同的 RID 添加到多个分组中，这些分组将被合并。

* `label` 允许您为源 object 和目标 object 之间生成的函数 link 指定自定义 label。

* `direction` 允许您更改 Search Around 函数所产生的函数 link 的方向性。提供的值必须是 `NONE`、`FORWARD` 或 `REVERSE` 之一。如果省略，默认为 `FORWARD`。由于存在 `linkTypeRid` 而出现的 link 不受 `direction` 影响。

* `layout` 允许您更改生成的 object 在添加到图中时使用的 layout。提供的值必须是 `auto`、`auto-grid`、`grid`、`linear-row`、`linear-column` 或 `circular` 之一。如果省略，默认为层次 layout。

* 此选项仅在应用程序中直接执行 Search Around 时可用，在从模板生成图时不可用。

* `directEdges` will be represented on the graph as an edge directly between two objects. If this edge is based on a link, its `linkTypeRid` as found in the Ontology can be supplied to show the link type's display name along this edge and make Vertex aware of the edge direction.
* `intermediateEdges` allow you to create edges between two objects based on events or other intermediate objects. An intermediate edge will be represented as an edge between two objects, with the intermediate object grouped into the edge. If many intermediate edges are returned between the same two objects, all intermediate objects will be grouped onto a single edge. As with direct edges, if the relationship represented is based on a pair of links (one from the source object to intermediate object, and a second from the intermediate object to target object), these link type RIDs can be supplied.
* `orphanObjectRids` allow you to return objects that don't have any links to other objects in your response. Any objects that take part in either an edge in `directEdges` or `intermediateEdges` do not need to be returned in here.
* `objectRidsToGroup` allows you to group objects into a single node by returning an array of groups, where each group is an array of object RIDs. Note: If you add the same RID to multiple groups, the groups will be merged together.
* `label` allows you to specify a custom label for the functional link generated between the source and target object.
* `direction` allows you to alter the directionality of the functional link produced by your search around function. The provided value must be one of `NONE`, `FORWARD`, or `REVERSE`. Defaults to `FORWARD` if omitted. Links that appear due to the presence of a `linkTypeRid` are not affected by `direction`.
* `layout` allows you to alter the layout which the resulting objects use when being added to the graph. The provided value must be one of `auto`, `auto-grid`, `grid`, `linear-row`, `linear-column`, or `circular`. Defaults to a hierarchy layout if omitted.
* This option is only available when executing a Search Around directly in the application, and not available when generating a graph from a template.
## Tips & troubleshooting
* 为最大化性能，所有代码应尽可能采用异步方式。

* Vertex 将使用函数的最新已发布版本。要发布您的 Function，您需要使用 semver 版本（例如 1.0.0）对所需的 branch/commit 进行标记。

* 您的仓库需要有权访问函数中要使用的所有 Ontology object 和 link。这可在 **Repository Settings** 的 **Ontology** 部分下进行配置。

* 如果 object type 及其 backing dataset 在与仓库不同的项目中定义，则包含您的仓库的项目将需要引用 backing dataset 和这些 object type。

* To maximize performance, all code should be as asynchronous as possible.
* Vertex will use the latest published version of a function. To publish your Function, you need to tag the branch/commit you want with a semver version, e.g. 1.0.0.
* Your repository needs access to all the Ontology objects & links you want to use in your function. This is configurable under the **Ontology** section of the **Repository Settings**.
* If the object types and their backing datasets are defined in a different project to the repository, the project containing your repository will need a reference to the backing datasets and those object types.
![Troubleshoot](/docs/resources/foundry/vertex/graph_generation_and_search_around-troubleshoot.jpg)
## Reference Examples:
以下示例包含两个 **Search Around** 函数。

The following example contains two **Search Around** functions.
第一个函数 `allFlights` 返回某条航线上的所有航班，并将其合并到 Airports 之间的单条边上。例如，在航线 "SAN -> FAT" 上运行时，它会产生以下结果：

The first function `allFlights` returns all flights along a route, merged onto a single edge between the Airports. For example, when run on route "SAN -> FAT", it produces the following:
![search\_around\_functions-all\_flights](/docs/resources/foundry/vertex/search_around_functions-all_flights.jpg)
第二个函数 `destinations` 允许用户选择一个距离，并返回距初始机场该航班数内的所有机场。例如，在机场 "\[ADK] Adak + Adak Island, AK" 上以距离 2 运行时，它会产生以下结果：

The second function `destinations` allows the user to choose a distance and returns all airports within that number of flights from the initial airport. For example, when run on airport "\[ADK] Adak + Adak Island, AK" with a distance of 2, it produces the following:
![search\_around\_functions-destinations](/docs/resources/foundry/vertex/search_around_functions-destinations.jpg)
```typescript
import { Function, Integer, OntologyObject } from "@foundry/functions-api"
import { ExampleDataAirport, ExampleDataRoute } from "@foundry/ontology-api";

export interface IGraphSearchAroundResultV1 {
directEdges?: IGraphSearchAroundResultDirectEdgeV1[];
intermediateEdges?: IGraphSearchAroundResultIntermediateEdgeV1[];
orphanObjectRids?: string[];
objectRidsToGroup?: string[][];
}

export interface IGraphSearchAroundResultDirectEdgeV1 {
sourceObjectRid: string;
targetObjectRid: string;
linkTypeRid?: string;
}

export interface IGraphSearchAroundResultIntermediateEdgeV1 {
sourceObjectRid: string;
sourceToIntermediateLinkTypeRid?: string;
intermediateObjectRid: string;
intermediateToTargetLinkTypeRid?: string;
targetObjectRid: string;
}

export class VertexSearchArounds {

@Function()
public async allFlights(routes: ExampleDataRoute[]): Promise<IGraphSearchAroundResultV1> {
const flights = await Promise.all(routes.map(route => route.flights.allAsync());

const intermediateEdges: IGraphSearchAroundResultIntermediateEdgeV1[] = [];

for (let i = 0; i < routes.length; i++) {
const route = routes[i];
const flightBetweenOriginAndDestination = flights[i];

const sourceObjectRid = route.departingAirport.get().rid!;
const targetObjectRid = route.arrivingAirport.get().rid!;

for (const flight of flightBetweenOriginAndDestination) {
intermediateEdges.push({
sourceObjectRid,
intermediateObjectRid: flight.rid!,
targetObjectRid,
});
}
}

const result: IGraphSearchAroundResultV1 = {
intermediateEdges,
};
return result;
}

@Function()
public async destinations(airport: ExampleDataAirport, distance: Integer): Promise<IGraphSearchAroundResultV1> {
let currentDistance = 0;
let currentAirports = [airport];

const directEdges: IGraphSearchAroundResultDirectEdgeV1[] = [];

while (currentDistance < distance) {
let nextAirports = new Set<ExampleDataAirport>();

const routesByAirport = await Promise.all(currentAirports.map(airport => airport.routes.allAsync()));
const destinationsByAirport = await Promise.all(
routesByAirport.map(routes =>
Promise.all(routes.map(route => route.arrivingAirport.getAsync()))
)
);

for (let i = 0; i < currentAirports.length; i++) {
const airport = currentAirports[i];
const destinations = destinationsByAirport[i];
for (const destination of destinations) {
directEdges.push({
sourceObjectRid: airport.rid!,
targetObjectRid: destination!.rid!,
});
}
nextAirports.add(destination!);
}

currentAirports = Array.from(nextAirports);
currentDistance++;
}

return { directEdges };
}
}
```