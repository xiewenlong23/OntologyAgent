<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/edit-interface-definition/
---
# Edit an interface definition
> **⚠️ 警告: Breaking**

> 由于 Interfaces 会暴露 API 名称，对 Interface 定义的任何更改都有可能破坏下游应用程序，并且必然会破坏现有的 object implementations。当向 Interface 添加新的必填 property 或 link type 约束时，使用该 Interface 的所有 Object Type 的 implementations **必须**在与 Ontology 相同的更新中完成。我们还建议同时更新您的 Interface 定义和 consumers。
> 如果您的下游应用程序无法与 Interface 更改同时更新，您可以选择创建该 Interface 的新版本（作为 [extension](/docs/foundry/interfaces/extend-interface/) 或独立 interface），并尽快迁移到新的 Interface 定义。
> **⚠️ 警告: Breaking**

> Because interfaces expose API names, any change to an interface definition has the potential to break downstream applications and will necessarily break existing object implementations. When adding a new required property or link type constraint to an interface, all implementations for object types that use the interface **must** be made in the same update to your Ontology. We also recommend updating your interface definitions and consumers at the same time.
> If your downstream applications cannot be updated at the same time as interface changes, you can alternatively create a new version of the interface (as an [extension](/docs/foundry/interfaces/extend-interface/) or a standalone interface) and migrate to the new interface definition as soon as possible.
## Add new properties
从 Interface 配置的 **Properties** 选项卡中，选择 **New property**。这将打开 Interface property 配置侧面板。

From the **Properties** tab of the interface configuration, choose **New property**. This will open an interface property configuration side panel.

> 📷 **[图片: Edit interface properties.]**

> 📷 **[图片: Edit interface properties.]**

用于编辑 property metadata 的可用选项被归类为四个不同的选项卡，可访问以下配置：

The available options for editing property metadata are clustered into four different tabs which give access to the following configurations:
1. **Display name and description：** 选择进入现有的 display name 或 description 以编辑文本。

2. **API name：** 选择进入现有的 API name 以更改其值。

3. **Property base type：** 从下拉菜单中选择 property 的 base type。property 的 type 限制可对其值执行的可能操作集。

* 例如，具有 base type `timestamp` 的 property 可以在 Object Explorer 的 timeline widget 中显示。

4. **Primary key constraint：** 指示 property 是否应为 primary key 或不能为 primary key。

1. **Display name and description:** Select into the existing display name or description to edit the text.
2. **API name:** Select into the existing API name to change its value.
3. **Property base type:** Select the property’s base type from the dropdown menu. The type of the property constrains the possible set of operations that can be done on the property’s values.
* For example, a property with base type `timestamp` can be shown in a timeline widget in Object Explorer.
4. **Primary key constraint:** Indicate whether a property should be a primary key or cannot be a primary key.
> **⚠️ 警告**

> 如果您对 Interface property types 进行了更改，则还必须更新实现此 Interface 的所有 Object Types。
> **⚠️ 警告**

> If you make a change to the interface property types, you must also update all object types implementing this interface.
5. **Type classes：** 应用 type classes 作为可由应用程序解释的附加 metadata。

* 请参阅 [type classes documentation](/docs/foundry/object-link-types/metadata-typeclasses/) 以获取可用 type classes 的列表。

6. **Render hints：** 通过从清单中选择 render hints 来改进 property value 的渲染方式以及索引到 Object Storage V1 (Phonograph) 的方式。

* 请参阅 [render hints documentation](/docs/foundry/object-link-types/metadata-render-hints/) 以获取可用 render hints 的描述。

7. **Visibility：** 选择现有的 visibility 以打开可用 visibilities 的下拉菜单。`prominent` property 将使应用程序优先向用户显示此 property。`hidden` property 将不会出现在用户应用程序中。

5. **Type classes:** Apply type classes as additional metadata that can be interpreted by applications.
* Review the [type classes documentation](/docs/foundry/object-link-types/metadata-typeclasses/) for a list of available type classes.
6. **Render hints:** Improve how a property value is rendered and indexed into Object Storage V1 (Phonograph) by selecting render hints from the checklist.
* See the [render hints documentation](/docs/foundry/object-link-types/metadata-render-hints/) for descriptions of the available render hints.
7. **Visibility:** Select the existing visibility to open a dropdown menu of available visibilities. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications.
## Add shared properties
从 Interface 配置的 **Properties** 选项卡中，选择 **Add shared properties** 并选择一个 shared property 添加到 Interface。

From the **Properties** tab of the interface configuration, select **Add shared properties** and choose a shared property to add to the interface.
## Add a link type constraint
从 **Link type constraints** 选项卡中，选择 **Create new link type constraint** 并添加必要的 [constraint metadata](/docs/foundry/interfaces/create-interface/#create-interface-link-types-optional)。

From the **Link type constraints** tab, select **Create new link type constraint** and add the necessary [constraint metadata](/docs/foundry/interfaces/create-interface/#create-interface-link-types-optional).
## Remove properties
从 **Properties** 选项卡中，选择要从此 Interface 中移除的 property 旁边的 **...**。或者，打开 Interface property 侧面板并选择右上角的垃圾桶图标。

From the **Properties** tab, select **...** next to the property you wish to remove from the interface. Alternatively, open the interface property side panel and select the trash icon in the upper right corner.

> 📷 **[图片: Remove property from an interface.]**

> 📷 **[图片: Remove property from an interface.]**

## Remove or edit link type constraints
在 **Link type constraint** 选项卡中，选择要编辑或从 Interface 中删除的 Link Type Constraint 旁的 **...**。

From the **Link type constraint** tab, select **...** next to the link type constraint you wish to edit or remove from the interface.

> 📷 **[图片: Remove or edit a link type constraint.]**

> 📷 **[图片: Remove or edit a link type constraint.]**

如果编辑 Constraint，您可以像[首次创建 link type constraint](/docs/foundry/interfaces/create-interface/#create-interface-link-types-optional)时一样更新元数据。

If editing a constraint, you can update the metadata as you would if you were [creating the link type constraint](/docs/foundry/interfaces/create-interface/#create-interface-link-types-optional) for the first time.