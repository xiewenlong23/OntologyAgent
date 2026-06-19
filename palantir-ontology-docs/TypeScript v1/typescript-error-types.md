<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/typescript-error-types/
---
# Error types
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更 [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 和可配置 resource requests 的支持，我们建议 [迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
除了在 TypeScript function 上声明一个 [output type](/docs/foundry/functions/types-reference/) 之外，您还可以声明一个 error type。这在 queries 的上下文中传播和处理错误时尤其有用。

In addition to declaring an [output type](/docs/foundry/functions/types-reference/) on your TypeScript function, you can also declare an error type. This can be particularly useful for propagating and handling errors in the context of queries.
## Define an error type
您可以使用从 `@foundry/functions-api` 导出的 `FunctionsError` 类型来定义 error type。它接受两个 type parameters；一个 string name 和一个可选的 type（默认为空对象）。任何 function 的 [valid output type](/docs/foundry/functions/types-reference/) 都可用作 error type，包括 objects 和 object sets。

You can define an error type using the `FunctionsError` type exported from `@foundry/functions-api`. It takes two type parameters; a string name and an optional type that defaults to an empty object. Any [valid output type](/docs/foundry/functions/types-reference/) for a function may be used as an error type, including objects and object sets.
您可以将多个 `FunctionsError` 类型 union 在一起，以为一组 function 定义可能的 errors。例如，您可以为获取员工 teammates 的 function 定义以下 error type：

You can union multiple `FunctionsError` types together to define a set of possible errors for your function. For example, you could define the following error type for a function that gets an employee's teammates:
```typescript
import { FunctionsError } from "@foundry/functions-api";
import { Employee } from "@foundry/ontology-api";

type GetTeammatesError =
| FunctionsError<"EmployeeNotFoundForId", string>
| FunctionsError<"MultipleEmployeesFoundForId", { employees: Employee[], employeeId: string }>
```
## Declare an error type on a function
要在 TypeScript function 上声明 error type，可以使用从 `@foundry/functions-api` 导出的 `FunctionsResult` 类型。它接受两个 type parameters；一个 output type 和一个 error type。

To declare an error type on a TypeScript function, you can use the `FunctionsResult` type exported from `@foundry/functions-api`. It takes two type parameters; an output type and an error type.
使用上一节中的 `GetTeammatesError` 示例，您可以像这样在 function 上声明 error type：

Using the `GetTeammatesError` example from the previous section, you can declare the error type on a function like so:
```typescript
import { Function, FunctionsError, FunctionsResult } from "@foundry/functions-api";
import { Employee } from "@foundry/ontology-api";

type GetTeammatesError =
| FunctionsError<"EmployeeNotFoundForId", string>
| FunctionsError<"MultipleEmployeesFoundForId", { employees: Employee[], employeeId: string }>

@Function()
public getTeammates(employeeId: string): FunctionsResult<Employee[], GetTeammatesError> {
...
}
```
请注意，默认情况下 `FunctionsResult` 类型包含一些可由 TypeScript function runtime infrastructure 返回的 errors：

Note that by default the `FunctionsResult` type includes a few errors that can be returned by the TypeScript function runtime infrastructure:
* **`FunctionsTypeScriptExecutorService:CpuTimeoutError`:** 当 function 超过 CPU time limit 时返回。

* **`FunctionsTypeScriptExecutorService:WallTimeoutError`:** 当 function 超过 wall time limit 时返回。

* **`FunctionsTypeScriptExecutorService:OutOfMemoryError`:** 当 function 超过 memory limit 时返回。

* **`FunctionsTypeScriptExecutorService:RuntimeError`:** 当 function 遇到其他 runtime error 时返回。

* **`FunctionsTypeScriptExecutorService:CpuTimeoutError`:** Returned when the function exceeds the CPU time limit.
* **`FunctionsTypeScriptExecutorService:WallTimeoutError`:** Returned when the function exceeds the wall time limit.
* **`FunctionsTypeScriptExecutorService:OutOfMemoryError`:** Returned when the function exceeds the memory limit.
* **`FunctionsTypeScriptExecutorService:RuntimeError`:** Returned when the function encounters some other runtime error.
## Return outputs and errors in your function
要返回 outputs 和 errors，您可以使用从 `@foundry/functions-api` 导出的 `FunctionsResult.ok` 和 `FunctionsResult.err` 方法：

To return outputs and errors, you can use the `FunctionsResult.ok` and `FunctionsResult.err` methods exported from `@foundry/functions-api`:
* **`FunctionsResult.ok`:** 接受一个输出值作为其参数。

* **`FunctionsResult.err`:** 接受一个 error 名称和值作为其参数。

* **`FunctionsResult.ok`:** Takes a single output value as its argument.
* **`FunctionsResult.err`:** Takes an error name and value as its arguments.
使用上一节中的 `getTeammates` 示例，您可以按如下方式返回 outputs 和 errors：

Using the `getTeammates` example from the previous section, you can return outputs and errors like so:
```typescript
import { Function, FunctionsError, FunctionsResult } from "@foundry/functions-api";
import { Employee } from "@foundry/ontology-api";

type GetTeammatesError =
| FunctionsError<"EmployeeNotFoundForId", string>
| FunctionsError<"MultipleEmployeesFoundForId", { employees: Employee[], employeeId: string }>

@Function()
public getTeammates(employeeId: string): FunctionsResult<Employee[], GetTeammatesError> {
const employees = await Objects.search().employee([employeeId]).allAsync();
if (employees.length === 0) {
return FunctionsResult.err("EmployeeNotFoundForId", employeeId);
}

if (employees.length > 1) {
return FunctionsResult.err("MultipleEmployeesFoundForId", { employees, employeeId });
}

const employee = employees[0];
const teammates = await employee.teammates.allAsync();
return FunctionsResult.ok(teammates);
}
```
## Handle errors from queries
当具有 error 类型的 Function 被[从另一个仓库作为 query 调用](/docs/foundry/functions/query-functions/#call-a-query-function)时,它会返回一个 `Result` 类型的响应,该响应可以是 `ok` 或 `err` 结果。

When a function with an error type is [called as a query from another repository](/docs/foundry/functions/query-functions/#call-a-query-function), it returns a `Result` type response, which can be an `ok` or `err` result.
您可以使用从 `@foundry/functions-api` 导出的 `isOk` 或 `isErr` 类型守卫来区分这两种可能的结果。例如,调用上一节中的 `getTeammates` 示例,假设您还[将其作为 query 发布](/docs/foundry/functions/query-functions/#query-decorator),并按如下方式处理响应：

You can use the `isOk` or `isErr` type guards exported from `@foundry/functions-api` to differentiate between the two possible results. For instance, call the `getTeammates` example from the previous section, assuming you also [published it as a query](/docs/foundry/functions/query-functions/#query-decorator), and handle the response like so:
```typescript
import { Function, isOk } from "@foundry/function-api";
import { getTeammates } from "@foundry/ontology-api/queries";

@Function()
public async myFunction(employeeId: string): Promise<string> {
const result = await getTeammates({ employeeId });

if (isOk(result)) {
const teammates = result.value;
// Do something with "teammates" here
...
}

// You can inspect the "name" field to case on each error by name and use the "value" field to get the error value
switch (result.error.name) {
case "EmployeeNotFoundForId": ...
case "MultipleEmployeesFoundForId": ...
case "FunctionsTypescriptExecutorService:OutOfMemoryError": ...
...
}
}
```