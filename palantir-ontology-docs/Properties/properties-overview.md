<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/properties-overview/
---
# Properties
[object type](/docs/foundry/object-link-types/object-types-overview/) 的 **property** 是现实世界实体或事件特征的模式定义。**property value** 是指 object 上 property 的值,或该现实世界实体或事件的单个实例。

A **property** of an [object type](/docs/foundry/object-link-types/object-types-overview/) is the schema definition of a characteristic of a real-world entity or event. A **property value** refers to the value of a property on an object, or a single instance of that real world entity or event.
例如,在 Ontology Manager 中,`Employee` object type 可能具有 `employee number`、`start date` 和 `role` properties。概念上的员工 "Melissa Chang" 可能具有 property values "11502" 对应 `employee number`,"October 9, 2016" 对应 `start date`,以及 "software engineer" 对应 `role`。

For example, in the Ontology Manager, an `Employee` object type may have properties `employee number`, `start date`, and `role`. The notional employee “Melissa Chang” may have property values “11502” for `employee number`, “October 9, 2016” for `start date`, and “software engineer” for `role`.
类似地,在 Ontology Manager 中,`Flight` object type 可能具有 `departure date`、`arrival date` 和 `passenger count` properties。object "JFK → SFO 24-02-2021" 可能具有 property values "24-02-2021" 对应 `departure date`,"25-02-2021" 对应 `arrival date`,以及 "150" 对应 `passenger count`。

Similarly, in the Ontology Manager, a `Flight` object type may have properties `departure date`, `arrival date`, and `passenger count`. The object “JFK → SFO 24-02-2021” may have property values “24-02-2021” for `departure date`, “25-02-2021” for `arrival date`, and “150” for `passenger count`.
支撑 Ontology 的概念与 dataset 的结构具有类似的概念。Ontology 中 property 的定义类似于 dataset 中的 column 的定义,而 property value 的定义类似于 dataset 中 field 的定义。例如,`Employee` dataset 可能具有 `departure date`、`arrival date` 和 `passenger count` 的 columns。在这种情况下,单个 field 将具有 employee "Melissa Chang" 所在行的 `employee number` 列的值 "11502"。

The concepts underpinning the Ontology have analogous concepts in the structure of a dataset. The definition of a property in the Ontology is analogous to that of a column in a dataset, while the definition of a property value is analogous to that of a field in the dataset. For example, an `Employee` dataset may have columns for `departure date`, `arrival date`, and `passenger count`. In this case, a single field will have the value “11502” for the `employee number` column of the row for employee “Melissa Chang.”
Foundry Ontology 不仅仅是一个抽象的数据模型，它会将每个本体（Ontology）概念映射到组织的实际数据，使该数据资产能够为实际应用提供支持。通过在 Ontology Manager 中向 object type 添加 backing datasources，可以在用户应用中创建和显示 property 值。要为 `Employee` 类型 object 的 `employee number`、`start date` 和 `role` properties 创建 property 值，组织需要向 `Employee` object type 添加 backing datasources，并将其员工目录以及其他企业数据接入 Ontology。

[PARA_1]
要了解更多关于 base types 的信息，请参阅 [base types](/docs/foundry/object-link-types/base-types/)。

[PARA_2]
Property 在 Ontology 中通过以下元数据表示：

[PARA_3]
* **ID（标识符）：** Property 的唯一标识符，主要用于在配置应用时引用该 property。例如，`start-date` 可以是 start date property 的 ID。

* **Display name（显示名称）：** 在用户应用中访问此 property 的值时显示给任何人的名称。例如，`start date` property 的 display name 可以是 `Start date`。

* **Description（描述）：** 关于该 property 的说明性文本，任何人都可以在用户应用中阅读。例如，`start date` property 的描述可以是 `The day the employee began new hire training`。

* **RID：** Foundry 中每个资源自动生成的唯一标识符。Property 的 RID 将在整个平台的错误消息中被引用。

* **Status（状态）：** 向用户和其他 Ontology 构建者发出的信号，表明该 property 在开发过程中的位置。可以是 `active`、`experimental` 或 `deprecated`。默认情况下，`start date` property 的状态为 `experimental`。阅读更多关于 [statuses](/docs/foundry/object-link-types/metadata-statuses/) 的内容。

* **API name（API 名称）：** 在代码中以编程方式引用该 property 时使用的名称。例如，`start date` property 的 API name 可以是 `startDate`。阅读更多关于 [API names](/docs/foundry/functions/api-objects-links/) 的内容。

* **Keys（键）：** 指示该 property 是否为 object type 的 title key 或 primary key。

* **Title key** 是作为该类型 object 显示名称的 property。例如，将 `full name` property 设置为 `Employee` object type 的 title key，将使用该 property 的值（例如假设的员工 "Melissa Chang" 和 "Diego Rodriguez"）作为各个 `Employee` object 的 display name。

* **Primary key** 是作为 object type 每个实例唯一标识符的 property，意味着 backing datasources 中每一行的该 property 值必须不同。例如，可以使用 `employee number` property 的值来将 "Melissa Chang" 标识为组织内的唯一员工。

* **Base type（基础类型）：** 指示该 property 的值类型，并确定在用户应用中可用的操作集。例如，`start date` property 的 base type 为 `date`。用户应用将允许您使用此 property 配置时间线 widget。

* **Value formatting（值格式化）：** 根据 property 的 base type，可应用数值格式化、日期和时间格式化、用户 ID 和资源 ID 格式化，将原始值转换为在用户应用中更易读的版本。阅读更多关于 [value formatting](/docs/foundry/object-link-types/value-formatting/) 的内容。

* **Conditional formatting（条件格式化）：** 在 property 上设置的规则，用于决定该 property 值在面向用户的应用中的呈现方式（例如颜色、对齐方式等）。例如，您可以在 `full name` property 上设置一条规则，当 `start date` property 的值是 2 周以内时，将其值显示为绿色，以在用户应用中标识新员工。阅读更多关于 [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/) 的内容。

* **Type classes（类型类）：** 由用户应用解释的附加元数据。阅读更多关于 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/) 的内容。

* **Render hints（渲染提示）：** 向用户应用提示如何呈现该 property，可能与相同 base type 的大多数 property 不同。许多 render hints 可用于影响定义该 property 的 object type 重新索引的性能。例如，如果您不希望任何用户在用户应用中对 `start date` property 进行搜索或排序，可以取消选中 `searchable` 和 `sortable` render hints，从而提高 `Employee` object type 的重新索引性能。阅读更多关于 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) 的内容。

* **Visibility（可见性）：** 向用户应用提示应如何突出显示该 property。`prominent` property 会使应用优先向用户显示该 property。`hidden` property 不会出现在用户应用中。默认情况下，`start date` property 的 visibility 为 `normal`。

[PARA_4]
[了解更多关于在 Ontology 中创建和配置 properties 的信息，以及关于 property 元数据验证要求的内容。](/docs/foundry/object-link-types/create-object-type/)

[PARA_5]
某些 property base types 的支持有限。这些类型在 property base type 选择器中以 `Limited support` 标签标示。

[PARA_6]
* `byte`：
* 此类型的 properties 不能在 action types 中使用。

* `decimal`：
* 此类型的 properties 不能在 action types 中使用，因为由于 JSON 和 Java 之间的转换，无法保证更新此数据类型时的精度。

* 此类型在 Object Storage V2 中同样不受支持。

* `float`：
* 此类型的 properties 不能在 action types 中使用。

* `short`：
* 此类型的 properties 不能在 action types 中使用。

* `vector`：
* Vectors 只能通过 [KNN](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) 进行查询。

* 最大 vector 维度为 2048。

[PARA_7]
要了解 action types 中 property base types 限制的更多信息，请参阅 [关于受支持 property 类型的文档](/docs/foundry/action-types/scale-property-limits/#supported-property-types)。

[PARA_8]
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

Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. Property values are created and displayed in user applications by adding backing datasources to an object type in the Ontology Manager. To create property values for properties `employee number`, `start date`, and `role` on objects of type `Employee`, an organization will add backing datasources to the `Employee` object type and feed their employee directory and other enterprise data into the Ontology.
## Supported property types
| Property base type                             | Valid as title key? | Valid as primary key? | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------|---------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Commonly used: `String`, `Integer`, `Short`    | Yes                 | Yes                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Time-based: `Date`, `Timestamp`                | Yes                 | Discouraged           | Typically, time values are inappropriate as primary keys, due to potentially unexpected collisions / uniqueness based on the storage format differing from the display format. In most cases, we recommend using `String` instead.                                                                                                                                                                                                                                                                                                                   |
| Number-like: `Boolean`, `Byte`, `Long`         | Yes                 | Discouraged           | `Boolean` limits your object type to two object instances. `Byte` properties can only be assigned in Actions via an `Integer` parameter, so in most cases we recommend using `Integer` properties instead. `Long` has [representational issues in Javascript ↗](https://www.w3schools.com/js/js_numbers.asp#:~\:text=JavaScript%20Numbers%20are%20Always%2064,the%20international%20IEEE%20754%20standard.), so not all frontend libraries and code work well with `Long` values greater than 1e15. In most cases, we recommend using `String` instead. |
| Float-like: `Float`, `Double`, `Decimal`       | Yes                 | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Vector`                                       | No                  | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Array`                                        | Yes                 | No                    | Array properties cannot contain null elements.

If the inner type of the `Array` is not a valid title property, the `Array` property also cannot be used as the title property.

Nested arrays are not supported in Object Storage V2.                                                                                                                                                                                                                                                                                                                                                            |
| `Struct`                                       | No                  | No                    | Struct properties do not support nesting, and fields cannot be arrays. See the [struct documentation](/docs/foundry/object-link-types/structs-overview/#struct-configuration) for detailed information on supported field types.                                                                                                                                                                                                                                                                                                                                                           |
| `Media Reference`, `Time Series`, `Attachment` | No                  | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Geopoint`                                      | Yes                 | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Geoshape`                                     | No                  | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Marking`                                      | No                  | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Cipher`                                       | Yes                 | No                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
要了解更多关于 base types 的信息，请参阅 [base types](/docs/foundry/object-link-types/base-types/)。

[PARA_2]
Property 在 Ontology 中通过以下元数据表示：

[PARA_3]
* **ID（标识符）：** Property 的唯一标识符，主要用于在配置应用时引用该 property。例如，`start-date` 可以是 start date property 的 ID。

* **Display name（显示名称）：** 在用户应用中访问此 property 的值时显示给任何人的名称。例如，`start date` property 的 display name 可以是 `Start date`。

* **Description（描述）：** 关于该 property 的说明性文本，任何人都可以在用户应用中阅读。例如，`start date` property 的描述可以是 `The day the employee began new hire training`。

* **RID：** Foundry 中每个资源自动生成的唯一标识符。Property 的 RID 将在整个平台的错误消息中被引用。

* **Status（状态）：** 向用户和其他 Ontology 构建者发出的信号，表明该 property 在开发过程中的位置。可以是 `active`、`experimental` 或 `deprecated`。默认情况下，`start date` property 的状态为 `experimental`。阅读更多关于 [statuses](/docs/foundry/object-link-types/metadata-statuses/) 的内容。

* **API name（API 名称）：** 在代码中以编程方式引用该 property 时使用的名称。例如，`start date` property 的 API name 可以是 `startDate`。阅读更多关于 [API names](/docs/foundry/functions/api-objects-links/) 的内容。

* **Keys（键）：** 指示该 property 是否为 object type 的 title key 或 primary key。

* **Title key** 是作为该类型 object 显示名称的 property。例如，将 `full name` property 设置为 `Employee` object type 的 title key，将使用该 property 的值（例如假设的员工 "Melissa Chang" 和 "Diego Rodriguez"）作为各个 `Employee` object 的 display name。

* **Primary key** 是作为 object type 每个实例唯一标识符的 property，意味着 backing datasources 中每一行的该 property 值必须不同。例如，可以使用 `employee number` property 的值来将 "Melissa Chang" 标识为组织内的唯一员工。

* **Base type（基础类型）：** 指示该 property 的值类型，并确定在用户应用中可用的操作集。例如，`start date` property 的 base type 为 `date`。用户应用将允许您使用此 property 配置时间线 widget。

* **Value formatting（值格式化）：** 根据 property 的 base type，可应用数值格式化、日期和时间格式化、用户 ID 和资源 ID 格式化，将原始值转换为在用户应用中更易读的版本。阅读更多关于 [value formatting](/docs/foundry/object-link-types/value-formatting/) 的内容。

* **Conditional formatting（条件格式化）：** 在 property 上设置的规则，用于决定该 property 值在面向用户的应用中的呈现方式（例如颜色、对齐方式等）。例如，您可以在 `full name` property 上设置一条规则，当 `start date` property 的值是 2 周以内时，将其值显示为绿色，以在用户应用中标识新员工。阅读更多关于 [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/) 的内容。

* **Type classes（类型类）：** 由用户应用解释的附加元数据。阅读更多关于 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/) 的内容。

* **Render hints（渲染提示）：** 向用户应用提示如何呈现该 property，可能与相同 base type 的大多数 property 不同。许多 render hints 可用于影响定义该 property 的 object type 重新索引的性能。例如，如果您不希望任何用户在用户应用中对 `start date` property 进行搜索或排序，可以取消选中 `searchable` 和 `sortable` render hints，从而提高 `Employee` object type 的重新索引性能。阅读更多关于 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) 的内容。

* **Visibility（可见性）：** 向用户应用提示应如何突出显示该 property。`prominent` property 会使应用优先向用户显示该 property。`hidden` property 不会出现在用户应用中。默认情况下，`start date` property 的 visibility 为 `normal`。

[PARA_4]
[了解更多关于在 Ontology 中创建和配置 properties 的信息，以及关于 property 元数据验证要求的内容。](/docs/foundry/object-link-types/create-object-type/)

[PARA_5]
某些 property base types 的支持有限。这些类型在 property base type 选择器中以 `Limited support` 标签标示。

[PARA_6]
* `byte`：
* 此类型的 properties 不能在 action types 中使用。

* `decimal`：
* 此类型的 properties 不能在 action types 中使用，因为由于 JSON 和 Java 之间的转换，无法保证更新此数据类型时的精度。

* 此类型在 Object Storage V2 中同样不受支持。

* `float`：
* 此类型的 properties 不能在 action types 中使用。

* `short`：
* 此类型的 properties 不能在 action types 中使用。

* `vector`：
* Vectors 只能通过 [KNN](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) 进行查询。

* 最大 vector 维度为 2048。

[PARA_7]
要了解 action types 中 property base types 限制的更多信息，请参阅 [关于受支持 property 类型的文档](/docs/foundry/action-types/scale-property-limits/#supported-property-types)。

[PARA_8]
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

To learn more about base types, see [base types](/docs/foundry/object-link-types/base-types/).