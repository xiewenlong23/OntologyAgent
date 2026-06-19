<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/use-shared-property/
---
# Use shared properties on object types
要将 object type 上的属性更新为共享属性，请完成以下步骤：

To update a property on an object type to a shared property, complete the following steps:
1. 导航到 Ontology Manager 中的 object type。

2. 在面板上选择要更新的属性，然后向下滚动到配置的 **Shared Property** 部分。

1. Navigate to the object type in the Ontology Manager.
2. Select the property on the panel that you want to update, then scroll down to the **Shared Property** section of the configuration.

> 📷 **[图片: 使用共享属性]**

> 📷 **[图片: Using a shared property]**

3. 使用下拉菜单选择要使用的现有共享属性，或使用 [shared property creation](/docs/foundry/object-link-types/create-shared-property/) 模态框将该属性转换为新的共享属性。

3. Use the dropdown menu to select an existing shared property to use, or convert the property to a new shared property with the [shared property creation](/docs/foundry/object-link-types/create-shared-property/) modal.
该属性随后将显示为共享属性。要将对共享属性的使用持久化到 Ontology 中，请选择右上角的 **Save**。

The property will then display as a shared property. To persist the use of the shared property to the Ontology, select **Save** in the upper right.
* 在 object 上使用共享属性时，对象特定属性的 property ID 和 API name 将保持不变，以免破坏依赖它们的现有下游工作流。

* 与共享属性关联时，从共享属性继承的属性元数据的直接编辑将被禁用。您仍然可以添加、删除或编辑 type classes。当加载属性时，最终的 type classes 集合将是来自该属性及其关联的共享属性的 type classes 的并集。

* 如果您使用的共享属性具有与所选属性不同的 [render hint](/docs/foundry/object-link-types/metadata-render-hints/) 配置值，则使用该共享属性将覆盖所选属性的配置值。请确保您的共享属性针对您的用例配置了适当的 render hints。

* When using a shared property on an object, the property ID and API name of the object-specific property will remain unchanged so as to not break existing downstream workflows that leverage them.
* While associated with a shared property, direct edits to property metadata that is inherited from the shared property will be disabled. You can still add, delete, or edit type classes. When the property is loaded, the resulting set of type classes will be a union of those from the property and its associated shared property.
* If the shared property you use has different [render hint](/docs/foundry/object-link-types/metadata-render-hints/) configuration values than the selected property, using the shared property will override the configuration values of the selected property. Make sure your shared property is configured with the proper render hints for your use case.
### Detach a shared property from an object
要将属性从共享属性中分离，请在 Ontology Manager 中 object type 上的同一属性面板中选择 **Detach**。

To detach a property from a shared property, use the same property panel on an object type in the Ontology Manager and select **Detach**.

> 📷 **[图片: 分离共享属性]**

> 📷 **[图片: Detach a shared property]**

这样做将移除该属性与共享属性之间的关联。

Doing so will remove the association between the property and the shared property.