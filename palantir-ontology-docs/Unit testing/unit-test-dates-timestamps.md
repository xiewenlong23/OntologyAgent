<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/unit-test-dates-timestamps/
---
# Mock dates, timestamps, and UUIDs
您可以通过使用 `jest.spyOn()` 注入一个 mock 来运行测试，从而指定非确定性 function 的输出。

You can specify the output of non-deterministic functions by utilizing `jest.spyOn()` to inject a mock to run the test.
### UUID functions
您可以通过注入 mock 来指定 `Uuid` 的输出。以下是一个示例：

You can specify the output of `Uuid` by injecting a mock. Here is an example:
```typescript
import { MyFunctions } from ".."

import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
import { Uuid } from "@foundry/functions-utils";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("creates new flight", () => {
const makeUuid = () => "my-uuid";
jest.spyOn(Uuid, "random").mockImplementation(() => makeUuid());

verifyOntologyEditFunction(() => myFunctions.createNewFlight())
.createsObject({
objectType: ExampleDataFlight,
properties: {
flightId: makeUuid()
}
})
})
});
```
这可以用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
import { Uuid } from "@foundry/functions-utils";

export class MyFunctions {
@Edits(ExampleDataFlight)
@OntologyEditFunction()
public createNewFlight(): void {
Objects.create().exampleDataFlight(Uuid.random());
}
}
```
#### Advanced UUID functions
在某些情况下，您可能希望完全控制 `Uuid` 的输出。这需要您调整正在测试的 function 的代码。例如，上面的 `createNewFlight` function 被包装在 `MyFunctions` 类中，您可以向该类添加一个构造函数，该函数接受带有默认值的 supplier。使用 supplier 更新后的 function 如下所示：

There are certain circumstances where you may want full control over the output of the `Uuid`. This requires you to adjust the code of the function you are testing. For example, the `createNewFlight` function above is wrapped in a class `MyFunctions` and you can add a constructor to the class that takes a supplier with a default value. The updated function with the supplier looks like this:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
import { Uuid } from "@foundry/functions-utils";

export class MyFunctions {
constructor (private UuidSupplier: () => string = Uuid.random){} // this new constructor in the class takes a supplier

@Edits(ExampleDataFlight)
@OntologyEditFunction()
public createNewFlightWithConstructor(): void {
Objects.create().exampleDataFlight(this.UuidSupplier());
}
}
```
可以使用对输出的完全控制来测试此更新后的 function（在这种情况下，我们将生成的 `Uuid` 设置为 `my-other-uuid`）：

This updated function can be tested with full control of the output (in this case we set the generated `Uuid` to be `my-other-uuid`):
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
import { Uuid } from "@foundry/functions-utils";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("creates new flight with supplier", () => {
const myNewFunctions = new MyFunctions(() => "my-other-uuid");

verifyOntologyEditFunction(() => myNewFunctions.createNewFlightWithConstructor())
.createsObject({
objectType: ExampleDataFlight,
properties: {
flightId: "my-other-uuid"
}
})

})
});
```
### Timestamp.now() functions
您可以通过注入 mock 来指定 `Timestamp.now()` 的输出。以下是一个示例：

You can specify the output of `Timestamp.now()` by injecting a mock. Here is an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
import { Timestamp } from "@foundry/functions-api";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("test timestamp now", () => {
const makeTimestamp = () => Timestamp.fromISOString("2018-06-13T12:11:13+05:00");
jest.spyOn(Timestamp, "now").mockImplementation(() => makeTimestamp());

const flight = Objects.create().exampleDataFlight("flightAnotherTest");
verifyOntologyEditFunction(() => myFunctions.startTakeoff(flight))
.modifiesObject({
object: flight,
properties: {
takeoff: makeTimestamp()
}
})
})
});
```
这可以用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits, Timestamp } from "@foundry/functions-api";
import { Objects, ExampleDataFlight } from "@foundry/ontology-api";

export class MyFunctions {
@Edits(ExampleDataFlight)
@OntologyEditFunction()
public startTakeoff(flight: ExampleDataFlight): void {
flight.takeoff = Timestamp.now();
}
}
```
### LocalDate.now() functions
你可以通过注入 mock 来指定 `LocalDate.now()` 的输出。以下是一个示例：

You can specify the output of `LocalDate.now()` by injecting a mock. Here is an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
import { LocalDate } from "@foundry/functions-api";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("test LocalDate now", () => {
const makeLocalDate = () => LocalDate.fromISOString("2018-06-13");
jest.spyOn(LocalDate, "now").mockImplementation(() => makeLocalDate());

const flight = Objects.create().exampleDataFlight("flightTest");
verifyOntologyEditFunction(() => myFunctions.dateTakeoff(flight))
.modifiesObject({
object: flight,
properties: {
date: makeLocalDate()
}
})
})
});
```
这可以用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits, LocalDate } from "@foundry/functions-api";
import { Objects, ExampleDataFlight } from "@foundry/ontology-api";

export class MyFunctions {
@Edits(ExampleDataFlight)
@OntologyEditFunction()
public dateTakeoff(flight: ExampleDataFlight): void {
flight.date = LocalDate.now();
}
}
```