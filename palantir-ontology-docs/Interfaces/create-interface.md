<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/create-interface/
---
# Create an interface
请按照以下步骤在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中创建一个新的 interface。

Follow the steps below to create a new interface in [Ontology Manager](/docs/foundry/ontology-manager/overview/).
1. 首先，通过检查左侧面板顶部的 **Ontologies** 下拉菜单，确认您正在使用所需的 ontology。

1. First, verify you are working within your ontology of choice by checking the **Ontologies** dropdown menu located at the top of the left side panel.
2. 要创建一个新的 interface，您可以执行以下任一操作：

* 在页面右上角，选择 **New > Interface**。

* 从左侧面板的 **Resources** 部分下，选择 **Interfaces > + New interface**。然后，在 **Interfaces** 页面中，从屏幕右上角选择 **New interface**。

2. To create a new interface, you can do either of the following:
* At the top right of the page, select **New > Interface**.
* From the left panel, select **Interfaces > + New interface** under the **Resources** section. Then, from the **Interfaces** page, select **New interface** from the top right corner of the screen.
3. 辅助工具的第一页提供了有关 interface 的信息。选择 **Next**。

> 📷 **[图片: Interface creation about page.]**

3. The first page of the helper provides information about interfaces. Select **Next**.

> 📷 **[图片: Interface creation about page.]**

4. 为您的 interface 输入显示名称（display name）和 API 名称（API name）。您还可以选择性地提供 interface 的描述并选择合适的图标。

4. Input the display name and API name for your interface. You can also optionally provide a description of the interface and select an appropriate icon.

> 📷 **[图片: Interface metadata creation]**

> 📷 **[图片: Interface metadata creation]**

5. 向您的 interface 添加 property。您可以在 interface 上本地定义 property（推荐），或使用 [shared property](/docs/foundry/object-link-types/shared-property-overview/)。对于每个 property，选择它是 **required（必填）** 还是 **optional（可选）**。

5. Add properties to your interface. You can define properties locally on the interface (recommended) or use [shared properties](/docs/foundry/object-link-types/shared-property-overview/). For each property, choose whether it is **required** or **optional**.

> 📷 **[图片: Interface property selection]**

> 📷 **[图片: Interface property selection]**

对于 **required** property，实现该 interface 的任何 object type 都必须提供从本地 property 到 interface property 的映射。对于 **optional** property，在实现过程中可以跳过映射。在构建 Marketplace 包时，optional property 非常有用，可以在不对 interface 引入难以解决的升级阻塞问题的情况下对其进行迭代。

For **required** properties, any object type that implements the interface must provide a mapping from a local property to the interface property. For **optional** properties, mapping may be skipped during implementation. Optional properties can be useful when building Marketplace packages to iterate on your interface without introducing upgrade blockers that may be difficult to resolve.
6. 选择一个项目来保存此 interface，然后选择 **Create**。

6. Select a project to save this interface to, then select **Create**.

> 📷 **[图片: Interface save location.]**

> 📷 **[图片: Interface save location.]**

7. 返回 Ontology Manager，在右上角选择 **Save** 以[对您的 ontology 进行更改](/docs/foundry/ontology-manager/save-changes/)。

7. Back in Ontology Manager, select **Save** in the upper right corner to [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/).
## Create interface link types (optional)
如果您希望此 Interface 链接到另一个 Interface 或 Object Type，可以选择性地向该 Interface 添加任何 [Interface link types](/docs/foundry/interfaces/interface-link-types-overview/)。

If you want this interface to link to another interface or object type, you can optionally add any [interface link types](/docs/foundry/interfaces/interface-link-types-overview/) to the interface.

> 📷 **[图片: Add a link type constraint]**

> 📷 **[图片: Add a link type constraint]**

1. 在左侧面板中选择 **Link type constraints**。

2. 然后，在右上角选择 **Create new link type constraint**。

1. Select **Link type constraints** in the left side panel.
2. Then, select **Create new link type constraint** in the top right corner.

> 📷 **[图片: Create a link type constraint]**

> 📷 **[图片: Create a link type constraint]**

如果您的建模用例需要 Interface link type，则实现该 Interface 的任何 Object Type 都必须添加新的或现有的 link type，以满足 Interface link type 约束。

If an interface link type is required for your modeling use case, any object type that implements the interface must add a new or existing link type that satisfies the interface link type constraints.