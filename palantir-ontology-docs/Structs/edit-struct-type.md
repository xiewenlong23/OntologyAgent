<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/edit-struct-type/
---
# Edit a struct property type
1. 在 Ontology Manager 中,打开左侧边栏的 **Object types** 选项卡,然后选择一个现有的 object type。

2. 在 object type 详情页面中,打开左侧边栏的 **Properties** 选项卡,并从 **Properties** 表格中选择相关的 struct property type。

3. 在 **Property editor** 面板中,滚动到 **Struct fields** 部分,然后选择您想要编辑的 struct field。所做的编辑次数将显示在 Ontology Manager 界面的右上角。

1. In Ontology Manager, open the **Object types** tab in the left sidebar and select an existing object type.
2. In the object type details page, open the **Properties** tab in the left sidebar, and select the relevant struct property type from the **Properties** table.
3. In the **Property editor** panel, scroll to the **Struct fields** section and select the struct field you would like to edit. The number of edits made will appear on the top right of the Ontology Manager interface.

> 📷 **[图片: Struct fields in the 'Property editor' panel.]**

> 📷 **[图片: Struct fields in the 'Property editor' panel.]**

4. 在 **Edit struct field** 对话框中进行必要的编辑,然后选择 **Confirm**。

4. Make the necessary edits in the **Edit struct field** dialog, and select **Confirm**.

> 📷 **[图片: The 'Edit struct field' dialog.]**

> 📷 **[图片: The 'Edit struct field' dialog.]**

> **ℹ️ 注意**

> 请注意,更改 struct field 的 API name 将导致生成新的 struct field RID。这将覆盖现有索引,其行为类似于更改 property type 的 property ID。任何引用已更新 struct field 的应用程序也需要相应更新。
> **ℹ️ 注意**

> Note that changing a struct field's API name will result in a new struct field RID being generated. This will override the existing index, similar to the behavior of changing the property ID of a property type. Any applications that reference the updated struct field will need to be updated as well.