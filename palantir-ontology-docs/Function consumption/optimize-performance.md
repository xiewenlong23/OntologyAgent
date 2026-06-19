<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/optimize-performance/
---
# Optimize performance
此页面描述了优化 function 性能和资源使用的最佳实践。遵循这些指南有助于最大程度地减少计算消耗，并确保您的 function 高效运行。

This page describes best practices for optimizing function performance and resource usage. Following these guidelines helps minimize compute consumption and ensures your functions run efficiently.
> **ℹ️ 提示**

> 有关计算成本以及 function 计费方式的信息，请参阅 [Ontology queries 的计算使用情况](/docs/foundry/ontologies/query-compute-usage/)。
> **ℹ️ 提示**

> For information about compute costs and how functions are metered, see [Compute usage with Ontology queries](/docs/foundry/ontologies/query-compute-usage/).
## Understand function compute costs
Function 的成本由多个组件组成：

The cost of a function has multiple components:
* **Overhead（开销）:** 每个 function execution 都有 4 compute-seconds 的固定开销，无论其执行内容如何。

* **Compute time（计算时间）:** function 执行所需的 vCPU 时间。

* **External calls（外部调用）:** 对平台其他部分（Ontology 查询、模型推理、LLM 调用）的调用会产生各自独立的成本。

* **Overhead:** Each function execution has a fixed overhead of 4 compute-seconds, regardless of what it does.
* **Compute time:** The vCPU time the function needs to execute.
* **External calls:** Calls to other parts of the platform (Ontology queries, model inference, LLM calls) incur their own costs.
有关平台中 compute-seconds 的计算和计量方式的更多信息，请参阅 [Usage types](/docs/foundry/resource-management/usage-types/)。

For more information about how compute-seconds are calculated and measured in the platform, see [Usage types](/docs/foundry/resource-management/usage-types/).
## Use the Performance tab
performance 选项卡提供了一个用于分析和识别 function 性能问题的工具。

The performance tab provides a tool to analyze and identify performance issues with your functions.
![functions-performance-tab](/docs/resources/foundry/functions/functions-performance-tab.png)
waterfall graph 将 operations 表示为沿 X 轴在时间上展开的横向条形图。每个 operation 都有标记，用于指示时间的消耗情况。

The waterfall graph represents operations as horizontal bars stretched out across time on the X-axis. There are markers for each operation to indicate how time is spent.
* **Execute function** 表示执行 function 代码所花费的 CPU 时间。

* **Load objects from arguments** 和 **Load objects from links** 表示调用底层 Ontology backend database service (OSS) 所花费的时间。

* **Execute function** indicates CPU time spent executing the function code.
* **Load objects from arguments** and **Load objects from links** indicate the time spent calling the underlying Ontology backend database service (OSS).
改善 function 性能的方法：

To improve function performance:
* 使用 Objects API 比在 function context 内更快速地聚合和遍历 links（如 [Prefer using the Objects API where possible](#prefer-using-the-objects-api-where-possible) 中所述）。

* 确保 Ontology backend service 的调用以并行方式进行，以避免顺序加载。如果有多个 `async`/`await` 调用，请使用 `Promise.all` 并行等待所有调用。

* 例如，一个常见的模式是对一个 list 使用 `.map()` 来创建 Promises，然后对结果 list 使用 `Promise.all`。

* **重要提示:** 使用 `Promise.all()` 可以提升执行速度，但不会降低 resource consumption 或 cost。操作次数不变——只是并行执行。Bulk operations 既更快又更具成本效益。
* 避免不必要的嵌套循环，因为这会增加执行时间。

* Use the Objects API to aggregate and traverse links more quickly than within function context (as described in [Prefer using the Objects API where possible](#prefer-using-the-objects-api-where-possible)).
* Ensure Ontology backend service calls are done in parallel to avoid sequential loads. If you have multiple `async`/`await` calls, use `Promise.all` to await all the calls in parallel.
* For example, a common pattern is to use `.map()` on a list to create Promises, then use `Promise.all` on the resulting list.
* **Important:** Using `Promise.all()` improves execution speed but does not reduce resource consumption or cost. You still make the same number of operations—they just run in parallel. Bulk operations are both faster and more cost-effective.
* Avoid unnecessary nested loops, which can increase execution time.
## Choose efficient input types
在设计 function 时，您选择的 input parameter 类型会显著影响性能。请使用满足需求的最高效的 input type。

When designing functions, the type of input parameter you choose significantly affects performance. Use the most efficient input type that meets your requirements.
**Best practice（最佳实践）:** 尽可能使用 object sets 以获得最高的效率和可扩展性。

**Acceptable（可接受）:** 当需要在内存中处理 objects 时，使用 object arrays。

**Anti-pattern（反模式）:** Single object parameters 仅应在 object type 仅包含一个实例，或特定业务逻辑确实需要对每个 object 进行单独处理时使用。

**Best practice:** Use object sets when possible for maximum efficiency and scalability.
**Acceptable:** Use object arrays when you need to work with objects in memory.
**Anti-pattern:** Single object parameters should only be used when your object type contains just one instance or when specific business logic genuinely requires per-object processing.
| Input type | Efficiency | Use case |
|------------|------------|----------|
| Object set | Best | Queryable set of objects; no upfront loading cost if you only need aggregations |
| Object array | Good | When you need to iterate over specific objects |
| Single object | Least efficient | When business logic requires processing one object at a time |
### Best practice: Object sets
作为 parameters 传递的 Objects 会触发 Ontology 查询以加载 object 数据。即使是单个 object input 也会触发一次调用以将该 object 加载到内存中。

Objects passed as parameters trigger Ontology queries to load the object data. Even a single object input triggers a call to load that object into memory.
**Object sets** 是更优选择，因为它们会延迟加载，直到您真正需要数据为止。如果您仅需要聚合（例如 count 或 sum），Ontology backend 会在不加载单个 objects 的情况下完成计算。

**Object sets** are preferable because they defer loading until you actually need the data. If you only need an aggregation (like count or sum), the Ontology backend computes it without loading individual objects.
```python tab="Python"
from functions.api import function, Float
from ontology_sdk.ontology.objects import ExampleDataAircraft
from ontology_sdk.ontology.object_sets import ExampleDataAircraftObjectSet

# Less efficient: Single object triggers upfront loading

@function()
def get_aircraft_name(aircraft: ExampleDataAircraft) -> str:
return aircraft.display_name

# Moderate: Array of objects triggers upfront loading

@function()
def get_aircrafts_names(aircraft_array: list[ExampleDataAircraft]) -> list[str]:
return [aircraft.display_name for aircraft in aircraft_array]

# Most efficient: Object set defers loading until needed

# Here, only the aggregated value is loaded in memory of the function
@function()
def count_aircrafts(aircraft_set: ExampleDataAircraftObjectSet) -> Float:
return aircraft_set.count().compute()
```
```typescript tab="TypeScript v2"
// getAircraftName.ts - Less efficient: Single object triggers upfront loading
import { Osdk } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";

export default function getAircraftName(aircraft: Osdk.Instance<ExampleDataAircraft>): string {
return aircraft.displayName!;
}

// getAircraftsNames.ts - Moderate: Array of objects triggers upfront loading
import { Osdk } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";

export default function getAircraftsNames(aircraftArray: Osdk.Instance<ExampleDataAircraft>[]): string[] {
return aircraftArray.map(e => e.displayName!);
}

// countAircrafts.ts - Most efficient: Object set defers loading until needed
// Here, only the aggregated value is loaded in memory of the function
import { ObjectSet } from "@osdk/client";
import { Integer } from "@osdk/functions";
import { ExampleDataAircraft } from "@ontology/sdk";

export default async function countAircrafts(aircraftSet: ObjectSet<ExampleDataAircraft>): Promise<Integer> {
const result = await aircraftSet.aggregate({
$select: { $count: "unordered" }
});
return result.$count;
}
```
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";
import { ObjectSet, ExampleDataAircraft } from "@foundry/ontology-api";

export class MyFunctions {
// Less efficient: Single object triggers upfront loading
@Function()
public getAircraftName(aircraft: ExampleDataAircraft): string {
return aircraft.displayName!;
}

// Moderate: Array of objects triggers upfront loading
@Function()
public getAircraftsNames(aircraftArray: ExampleDataAircraft[]): string[] {
return aircraftArray.map(e => e.displayName!);
}

// Most efficient: Object set defers loading until needed
// Here, only the aggregated value is loaded in memory of the function
@Function()
public async countAircrafts(aircraftSet: ObjectSet<ExampleDataAircraft>): Promise<Integer> {
const count = await aircraftSet.count();
return count!;
}
}
```
## Load objects efficiently
function 中性能问题的常见来源是低效地加载 objects。在循环中逐个加载 objects 会导致每次迭代都与 ontology 发生一次往返。

The common source of performance issues in functions comes from loading objects inefficiently. Loading objects one at a time in a loop causes a round-trip to the ontology on each iteration.
### Anti-pattern: Loading objects one by one
在循环中加载 objects 是一种会显著影响性能的 anti-pattern。每次迭代都会向 Ontology 发起单独的查询：

Loading objects inside a loop is an anti-pattern that significantly impacts performance. Each iteration makes a separate query to the Ontology:
```python tab="Python"
from functions.api import function
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import ExampleDataAircraft

# Anti-pattern: Objects loaded one by one in a loop

@function()
def for_loop_worst(pks_list: list[str]) -> int:
client = FoundryClient()
seats_count = 0

for current_pk in pks_list:
aircrafts = client.ontology.objects.ExampleDataAircraft.where(
ExampleDataAircraft.object_type.tail_number == current_pk
).page()
aircraft = aircrafts.data[0]
seats_count += aircraft.number_of_seats or 0

return seats_count

# Better: Load all objects in one call, then iterate

@function()
def for_loop_better(pks_list: list[str]) -> int:
client = FoundryClient()
seats_count = 0

aircrafts = client.ontology.objects.ExampleDataAircraft.where(
ExampleDataAircraft.object_type.tail_number.in_(pks_list)
)

for aircraft in aircrafts:
seats_count += aircraft.number_of_seats or 0

return seats_count

# Best: Let the backend perform the aggregation

@function()
def for_loop_best(pks_list: list[str]) -> int:
client = FoundryClient()

result = client.ontology.objects.ExampleDataAircraft.where(
ExampleDataAircraft.object_type.tail_number.in_(pks_list)
).sum(ExampleDataAircraft.object_type.number_of_seats).compute()

return int(result or 0)
```
```typescript tab="TypeScript v2"
// forLoopWorst.ts - Anti-pattern: Objects loaded one by one in a loop
import { Client, Osdk } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Integer } from "@osdk/functions";

export default async function forLoopWorst(client: Client, pks_list: string[]): Promise<Integer> {
let seatsCount = 0;

for (const currentPk of pks_list) {
const fetchedPage = await client(ExampleDataAircraft).where({
tailNumber: { $eq: currentPk }
}).fetchPage();
const aircraft = fetchedPage.data[0];
seatsCount += aircraft?.numberOfSeats ?? 0;
}

return seatsCount;
}

// forLoopBetter.ts - Better: Load all objects in one call, then iterate
import { Client, Osdk } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Integer } from "@osdk/functions";

export default async function forLoopBetter(client: Client, pks_list: string[]): Promise<Integer> {
let seatsCount = 0;

const allObjects = client(ExampleDataAircraft).where({
tailNumber: { $in: pks_list }
});

for await (const currentObject of allObjects.asyncIter()) {
seatsCount += currentObject?.numberOfSeats ?? 0;
}

return seatsCount;
}

// forLoopBest.ts - Best: Let the backend perform the aggregation
import { Client } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Integer } from "@osdk/functions";

export default async function forLoopBest(client: Client, pks_list: string[]): Promise<Integer> {
const result = await client(ExampleDataAircraft).where({
tailNumber: { $in: pks_list }
}).aggregate({
$select: { "numberOfSeats:sum": "unordered" }
});

return result.numberOfSeats.sum!;
}
```
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";
import { Objects, ExampleDataAircraft } from "@foundry/ontology-api";

export class MyFunctions {
// Anti-pattern: Objects loaded one by one in a loop
@Function()
public forLoopWorst(pks_list: string[]): Integer {
let seatsCount = 0;

for (const currentPk of pks_list) {
const aircraft = Objects.search()
.exampleDataAircraft()
.filter(o => o.tailNumber.exactMatch(currentPk))
.all()[0];
seatsCount += aircraft.numberOfSeats ?? 0;
}

return seatsCount;
}

// Better: Bulk load objects, then iterate
@Function()
public forLoopBetter(pks_list: string[]): Integer {
const allObjects = Objects.search()
.exampleDataAircraft()
.filter(o => o.tailNumber.exactMatch(...pks_list))
.all();

let seatsCount = 0;
for (const currentObject of allObjects) {
seatsCount += currentObject.numberOfSeats ?? 0;
}

return seatsCount;
}

// Best: Let the backend perform the aggregation
@Function()
public async forLoopBest(pks_list: string[]): Promise<Integer> {
const seatsCount = await Objects.search()
.exampleDataAircraft()
.filter(o => o.tailNumber.exactMatch(...pks_list))
.sum(o => o.numberOfSeats);

return seatsCount!;
}
}
```
### Best practice: Backend aggregations
当您需要计算 count、sum 或 average 等聚合值时，请使用 Ontology backend 的 aggregation 功能，而不是在 function 中加载 objects 后再进行计算。

When you need to compute aggregates like counts, sums, or averages, use the Ontology backend's aggregation capabilities instead of loading objects and computing in your function.
## Prefer using the Objects API where possible
使用 [Workshop's derived properties](/docs/foundry/workshop/widgets-object-table/#function-backed-columns) 时，一种常见的范式是通过聚合每个 object 的 links 来计算 property 值（例如，统计相关 objects 的数量）。

A common paradigm when using [Workshop's derived properties](/docs/foundry/workshop/widgets-object-table/#function-backed-columns) is to calculate the property value by aggregating over each object's links (for example, counting the number of related objects).
虽然下面的代码可以工作，但函数本身必须检索所有链接的 object，然后执行聚合操作（在这种情况下，计算长度）：

Although the code below works, the function itself must retrieve all linked objects, and then perform an aggregation (in this case, calculating the length):
```typescript
@Function()
public async getEmployeeProjectCount(employees: Employee[]): Promise<FunctionsMap<Employee, Integer>> {
const promises = employees.map(employee => employee.workHistory.allAsync());
const allEmployeeProjects = await Promise.all(promises);
let functionsMap = new FunctionsMap();
for (let i = 0; i < employees.length; i++) {
functionsMap.set(employees[i], allEmployeeProjects[i].length);
}
return functionsMap;
}
```
虽然上述方法利用了 async API 和异步函数（参见 [Optimizing link traversals](#optimizing-link-traversals)），但通常使用 Objects API 提供的聚合方法会更有优势：

While the above takes advantage of the async API and asynchronous functions (see [Optimizing link traversals](#optimizing-link-traversals)), it's often beneficial to use the aggregation methods provided by the Objects API:
```typescript
@Function()
public async getEmployeeProjectCount(employees: Employee[]): Promise<FunctionsMap<Employee, Integer>> {
const result: FunctionsMap<Employee, Integer> = new FunctionsMap();
// Get all projects that have an employeeId matching from the employees parameter, then count how many projects are mapped to each employeeId
const aggregation = await Objects.search().project()
.filter(project => project.employeeId.exactMatch(...employees.map(employee => employee.id)))
.groupBy(project => project.employeeId.byFixedWidths(1))
.count();

const map = new Map();
aggregation.buckets.forEach(bucket => {
// bucket.key.min represents the employeeId as each bucket size is 1.
map.set(bucket.key.min, bucket.value);
});
employees.forEach(employee => {
const value = map.get(employee.primaryKey);
if (value === undefined) {
return;
}
result.set(employee, value);
});

return result;
}
```
通过这种方式，您可以一步完成聚合操作，而无需先拉取所有链接的 project。

In this way, you can perform the aggregation in a single step without needing to pull in all linked projects first.
> **ℹ️ 注意**

> 请注意，聚合操作的常规限制仍然适用。特别需要注意的是，对字符串 ID 使用 `.topValues()` 只能返回前 1000 个值。聚合操作目前最大支持 10K buckets，因此您可能需要执行多次聚合才能获得所需结果。更多详情请参见 [Computing Aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations)。
> **ℹ️ 注意**

> Note that the usual limitations of aggregations still apply. In particular, `.topValues()` on string IDs will only return the top 1000 values. Aggregations are currently limited to a maximum of 10K buckets, so you may need to perform multiple aggregations to retrieve the desired result. See [Computing Aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations) for more details.
## Optimizing link traversals
Function 中最常见的性能问题来源是以低效的方式遍历 link。通常，这发生在您编写循环遍历许多 object 的代码，并在每次循环迭代时调用 API 来加载相关 object 的情况下。

The most common source of performance issues in functions comes from traversing links in an inefficient manner. Often, this occurs when you write code that loops over many objects and calls an API to load related objects on every iteration of the loop.
```typescript
for (const employee of employees) {
const pastProjects = employee.workHistory.all();
}
```
在此示例中，循环的每次迭代都将加载单个 employee 的历史 project，这会导致一次数据库往返。为了避免这种性能下降，您可以在一次遍历多个 link 时使用异步 link 遍历 API（`getAsync()` 和 `allAsync()`）。下面是一个编写的用于异步加载 link 的 function 示例：

In this example, each iteration of the loop will load an individual employee's past projects, causing a round-trip to the database. To avoid this slowdown, you can use the asynchronous link traversal APIs (`getAsync()` and `allAsync()`) when traversing many links at once. Below is an example of a function that is written to load links asynchronously:
```typescript
@Function()
public async findEmployeeWithMostProjects(employees: Employee[]): Promise<Employee> {
// Create a Promise to load projects for each employee
const promises = employees.map(employee => employee.workHistory.allAsync());
// Dispatch all the promises, which will load all links in parallel
const allEmployeeProjects = await Promise.all(promises);
// Iterate through the results to find the employee who has the greatest number of projects
let result;
let maxProjectsLength;
for (let i = 0; i < employees.length; i++) {
const employee = employees[i];
const projects = allEmployeeProjects[i];

if (!result || projects.length > maxProjectsLength) {
result = employee;
maxProjectsLength = projects.length;
}
}

return result;
}
```
此示例使用 ES6 [async function ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)，可以方便地处理从 `.getAsync()` 和 `.allAsync()` 方法返回的 `Promise` 返回值。

This example uses an ES6 [async function ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function), which makes it convenient to handle the `Promise` return values that are returned from the `.getAsync()` and `.allAsync()` methods.
## Understand async operations and resource usage
异步操作可以加快 function 执行速度，但可能不会减少资源使用。理解这一区别对于成本优化非常重要。

Asynchronous operations can speed up function execution, but they may not reduce resource usage. Understanding this distinction is important for cost optimization.
```python tab="Python"
from functions.api import function, Float
from ontology_sdk.ontology.object_sets import ExampleDataAircraftObjectSet

# Best: Bulk operation using search around

@function
def bulk_processing(aircraft_set: ExampleDataAircraftObjectSet) -> Float:
all_maintenance_events = aircraft_set.search_around_example_data_aircraft_maintenance_event()
return all_maintenance_events.count().compute()
```
```typescript tab="TypeScript v2"
// forLoopAsync.ts - Faster execution, but still multiple Ontology calls
import { Client, ObjectSet, Osdk } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Integer } from "@osdk/functions";

async function getMaintenanceEventCount(
client: Client,
aircraft: Osdk.Instance<ExampleDataAircraft>
): Promise<Integer> {
const aircraftSet = client(ExampleDataAircraft).where({
tailNumber: { $eq: aircraft.tailNumber }
});
const maintenanceEvents = aircraftSet.pivotTo("exampleDataAircraftMaintenanceEvent");
const result = await maintenanceEvents.aggregate({
$select: { $count: "unordered" }
});
return result.$count ?? 0;
}

export default async function forLoopAsync(
client: Client,
aircraftSet: ObjectSet<ExampleDataAircraft>
): Promise<Integer> {
const allObjects: Osdk.Instance<ExampleDataAircraft>[] = [];
for await (const obj of aircraftSet.asyncIter()) {
allObjects.push(obj);
}

const futures = allObjects.map(obj => getMaintenanceEventCount(client, obj));
const results = await Promise.all(futures);

return results.reduce((sum, count) => sum + count, 0);
}

// bulkProcessing.ts - Best: Single Ontology operation
import { ObjectSet } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Integer } from "@osdk/functions";

export default async function bulkProcessing(
aircraftSet: ObjectSet<ExampleDataAircraft>
): Promise<Integer> {
const allMaintenanceEvents = aircraftSet.pivotTo("exampleDataAircraftMaintenanceEvent");
const result = await allMaintenanceEvents.aggregate({
$select: { $count: "unordered" }
});
return result.$count ?? 0;
}
```
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";
import { ObjectSet, ExampleDataAircraft } from "@foundry/ontology-api";
import { Objects } from "@foundry/ontology-api";

export class MyFunctions {
private async getMaintenanceEventCount(aircraft: ExampleDataAircraft): Promise<Integer> {
const aircraftSet = Objects.search().exampleDataAircraft([aircraft]);
const maintenanceEvents = aircraftSet.searchAroundExampleDataAircraftMaintenanceEvent();
return await maintenanceEvents.count() ?? 0;
}

// Faster execution, but still multiple Ontology calls
@Function()
public async forLoopAsync(aircraftSet: ObjectSet<ExampleDataAircraft>): Promise<Integer> {
const allObjects = aircraftSet.all();
const futures = allObjects.map(obj => this.getMaintenanceEventCount(obj));
const results = await Promise.all(futures);
return results.reduce((sum, count) => sum + count, 0);
}

// Best: Single Ontology operation
@Function()
public async bulkProcessing(aircraftSet: ObjectSet<ExampleDataAircraft>): Promise<Integer> {
const allMaintenanceEvents = aircraftSet.searchAroundExampleDataAircraftMaintenanceEvent();
return await allMaintenanceEvents.count() ?? 0;
}
}
```
> **⚠️ 警告: 异步操作提升的是速度，而非成本**

> 使用 `Promise.all()` 等异步操作可以通过并行运行操作来提高执行速度。但是，重要的是要理解异步操作 **并不能减少资源消耗或成本**——它们只是让事情变得更快。
> **⚠️ 警告: Async operations improve speed, not cost**

> Using asynchronous operations like `Promise.all()` can improve execution speed by running operations in parallel. However, it is important to understand that async operations **do not reduce resource consumption or cost**—they just make things faster.
> 例如，将循环中的单个查询并行化比顺序执行它们更快，但您仍然在进行相同数量的查询。**将计算推到后端的 bulk operation 在速度和资源效率上都优于上述任何方法**。
> For example, parallelizing a loop of individual queries is faster than running them sequentially, but you are still making the same number of queries. **Bulk operations that push computation to the backend are both faster and more resource-effective** than either approach.
## Write efficient ontology edits
在编写用于编辑 object 的 function 时，请应用相同的 bulk-loading 原则。一次性加载所有 object，而不是逐个加载。

When writing functions that edit objects, apply the same bulk-loading principles. Load all objects upfront rather than one at a time.
### Editing large set of objects
When editing large numbers of objects, use pagination (explicit or implicit via `iterate` or `asyncIter`) to process them in manageable chunks without loading everything into memory at once.
```python tab="Python"
from functions.api import function, OntologyEdit
from ontology_sdk.ontology.objects import ExampleDataAircraft
from ontology_sdk.ontology.object_sets import ExampleDataAircraftObjectSet
from ontology_sdk import FoundryClient

# Single object edit

@function(edits=[ExampleDataAircraft])
def edit_aircraft_name(aircraft: ExampleDataAircraft) -> list[OntologyEdit]:
ontology_edits = FoundryClient().ontology.edits()
editable = ontology_edits.objects.ExampleDataAircraft.edit(aircraft)
editable.display_name = "new display name"
return ontology_edits.get_edits()

# Bulk edit using object set with iteration

@function(edits=[ExampleDataAircraft])
def edit_all_aircrafts(aircraft_set: ExampleDataAircraftObjectSet) -> list[OntologyEdit]:
ontology_edits = FoundryClient().ontology.edits()

for aircraft in aircraft_set.iterate():
editable = ontology_edits.objects.ExampleDataAircraft.edit(aircraft)
editable.display_name = "new display name"

return ontology_edits.get_edits()

# Alternative: Pagination

# This processes objects in chunks. The iterate() method above takes care of it behind the scenes.
@function(edits=[ExampleDataAircraft])
def edit_all_with_pagination(aircraft_set: ExampleDataAircraftObjectSet) -> list[OntologyEdit]:
edits = FoundryClient().ontology.edits()

next_token = None
while True:
page = aircraft_set.page(1000, next_token)
for aircraft in page.data:
editable = edits.objects.ExampleDataAircraft.edit(aircraft)
editable.status = "reviewed"

next_token = page.next_page_token
if not next_token:
break

return edits.get_edits()
```
```typescript tab="TypeScript v2"
// editAircraftName.ts - Single object edit
import { Osdk, Client } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Edits, createEditBatch } from "@osdk/functions";

type OntologyEdit = Edits.Object<ExampleDataAircraft>;

export default async function editAircraftName(
client: Client,
aircraft: Osdk.Instance<ExampleDataAircraft>
): Promise<OntologyEdit[]> {
const batch = createEditBatch<OntologyEdit>(client);
batch.update(aircraft, { displayName: "new display name" });
return batch.getEdits();
}

// editAllAircrafts.ts - Bulk edit using object set
import { Client, ObjectSet } from "@osdk/client";
import { ExampleDataAircraft } from "@ontology/sdk";
import { Edits, createEditBatch } from "@osdk/functions";

type OntologyEdit = Edits.Object<ExampleDataAircraft>;

export default async function editAllAircrafts(
client: Client,
aircraftSet: ObjectSet<ExampleDataAircraft>
): Promise<OntologyEdit[]> {
const batch = createEditBatch<OntologyEdit>(client);

for await (const aircraft of aircraftSet.asyncIter()) {
batch.update(aircraft, { displayName: "new display name" });
}

return batch.getEdits();
}
```
```typescript tab="TypeScript v1"
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { ObjectSet, ExampleDataAircraft } from "@foundry/ontology-api";

export class MyFunctions {
// Single object edit
@Edits(ExampleDataAircraft)
@OntologyEditFunction()
public editAircraftName(aircraft: ExampleDataAircraft): void {
aircraft.displayName = "new display name";
}

// Array edit
@Edits(ExampleDataAircraft)
@OntologyEditFunction()
public editAircraftsNames(aircraftArray: ExampleDataAircraft[]): void {
aircraftArray.forEach(aircraft => {
aircraft.displayName = "new display name";
});
}

// Object set edit - most efficient when you need to edit many objects
@Edits(ExampleDataAircraft)
@OntologyEditFunction()
public editAllAircrafts(aircraftSet: ObjectSet<ExampleDataAircraft>): void {
aircraftSet.all().forEach(aircraft => {
aircraft.displayName = "new display name";
});
}
}
```
## Optimize derived column generation
Workshop supports computing derived properties using functions on objects (FOO). Workshop applications typically call these functions with a few dozen rows of content from an object table. The function then returns a map where each object is mapped to the display value in the derived column.
### Base implementation without optimization
Below is a non-optimized implementation that serves as the base case:
```typescript
import { Function, FunctionsMap, Double } from "@foundry/functions-api";
import { Objects, ObjectSet, objectTypeA } from "@foundry/ontology-api";

export class MyFunctions {
/**
* This Function takes an ObjectSet as input, and generates a derived column as output.
* This derived column maps each object instance to the numeric value that will populate the column.
* This implementation is a trivial for-loop that multiplies an object property by a constant value.
* This serves as the base case that we will improve below.
*/
@Function()
public getDerivedColumn_noOptimization(objects: ObjectSet<objectTypeA>, scalar: Double): FunctionsMap<objectTypeA, Double> {
// Define the result map to return
const resultMap = new FunctionsMap<objectTypeA, Double>();

/* There is a limit to the number of objects that can be loaded in memory.
* See enforced limit documentation for current object set load limits.
*/
const allObjs: objectTypeA[] = objects.all();

// For each loaded object, perform the computation. If the result is defined, store it in the result map.
allObjs.forEach(o => {
const result = this.computeForThisObject(o, scalar);
if (result) {
resultMap.set(o, result);
}
});

return resultMap;
}

// An example of a function that computes the required value for the provided object.
private computeForThisObject(obj: objectTypeA, scalar: Double): Double | undefined {
if (scalar === 0) {
// Division by zero error
return undefined;
}
// Checks if exampleProperty is defined, and divides if so. If not, it returns undefined.
return obj.exampleProperty ? obj.exampleProperty / scalar : undefined;
}
}
```
### Parallel execution optimization
If the computation is complex, it is possible to reduce compute time by using asynchronous execution. This way, computations for each object are executed in parallel:
```typescript
import { Function, FunctionsMap, Double } from "@foundry/functions-api";
import { Objects, ObjectSet, objectTypeA, objectTypeB } from "@foundry/ontology-api";

/**
* This function takes a list of strings that are object primaryKeys as input, and generates a derived column as output.
*/
@Function()
public async getDerivedColumn_parallel(objects: ObjectSet<objectTypeA>, scalar: Double): Promise<FunctionsMap<objectTypeA, Double>> {
// Define the result map
const resultMap = new FunctionsMap<objectTypeA, Double>();

/* There is a limit to the number of objects that can be loaded in memory.
* See enforced limit documentation for current object set load limits.
* This should not be a problem as Workshop can lazy-load as users are scrolling.
*/
const allObjs: objectTypeA[] = objects.all();

// Launch parallel computations for each object in the array
const promises = allObjs.map(currObject => this.computeForThisObject(currObject, scalar));

// Use Promise.all to parallelize async execution of helper function
const allResolvedPromises = await Promise.all(promises);

// Populate resultMap with results
for (let i = 0; i < allObjs.length; i++) {
resultMap.set(allObjs[i], allResolvedPromises[i]);
}

return resultMap;
}

// An example of a function that computes the required value for the provided object.
private async computeForThisObject(obj: objectTypeA, scalar: Double): Promise<Double | undefined> {
if (scalar === 0) {
// Division by zero error
return undefined;
}
// Checks if exampleProperty is defined, and divides if so. If not, it returns undefined.
return obj.exampleProperty ? obj.exampleProperty / scalar : undefined;
}
```
### Advanced: Ontology filtering within computation
对于需要查询 Ontology 的每个对象的更复杂情况，请参阅以下示例。

**注意：** 如果使用 `TwoDimensionalAggregation`，在 Workshop 中将填充 [Chart XY widget](/docs/foundry/workshop/widgets-chart/)，情况也是如此。您可以传递一个 category string（bucket）列表进行计算，而不是传递一个 object instance 列表。以下是一个示例：

For more complex cases where each object requires querying the Ontology, see the below examples.
**Note:** The same applies with a `TwoDimensionalAggregation` that would populate a [Chart XY widget](/docs/foundry/workshop/widgets-chart/) in Workshop. You can pass a list of category strings (buckets) to compute, instead of a list of object instances. Below is an example:
```typescript
/**
* An example of a function that computes the required value for the provided object.
* For a given object, query the Ontology (filter for other objects, search-around to another object set, etc.)
*/
@Function()
private async computeForThisObject_filterOntology(obj: objectTypeA): Promise<Double> {
// Create an object set by filtering on some properties
const currObjectSet = await Objects.search().objectTypeB().filter(o => o.property.exactMatch(obj.exampleProperty));
// Note: If there is an existing link between the ObjectTypes, an alternative would be:
// const currObjectSet = await Objects.search().objectTypeA([obj]).searchAroundObjectTypeB();

// Compute the aggregation for this object set
return await this.computeMetric_B(currObjectSet);
}

@Function()
public async computeMetric_B(objs: ObjectSet<objectTypeB>): Promise<Double> {
// Set up calls to different parts of the equation
const promises = [this.sumValue(objs), this.sumValueIfPresent(objs)];

// Execute all promises
const allResolvedPromises = await Promise.all(promises);

// Get values from the promises
const sum = allResolvedPromises[0];
const sumIfPresent = allResolvedPromises[1];

// Perform calculation
return sum / sumIfPresent;
}

@Function()
public async sumValue(objs: ObjectSet<objectTypeB>): Promise<Double> {
// Sum the values of the objects
const aggregation = await objs.sum(o => o.propertyToAggregateB);
const firstBucketValue = aggregation.primaryKeys[0].value;
return firstBucketValue;
}

@Function()
public async sumValueIfPresent(objs: ObjectSet<objectTypeB>): Promise<Double> {
// Sum the object values if they are not null
const aggregation = await objs.filter(o => o.metric.hasProperty()).sum(o => o.propertyToAggregateA);
const firstBucketValue = aggregation.primaryKeys[0].value;
return firstBucketValue;
}
```
### Converting to TwoDimensionalAggregation
要与 Workshop 中的 [Chart XY widget](/docs/foundry/workshop/widgets-chart/) 配合使用，您可以将 FunctionsMap 转换为 TwoDimensionalAggregation：

For use with [Chart XY widgets](/docs/foundry/workshop/widgets-chart/) in Workshop, you can convert a FunctionsMap to a TwoDimensionalAggregation:
```typescript
@Function()
public async getDerivedColumn_parallel_asTwoDimensional(objects: ObjectSet<objectTypeA>, scalar: Double): Promise<TwoDimensionalAggregation<string>> {
const resultMap: FunctionsMap<objectTypeA, Double> = await this.getDerivedColumn_parallel(objects, scalar);

// Create a TwoDimensionalAggregation from the resultMap
const aggregation: TwoDimensionalAggregation<string> = {
// Map the entries (object -> Double) of resultMap to (string -> Double)
buckets: Array.from(resultMap.entries()).map(([key, value]) => ({
key: key.pkProperty, // Use the primary key property
value
})),
};

return aggregation;
}
```