<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/edits-overview/
---
# Ontology edits
**Ontology edit** 是创建、修改或删除 object 的行为。Functions 支持返回 [Ontology edits](/docs/foundry/functions/types-reference/#ontology-edit),供 [function-backed action](/docs/foundry/action-types/function-actions-overview/) 使用。

An **Ontology edit** is the act of creating, modifying, or deleting an object. Functions support returning [Ontology edits](/docs/foundry/functions/types-reference/#ontology-edit) for use in a [function-backed action](/docs/foundry/action-types/function-actions-overview/).
* TypeScript v1 functions 使用 `@OntologyEditFunction` 装饰器编写,该装饰器提供了特殊语义以简化你的代码。TypeScript v1 functions 还使用 [`@Edits` 装饰器](/docs/foundry/functions/api-ontology-edits/#the-edits-decorator) 向 actions 提供 provenance 信息,这些 actions 可以利用该信息来[强制执行权限](/docs/foundry/action-types/permissions/)。你可以使用用于[验证 Ontology edits](/docs/foundry/functions/unit-test-ontology-edits/) 的 API 为 TypeScript v1 Ontology edit functions 编写单元测试。

* TypeScript v2 functions 使用从 `@osdk/functions` 包导出的 [`createEditBatch`](/docs/foundry/functions/typescript-v2-ontology-edits/#construct-an-ontology-edits-batch) function 编写。这些 functions 依赖 `Edits` 类型向 actions 提供 provenance 信息。

* Python functions 通过使用从 Ontology SDK 导出的 [`FoundryClient`](/docs/foundry/functions/python-ontology-edits/#construct-an-ontology-edits-container) 创建一个 edits 容器来编写。这些 functions 依赖 [`@function`](/docs/foundry/functions/python-ontology-edits/#define-an-edit-function) 装饰器的 `edits` 参数向 actions 提供 provenance 信息。

* TypeScript v1 functions are authored using the `@OntologyEditFunction` decorator, which provides special semantics to simplify your code. TypeScript v1 functions also use the [`@Edits` decorator](/docs/foundry/functions/api-ontology-edits/#the-edits-decorator)  to provide actions with provenance information, which the actions may use to [enforce permissions](/docs/foundry/action-types/permissions/). You can write unit tests for TypeScript v1 Ontology edit functions using the APIs available for [verifying Ontology edits](/docs/foundry/functions/unit-test-ontology-edits/).
* TypeScript v2 functions are authored using the [`createEditBatch`](/docs/foundry/functions/typescript-v2-ontology-edits/#construct-an-ontology-edits-batch) function exported from the `@osdk/functions` package. These functions rely on the `Edits` type to provide actions with provenance information.
* Python functions are authored by creating an edits container using the [`FoundryClient`](/docs/foundry/functions/python-ontology-edits/#construct-an-ontology-edits-container) exported from the Ontology SDK. These functions rely on the `edits` parameter of the [`@function`](/docs/foundry/functions/python-ontology-edits/#define-an-edit-function) decorator to provide actions with provenance information.
本文档的其余部分将介绍 Ontology edit functions 在幕后是如何工作的,以帮助你更好地理解底层基础设施。

The rest of this document describes how Ontology edit functions work behind the scenes to provide you with a better understanding of the underlying infrastructure.
### When edits are applied
关于 Ontology edit functions 的一个常见误解是:运行它们是否会更新 Ontology 中的 objects。当你在 **Authoring** 中的 functions helper 中运行 Ontology edit function 时,这些 edits 不会应用到实际的 objects 上。使用 function 更新 objects 的唯一方式是按照 [function-backed actions](/docs/foundry/action-types/function-actions-overview/) 文档中的描述,将 action 配置为使用该 function。

A common misunderstanding about Ontology edit functions is whether or not running them will update objects in the Ontology. When you run an Ontology edit function in the functions helper in **Authoring**, edits are not applied to the actual objects. The only way to update objects using a function is by configuring an action to use the function as described in the documentation for [function-backed actions](/docs/foundry/action-types/function-actions-overview/).
这意味着你可以在 functions helper 中自由地运行 Ontology edit functions,以在各种输入上验证结果,无需担心 object 本身会被更新。

This means that you can freely run Ontology edit functions in the functions helper to validate results on various inputs, without concern that the objects themselves will be updated.
![Results pane](/docs/resources/foundry/functions/results-pane-edits.png "Results pane showing edits made to objects.")
### Caveats
#### Edits and object search
对 objects 和 links 的更改会在你的 function 执行完成*之后*传播到 object set API。这意味着 `Objects.search()` API 将使用旧的 objects、properties 和 links。因此,search、filtering、search arounds 和 aggregations 可能无法反映对 Ontology 的 edits,包括创建和删除操作。你的 function 需要手动处理这种情况。

Changes to objects and links are propagated to the object set APIs *after* your function has finished executing. This means that `Objects.search()` APIs will use the old objects, properties, and links. As a result, search, filtering, search arounds, and aggregations may not reflect the edits to the Ontology, including creation and deletion. Your function will need to handle this case manually.
在以下示例中,假设存在一个 ID 为 1 的 Employee。

For the following example, assume there is an Employee with ID 1.
```typescript tab="TypeScript v1"
import { OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Employee, Objects } from "@foundry/ontology-api";

export class CaveatEditFunctions {
@Edits(Employee)
@OntologyEditFunction()
public async editAndSearch(): Promise<void> {
const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
employeeOne.name = "Bob";

const count = await Objects.search().employee().filter(e => e.name.exactMatch("Bob")).count() ?? -1;
console.log(count);
// Expected: 1, Actual: 0
}
}
```
```typescript tab="TypeScript v2"
import { Client } from "@osdk/client";
import { Employee } from "@ontology/sdk";
import { Edits, createEditBatch } from "@osdk/functions";

type OntologyEdit = Edits.Object<Employee>;

async function editAndSearch(client: Client): OntologyEdit[] {
const batch = createEditBatch<OntologyEdit>(client);

const employeeOne = await client(Employee).fetchOne(1);
batch.update(employeeOne, { name: "Bob" });

const count = await client(Employee)
.where({
name: {
$eq: "Bob"
}
})
.aggregate({
$select: {
$count: "unordered"
}
})
.then(response => response.$count);
console.log(count);
// Expected: 1, Actual: 0

return batch.getEdits();
}

export default editAndSearch;
```
```python tab="Python"
from functions.api import function, OntologyEdit
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Employee

@function(edits=[Employee])
def edit_and_search() -> list[OntologyEdit]:
client = FoundryClient()
ontology_edits = client.ontology.edits()

employee = client.ontology.objects.Employee.get(1)
editable_employee = ontology_edits.objects.Employee.edit(employee)
editable_employee.name = "Bob"

count = client.ontology.objects.Employee.where(Employee.object_type.name == "Bob").count().compute()
print(count)
# Expected: 1, Actual: 0

return ontology_edits.get_edits()
```
#### Optional arrays in function-backed actions
在代码仓库中运行 `@OntologyEditFunction` 时,省略的可选数组会被视为 `undefined`,而通过 action 执行该 Function 时,它们会以空数组的形式传入。

While omitted optional arrays are handled as `undefined` when running an `@OntologyEditFunction` in code repositories, they are passed as empty arrays when executing the function through an action.