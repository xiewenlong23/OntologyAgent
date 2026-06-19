<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/extend-interface/
---
# Extend an interface
扩展 Interface 允许您将多个 Interface 组合在一起，创建一个新的、更具体的 Interface。这对于构建实施多个 [capability interfaces](/docs/foundry/interfaces/interface-overview/) 的 [abstract object interfaces](/docs/foundry/interfaces/interface-overview/) 特别有用。Interface 会继承其扩展的 Interface 的共享 Property 和 Link。一个 Interface 可以扩展任意数量的其他 Interface。

Extending an interface allows you to compose interfaces together, creating a new, more specific interface. This is particularly useful for constructing [abstract object interfaces](/docs/foundry/interfaces/interface-overview/) that implement multiple [capability interfaces](/docs/foundry/interfaces/interface-overview/). An interface inherits the shared properties and links of the interface it extends. An interface can extend any number of other interfaces.
要扩展 Interface，请按照以下步骤操作。

To extend an interface, follow the steps below.
1. 在 Ontology Manager 中，选择要扩展的 Interface 以打开 Interface 概览页面。

1. From Ontology Manager, select the interface you wish to extend to open the interface overview page.
2. 在概览页面中，从左侧面板选择 **Extension**。

2. From the overview page, select **Extension** from the left side panel.
3. 在 interface 扩展页面中，选择 **Add extension**。

3. From the interface extensions page, select **Add extension**.

> 📷 **[图片: Add an extension to an interface.]**

> 📷 **[图片: Add an extension to an interface.]**

4. 从下拉菜单中，选择要从当前 interface 扩展的 interface。

4. From the dropdown menu, select the interface to extend from your current interface.

> 📷 **[图片: Confirm interface extension.]**

> 📷 **[图片: Confirm interface extension.]**

5. 在确认对话框中，查看将添加到 interface 扩展的共享 properties 和 links，然后选择 **Confirm**。

5. In the confirmation dialog, review the shared properties and links that will be added to the interface extension and select **Confirm**.
6. 在右上角选择 **Save**，将 interface 扩展添加到 Ontology 中。

6. Select **Save** in the upper right corner to add the interface extension to the Ontology.
您也可以移除扩展以解除一个 interface 与另一个 interface 的关联。此操作将移除所有继承的共享 properties，移除所有继承的 link type 约束，并断开扩展 interface 与基础 interface 的关联。

You can also remove an extension to decouple one interface from another. This action will remove all inherited shared properties from the interface, remove all inherited link type constraints, and disassociate the extending interface from the base interface.

> 📷 **[图片: Remove an existing interface extension.]**

> 📷 **[图片: Remove an existing interface extension.]**

