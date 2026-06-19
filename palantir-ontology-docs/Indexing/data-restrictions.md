<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-indexing/data-restrictions/
---
# Data restrictions
Object Storage V2 (OSv2) 强制实施数据限制，以确保进入 ontology 的数据质量、提供更具确定性的行为，并提高整个平台的可读性。这些限制会在 indexing 期间进行验证。对于由 batch datasources 支持的 object types，违规行为将导致 indexing jobs 失败。对于由 streaming datasources 支持的 object types，违反这些限制的 records 将被丢弃。

Object Storage V2 (OSv2) enforces data restrictions to ensure the quality of data going into the ontology, provide more deterministic behavior, and increase legibility across the platform. These restrictions are validated during indexing. For object types backed by batch datasources, violations will cause indexing jobs to fail. For object types backed by streaming datasources, records that violate these restrictions are dropped.
## Primary keys and uniqueness
OSv2 强制要求 datasources 的 object primary keys 唯一。如果在单个 transaction 中存在重复的 primary keys，indexing 将失败并抛出错误。如果跨 transactions 存在重复的 primary keys，则将使用后面 transaction 中的版本。

OSv2 enforces unique object primary keys for datasources. If there are duplicate primary keys within a single transaction, indexing will fail and throw an error. If there are duplicate primary keys across transactions, the version in the later transaction will be used.
OSv2 禁止将某些数据类型用作 primary keys，以鼓励遵循 Ontology 建模最佳实践。以下类型**不能**用作 primary keys：

OSv2 prevents certain data types from being used as primary keys in order to encourage Ontology modeling best practices. The following types **cannot** be used as primary keys:
* Geopoint
* Geoshapes
* Arrays
* Time series properties
* Real number 类型（decimal、double、float）

* Geopoint
* Geoshapes
* Arrays
* Time series properties
* Real number types (decimal, double, float)
## Property type restrictions
* OSv2 在每次 sync 时强制 datasource schema 和 object type schema 之间的数据类型一致性。属性的不兼容数据类型将导致 build 失败。

* 当更改现有 property 的 base type 时（例如，从 `Double` 更改为 `Integer`），该属性的所有现有值必须严格与目标类型兼容。如果任何数据条目包含与新类型不兼容的值（例如在更改为 Integer 时包含小数，或包含货币符号），则 migration 将失败，并显示诸如 `A property could not be cast to the new type` 的错误。如果存在不兼容的值，schema migrations 将不会进行，并且 migration 过程无法自动清理或强制转换这些值。

* OSv2 不允许将 `NaN` 或 `±infinity` 用作 property 值。

* OSv2 不允许空字符串；在 OSv1 中，空字符串会被静默转换为 nulls。

* `Lat, Long` 应为不带括号的逗号分隔字符串，例如 `-29.123, 150.982`。

* OSv2 不允许包含嵌套数组的 properties。

* OSv2 不允许具有 array 数据类型的 properties 在数组内包含 null 元素。

* OSv2 在 restricted view datasources 的细粒度权限策略中支持 `Not` 条件，其中取反的字段是 collection 并具有**非空**约束。这可以在 Ontology Manager 中通过将相关 property 标记为 **required** 进行配置。

* OSv2 对 geopoint properties 实施更严格的验证。

* OSv2 enforces data type coherence between datasource schema and object type schema on every sync. Incompatible data types for a property will cause the build to fail.
* When changing the base type of an existing property (for example, from `Double` to `Integer`), all existing values for that property must be strictly compatible with the target type. If any data entries include values incompatible with the new type (such as fractional numbers when changing to Integer, or currency symbols), the migration will fail with an error such as `A property could not be cast to the new type`. Schema migrations will not proceed if incompatible values exist, and the migration process cannot automatically clean or coerce these values.
* OSv2 does not allow `NaN` or `±infinity` as property values.
* Empty strings are not allowed in OSv2; in OSv1, empty strings were silently converted to nulls.
* `Lat, Long` should be a comma-separated string with no parentheses, for example `-29.123, 150.982`.
* OSv2 does not allow properties with nested arrays.
* OSv2 does not allow properties with array data types to have null elements within the array.
* OSv2 supports `Not` conditions in granular permissioning policies of restricted view datasources where the negated field is a collection and has a **non-empty** constraint. This can be configured in Ontology Manager by marking the relevant property as **required**.
* OSv2 has stricter validations on geopoint properties.
## Property size limits
OSv2 对单个 properties 强制实施大小限制，以确保可靠的 indexing 性能和稳定性。这些限制解决了在处理大型 property 值时可能出现的序列化约束和内存压力问题。

OSv2 enforces size limits on individual properties to ensure reliable indexing performance and stability. These limits address serialization constraints and memory pressure that can occur when processing large property values.
| Property type | Maximum size |
| ------------- | ------------ |
| String properties | 12 MB |
| Array properties | 100,000 elements |
超出这些限制的 properties 将导致 indexing jobs 失败。这些限制最初针对由 batch datasources 支持的 object types 强制实施；未来将对具有 streaming datasources 的 object types 应用类似的限制。

Properties exceeding these limits will cause indexing jobs to fail. These limits are initially enforced for object types backed by batch datasources; similar limits will be applied to object types with streaming datasources in the future.
### Recommendations for large data
* **大型字符串属性：** 如果您需要存储超过 12 MB 的数据，请改用 [media reference property](/docs/foundry/object-link-types/base-types/#media-references)。Media reference 允许您将大文件或二进制内容与 object 关联，而不会影响 indexing 性能。

* **大型数组：** 如果您需要建模的关系将超过 100,000 个元素，请考虑使用 [link type](/docs/foundry/object-link-types/create-link-type/) 来代替数组属性。Link 提供了一种更具可扩展性和可查询性的方式来表示 object 之间的关系。

* **Large string properties:** If you need to store data exceeding 12 MB, use a [media reference property](/docs/foundry/object-link-types/base-types/#media-references) instead. Media references allow you to associate large files or binary content with an object without impacting indexing performance.
* **Large arrays:** If you need to model relationships that would exceed 100,000 elements, consider using [link types](/docs/foundry/object-link-types/create-link-type/) instead of array properties. Links provide a more scalable and queryable way to represent relationships between objects.