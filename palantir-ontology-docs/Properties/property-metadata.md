<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/property-metadata/
---
# Metadata reference
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

A property is represented in the Ontology by the following metadata:
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

* **ID:** A unique identifier of the property, primarily used to reference the property when configuring an application. For example, `start-date` may be the ID of the start date property.
* **Display name:** The name shown to anyone accessing property values for this property in user applications. For example, the display name for the `start date` property may be `Start date`.
* **Description:** Explanatory text about the property that anyone can read in user applications. For example, the description of the `start date` property may be `The day the employee began new hire training`.
* **RID:** An automatically generated unique identifier for every resource in Foundry. A property’s RID will be referenced in error messages across the platform.
* **Status:** A signal to users and other Ontology builders about where in the development process the property stands. It can be `active`, `experimental`, or `deprecated`. By default, the `start date` property will have status `experimental`. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* **API name:** The name used when referring to the property programmatically in code. For example, the API name of the `start date` property may be `startDate`. Read more about [API names](/docs/foundry/functions/api-objects-links/).
* **Keys:** An indication of whether the property is the object type’s title key or primary key.
* The **title key** is the property that acts as a display name for objects of this type. For example, setting the `full name` property as the title key of the `Employee` object type will use the values of that property, such as the notional employees “Melissa Chang” and “Diego Rodriguez” as the display names for each respective `Employee` object.
* The **primary key** is the property that acts as a unique identifier for each instance of an object type, meaning that each row in the backing datasources must have a different value for this property. For example, the value of the `employee number` property may be used to identify “Melissa Chang” as a unique employee within the organization.
* **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.
* **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Read more about [value formatting](/docs/foundry/object-link-types/value-formatting/).
* **Conditional formatting:** Rules set on a property that dictate how that property value will render (e.g coloring, alignment, etc.) in user facing applications. For example, you may set a rule on the `full name` property that colors its values green if the value of the `start date` property was less than 2 weeks ago, in order to indicate a new hire in user applications. Read more about [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/).
* **Type classes:** Additional metadata that are interpreted by user applications. Read more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
* **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type the property is defined on. For example, if you don’t expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Read more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).
* **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have visibility `normal`.
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

[Learn more about creating and configuring properties in the Ontology and about validation requirements for property metadata.](/docs/foundry/object-link-types/create-object-type/)
## Property base types with limited support
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

Some property base types have limited support. These types are indicated with the `Limited support` tag which is visible in the property base type picker.
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

* `byte`:
* Properties of this type cannot be used within action types.
* `decimal`:
* Properties of this type cannot be used within action types as the precision cannot be guaranteed when updating this data type due to the conversion between JSON and Java.
* This type is also not supported in Object Storage V2.
* `float`:
* Properties of this type cannot be used within action types.
* `short`:
* Properties of this type cannot be used within action types.
* `vector`:
* Vectors can only be queried by [KNN](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn).
* The max vector dimension is 2048.
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

For more information on the limitations of property base types in action types, see [the documentation on supported property types](/docs/foundry/action-types/scale-property-limits/#supported-property-types).