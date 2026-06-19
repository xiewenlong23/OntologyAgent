<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-ontology-edits/
---
# Ontology edits
除了编写从 Ontology 读取数据的 functions 之外，您还可以编写用于创建 objects 以及编辑 objects 之间 properties 和 links 的 functions。

本文档介绍 functions 中可用的 object edit API。

有关 edit functions 工作原理的更多详细信息，请参阅 [概述页面](/docs/foundry/functions/edits-overview/)。

In addition to writing functions that read data from the Ontology, you can also write functions that create objects and edit the properties and links between objects.
This page documents the object edit APIs available to you in functions.
For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).
为了使 function 中创建的 edits 实际生效，Ontology edit functions *必须配置为 [function-backed Action](/docs/foundry/action-types/function-actions-overview/)*。

以这种方式配置 Action 允许您提供额外的元数据、配置权限，并在各种操作 Interface 中访问该 Action。

如 [文档](/docs/foundry/functions/edits-overview/#when-edits-are-applied) 中所述，在 Action 之外运行 edit function 不会实际修改任何 object 数据。

For the edits created in a function to actually be applied, Ontology edit functions *must be configured as a [function-backed Action](/docs/foundry/action-types/function-actions-overview/)*.
Configuring an Action in this way allows you to provide additional metadata, configure permissions, and access the Action in various operational interfaces.
As noted in the [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied), running an edit function outside of an Action will not actually modify any object data.
> **⚠️ 警告: Warning**

> 在编辑 objects 之后立即搜索它们可能会返回意外结果。有关详细信息，请参阅 [Caveats 部分](/docs/foundry/functions/edits-overview/#edits-and-object-search)。
> **⚠️ 警告: Warning**

> Searching for objects immediately after editing them may return unexpected results. See the [Caveats section](/docs/foundry/functions/edits-overview/#edits-and-object-search) for details.
## Define an edit function
编辑 Ontology 的 functions 必须：

Functions that edit the Ontology must:
* 使用从 `functions.api` 导入的 `@function(edits=[MyObjectType])` 装饰器进行装饰，以指定将被编辑的 Object Types。

* 具有从 `functions.api` 导入的显式 `list[OntologyEdit]` 返回类型提示。

* Be decorated with the `@function(edits=[MyObjectType])` decorator imported from `functions.api` to specify the object types that will be edited.
* Have an explicit `list[OntologyEdit]` return type hint imported from `functions.api`.
## Construct an Ontology edits container
要在 Python function 中执行 Ontology edits，首先从 [OSDK client](/docs/foundry/functions/python-functions-on-objects/) 构造一个 Ontology edits 容器。例如：

To perform Ontology edits in a Python function, first construct an Ontology edits container from the [OSDK client](/docs/foundry/functions/python-functions-on-objects/). For example:
```python
ontology_edits = FoundryClient().ontology.edits()
```
此容器用于跟踪 function 中所做的所有 edits。

This container is used to keep track of all edits made in a function.
## Update properties
Python functions 中的 Ontology objects 默认是只读的。修改其 properties 的尝试将引发异常。

Ontology objects in Python functions are read-only by default. Attempts to modify their properties will raise an exception.
要编辑一个 object，首先使用 Ontology edits 容器获取该 object 的可编辑视图，可以来自现有的 object 实例：

In order to edit an object, first obtain an editable view of that object using an Ontology edits container, either from an existing object instance:
```python
editable_object = ontology_edits.objects.MyObjectType.edit(my_object)
```
或给定一个 object primary key：

or given an object primary key:
```python
editable_object = ontology_edits.objects.MyObjectType.edit(object_primary_key)
```
一旦你有了一个可编辑对象（editable object），就可以通过重新赋值该对象的 property 值来编辑 property 值。例如：

Once you have an editable object, you can edit property values by reassigning the property value for an object. For example:
```python
editable_employee.last_name = new_name
```
在同一个 function 执行中，之后访问 `editable_employee` 的 `last_name` property 值将得到刚刚设置的新值。但是，原始的不可编辑对象将*不会*反映这些更改。

Subsequent access to the `last_name` property value of `editable_employee` later in the same function execution will yield the new value that was just set. However, the original non-editable object will *not* reflect the changes.
可编辑对象上的 [Array properties](/docs/foundry/functions/api-objects-links/#array-properties) 是只读的。要修改 array，请创建其副本，修改副本，然后更新该 property：

[Array properties](/docs/foundry/functions/api-objects-links/#array-properties) on editable objects are read-only. To modify an array, create a copy of it, modify the copy, then update the property:
```python
# Copy to a new array
array_copy = list(editable_object.my_array_property)
# Now you can modify the copied array
array_copy.append(new_item)
# Then overwrite the property value
editable_object.my_array_property = array_copy
```
请注意，现有对象的主键（primary key）property 值不能被更新。

Note that the primary key property value of an existing object cannot be updated.
## Update links
Single-link 和 multi-link properties 有多种更新 link 的方法：

Single-link and multi-link properties have various methods for updating links:
```python
# Set an Employee's supervisor
editable_employee.supervisor.set(new_supervisor)

# Clear an Employee's supervisor
editable_employee.supervisor.clear()

# Add a new report to the given employee
editable_employee.reports.add(new_report)

# Remove an old report associated with the given employee
editable_employee.reports.remove(new_report)
```
与更新 properties 一样，在更新之后访问 `editable_employee` 的 links 将反映你所做的更新。

As with updating properties, accessing links of `editable_employee` after they have been updated will reflect the updates you have made.
## Create objects
你可以使用 Ontology edits 容器上的 `MyObjectType.create()` 方法来创建新对象。在创建新对象时，必须为其 primary key 指定一个值。

You can create new objects using the `MyObjectType.create()` method on the Ontology edits container. When creating a new object, you must specify a value for its primary key.
在这个例子中，我们创建了一个具有给定 ID 的新 Ticket 对象，设置其 `due_date` property，并通过修改 `assigned_tickets` link 将其分配给给定的 Employee。

In this example, we create a new Ticket object with the given ID, set its `due_date` property, and assign it to the given Employee by modifying the `assigned_tickets` link.
```python
from datetime import datetime, timedelta

from functions.api import function, Integer, Array, OntologyEdit
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Employee, Ticket

@function(edits=[Employee, Ticket])
def create_new_ticket_and_assign_to_employee(
employee: Employee,
ticket_id: Integer
) -> list[OntologyEdit]:
ontology_edits = FoundryClient().ontology.edits()

new_ticket = ontology_edits.objects.Ticket.create(ticket_id)
new_ticket.due_date = datetime.now() + timedelta(days=7)

editable_employee = ontology_edits.objects.Employee.edit(employee)
editable_employee.assigned_tickets.add(new_ticket)

return ontology_edits.get_edits()
```
除了 primary key 之外，property 值也可以直接传递给 create 方法。例如：

Property values may also be passed directly to the create method in addition to the primary key. For example:
```python
new_due_date = datetime.now() + timedelta(days=7)
new_ticket = ontology_edits.objects.Ticket.create(ticket_id, due_date=new_due_date)
```
## Delete objects
你可以通过调用 Ontology edits 容器上的 `MyObjectType.delete()` 方法来删除一个对象。

You can delete an object by calling the `MyObjectType.delete()` method on the Ontology edits container.
在这个例子中，我们删除了分配给给定员工的所有 tickets：

In this example, we delete all the tickets assigned to the given employee:
```python
for ticket in employee.tickets:
ontology_edits.objects.Ticket.delete(ticket)
```
对象也可以使用 primary key 而不是实例来删除：

Objects may also be deleted using a primary key instead of an instance:
```python
ontology_edits.objects.Ticket.delete(ticket_id)
```