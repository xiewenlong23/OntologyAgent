<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/typescript-v2-ontology-edits/
---
# Ontology edits
除了编写从 Ontology 读取数据的 function 之外，您还可以编写用于创建 object 以及编辑 object 之间的 property 和 link 的 function。

本页档介绍了在 function 中可用的 object 编辑 API。

有关 edit function 工作原理的更多详细信息，请参阅 [概述页](/docs/foundry/functions/edits-overview/)。

In addition to writing functions that read data from the Ontology, you can also write functions that create objects and edit the properties and links between objects.
This page documents the object edit APIs available to you in functions.
For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).
要使在 function 中创建的 edits 实际生效，Ontology edit functions *必须配置为 [function-backed Action](/docs/foundry/action-types/function-actions-overview/)*。

以这种方式配置 Action 允许你提供额外的元数据、配置权限,并在各种 operational interfaces 中访问该 Action。

正如 [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied) 中所述,在 Action 之外运行 edit function 实际上不会修改任何 object 数据。

For the edits created in a function to actually be applied, Ontology edit functions *must be configured as a [function-backed Action](/docs/foundry/action-types/function-actions-overview/)*.
Configuring an Action in this way allows you to provide additional metadata, configure permissions, and access the Action in various operational interfaces.
As noted in the [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied), running an edit function outside of an Action will not actually modify any object data.
> **⚠️ 警告: Warning**

> 在编辑对象后立即搜索它们可能会返回意外结果。有关详细信息,请参阅 [Caveats 部分](/docs/foundry/functions/edits-overview/#edits-and-object-search)。
> **⚠️ 警告: Warning**

> Searching for objects immediately after editing them may return unexpected results. See the [Caveats section](/docs/foundry/functions/edits-overview/#edits-and-object-search) for details.
## Define an edit function
编辑 Ontology 的 Functions 必须使用从 `@osdk/functions` 包导出的 `Edits` 类型显式声明将被编辑的实体。以下示例声明了一个新类型,表示对 `Employee` 和 `Ticket` object types 的 edits,以及 `Employee` 和 `Ticket` 之间的 link type。对多个实体的 edits 需要使用 `|` 运算符进行连接。

Functions that edit the Ontology must explicitly declare the entities that will be edited using the `Edits` type exported from the `@osdk/functions` package. The following example declares a new type representing edits to the `Employee` and `Ticket` object types, as well as a link type between `Employee` and `Ticket`. Edits to multiple entities need to be joined with the `|` operator.
```typescript
import { Employee, Ticket } from "@ontology/sdk";
import { Edits } from "@osdk/functions";

type OntologyEdit = Edits.Object<Employee> | Edits.Interface<Person> | Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;
```
然后你必须声明该 function 返回新类型 edits 的数组。

You must then declare that the function returns an array of edits of the new type.
```typescript
export default function createNewTicketAndAssignToEmployee(): OntologyEdit[] {
// ...
}
```
## Construct an Ontology edits batch
要在 TypeScript v2 function 中执行 Ontology edits,首先使用从 `@osdk/functions` 导出的 `createEditBatch` function 构造一个 Ontology edits batch,将先前声明的类型作为类型参数传入:

To perform Ontology edits in a TypeScript v2 function, first construct an Ontology edits batch using the `createEditBatch` function exported from `@osdk/functions`, passing the previously declared type as a type argument:
```typescript
import { Employee, Ticket } from "@ontology/sdk";
import { Client } from "@osdk/client";
import { createEditBatch, Edits } from "@osdk/functions";

type OntologyEdit = Edits.Object<Employee> | Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;

export default function createNewTicketAndAssignToEmployee(client: Client): OntologyEdit[] {

const batch = createEditBatch<OntologyEdit>(client);
// ...
}
```
此 batch 用于跟踪 function 中所做的所有 edits。

This batch is used to keep track of all edits made in a function.
## Update properties
### Object properties
使用在所创建 batch 上可用的 `update` 方法来修改一个或多个 object properties:

Use the `update` method available on the created batch to modify one or more object properties:
```typescript
batch.update(employee, { lastName: newName });
```
如果你尚未将 `employee` object instance 加载到内存中,也可以通过引用 object 的 API name 和 primary key 来更新它:

If you have not loaded the `employee` object instance into memory, you can also update it by referencing the object's API name and primary key:
```typescript
batch.update({ $apiName: "Employee", $primaryKey: 23 }, { lastName: newName });
```
在同一 function 执行的后续部分中,对 `employee` 的 `lastName` property 值的访问将*不会*反映你在 edit batch 上调用 `update` 时所做的更改。

Subsequent access to the `lastName` property value of `employee` later in the same function execution will *not* reflect the changes that you make when calling `update` on the edit batch.
有时,将一个 object type 实例的所有 property 值复制到另一个实例是很有用的。以下示例将 `employee2` 的 property 值分配给 `employee1`:

Sometimes, it is useful to copy all of the property values of one instance of an object type to another instance. The following example assigns the property values of `employee2` to `employee1`:
```typescript
batch.update(employee1, employee2);
```
请注意,现有 object 的 primary key property 值无法更新。

Note that the primary key property value of an existing object cannot be updated.
### Interface properties
你可以使用 `update` 方法通过 Ontology interface 修改 object 的 interface properties。在下面的示例中,`person` 的类型是 Ontology interface,但底层 instance 是实现 `Person` interface 的 object。

You can use the `update` method to modify the interface properties of an object through an Ontology interface. In the example below, the type of `person` is an Ontology interface, but the underlying instance is an object that implements the `Person` interface.
`update` 方法对 object types 和 interfaces 都接受两个参数。对于 interfaces,它接受将被修改的 interface 和要修改的 interface properties。

The `update` method takes two arguments both for object types and interfaces. For interfaces, it takes the interface that will be modified and the interface properties to be modified.
```typescript
batch.update(person, { firstName: newFirstName });
```
请注意,由底层 object 的 primary key property 实现的 interface property 无法更新。

Note that an interface property that is implemented by the primary key property of the underlying object cannot be updated.
## Update links
对于多对多 links,在所创建的 batch 上提供 `link` 和 `unlink` 方法,用于在 objects 之间添加或删除 links。

For many-to-many links, the `link` and `unlink` methods are available on the created batch to add or remove links between objects.
```typescript
// Assign an employee to an office.
batch.link(employee, "office", office);

// Unassign an office from an employee.
batch.unlink(employee, "office", office);
```
For one-to-one and one-to-many links, use the `update` method available on the created batch to modify the foreign key property of the source object. The example below illustrates a one-to-many link. An employee can have multiple tickets, but each ticket can only have one employee.
```typescript
// Assign a ticket to an employee.
batch.update({ $apiName: "Ticket", $primaryKey: 13 }, { assignedEmployeeId: 52 });

// Unassign a ticket.
batch.update({ $apiName: "Ticket", $primaryKey: 13 }, { assignedEmployeeId: undefined });
```
As with updating properties, you can also reference either side of the link with an API name and primary key if you have not loaded a concrete instance of the object type previously.
```typescript
// Assign a ticket to an employee.
batch.link({ $apiName: "Employee", $primaryKey: 23 }, "assignedTickets", { $apiName: "Ticket", $primaryKey: 12 });

// Unassign a ticket from an employee.
batch.unlink({ $apiName: "Employee", $primaryKey: 23 }, "assignedTickets", { $apiName: "Ticket", $primaryKey: 12 });
```
## Create objects
### Objects
You can create new objects using the `create` method on the edit batch. When creating a new object, you must specify a value for its primary key and can optionally initialize any other properties.
In this example, we create a new `Ticket` object with the given ID, set its `dueDate` property, and assign it to the given `Employee` by modifying the `assignedTickets` link. To simplify the calculation of the new value of `dueDate`, we use the `luxon` library.
```typescript
import { Employee, Ticket } from "@ontology/sdk";
import { Client, Osdk } from "@osdk/client";
import { createEditBatch, Edits, Integer } from "@osdk/functions";
import { DateTime } from "luxon";

type OntologyEdit = Edits.Object<Employee> | Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;

export default function createNewTicketAndAssignToEmployee(
client: Client,
employee: Osdk.Instance<Employee>,
ticketId: Integer,
): OntologyEdit[] {
const batch = createEditBatch<OntologyEdit>(client);

batch.create(Ticket, {
ticketId,
dueDate: DateTime.now().plus({ days: 7 }).toFormat('yyyy-MM-dd'),
});

// The new ticket does not exist in the Ontology as a concrete instance, but we can link it
// by referencing its API name and primary key.
batch.link(employee, "assignedTickets", { $apiName: "Ticket", $primaryKey: ticketId });

return batch.getEdits();
}
```
### Interfaces
You can create new object instances through interfaces by calling the `create` method and specifying an interface, underlying object type, and a set of interface properties. One of the interface properties supplied must be implemented by the primary key property of the underlying object type.
```typescript
editBatch.create(Person, {
$objectType: "Employee",
firstName: "John",
lastName: "Doe",
});
```
## Delete objects
### Objects
You can delete an object by calling the `delete` method on the edit batch.
In this example, we delete all the tickets assigned to the given employee:
```typescript
for await (const ticket of employee.$link.assignedTickets.asyncIter()) {
batch.delete(ticket);
}
```
Objects may also be deleted using a primary key instead of an instance:
```typescript
batch.delete({ $apiName: "Ticket", $primaryKey: 12 });
```
### Interfaces
You can delete an object through an interface by calling the `delete` method.
```typescript
batch.delete(person);
```
## Edits on struct properties
Ontology struct properties for both object and interface types can be edited with TypeScript v2 functions. [Struct types](/docs/foundry/functions/types-reference/#structcustom-type) in TypeScript v2 are defined using TypeScript interfaces.  Struct types in functions can be used to edit Ontology struct properties, as long as they contain the same fields as the struct property, with field names matching the API names of the Ontology struct property fields.
```typescript
interface Address {
street: string,
city: string,
state: string,
country: string,
zipcode: string,
}

export default function updateEmployeeAddress(
client: Client,
employee: Osdk.Instance<Employee>,
newAddress: Address
): OntologyEdit[] {
const batch = createEditBatch<OntologyEdit>(client);
batch.update(employee, { address: newAddress });
return batch.getEdits();
}
```