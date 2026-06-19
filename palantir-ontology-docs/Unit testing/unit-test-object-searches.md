<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/unit-test-object-searches/
---
# Stub object searches and aggregations
在编写单元测试时，您可能希望为 object set 搜索或 object 聚合创建预定义答案（也称为"stubs"），以在编写单元测试时为代码发出的调用指定响应。您需要从 `"@foundry/functions-testing-lib"` 中导入 `{ whenObjectSet }` 才能使用 stubs。

When writing unit tests you may want to create canned answers (also called "stubs") for object sets searches or object aggregations to dictate the responses to the calls your code is making when writing unit tests. You need to import `{ whenObjectSet }` from `"@foundry/functions-testing-lib"` to use stubs.
#### Testing filters on object sets
```typescript
import { Objects } from "@foundry/ontology-api";

const objectSet = Objects.search().objectType();

expect(myFunctions.filterObjectSet(objectSet))
.toEqual(objectSet.filter(s => s.prop.range().gte(0)))
```
#### Testing aggregations on an object property using stubs
您可以使用 stubs 来定义对 aggregation 调用的响应。

You can define the response to aggregation calls using stubs.
```typescript
import { whenObjectSet } from "@foundry/functions-testing-lib"

whenObjectSet(Objects.search().objectType().sum(s => s.property)).thenReturn(55);
```
这意味着每当运行 `Objects.search().objectType().sum(s => s.property))` 时，结果将为 55。

This means that whenever `Objects.search().objectType().sum(s => s.property))` is run, the result will be 55.
#### Testing objects using stubs
您还可以使用 stubs 为某些 object 搜索定义响应。

You can also define the response to certain object searches using stubs.
```typescript
import { whenObjectSet } from "@foundry/functions-testing-lib";

whenObjectSet(Objects.search().objectType().orderBy().takeAsync(10)).thenReturn([employeeObj])
await expect(myFunctions.aggregateSum(objectSet)).resolves.toEqual(65);
```
这意味着每当运行此特定的 objects 搜索 aggregation 时，property 的总和将解析为 65。

This means that whenever this particular objects search aggregation is run, the property sum will resolve to 65.
#### Testing different object sets using stubs
您可以通过重载 search 构造函数来 mock 多个特定的 object set 搜索。您必须为每个 object 提供一个 `rid` property。

You can mock multiple specific object set searches by overloading the search constructor. You must give each object a `rid` property.
```typescript
import { whenObjectSet } from "@foundry/functions-testing-lib";

const objA = Objects.create().objectType('a');
const objB = Objects.create().objectType('b');

objA.rid = 'ridA';
objB.rid = 'ridB';

whenObjectSet(Objects.search().ObjType([objA]).all()).thenReturn([objA]);
whenObjectSet(Objects.search().ObjType([objB, objB]).all()).thenReturn([objA, objB]);
```