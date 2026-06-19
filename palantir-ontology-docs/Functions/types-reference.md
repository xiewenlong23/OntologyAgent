<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/types-reference/
---
# Types reference
为了发布到 registry，TypeScript function 必须对所有输入参数具有显式类型注解，并指定显式返回类型。以下是当前支持的 function registry 类型及其对应语言类型的完整列表。

In order to be published to the registry, a TypeScript function must have explicit type annotations on all input parameters and specify an explicit return type. Below is the full list of currently supported function registry types and their corresponding language types.
| Function registry type             | TypeScript v1 type                       | TypeScript v2 type                        | Python type                               |                                           |
|------------------------------------|------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| Attachment                         | `Attachment`                             | `Attachment`                              | `Attachment`                              | [Example](#attachment)                    |
| Boolean                            | `boolean`                                | `boolean`                                 | `bool`                                    | [Example](#boolean)                       |
| Binary                             | Not supported                            | Not supported                             | `bytes`                                   | [Example](#binary)                        |
| Byte                               | Not supported                            | Not supported                             | `int*`                                    | [Example](#byte)                          |
| Classification marking             | `ClassificationMarking`                  | `ClassificationMarking`                   | `ClassificationMarking`                   | [Example](#classification-marking)        |
| Date                               | `LocalDate`                              | `DateISOString`                           | `datetime.date`                           | [Example](#date)                          |
| Decimal                            | Not supported                            | Not supported                             | `decimal.Decimal`                         | [Example](#decimal)                       |
| Double                             | `Double`                                 | `Double`                                  | `float*`                                  | [Example](#double)                        |
| Float                              | `Float`                                  | `Float`                                   | `float`                                   | [Example](#float)                         |
| GeoPoint                           | `GeoPoint`                               | `Point`                                   | `GeoPoint`                                | [Example](#geopoint)                      |
| GeoShape                           | `GeoShape`                               | `Geometry`                                | `GeoShape`                                | [Example](#geoshape)                      |
| Group                              | `Group`                                  | `GroupId`                                 | `GroupId`                                 | [Example](#group)                         |
| Integer                            | `Integer`                                | `Integer`                                 | `int`                                     | [Example](#integer)                       |
| Interface                          | Not supported                            | `Osdk.Instance<MyInterface>`              | Not supported                             | [Example](#interface)                     |
| Interface object set               | Not supported                            | `ObjectSet<MyInterface>`                  | Not supported                             | [Example](#interface-object-set)          |
| List                               | `T[]` or `Array<T>`                      | `T[]` or `Array<T>`                       | `list[T]`                                 | [Example](#list)                          |
| Long                               | `Long`                                   | `Long`                                    | `int*`                                    | [Example](#long)                          |
| Mandatory marking                  | `MandatoryMarking`                       | `MandatoryMarking`                        | `MandatoryMarking`                        | [Example](#mandatory-marking)             |
| Map                                | `FunctionsMap<K, V>`                     | `Record<K, V>`                            | `dict[K, V]`                              | [Example](#map)                           |
| Media reference                    | `MediaItem`                              | `Media`                                   | `Media`                                   | [Example](#media)                         |
| Notification                       | `Notification`                           | `Notification`                            | `Notification`                            | [Example](#notification)                  |
| Object                             | `MyObjectType`                           | `Osdk.Instance<MyObjectType>`             | `MyObjectType`                            | [Example](#object)                        |
| Object set                         | `ObjectSet<MyObjectType>`                | `ObjectSet<MyObjectType>`                 | `MyObjectTypeObjectSet`                   | [Example](#object-set)                    |
| Ontology edit                      | `void`                                   | `Edits`                                   | `OntologyEdit`                            | [Example](#ontology-edit)                 |
| Optional                           | `T \| undefined`                         | `T \| undefined`                          | `typing.Optional` or `T \| None`          | [Example](#optional)                      |
| Principal                          | `Principal`                              | `Principal`                               | `Principal`                               | [Example](#principal)                     |
| Range                              | `IRange<T>`                              | `Range<T>`                                | `Range[T]`                                | [Example](#range)                         |
| Set                                | `Set<T>`                                 | Not supported                             | `set[T]`                                  | [Example](#set)                           |
| Short                              | Not supported                            | Not supported                             | `int*`                                    | [Example](#short)                         |
| String                             | `string`                                 | `string`                                  | `str`                                     | [Example](#string)                        |
| Struct/custom type                 | `interface`                              | `interface`                               | `dataclasses.dataclass`                   | [Example](#structcustom-type)             |
| Timestamp                          | `Timestamp`                              | `TimestampISOString`                      | `datetime.datetime`                       | [Example](#timestamp)                     |
| Two-dimensional aggregation        | `TwoDimensionalAggregation<K, V>`        | `TwoDimensionalAggregation<K, V>`         | `TwoDimensionalAggregation[K, V]`         | [Example](#two-dimensional-aggregation)   |
| Three-dimensional aggregation      | `ThreeDimensionalAggregation<K, S, V>`   | `ThreeDimensionalAggregation<K, S, V>`    | `ThreeDimensionalAggregation[K, S, V]`    | [Example](#three-dimensional-aggregation) |
| User                               | `User`                                   | `UserId`                                  | `UserId`                                  | [Example](#user)                          |
> **ℹ️ 注意**

> 尽管 `Integer` 和 `Long` 都对应于 Python 类型 `int`，但任何在 function signature 中直接标记为 `int` 的字段都将注册为 `Integer` 类型。因此，我们建议改用 API 中的 `Integer` 或 `Long` 类型来注册数值数据类型。类似的指南也适用于 `Float` 和 `Double`；如果 Python 类型 `float` 直接出现在您的 function signature 中，则默认会注册为 `Float`。
> **ℹ️ 注意**

> Although both `Integer` and `Long` correspond to the Python type `int`, any fields marked as `int` directly in your function signature will be registered with type `Integer`. Therefore, we instead recommend using either the `Integer` or `Long` types from the API to register numerical data types. Similar guidelines apply to `Float` and `Double`; if  the Python type `float` is directly in your function signature, it will be registered as `Float` by default.
## Scalar types
标量类型表示单个值，通常用于保存文本、数值或时间数据。

Scalar types represent a single value and are commonly used to hold textual, numeric, or temporal data.
在 JavaScript 和 TypeScript 中，有一个常用的 `number` 类型用于表示整数值和浮点值。为了提供进一步的类型验证和结构化，对于 TypeScript v1 function，我们仅支持从 `@foundry/functions-api` 包导出的数值别名；对于 TypeScript v2 function，则仅支持从 `@osdk/functions` 包导出的数值别名。同样，在 Python function 中处理数值类型时，我们建议使用从 `functions.api` 模块导出的类型别名。

In JavaScript and TypeScript, there is one `number` type that is commonly used to represent both integer and floating-point values. In order to provide further type validation and structure, we only support the numeric aliases exported from the `@foundry/functions-api` package for TypeScript v1 functions and the `@osdk/functions` package for TypeScript v2 functions. Similarly, when working with numeric types in Python functions we recommend using the type aliases exported from the `functions.api` module.
### Boolean
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public isEven(num: Integer): boolean {
return num % 2 === 0;
}
}
```
```typescript tab="TypeScript v2"
import { Integer } from "@osdk/functions";

function isEven(num: Integer): boolean {
return num % 2 === 0;
}

export default isEven;
```
```python tab="Python"
from functions.api import function, Integer

@function
def is_even(num: Integer) -> bool:
return n % 2 == 0
```
### String
```typescript tab="TypeScript v1"
import { Function } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public greet(name: string): string {
return `Hello, ${name}!`;
}
}
```
```typescript tab="TypeScript v2"
function greet(name: string): string {
return `Hello, ${name}!`;
}

export default greet;
```
```python tab="Python"
from functions.api import function

@function
def greet(name: str) -> str:
return f"Hello, {name}!"
```
### Short
表示从 -32,768 到 32,767 的整数值。

Represents integer values from -32,768 to 32,767.
在 Python function 中，`Short` 类型是内置 `int` 类型的别名。

In Python functions, the `Short` type is an alias for the built-in `int` type.
```python tab="Python"
from functions.api import function, Short

@function
def increment(num: Short) -> Short:
return num + 1
```
### Integer
表示从 (-2<sup>31</sup>) 到 (2<sup>31</sup> - 1) 的整数值。

Represents integer values from (-2<sup>31</sup>) to (2<sup>31</sup> - 1).
* 在 TypeScript v1 和 v2 Function 中,`Integer` 类型是内置 `number` 类型的别名。

* 在 Python Function 中,`Integer` 类型是内置 `int` 类型的别名。

* In both TypeScript v1 and v2 functions, the `Integer` type is an alias for the built-in `number` type.
* In Python functions, the `Integer` type is an alias for the built-in `int` type.
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public sum(a: Integer, b: Integer): Integer {
return a + b;
}
}
```
```typescript tab="TypeScript v2"
import { Integer } from "@osdk/functions";

function sum(a: Integer, b: Integer): Integer {
return a + b;
}

export default sum;
```
```python tab="Python"
from functions.api import function, Integer

@function
def sum(a: Integer, b: Integer) -> Integer:
return a + b
```
### Long
表示从 -(2<sup>53</sup> - 1) 到 (2<sup>53</sup> - 1) 的整数值。这些范围等同于 JavaScript 中的 `Number.MIN_SAFE_INTEGER` 和 `Number.MAX_SAFE_INTEGER`,以防止从浏览器上下文调用 Function 时出现精度丢失。

Represents integer values from -(2<sup>53</sup> - 1) to (2<sup>53</sup> - 1). These bounds are equivalent to `Number.MIN_SAFE_INTEGER` and `Number.MAX_SAFE_INTEGER` in JavaScript to prevent precision loss when functions are called from browser contexts.
* 在 TypeScript v1 Function 中,`Long` 类型是内置 `number` 类型的别名。在 TypeScript v2 Function 中,`Long` 类型是内置 `string` 类型的别名。

* 在 Python Function 中,`Long` 类型是内置 `int` 类型的别名。

* In TypeScript v1 functions, the `Long` type is an alias for the built-in `number` type. In TypeScript v2 functions, the `Long` type is an alias for the built-in `string` type.
* In Python functions, the `Long` type is an alias for the built-in `int` type.
```typescript tab="TypeScript v1"
import { Function, Long } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public subtract(a: Long, b: Long): string {
return (BigInt(a) - BigInt(b)).toString();
}
}
```
```typescript tab="TypeScript v2"
import { Long } from "@osdk/functions";

function subtract(a: Long, b: Long): string {
return (BigInt(a) - BigInt(b)).toString();
}

export default subtract;
```
```python tab="Python"
from functions.api import function, Long

@function
def subtract(a: Long, b: Long) -> str:
return str(a - b)
```
### Float
表示 32 位浮点数。

Represents a 32-bit floating-point number.
* 在 TypeScript v1 和 v2 Function 中,`Float` 类型是内置 `number` 类型的别名。

* 在 Python Function 中,`Float` 类型是内置 `float` 类型的别名。

* In both TypeScript v1 and v2 functions, the `Float` type is an alias for the built-in `number` type.
* In Python functions, the `Float` type is an alias for the built-in `float` type.
```typescript tab="TypeScript v1"
import { Float, Function } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public multiply(a: Float, b: Float): Float {
return a * b;
}
}
```
```typescript tab="TypeScript v2"
import { Float } from "@osdk/functions";

function multiply(a: Float, b: Float): Float {
return a * b;
}

export default multiply;
```
```python tab="Python"
from functions.api import function, Float

@function
def multiply(a: Float, b: Float) -> Float:
return a * b
```
### Double
表示 64 位浮点数。

Represents a 64-bit floating-point number.
* 在 TypeScript v1 和 v2 Function 中,`Double` 类型是内置 `number` 类型的别名。

* 在 Python Function 中,`Double` 类型是内置 `float` 类型的别名。

* In both TypeScript v1 and v2 functions, the `Double` type is an alias for the built-in `number` type.
* In Python functions, the `Double` type is an alias for the built-in `float` type.
```typescript tab="TypeScript v1"
import { Double, Function } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public divide(a: Double, b: Double): Double {
return a / b;
}
}
```
```typescript tab="TypeScript v2"
import { Double } from "@osdk/functions";

function divide(a: Double, b: Double): Double {
return a / b;
}

export default divide;
```
```python tab="Python"
from functions.api import function, Double

@function
def divide(a: Double, b: Double) -> Double:
return a / b
```
### Decimal
```python tab="Python"
from decimal import Decimal
from functions.api import function

@function
def return_pi() -> Decimal:
return Decimal('3.1415926535')
```
### Date
表示日历日期。

Represents a calendar date.
```typescript tab="TypeScript v1"
import { Function, LocalDate } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public returnDate(): LocalDate {
return LocalDate.fromISOString("1999-10-17");
}
}
```
```typescript tab="TypeScript v2"
import { DateISOString } from "@osdk/functions";

function returnDate(): DateISOString {
return "1999-10-17";
}

export default returnDate;
```
```python tab="Python"
from datetime import date
from functions.api import function, Date

@function
def return_date() -> Date:
return date.fromisoformat('1999-10-17')
```
### Timestamp
表示一个时间瞬间。

Represents an instant in time.
```typescript tab="TypeScript v1"
import { Function, Timestamp } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getCurrentTimestamp(): Timestamp {
return Timestamp.now();
}
}
```
```typescript tab="TypeScript v2"
import { TimestampISOString } from "@osdk/functions";

function getCurrentTimestamp(): TimestampISOString {
const now = new Date();
return now.toISOString();
}

export default getCurrentTimestamp;
```
```python tab="Python"
from datetime import datetime
from functions.api import function, Timestamp

@function
def get_current_timestamp() -> Timestamp:
return datetime.now()
```
### Binary
在 Python Function 中,`Binary` 类型是内置 `bytes` 类型的别名。

In Python functions, the `Binary` type is an alias for the built-in `bytes` type.
```python tab="Python"
from functions.api import function

@function
def encode_utf8(param: str) -> bytes:
return param.encode('utf-8')
```
### Byte
在 Python Function 中,`Byte` 类型是内置 `int` 类型的别名。

In Python functions, the `Byte` type is an alias for the built-in `int` type.
```python tab="Python"
from functions.api import function, Byte

@function
def get_first_byte(param: str) -> Byte:
if len(param) == 0:
raise Exception("String length cannot be zero.")
return param.encode('utf-8')[0]
```
### Mandatory marking
Marking 是强制性的访问控制机制,要求用户必须具有特定的 marking 才能访问数据,从而限制访问权限。

Markings are mandatory controls that restrict access by requiring a user to have a particular marking in order to access data.
```typescript tab="TypeScript v1"
import { OntologyEditFunction, MandatoryMarking } from "@foundry/functions-api";
import { Employee, Objects } from "@foundry/ontology-api";

export class MyFunctions {
@Edits(Employee)
@OntologyEditFunction()
public async editMandatoryMarkings(markings: MandatoryMarking[]): Promise<void> {
const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
employeeOne.markingsProperty = markings;
}
}
```
```typescript tab="TypeScript v2"
import { Client } from "@osdk/client";
import { Employee } from "@ontology/sdk";
import { Edits, createEditBatch, MandatoryMarking } from "@osdk/functions";

type OntologyEdit = Edits.Object<Employee>;

function editMandatoryMarkings(markings: MandatoryMarking[]): OntologyEdit[] {
const batch = createEditBatch<OntologyEdit>(client);

const employeeOne = await client(Employee).fetchOne(1);
batch.update(employeeOne, { markingsProperty: markings });

return batch.getEdits();
}

export default editMandatoryMarkings;
```
```python tab="Python"
from foundry_sdk_runtime import Marking
from functions.api import function, MandatoryMarking, OntologyEdit
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Employee

@function
def edit_mandatory_markings(markings: list[MandatoryMarking]) -> list[OntologyEdit]:
ontology_edits = FoundryClient().ontology.edits()
employee: Optional[Employee] = client.ontology.objects.Employee.get("primary_key")
if employee is None:
return []
editable_employee = ontology_edits.objects.Employee.edit(employee)

editable_employee.markings_property = [Marking(m) for m in markings]
# Assigning type "list[MandatoryMarking]" also works, but gives an LSP warning:
# editable_employee.markings_property = markings

return ontology_edits.get_edits()
```
### Classification marking
基于分类的访问控制 (CBAC) 是用于保护敏感政府信息的强制性控制机制。它们通过要求用户必须具有特定的分类 marking 才能访问信息来限制访问权限。

Classification-based access controls (CBAC) are mandatory controls used to protect sensitive government information. They restrict access by requiring a user to have a particular classification marking in order to access information.
```typescript tab="TypeScript v1"
import { OntologyEditFunction, ClassificationMarking } from "@foundry/functions-api";
import { Employee, Objects } from "@foundry/ontology-api";

export class MyFunctions {
@Edits(Employee)
@OntologyEditFunction()
public async editClassificationMarkings(markings: ClassificationMarking[]): Promise<void> {
const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
employeeOne.markingsProperty = markings;
}
}
```
```typescript tab="TypeScript v2"
import { Client } from "@osdk/client";
import { Employee } from "@ontology/sdk";
import { Edits, createEditBatch, ClassificationMarking } from "@osdk/functions";

type OntologyEdit = Edits.Object<Employee>;

function editClassificationMarkings(markings: ClassificationMarking[]): OntologyEdit[] {
const batch = createEditBatch<OntologyEdit>(client);

const employeeOne = await client(Employee).fetchOne(1);
batch.update(employeeOne, { markingsProperty: markings });

return batch.getEdits();
}

export default editClassificationMarkings;
```
```python tab="Python"
from foundry_sdk_runtime import Marking
from functions.api import ClassificationMarking, function, OntologyEdit
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Employee

@function
def edit_classification_markings(markings: list[ClassificationMarking]) -> list[OntologyEdit]:
ontology_edits = FoundryClient().ontology.edits()
employee: Optional[Employee] = client.ontology.objects.Employee.get("primary_key")
if employee is None:
return []
editable_employee = ontology_edits.objects.Employee.edit(employee)

editable_employee.markings_property = [Marking(m) for m in markings]
# Assigning type "list[ClassificationMarking]" also works, but gives an LSP warning:
# editable_employee.markings_property = markings

return ontology_edits.get_edits()
```
## Collection types
Collection 类型由其他类型参数化。例如,Array\[String] 是字符串列表,Map\[String, Integer] 是键为字符串、值为整数的字典。必须指定参数化类型,且该类型必须是另一种受支持的类型。Map 的键只能是标量类型或 Ontology Object Type。

Collection types are parameterized by other types. For example, Array\[String] is a list of strings and Map\[String, Integer] is a dictionary with string keys and integer values. The parameterized types must be specified, and the type must be another supported type. Map keys can only be scalar types or an Ontology object type.
### List
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public filterForEvenIntegers(nums: Integer[]): Integer[] {
return nums.filter(num => num % 2 === 0);
}
}
```
```typescript tab="TypeScript v2"
import { Integer } from "@osdk/functions";

function filterForEvenIntegers(nums: Integer[]): Integer[] {
return nums.filter(num => num % 2 === 0);
}

export default filterForEvenIntegers;
```
```python tab="Python"
from functions.api import function, Integer

@function
def filter_for_even_integers(nums: list[Integer]) -> list[Integer]:
return [n for n in nums if n % 2 == 0]
```
### Map
Map 通常用于通过标量类型进行键控,并访问可以是任何其他 function registry 类型的关联值。

Maps are commonly used to key by a scalar type and access an associated value that can be of any other function registry type.
```typescript tab="TypeScript v1"
import { Function, FunctionsMap } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getMap(): FunctionsMap<string, string> {
const myMap = new FunctionsMap<string, string>();

myMap.set("Name", "Phil");
myMap.set("Favorite Color", "Blue");

return myMap;
}
}
```
```typescript tab="TypeScript v2"
function getMap(): Record<string, string> {
const myMap: Record<string, string> = {};

myMap["Name"] = "Phil";
myMap["Favorite Color"] = "Blue";

return myMap;
}

export default getMap;
```
```python tab="Python"
from functions.api import function

@function
def get_map() -> dict[str, str]:
my_map = {}

my_map["Name"] = "Phil"
my_map["Favorite Color"] = "Blue"

return my_map
```
此外,map 支持将 Ontology 对象用作键。

Additionally, maps support Ontology objects as keys.
```typescript tab="TypeScript v1"
import { Function, FunctionsMap } from "@foundry/functions-api";
import { Airplane } from "@foundry/ontology-api";

export class MyFunctions {
@Function()
public getObjectMap(aircraft: Airplane[]): FunctionsMap<Airplane, Integer | undefined> {
const myMap = new FunctionsMap<Airplane, Integer | undefined>();

aircraft.forEach(obj => {
myMap.set(obj, obj.capacity);
});

return myMap;
}
}
```
```typescript tab="TypeScript v2"
import { ObjectSpecifier, Osdk } from "@osdk/client";
import { Integer } from "@osdk/functions";
import { Airplane } from "@ontology/sdk";

function getObjectMap(aircraft: Osdk.Instance<Airplane>[]): Record<ObjectSpecifier<Airplane>, Integer | undefined> {
const myMap: Record<ObjectSpecifier<Airplane>, Integer | undefined> = {};

aircraft.forEach(obj => {
myMap[obj.$objectSpecifier] = obj.capacity;
});

return myMap;
}

export default getObjectMap;
```
```python tab="Python"
from functions.api import function, Integer
from ontology_sdk.ontology.objects import Airplane

@function
def get_object_map(aircraft: list[Airplane]) -> dict[Airplane, Integer | None]:
my_map = {}

for a in aircraft:
my_map[a] = a.capacity

return my_map
```
### Set
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getSizeOfSet(mySet: Set<Integer>): Integer {
return mySet.size;
}
}
```
```python tab="Python"
from functions.api import function, Integer

@function
def get_size_of_set(my_set: set[Integer]) -> Integer:
return len(my_set)
```
### Optional
* 在 TypeScript function 中,可选参数声明为 `varName?: T` 或 `varName: T | undefined`。例如,具有名为 `value` 的可选 Integer 参数的 function 可以声明为 `value?: Integer` 或 `value: Integer | undefined`。TypeScript function 还可以通过指定 `T | undefined` 类型来声明可选的返回类型。例如,可能返回 `Integer` 或没有值的 function 将具有 `Integer | undefined` 的返回类型。

* 在 Python function 中,可使用 `typing.Optional[T]` 或 `T | None` 来声明可选参数和返回值。`T | None` 语法需要 Python 3.10 或更高版本。

* 在 TypeScript 和 Python function 中,都必须指定参数化类型 `T`,且该类型必须是另一个支持的类型。

* In TypeScript functions, optional parameters are declared as `varName?: T` or `varName: T | undefined`. For example, a function that has an optional integer parameter named `value` could be declared as either `value?: Integer` or `value: Integer | undefined`. TypeScript functions can also declare an optional return type by specifying a type of `T | undefined`. For example, a function that may return either an `Integer` or no value would have a return type of `Integer | undefined`.
* In Python functions, optional parameters and return values can be declared using `typing.Optional[T]` or `T | None`. The `T | None` syntax requires Python 3.10 or greater.
* In both TypeScript and Python functions, the parameterized type `T` must be specified, and it must be another supported type.
```typescript tab="TypeScript v1"
import { Function } from "@foundry/functions-api";

export class MyFunction {
@Function()
public greet(name?: string): string | undefined {
if (name === undefined) {
return undefined;
}
return `Hello, ${name}!`;
}
}
```
```typescript tab="TypeScript v2"
function greet(name?: string): string | undefined {
if (name === undefined) {
return undefined;
}
return `Hello, ${name}!`;
}

export default greet;
```
```python tab="Python"
from functions.api import function

@function
def greet(name: str | None) -> str | None:
if name is None:
return None
return f"Hello, {name}!"
```
Function 还支持在 function 签名中使用默认值。

Functions also support default values in the function signature.
```typescript tab="TypeScript v1"
import { Double, Function } from "@foundry/functions-api";
import { Customer } from "@foundry/ontology-api";

export class MyFunctions {
@Function()
public computeRiskFactor(customer: Customer, weight: Double = 0.75): Double {
// ...
}
}
```
```typescript tab="TypeScript v2"
import { Double } from "@osdk/functions";
import { Osdk } from "@osdk/client";
import { Customer } from "@ontology/sdk";

function computeRiskFactor(customer: Osdk.Instance<Customer>, weight: Double = 0.75): Double {
// ...
}

export default computeRiskFactor;
```
```python tab="Python"
from functions.api import function, Double
from ontology_sdk.ontology.objects import Customer

@function
def compute_risk_factor(customer: Customer, weight: Double = 0.75) -> Double:
# ...
```
### Struct/custom type
自定义类型由其他支持的类型(包括其他自定义类型)组成,可用于 function 签名中。

Custom types are composed of other supported types (including other custom types) and can be used in function signatures.
* 在 TypeScript function 中,自定义类型是使用 `interface` 关键字定义的用户自定义 TypeScript interface。

* 可选字段通过 `?` 可选标记或与 `undefined` 的联合类型来支持。

* In TypeScript functions, custom types are user-defined TypeScript interfaces using the `interface` keyword.
* Optional fields are supported through either the `?` optional token or a union with `undefined`.
* 在 Python function 中,自定义类型是用户自定义的 Python 类。
* 要成为有效的自定义类型,该类必须遵循以下规则:
* 类必须对其所有字段进行类型注解。

* 字段类型必须是支持的类型;既可以使用原始 API 类型,也可以使用原生 Python 类型(如上表所定义)。

* `__init__` 方法必须仅接受与字段具有相同名称和类型注解的命名参数。

* 可以使用 [`dataclasses.dataclass` ↗](https://docs.python.org/3/library/dataclasses.html) 装饰器来自动生成符合这些要求的 `__init__` 方法。

* In Python functions, custom types are user-defined Python classes.
* To be a valid custom type, the class must adhere to the following:
* The class must have type annotations on all of its fields.
* The field types must be supported types; either the primitive API types or native Python types (as defined in the table above) may be used.
* The `__init__` method must accept only named arguments with the same names and type annotations as the fields.
* The [`dataclasses.dataclass` ↗](https://docs.python.org/3/library/dataclasses.html) decorator can be used to automatically generate an `__init__` method that conforms with these requirements.
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";
import { Passenger } from "@foundry/ontology-api";

interface PassengerInfo {
name?: string;
age?: Integer;
}

export class MyFunctions {
@Function()
public getPassengerInfo(passenger: Passenger): PassengerInfo {
return {
name: passenger.name,
age: passenger.age,
};
}
}
```
```typescript tab="TypeScript v2"
import { Osdk } from "@osdk/client";
import { Integer } from "@osdk/functions";
import { Passenger } from "@ontology/sdk";

interface PassengerInfo {
name?: string;
age?: Integer;
}

function getPassengerInfo(passenger: Osdk.Instance<Passenger>): PassengerInfo {
return {
name: passenger.name,
age: passenger.age,
};
}

export default getPassengerInfo;
```
```python tab="Python"
from dataclasses import dataclass
from functions.api import function, Integer
from ontology_sdk.ontology.objects import Passenger

@dataclass
class PassengerInfo:
name: str | None
age: Integer | None

@function
def get_passenger_info(passenger) -> PassengerInfo:
return PassengerInfo(
name=passenger.name,
age=passenger.age
)
```
## Aggregation types
聚合类型可以从 function 返回,供平台的其他部分使用,例如 [Workshop](/docs/foundry/workshop/overview/) 中的 Charts。

Aggregation types can be returned from functions for use in other parts of the platform, such as Charts in [Workshop](/docs/foundry/workshop/overview/).
支持两种聚合类型:

There are two supported aggregation types:
* [二维聚合](#two-dimensional-aggregation) 从单个 bucket 键映射到数值。例如,这可用于表示某种聚合,例如具有特定职位的员工数量。

* [三维聚合](#three-dimensional-aggregation) 从两个 bucket 键映射到数值。这可用于表示某种聚合,例如按每位员工的职位和办公地点统计的员工数量。

* A [two-dimensional aggregation](#two-dimensional-aggregation) maps from a single bucket key to a numeric value. For example, this could be used to represent an aggregation such as a count of employees with a specific job title.
* A [three-dimensional aggregation](#three-dimensional-aggregation) maps from two bucket keys to a numeric value. This could be used to represent an aggregation such as a count of employees by each employee's job title and home office.
聚合可以由多种类型作为键:

Aggregations can be keyed by several types:
* [Boolean](#boolean) bucket 表示值为 `true` 或 `false` 的数据。

* [String](#string) bucket 可用于表示分类值。

* [Range](#range) bucket 表示 bucket 键为值范围的聚合。这些可用于表示图表中的直方图或日期坐标轴。

* 数值范围,包括 [Integer](#integer) 和 [Double](#double),表示对数值的分桶聚合。

* 日期和时间范围,包括 [Date](#date) 和 [Timestamp](#timestamp),表示对日期范围的分桶聚合。

* [Boolean](#boolean) buckets represent values that are either `true` or `false`.
* [String](#string) buckets can be used to represent categorical values.
* [Range](#range) buckets represent aggregations where the bucket key is a range of values. These can be used to represent a histogram or date axis in a chart.
* Numeric ranges, including [Integer](#integer) and [Double](#double), represent bucketed aggregations on numeric values.
* Date and time ranges, including on [Date](#date) and [Timestamp](#timestamp), represent bucketed aggregations on date ranges.
### Range
```typescript tab="TypeScript v1"
import { Function, Integer, IRange } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getRange(min: Integer, max: Integer): IRange<Integer> {
return {
min,
max,
};
}
}
```
```typescript tab="TypeScript v2"
import { Integer, Range } from "@osdk/functions";

function getRange(min: Integer, max: Integer): Range<Integer> {
return {
min,
max,
};
}

export default getRange;
```
```python tab="Python"
from functions.api import function, Integer, Range

@function
def get_range(min: Integer, max: Integer) -> Range[Integer]:
return Range(
min=min,
max=max
)
```
### Two-dimensional aggregation
```typescript tab="TypeScript v1"
import { Double, Function, TwoDimensionalAggregation } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public myTwoDimensionalAggregation(): TwoDimensionalAggregation<string, Double> {
return {
buckets: [
{ key: "bucket1", value: 5.0 },
{ key: "bucket2", value: 6.0 },
],
};
}
}
```
```typescript tab="TypeScript v2"
import { Double, TwoDimensionalAggregation } from "@osdk/functions";

function myTwoDimensionalAggregationFunction(): TwoDimensionalAggregation<string, Double> {
return [
{ key: "bucket1", value: 5.0 },
{ key: "bucket2", value: 6.0 },
];
}

export default myTwoDimensionalAggregationFunction;
```
```python tab="Python"
from functions.api import (
function,
Double,
TwoDimensionalAggregation,
SingleBucket
)

@function
def my_two_dimensional_aggregation_function() -> TwoDimensionalAggregation[str, Double]:
return TwoDimensionalAggregation(
buckets=[
SingleBucket(key="bucket1", value=Double(5.0)),
SingleBucket(key="bucket2", value=Double(6.0)),
]
)
```
### Three-dimensional aggregation
```typescript tab="TypeScript v1"
import { Double, Function, ThreeDimensionalAggregation } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public myThreeDimensionalAggregation(): ThreeDimensionalAggregation<string, string, Double> {
return {
buckets: [
{
key: "group-by-1",
value: [
{ key: "partition-by-1", value: 5.0 },
{ key: "partition-by-2", value: 6.0 },
],
},
{
key: "group-by-2",
value: [
{ key: "partition-by-1", value: 7.0 },
{ key: "partition-by-2", value: 8.0 },
],
},
]
};
}
}
```
```typescript tab="TypeScript v2"
import { Double, ThreeDimensionalAggregation } from "@osdk/functions";

function myThreeDimensionalAggregation(): ThreeDimensionalAggregation<string, string, Double> {
return [
{
key: "group-by-1",
value: [
{ key: "partition-by-1", value: 5.0 },
{ key: "partition-by-2", value: 6.0 },
],
},
{
key: "group-by-2",
value: [
{ key: "partition-by-1", value: 7.0 },
{ key: "partition-by-2", value: 8.0 },
],
},
];
}

export default myThreeDimensionalAggregation;
```
```python tab="Python"
from functions.api import (
function,
Double,
ThreeDimensionalAggregation,
SingleBucket,
NestedBucket,
)

@function
def my_three_dimensional_aggregation_function() -> (
ThreeDimensionalAggregation[str, str, Double]
):
return ThreeDimensionalAggregation(
buckets=[
NestedBucket(key="group-by-1", buckets=[
SingleBucket(key="partition-by-1", value=Double(5.0)),
SingleBucket(key="partition-by-2", value=Double(6.0)),
]),
NestedBucket(key="group-by-2", buckets=[
SingleBucket(key="partition-by-1", value=Double(7.0)),
SingleBucket(key="partition-by-2", value=Double(8.0)),
])
]
)
```
## Ontology types
> **ℹ️ 注意: Ontology imports**

> 要在 function 签名中使用 object type,必须将它们导入到您的 repository 中。[详细了解 Ontology imports。](/docs/foundry/functions/ontology-imports/)
> **ℹ️ 注意: Ontology imports**

> Object types must be imported into your repository to use them in function signatures. [Learn more about Ontology imports.](/docs/foundry/functions/ontology-imports/)
### Object
来自您的 Ontology 的 object type 可在 function 签名中用作输入和输出。要接受或返回 object type 的单个实例,请从您的 Ontology SDK 导入该 object type,并使用该类型对 function 进行注解。

Object types from your ontology can be used as both inputs and outputs in your function signature. To either accept or return a single instance of an object type, import the object type from your Ontology SDK and use that type to annotate your function.
```typescript tab="TypeScript v1"
import { Function, Integer } from "@foundry/functions-api";
import { Airplane } from "@foundry/ontology-api";

export class MyFunctions {
@Function()
public getCapacity(airplane: Airplane): Integer {
return airplane.capacity;
}
}
```
```typescript tab="TypeScript v2"
import { Osdk } from "@osdk/client";
import { Integer } from "@osdk/functions";
import { Airplane } from "@ontology/sdk";

function getCapacity(airplane: Osdk.Instance<Airplane>): Integer {
return airplane.capacity;
}

export default getCapacity;
```
```python tab="Python"
from functions.api import function, Integer
from ontology_sdk.ontology.objects import Airplane

@function
def get_capacity(airplane: Airplane) -> Integer:
return airplane.capacity
```
在 TypeScript v2 中,对 object type 的引用作为 [struct](#structcustom-type) 参数字段受到支持。要接受包含 object type 实例的 struct 或 struct 列表,请创建一个带有来自 Ontology SDK 的 object type 字段的自定义类型输入。这可以与 [Ontology Edits](#ontology-edit) 配合使用,以支持从其他 object type 派生创建多个 object type 实例等工作流。

In TypeScript v2, references to object types are supported as [struct](#structcustom-type) parameter fields. To accept a struct or struct list with object type instances, create a custom type input with an object type field from your Ontology SDK. This can be paired with [Ontology Edits](#ontology-edit) to support workflows such as creating multiple instances of an object type derived from other object types.
```typescript tab="TypeScript v2"
import { Osdk } from "@osdk/client";
import { Integer } from "@osdk/functions";
import { Airplane, Passenger, Ticket } from "@ontology/sdk";

type TicketEdit = Edits.Object<Ticket>

interface TicketInfo {
airplane?: Osdk.Instance<Airplane>;
passenger?: Osdk.Instance<Passenger>;
seat?: String;
}

function createTickets(ticketInfo: TicketInfo[]): TicketEdit[] {
const batch = createEditBatch<TicketEdit>(client);

ticketInfo.forEach(i => batch.create(TicketEdit, {
flightNumber: i.airplane.flightNumber,
passengerName: i.passenger.name,
seat: i.seat}))

return batch.getEdits();
}

export default createTickets;
```
### Object set
There are two ways to pass a collection of objects into and out of a function: concrete collections of objects (such as arrays), or object sets.
Passing an array of objects to a function enables executing logic over a concrete list of objects at the expense of loading the objects into the function execution environment up front. An object set, however, allows you to perform filtering, search-around, and aggregation operations and only load the final result when you request it.
> **✅ 成功**

> We recommend using an object set instead of an array because an object set often achieves better performance and allows more than 10,000 objects to be passed into the function.
The below example shows how to filter an object set without loading the objects into memory, allowing you to return the filtered object set to a different part of the application.
```typescript tab="TypeScript v1"
import { Function } from "@foundry/functions-api";
import { Airplane, ObjectSet } from "@foundry/ontology-api";

export class MyFunctions {
@Function()
public filterAircraft(aircraft: ObjectSet<Airplane>): ObjectSet<Airplane> {
return aircraft.filter(a => a.capacity.range().gt(200));
}
}
```
```typescript tab="TypeScript v2"
import { ObjectSet } from "@osdk/client";
import { Airplane } from "@ontology/sdk";

function filterAircraft(aircraft: ObjectSet<Airplane>): ObjectSet<Airplane> {
return aircraft
.where({
capacity: {
$gt: 200,
}
});
}

export default filterAircraft;
```
```python tab="Python"
from functions.api import function
from ontology_sdk.ontology.objects import Airplane
from ontology_sdk.ontology.object_sets import AirplaneObjectSet

@function
def filter_aircraft(aircraft: AirplaneObjectSet) -> AirplaneObjectSet:
return aircraft.where(Airplane.capacity > 200)
```
### Interface
Interface types from your Ontology can be used as both inputs and outputs in TypeScript v2 function signatures. They are not supported in TypeScript v1 or Python.
```typescript tab="TypeScript v2"
import { Osdk } from "@osdk/client";
import { Integer } from "@osdk/functions";
import { Person } from "@ontology/sdk";

function getAge(person: Osdk.Instance<Person>): Integer {
return person.age;
}

export default getAge;
```
### Interface object set
Interface object sets can be both inputs and outputs in TypeScript v2 function signatures.
```typescript tab="TypeScript v2"
import { ObjectSet } from "@osdk/client";
import { Person } from "@ontology/sdk";

function filterPeople(people: ObjectSet<Person>): ObjectSet<Person> {
return people
.where({
age: {
$gt: 200,
}
});
}

export default filterPeople;
```
### Ontology edit
In addition to writing functions that read data from the Ontology, you can also write functions that create objects and edit the properties and links between objects. For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).
To be registered as edit functions, TypeScript v1 functions require a `void` return type in the signature. TypeScript v2 and Python functions, however, require explicitly returning a list of Ontology edits.
```typescript tab="TypeScript v1"
import { Edits, OntologyEditFunction } from "@foundry/functions-api";
import { Employee, LaptopRequest, Objects } from "@foundry/ontology-api";

export class MyFunctions {

@Edits(Employee, LaptopRequest)
@OntologyEditFunction()
public assignEmployee(newEmployee: Employee, leadEmployee: Employee): void {

const newLaptopRequest = Objects.create().laptopRequest(Date.now().toString());
newLaptopRequest.employeeName = newEmployee.name;

newEmployee.lead.set(leadEmployee);
}
}
```
```typescript tab="TypeScript v2"
import { Client } from "@osdk/client";
import { createEditBatch, Edits } from "@osdk/functions";
import { Employee, LaptopRequest } from "@ontology/sdk";

type EmployeeEdit =
| Edits.Object<Employee>
| Edits.Object<LaptopRequest>
| Edits.Link<Employee, "lead">;

function assignEmployee(
client: Client,
newEmployee: Osdk.Instance<Employee>,
leadEmployee: Osdk.Instance<Employee>
): EmployeeEdit[] {

const batch = createEditBatch<EmployeeEdit>(client);

batch.create(LaptopRequest, {
id: Date.now().toString(),
employeeName: newEmployee.name,
});
batch.link(newEmployee, "lead", leadEmployee);

return batch.getEdits();
}

export default assignEmployee;
```
```python tab="Python"
from functions.api import function, OntologyEdit
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Employee, LaptopRequest
from time import time

@function
def assign_employee(new_employee: Employee, lead_employee: Employee) -> list[OntologyEdit]:

ontology_edits = FoundryClient().ontology.edits()

new_laptop_request = ontology_edits.objects.LaptopRequest.create(str(int(time() * 1000)))
new_laptop_request.employee_name = new_employee.name

new_employee.lead.set(lead_employee)

return ontology_edits.get_edits()
```
### Attachment
```typescript tab="TypeScript v1"
import { Attachment, Function } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public loadAttachmentContents(attachment: Attachment): Promise<string> {
return attachment.readAsync().then(blob => blob.text());
}
}
```
```typescript tab="TypeScript v2"
import { Attachment } from "@osdk/functions";

function loadAttachmentContents(attachment: Attachment): Promise<string> {
return attachment.fetchContents().then(response => response.text());
}

export default loadAttachmentContents;
```
```python tab="Python"
from functions.api import function, Attachment

@function
def load_attachment_contents(attachment: Attachment) -> str:
return attachment.read().getvalue().decode('utf-8')
```
### Notification
Notification types can be returned from a function to flexibly configure notifications that should be sent in the platform. For example, you can author a function that takes in parameters such as a `User` and an object type and returns a Notification with a configured message.
* A `Notification` consists of two fields: a `ShortNotification` and `EmailNotificationContent`.
* A `ShortNotification` represents a summarized version of the notification, which will be shown within the Foundry platform. It includes a short `heading`, `content`, and a collection of `Link`s.
* `EmailNotificationContent` represents a rich version of the notification which can be sent externally via email. It includes a `subject`, a `body` consisting of headless HTML, and a collection of `Link`s.
* A `Link` has a user-facing `label` and a `linkTarget`. The `LinkTarget` can be a URL, an `OntologyObject`, or a `rid` of any resource within Foundry.
For an example of how to use the Notifications API, review [our guide](/docs/foundry/functions/configure-notifications/).
```typescript tab="TypeScript v1"
import {
EmailNotificationContent,
Function,
Notification,
ShortNotification,
} from "@foundry/functions-api";

export class MyFunctions {
@Function()
public buildNotification(): Notification {
return Notification.builder()
.shortNotification(ShortNotification.builder()
.heading("Issue reminder")
.content("Investigate this issue.")
.build())
.emailNotificationContent(EmailNotificationContent.builder()
.subject("New issue")
.body("hello")
.build())
.build();
}
}
```
```typescript tab="TypeScript v2"
import {
Notification
} from "@osdk/functions";

export default function buildNotification(): Notification {
return {
platformNotification: {
heading: "Issue reminder",
content: "Investigate this issue.",
links: []
},
emailNotification: {
subject: "New issue"
body: "hello",
links: []
}
};
}
```
```python tab="Python"
from functions.api import function, Notification, PlatformNotification, EmailNotification

@function()
def buildNotification() -> Notification:
return Notification(
platform_notification=PlatformNotification(
heading="Issue reminder",
content="Investigate this issue.",
links=[]
),
email_notification=EmailNotification(
subject="New issue",
body="hello",
links=[]
),
)

```
## Media types
### Media
Functions can accept and return media items. In TypeScript v1, use the `MediaItem` type. In TypeScript v2 and Python, use `Media` as both the input and output type. Callers can pass an existing `MediaReference`, for example, a media property on an object, into the function. Downstream consumers can use the returned value to fetch contents, fetch metadata, or attach it to another object. For more information, review the guide on [media](/docs/foundry/functions/media/).
```typescript tab="TypeScript v1"
import { Function, MediaItem } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public async echoMedia(media: MediaItem): Promise<string | undefined> {
const mimeType: string = media.mimeType;
// Fetch type-specific metadata (page count, dimensions, duration, and so on)
const metadata = await media.getMetadataAsync();
// Read the binary contents as a Blob
const contents: Blob = await media.readAsync();
// Narrow to a specialized subtype to call type-specific methods
if (MediaItem.isDocument(media)) {
const text = await media.extractTextAsync({ startPage: 0, endPage: 1 });
} else if (MediaItem.isAudio(media)) {
const transcript = await media.transcribeAsync();
}
return undefined;
}
}
```
```typescript tab="TypeScript v2"
import type { Media } from "@osdk/client";

export default async function echoMedia(media: Media): Promise<Media> {
// Get the underlying MediaReference
const mediaReference = media.getMediaReference();
// Fetch slim metadata: path, sizeBytes, mediaType
const metadata = await media.fetchMetadata();
// Fetch contents as a Response; call .blob() or .arrayBuffer() for bytes
const response = await media.fetchContents();
const contents = await response.blob();
return media;
}
```
```python tab="Python"
from foundry_sdk.v2.core.models import MediaReference
from functions.api import function, Media

@function
def echo_media(media: Media) -> Media:
# Get the underlying MediaReference
media_reference: MediaReference = media.get_media_reference()
# Fetch slim metadata: path, size_bytes, media_type
metadata = media.get_media_metadata()
# Fetch type-specific metadata (page count, dimensions, duration, and more by type)
full_metadata = media.get_media_full_metadata()
# Fetch the binary contents as a BytesIO stream
contents = media.get_media_content()
return media
```
## Users, groups, and principals
A Principal represents either a Foundry user account or group. These types can be passed into a function to allow accessing information associated with a user or group, such as a group's name or a user's first and last name or email address. All Principal types are exported from the `@foundry/functions-api` package.
* A `User` always has a username, and may have a `firstName`, `lastName`, or `email`. It also includes all fields associated with a `Principal`.
* A `Group` has a name. It also includes all fields associated with a `Principal`.
* A `Principal` can be either a `User` or a `Group`. You can inspect the `type` field to determine whether a given `Principal` is a `User` or a `Group`. In addition to `User` and `Group`-specific fields, a `Principal` has an `id`, `realm`, and dictionary of `attributes`.
### User
```typescript tab="TypeScript v1"
import { Function, User } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getUserEmail(user: User): string {
return user.email;
}
}
```
```typescript tab="TypeScript v2"
import { UserId } from "@osdk/functions";
import { Users } from "@osdk/foundry.admin";
import { Client } from "@osdk/client";

export default function getUserEmail(client:Client, userId: UserId): string {
const user = Users.get(client, userId)
return user.email;
}
```
```python tab="Python"
from functions.api import function, UserId
from foundry_sdk import FoundryClient
import foundry_sdk

@function()
def getUserEmail(user_id: UserId) -> string:
client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
user = client.admin.User.get(user_id)
return user.email
```
### Group
```typescript tab="TypeScript v1"
import { Function, Group } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getGroupName(group: Group): string {
return group.name;
}
}
```
```typescript tab="TypeScript v2"
import { GroupId } from "@osdk/functions";
import { Groups } from "@osdk/foundry.admin";
import { Client } from "@osdk/client";

export default function getGroupName(client: Client, groupId: GroupId): string {
const group = Groups.get(client, groupId)
return group.name;
}
```
```python tab="Python"
from functions.api import function, GroupId
from foundry_sdk import FoundryClient
import foundry_sdk

@function()
def getGroupName(group_id: GroupId) -> string:
client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
group = client.admin.Group.get(group_id)
return group.name
```
### Principal
```typescript tab="TypeScript v1"
import { Function, Principal } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public getPrincipalType(principal: Principal): string {

switch (principal.type) {
case "user":
return "User";
case "group":
return "Group";
default:
return "Unknown";
}
}
}
```
```typescript tab="TypeScript v2"
import { GroupId, Principal, UserId } from "@osdk/functions";

export default async function getPrincipals(client: Client, userId: UserId, groupId: GroupId): Principal[] {
return [{type: "user", id: userId}, {type: "group", id: groupId}];
}
```
```python tab="Python"
from functions.api import Array, function, GroupId, Principal, UserId

@function()
def getPrincipals(user_id: UserId, group_id: GroupId) -> Array[Principal]:
return [Principal.user(user_id), Principal.group(group_id)]
```
## Geometry types
Geometry 类型表示函数中的空间数据和地理形状。支持两种 geometry 类型:

Geometry types represent spatial data and geographic shapes in your functions. Two geometry types are supported:
* **GeoPoint** 表示一个具有纬度和经度坐标的单一地理点。

* **GeoShape** 表示任何有效的 GeoJSON 几何图形，包括 Points、Polygons、LineStrings 和其他形状。

* **GeoPoint** represents a single geographic point with latitude and longitude coordinates.
* **GeoShape** represents any valid GeoJSON geometry, including Points, Polygons, LineStrings, and other shapes.
这些类型遵循 [GeoJSON 规范 ↗](https://geojson.org/)，可用于空间操作、地图绘制和地理分析。请注意，根据 GeoJSON 规范，位置参数的顺序为经度、纬度。

These types follow the [GeoJSON specification ↗](https://geojson.org/) and can be used for spatial operations, mapping, and geographic analysis. Note that positional arguments follow longitude, latitude order as per the GeoJSON spec.
### GeoPoint
以下示例展示如何创建并返回一个 GeoPoint。

The following example shows how to create and return a GeoPoint.
```typescript tab="TypeScript v1"
import { Function, GeoPoint } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public createPoint(): GeoPoint {
return GeoPoint.fromCoordinates({
latitude: 37.7749,
longitude: -22.4194
});
}
}
```
```typescript tab="TypeScript v2"
import { Point } from "@osdk/functions";

function createPoint(): Point {
return {
type: "Point",
coordinates: [-22.4194, 37.7749]
};
}

export default createPoint;
```
```python tab="Python"
from functions.api import function, GeoPoint

@function
def create_point() -> GeoPoint:
return GeoPoint(type="Point", coordinates=[-22.4194, 37.7749])
```
### GeoShape
以下示例展示如何创建并返回一个 Polygon。

The following example shows how to create and return a Polygon.
```typescript tab="TypeScript v1"
import { Function, Polygon, GeoPoint } from "@foundry/functions-api";

export class MyFunctions {
@Function()
public createPolygon(): Polygon {
const ring: GeoPoint[] = [
GeoPoint.fromCoordinates({ latitude: 37.8, longitude: -22.4 }),
GeoPoint.fromCoordinates({ latitude: 37.8, longitude: -22.5 }),
GeoPoint.fromCoordinates({ latitude: 37.7, longitude: -22.5 }),
GeoPoint.fromCoordinates({ latitude: 37.7, longitude: -22.4 }),
GeoPoint.fromCoordinates({ latitude: 37.8, longitude: -22.4 })
];
return Polygon.fromLinearRings([ring]);
}
}
```
```typescript tab="TypeScript v2"
import { Geometry } from "@osdk/functions";

function createPolygon(): Geometry {
return {
type: "Polygon",
coordinates: [[
[-22.4, 37.8],
[-22.5, 37.8],
[-22.5, 37.7],
[-22.4, 37.7],
[-22.4, 37.8]
]]
};
}

export default createPolygon;
```
```python tab="Python"
from functions.api import function, Polygon

@function
def create_polygon() -> Polygon:
return Polygon(
type="Polygon",
coordinates=[[
[-22.4, 37.8],
[-22.5, 37.8],
[-22.5, 37.7],
[-22.4, 37.7],
[-22.4, 37.8]
]])
```