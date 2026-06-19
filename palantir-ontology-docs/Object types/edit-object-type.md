<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/edit-object-type/
---
# Edit object types
> **⚠️ 警告: Warning**

> 编辑 object type 及其 properties 可能会产生 **破坏应用程序的后果，从而中断用户工作流**。在对任何 object type 或 property 进行编辑之前，请阅读下面关于 [potential breaking changes](#potential-breaking-changes) 的部分。
> **⚠️ 警告: Warning**

> Editing an object type and its properties can have **application-breaking consequences that can disrupt user workflows**. Read the section below on [potential breaking changes](#potential-breaking-changes) **before** proceeding with any object type or property edits.
## Potential breaking changes
### Object type without writeback
需要 Object Storage V1 (Phonograph) 注销并重新注册 object type 的 backing datasources 的更改，将导致该类型的 objects 在重新索引期间在用户应用程序中**不可用**；这些更改如下所述。

Changes that require Object Storage V1 (Phonograph) to unregister and reregister the backing datasources of an object type will make the objects of that type **unavailable** in user applications during that reindex time; these changes are described below.
保存时，以下更改将注销并重新注册（或删除）object type 的 backing datasources：

The following changes will unregister and reregister (or delete) the backing datasources of an object type when saved:
* 更改 object type 的 backing datasource。

* 更改 object type 的 primary key。

* 删除 object type。

* Changing an object type’s backing datasource.
* Changing the primary key of an object type.
* Deleting an object type.
当您尝试保存这些更改时，系统将警告您对用户应用程序的潜在影响。

When you try to save any of these changes, you will be warned about the potential impact on user applications.

> 📷 **[图片: Warning: Reindexing will make objects unavailable]**

> 📷 **[图片: Warning: Reindexing will make objects unavailable]**

例如，如果一个 object type 在 Workshop 应用程序中使用，则该 Workshop 应用程序将在重新索引完成之前无法使用。您可以在其 **Datasources** 页面的 **Phonograph** 窗格中跟踪该 object type 的重新索引进度。

For example, if an object type is used in a Workshop application, that Workshop application will be broken until the reindex completes. You can track the progress of the reindex for an object type in the **Phonograph** pane of its **Datasources** page.

> 📷 **[图片: Tracking reindex in Phonograph]**

> 📷 **[图片: Tracking reindex in Phonograph]**

[了解更多关于 Object Storage V1 (Phonograph) 的信息。](/docs/foundry/object-databases/object-storage-v1/)

[Learn more about Object Storage V1 (Phonograph).](/docs/foundry/object-databases/object-storage-v1/)
### Object type with writeback
如果一个 object type 启用了 writeback,在对该 object type 进行编辑时需要格外小心。对 object type 所做的编辑历史会存储在 Object Storage V1 (Phonograph) 中。每次构建 writeback dataset 时,都会重新应用编辑历史,以获得 writeback dataset 中被编辑 object 的最终状态。当一个 object type 的 backing datasources 从 Object Storage V1 (Phonograph) 注销时,Object Storage V1 (Phonograph) 中的编辑历史将被删除,未来 writeback dataset 的构建将会失败。

If an object type has writeback enabled, extra precaution should be taken when making edits to that object type. The history of edits made to an object type are stored in Object Storage V1 (Phonograph). Every time a writeback dataset is built, the history of edits is reapplied to get the final state of edited objects in the writeback dataset. When the backing datasources of an object type are unregistered from Object Storage V1 (Phonograph), the history of edits in Object Storage V1 (Phonograph) is deleted and future builds of the writeback dataset will fail.
除了[上一节](#object-type-without-writeback)中列出的需要注销的更改外,对于具有 writeback 的 object type,当对**曾经**收到过编辑的 object type 的**任何** property 进行 schema 更改时,也需要注销,即使该 property 当前没有收到编辑。Schema 更改包括对 property 的 ID 和 base type 的更改。

In addition to the changes that require unregistering that were listed in the [previous section](#object-type-without-writeback), unregistering is required for object types with writeback when schema changes are made to **any** property of an object type that has **ever** received edits, even if it does not currently receive edits. Schema changes include changes to the ID and base type of a property.
以下更改***不需要***注销,因此不会面临丢失编辑历史的风险:

The following changes ***do not*** require unregistering and therefore do not risk losing the edit history:
* 更改已收到编辑的 property 的 display name、title key、render hints、type classes 和 visibility 将***不***需要 object type 注销。

* 删除 fields 或对从未收到编辑的 fields 进行 schema 更改将***不***需要 object type 注销,因此不会擦除或撤消对其他正在接收编辑的 fields 的编辑。

* Changing the display name, title key, render hints, type classes, and visibility of a property that has received edits will ***not*** require the object type to unregister.
* Deleting fields or making schema changes to fields that have never received edits will ***not*** require the object type to unregister, and therefore will not erase or undo edits on other fields that are receiving edits.
> **⚠️ 警告: Warning**

> Object Storage V1 (Phonograph) **不会**自动注销 object type 的 backing datasources 来响应这些 schema 更改。相反,reindex 将会失败,并且只有在撤销已保存的 schema 更改、或者您在 object type **Datasource** 页面中的 **Phonograph** 面板中手动注销并重新注册 object type 的 backing datasources 时才会成功。
> **⚠️ 警告: Warning**

> Object Storage V1 (Phonograph) will **not** automatically unregister the backing datasources of an object type in response to one of these schema changes. Instead, the reindex will fail and will only succeed if the saved schema changes are undone, or if you manually unregister and reregister the backing datasources of the object type in the **Phonograph** pane of the object type’s **Datasource** page.
property 编辑器中的 properties 面板会突出显示一个 field 是否曾经收到过编辑。

The properties pane in the property editor highlights whether a field has ever received edits.

> 📷 **[图片: Properties pane]**

> 📷 **[图片: Properties pane]**

此外,当您尝试保存任何可能擦除编辑历史的更改时,您将收到关于对编辑潜在影响的警告。

Furthermore, when you try to save any changes that risk erasing the edit history, you will be warned about the potential impact on edits.

> 📷 **[图片: Warning about impact on edits]**

> 📷 **[图片: Warning about impact on edits]**

现在您已经了解了编辑现有 object types 和 properties 时的注意事项,您可以安全地进行更改了。

Now that you understand the considerations in editing existing object types and properties, you can safely make your changes.
## Edit an existing object type
* [导航到现有的 object type](#navigate-to-an-existing-object-type)

* [删除 object type](#delete-an-object-type)

* [更改 backing datasource](#change-a-backing-datasource)

* [编辑 object type 的 metadata](#edit-an-object-types-metadata)

* [Navigate to an existing object type](#navigate-to-an-existing-object-type)
* [Delete an object type](#delete-an-object-type)
* [Change a backing datasource](#change-a-backing-datasource)
* [Edit an object type’s metadata](#edit-an-object-types-metadata)
### Navigate to an existing object type
您可以随时通过从主页侧边栏选择 object type 页面并从列表中选择不同的 object type 来更改您正在使用的 object type。您也可以随时在应用程序顶部的搜索栏中搜索新的 object type。[了解更多关于导航的信息。](/docs/foundry/ontology-manager/navigation/)

You can always change the object type you are working on by selecting the object type page from the home page sidebar and selecting a different object type from the list. You can also always search for a new object type in the search bar in the application header. [Read more about navigation.](/docs/foundry/ontology-manager/navigation/)
### Delete an object type
您可以通过选择 object type 视图侧边栏右上角的 ![...](/docs/resources/foundry/object-link-types/three-dots.png) (三个点) 图标(见下图),然后从下拉菜单中选择 **Delete** 选项来删除 object type。将弹出一个对话框,确认您要将该 object type 及其所有关联的 link types 标记为删除。

You can delete an object type by selecting the ![...](/docs/resources/foundry/object-link-types/three-dots.png) (three dots) icon at the top right of the object type view sidebar (see image below) and then selecting the **Delete** option from the dropdown. A dialog will pop up to confirm you want to stage the object type and all of its associated link types for deletion.
* 请注意,object type 的删除只有在您保存更改后才会生效,并且会破坏引用该 object type 的任何 view 或 application。

* 状态为 `active` 的 object types 无法被删除。[了解更多关于 status 的信息。](/docs/foundry/object-link-types/metadata-statuses/)

* Note that the deletion of the object type only takes effect after you save your changes, and will break any views or applications referencing the object type.
* Object types with an `active` status cannot be deleted. [Read more about statuses.](/docs/foundry/object-link-types/metadata-statuses/)

> 📷 **[图片: 删除 Object Type]**

> 📷 **[图片: Delete object type]**

### Change a backing datasource
您可以通过以下步骤更改 backing datasource：

You can change a backing datasource with the following steps:
1. 通过在 object type 的 **Properties** 页面顶部选择 **Edit property mapping**，导航至 property editor。

2. 在 **Datasources** 窗格顶部选择 ![pen](/docs/resources/foundry/object-link-types/pen.png) **Replace** 按钮。这将允许您在 Foundry 中浏览并选择可用的 datasource。

1. Navigate to the property editor by selecting **Edit property mapping** at the top of the **Properties** page of an object type.
2. Select the ![pen](/docs/resources/foundry/object-link-types/pen.png) **Replace** button at the top of the **Datasources** pane. This will allow you to browse and select available datasources in Foundry.
> **⚠️ 警告: Warning**

> 更改 object type 的 backing datasource 将移除旧 datasource 中列与该 object type 的 property 之间的所有连接。**仅当**您更改为与旧 datasource **具有相同 schema** 的新 datasource 时，property 才会自动重新映射。否则，您需要将 object type 的 property 重新映射到新 datasource。
> **⚠️ 警告: Warning**

> Changing the backing datasource of an object type will remove any connection between columns in the old datasource and the object type’s properties. Properties will be automatically remapped for you **only if** you change to a new datasource with the **same schema** as the old datasource. Otherwise, you will need to remap the object type’s properties to the new datasource.
![Backing datasource](/docs/resources/foundry/object-link-types/edit-object-type-backing-datasource.png)
### Edit an object type’s metadata
![Edit object type metadata](/docs/resources/foundry/object-link-types/edit-object-type-metadata-annotated.png)
1. **Icon:** 选择默认 icon 以自定义 object type 的 icon 和颜色，当用户在用户应用程序中查看此类型的 object 时将显示该样式。

2. **Display names and description:** 选择现有的 display names 或 description 进行编辑。

3. **Status:** 选择现有 status 以打开可用状态的下拉列表。可从 `deprecated`、`experimental` 和 `active` 状态中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

4. **Visibility:** 选择现有 visibility 以打开可用可见性的下拉列表。`prominent` object type 将使应用程序优先向用户显示此 object type。`hidden` object type 将不会出现在用户应用程序中。

5. **API name:** 选择现有 API name 以更改其值。

* 请注意，对于状态为 `active` 的 object type，无法更改其 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#api-name)。

1. **Icon:** Select the default icon to customize the icon and color of the object type that will appear in user applications when a user views an object of this type.
2. **Display names and description:** Select into the existing display names or description to edit the text.
3. **Status:** Select the existing status to open a dropdown of available statuses. Choose from the `deprecated`, `experimental`, and `active` statuses.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
4. **Visibility:** Select the existing visibility to open a dropdown of available visibilities. A `prominent` object type will lead applications to show this object type first to users. A `hidden` object type will not appear in user applications.
5. **API name:** Select into the existing API name to change its value.
* Note that you cannot change the API name for object types with an `active` status.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* Read more about [valid API names](/docs/foundry/object-link-types/create-object-type/#api-name).
> **ℹ️ 注意**

> object type 的 object ID 在初始 object type 创建过程之后无法编辑。
> **ℹ️ 注意**

> The object ID of an object type cannot be edited after the initial object type creation process.
## Troubleshooting
#### Error: `Phonograph2:FoundryColumnNameNotFound`
如果您收到错误 `Phonograph2:FoundryColumnNameNotFound`，则表示支撑您尝试保存的 object type 的 datasource 中有一个列已被移除，并且存在一个未映射的 property。该 property 需要被映射或删除。

If you receive the error `Phonograph2:FoundryColumnNameNotFound`, a column has been removed from the datasource backing the object type you are trying to save and a property is left unmapped. The property needs to either be mapped or deleted.
#### Error: `Phonograph2:InvalidColumnRemoval`
如果您收到错误 `Phonograph2:InvalidColumnRemoval`，则表示已移除一个支撑已接收编辑的 property 的列。需要将该列重新添加回 datasource，或者将该 object type 取消注册后重新注册。

If you receive the error `Phonograph2:InvalidColumnRemoval`, a column has been removed that was backing a property that has received edits. Either the column needs to be added back to the datasource, or the object type needs to be unregistered and reregistered.
请参阅上文关于 [potential breaking changes](#potential-breaking-changes) 的部分以了解更多信息。

See the section above on [potential breaking changes](#potential-breaking-changes) to learn more.
#### Error: `Phonograph2:InvalidColumnFieldSchemaChange`
如果您收到错误 `Phonograph2:InvalidColumnFieldSchemaChange`，则表示一个已接收编辑的 property 的 ID 或 key 已被更改。需要还原该更改，或者将该 object type 取消注册后重新注册。

If you receive the error `Phonograph2:InvalidColumnFieldSchemaChange`, a property that has received edits has had its ID or key changed. Either the change needs to be reverted, or the object type needs to be unregistered and reregistered.
请参阅上文关于 [potential breaking changes](#potential-breaking-changes) 的部分以了解更多信息。

See the section above on [potential breaking changes](#potential-breaking-changes) to learn more.
#### Error: `OntologyMetadata:IncompatibleFoundryFieldSchemaForPropertyType`
如果您收到错误 `OntologyMetadata:IncompatibleFoundryFieldSchemaForPropertyType`，则表示您正在尝试使用与其所支撑的列类型不兼容的 base type 保存 property。例如，列 X 的类型可能已更改为 "string"，但被映射到 base type 为 "integer" 的 property X。

If you receive the error `OntologyMetadata:IncompatibleFoundryFieldSchemaForPropertyType`, you are trying to save a property with a base type that is incompatible with the column type that is backing it. For example, the type of column X may been changed to “string”, but is mapped to property X of base type “integer”.
#### Error: `Phonograph2:SchemaMismatch`
如果您收到错误 `Phonograph2:SchemaMismatch`，则您可能对支撑该 object 的 schema 进行了有意更改，但尚未在 Ontology Manager 中更新该 object 的 property type。通过编辑 property 的数据类型以接受新类型来修改 Ontology。发布更改并重新构建 dataset，然后启动对该 object 的重新索引。

If you receive the error `Phonograph2:SchemaMismatch`, you likely made an intentional change to the schema that backs the object but have have not yet updated the object's property types in Ontology Manager. Modify the Ontology by editing the property's data type to accept the new type. Publish the changes and rebuild the dataset, then initiate a re-index of the object.
#### Error: `FieldTypeIncompatibleWithOntologyPropertyType`
如果您收到错误 `FieldTypeIncompatibleWithOntologyPropertyType` 或收到消息 "Failed to Update Object Type in Phonograph"，则表示支撑您 object 的 dataset 中的数据类型与 ontology 期望的数据类型之间存在不匹配。您必须确保在 dataset 和 ontology 中都反映任何 schema 更新。

If you receive the error `FieldTypeIncompatibleWithOntologyPropertyType` or receive the message "Failed to Update Object Type in Phonograph", there is a mismatch between the data types in the dataset that backs your object and the data types that the ontology expects. You must ensure that any schema updates are reflected in both the dataset and the ontology.
如果您确实对 ontology 或 dataset 进行了任何有意更改，请与 object 及其 backing 数据源的所有者沟通，以了解最近的更改。

If you did make any intentional changes to the ontology or the dataset, communicate with the owner of the object and its backing data source to understand recent changes.