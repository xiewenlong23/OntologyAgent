<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/undefined-values/
---
# Handle undefined values
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 Function。如需更[强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 的支持以及可配置的资源请求，我们建议[迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
以下是在处理访问 Property 或 Link 时可能返回的 `undefined` 值时，两种实用的模式。

Below are two useful patterns for handling `undefined` values which may be returned from accessing properties or links.
### Explicit checks
```typescript
@Function()
public getFullName(employee: Employee): string {
if (!(employee.firstName && employee.lastName)) {
throw new UserFacingError("Cannot derive full name because either first or last name is undefined.");
}
return employee.firstName + " " + employee.lastName;
}
```
通过检查 `firstName` 和 `lastName` 字段是否都已定义，TypeScript 编译器会知道带有 `return` 语句的最后一行可以正确编译。这种方法的好处是类型检查更加明确，并且在存在 `undefined` 值的情况下，您可以抛出更明确的错误来说明问题所在。

By checking that both the `firstName` and `lastName` fields are defined, the TypeScript compiler knows that the final line with the `return` statement can compile correctly. The benefit of this approach is that type checking is more explicit, and in the case where `undefined` values are present, you can throw a more explicit error about what went wrong.
### Non-null assertion operator
您可以使用 TypeScript [非空断言运算符 ↗](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator)（`!`）来忽略 `undefined` 的情况。

You can use the TypeScript [non-null assertion operator ↗](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator) (`!`) to ignore the `undefined` case.
```typescript
@Function()
public getFullName(employee: Employee): string {
return employee.firstName! + " " + employee.lastName!;
}
```
此方法只是覆盖 TypeScript 编译器的检查，并断言您正在访问的字段是已定义的。虽然这样可以使代码更简洁，但当某个字段实际为 `undefined` 时，可能会导致难以理解的错误。我们建议在可能的情况下进行显式检查。

This approach simply overrides the TypeScript compiler and asserts that the fields you're accessing are defined. Although this makes for more concise code, this can lead to cryptic errors in the case when one of the fields turns out to be `undefined`. We recommend making explicit checks when possible.