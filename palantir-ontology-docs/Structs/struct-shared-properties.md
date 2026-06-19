<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/struct-shared-properties/
---
# Struct properties and shared property types
Struct 属性可被本地和共享 property type 使用。在转换或将本地 property type 提升为共享 property type 时，struct 字段需要重新映射。由共享 property type 支持的本地 struct property type 将继承共享 property type 的字段，但不包括 struct 字段资源标识符 (RIDs)。然后，struct 字段元数据（显示名称、描述、别名）将从共享 property type 继承，但 struct 字段将保留其原始 RIDs。

Struct properties can be used by local and shared property types. When converting, or promoting a local property type to a shared property type, struct fields need to be re-mapped. Local struct property types backed by shared property types will inherit shared property type fields except for the struct field resource identifiers (RIDs). Struct field metadata (display name, description, aliases) will then be inherited from the shared property type, but struct fields with keep their original RIDs.
## Create a struct type shared property
1. 在 Ontology Manager 中，您可以通过两种方式创建 struct 类型的 shared property：

* 从主页右上角，选择 **New > Shared property**

> 📷 **[图片: Shared property option from the New dropdown menu.]**

1. In Ontology Manager, you can create a struct type shared property in two ways:
* From the top right of the homepage, select **New > Shared property**

> 📷 **[图片: Shared property option from the New dropdown menu.]**

* 选择 **Shared properties > + New shared property**

> 📷 **[图片: + New shared property option in the Shared properties tab.]**

* Select **Shared properties > + New shared property**

> 📷 **[图片: + New shared property option in the Shared properties tab.]**

2. 在主面板中，选择 **New shared property** 按钮。这将打开一个辅助工具，您可以在其中配置 shared property 的元数据，包括名称、描述、别名和 API 名称。然后选择 **Next** 继续。

2. In the main panel, select the **New shared property** button. This will open a helper where you can configure metadata of the shared property including the name, description, aliases, and API name. Then select **Next** to proceed.

> 📷 **[图片: The 'Create shared property' dialog.]**

> 📷 **[图片: The 'Create shared property' dialog.]**

3. 配置基类型、值类型、可见性以及是否要求该 property 必须有值。

3. Configure the base type, value type, visibility, and whether to require values for the property.

> 📷 **[图片: Create shared property window on the configuration step.]**

> 📷 **[图片: Create shared property window on the configuration step.]**

4. 选择一个项目来保存此 shared property。

4. Select a project to save this shared property to.

> 📷 **[图片: Select save location for the shared property.]**

> 📷 **[图片: Select save location for the shared property.]**

5. 返回 Ontology Manager，在右上角选择 **Save** 以[将更改应用于您的 ontology](/docs/foundry/ontology-manager/save-changes/)。

5. Back in Ontology Manager, select **Save** in the upper right corner to [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/).
## Attach a struct type shared property
1. 在 Ontology Manager 中，打开 **Properties** 标签页，并从 **Properties** 表格中选择所需的 property。

2. 在右侧的 **Property editor** 中，向下滚动到 **Shared property**，并在 **Assign** 下选择一个 shared property。这将在两个 property 之间共享 property 元数据。

1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.
2. In the **Property editor** to the right, scroll down to **Shared property** and select a shared property under **Assign**. This will share property metadata among both properties.

> 📷 **[图片: The shared property dropdown in the Assign section.]**

> 📷 **[图片: The shared property dropdown in the Assign section.]**

**Note:** To add new struct fields after assigning a shared property type to a local struct property type, you must add the new struct fields to the shared property type and map them to datasource columns for all local struct property types that are backed by the shared property.
**Note:** To add new struct fields after assigning a shared property type to a local struct property type, you must add the new struct fields to the shared property type and map them to datasource columns for all local struct property types that are backed by the shared property.
## Convert a struct property type into a shared property
The following instructions detail how to convert a struct property into a struct property backed by a shared property type.
The following instructions detail how to convert a struct property into a struct property backed by a shared property type.
1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.
2. In the **Property editor** to the right, scroll down and select **Convert to a shared property**, which backs the struct property by a shared property type.
1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.
2. In the **Property editor** to the right, scroll down and select **Convert to a shared property**, which backs the struct property by a shared property type.

> 📷 **[图片: The 'Convert to a shared property' button in the Property editor.]**

> 📷 **[图片: The 'Convert to a shared property' button in the Property editor.]**

