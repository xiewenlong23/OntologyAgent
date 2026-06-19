<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/unit-test-ontology-edits/
---
# Verify Ontology edits
您可以使用 `verifyOntologyEditFunction()` API 来验证 function 执行的编辑操作。您需要从 `"@foundry/functions-testing-lib"` 中导入它。这允许您围绕以下列出的工作流创建单元测试。

You can use the `verifyOntologyEditFunction()` API to verify edits performed by your function. You need to import it from `"@foundry/functions-testing-lib"`. This allows you to create unit tests around the workflows listed below.
#### Verify object creation
您可以使用 `.createsObjects` 方法来验证 object 的创建。以下是一个示例：

You can use the `.createsObjects` method to verify an object creation. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataAirport } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("create airport", () => {
verifyOntologyEditFunction(() => myFunctions.createAirport("airportCode", "airportDisplayName"))
.createsObject(
{
objectType: ExampleDataAirport,
properties: {
airport: "airportCode",
displayAirportName: "airportDisplayName",
},
});
});
});
```
这可以用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataAirport } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataAirport)
@OntologyEditFunction()
public createAirport(airport: string, displayName: string): void {
const newAirport = Objects.create().exampleDataAirport(airport);
newAirport.displayAirportName = displayName;
}
}
```
#### Verify edits on a newly created object
您可以验证涉及新创建 object 的编辑操作。例如，您可能希望创建一个新的 `ExampleDataFlight` object 并验证是否创建了指向 `new-flight-delay-0` 的 link。以下是一个示例：

You can verify edits that are created involving a newly created object. For example, you may want to create a new `ExampleDataFlight` objects and verify that the link is created to the `new-flight-delay-0`. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("single key with single created object", () => {
const flight = Objects.create().exampleDataFlight("flightTest");
verifyOntologyEditFunction(() => myFunctions.createAndLinkDelays(flight, 1))
.createsObject({
objectType: ExampleFlightDelayEvent,
properties: {
eventId: "new-flight-delay-0",
},
})
.addsLink(edits => ({
link: flight.flightDelayEvent,
linkedObject: edits.createdObjects.byObjectType(ExampleFlightDelayEvent)[0],
}))
});
});
```
这可以用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, Integer, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataFlight, ExampleFlightDelayEvent )
@OntologyEditFunction()
public createAndLinkDelays(flight: ExampleDataFlight, numDelay: Integer): void {
for (let n = 0; n < numDelay; n++) {
const delay = Objects.create().exampleFlightDelayEvent(`new-flight-delay-${n}`);
flight.flightDelayEvent.add(delay);
}
}
}
```
#### Verify object property edits
您可以使用 `.modifiesObjects` 来验证对 property 的编辑。以下是一个示例：

You can verify edits to the property using `.modifiesObjects`. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("modifies aircraft of the flight", () => {
const flight = Objects.create().exampleDataFlight("NY -> LA");
const oldAircraft = Objects.create().exampleDataAircraft("N11111");
flight.aircraft.set(oldAircraft);
const newAircraft = Objects.create().exampleDataAircraft("A00000");
verifyOntologyEditFunction(() => myFunctions.assignAircraftToFlight(flight, newAircraft))
.modifiesObject(
{
object: flight,
properties: {
tailNumber: "A00000"
}
})
});
});
```
这可以用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataFlight)
@OntologyEditFunction()
public assignAircraftToFlight(flight: ExampleDataFlight, aircraft: ExampleDataAircraft): void {
flight.aircraft.clear();
aircraft.flight.set(flight);
flight.tailNumber = aircraft.tailNumber;
}
}
```
#### Verify no other edits to an object
您可以使用可选的 `.hasNoMoreEdits()` 来确保没有其他编辑操作。这意味着只允许指定的编辑操作，如果检测到其他编辑操作，验证将失败。以下是一个示例：

You can ensure there are no other edits using the optional `.hasNoMoreEdits()`. This means that only the specified edits are allowed, and the verification will fail if other edits are detected. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("single key with linked object", () => {
const flight = Objects.create().exampleDataFlight("flightAnotherTest");
const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
verifyOntologyEditFunction(() => myFunctions.linkDelays(flight, delay))
.addsLink({link: flight.flightDelayEvent, linkedObject: delay })
.hasNoMoreEdits();
});
});
```
在使用 `.hasNoMoreEdits()` 时，您可以忽略发生的某些类型的编辑操作。您可以通过传递一个包含以下部分或全部字段的对象来实现：

When using `.hasNoMoreEdits()`, you can ignore specific kinds of edits that take place. You do this by passing an object with some or all of the following:
* `ignoreExtraCreatedObjects: true`
* `ignoreExtraModifiedObjects: true`
* `ignoreExtraDeletedObjects: true`
* `ignoreExtraLinkedObjects: true`
* `ignoreExtraUnlinkedObjects: true`
* `ignoreExtraCreatedObjects: true`
* `ignoreExtraModifiedObjects: true`
* `ignoreExtraDeletedObjects: true`
* `ignoreExtraLinkedObjects: true`
* `ignoreExtraUnlinkedObjects: true`
#### Verify link creation to an object
你可以使用 `.addsLink` 验证对象上的 link 创建。以下是一个示例：

You can verify link creation on an object using `.addsLink`. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("single key with linked object", () => {
const flight = Objects.create().exampleDataFlight("flightAnotherTest");
const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
verifyOntologyEditFunction(() => myFunctions.linkDelays(flight, delay))
.addsLink({link: flight.flightDelayEvent, linkedObject: delay })
.hasNoMoreEdits();
});
});
```
此测试等同于测试相反方向的相同 link：

This test is equivalent to testing for the same link going in the opposite direction:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("single key with linked object reverse", () => {
const flight = Objects.create().exampleDataFlight("flightAnotherTest");
const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
verifyOntologyEditFunction(() => myFunctions.linkDelays(flight, delay))
.addsLink({link: delay.flight, linkedObject: flight })
.hasNoMoreEdits();
});
});
```
这可用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataFlight, ExampleFlightDelayEvent )
@OntologyEditFunction()
public linkDelays(flight: ExampleDataFlight, delay: ExampleFlightDelayEvent): void {
flight.flightDelayEvent.add(delay);
}
}
```
#### Verify link removal from an object
你可以使用 `.removesLink` 验证对象上的 link 移除。以下是一个示例：

You can verify link removal from an object using `.removesLink`. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("test link removal", () => {
const flight = Objects.create().exampleDataFlight("flightAnotherTest");
const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
flight.flightDelayEvent.add(delay);
verifyOntologyEditFunction(() => myFunctions.removeAllDelays(flight))
.removesLink({link: flight.flightDelayEvent, unlinkedObject: delay })
.hasNoMoreEdits();
});
});
```
这可用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataFlight, ExampleFlightDelayEvent)
@OntologyEditFunction()
public removeAllDelays(flight: ExampleDataFlight): void {
flight.flightDelayEvent.clear();
}
}
```
#### Verify deleting an object
你可以使用 `.deletesObject` 验证删除对象。以下是一个示例：

You can verify deleting an object using `.deletesObject`. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("test object deletion", () => {
const flight = Objects.create().exampleDataFlight("flightAnotherTest");
verifyOntologyEditFunction(() => myFunctions.deleteFlight(flight))
.deletesObject(flight)
.hasNoMoreEdits();
});
});
```
这可用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataFlight)
@OntologyEditFunction()
public deleteFlight(flight: ExampleDataFlight): void {
flight.delete();
}
}
```
#### Verify multiple objects were created
你可以使用 `.createsObjects` 方法并传入一个列表来创建多个用于测试的对象。以下是一个示例：

You can use the `.createsObjects` method and pass in a list to create multiple objects to test on. Here's an example:
```typescript
import { MyFunctions } from ".."

import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

describe("example test suite", () => {
const myFunctions = new MyFunctions();

test("single key with many created objects", () => {
const flight = Objects.create().exampleDataFlight("flightTest");
verifyOntologyEditFunction(() => myFunctions.createAndLinkDelays(flight, 3))
.createsObjects(
[0, 1, 2].map(i => ({
objectType: ExampleFlightDelayEvent,
properties: {
eventId: "new-flight-delay-" + i,
},
})),
)
.addsLinks(edits =>
edits.createdObjects.byObjectType(ExampleFlightDelayEvent).map(event => ({
link: flight.flightDelayEvent,
linkedObject: event,
})),
)
.hasNoMoreEdits();
});
});
```
这可用于测试以下 function：

This can be used to test the following function:
```typescript
import { Function, Integer, OntologyEditFunction, Edits } from "@foundry/functions-api";
import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(ExampleDataFlight, ExampleFlightDelayEvent )
@OntologyEditFunction()
public createAndLinkDelays(flight: ExampleDataFlight, numDelay: Integer): void {
for (let n = 0; n < numDelay; n++) {
const delay = Objects.create().exampleFlightDelayEvent(`new-flight-delay-${n}`);
flight.flightDelayEvent.add(delay);
}
}
}
```
### Asynchronous ontology edits
你可以按如下方式验证异步的 ontology 编辑：

You can verify asynchronous ontology edits as follows:
```typescript
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";

test("test async edit function", async () => {
const obj = Objects.create().objectWithAllPropertyTypes(1);
(await verifyOntologyEditFunction(() => myFunctions.setDateAndTimestampToNow(obj))).modifiesObject({
object: obj,
properties: {
timestampProperty: makeTimestamp(),
},
});
});
```
### Multiple verifications
正如我们在上面的示例中所看到的，我们可以链式调用验证方法。以下模式说明了这一点：

As we have seen in the examples above, we can chain verifications. The following pattern illustrates this:
```typescript
import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
import { Objects, ExampleDataObject } from "@foundry/ontology-api";

test("multiple action edit", () => {
verifyOntologyEditFunction(() => myFunctions.multistageEdits("objectId", "objectName"))
.createsObject({...})
.modifiesObjects({...})
.addsLinks({...})
.removesLinks({...})
.deletesObject(...)
.hasNoMoreEdits();
});
```