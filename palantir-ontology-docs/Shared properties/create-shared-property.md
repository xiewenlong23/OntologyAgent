<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/create-shared-property/
---
# Create a shared property
从 Ontology Manager 应用程序中的共享属性页面创建并配置一个新的共享属性。

Create and configure a new shared property from the shared property page in the Ontology Manager application.
要访问此页面，请按照以下步骤操作：

To access the page, follow the steps below:
1. 在 Ontology Manager 中选择 **Shared properties** 菜单选项。

1. Select the **Shared properties** menu option in Ontology Manager.

> 📷 **[图片: Ontology Manager 中的共享属性页面]**

> 📷 **[图片: Shared properties page in Ontology Manager]**

2. 进入共享属性页面后，在右上角选择 **New shared property**。

2. Once on the shared property page, select **New shared property** at the top right.

> 📷 **[图片: 创建共享属性按钮]**

> 📷 **[图片: Create shared property button]**

3. 这将打开共享属性创建模态框，您可以在其中配置名称、描述、类型和其他元数据以创建共享属性。

3. This will open the shared property creation modal, where you can configure the name, description, type, and other metadata to create the shared property.

> 📷 **[图片: 创建共享属性模态框]**

> 📷 **[图片: Create shared property modal]**

共享属性可以使用常规属性元数据的子集进行配置：

A shared property can be configured with a subset of regular property metadata:
* **Name:** 共享 property 的名称。

* **Description:** 关于共享 property 的说明文字。例如，`start date` 共享 property 的描述可以是 `The day the employee or contractor began working`。

* **Base type:** 指示此 property 的值类型，并决定用户应用程序中可用的操作集。例如，`start date` property 的 base type 将为 `date`。用户应用程序将允许您使用此 property 配置 timeline widget。Base types 与底层 column type 相关，并且必须与 column type 匹配才能应用于 object type。

* **Value formatting:** 根据 property 的 base type，可以使用数值格式化、日期和时间格式化、user ID 以及 resource ID 格式化应用于该 property，在用户应用程序中将其原始值转换为更易读的版本。了解更多关于 [value formatting](/docs/foundry/object-link-types/value-formatting/) 的信息。

* **Type classes:** 由用户应用程序解释的附加 metadata。了解更多关于 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/) 的信息。

* **Render hints:** 向用户应用程序提供的关于如何渲染该 property 的指示，可能与同一 base type 的大多数 property 不同。许多 render hints 可用于影响定义该 property 的 object type 重新索引的性能。例如，如果您不希望任何用户在用户应用程序中对 `start date` property 进行搜索或排序，您可以取消选中 `searchable` 和 `sortable` render hints，从而提升 `Employee` object type 的重新索引性能。了解更多关于 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) 的信息。

* **Visibility:** 向用户应用程序指示该 property 的显示突出程度。`prominent` property 将使应用程序优先向用户显示此 property。`hidden` property 将不会出现在用户应用程序中。默认情况下，`start date` property 将具有 `normal` visibility。

* **Name:** The name for the shared property.
* **Description:** Explanatory text about the shared property. For example, the description of the `start date` shared property may be `The day the employee or contractor began working`.
* **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property. Base types are related to the underlying column type and must match the column type in order to be applied on an object type
* **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID, and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Learn more about [value formatting](/docs/foundry/object-link-types/value-formatting/).
* **Type classes:** Additional metadata that are interpreted by user applications. Learn more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
* **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type on which the property is defined. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Learn more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).
* **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have `normal` visibility.
4. 要将共享 property 持久化到 Ontology，请在 Ontology Manager 右上角选择 **Save**。

4. To persist the shared property to the Ontology, select **Save** in the upper right of the Ontology Manager.