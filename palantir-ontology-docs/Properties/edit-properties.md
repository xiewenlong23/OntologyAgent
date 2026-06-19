<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/edit-properties/
---
# Edit object type properties
### Delete a property
在 property 编辑器中，在 properties 面板内，将鼠标悬停在您要删除的 property 上，然后选择 **Delete property**。

From within the property editor, in the properties pane, hover over the property you want to delete and select **Delete property**.
* 请注意，property 的删除仅在您保存更改后生效，并且会中断引用该 property 的任何视图或应用程序。

* 状态为 `active` 的 property **不能** 被删除。

* 详细了解 [状态](/docs/foundry/object-link-types/metadata-statuses/)。

* Note that the deletion of the property only takes effect after you save your changes, and will break any views or applications referencing the property.
* Properties with an `active` status **cannot** be deleted.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
### Change the column backing a property
在 property 编辑器中，在 properties 面板内，将鼠标悬停在您要取消映射的 property 上，然后选择 **Unlink property**。要将 property 链接到新列，请将鼠标悬停在该 property 上并选择 **Map to a column**。

From within the property editor, in the properties pane, hover over the property you want to unmap and select **Unlink property**. To link the property to a new column, hover over the property and select **Map to a column**.
![Mapping to a column](/docs/resources/foundry/object-link-types/edit-object-type-map-to-column.png)
### Edit a property type’s metadata
您可以通过选择 property type 来编辑其元数据，如下图所示。

You can edit metadata for a property type by selecting the property type, as shown in the image below.

> 📷 **[图片: Edit property metadata]**

> 📷 **[图片: Edit property metadata]**

用于编辑 property metadata 的可用选项被归类为四个不同的标签页，这些标签页提供对以下配置的访问：

The available options for editing property metadata are clustered into four different tabs which give access to the following configurations:
1. **Display name and description：** 选择进入现有的 display name 或 description 以编辑文本。

2. **Status：** 选择现有 status 以打开可用状态的下拉列表。从 `deprecated`、`experimental` 和 `active` 状态中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

3. **API name：** 选择进入现有 API name 以更改其值。

* 请注意，对于状态为 `active` 的 properties，您**无法**更改其 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#api-name)。

4. **Keys：** 指示 property 是否为 object type 的 title key 或 primary key。

* 请注意，对于状态为 `active` 的 object type，您**无法**更改其 primary key。

* 详细了解 [keys](/docs/foundry/object-link-types/create-object-type/#configure-the-primary-key-and-title-key) 和 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

5. **Value formatting：** 对 property 的值应用特殊格式化程序，以使其在 applications 中更易读。

* 详细了解 [value formatters](/docs/foundry/object-link-types/value-formatting/)。

6. **Conditional formatting：** 对 property 应用规则，以规定其在 applications 中的呈现方式。

* 详细了解 [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/)。

7. **Property base type：** 从下拉列表中选择 property 的 base type。property 的 type 限制了可对其值执行的可能操作集。

* 例如，base type 为 `timestamp` 的 property 可以在 Object Explorer 的 timeline widget 中显示。

* 如果 property 的 type 与其 backing column 的 type 不兼容，您将收到错误提示。

1. **Display name and description:** Select into the existing display name or description to edit the text.
2. **Status:** Select the existing status to open a dropdown of available statuses. Choose from the `deprecated`, `experimental`, and `active` statuses.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
3. **API name:** Select into the existing API name to change its value.
* Note that you **cannot** change the API name for properties with an `active` status.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* Read more about [valid API names](/docs/foundry/object-link-types/create-object-type/#api-name).
4. **Keys:** Indicate whether a property is the object type’s title key or primary key.
* Note that you **cannot** change the primary key of an object type with an `active` status.
* Read more about [keys](/docs/foundry/object-link-types/create-object-type/#configure-the-primary-key-and-title-key) and about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
5. **Value formatting:** Apply a special formatter to the values of a property to make them more readable in applications.
* Read more about [value formatters](/docs/foundry/object-link-types/value-formatting/).
6. **Conditional formatting:** Apply rules to a property that dictate how it will be rendered in applications.
* Read more about [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/).
7. **Property base type:** Select the property’s base type from the dropdown. The type of the property constrains the possible set of operations that can be done on the property’s values.
* For example, a property with base type `timestamp` can be shown in a timeline widget in Object Explorer.
* You will receive an error if the type of a property is not compatible with the type of its backing column.
> **⚠️ 警告**

> 如果您对 object property types 进行了更改，则还必须更新与该 object 上 property 交互的 Actions 所期望的 type。为此，请在 Ontology Manager 中打开该 Action 并编辑期望的 type。
> **⚠️ 警告**

> If you make a change to object property types, you must also update the type expected by Actions that interact with property on that object. To do this, open the Action in Ontology Manager and edit the expected type.
8. **Type classes：** 应用 type classes 作为可由 applications 解释的附加元数据。

* 有关可用 type classes 的列表，请参阅 [type classes documentation](/docs/foundry/object-link-types/metadata-typeclasses/)。

9. **Render hints：** 从提供的清单中选择要应用于 property 的 render hints，以改善 property value 的呈现方式以及将其索引到 Object Storage V1 (Phonograph) 中的方式。

* 有关可用 render hints 的描述，请参阅 [render hints documentation](/docs/foundry/object-link-types/metadata-render-hints/)。

10. **Visibility：** 选择现有 visibility 以打开可用可见性的下拉列表。`prominent` property 将使 applications 优先向用户显示该 property。`hidden` property 将不会出现在用户 applications 中。

8. **Type classes:** Apply type classes as additional metadata that can be interpreted by applications.
* See the [type classes documentation](/docs/foundry/object-link-types/metadata-typeclasses/) for a list of available type classes.
9. **Render hints:** Select render hints from the supplied checklist that you want applied to a property in order to improve how a property value is rendered and indexed into Object Storage V1 (Phonograph).
* See the [render hints documentation](/docs/foundry/object-link-types/metadata-render-hints/) for descriptions of the available render hints.
10. **Visibility:** Select the existing visibility to open a dropdown of available visibilities. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications.
更改 property metadata 后，启动受影响 object 的重新索引以更新 Ontology。

After making a change to property metadata, initiate a re-index of the affected object to update the Ontology.
### Bulk edit multiple properties
您可以在 property editor 中通过按住 **Cmd/Ctrl** 键并选择 properties 来同时选择多个 properties。一旦选择了多个 properties，以下批量编辑操作将变为可用：

You can select multiple properties in the property editor by holding the **Cmd/Ctrl** key while selecting properties. Once multiple properties are selected, the following bulk editing actions become available:
* 更改 base type。

* 添加/移除 type classes。

* 更改 render hints。

* 更改 visibility。

* 添加/移除 value formatting。

* Changing base type.
* Adding/removing of type classes.
* Changing render hints.
* Changing visibility.
* Adding/removing value formatting.
![Edit property metadata](/docs/resources/foundry/object-link-types/edit-object-type-bulk-edit-multiple-properties.png)
您也可以从 property editor 外部批量编辑上述某些字段，方法是从 object type 视图的侧边栏中选择 **Properties** 页面。只需选择要编辑的 properties 旁边的复选框，表格顶部将出现一个新行，其中包含用于批量编辑的选项。

You can also bulk edit some of the above fields from outside of the property editor, by selecting the **Properties** page from the sidebar of an object type view. Simply select the checkboxes next to the properties you want to edit and a new row will appear at the top of the table with options for bulk editing.