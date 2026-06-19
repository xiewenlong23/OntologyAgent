<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/unit-test-getting-started/
---
# Getting started
Functions 自带对 [Jest ↗](https://jestjs.io/) 单元测试的支持。按照本指南中的步骤为你的 repository 设置单元测试工具。

Functions ships with support for [Jest ↗](https://jestjs.io/) unit tests. Follow the steps in this guide to get unit testing tools set up for your repository.
默认情况下，functions 包含一个位于测试文件 `functions-typescript/src/__tests__/index.ts` 中的单元测试。你可以在 `__tests__` 文件夹中的任何位置创建测试文件。

By default, functions includes a unit test located in the test file `functions-typescript/src/__tests__/index.ts`. You can create test files anywhere in the `__tests__` folder.
## Example
例如，我们可能想要测试 `functions-typescript/src/index.ts` 中的以下 function `addOne`：

For example, we may want to test the following function `addOne` in `functions-typescript/src/index.ts`:
```typescript
import { Function, Integer } from "@foundry/functions-api";

export class MyFunctions {

@Function()
public addOne(n: Integer): Integer {
return n + 1;
}
}
```
我们可以通过编写以下测试 `test add one` 来测试 function `addOne`：

We can test the function `addOne` by writing the following test `test add one`:
```typescript
import { MyFunctions } from ".."

describe("example test suite", () => {
const myFunctions = new MyFunctions();
test("test add one", () => {
expect(myFunctions.addOne(42)).toEqual(43);
});
});
```
有关你可用的完整测试 API 的详细信息，请参阅 [Jest API ↗](https://jestjs.io/docs/en/api)。

Refer to the [Jest API ↗](https://jestjs.io/docs/en/api) for details about the full testing API available to you.
## Running tests
你可以通过点击位于右上角的 `Test` 按钮来运行所有测试，或者通过点击每个测试行号旁边的三角形"播放"按钮来单独运行每个测试。

You can run all your tests by clicking on the `Test` button located on the top right, or run each individual test by clicking on the triangular "Play" button located beside the line number for each test.
![button-run-tests](/docs/resources/foundry/functions/button-run-tests.png)
当你点击 **Commit** 时，所有测试也会在 Checks 中运行：

When you click **Commit**, all tests will also run in Checks:

> 📷 **[图片: run-tests]**

> 📷 **[图片: run-tests]**

## Next steps
接下来，了解可用于测试与 Ontology 交互的 functions 的各种选项：

Next, learn about the range of options available for testing functions that interact with the Ontology:
* [创建 stub objects](/docs/foundry/functions/unit-test-stub-objects/)

* [验证 Ontology 编辑](/docs/foundry/functions/unit-test-ontology-edits/)

* [Stub Object 搜索和聚合](/docs/foundry/functions/unit-test-object-searches/)

* [Create stub objects](/docs/foundry/functions/unit-test-stub-objects/)
* [Verify Ontology edits](/docs/foundry/functions/unit-test-ontology-edits/)
* [Stub Object searches and aggregations](/docs/foundry/functions/unit-test-object-searches/)