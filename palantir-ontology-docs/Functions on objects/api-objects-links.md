<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/api-objects-links/
---
# API: Objects and links
导入到您项目中的每个 [Object Type](/docs/foundry/object-link-types/object-types-overview/) 都会被转换为 TypeScript API，以便您轻松访问和操作 Foundry 中可用的 objects。

Every [object type](/docs/foundry/object-link-types/object-types-overview/) imported into your project is converted to a TypeScript API so you can easily access and manipulate objects available in Foundry.
### Properties
每个 Object Type 的 [Properties](/docs/foundry/object-link-types/properties-overview/) 都会转换为为每个 Object Type 生成的 TypeScript Interface 上的字段。生成的字段名称使用在 ontology 中指定的 API Name。

[Properties](/docs/foundry/object-link-types/properties-overview/) of each object type are converted to fields on the TypeScript interface generated for each object type. The generated field name uses the API Name specified in the ontology.
您可以使用简单的点表示法访问每个 property 的字段：

You can access the fields for each property with simple dot notation:
```typescript
const firstName = employee.firstName;
```
请注意，由于 properties 可能没有具体的值，因此访问 property 值时返回的类型可能是 `undefined`。除非您明确处理 `undefined` 的情况，否则 TypeScript 编译器会报错。有关此内容的更多详细信息，请参阅[本指南](/docs/foundry/functions/undefined-values/)。

Note that because properties may not have a concrete value set, the returned type when accessing a property value could be `undefined`. The TypeScript compiler will give an error unless you explicitly handle the `undefined` case. See [this guide](/docs/foundry/functions/undefined-values/) for more details on this.
#### Array properties
Object Type 上的 Array 属性会转换为 `ReadOnlyArray` 类型。这是为了让[编辑](/docs/foundry/functions/api-ontology-edits/) Array 属性的语义更加清晰——修改 Array 属性的值的唯一方法是使用全新的 Array 值对其进行更新。

Array properties on an object type are converted to `ReadOnlyArray` types. This is so that the semantics for [editing](/docs/foundry/functions/api-ontology-edits/) an array property are clear—the only way to modify the values of an array property is to update it with an entirely new array value.
如果您想操作 Array 属性的值，请先复制它：

If you want to manipulate the values of an array property, make a copy of it:
```typescript
// Copy to a new array
let arrayCopy = [...myObject.myArrayProperty];
// Now you can modify the copied array
arrayCopy.push(newItem);
```
### Link types
Object Type 之间的 [Link Types](/docs/foundry/object-link-types/link-types-overview/) 也会转换为每个 Object Type 的 TypeScript Interface 上的字段。要遍历该 link，请访问该字段，然后调用用于加载 objects 的方法之一。Link Type 字段名称是使用在 ontology 中指定的 API Name 生成的。

[Link types](/docs/foundry/object-link-types/link-types-overview/) between object types are also converted to fields on the TypeScript interface for each object type. To traverse the link, access the field and then call one of the methods used to load the objects. Link type field names are generated using the API Name specified in the ontology.
Foundry Ontology 支持定义 1-to-1、1-to-many 和 many-to-many link types。当访问 link 的 `1` 一侧时，生成的字段是 `SingleLink` 类型。您可以使用 `get()` 或 `getAsync()` 方法访问 linked object：

The Foundry Ontology supports defining 1-to-1, 1-to-many, and many-to-many link types. When accessing the `1` side of a link, the generated field is of the `SingleLink` type. You can access the linked object using the `get()` or `getAsync()` methods:
```typescript
const manager = employee.manager.get();
```
与 properties 一样，当您遍历 1-to-1 或 many-to-1 link 时，如果没有 linked object，返回值可能是 `undefined`。对于这些 link，请遵循[指南](/docs/foundry/functions/undefined-values/) 来处理 `undefined` 值。

As with properties, when you traverse a 1-to-1 or many-to-1 link, the return value may be `undefined` if there is no linked object. Follow the [guide](/docs/foundry/functions/undefined-values/) for handling `undefined` values for these links.
当访问 link 的 `many` 一侧时，生成的字段是 `MultiLink` 类型。您可以使用 `all()` 或 `allAsync()` 方法访问 linked objects 的 Array。如果没有 linked objects，这些方法将返回一个空 Array。

When accessing the `many` side of a link, the generated field is of the `MultiLink` type. You can access an Array of linked objects using the `all()` or `allAsync()` methods. If there are no linked objects, these methods will return an empty Array.
```typescript
const employees = employee.reports.all();
```
遍历链接可能开销很大，因为它需要在后端加载哪些对象被链接了。关于如何更高效地执行链接遍历的详细信息，请参阅[此章节](/docs/foundry/functions/optimize-performance/#optimizing-link-traversals)。

Traversing links can be expensive because it requires loading which objects are linked in the backend. For details about how to perform link traversals more efficiently, see [this section](/docs/foundry/functions/optimize-performance/#optimizing-link-traversals).
调用 `.all()` 或 `.allAsync()` 返回的链接对象数组是一个 `ReadOnlyArray`。如果需要修改该数组，请先复制一份：

The array of linked objects returned from calling `.all()` or `.allAsync()` is a `ReadOnlyArray`. If you want to modify the array, make a copy of it first:
```typescript
let copiedEmployees = [...employee.reports.all()];
```
您可以将链接作为 `ObjectSet` 进行遍历，以避免在内存中加载链接的对象实例。当链接在 Ontology 中创建时，将在此类型的 object set 上生成 API，以便"search around"到其他链接的 object set。

You can traverse links as an `ObjectSet` to avoid loading linked object instances in the memory. When links are created in the Ontology, APIs will be generated on an object set of this type to "search around" to other linked object sets.
```typescript
import { ObjectSet, Employee } from "@foundry/ontology-api";

// Assume you have an object set available:
// const employee_id = "123";
// const employeeObjectSet : ObjectSet<Employee> = Objects.search().employee().filter(exactMatch(employee_id));

const linkedObjs: ObjectSet<OtherObjectType> = employeeObjectSet.searchAroundToOtherObjectType();
```
如果您操作单个对象实例并从该实例进行 search around，您将得到一个 `MultiLink<objectType>`。您无法将此 `MultiLink` 转换为 `ObjectSet`；您必须将对象实例转换为 object set 才能 pivot 到其他 object set。

If you operate on a single instance of an object and search around from there, you will get a `MultiLink<objectType>`. You cannot convert this `MultiLink` to an `ObjectSet`; you must convert the object instance to an object set to pivot to other object sets.
```typescript
// Assuming:
// const employee: Employee

// MultiLink can be loaded in memory to process further.

const linkedObjs: MultiLink<objectType> = employee.reports

// Convert a sole object instance to an object set. This statement will take longer than an `employee().filter()` statement.
const employeeObjectSet : ObjectSet<Employee> = Objects.search().employee([employee])

// From there, you can use the above "searchAroundToOtherObjectType" to process only object sets.
```
### Ontology metadata
Functions 通过提供 objects 和 properties 的列表来访问可用的 Ontology。可通过访问每个 object type 的常量类型来获取 Ontology 元数据信息。有关更多详细信息，请参阅以下章节。

Functions provides access to the available Ontology by providing the list of objects and properties. Ontology metadata information is available by accessing the constant types of each object type. See the sections below for more details.
#### Object property metadata
对象 properties 还包括类型元数据，它以编程方式提供对每个 property 类型的访问。您可以将此功能用于高级工作流，例如识别给定类型的所有 properties 或验证给定 property 名称是否具有特定类型。

Object properties also include type metadata, which provides programmatic access to the type of each property. You can use this functionality for advanced workflows like identifying all properties of a given type or validating that a given property name has a specific type.
例如，对于包含 employee object **type** 的 Ontology，您可以按如下方式访问该 object **type's** property 的类型信息：

For instance, for an Ontology that contains an employee object **type**, you can access the type information on that object **type's** property as follows:
```typescript
import { Employee } from "@foundry/ontology-api";
...
const type = Employee.properties.firstName;
```
在这种情况下，如果 `firstName` 是 `Employee` object type 上的一个 string property，那么其类型将是 `StringPropertyBaseType`。

In this case, if `firstName` is a string property on the `Employee` object type, then its type will be a `StringPropertyBaseType`.
可用的 property 类型如下：

The following property types are available:
* `BooleanPropertyBaseType`
* `BytePropertyBaseType`
* `DatePropertyBaseType`
* `FloatPropertyBaseType`
* `TimestampPropertyBaseType`
* `ShortPropertyBaseType`
* `GeohashPropertyBaseType` (与 `geopoint` properties 一起使用，此前名为 `geohash` properties。)

* `DecimalPropertyBaseType`
* `StringPropertyBaseType`
* `LongPropertyBaseType`
* `IntegerPropertyBaseType`
* `DoublePropertyBaseType`
* `ArrayPropertyBaseType`
* `VectorPropertyBaseType`
* `BooleanPropertyBaseType`
* `BytePropertyBaseType`
* `DatePropertyBaseType`
* `FloatPropertyBaseType`
* `TimestampPropertyBaseType`
* `ShortPropertyBaseType`
* `GeohashPropertyBaseType` (To be used with `geopoint` properties, previously named `geohash` properties.)
* `DecimalPropertyBaseType`
* `StringPropertyBaseType`
* `LongPropertyBaseType`
* `IntegerPropertyBaseType`
* `DoublePropertyBaseType`
* `ArrayPropertyBaseType`
* `VectorPropertyBaseType`