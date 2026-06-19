<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/decorators/
---
# Decorators
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更 [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)(包括对 Ontology SDK 的支持以及可配置的资源请求),我们建议 [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
[TypeScript ↗](https://www.typescriptlang.org/docs/handbook/basic-types.html) functions 被声明为 [TypeScript class ↗](https://www.typescriptlang.org/docs/handbook/classes.html) 的方法。要使 function 被发现并发布,需要满足以下几个要求:

[TypeScript ↗](https://www.typescriptlang.org/docs/handbook/basic-types.html) functions are declared as methods of a [TypeScript class ↗](https://www.typescriptlang.org/docs/handbook/classes.html). There are a few requirements for a function to be discovered and published:
* 该方法必须是 `public`

* 该方法所属的类必须从 `functions-typescript/src/index.ts` 文件导出

* 该方法必须使用从 `@foundry/functions-api` 包导入的以下装饰器之一进行装饰：

* `@Function()` 用于通用 functions。

* [`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) 用于将作为 Action 后端的 functions。

* 在使用 [`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) 方法时，可通过 `@Edits([object type])` 装饰器可选地指定 Object 来源信息。

* 如果缺少 `@Edits([object type])` 装饰器，将通过对代码的静态分析以尽力推断的方式获取 Object 来源信息。

* `@Query({ apiName: "userDefinedAPIName"})` 用于希望通过 [Foundry API](/docs/foundry/api/general/overview/introduction/) 执行的只读查询。请注意，此装饰器不应与 `@Function` 装饰器一起使用；应单独使用。

* The method must be `public`
* The class the method belongs to must be exported from the `functions-typescript/src/index.ts` file
* The method must be decorated with one of the following decorators imported from the `@foundry/functions-api` package:
* `@Function()` for generic functions.
* [`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) for functions that will back an Action.
* Object provenance information may be optionally specified with the `@Edits([object type])` decorator when using the[`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) method.
* Object provenance information will be inferred on a best-efforts basis using the static analysis of code if the `@Edits([object type])` decorator is absent.
* `@Query({ apiName: "userDefinedAPIName"})` for read-only queries that you want to execute through [Foundry API](/docs/foundry/api/general/overview/introduction/). Note that this decorator should not be used in addition to the `@Function` decorator; it should be used on its own.
以下是以这种方式正确导出的 function 示例：

Here are examples of functions that are correctly exported in this way:
```typescript
import { Function, OntologyEditFunction, Query, Integer, Edits } from "@foundry/functions-api";
import { Employee } from "@foundry/ontology-api";

export class MyUsefulFunctions {
@Function()
public incrementNumber(x: Integer): Integer {
return x + 1;
}

@Edits(Employee)
@OntologyEditFunction()
public updateName(employee: Employee, newName: string): void {
employee.firstName = newName;
}

@Query({ apiName: "getEmployeesByName" })
public async getEmployeesByName(name: string): Promise<ObjectSet<Employee>> {
return Objects.search().employee().filter(employee => employee.firstName.exactMatch(name));
}
}
```
任何 private 或未使用相关装饰器进行装饰的方法都不会发布到 function registry。这允许用户创建辅助 functions 和工具，以便复用或组织代码。

Any method that is private or not decorated with the relevant decorations will not be published to the function registry. This allows users to create helper functions and utilities for reuse or organization.
> **ℹ️ 注意: 重新发布**

> 请注意，TypeScript 仓库中的每个 function 由其类名和方法名唯一定义——如果您更改类名或方法名，该 function 将以新的标识符发布。
> **ℹ️ 注意: Republishing**

> Note that each function in a TypeScript repository is uniquely defined by its class name and method name—if you change the name of the class or method, the function will be published under a new identifier.