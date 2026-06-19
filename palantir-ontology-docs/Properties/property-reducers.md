<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/property-reducers/
---
# Property reducers \[Beta]
> **ℹ️ 注意: Beta**

> Property reducers 处于开发的 [beta](/docs/foundry/platform-overview/development-life-cycle/) 阶段，可能在您的注册中不可用。在积极开发过程中，功能可能会发生变化。

[PARA_9]
**Property reducer** 使您能够将 [array property](/docs/foundry/object-link-types/properties-overview/#supported-property-types) 转换为数组中的单个值，以用于显示和 interface 实现目的。Reduction *不会* 更改底层的 property type 或存储的 property 数据；相反，它在读取 property 值时提供对数组中归约值的访问。

[PARA_10]
例如，对包含多个检查日期的数组应用 reducer，可以实现在表或应用中查看该 property 时仅显示最近的日期，同时确保完整的数组仍可被查询和其他操作访问。支持 reducers 的应用（例如 [Workshop](/docs/foundry/workshop/overview/)）还允许您在悬停或展开视图中查看完整的数组。

[PARA_11]
Reducers 适用于包含数值型、时间型、字符串和布尔型 base types 的 array properties。您可以根据使用受支持 base type 的任何 struct 字段对 [struct](/docs/foundry/object-link-types/structs-overview/) 数组进行归约。请查看下方的 [tables](#supported-and-unsupported-base-types) 以了解 property reducer 受支持的 base types 的更多信息。

[PARA_12]
在以下情况下使用 property reducers：

[PARA_13]
* 您的历史或时间数据存储在数组中，例如检查日期、状态更新或测量读数。

* 您希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留 property 的完整历史记录。

* Array properties 需要非数组类型才能令人满意地实现 [interface properties](/docs/foundry/interfaces/implement-interface/)。

[PARA_14]
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。
> **ℹ️ 注意: Beta**

> Property reducers are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.
**Property reducer** 使您能够将 [array property](/docs/foundry/object-link-types/properties-overview/#supported-property-types) 转换为数组中的单个值，以用于显示和 interface 实现目的。Reduction *不会* 更改底层的 property type 或存储的 property 数据；相反，它在读取 property 值时提供对数组中归约值的访问。

[PARA_10]
例如，对包含多个检查日期的数组应用 reducer，可以实现在表或应用中查看该 property 时仅显示最近的日期，同时确保完整的数组仍可被查询和其他操作访问。支持 reducers 的应用（例如 [Workshop](/docs/foundry/workshop/overview/)）还允许您在悬停或展开视图中查看完整的数组。

[PARA_11]
Reducers 适用于包含数值型、时间型、字符串和布尔型 base types 的 array properties。您可以根据使用受支持 base type 的任何 struct 字段对 [struct](/docs/foundry/object-link-types/structs-overview/) 数组进行归约。请查看下方的 [tables](#supported-and-unsupported-base-types) 以了解 property reducer 受支持的 base types 的更多信息。

[PARA_12]
在以下情况下使用 property reducers：

[PARA_13]
* 您的历史或时间数据存储在数组中，例如检查日期、状态更新或测量读数。

* 您希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留 property 的完整历史记录。

* Array properties 需要非数组类型才能令人满意地实现 [interface properties](/docs/foundry/interfaces/implement-interface/)。

[PARA_14]
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。

A **property reducer** enables you to transform an [array property](/docs/foundry/object-link-types/properties-overview/#supported-property-types) into a single value in the array for display and interface implementation purposes. Reduction does *not* change the underlying property type or property data stored; instead, it provides access to the reduced value in the array when reading the property value.
例如，对包含多个检查日期的数组应用 reducer，可以实现在表或应用中查看该 property 时仅显示最近的日期，同时确保完整的数组仍可被查询和其他操作访问。支持 reducers 的应用（例如 [Workshop](/docs/foundry/workshop/overview/)）还允许您在悬停或展开视图中查看完整的数组。

[PARA_11]
Reducers 适用于包含数值型、时间型、字符串和布尔型 base types 的 array properties。您可以根据使用受支持 base type 的任何 struct 字段对 [struct](/docs/foundry/object-link-types/structs-overview/) 数组进行归约。请查看下方的 [tables](#supported-and-unsupported-base-types) 以了解 property reducer 受支持的 base types 的更多信息。

[PARA_12]
在以下情况下使用 property reducers：

[PARA_13]
* 您的历史或时间数据存储在数组中，例如检查日期、状态更新或测量读数。

* 您希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留 property 的完整历史记录。

* Array properties 需要非数组类型才能令人满意地实现 [interface properties](/docs/foundry/interfaces/implement-interface/)。

[PARA_14]
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。

For example, applying a reducer to an array with multiple inspection dates allows you to display only the most recent date when viewing the property in a table or application but ensures the full array remains accessible for queries and other operations. Applications that support reducers, such as [Workshop](/docs/foundry/workshop/overview/), also enable you to view the complete array on hover or in expanded views.
Reducers 适用于包含数值型、时间型、字符串和布尔型 base types 的 array properties。您可以根据使用受支持 base type 的任何 struct 字段对 [struct](/docs/foundry/object-link-types/structs-overview/) 数组进行归约。请查看下方的 [tables](#supported-and-unsupported-base-types) 以了解 property reducer 受支持的 base types 的更多信息。

[PARA_12]
在以下情况下使用 property reducers：

[PARA_13]
* 您的历史或时间数据存储在数组中，例如检查日期、状态更新或测量读数。

* 您希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留 property 的完整历史记录。

* Array properties 需要非数组类型才能令人满意地实现 [interface properties](/docs/foundry/interfaces/implement-interface/)。

[PARA_14]
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。

Reducers work with array properties containing numeric, temporal, string, and boolean base types. You can reduce [struct](/docs/foundry/object-link-types/structs-overview/) arrays based on any struct field that uses a supported base type. Review the [tables below](#supported-and-unsupported-base-types) to learn more about a property reducer's supported base types.
## When to use property reducers
在以下情况下使用 property reducers：

[PARA_13]
* 您的历史或时间数据存储在数组中，例如检查日期、状态更新或测量读数。

* 您希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留 property 的完整历史记录。

* Array properties 需要非数组类型才能令人满意地实现 [interface properties](/docs/foundry/interfaces/implement-interface/)。

[PARA_14]
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。

Use property reducers when:
* 您的历史或时间数据存储在数组中，例如检查日期、状态更新或测量读数。

* 您希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留 property 的完整历史记录。

* Array properties 需要非数组类型才能令人满意地实现 [interface properties](/docs/foundry/interfaces/implement-interface/)。

[PARA_14]
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。

* Your historical or temporal data is stored in arrays, such as inspection dates, status updates, or measurement readings.
* You want to display the latest/earliest, highest/lowest, or first/last array value in a table or application while preserving the property's full history.
* Array properties require non-array types to satisfactorily implement [interface properties](/docs/foundry/interfaces/implement-interface/).
## Supported and unsupported base types
Reducers 适用于基于底层 base type 的 array properties。以下 tables 对哪些数组子类型支持 reducers、哪些不支持进行了分类。

Reducers work with array properties based on the underlying base type. The following tables categorize which array subtypes support reducers and which do not.
### Supported base types
Property reducers 可用于包含以下子类型的数组：

Property reducers are available for arrays containing the following subtypes:
| Category | Base types | Reducer options |
|----------|-----------|----------------|
| **Numeric** | `Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`, `Decimal` | Highest, lowest |
| **Temporal** | `Date`, `Timestamp`| Most recent (latest), Least recent (earliest) |
| **String** | `String` | First, last (lexicographically) |
| **Boolean** | `Boolean` | True first, false first |
| **Struct** | By any supported struct field [outlined below](#support-for-struct-arrays) | Depends on the base type of the struct field |
### Unsupported base types
Property reducers *不可*用于包含以下子类型的数组：

Property reducers are *not* available for arrays containing the following subtypes:
* `Attachment`
* `Cipher Text`
* `Geohash`
* `Geoshape`
* `Geotime Series Reference`
* `Marking`
* `Media Reference`
* `Time Dependent`
* `Vector`
* `Attachment`
* `Cipher Text`
* `Geohash`
* `Geoshape`
* `Geotime Series Reference`
* `Marking`
* `Media Reference`
* `Time Dependent`
* `Vector`
### Support for struct arrays
Reducers 根据 struct 内的特定 **field**（而非 struct 本身）对 struct 数组进行操作。只能通过使用上述 [supported base types](#supported-base-types) 中之一的 struct 字段进行 reduce。还可以使用不同的 struct 字段配置多个 reducers，以处理平局（tie-breaking）场景。

Reducers function on struct arrays based on a specific **field** within the struct, not the struct itself. You can only reduce by struct fields that use one of the [supported base types](#supported-base-types) listed above. You can also configure multiple reducers using different struct fields to handle tie-breaking scenarios.
## Configure a property reducer
1. 导航至 **Ontology Manager**。

2. 在左侧面板的 **Resources** 下选择 **Object types**，搜索并选择您的 object type。

3. 从 object type 的 **Properties** 选项卡中选择要配置的数组 property。

4. 在右侧打开的 property 编辑器面板中选择 **Interaction** 选项卡。

5. 滚动至 **Reduce array** 部分。

1. Navigate to **Ontology Manager**.
2. Search for and select your object type by choosing **Object types** under **Resources** in the left panel.
3. Select the array property to configure from your object type's **Properties** tab.
4. Choose the **Interaction** tab in the property editor panel that opens on the right.
5. Scroll to the **Reduce array** section.

> 📷 **[图片: Property sidebar with Interactions tab]**

> 📷 **[图片: Property sidebar with Interactions tab]**

6. 选择 **Add array reducer**。

7. 根据 property 的 base type，选择所需的 [reducer option](#supported-base-types)。

6. Select **Add array reducer**.
7. Select your desired [reducer option](#supported-base-types) based on the property's base type.

> 📷 **[图片: Add reducer section]**

> 📷 **[图片: Add reducer section]**

8. **保存**您的更改。

8. **Save** your changes.
## Configure a property reducer for struct arrays
Struct 数组为 reducers 提供了最大的灵活性。您可以根据使用 [supported base type](#supported-base-types) 的 struct 中的任何字段进行 reduce，并配置多个 reducers 以应对平局（tie-breaking）场景。

Struct arrays offer the most flexibility for reducers. You can reduce based on any field in the struct that uses a [supported base type](#supported-base-types) and configure multiple reducers for tie-breaking scenarios.
### Example: Customer review history
考虑一个 `Product` object type，其具有一个 `customerReviews` struct 数组 property，其中包含以下字段：

Consider a `Product` object type with a `customerReviews` struct array property that contains the following fields:
* `rating`（`Integer`）：一到五星的评分。

* `reviewDate`（`Date`）：客户发表评论的日期。

* `reviewerName`（`String`）：评论者的姓名。

* `verifiedPurchase`（`Boolean`）：表示购买是否已验证。

* `rating` (`Integer`): A one to five star rating.
* `reviewDate` (`Date`): The date the customer posted the review.
* `reviewerName` (`String`): The reviewer's name.
* `verifiedPurchase` (`Boolean`): Indicates whether or not the purchase was verified.
`Product` object 的 `customerReviews` property 的示例数据如下所示：

Sample data for a `Product` object's `customerReviews` property resembles:
| `rating` | `reviewDate` | `reviewerName` | `verifiedPurchase` |
|--------|-----------|--------------|-----------------|
| 5 | 2024-11-20 | Alice Chen | true |
| 3 | 2024-11-15 | Bob Smith | false |
| 4 | 2024-11-22 | Carol Lee | true |
### Configure a single reducer
> **✅ 成功: Tip**

> 在继续操作之前，请查阅 [property reducer configuration instructions](#configure-a-property-reducer) 和 [supported base types](#supported-base-types) 表格。
> **✅ 成功: Tip**

> Review the [property reducer configuration instructions](#configure-a-property-reducer) and the [supported base types](#supported-base-types) table before proceeding.
您可以在 struct 字段上配置单个 reducer，Foundry 将使用该 reducer 将 struct 数组 reduce 为单个 struct，并通过配置了 reducer 的字段对要显示的值进行排序。

You can configure a single reducer on a struct field, which Foundry uses to reduce the array of structs to a single struct, sorting the values to display by the field with the configured reducer.
* **Single reducer:** Render the latest `reviewDate`.
* **Result:** Displays the struct containing Carol Lee's four star review from `2024-11-22`.
* **Single reducer:** Render the latest `reviewDate`.
* **Result:** Displays the struct containing Carol Lee's four star review from `2024-11-22`.
Users can still query for and access the full review history.
Users can still query for and access the full review history.
### Configure multiple reducers
You can configure multiple reducers to handle tie-breaking scenarios:
You can configure multiple reducers to handle tie-breaking scenarios:
* **Primary reducer:** Sort the structs and display the struct with the latest `reviewDate`.
* **Fallback reducer:** Render the highest `rating`.
* **Use case:** If two reviews are posted on the same day, render the higher-rated review.
* **Primary reducer:** Sort the structs and display the struct with the latest `reviewDate`.
* **Fallback reducer:** Render the highest `rating`.
* **Use case:** If two reviews are posted on the same day, render the higher-rated review.
The fallback reducer *only* applies when the primary reducer results in multiple items. The primary reducer is always evaluated first, and only items that tie on the primary criteria are further reduced by the fallback reducer. This reduction behavior is repeated for any additional configured reducers.
The fallback reducer *only* applies when the primary reducer results in multiple items. The primary reducer is always evaluated first, and only items that tie on the primary criteria are further reduced by the fallback reducer. This reduction behavior is repeated for any additional configured reducers.

> 📷 **[图片: Struct array reducer configuration]**

> 📷 **[图片: Struct array reducer configuration]**

## How reducers appear in applications
Applications that support reducers display the reduced value in compact views like tables or lists, while providing access to the full array through an expanded view or on-hover mechanism. This approach allows users to quickly scan data without seeing verbose array representations, while still being able to inspect the complete array when needed.
Applications that support reducers display the reduced value in compact views like tables or lists, while providing access to the full array through an expanded view or on-hover mechanism. This approach allows users to quickly scan data without seeing verbose array representations, while still being able to inspect the complete array when needed.
For example, an application might display only `2024-11-22` (the most recent date) in a table cell, but reveal the full array of dates when the user hovers over or expands that cell.
For example, an application might display only `2024-11-22` (the most recent date) in a table cell, but reveal the full array of dates when the user hovers over or expands that cell.
## Use property reducers with interfaces
Use property reducers to ensure an array property can implement non-array interface properties. This allows object types with array data to be mapped to [interface properties](/docs/foundry/interfaces/implement-interface/) that expect single values.
Use property reducers to ensure an array property can implement non-array interface properties. This allows object types with array data to be mapped to [interface properties](/docs/foundry/interfaces/implement-interface/) that expect single values.
### Example: Render the most recent equipment maintenance date through an interface implementation
**Interface:** `Asset`
**Interface:** `Asset`
* Property: `lastMaintenanceDate` (`Date`)
* Property: `lastMaintenanceDate` (`Date`)
**Object type:** `Equipment`
**Object type:** `Equipment`
* Property: `maintenanceHistory` (`Date` array)
* Values: `[2024-01-15, 2024-03-22, 2024-11-01]`
* **Reducer:** Latest `maintenanceHistory` date.
* **Implementation:** `Date` array property implements a single `Date` through the configured reducer. A user will see `2024-11-01` when viewing the property via the interface.
* Property: `maintenanceHistory` (`Date` array)
* Values: `[2024-01-15, 2024-03-22, 2024-11-01]`
* **Reducer:** Latest `maintenanceHistory` date.
* **Implementation:** `Date` array property implements a single `Date` through the configured reducer. A user will see `2024-11-01` when viewing the property via the interface.
The `Equipment` object type can implement the `Asset` interface because the reducer allows its `maintenanceHistory` array property to be represented as a single `Date` value. When users view an `Equipment` object through the `Asset` interface, they see only the most recent maintenance date.
The `Equipment` object type can implement the `Asset` interface because the reducer allows its `maintenanceHistory` array property to be represented as a single `Date` value. When users view an `Equipment` object through the `Asset` interface, they see only the most recent maintenance date.

> 📷 **[图片: Interface implementation via reducer]**

> 📷 **[图片: Interface implementation via reducer]**

> **⚠️ 警告**

> 当在 object type 上使用 reduced array value 来满足作为 [interface action](/docs/foundry/action-types/actions-on-interfaces/) 参数的 interface property 时,在对该类型的 object 调用该 action 将返回 error。但是,你仍然可以通过 reduced array value 对未实现该 interface 的 object 使用该 interface action。
> **⚠️ 警告**

> When using a reduced array value on an object type to satisfy an interface property that is a parameter of an [interface action](/docs/foundry/action-types/actions-on-interfaces/), the action will return an error when called on objects of that type. However, you can still use the interface action for objects that do not implement the interface through a reduced array value.
## Combine property reducers with struct main fields
当将 property reducer 与 [struct main field](/docs/foundry/object-link-types/struct-main-fields/) 结合使用时,你可以启用 property display 并扩展它们可以实现的 interface 的数量和形态。

When you combine property reducers with [struct main fields](/docs/foundry/object-link-types/struct-main-fields/), you enable property display and expand the number and shape of interfaces they can implement.
请参考下面的 `Event` object type,它包含一个 `Locations` property,该 property 是一个 struct 数组:

Consider the `Event` object type below, which contains a `Locations` property that is an array of structs:
**Object type:** `Event`
**Object type:** `Event`
* Property: `locations`(`Struct` 数组)

* Struct 字段:`streetName`(`String`)、`dateCollected`(`Date`)、`numberOfGuests`(`Integer`)。

* **已配置的 Main field:** `streetName`

* **已配置的 Reducer:** 按 `dateCollected` 取最新。

* Property: `locations` (`Struct` array)
* Struct fields: `streetName` (`String`), `dateCollected` (`Date`), `numberOfGuests` (`Integer`).
* **Main field configured:** `streetName`
* **Reducer configured:** Most recent by `dateCollected`.
将 `streetName` 字段配置为 main field,并将最近的 `dateCollected` 配置为 property reducer,这将启用多种 interface 实现选项:

With the `streetName` field configured as the main field and most recent `dateCollected` as the property reducer, this enables multiple interface implementation options:
| Configuration | Can implement |
|---------------|---------------|
| Neither feature configured | `Struct Array` only |
| Main field only | `Struct Array`, `String Array` |
| Reducer only | `Struct Array`, `Struct` |
| **Both configured** | `Struct Array`, `String Array`, `Struct`, `String` |
举例来说,当同时配置了 struct main field 和 property reducer 时,你可以使用 `locations` property 来满足 interface 中的 *单个* string property,例如下方图片中假设的 `Event` interface 的 `Event street name`。

As an example, with both a struct main field and property reducer configured, you can use the `locations` property to fulfill a *single* string property from an interface, such as `Event street name` from the notional `Event` interface in the image below.

> 📷 **[图片: 通过 reducer 和 main field 实现单个 string]**

> 📷 **[图片: Single string implementation via reducer and main field]**

当同时配置 struct main field 和 property reducer 时,转换过程:

When you configure both a struct main field and a property reducer, the transformation:
* 应用已配置的 property reducer,根据日期获取最新的 location。

* 提取已配置的 main field 并将其值作为 string 返回。

* Applies the configured property reducer, fetching the most recent location based on its date.
* Extracts the configured main field and returns its value as a string.
这意味着单个 property 可以实现需要以下任意类型的 interface:`Struct Array`、`String Array`、`Struct` 或 `String`。

This means a single property can implement interfaces requiring any of these types: `Struct Array`, `String Array`, `Struct`, or `String`.
## Limitations and considerations
* **无法直接查询 reduced value:** 你无法基于 reduced value 进行过滤或查询。查询作用于完整数组,而不是 reduced 后的表示。

* **不支持针对 reduced 或 struct main field 实现的 interface action:** 针对通过 property reducer 或 [struct main field](/docs/foundry/object-link-types/struct-main-fields/) 实现的 property 进行编辑的 [Interface action](/docs/foundry/action-types/actions-on-interfaces/),在对这些类型的 object 调用时将返回 error。这是因为 reduced value 和 struct main field value 无法被转换回底层的 object property。例如,从数组中选择一个元素的 reducer 没有逆向操作来重建完整数组;提取部分字段的 struct main field 无法填充剩余字段。不针对这些 property 的 interface action,或针对未通过 reducer 或 struct main field 实现 interface 的 object 的 action,均按预期正常工作。

* **No direct querying of reduced value:** You cannot filter or query based on the reduced value. Queries operate on the full array, not the reduced representation.
* **Interface actions are not supported for reduced or struct main field implementations:** [Interface actions](/docs/foundry/action-types/actions-on-interfaces/) that edit a property implemented through a property reducer or [struct main field](/docs/foundry/object-link-types/struct-main-fields/) will return an error when called on objects of that type. This is because reduced and struct main field values cannot be translated back to the underlying object property. For example, a reducer that selects one element from an array has no inverse operation to reconstruct the full array; struct main fields that extract a subset of fields have no way to populate the remaining ones. Interface actions that do not target these properties, or that target objects implementing the interface without reducers or struct main fields, work as expected.
## FAQs
### Can I change or remove a reducer after configuration?
可以。你可以随时在 Ontology Manager 中修改或移除 reducer。变更不需要 reindex 并立即生效。

Yes, you can modify or remove reducers at any time in Ontology Manager. Changes do not require a reindex and take effect immediately.
### What happens if multiple items tie for the reducer criteria?
对于 struct 数组,你可以配置 fallback reducer 来处理并列情况。Fallback reducer 仅针对在主 reducer 上并列的项进行评估。对于 primitive 数组或没有 fallback reducer 的 struct,将以确定但无序的方式返回其中一个并列值。

For struct arrays, you can configure fallback reducers to handle ties. The fallback reducer is only evaluated for items that tie on the primary reducer. For primitive arrays or structs without fallback reducers, one of the tied values is returned in a deterministic but unordered manner.
### Can I use reducers with edit-only properties?
可以。你可以为 [edit-only property](/docs/foundry/object-link-types/edit-only-properties/) 配置 reducer。Reducer 配置与该 property 是否具有 backing column 无关。

Yes, you can configure reducers for [edit-only properties](/docs/foundry/object-link-types/edit-only-properties/). The reducer configuration is independent of whether the property has a backing column.
### Do reducers function across all applications?
应用程序正在逐步推出对 reduced properties 的支持。如果您在某个 property 上配置了 reducer，但使用的应用程序尚不支持 reducer，则不应破坏任何现有功能，该 property 将继续以数组形式显示。只有支持 reducer 的应用程序才具备显示 reduced value 的能力。

Applications are progressively rolling out support for reduced properties. If you configure a reducer on a property and use an application that doesn't yet support reducers, it should not break any existing functionality, the property will simply continue to be displayed as an array. Only applications that support reducers will have the ability to display the reduced value.