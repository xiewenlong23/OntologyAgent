<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/edit-only-properties/
---
# Edit-only properties
仅编辑 property（edit-only properties）允许您定义不直接映射到 Object Type 后端数据集中某一列的 Ontology property。

这在您希望在不修改底层数据集的情况下与 Object Type 一起存储额外信息时特别有用。

Edit-only properties allow you to define Ontology properties that are not directly mapped to a column in the backing dataset of the object type.
This is particularly useful for situations where you may want to store additional information alongside your object types without modifying the underlying dataset.
## Summary of edit-only properties
在使用仅编辑 property 时，请牢记以下几点：

When working with edit-only properties, keep the following in mind:
* **不映射到后端数据集中的列：** 仅编辑 property 不需要映射到后端数据集中的特定列。这允许您在后端列存在之前轻松创建新 property，或创建仅通过 ontology 进行编辑的 property。

* **授权给 Object Type 的后端数据集之一：** 为确保数据一致性和安全性，仅编辑 property 必须授权给 Object Type 的后端数据集之一。

* **仅在 Object Storage V2 中可用：** 仅编辑 property 是 Object Storage V2 的 Object Type 独占可用的功能。

* **No mapping to a column in the backing dataset:** Edit-only properties are not required to be mapped to a specific column in the backing dataset. This allows you to easily create new properties before the backing column exists, or create properties that will only be edited through the ontology.
* **Permissioned to one of the datasets backing the object type:** To ensure data consistency and security, edit-only properties must be permissioned to one of the datasets backing the object type.
* **Available only in Object Storage V2:** Edit-only properties are a feature that is exclusively available for object types leveraging Object Storage V2.
### Creating edit-only properties
1. 导航至 **Ontology Manager**。

2. 选择您要向其添加仅编辑 property 的 Object Type。

3. 选择 **Create Property** 并填写必需的详细信息，包括 property 名称、类型和描述。

4. 在 **Data** 部分，开启 **Edit-only property** 开关并选择一个数据集进行授权（如果您的 Object Type 有多个后端数据集）。

5. **保存** 您的更改以创建仅编辑 property。

1. Navigate to the **Ontology Manager**.
2. Choose the object type to which you want to add an edit-only property.
3. Select **Create Property** and fill in the required details, including the property name, type, and description.
4. Under the **Data** section, toggle on the **Edit-only property** toggle and choose a dataset to permission to (if you have more than one dataset backing the object type).
5. **Save** your changes to create the edit-only property.

> 📷 **[图片: Edit-only property]**

> 📷 **[图片: Edit-only property]**

### Mapping edit-only properties to dataset columns
如果您稍后决定在后端数据集中添加与当前为仅编辑的 property 相对应的列，您可以轻松地将该 property 映射到新列。

If you later decide to add a column to your backing dataset that corresponds to a property that is currently edit-only, you can easily map that property to the new column.
1. 导航至 **Ontology Manager**。

2. 选择您要映射其仅编辑 property 的 Object Type。

3. 选择该仅编辑 property 以打开其详细信息。

4. 在 **Data** 部分，关闭仅编辑 property 开关并从某个后端数据集中选择一列。
5. **保存** 您的更改。

1. Navigate to the **Ontology Manager**.
2. Choose the object type with the edit-only property you want to map.
3. Select the edit-only property to open its details.
4. Under the **Data** section, untoggle the edit-only property and choose a column from one of the backing datasets.
5. **Save** your changes.