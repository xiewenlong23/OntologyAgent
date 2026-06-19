<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/implement-interface/
---
# Implement an interface
一旦定义，interface 可以由任何符合该 interface 定义的 object type 来实现。这意味着 object type 必须具有与 interface 必需 properties 相对应并满足这些必需 properties 的 properties，并且具有满足 interface 上定义的所有必需 link type 约束的 links。

Once defined, an interface can be implemented by any object type that conforms to the interface definition. This means that object types must have properties that map onto and satisfy the interface's required properties, and possess links that satisfy all required link type constraints defined on the interface.
使用 object type 实现 interface 表明该 object type 是 Ontology 中 interface 的具体实例。此声明促进了 object type 上的附加功能，即：

Implementing an interface with an object type indicates that that object type is a concrete instance of the interface within the Ontology. This declaration facilitates additional functionality on the object type, namely:
* 针对 interface 的 Object Set Service 搜索将返回实现 object type 的匹配对象。

* 实现 object type 的对象可以使用其本地 API 名称（当类型为具体 object type 时）以及 properties 和 links 的 interface API 名称（当类型为 interface 类型时）进行交互。

* Object Set Service searches against the interface will return matching objects of the implementing object type.
* Objects of the implementing object type can be interacted with using both their local API names when typed as the concrete object type and the interface API names for properties and links when typed as the interface type.
简而言之，实现 interface 允许应用程序使用者通过 interface 定义与所有实现对象进行交互。这允许使用 interface 作为 API 层编写应用程序代码，而不需要应用程序单独支持每个实现 object type。此外，通过使用 interface 作为应用程序 API 层，可以通过让新的 object type 实现应用程序 interface 来将其添加到应用程序中，而无需更改代码以显式支持新的 object type。

In short, implementing an interface allows application consumers to interact with any and all implementing objects through the interface definition. This allows application code to be written using the interface as an API layer instead of requiring the application to support every implementing object type individually. Additionally, by using the interface as an application API layer, new object types can be added to the application by having them implement the application interface without requiring code changes to explicitly support the new object type.
## How to implement an interface in Ontology Manager
按照以下步骤使用 object type 实现 interface。

Follow the steps below to implement an interface with an object type.
### 1. Select your interface and object type
首先，在 Ontology Manager 中导航到该 object type 并打开 **Interfaces** 选项卡。在页面右上角选择 **+ Implement new interface**。

First, navigate to the object type in Ontology Manager and open the **Interfaces** tab. Select **+ Implement new interface** in the top right corner of the page.

> 📷 **[图片: Implement an interface from an object type.]**

> 📷 **[图片: Implement an interface from an object type.]**

在弹出的对话框中，选择要实现的 interface。

In the dialog that appears, select the interface to implement.

> 📷 **[图片: Select interface to implement.]**

> 📷 **[图片: Select interface to implement.]**

或者，导航到 interface 概览页面，在 **Implementations（实现）** 部分选择 **+ New（新建）**。

Alternatively, navigate to the interface overview page and select **+ New** in the **Implementations** section.

> 📷 **[图片: Implement an interface from the interface overview.]**

> 📷 **[图片: Implement an interface from the interface overview.]**

然后，选择实现该 interface 的 object type。

Then, select the object type to implement the interface.

> 📷 **[图片: Select interface to implement.]**

> 📷 **[图片: Select interface to implement.]**

### 2. Map local properties
要实现一个 interface，object type 必须声明将现有 object property 映射到所需的 interface property。如果某个 interface property 被标记为 **optional（可选）**，则可以跳过映射。

To implement an interface, an object type must declare a mapping of existing object properties onto the required interface properties. If an interface property is marked as **optional**, mapping may be skipped.

> 📷 **[图片: Map properties between the interface and the implementing object type.]**

> 📷 **[图片: Map properties between the interface and the implementing object type.]**

### 3. Map link type constraints
如果 interface 上声明了任何必需的 [link type constraints（link type 约束）](/docs/foundry/interfaces/interface-link-types-overview/)，则必须在 object type 上为每个必需的 link type 约束选择一个满足条件的 link type。您还可以为任何非必需的 link type 约束选择性地提供 link 映射。您可以选择现有的 link type 或创建一个新的 link type 来满足每个约束。

If any required [link type constraints](/docs/foundry/interfaces/interface-link-types-overview/) are declared on the interface, you must select a link type on the object type that satisfies each required link type constraint. You can also optionally provide a link mapping for any non-required link type constraints. You can choose an existing link type or create a new one to satisfy each constraint.

> 📷 **[图片: Map link types to fulfill link type constraints.]**

> 📷 **[图片: Map link types to fulfill link type constraints.]**

### 4. Save changes
选择 **Save（保存）** 以将更改应用到您的 Ontology。

Select **Save** to make the changes to your Ontology.
## How to implement an interface in Pipeline Builder
按照以下步骤在 Pipeline Builder 中对 [object type output（object type 输出）](/docs/foundry/pipeline-builder/outputs-add-ontology-output/#add-an-object-type-output) 实现 interface。

Follow the steps below to implement an interface on an [object type output](/docs/foundry/pipeline-builder/outputs-add-ontology-output/#add-an-object-type-output) in Pipeline Builder.
### 1. Open output type configuration
选择要实现 interface 的 object type output，然后选择 **Edit（编辑）** 选项。

Select the object type output that you would like to implement an interface, then select the **Edit** option.

> 📷 **[图片: Edit object type output.]**

> 📷 **[图片: Edit object type output.]**

### 2. Select the interface to implement
选择 **Implement interface**。

Select **Implement interface**.

> 📷 **[图片: Select Implement interface.]**

> 📷 **[图片: Select Implement interface.]**

然后，选择要 implement 的 interface，并选择 **Implement and go to mapping**。

Then, select the interface to implement and choose **Implement and go to mapping**.

> 📷 **[图片: Interface selection and go to mapping.]**

> 📷 **[图片: Interface selection and go to mapping.]**

### 3. Map local properties
要 implement 一个 interface，Object Type 必须包含该 interface 的 shared properties **或**声明将现有 Object Properties 映射到 interface shared properties 的 mapping。Interface 和 Object Type 上同时存在的 shared properties 将自动映射。Object Type 上不存在的任何 shared properties 将要求您手动输入 mapping 以满足 interface 定义。

To implement an interface, an object type must contain the interface's shared properties **or** declare a mapping of existing object properties onto the interface shared properties. Shared properties that are present on both the interface and object type will be automatically mapped. Any shared properties that are not on the object type will require you to manually input a mapping to satisfy the interface definition.

> 📷 **[图片: Map local properties.]**

> 📷 **[图片: Map local properties.]**

### 4. Review implemented interfaces
您可以在 output type configuration 面板中查看此 Object Type 实现的 interfaces。

You can view the interfaces implemented by this object type output from the output type configuration panel.

> 📷 **[图片: Review implemented interfaces.]**

> 📷 **[图片: Review implemented interfaces.]**

> **ℹ️ 注意**

> Pipeline Builder 目前不支持在 implement interface 时进行 link type constraint mapping。如果您的 interface 包含必需的 link type constrains，则必须通过 Ontology Manager 来 implement 该 interface。
> **ℹ️ 注意**

> Pipeline Builder does not currently support link type constraint mapping when implementing an interface. If your interface contains required link type constrains, you must implement the interface through Ontology Manager.