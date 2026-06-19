<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/shared-property-metadata/
---
# Metadata reference
共享 property 在 Ontology 中由以下 metadata 表示：

A shared property is represented in the Ontology by the following metadata:
* **Name（名称）：** 共享属性的名称。

* **Description（描述）：** 任何人都可以在用户应用程序中阅读的有关共享属性的说明性文本。例如，`start date` 共享属性的描述可以是 `The day the employee began new hire training`。

* **RID：** Foundry 中每个资源自动生成的唯一标识符。属性的 RID 将在整个平台的错误消息中被引用。

* **Base type（基础类型）：** 指示此属性值的类型，并确定用户应用程序中可用的操作集合。例如，`start date` 属性的基础类型将为 `date`。用户应用程序将允许您使用此属性配置 timeline widget。

* **Value formatting（值格式化）：** 根据属性的基础类型，可以使用数值格式化、日期和时间格式化、用户 ID 以及 resource ID 格式化来应用于属性，在用户应用程序中将其原始值转换为更易读的版本。了解更多关于 [value formatting](/docs/foundry/object-link-types/value-formatting/) 的信息。

* **Type classes（类型类）：** 由用户应用程序解释的附加元数据。了解更多关于 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/) 的信息。

* **Render hints（渲染提示）：** 向用户应用程序提示如何渲染此属性的指示，可能与同一基础类型的大多数属性不同。许多 render hints 可用于影响定义该属性的 object type 重新索引的性能。例如，如果您不希望任何用户在用户应用程序中对 `start date` 属性进行搜索或排序，您可以取消选中 `searchable` 和 `sortable` render hints，从而提高 `Employee` object type 的重新索引性能。了解更多关于 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) 的信息。

* **Visibility（可见性）：** 向用户应用程序提示如何突出显示属性的指示。`prominent` 属性将使应用程序优先向用户显示此属性。`hidden` 属性将不会出现在用户应用程序中。默认情况下，`start date` 属性将具有 `normal` 可见性。

* **Usage（使用情况）：** 使用此共享属性的 object types。例如，`start date` 属性可以由 Ontology 中的 `Employee`、`Contractor` 和其他 object types 使用。

* **Name:** The name for the shared property.
* **Description:** Explanatory text about the shared property that anyone can read in user applications. For example, the description of the `start date` shared property may be `The day the employee began new hire training`.
* **RID:** An automatically generated unique identifier for every resource in Foundry. A property’s RID will be referenced in error messages across the platform.
* **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.
* **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID, and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Learn more about [value formatting](/docs/foundry/object-link-types/value-formatting/).
* **Type classes:** Additional metadata that are interpreted by user applications. Learn more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
* **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type on which the property is defined. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Learn more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).
* **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have `normal` visibility.
* **Usage:** The obect types on which a shared property is used. For example, the `start date` property can be in use by the `Employee`, `Contractor`, and other object types within the Ontology.