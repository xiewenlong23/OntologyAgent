<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/edit-shared-property/
---
# Edit shared properties
### Edit shared property metadata
您可以通过首先从 Ontology Manager 的 **Shared property** 页面中选择要编辑的共享 property 来编辑其 metadata。

You can edit metadata for a shared property by first selecting the shared property to edit from the **Shared property** page of the Ontology Manager.

> 📷 **[图片: Edit shared property metadata]**

> 📷 **[图片: Edit shared property metadata]**

用于编辑共享 property metadata 的可用选项被归类为四个不同的选项卡：**General**、**Display**、**Interaction** 和 **Details**。这些选项卡包含以下配置：

The available options for editing shared property metadata are clustered into four different tabs: **General**, **Display**, **Interaction**, and **Details**. These tabs contain the following configurations:
* **Name:** 共享 property 的名称。

* **Description:** 关于共享 property 的说明文字。例如，`start date` 共享 property 的描述可以是 `The day the employee or contractor began working`。

* **Base type:** 指示此 property 的值类型，并决定用户应用程序中可用的操作集。例如，`start date` property 的 base type 将为 `date`。用户应用程序将允许您使用此 property 配置 timeline widget。

* **Value formatting:** 根据 property 的 base type，可以使用数值格式化、日期和时间格式化、user ID 以及 resource ID 格式化应用于该 property，在用户应用程序中将其原始值转换为更易读的版本。了解更多关于 [value formatting](/docs/foundry/object-link-types/value-formatting/) 的信息。

* **Type classes:** 由用户应用程序解释的附加 metadata。了解更多关于 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/) 的信息。

* **Render hints:** 向用户应用程序提供的关于如何渲染该 property 的指示，可能与同一 base type 的大多数 property 不同。许多 render hints 可用于影响定义该 property 的 object type 重新索引的性能。例如，如果您不希望任何用户在用户应用程序中对 `start date` property 进行搜索或排序，您可以取消选中 `searchable` 和 `sortable` render hints，从而提升 `Employee` object type 的重新索引性能。了解更多关于 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) 的信息。

* **Visibility:** 向用户应用程序指示该 property 的显示突出程度。`prominent` property 将使应用程序优先向用户显示此 property。`hidden` property 将不会出现在用户应用程序中。默认情况下，`start date` property 将具有 `normal` visibility。

* **Name:** The name for the shared property.
* **Description:** Explanatory text about the shared property. For example, the description of the `start date` shared property may be `The day the employee or contractor began working`.
* **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.
* **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID, and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Learn more about [value formatting](/docs/foundry/object-link-types/value-formatting/).
* **Type classes:** Additional metadata that are interpreted by user applications. Learn more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
* **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type on which the property is defined. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Learn more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).
* **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have `normal` visibility.
此外，您可以在 **Usage** 选项卡上查看使用此共享 property 的 object types，并在 **Permissions** 选项卡上更新共享 property 的权限。

Additionally, you can view the object types that use this shared property on the **Usage** tab and update the permissions on the shared property on the **Permissions** tab.
### Delete a shared property
要删除共享 property，请完成以下步骤：

To delete a shared property, complete the following steps:
1. 导航至 Ontology Manager 的 **Shared property** 页面。

2. 选择一个或多个要删除的共享 property，然后选择 **Delete property**。

1. Navigate to the **Shared property** page of the Ontology Manager.
2. Select one or more shared properties for deletion, then select **Delete property**.

> 📷 **[图片: Delete shared property]**

> 📷 **[图片: Delete shared property]**

3. 在弹窗中确认删除操作。

3. Confirm the delete action in the modal.

> 📷 **[图片: Confirm shared property deletion]**

> 📷 **[图片: Confirm shared property deletion]**

4. 在右上角选择 **Save**。

4. Select **Save** in the upper right.
> **⚠️ 警告**

> 当共享 property 被删除后，所有使用此共享 property 的 object types 将恢复为常规 property。
> **⚠️ 警告**

> When a shared property is deleted, all object types using this shared property will revert to regular properties.