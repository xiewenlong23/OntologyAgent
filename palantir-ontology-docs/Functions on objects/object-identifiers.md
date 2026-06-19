<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/object-identifiers/
---
# Object identifiers
在 Foundry 中，对象的标识有几种不同的表示方式，理解这些不同的表示方式对于在 functions 中编写正确的代码非常重要。本节将介绍标识对象的各种方式及其对代码的影响。

The identity of an object in Foundry is represented in a few different ways, and understanding these different representations can be important for writing correct code in functions. This section explains the various ways that objects are identified and the implications for your code.
## Types of identifiers
### Object RIDs
"RID" 指的是 [Resource Identifier ↗](https://github.com/palantir/resource-identifier)，即 Palantir 的开源规范，用于标识一个实体。Ontology 对象在创建时被分配一个 RID，无论是通过索引底层数据集还是作为 Action 的一部分。

A "RID" refers to a [Resource Identifier ↗](https://github.com/palantir/resource-identifier), Palantir’s open-source specification used to identify an entity. Ontology objects have a RID assigned to them when they are created, either from indexing a backing dataset or as part of an Action.
在 functions 中，每个 [Ontology object](/docs/foundry/functions/api-objects-links/) 都有一个类型为 `string | undefined` 的 `rid` 字段。RID 可能为 undefined 的原因是，可以使用 [object creation](/docs/foundry/functions/api-ontology-edits/#creating-objects) API 在 functions 中创建新对象。新创建的对象的 `rid` 值始终为 `undefined`，而已存在的对象的 `rid` 始终是已定义的。

In functions, every [Ontology object](/docs/foundry/functions/api-objects-links/) has a `rid` field of type `string | undefined`. The reason a RID may be undefined is that it’s possible to create a new object in functions using the [object creation](/docs/foundry/functions/api-ontology-edits/#creating-objects) API. Newly created objects always have a `rid` value of `undefined`, while existing objects always have a defined `rid`.
### Primary keys
对象也可以通过其 object type 和 primary key 进行唯一标识。primary key 是一个唯一的 `propertyId` 和值对。例如，Employee object type 可以通过一个名为 `employeeId` 的 `string` property 进行唯一标识。

Objects can also be uniquely identified by their object type and primary key. A primary key is a unique `propertyId` and value pair. For example, an Employee object type may be uniquely identified by a `string` property called `employeeId`.
所有 Ontology 对象始终具有存在的 `typeId` 和 `primaryKey` 字段，包括新创建的对象。这是因为在创建新对象时需要提供 primary key。

All Ontology objects always have a `typeId` and `primaryKey` field that is present, including newly created objects. This is because you are required to provide the primary key when creating a new object.
## Implications for code
### Checking for equality
在 functions 中，每个 Ontology object 使用 [JavaScript object ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) 表示。一个 Ontology object 可能会被表示为多个 JavaScript object。例如，如果您多次从 [Object search](/docs/foundry/functions/api-object-sets/) 加载同一个 Ontology object，或者从 Object search 加载一个对象的同时该对象又作为参数传入，则可能会出现这种情况：

Within functions, each Ontology object is represented using a [JavaScript object ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object). It’s possible for one Ontology object to be represented as multiple JavaScript objects. For example, this can happen if you load the Ontology object from an [Object search](/docs/foundry/functions/api-object-sets/) multiple times, or load an object from an Object search in addition to having it passed in as a parameter:
```typescript
public myFunction(employee: Employee): void {
const employee2 = Objects.search().employee()
.filter(e => e.id.exactMatch(employee.id))
.all()[0];
console.log(employee == employee2); // false
console.log(employee === employee2); // false
console.log(employee.id === employee2.id); // true
}
```
尽管在上例中 `employee` 和 `employee2` 引用的是同一个概念上的 Ontology object，但使用 `==` 和 `===` 运算符比较它们会返回 `false`，因为这两个变量引用的是两个不同的 JavaScript object。仅比较 `rid` 字段可能存在问题，因为新创建的对象的 `rid` 为 `undefined`。

Even though both `employee` and `employee2` refer to the same conceptual Ontology object in the above example, comparing them using the `==` and `===` operators returns `false` because the variables refer to two distinct JavaScript objects. Simply comparing the `rid` fields can be problematic because newly created objects have a `rid` of `undefined`.
因此，比较两个 Ontology object 是否相等的最佳方式是比较 `typeId` 和 `primaryKey`：

As a result, the best way to compare two Ontology objects for equality is to compare the `typeId` and `primaryKey`:
```typescript
function isEqual(o1: OntologyObject, o2: OntologyObject) {
return o1.typeId === o2.typeId
&& JSON.stringify(o1.primaryKey) == JSON.stringify(o2.primaryKey);
}
```
### Object mappings
存储从对象到某个值的映射通常非常有用。例如，您可能希望遍历一个对象数组并存储其值，以便更高效地进行查找。

It can often be useful to store a mapping from an object to some value. For example, you may want to iterate through an array of objects and store values for more efficient lookup.
由于上述相等性检查的问题，您不能简单地使用 JavaScript Map 来为每个对象存储值。相反，您可以使用 [FunctionsMap](/docs/foundry/functions/types-reference/#collection-types)，它专门设计用于支持将 OntologyObject 用作键。

Because of the equality checking issues described above, you cannot simply use a JavaScript Map to store values for each object. Instead, you can use a [FunctionsMap](/docs/foundry/functions/types-reference/#collection-types) which is specifically designed to support OntologyObjects as keys.