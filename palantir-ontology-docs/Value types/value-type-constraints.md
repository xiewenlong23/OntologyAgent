<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/value-type-constraints/
---
# Value type constraints
每个 value type 可以选择性地定义一个 constraint 来强制执行数据验证。您可以在 **Value Type Manager** 应用程序中 [创建新的 value type](/docs/foundry/object-link-types/create-value-type/) 时配置这些约束。可用的 value type constraints 以及它们可以应用到的 base types 如下：

Each value type may optionally define a constraint to enforce data validation. You can configure these constraints when [creating a new value type](/docs/foundry/object-link-types/create-value-type/) in the **Value Type Manager** application. The available value type constraints, along with what base types they can be applied to, are below:
* **Enum (one of)：** 表示一组静态允许值的 constraint。

* **有效的 base types：** String、Boolean、Decimal、Double、Float、Integer 或 Short。

* 对于 String properties，enum 值可以选择大小写敏感或不敏感。

* **Range：** 最小值、最大值或允许值的范围。

* **有效的 base types：** Decimal、Double、Float、Integer、Short、Date、Timestamp、String 或 Array。

* 对于 String properties，约束的是字符串的长度。

* 对于 Array properties，约束的是 array 的大小。

* **Enum (one of):** A constraint representing a static set of allowed values.
* **Valid base types:** String, Boolean, Decimal, Double, Float, Integer, or Short.
* For String properties, the enum values may optionally be case-sensitive or case-insensitive.
* **Range:** A minimum value, maximum value, or range of allowed values.
* **Valid base types:** Decimal, Double, Float, Integer, Short, Date, Timestamp, String, or Array.
* For String properties, the length of the string is constrained.
* For Array properties, the size of the array is constrained.
此外，以下 property types 具有可用的特定于类型的额外 constraints：

Additionally, the following property types have additional type-specific constraints available:
* **String：**
* **Regex：** 字符串必须匹配的正则表达式模式。regex 验证可以选择仅在匹配属性值的子字符串时通过。

* **RID：** 字符串必须是有效的 rid。

* **UUID：** 字符串必须是有效的 UUID。

* **Array：**
* **Uniqueness：** array 的所有元素必须是唯一的。

* **Nested：** 可以对 array 的元素应用 value type constraint。例如，可以对 array 中的每个字符串应用 regex constraint。

* **Struct：**
* **Element constraints：** struct 字段标识符与 value type 引用之间的映射，其中 struct 字段标识符指示应应用引用的 value type 的 struct 组件。

* **String:**
* **Regex:** A regex pattern that the string must match. The regex validation may optionally pass when matching only a substring of the property value.
* **RID:** The string must be a valid rid.
* **UUID:** The string must be a valid UUID.
* **Array:**
* **Uniqueness:** All elements of the array must be unique.
* **Nested:** A value type constraint can be applied to the elements of the array. For example, a regex constraint could be applied to every string in an array.
* **Struct:**
* **Element constraints:** A mapping between a struct field identifier and a value type reference, where the struct field identifier indicates the struct component to which the referenced value type should be applied.