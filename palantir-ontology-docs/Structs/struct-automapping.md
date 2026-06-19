<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/struct-automapping/
---
# Automapping struct properties
Automapping 允许用户自动映射所有列,而不是手动映射。

Automapping allows users to map all columns automatically rather than manually.
## Automap struct types in Ontology Manager
如果 object 已经被创建,用户可以使用 **Automap all** 功能来自动映射所有列。

If the object has already been created, users can automap all columns by using the **Automap all** feature.
1. 在 Ontology Manager 中,进入 **Properties** 选项卡并选择所需的 property。

2. 在 **Column mapping** 选项卡下,选择所需的 column。

1. In Ontology Manager, enter the **Properties** tab and select the desired property.
2. Under the **Column mapping** tab, select the desired column.

> 📷 **[图片: The 'Column mapping' tab and the 'Automap all' button.]**

> 📷 **[图片: The 'Column mapping' tab and the 'Automap all' button.]**

3. 选择 **Automap all**。

3. Select **Automap all**.
## Automap struct types in Pipeline Builder
如果对象尚未创建，可以在初始对象创建时使用 object type creation wizard（对象类型创建向导）完成 automapping。

If the object has not yet been created, automapping can be done on initial object creation with the object type creation wizard.
1. 在您的 Pipeline Builder pipeline 中，打开相关 dataset，并在右上角选择 **All Actions** 下拉菜单。

1. In your Pipeline Builder pipeline, open the relevant dataset and select the **All Actions** dropdown in the top right.

> 📷 **[图片: dataset 详情页面中的 All actions 下拉菜单。]**

> 📷 **[图片: The All actions dropdown in the dataset detail page.]**

2. 选择 **Create object type** 以创建一个新对象。

2. Select **Create object type** to create a new object.

> 📷 **[图片: “Create a new object”对话框中的 Properties 选项卡。]**

> 📷 **[图片: The Properties tab in the 'Create a new object' dialog.]**

3. 在 **Properties** 下，添加需要进行映射的所需 properties。

4. 选择 **Next** 并完成剩余步骤以创建 automapped object type。

3. Under **Properties**, add the desired properties to be mapped.
4. Select **Next** and complete the remaining steps to create an automapped object type.