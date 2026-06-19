<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/actions-on-structs/
---
# Actions on structs
[Struct property](/docs/foundry/object-link-types/structs-overview/) 值可以通过 actions 创建和修改，通过 struct parameter 中提供的值来实现。

[Struct property](/docs/foundry/object-link-types/structs-overview/) values can be created and modified with actions, through values supplied in a struct parameter.
## Struct parameters
struct parameter 是基类型为 `STRUCT` 的 parameter，其中该类型包含嵌套的 parameter fields，这些字段具有各自的名称和基类型。struct parameter 只能用于为 struct property 提供值。struct parameter fields 支持的基类型为 `BOOLEAN`、`DATE`、`DOUBLE`、`GEOPOINT`、`INTEGER`、`LONG`、`STRING` 和 `TIMESTAMP`。

A struct parameter is a parameter of base type `STRUCT`, where the type contains nested parameter fields that have their own individual names and base types. A struct parameter can be only be used to supply values for a struct property. The supported base types for struct parameter fields are  `BOOLEAN`, `DATE`, `DOUBLE`, `GEOPOINT`, `INTEGER`, `LONG`, `STRING`, and `TIMESTAMP`.
下面，我们有一个用于 `Create Ticket` action 的 `Resolution` struct parameter。`summary`、`resolutionTime` 和 `owner` 的嵌套字段将 ticket 的解决方式信息编译到单个 parameter 中。

Below, we have a `Resolution` struct parameter for a `Create Ticket` action. The nested fields of `summary`, `resolutionTime`, and `owner` compile information on how the ticket was resolved into a single parameter.
![A struct parameter with nested fields.](/docs/resources/foundry/action-types/struct-parameter-nested-fields.png)
## Defining actions on struct properties
使用带有 struct parameters 的 actions，您可以创建和修改具有 struct properties 的 object types。struct property 的值通过映射到该 property 的 struct parameter 提交；struct property 的每个单独字段映射到 struct parameter 的特定字段。在下面的示例中，`Resolution` struct parameter 的每个字段都映射到 `Ticket` object type 的 `Resolution` struct property 中其对应的字段。

Using actions with struct parameters, you can create and modify object types with struct properties. The values for the struct property are submitted in a struct parameter mapped to the property; each individual field of the struct property is mapped to a specific field of a struct parameter. In the example below, each field of the `Resolution` struct parameter is mapped to its corresponding field in the `Resolution` struct property of the `Ticket` object type.
![Struct property field mappings.](/docs/resources/foundry/action-types/struct-field-mapping.png)
struct property 与 struct parameter 之间的映射必须是完整的，struct property 的每个字段都必须映射到 struct parameter 中的一个字段。struct parameter 字段的基类型*必须*与映射的 struct property 字段的基类型匹配。如果要对 struct property 类型进行任何破坏性更改（例如，添加新字段、删除字段或更改字段的基类型），则还必须修改相关的 action types 以纳入这些更改。

A mapping between a struct property and a struct parameter must be complete, with each field of the struct property mapped to a field in the struct parameter. The base type of the struct parameter field *must* match the base type of a mapped struct property field. If any breaking changes are to be made to the struct property type (for example, if a new field is added, a field is deleted, or a field's base type is changed), then the related action types must also be modified to incorporate those changes.
### Struct parameters in an action form
struct parameter 可以像任何其他 parameter 类型一样通过 action forms 填充。但是，struct parameter fields 在表单中作为一个组进行渲染，而不是单独渲染。

A struct parameter can be populated through action forms similarly to any other parameter type. However, struct parameter fields are rendered as a group in the form instead of individually.
![Struct parameter in an action form.](/docs/resources/foundry/action-types/struct-parameter-form.png)
## Default values for struct parameter fields
默认值是为 struct parameter fields 单独定义的。每个 struct parameter field 映射到指定 object type 的 struct property 的字段。必须为 struct parameter 中的所有字段定义默认值，并且必须映射到同一 object type struct property 的字段。只有 struct property 字段才能充当 struct parameter 字段的默认值。其 struct property 字段将充当默认值的 object type 在 `ObjectReference` parameter 中指定。

Default values are defined individually for struct parameter fields. Each struct parameter field is mapped to fields of a specified object type's struct property. A default value must be defined for all fields in the struct parameter and must be mapped to fields of the same object type struct property. Only struct property fields can act as default values for struct parameter fields. The object type whose struct property fields will act as default values is specified in the `ObjectReference` parameter.
![Define default values for struct parameter fields.](/docs/resources/foundry/action-types/struct-parameter-default-values.png)
在提交 action 时，会提供 `ObjectReference` parameter 中指定类型的 object 实例，该 object 的 struct property 字段值将自动填充相应 struct parameter 字段的值。

An instance of an object of the type specified in the `ObjectReference` parameter is supplied when submitting the action, and that object's struct property field values will automatically fill in the values of the corresponding struct parameter fields.
![Default values applied for struct parameter fields.](/docs/resources/foundry/action-types/struct-parameter-form-default-values.png)
## Constraints on struct parameter fields
可以为 struct parameter fields 单独配置 constraints，就像常规 parameters 一样。例如，可以对 string 类型的 struct parameter fields 定义 string length constraint，以仅允许长度在 10 到 500 个字符之间的 string 值。这意味着 `Resolution` struct parameter 的 `summary` 字段必须至少为 10 个字符长，但不超过 500 个字符。

Constraints can be configured individually for struct parameter fields, as with regular parameters. For example, a string length constraint can be defined on struct parameter fields of string types to only allow string value that are between 10 and 500 characters long. This would mean that the `summary` field of a the `Resolution` struct parameter must be at least 10 characters long, but no longer than 500 characters.
![Define constraints for struct parameter fields.](/docs/resources/foundry/action-types/struct-parameter-field-constraint.png)
struct parameter 值仅在*所有*字段都满足定义的 constraint 时才有效。用户仅当每个字段值都满足为其定义的 constraints 时才能提交 struct parameter 值。正如为 `summary` 字段所定义的那样，短于 10 个字符的值将是无效的。

A struct parameter value is *only* valid if *all* fields meet the defined constraint. Users can only submit a struct parameter value if each field value satisfies the constraints defined on them. As defined for the `summary` field, a value shorter than 10 characters would be invalid.
![Constraints applied to struct parameter field values.](/docs/resources/foundry/action-types/invalid-struct-parameter-value.png)
## Limitations
在使用 actions 创建或修改 struct parameters 时，请考虑以下限制：

Consider the following limitations when creating or modifying struct parameters with actions:
* Struct property 值只能通过 *struct parameters* 创建或修改。不支持其他形式的输入，例如静态值或对 object properties 的引用。

* 一个 struct property 只能通过 *单个* struct parameter 创建或修改。actions 中的 struct property 映射不能使用多个 parameter。

* struct parameter 只能用于创建或修改 *struct* properties。struct parameter 字段不能单独用于创建或修改非 struct properties。

* 只有对 *单个 object type struct property 值* 的引用才能作为 struct parameter 字段的默认值。不支持其他形式的输入，例如静态值。

* Struct property values can only be created or modified through *struct parameters*. Other forms of entry, such as static values or references to object properties, are not supported.
* A struct property can only be created or modified through a *single* struct parameter. A struct property mapping in actions cannot more than one parameter.
* A struct parameter can only be used to create or modify *struct* properties. Struct parameter fields cannot be used individually to create or modify non-struct properties.
* Only references to *a single object type struct property values* can act as default values for struct parameter fields. Other forms of entry, such as static values, are not supported.