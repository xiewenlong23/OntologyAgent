<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/create-struct-type/
---
# Create a struct property type
从 Ontology Manager 中的 **Object types** 页面创建并配置新的 struct property。有关 struct properties 的更多信息，请参阅 [概述](/docs/foundry/object-link-types/structs-overview/)。

Create and configure a new struct property from the **Object types** page in Ontology Manager. For more information about struct properties, see the [overview](/docs/foundry/object-link-types/structs-overview/).
1. 在 Ontology Manager 中，打开左侧边栏中的 **Object types** 选项卡，然后选择一个现有的 object type。

2. 在 object type 详细信息页面中，打开左侧边栏中的 **Properties** 选项卡，然后选择 **Properties** 表格右上角的 **Create property** 按钮。

1. In Ontology Manager, open the **Object types** tab in the left sidebar and select an existing object type.
2. In the object type details page, open the **Properties** tab in the left sidebar, and select the **Create property** button on the top right of the **Properties** table.

> 📷 **[图片: object type 的 Properties 表格和 'Property editor' 面板。]**

> 📷 **[图片: The object type Properties table and 'Property editor' panel.]**

3. 在 **Property editor** 面板中，添加名称和描述，并从 **Base type** 下拉菜单中选择 **Struct**。

3. In the **Property editor** panel, add a name and description, and select **Struct** from the **Base type** dropdown menu.

> 📷 **[图片: Base type 下拉菜单，其中选择了 'Struct'。]**

> 📷 **[图片: The Base type dropdown with 'Struct' selected.]**

4. 向下滚动到 **Data** 部分,然后从下拉菜单中选择一个 **Backing column**。

4. Scroll down to the **Data** section and select a **Backing column** from the dropdown.

> 📷 **[图片: Choose a backing column in the Data section of the Property editor.]**

> 📷 **[图片: Choose a backing column in the Data section of the Property editor.]**

5. 在 **Struct fields** 部分,选择 **Add field**,然后选择 **New field**。

5. In the **Struct fields** section, select **Add field**, then **New field**.

> 📷 **[图片: Sample struct fields in a struct property type.]**

> 📷 **[图片: Sample struct fields in a struct property type.]**

6. 为新的 struct field 命名,并可选择性地添加描述。

7. 最后,将 datasource 中的某一列映射到新的 struct field。

6. Name the new struct field and optionally add a description.
7. Lastly, map a column from a datasource to the new struct field.