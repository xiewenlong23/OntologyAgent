<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/unit-test-stub-objects/
---
# Create stub objects
你可以使用 `Objects.create()` 创建并定义你的 mock 对象，其使用方式与常规 function 相同。然后你可以在编写单元测试时使用这些 mock 对象。以下是一个示例：

You can create and define your mock objects using `Objects.create()`, which can be used the same way as if it was a regular function. You can then use these mock objects when writing unit tests. Here is an example:
```typescript
import { MyFunctions } from ".."

import { Objects, ExampleDataAirport } from "@foundry/ontology-api";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("test created objects", () => {
const JFK = Objects.create().exampleDataAirport("JFK Test");
JFK.displayAirportName = "John F. Kennedy International";
expect(myFunctions.getAirportName(JFK)).toEqual("John F. Kennedy International");
});
});
```
作为参考，上述示例使用的是 Jest 语法 [`expect(...).toEqual(...)` ↗](https://jestjs.io/docs/expect#toequalvalue)。

For reference, the above example is using the Jest syntax [`expect(...).toEqual(...)` ↗](https://jestjs.io/docs/expect#toequalvalue).