<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/api-ontology-edits/
---
# Ontology edits
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更 [强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 和可配置 resource requests 的支持，我们建议 [迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
除了编写基于 Ontology 返回派生值的 functions 之外，您还可以编写用于编辑 Ontology 中对象之间 properties 和 links 的 functions。本页记录了 functions 中可用的对象编辑 API。有关 edit functions 工作原理的更多详细信息，请参阅 [概述页面](/docs/foundry/functions/edits-overview/)。

In addition to writing functions that return derived values based on the Ontology, you can also write functions that edit the properties and links between objects in the Ontology. This page documents the object edit APIs available to you in functions. For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).
要在运营环境中实际使用，**Ontology edit functions 必须配置为一个 Action**，称为 [function-backed Action](/docs/foundry/action-types/function-actions-overview/)。通过这种方式配置 Action 可以让您提供额外的元数据、配置权限，并在各种运营 interfaces 中访问该 Action。正如 [文档](/docs/foundry/functions/edits-overview/#when-edits-are-applied) 中所述，在 Action 之外运行 edit function 实际上不会修改任何对象数据。

To actually be used in an operational context, **Ontology edit functions must be configured as an Action**, known as a [function-backed Action](/docs/foundry/action-types/function-actions-overview/). Configuring an Action in this way allows you to provide additional metadata, configure permissions, and access the Action in various operational interfaces. As noted in the [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied), running an edit function outside of an Action will not actually modify any object data.
> **⚠️ 警告: Warning**

> 在编辑对象后搜索这些对象可能会返回意外结果。有关详细信息，请参阅 [Caveats 部分](/docs/foundry/functions/edits-overview/#edits-and-object-search)。
> **⚠️ 警告: Warning**

> Searching for objects after editing them may return unexpected results. See the [Caveats section](/docs/foundry/functions/edits-overview/#edits-and-object-search) for details.
## Declaring an edit function
编辑 Ontology 的 functions 必须：

Functions that edit the Ontology must:
* 使用从 `@foundry/functions-api` 导入的 `@OntologyEditFunction()` 装饰器进行装饰

* 使用从 `@foundry/functions-api` 导入的 `@Edits([object type])` 装饰器进行装饰，以指定将被编辑的 Object Type

* 具有显式的 `void` 返回类型

* Be decorated with the `@OntologyEditFunction()` decorator imported from `@foundry/functions-api`
* Be decorated with the `@Edits([object type])` decorator imported from `@foundry/functions-api` to specify the object types that will be edited
* Have an explicit `void` return type
## Updating properties
您可以通过简单地为对象的 Property 赋值来编辑 Property 值。例如：

You can edit property values by simply reassigning the property value for an object. For example:
```typescript
employee.lastName = newName;
```
如果您在同一个 Function 执行中稍后访问 `lastName` Property 值，则将返回您刚刚设置的新值。

If you access the `lastName` property value later in the same function execution, the new value that you just set will be returned.
对象上的 [Array properties](/docs/foundry/functions/api-objects-links/#array-properties) 是使用 `ReadOnlyArray` 类型生成的。要修改 Array，请创建它的副本，修改该副本，然后更新 Property：

[Array properties](/docs/foundry/functions/api-objects-links/#array-properties) on objects are generated with the `ReadOnlyArray` type. To modify an array, create a copy of it, modify the copy, then update the property:
```typescript
// Copy to a new array
let arrayCopy = [...myObject.myArrayProperty];
// Now you can modify the copied array
arrayCopy.push(newItem);
// Then overwrite the property value
myObject.myArrayProperty = arrayCopy;
```
请注意，您无法更新现有对象的主键 Property 值。

Note that you cannot update the primary key property value of an existing object.
## Updating links
`SingleLink` 和 `MultiLink` Interface 具有多种可用于更新 Link 的方法：

The `SingleLink` and `MultiLink` interfaces have various methods you can use to update links:
```typescript
// Set an Employee's supervisor
employee.supervisor.set(newSupervisor);

// Clear an Employee's supervisor
employee.supervisor.clear();

// Add a new report to the given employee
employee.reports.add(newReport);

// Remove an old report associated with the given employee
employee.reports.remove(oldReport);
```
与更新 Property 一样，在更新后访问 Link 会反映您所做的更新。

As with updating properties, accessing links after they have been updated reflects the updates you have made.
## Creating objects
您可以使用从 `@foundry/ontology-api` 获取的 `Objects.create()` Interface 来创建新对象。创建新对象时，您必须为其主键指定一个值。

You can create new objects using the `Objects.create()` interface available from `@foundry/ontology-api`. When creating a new object, you have to specify a value for its primary key.
在此示例中，我们使用给定的 ID 创建一个新的 Ticket 对象，设置其 `dueDate` Property，并将其分配给给定的 Employee（通过修改 `assignedTickets` Link）。

In this example, we create a new Ticket object with the given ID, set its `dueDate` property, and assign it to the given Employee (by modifying the `assignedTickets` link).
```typescript
import { OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Employee, Objects, Tickets } from "@foundry/ontology-api";

export class TicketActionFunctions {
@Edits(Employee, Tickets)
@OntologyEditFunction()
public createNewTicketAndAssignToEmployee(employee: Employee, ticketId: Integer): void {
const newTicket = Objects.create().ticket(ticketId);

newTicket.dueDate = LocalDate.now().plusDays(7);

employee.assignedTickets.add(newTicket);
}
}
```
## Deleting objects
您可以通过调用 `.delete()` 方法来删除一个对象。

You can delete an object by calling the `.delete()` method.
在此示例中，我们删除分配给给定 Employee 的所有 Ticket。

In this example, we delete all the tickets assigned to the given employee.
```typescript
const tickets = employee.tickets.all();
tickets.forEach(ticket => ticket.delete());
```
## How edits are captured
当 Ontology edit Function 被执行时，所有对对象的更新都会被 Functions 基础设施捕获，并在 Function 执行结束时返回。这包括通过 `Objects.create()` API 创建的新对象、所有 Property 更新以及对象删除。

When an Ontology edit function is executed, all updates to objects are captured by the functions infrastructure and returned at the end of the function execution. This includes new object creations via the `Objects.create()` API, all property updates, and object deletions.
Edits 会以智能方式合并，以便在 Action 中应用最小化的编辑集合。例如，如果您创建一个新对象然后更新其 Property，则将返回一个包含 Property 更新的单个 **Create Object** Edit。类似地，更新现有对象的多个 Property 将返回一个包含所有 Property 编辑的单个 **Update Object** Edit。删除一个对象将清除删除之前对该对象执行的任何其他 Property 编辑。整个 Function 必须成功执行，才能生成传递给执行原子事务的 Actions service 的编辑列表。

Edits are collapsed intelligently so that the minimal set of edits are applied in an action. For example, if you create a new object and then update its properties, a single **Create Object** edit will be returned containing the property updates. Similarly, updating multiple properties of an existing object will return a single **Update Object** edit containing all of the property edits. Deleting an object will erase any other property edits that were done before the deletion. The entire function must succeed in order to generate the list of edits which is passed to the actions service executing the atomic transaction.
捕获的 Ontology Edits 作为列表从 Function 执行中返回，这就是 Ontology edit Function 必须具有 `void` 或 `Promise<void>` 返回类型的原因。当它们被执行时，函数的真正返回类型是 Ontology Edits 的列表，因此不可能同时返回另一个值。

The captured Ontology edits are returned as a list from the function execution, which is why Ontology edit functions must have a return type of `void` or `Promise<void>`. When they are executed, the true return type of the function is a list of Ontology edits, so it is not possible to simultaneously return another value.
Edits 在单个 Function 执行的整个生命周期中以单个 edit store 进行捕获。这意味着可以调用进入用于创建、更新或删除对象的辅助 Function，即使这些辅助 Function 未作为 Ontology edit Function 发布。例如：

Edits are captured in a single edit store over the entire lifecycle of a single function execution. This means that it is possible to call into helper functions which create, update, or delete objects, even if those helper functions are not published as Ontology edit functions. For example:
```typescript
export class HelperEditFunctions {
@Edits(ObjectA, ObjectB)
@OntologyEditFunction()
public createAndLink(): void {
const objectA = this.createObjectA();
const objectB = this.createObjectB();
objectA.linkToB.set(objectB);
}

/**
* Even though these helper functions are not annotated with @OntologyEditFunction(),
* they can create new objects for use in other edit functions.
*/
private createObjectA(): ObjectA {
const objectA = Objects.create().objectA(this.generateRandomId());
objectA.prop1 = "example";
objectA.prop2 = 42;
return objectA;
}

private createObjectB(): ObjectB {
const objectB = Objects.create().objectB(this.generateRandomId());
objectB.prop1 = "another example";
return objectB;
}

/* Generate your primary keys as needed. For example,
import { Uuid } from "@foundry/functions-utils";
private generateRandomId(){
return Uuid.random();
}
*/
}
```
## Retrieving edited values
当在 function 中完成编辑后，functions 基础设施在您读取时将返回编辑后的值。例如，设置 object 的 property 然后检索它将返回新值：

When edits are done in a function, the functions infrastructure will return the edited values when you read them. For example, setting a property of an object and then retrieving it will return the new value:
```
airplane.departureTime = newDepartureTime;
console.log(airplane.departureTime); // Will log newDepartureTime
```
删除 object 将使其从搜索结果中移除，并防止访问其 properties。

Deleting an object will remove it from search results and prevent access to its properties.
## The @Edits decorator
Actions 可能需要来源信息（provenance information）来强制执行其权限。要为 actions 提供这些信息，您可以使用 `@Edits` 装饰器（decorator）并为您的 function 返回编辑的 object types 指定类型。

Actions may require provenance information to enforce its permissions. To provide actions with this information, you can use the `@Edits` decorator and specify the object types for which your function returns edits.
使用 `@Edits` 装饰器时请考虑以下几点：

Consider the following when using the `@Edits` decorator:
* 编辑 properties 时，应声明被编辑的 object 的类型。

* 编辑一对一或一对多 links 时，应声明具有外键 property 的 object 的类型。

* 编辑 join table links 时，应同时声明源和目标的 object types。

* When editing properties, the type of the object that was edited should be declared.
* When editing one-to-one or one-to-many links, the type of the object with the foreign key property should be declared.
* When editing join table links, both the source and target object types should be declared.
> **⚠️ 警告**

> Functions 对您的代码执行静态分析以自动检测引用的 object types。但是，静态分析*可能无法*正确检测到引用。我们强烈建议您始终使用 `@Edits` 装饰器来提供关于引用的 object types 的来源信息。
> **⚠️ 警告**

> Functions perform static analysis of your code to automatically detect referenced object types. However, static analysis *may fail* to properly detect a reference. We strongly recommend that you always use the `@Edits` decorator to provide provenance information about referenced object types.
对于以下示例，object types `Employee` 和 `Aircraft` 由一个 function 编辑：

For the following example, the object types `Employee` and `Aircraft` are edited by a function:
```typescript
import { OntologyEditFunction } from "@foundry/functions-api";
import { Employee, Aircraft, Objects } from "@foundry/ontology-api";

export class MyOntologyEditFunction {
@Edits(Aircraft, Employee)
@OntologyEditFunction()
public myFunction(): void {
const x = Objects.search().aircraft().all()[0];
x.businessCapacity = 3;
const y = Objects.search().employee().all()[0];
y.department = "HR";
}
}
```
如果您通过 `Objects.search()` API 检索（或物化）先前编辑过的 object，将返回编辑后的值：

If you retrieve (or materialize) a previously edited object through the `Objects.search()` API, the edited value will be returned:
```typescript
import { OntologyEditFunction } from "@foundry/functions-api";
import { Employee, Objects } from "@foundry/ontology-api";

export class CaveatEditFunctions {
@Edits(Employee)
@OntologyEditFunction()
public async editAndSearch(): Promise<void> {
const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
employeeOne.name = "Bob";

// Retrieve the already edited object
const employeeOneAgain = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
console.log(employeeOneAgain.name); // Prints "Bob"
}
}
```