<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/edits-generate-id/
---
# Generate unique IDs for new objects
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更[强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 和可配置 resource requests 的支持，我们建议[迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
在编写用于创建 objects 的 [Ontology edit function](/docs/foundry/functions/edits-overview/) 时，您可能希望为新创建的 object 生成一个唯一 ID。您可以在 functions 中通过使用 `@foundry/functions-utils` 包来生成全局唯一标识符。

When writing an [Ontology edit function](/docs/foundry/functions/edits-overview/) that creates objects, you may want to generate a unique ID for the newly created object. You can set this up in functions by using the `@foundry/functions-utils` package to generate a globally unique identifier.
## Import the package
`@foundry/functions-utils` 包默认已安装，但如果该包未出现在 `package.json` 文件中：

The `@foundry/functions-utils` package is installed by default, but if the package is not present in the `package.json` file:
* 在 `"dependencies"` 部分，添加 `"@foundry/functions-utils": "0.1.0"`

* In the `"dependencies"` section, add `"@foundry/functions-utils": "0.1.0"`
如[有关添加依赖项的文档](/docs/foundry/functions/add-dependencies/)中所述，请记得重新启动 Code Assist，以使新包可用于自动补全。

As mentioned in the [documentation on adding dependencies](/docs/foundry/functions/add-dependencies/), remember to restart Code Assist to have the new package available for autocomplete.
## Use the package in code
要生成唯一 ID，您可以使用 `@foundry/functions-utils` 包中的 `Uuid.random()` 工具函数。下面的代码示例展示了如何在 Ontology edit function 示例中使用 `random` 函数。

To generate a unique ID, you can use the `Uuid.random()` utility function from the `@foundry/functions-utils` package. The below code example shows how you could use the `random` function in an example Ontology edit function.
```typescript
import { OntologyEditFunction, Timestamp } from "@foundry/functions-api";
import { Objects } from "@foundry/ontology-api";
import { Uuid } from "@foundry/functions-utils";

export class ExampleEditFunctions {
@Edits(FlightScenario)
@OntologyEditFunction()
public createFlightScenario(): void {
const scenario = Objects.create().flightScenarios(Uuid.random());
scenario.scenarioName = "New scenario";
scenario.creationTime = Timestamp.now();
}
}
```