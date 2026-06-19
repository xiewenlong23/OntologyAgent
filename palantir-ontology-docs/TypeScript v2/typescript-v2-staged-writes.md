<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/typescript-v2-staged-writes/
---
# Staged writes \[Beta]
> **ℹ️ 注意: Beta**

> Staged writes are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development. Contact Palantir Support to request access.
> Live preview and published function preview are only supported in Code Repositories, not in local development or VS Code workspace environments.
Staged writes provide an additional execution model for functions that edit objects in the Ontology. Unlike edits made via regular [Ontology edit functions](/docs/foundry/functions/typescript-v2-ontology-edits/), staged-write functions:
* Provide a read-after-write guarantee for Ontology edits applied in the function. All edits applied within the function are staged and will be reflected in Ontology queries and aggregations later in the function.
* Allow nested calls to other staged-write functions making Ontology edits.
This page shows how to write staged-write functions and documents their unique properties. For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).
## Key differences from regular Ontology edit functions
Staged-write 函数在几个重要方面与常规 edit 函数不同。

Staged-write functions differ from regular edit functions in several important ways.
### Read-after-write guarantee
在 staged-write 函数中,任何 Ontology 数据的读取都将反映函数中之前所做的所有 edits(以及在同一 action execution 中由调用的 staged-write 函数所做的所有 edits)。这些 edits 仅处于暂存状态(staged),对其他用户发起的 queries 或在 execution 上下文之外通过 functions 发起的 queries 不可见。这允许你使用 search requests 和 aggregations 从函数内部查询 Ontology,所有暂存的 edits 都会反映在 query 的结果中。

Within a staged-write function, any Ontology data read will reflect all edits previously made in the function (and all edits made in a calling staged-write function within the same action execution). Such edits are staged only and are not visible in queries made by other users or through functions outside the context of the execution. This allows you to query the Ontology from within the function using search requests and aggregations with all staged edits being reflected in the result of the query.
### No requirement to return edits at the end of the function
常规的 Python 和 TypeScript V2 Ontology edit 函数要求将一批 Ontology edits 作为函数的返回值返回,这些 edits 才能被应用。在 staged-write 函数中,Ontology edits 会被自动暂存,并将在函数 execution 结束时(当 action 完成时)应用到 Ontology。这使函数的返回值可以用于向调用方返回其他信息。

Regular Python and TypeScript V2 Ontology edit functions require returning a batch of Ontology edits as the return value of the function for those edits to be applied. In staged-write functions, the Ontology edits are automatically staged and will be applied to the Ontology at the end of the function execution when the action completes. This frees up the return value of the function to return other information to the caller.
例如,你可以应用一个 action,该 action 执行一个 TypeScript V2 staged-write 函数,然后进行一些 edits,并进一步调用一个 AIP Logic 函数。AIP Logic 函数发起的 Queries 将返回在 TypeScript V2 函数中所做的 Ontology 更改;AIP Logic 函数所做的任何额外 edits 将加入同一组暂存的 edits 中,无需作为 Logic 函数的一部分返回它们。所有暂存的 edits 将在 action 完成后自动应用。

For example, you can apply an action that executes a TypeScript V2 staged-write function which then makes some edits and further calls an AIP Logic function. Queries made by the AIP Logic function will return the Ontology changes made in the TypeScript V2 function; any additional edits made by the AIP Logic function will join the same staged edits without a need to return them as part of the Logic function. All staged edits will be applied automatically once the action completes.
### Atomic execution
staged-write 函数中的所有 operations,包括 queries、function calls 和 AIP Logic executions,都会将其 edits 一起暂存。这些暂存的 edits 会在函数成功完成后被提交(即应用到 Ontology)。如果函数抛出错误,Ontology 将保持不变,并且在 action 重试该函数之前,所有暂存的 edits 将被丢弃。

All operations within a staged-write function, including queries, function calls, and AIP Logic executions, stage their edits together. Those staged edits are committed (that is, applied to the Ontology) after the function completes successfully. If the function throws an error, the Ontology remains unmodified and all staged edits are discarded before the function is retried by the action.
### `WriteableClient`
staged-write 函数使用 `WriteableClient` 而不是标准的 `Client`。`WriteableClient` 提供了直接用于创建、更新和删除 objects 的方法,无需构建 edit batch。

Staged-write functions use a `WriteableClient` instead of the standard `Client`. The `WriteableClient` provides direct methods for creating, updating, and deleting objects without needing to construct an edit batch.
## Define a staged-write function
staged-write 函数必须使用从 `@osdk/functions` 包导出的 `Edits` 类型显式声明将要编辑的 entities。第一个参数必须是 `WriteableClient<T>`,其中 `T` 是该函数将执行的所有 edit 类型的联合。返回值不再受限于 edits 数组,因此你可以返回任何值。以下示例声明了一个将编辑 `Employee` object type 的函数:

Staged-write functions must explicitly declare the entities that will be edited using the `Edits` type exported from the `@osdk/functions` package. The first parameter must be a `WriteableClient<T>` where `T` is the union of all edit types the function will perform. The return value is no longer constrained to be an array of edits so you can return any value. The following example declares a function that will edit the `Employee` object type:
```typescript
import { Employee } from "@ontology/sdk";
import { Edits, Integer } from "@osdk/functions";
import { WriteableClient } from "@osdk/functions/experimental";

type OntologyEdit = Edits.Object<Employee>;

export default async function assignTicket(
client: WriteableClient<OntologyEdit>,
employeeId: string,
ticketId: string
): Promise<Integer> {
// ...
}
```
## Create objects
使用 `WriteableClient` 上的 `create` 方法来创建新 objects。你必须指定 object type 并提供 primary key 的值,以及你希望初始化的任何其他 properties。

Use the `create` method on the `WriteableClient` to create new objects. You must specify the object type and provide a value for the primary key, along with any other properties you want to initialize.
```typescript
import { Employee } from "@ontology/sdk";
import { Edits } from "@osdk/functions";
import { WriteableClient } from "@osdk/functions/experimental";

type OntologyEdit = Edits.Object<Employee>;

async function createEmployee(
client: WriteableClient<OntologyEdit>,
employeeId: string,
firstName: string,
lastName: string
): Promise<Integer> {
await client.create(Employee, {
employeeId: employeeId,
firstName: firstName,
lastName: lastName
});

return employeeId;
}

export default createEmployee;
```
### Creating with generated IDs
当你需要生成一个 ID 然后立即使用它时:

When you need to generate an ID and then use it immediately:
```typescript
import { Ticket } from "@ontology/sdk";
import { Edits, Integer } from "@osdk/functions";
import { WriteableClient } from "@osdk/functions/experimental";
import { randomUUID } from "crypto";

type OntologyEdit = Edits.Object<Ticket>;

async function createTicket(
client: WriteableClient<OntologyEdit>,
title: string
): Promise<string> {
const ticketId = randomUUID();

await client.create(Ticket, {
ticketId: ticketId,
title: title,
status: "open"
});

return ticketId;
}

export default createTicket;
```
## Update objects
### Object properties
使用 `WriteableClient` 上的 `update` 方法来修改 object properties:

Use the `update` method on the `WriteableClient` to modify object properties:
```typescript
await client.update(employee, { lastName: newName });
```
你也可以通过引用 object 的 API name 和 primary key 来更新它:

You can also update an object by referencing its API name and primary key:
```typescript
await client.update({ $apiName: "Employee", $primaryKey: 23 }, { lastName: newName });
```
staged-write 函数不支持 Interface edits。

Interface edits are not supported in staged-write functions.
## Delete objects
你可以通过在 `WriteableClient` 上调用 `delete` 方法来删除一个 object:

You can delete an object by calling the `delete` method on the `WriteableClient`:
```typescript
await client.delete(ticket);
```
也可以使用 primary key 而不是 instance 来删除 objects:

Objects may also be deleted using a primary key instead of an instance:
```typescript
await client.delete({ $apiName: "Ticket", $primaryKey: 12 });
```
## Create or delete links
使用 `WriteableClient` 上的 `link` 和 `unlink` 方法来添加或移除 objects 之间的多对多 links:

Use the `link` and `unlink` methods on the `WriteableClient` to add or remove many to many links between objects:
```typescript
// Assign a ticket to an employee
await client.link(employee, "assignedTickets", ticket);

// Unassign a ticket from an employee
await client.unlink(employee, "assignedTickets", ticket);
```
您还可以使用 API 名称和主键引用 link 的任意一侧：

You can also reference either side of the link with an API name and primary key:
```typescript
await client.link(
{ $apiName: "Employee", $primaryKey: 23 },
"assignedTickets",
{ $apiName: "Ticket", $primaryKey: 12 }
);
```
要编辑 one to many link，请使用 create 或 update object edit 来编辑外键 property。

To edit one to many links, edit the foreign key property using a create or update object edit.
## Read-after-write within a staged-write function
staged-write function 的一个关键优势是能够读取在同一 execution 中刚刚写入的数据。这对于实现需要强一致性的工作流非常有用。

One of the key advantages of staged-write functions is the ability to read data that was just written in the same execution. This is useful for implementing workflows that require immediate consistency.
```typescript
import { Employee, Ticket } from "@ontology/sdk";
import { Edits, Integer } from "@osdk/functions";
import { WriteableClient } from "@osdk/functions/experimental";
import { randomUUID } from "crypto";

type OntologyEdit = Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;

async function assignTicketAndCheckWorkload(
client: WriteableClient<OntologyEdit>,
employeeId: Integer,
title: string
): Promise<{ ticketId: string, totalAssignedTickets: number }> {
const ticketId = randomUUID();

// Create the ticket
await client.create(Ticket, {
ticketId: ticketId,
title: title,
status: "open"
});

// Assign the ticket to the employee
await client.link(
{ $apiName: "Employee", $primaryKey: employeeId },
"assignedTickets",
{ $apiName: "Ticket", $primaryKey: ticketId }
);

// Query the employee's total workload including the newly assigned ticket.
// This works because of the read-after-write guarantee.
const result = await client.aggregate(Ticket, (tickets) =>
tickets
.where(ticket => ticket.assignedTo.employeeId.exactMatch(employeeId))
.where(ticket => ticket.status.exactMatch("open"))
.count()
);

return {
ticketId: ticketId,
totalAssignedTickets: result
};
}

export default assignTicketAndCheckWorkload;
```
## Calling other functions from a staged-write function
当您在 staged-write function 中调用另一个 function 或 query 时，这些操作会参与相同的 staged edits。任何读取都将反映在 execution 中先前 staged 的 edits，并且被调用 function 所做的任何 edits 都会添加到相同的 staged edits 中。这适用于：

When you invoke another function or query from within a staged-write function, those operations participate in the same staged edits. Any reads will reflect edits previously staged in the execution, and any edits the called function makes are added to the same staged edits. This applies to:
* 其他 TypeScript staged-write function

* AIP Logic function
* Ontology query
* Other TypeScript staged-write functions
* AIP Logic functions
* Ontology queries
如果顶层 function 成功完成，则在所有嵌套调用中 staged 的每个 edit 将一起提交。如果任何调用抛出错误，则整个批次将回滚。

If the top-level function completes successfully, every edit staged across the nested calls is committed together. If any call throws, the entire batch is rolled back.
在下面的示例中，`assignTicket` 是一个从同一仓库发布的独立 staged-write function。`bulkAssignTickets` 通过 OSDK 生成的 `$Queries` import 来调用它；每次调用都会将其 edits 添加到相同的 staged edits 中。

In the example below, `assignTicket` is a separate staged-write function published from the same repository. `bulkAssignTickets` calls it via the OSDK-generated `$Queries` import; each invocation adds its edits to the same staged edits.
```typescript
import { Employee, Ticket, $Queries } from "@ontology/sdk";
import { Edits, Integer } from "@osdk/functions";
import { WriteableClient } from "@osdk/functions/experimental";

type OntologyEdit = Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;

async function bulkAssignTickets(
client: WriteableClient<OntologyEdit>,
employeeId: Integer,
ticketIds: string[]
): Promise<Integer> {
let assignedCount = 0;

for (const ticketId of ticketIds) {
// Each call to `assignTicket` stages its edits alongside those of
// the calling function.
await client($Queries.assignTicket).executeFunction({
employeeId: employeeId,
ticketId: ticketId,
});

assignedCount++;
}

// All staged edits across the nested calls will be committed together
// when the top-level function completes.
return assignedCount;
}

export default bulkAssignTickets;
```
## Execution lifecycle
理解 staged edits 何时被提交对于构建可靠的 function 非常重要：

Understanding when staged edits are committed is important for building reliable functions:
1. **Function execution：** 所有操作（create、update、delete、read、嵌套 function 调用）都会被 staged 到 Ontology。它们对 function 本身以及所有嵌套 function 可见，但在提交之前不会出现在当前 execution 之外。

2. **Commit：** 如果 function 成功完成，所有 staged edits 将在 action 结束之前被提交。

3. **Rollback on error：** 如果 function 抛出错误，Ontology 将保持不变，并且所有 staged edits 将被丢弃。然后该 function 将被 action 重试。

1. **Function execution:** All operations (creates, updates, deletes, reads, nested function calls) are staged to the Ontology. They are visible to the function itself and all nested functions but do not appear outside of the current execution until committed.
2. **Commit:** If the function completes successfully, all staged edits are committed before the action finishes.
3. **Rollback on error:** If the function throws an error, the Ontology remains unmodified and all staged edits are discarded. The function is then retried by the action.
```typescript
import { Employee } from "@ontology/sdk";
import { Edits, Integer } from "@osdk/functions";
import { WriteableClient } from "@osdk/functions/experimental";

async function updateEmployeeWithValidation(
client: WriteableClient<Edits.Object<Employee>>,
employeeId: Integer,
newSalary: number
): Promise<Integer> {
// Validate input
if (newSalary < 0) {
// Staged edits will be discarded
throw new Error("Salary cannot be negative");
}

// Update the employee
await client.update(
{ $apiName: "Employee", $primaryKey: employeeId },
{ salary: newSalary }
);

// If we reach here, all staged edits will be committed atomically
}

export default updateEmployeeWithValidation;
```