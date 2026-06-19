<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/create-ontology-objects-from-gaia/
---
# Create Ontology objects from Gaia
与您可以[将 Ontology 中的数据添加到 Gaia 地图](/docs/foundry/geospatial/add-ontology-data-to-gaia/)的方式类似，您也可以通过在实现了 Gaia Geoshape Creatable、Gaia Geopoint Creatable 或 MILSTD 2525C Symbol [interface](/docs/foundry/interfaces/interface-overview/) 的 object type 内对对象进行标记，从而根据您在地图上绘制的 shape、放置的 point 或配置的 tactical graphic 来创建 Ontology 对象。

Similar to how you can [add data from the Ontology to a Gaia map](/docs/foundry/geospatial/add-ontology-data-to-gaia/), you can also create Ontology objects from a shape you draw, a point you drop, or a tactical graphic you configure on a map by tagging the object within an object type which implements the Gaia Geoshape Creatable, Gaia Geopoint Creatable, or the MILSTD 2525C Symbol [interface](/docs/foundry/interfaces/interface-overview/).
> **⚠️ 警告**

> MILSTD 2525C Symbol interface 通过 Palantir 的 [Defense OSDK](/docs/defense-osdk/api) 提供，它取代了 Gaia Milsym Creatable interface，后者目前处于 [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/#planned-deprecation) 阶段，并将于 2026 年 7 月被弃用。有关 Defense OSDK interface 的可用性或您注册中 Gaia Milsym Creatable interface 的弃用事宜，请联系 Palantir Support。
> **⚠️ 警告**

> Made available through Palantir's [Defense OSDK](/docs/defense-osdk/api), the MILSTD 2525C Symbol interface supersedes the Gaia Milsym Creatable interface, which is in the [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/#planned-deprecation) phase of development and will be deprecated by July 2026. Contact Palantir Support with questions about the availability of Defense OSDK interfaces or the deprecation of the Gaia Milsym Creatable interface on your enrollment.
> 如果您的注册中*同时*提供这两个 interface，请实现 MILSTD 2525C Symbol interface，而不是 Gaia Milsym Creatable interface。
> If *both* interfaces are available on your enrollment, implement the MILSTD 2525C Symbol interface instead of the Gaia Milsym Creatable interface.
![A Gaia map's Create shape window in the left panel is displayed, where a user can tag a shape drawn on a map as an object within an object type in their Ontology.](/docs/resources/foundry/object-link-types/create-shape.png)
> **⚠️ 警告**

> 要从 Gaia 地图创建 Ontology 对象，您的注册必须同时使用 Foundry 和 Gotham。
> **⚠️ 警告**

> To create Ontology objects from a Gaia map, your enrollment must use both Foundry and Gotham.
以下各节概述了将 Gaia shape、point 和 tactical graphic 与 Ontology 集成的端到端流程：

The sections below outline the end-to-end process to integrate Gaia shapes, points, and tactical graphics with the Ontology:
* [安装所有必要的 Marketplace 产品](#install-prerequisite-marketplace-products)。

* [在由 restricted view 支持的受支持 object type 上实现 Gaia Geoshape Creatable interface](#create-an-object-type-that-implements-the-gaia-geoshape-creatable-interface)。

* [在由 restricted view 支持的受支持 object type 上实现 Gaia Geopoint Creatable interface](#create-an-object-type-that-implements-the-gaia-geopoint-creatable-interface)。

* [在由 restricted view 支持的受支持 object type 上实现 MILSTD 2525C Symbol interface](#create-an-object-type-that-implements-the-milstd-2525c-symbol-interface)。

* [注册您的 ontology 并在 Gaia 中搜索您的 object type](#register-your-ontology-and-its-types)。

* [在地图上绘制新 shape 并将其标记到您的 object type 中](#draw-a-new-shape-on-your-gaia-map-and-tag-it-to-an-object-type)。

* [在地图上放置新 point 并将其标记到您的 object type 中](#drop-a-new-point-on-your-gaia-map-and-tag-it-to-an-object-type)。

* [根据在地图上绘制的 shape 配置 tactical graphic 并将其标记到您的 object type 中](#configure-a-tactical-graphic-on-your-gaia-map-and-tag-it-to-an-object-type)。

* [Install all necessary Marketplace products](#install-prerequisite-marketplace-products).
* [Implement the Gaia Geoshape Creatable interface on a supported object type backed by a restricted view](#create-an-object-type-that-implements-the-gaia-geoshape-creatable-interface).
* [Implement the Gaia Geopoint Creatable interface on a supported object type backed by a restricted view](#create-an-object-type-that-implements-the-gaia-geopoint-creatable-interface).
* [Implement the MILSTD 2525C Symbol interface on a supported object type backed by a restricted view](#create-an-object-type-that-implements-the-milstd-2525c-symbol-interface).
* [Register your ontology and search for your object types in Gaia](#register-your-ontology-and-its-types).
* [Draw a new shape on your map and tag it within your object type](#draw-a-new-shape-on-your-gaia-map-and-tag-it-to-an-object-type).
* [Drop a new point on your map and tag it within your object type](#drop-a-new-point-on-your-gaia-map-and-tag-it-to-an-object-type).
* [Configure a tactical graphic from a shape drawn on your map and tag it within your object type](#configure-a-tactical-graphic-on-your-gaia-map-and-tag-it-to-an-object-type).
## Install prerequisite Marketplace products
[Marketplace](/docs/foundry/marketplace/overview/) 是 Foundry 的应用商店，用于提供已发布的数据产品或平台资源集合供用户安装。您可以通过主页上的 **Search...** 栏或 **Applications** 入口访问 Marketplace。

[Marketplace](/docs/foundry/marketplace/overview/) is Foundry's storefront for published data products or collections of platform resources made available for user installation. You can access Marketplace through the **Search...** bar or the **Applications** portal on your home screen.
进入 Marketplace 后，请安装以下产品：

Once you launch Marketplace, install the following products:
* [来自 Core Ontology Store 的 Core Property Types](#core-property-types-from-the-core-ontology-store)，其中包含核心共享 property type，例如对象的 classification 和 geoshape，可用于您 ontology 中的多个 object type。

* [来自 Gaia App Store 的 Gaia Geoshape Creatable interface](#gaia-geoshape-creatable-interface-from-the-gaia-app-store)，它描述了地理空间 object type 的 shape，以便对相同 shape 的其他 object type 进行一致的建模和交互。

* [来自 Gaia App Store 的 Gaia Geopoint Creatable interface](#gaia-geopoint-creatable-interface-from-the-gaia-app-store)，它描述了单个 point object type 的 position。

* [Core Property Types from the Core Ontology Store](#core-property-types-from-the-core-ontology-store), which contains core shared property types, such as an object's classification and geoshape, that can be used on multiple object types in your ontology.
* [Gaia Geoshape Creatable interface from the Gaia App Store](#gaia-geoshape-creatable-interface-from-the-gaia-app-store), which describes the shape of a geospatial object type to enable consistent modeling of and interaction with other object types of the same shape.
* [Gaia Geopoint Creatable interface from the Gaia App Store](#gaia-geopoint-creatable-interface-from-the-gaia-app-store), which describes the position of a single point object type.
### Core Property Types from the Core Ontology Store
> **ℹ️ 注意**

> 如果 Marketplace 中没有包含 Core Property Types 产品的 Core Ontology Store，请联系 Palantir Support，以将 Core Ontology 作为 [Foundry product](/docs/foundry/marketplace/foundry-products/) 安装到您的 Foundry 注册中。
> **ℹ️ 注意**

> Contact Palantir Support to install the Core Ontology on your Foundry enrollment as a [Foundry product](/docs/foundry/marketplace/foundry-products/) if the Core Ontology Store, which contains the Core Property Types product, is not available in Marketplace.
### Gaia Geoshape Creatable interface from the Gaia App Store
在 Foundry 中，[interface](/docs/foundry/interfaces/interface-overview/) 存在于您的 ontology 中，用于描述 object type 的 shape 及其功能，从而实现对具有共同 shape 的 object type 之间的一致建模和交互。您可以在多个 object type 上实现一个 interface，并且 interface 可以扩展任意数量的其他 interface。一旦在 object type 上实现，Gaia Geoshape Creatable interface 使您能够根据在 Gaia 地图上绘制的 shape 在 ontology 中创建对象。

In Foundry, [interfaces](/docs/foundry/interfaces/interface-overview/) exist within your ontology to describe an object type's shape as well as its capabilities, enabling consistent modeling and interaction between object types of a common shape. You can implement an interface on multiple object types, and interfaces may extend any number of other interfaces. Once implemented on an object type, the Gaia Geoshape Creatable interface enables you to create objects in your ontology from shapes drawn on a Gaia map.
> **⚠️ 警告**

> Gaia Geoshape Creatable interface 取代了已弃用的 Gaia Geocreatable interface。如果您无法在 Marketplace 中访问 Gaia Geoshape Creatable interface，请联系 Palantir Support。
> **⚠️ 警告**

> The Gaia Geoshape Creatable interface supersedes the deprecated Gaia Geocreatable interface. Contact Palantir Support if you are unable to access the Gaia Geoshape Creatable interface in Marketplace.
要从 Marketplace 安装 Gaia Geoshape Creatable interface：

To install the Gaia Geoshape Creatable interface from Marketplace:
1. 返回 Marketplace，在 **Search stores...** 中搜索 `Gaia App Store`。

2. 选择 `Gaia Geoshape Creatable` 产品。

3. 选择屏幕右侧的蓝色 **Install** 按钮以启动草稿安装。您可以选择性地为安装添加描述性后缀。

4. 确定一个用于保存安装的 **Namespace**。Marketplace 将在所选 **Namespace** 中自动创建一个新的 **Project**。

5. 在 **Permissions** 下配置产品的分类和访问控制。您在 **Classification based access control (CBAC)** 下选择的分类定义了安装的*最高*分类。

6. 选择 **Next** 以启动安装窗口的 **Inputs** 页面。

7. 在左侧面板的 **Inputs** 下选择 **Shared properties** 选项卡，将 ontology 中的 `Geoshape` 共享 property 映射到您的新 interface。

8. 选择 **Next** 以启动安装窗口的 **Content** 页面。

1. Navigate back to Marketplace and search for the `Gaia App Store` in **Search stores...**.
2. Choose the `Gaia Geoshape Creatable` product.
3. Select the blue **Install** button on the right side of your screen to launch a draft installation. You can optionally add a descriptive suffix to your installation.
4. Identify a **Namespace** where your installation will save. Marketplace will automatically create a new **Project** within the chosen **Namespace**.
5. Configure the product's classification and access controls under **Permissions**. The classification you select under **Classification based access control (CBAC)** defines the *maximum* classification for the installation.
6. Select **Next** to launch the installation window's **Inputs** page.
7. Select the **Shared properties** tab under **Inputs** in the left panel to map the `Geoshape` shared property from your ontology to your new interface.
8. Select **Next** to launch the installation window's **Content** page.
![The Gaia Geoshape Creatable interface's Shared properties page is displayed, where a user configures shared properties to include in their interface.](/docs/resources/foundry/object-link-types/map-geoshape-creatable-inputs-as-spts.png)
9. （可选）开启 **Prefix Ontology entities** 并输入有效的前缀。请注意，您的前缀不能包含某些特殊字符，例如圆括号或方括号。

10. 在屏幕右侧选择需要在 Ontology 上启用的 **schema migrations**。您可以在现有的 [object edits and materializations documentation](/docs/foundry/object-edits/schema-migrations/) 中参考其他 schema 管理信息。

11. 根据您的用例需要，在 **New versions** 中更新自动配置，然后再选择 **Next**。Marketplace 会预先配置某些 product 以实现自动升级。

12. 检查您 interface 的配置，然后选择 **Install**。

9. Optionally toggle on **Prefix Ontology entities** and insert a valid prefix. Note that your prefix may not contain certain special characters, such as parentheses or brackets.
10. Choose which **Ontology schema migrations** to enable on the right side of your screen. You can reference additional schema management information within the existing [object edits and materializations documentation](/docs/foundry/object-edits/schema-migrations/).
11. Update the automatic configurations in **New versions** as necessary for your use case before you select **Next**. Marketplace pre-configures certain products to upgrade automatically.
12. Review your interface's configurations and select **Install**.
### Gaia Geopoint Creatable interface from the Gaia App Store
要从 Marketplace 的 Gaia App Store 安装 Gaia Geopoint Creatable interface，请从 store 菜单中选择 `Gaia Geopoint Creatable` product。Marketplace 的 interface 安装工作流在不同的 interface 之间是通用的，因此您可以按照上文 [Geoshape Creatable interface 安装说明](#gaia-geoshape-creatable-interface-from-the-gaia-app-store) 中列出的相同步骤进行操作，但有以下区别：

To install the Gaia Geopoint Creatable interface from Marketplace's Gaia App Store, select the `Gaia Geopoint Creatable` product from the store menu. Marketplace's interface installation workflows are common across different interfaces, so you can follow the same steps outlined in the [Geoshape Creatable interface installation instructions](#gaia-geoshape-creatable-interface-from-the-gaia-app-store) above with the following distinctions:
* 在 **Inputs** 窗口的 **Shared properties** 部分中，将您 ontology 中的 `Geopoint` shared property 映射到 Gaia Geopoint Creatable interface。

* In the **Shared properties** section of the **Inputs** window, map the `Geopoint` shared property from your ontology to the Gaia Geopoint Creatable interface.
## Create an object type that implements the Gaia Geoshape Creatable interface
在您 ontology 中由 [dataset](/docs/foundry/data-integration/datasets/) 或 [restricted view](/docs/foundry/security/restricted-views/) 支持的 object type 实现了 Gaia Geoshape Creatable interface 之后，Gaia 可以发现它们。在以下部分中，您将：

Gaia can discover object types backed by a [dataset](/docs/foundry/data-integration/datasets/) or [restricted view](/docs/foundry/security/restricted-views/) in your ontology after they implement the Gaia Geoshape Creatable interface. In the following sections, you will:
* [创建支持 object type 的 dataset 或 restricted view](#create-an-object-type-backing-dataset-or-restricted-view)。

* [创建 object type 并确保其与 Gotham 集成](#create-an-object-type-and-ensure-it-integrates-with-gotham)。

* [配置 action type 以在 Gaia 中启用 object creation](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia)。

* [实现 Gaia Geoshape Creatable interface](#implement-the-gaia-geoshape-creatable-interface)。

* [Create an object type-backing dataset or restricted view](#create-an-object-type-backing-dataset-or-restricted-view).
* [Create an object type and ensure it integrates with Gotham](#create-an-object-type-and-ensure-it-integrates-with-gotham).
* [Configure an action type to enable object creation in Gaia](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia).
* [Implement the Gaia Geoshape Creatable interface](#implement-the-gaia-geoshape-creatable-interface).
### Create an object type-backing dataset or restricted view
> **ℹ️ 注意**

> 如果您计划根据用户的 classification 或通过应用 [markings](/docs/foundry/security/markings/) 来保护 object 访问安全，则应创建 restricted view。如果您的用例不需要 classification-based access 或 markings 提供的额外 object 安全保护，则应创建 dataset 来支持您的 object type。
> **ℹ️ 注意**

> You should create a restricted view if you plan to secure objects based on a user's classification or by applying [markings](/docs/foundry/security/markings/) to control file access. If your use case does not require the additional object security provided by classification-based access or markings, then you should create a dataset to back to your object type.
要创建可与 Gaia 集成的 object type，您首先需要创建一个 dataset 或 restricted view，其中至少包含以下列：

To create an object type that can integrate with Gaia, you will first need to create a dataset or restricted view that contains, at a minimum, the following columns:
* `Geoshape`：将其设置为 `string` 类型，Gaia 将自动使用您绘制的 object 的 shape 进行填充。

* `Object ID`：将其设置为 `string` 类型，Foundry 将自动为您在 Gaia 中创建为 object 的每个 shape 填充唯一 ID。这将用作您的 object type 的主键。

* `Classification`：将其设置为 `array` 类型，以捕获您的 object 的 classification。仅当 restricted view 支持您的 object type 时，才 *需要* `Classification` 列。

* `Geoshape`, which you will set as a `string` for Gaia to automatically populate with your drawn object's shape.
* `Object ID`, which you will set as a `string` for Foundry to automatically populate with a unique ID for each Gaia shape you create as an object. This will serve as your object type's primary key.
* `Classification`, which you will set as an `array` to capture your object's classification. A `Classification` column is *only* required if a restricted view backs your object type.
> **✅ 成功**

> 您可以根据自己的具体用例在 dataset 或 restricted view 中配置其他列，例如设置为 `string` 类型的 `Name`、`Category` 或 `Notes` 列，以捕获用户输入的有关 object 的描述性信息。
> **✅ 成功**

> You can configure additional columns in your dataset or restricted view based on your specific use case, such as `Name`, `Category`, or `Notes` columns set as `strings` to capture user-entered descriptive information about the object.
在您的 Project 中选择 **New** 按钮以上传现有文件（例如 `.csv` 文件），或使用 [Fusion](/docs/foundry/fusion/overview/) 创建一个 standalone dataset 或支持您 restricted view 的 dataset。如果您使用 dataset 来支持您的 object type，则可以跳过下面的 restricted view 创建说明，直接进入 [创建 object type](#create-an-object-type-and-ensure-it-integrates-with-gotham)。

Select the **New** button in your Project to upload an existing file, such as a `.csv`, or use [Fusion](/docs/foundry/fusion/overview/) to create a standalone dataset or a dataset that backs your restricted view. If you use a dataset to back your object type, you can skip the restricted view creation instructions below and proceed to [create your object type](#create-an-object-type-and-ensure-it-integrates-with-gotham).
![Users can select the New button from their Project to upload data as a .csv or create a new Fusion sheet to store data which will back a restricted view.](/docs/resources/foundry/object-link-types/create-new-dataset-upload-fusion.png)
> **✅ 成功**

> 您可以在 Foundry 的 [security](/docs/foundry/security/restricted-views/#create-restricted-views) 和 [object permissions](/docs/foundry/object-permissioning/configuring-rv-access-controls/) 文档中参考其他 restricted view 创建说明。
> **✅ 成功**

> You can reference additional restricted view creation instructions in Foundry's [security](/docs/foundry/security/restricted-views/#create-restricted-views) and [object permissions](/docs/foundry/object-permissioning/configuring-rv-access-controls/) documentation.
您的 restricted view 应包含一个 [granular policy](/docs/foundry/security/restricted-views/#compose-a-granular-policy)，该策略根据用户的 [classification access](/docs/foundry/security/classification-based-access-controls/) 限制对 view 中数据的访问。在 **Create '{restricted view}'** 窗口中，将 granular policy 的编写作为第一步。

Your restricted view should contain a [granular policy](/docs/foundry/security/restricted-views/#compose-a-granular-policy) that restricts user access to the data contained in the view based on their [classification access](/docs/foundry/security/classification-based-access-controls/). Compose the granular policy as the first step in the **Create '{restricted view}'** window.
![An example restricted view policy is displayed.](/docs/resources/foundry/object-link-types/create-restricted-view.png)
> **⚠️ 警告**

> 如果一个 object 包含 CBAC 或 mandatory marking property 来限制其访问，那么 Foundry 将使用从 Gaia map 继承的 CBAC 或 mandatory markings 来创建 object，而 *不会* 应用在 map 的 security 和 sharing 设置中定义的 group 限制。
> **⚠️ 警告**

> If an object contains a CBAC or mandatory marking property to restrict its access, then Foundry creates objects using the CBAC or mandatory markings it inherits from the Gaia map and will *not* apply group restrictions defined in the map's security and sharing settings.
您可以参考下方 JSON 中的示例 policy。

You can reference an example policy in JSON below.
```json
{
"condition": {
"and": {
"conditions": [
{
"markings": {
"value": {
"field": {
"fieldName": "classification"
},
"type": "field"
},
"filters": [
{
"markingTypes": {
"markingTypes": [
"CBAC"
]
},
"type": "markingTypes"
}
]
},
"type": "markings"
}
]
},
"type": "and"
}
}
```
### Create an object type and ensure it integrates with Gotham
配置好 restricted view 后，启动 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 并按照以下步骤创建您的 object type：

Once you configure your restricted view, launch [Ontology Manager](/docs/foundry/ontology-manager/overview/) and follow the steps below to create your object type:
1. 从屏幕右上角选择 **New** > **Object type**。

2. 选择 **Use existing datasource**,然后选择 **Select datasource** 来定位并 **Select** 您的 restricted view,之后选择 **Next**。

3. 为您的 object type 命名,并可选择性地输入 **Description**。

4. 将 `Object ID` 设为 **Primary Key**,将 `Name` 设为 **Title**。

5. 确保 `Classification` 的 **Property** 是一个字符串数组,`Geoshape` 的 **Property** 为 geoshape。如果您的 object type 由 restricted view 支撑,则仅需验证前者。

1. Select **New** > **Object type** from the top right of your screen.
2. Select **Use existing datasource** and choose **Select datasource** to locate and **Select** your restricted view before choosing **Next**.
3. Name your object type and optionally enter a **Description**.
4. Set `Object ID` as the **Primary Key** and `Name` as the **Title**.
5. Ensure `Classification`'s **Property** is an array of strings and `Geoshape`'s **Property** is geoshape. You will only need to validate the former if a restricted view backs your object type.
![Ontology Manager's Create a new object type window is displayed, where a user can set an object type's Primary Key and Title as well as configure properties.](/docs/resources/foundry/object-link-types/object-type-classification-array.png)
6. 选择 **Create**,因为您将在 object type 创建*之后*生成并配置 action type。

6. Select **Create**, as you will generate and configure action types *after* object type creation.
在 Ontology Manager 中可以查看您草稿的 object type 之后,接下来您需要将 `Classification` 和 `Geoshape` 属性选为 ontology 中的 shared property type。选择 **Overview** 下方的 **Properties** 面板,然后按照以下步骤完成 shared property type 选择过程:

With your draft object type viewable in Ontology Manager, you will next select the `Classification` and `Geoshape` properties as shared property types in your ontology. Select the **Properties** panel beneath **Overview** and follow the steps below to complete the shared property type selection process:
> **✅ 成功**

> 如果您使用的数据集(用于支撑您的 object type)中*不*包含 `Classification` 属性,则您应该按照以下步骤 1 和 4 为您的 `Geoshape` 属性完成相应操作。
> **✅ 成功**

> If you are using a dataset to back your object type that does *not* contain a `Classification` property, then you should complete steps 1 and 4 below for your `Geoshape` property.
1. 从属性列表中选择 `Classification`,以在屏幕右侧启动 **Property editor** 窗口。

2. 更新 **Base type** 下拉菜单,使其分别包含 `Mandatory control` 和 `CBAC Marking`。

3. 配置该属性的 **Max Classification**。

1. Select `Classification` from your list of properties to launch the **Property editor** window on the right side of your screen.
2. Update the **Base type** dropdown menus to contain `Mandatory control` and `CBAC Marking`, respectively.
3. Configure the property's **Max Classification**.

> 📷 **[图片: 显示 Property editor 窗口,用户可以在其中将属性映射为 shared property type]**

> 📷 **[图片: The Property editor window is displayed, where a user can map properties as shared property types]**

> **⚠️ 警告**

> 如果您无法将 **Mandatory control** 选为 `Classification` 的 base type,请联系您的 Palantir Support,因为 **Mandatory control** 标记通常并非在所有 Foundry 注册中可用。
> **⚠️ 警告**

> Contact your Palantir Support if you are unable to select **Mandatory control** as the base type for `Classification`, as **Mandatory control** markings are not generally available across all Foundry enrollments.
4. 向下滚动至窗口底部的 **Shared property** 部分,使用下拉菜单将 `Classification` 分配为 shared property。

4. Scroll to the bottom of the window to the **Shared property** section and use the dropdown menu to assign `Classification` as a shared property.
![Assign a shared property through the Shared property section of the Property editor window.](/docs/resources/foundry/object-link-types/assign-classification-spt.png)
对您的 `Geoshape` 属性重复上述步骤 1 和 4,因为您*不*需要配置其 mandatory control 标记或 classification。

Repeat steps 1 and 4 above for your `Geoshape` property, as you will *not* need to configure its mandatory control markings or classification.
选择屏幕顶部的绿色 **Save** 按钮以将增量更改发布到您的 ontology,然后再继续操作。

Select the green **Save** button at the top of the screen to publish incremental changes to your ontology before proceeding.
如果您的 Foundry 注册包含 Map Rendering Service (MRS),则 ontology 中具有 geospatial property type 的 object type 会自动与 Gotham 集成,您可以继续[创建一个 action type 以在 Gaia 中启用 object creation](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia)。按照 [Gotham 集成文档](/docs/foundry/object-link-types/enable-gotham-integration/#how-to-check-if-your-enrollment-contains-mrs) 中的步骤检查您的注册是否包含 MRS。如果您的注册*不*包含 MRS,则[按照说明](/docs/foundry/object-link-types/enable-gotham-integration/#toggle-on-type-mapping-in-foundrys-ontology-manager)将 ontology 中的数据与 Gotham 集成。

If your Foundry enrollment contains Map Rendering Service (MRS), then object types in your ontology with a geospatial property type automatically integrate with Gotham, and you can proceed to [create an action type to enable object creation in Gaia](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia). Follow the steps [in the Gotham integration documentation](/docs/foundry/object-link-types/enable-gotham-integration/#how-to-check-if-your-enrollment-contains-mrs) to check if your enrollment contains MRS. If your enrollment does *not* contain MRS, then [follow the instructions](/docs/foundry/object-link-types/enable-gotham-integration/#toggle-on-type-mapping-in-foundrys-ontology-manager) to integrate data in your ontology with Gotham.
> **ℹ️ 注意**

> 有关 MRS 安装或功能的问题,请联系 Palantir Support。
> **ℹ️ 注意**

> Contact Palantir Support with questions about MRS installation or functionality.
### Create and configure an action type to enable object creation in Gaia
创建 object type 并确保其与 Gotham 集成后,请导航回 Ontology Manager 中的 **Overview** 窗口。在这里,创建一个 [action type](/docs/foundry/action-types/overview/),使用户能够从形状创建和编辑 object,并从 Gaia 配置其属性(例如 `Name` 和 `Category`)。

Once you create your object type and ensure it integrates with Gotham, navigate back to the **Overview** window in Ontology Manager. Here, create an [action type](/docs/foundry/action-types/overview/) that enables users to create and edit objects from shapes and configure their properties, such as `Name` and `Category`, from Gaia.
> **⚠️ 警告**

> 您的 Foundry 注册必须包含 MRS 才能在 Gaia 中编辑 Ontology object,因为此功能不适用于通过 type mapping 添加到 Gaia 中的 object。有关 MRS 安装或功能的问题,请联系 Palantir Support。
> **⚠️ 警告**

> Your Foundry enrollment must contain MRS to edit Ontology objects in Gaia, as this capability does not extend to objects added to Gaia through type mapping. Contact Palantir Support with questions about MRS installation or functionality.
按照以下步骤配置您的 action type:

Follow the steps below to configure your action type:
1. 在 Object Type 的 **Overview** 窗口中,从 **Action types** 部分选择 **New**,以启动 **Create a new action type** 弹出窗口。

1. Select **New** from the **Action types** section of your object type's **Overview** window to launch the **Create a new action type** pop-up window.
> **✅ 成功**

> 如果无法在 **Action types** 中选择 **New** 按钮,则可以在 **Datasources** 窗口中切换 Object Type 的 **Allow edits**。
> **✅ 成功**

> If you are unable to select the **New** button in **Action types**, then you can toggle on **Allow edits** on your object type in the **Datasources** window.
2. 在 **Object actions** 下选择 **Modify or create object**,然后选择 **Next**。

3. 从 **Or create a new object with** 下拉菜单中选择 **Auto-generated primary key**。

4. 选择 **Add property** 将所有现有的 Property 添加到 Action Type,然后选择 **Next** 来配置 Action Type 的元数据。

2. Select **Modify or create object** under **Object actions** before choosing **Next**.
3. Select **Auto-generated primary key** from the **Or create a new object with** dropdown menu.
4. Select **Add property** to add all your existing properties to the action type, then choose **Next** to configure your action type's metadata.
![The Create a new action type window is displayed, where a user can map action parameters used as action inputs.](/docs/resources/foundry/object-link-types/configure-create-or-modify-action-type-properties.png)
> **ℹ️ 注意**

> 仅当 restricted view 支撑您的 Object Type 时,才需要映射 `Classification` Property。
> **ℹ️ 注意**

> You will only need to map a `Classification` property if a restricted view backs your object type.
5. 命名您的 Action Type,并可选择输入描述以及更新其默认图标。

6. 选择可以执行该 Action 的 **Organization**、**Group** 或 **User**,然后选择 **Create**。

5. Name your action type, and optionally enter a description and update its default icon.
6. Select an **Organization**, **Group**, or **User** who may execute the action, then select **Create**.
选择屏幕顶部的绿色 **Save** 按钮,将增量更改发布到您的 Ontology,然后再继续。

Select the green **Save** button at the top of the screen to publish incremental changes to your ontology before proceeding.
接下来,您将按照以下步骤配置 Action Type 的 **Rules** 和 **Parameters**:

Next, you will configure your action type's **Rules** and **Parameters** by following the steps below:
1. 从屏幕左侧选择 **Rules**。

2. 通过选择 **Configure parameter** 旁边的箭头图标,验证 `Geoshape` Property 的配置。

* 确保 `Geoshape` Property 的类型为屏幕右侧 **Type** 下拉菜单中的 `Geoshape` 或 `String`。

* 确保在 **General** 面板中选择了 **Disabled** 选项,以使用户无法手动配置 `Geoshape` 的位置。

1. Select **Rules** from the left side of the screen.
2. Validate the `Geoshape` property's configurations by selecting the arrow icon next to **Configure parameter**.
* Ensure the `Geoshape` property's type is either `Geoshape` or `String` from the **Type** dropdown menu on the right side of the screen.
* Ensure the **Disabled** option is selected in the **General** panel so a user cannot manually configure the location of a `Geoshape`.
![Ontology Manager's Create object window is displayed, where a user can map properties in the Rules panel to create a rule.](/docs/resources/foundry/object-link-types/configure-create-object-type.png)
3. 从屏幕左侧的 **Form content** 面板中选择您的 `Classification` Property,并验证其 **Type** 是否为 `Mandatory control`。仅当 restricted view 支撑您的 Object Type 时,才需要配置 `Classification` Property。

4. 选择 **Back to Form**,然后通过选择 **Object Id** 面板最右侧的 **X** 图标,从 **Form content** 中删除 `Object Id`。Foundry 将自动为从 Gaia 创建的每个 Object 生成一个唯一 ID。

5. 选择屏幕顶部的绿色 **Save** 按钮,将 Action Type 的配置保存到 Ontology。

3. Select your `Classification` property from the **Form content** panel on the left side of your screen and verify that its **Type** is `Mandatory control`. You will only need to configure a `Classification` property if a restricted view backs your object type.
4. Select **Back to Form** and remove `Object Id` from **Form content** by selecting the **X** icon on the far right side of the **Object Id** panel. Foundry will automatically generate a unique ID for each object created from Gaia.
5. Select the green **Save** button at the top of your screen to save your action type's configurations to the Ontology.
### Implement the Gaia Geoshape Creatable interface
在 Ontology Manager 中创建和配置 Object Type 的最后一步是实现您[之前从 Marketplace 安装的](#gaia-geoshape-creatable-interface-from-the-gaia-app-store) Gaia Geoshape Creatable Interface。返回到 Object Type 的 **Overview** 页面,并按照以下步骤在将更改保存到 Ontology 之前实现 Interface:

The final step in creating and configuring your object type in Ontology Manager is to implement the Gaia Geoshape Creatable interface that you [previously installed from Marketplace](#gaia-geoshape-creatable-interface-from-the-gaia-app-store). Navigate back to your object type's **Overview** page and follow the steps below to implement the interface before saving changes to your ontology:
1. 导航到屏幕左侧 **Object Views** 下方的 **Interfaces** 窗口。

2. 选择 **Implement new interface** 并搜索 `Gaia Geoshape Creatable`,然后选择 **Next**。

3. 选择 **Choose an option** > **Replace existing**,以将 Ontology 的 `Geoshape` shared property type 映射到实现该 Interface 的 Object Type。

4. 选择 **Confirm** 以关闭 **Implement an interface** 窗口,并将新配置的 Interface **Save** 到您的 Ontology。

1. Navigate to the **Interfaces** window beneath **Object Views** on the left side of your screen.
2. Select **Implement new interface** and search for `Gaia Geoshape Creatable` before choosing **Next**.
3. Select **Choose an option** > **Replace existing** to map your ontology's `Geoshape` shared property type to the object type implementing the interface.
4. Select **Confirm** to close the **Implement an interface** window and **Save** the newly configured interface to your ontology.
![Ontology Manager's Interfaces window displays the Gaia Geoshape Creatable interface after it has been implemented on an object type.](/docs/resources/foundry/object-link-types/implemented-gaia-geoshape-creatable-interface.png)
## Create an object type that implements the Gaia Geopoint Creatable interface
要创建一个实现 Gaia Geopoint Creatable Interface 的 Object Type,您可以按照[上述 Gaia Geoshape Creatable Interface 的 Object Type 创建说明](#create-an-object-type-that-implements-the-gaia-geoshape-creatable-interface)中的相同步骤进行操作,但每个部分有以下区别:

To create an object type that implements the Gaia Geopoint Creatable interface, you can follow the same steps outlined in the [object type creation instructions for the Gaia Geoshape Creatable interface above](#create-an-object-type-that-implements-the-gaia-geoshape-creatable-interface) with the following distinctions in each section:
* [创建支撑 Object Type 的 restricted view](#create-an-object-type-backing-dataset-or-restricted-view)。

* 创建一个 `Geopoint` 列,而不是 `Geoshape` 列。

* [创建 Object Type 并确保它与 Gotham 集成](#create-an-object-type-and-ensure-it-integrates-with-gotham)。

* 在 Object Type 创建窗口中,确保 `Geopoint` 的 **Property** 为 geopoint。

* [配置 Action Type 以在 Gaia 中启用 Object 创建](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia)。

* 确保在 Action Type 的 **Parameters** 窗口中,`Geopoint` Property 的 **Type** 为 `Geopoint`。

* [实现 Gaia Geoshape Creatable Interface](#implement-the-gaia-geoshape-creatable-interface)。

* 搜索 `Gaia Geopoint Creatable` 而不是 `Gaia Geoshape Creatable` Interface。

* 在映射 Ontology 的 shared property types 时,为 `Geopoint` Property 选择 **Replace existing**,而不是为 `Geoshape` Property 选择。

* [Create an object type-backing restricted view](#create-an-object-type-backing-dataset-or-restricted-view).
* Create a `Geopoint` instead of `Geoshape` column.
* [Create an object type and ensure it integrates with Gotham](#create-an-object-type-and-ensure-it-integrates-with-gotham).
* In the object type creation window, ensure `Geopoint`'s **Property** is geopoint.
* [Configure an action type to enable object creation in Gaia](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia).
* Ensure your `Geopoint` property's **Type** is `Geopoint` in your action type's **Parameters** window.
* [Implement the Gaia Geoshape Creatable interface](#implement-the-gaia-geoshape-creatable-interface).
* Search for the `Gaia Geopoint Creatable` instead of the `Gaia Geoshape Creatable` interface.
* When mapping your ontology's shared property types, select **Replace existing** for the `Geopoint` instead of the `Geoshape` property.
## Create an object type that implements the MILSTD 2525C Symbol interface
> **⚠️ 警告**

> 与 Gaia Geoshape Creatable 和 Gaia Geopoint Creatable Interfaces 不同,您**必须**使用 restricted view 来支撑实现 MILSTD 2525C Symbol Interface 的 Object Type。
> **⚠️ 警告**

> Unlike the Gaia Geoshape Creatable and Gaia Geopoint Creatable interfaces, you **must** use a restricted view to back an object type that implements the MILSTD 2525C Symbol interface.
要创建一个实现 MILSTD 2525C Symbol Interface 的 Object Type,您可以按照[上述 Gaia Geoshape Creatable Interface 的 Object Type 创建说明](#create-an-object-type-that-implements-the-gaia-geoshape-creatable-interface)中的相同步骤进行操作,但每个部分有以下区别:

To create an object type that implements the MILSTD 2525C Symbol interface, you can follow the same steps outlined in the [object type creation instructions for the Gaia Geoshape Creatable interface above](#create-an-object-type-that-implements-the-gaia-geoshape-creatable-interface) with the following distinctions in each section:
* [创建 object type 支撑的 restricted view](#create-an-object-type-backing-dataset-or-restricted-view)。

* 您*只*需要创建 `Object ID`、`Classification` 和 `Title` 列。

* [创建 object type 并确保它与 Gotham 集成](#create-an-object-type-and-ensure-it-integrates-with-gotham)。

* 在 object type 创建窗口中，将 `Object ID` 设为 **Primary key**，将 `Title` 设为 **Title**。

* [Create an object type-backing restricted view](#create-an-object-type-backing-dataset-or-restricted-view).
* You will *only* need to create `Object ID`, `Classification`, and `Title` columns.
* [Create an object type and ensure it integrates with Gotham](#create-an-object-type-and-ensure-it-integrates-with-gotham).
* In the object type creation window, set `Object ID` as the **Primary key** and `Title` as the **Title**.
当 [配置 action type 以启用 object 创建](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia) 时，确保在选择 **Next** 之前，在 **Create a new action type** 窗口中至少映射 `Classification`、`Symbol Anchor Points` 和 `SIDC` properties。

When [configuring an action type to enable object creation](#create-and-configure-an-action-type-to-enable-object-creation-in-gaia), ensure you map *at least* the `Classification`, `Symbol Anchor Points`, and `SIDC` properties in the **Create a new action type** window before you select **Next**.
![The Create a new action type window is displayed for an object type implementing the MILSTD 2525C Symbol interface, where a user can map action parameters used as action inputs.](/docs/resources/foundry/object-link-types/configure-milsym-action-type-properties.png)
在继续之前，选择屏幕顶部的绿色 **Save** 按钮将增量更改发布到您的 ontology。

Select the green **Save** button at the top of the screen to publish incremental changes to your ontology before proceeding.
接下来，按照以下步骤配置您的 action type 的 **Rules** 和 **Parameters**：

Next, you will configure your action type's **Rules** and **Parameters** by following the steps below:
1. 从屏幕左侧选择 **Rules**。

2. 选择您 `Classification` property 右侧的箭头图标以 **Configure parameter**。

1. Select **Rules** from the left side of the screen.
2. Select the arrow icon to the right of your `Classification` property to **Configure parameter**.
![The Rules panel in an action type's creation window displays properties mapped as action type inputs.](/docs/resources/foundry/object-link-types/configure-milsym-action-type.png)
3. 在 **General** 部分中开启 **Disabled**，以确保创建的对象从您的 Gaia 地图继承其 classification 标记。

4. 在 **Set a parameter max classification** 下选择 **Add**，以确保 action type 的最大 classification 与 object type 的最大 classification 匹配。

3. Toggle on **Disabled** in the **General** section to ensure the object created inherits its classification markings from your Gaia map.
4. Select **Add** under **Set a parameter max classification** to ensure the action type's maximum classification matches the object type's maximum classification.
![The action form's Classification parameter is displayed, where a user can validate its Type, Disable its editing, and configure its maximum classification.](/docs/resources/foundry/object-link-types/configure-milsym-classification-parameter.png)
5. 选择屏幕顶部的绿色 **Save** 按钮，将 action type 发布到您的 ontology。

5. Select the green **Save** button at the top of the screen to publish the action type to your ontology.
> **⚠️ 警告**

> 由于 [目前不支持在 action 中使用 struct properties](/docs/foundry/object-link-types/structs-overview/#current-levels-of-support)，您将无法将 `Speed Modifier (Z)` 或 `Altitude/Depth Modifier (X)` properties 配置为 action type parameters。
> **⚠️ 警告**

> Since the [use of struct properties in actions is not currently supported](/docs/foundry/object-link-types/structs-overview/#current-levels-of-support), you will not be able to configure the `Speed Modifier (Z)` or `Altitude/Depth Modifier (X)` properties as action type parameters.
* [实现 Gaia Geoshape Creatable interface](#implement-the-gaia-geoshape-creatable-interface)。

* 搜索 `MILSTD 2525C Symbol` 而非 `Gaia Geoshape Creatable` interface。

* 映射 ontology 的 shared property types 时，为您的 `Classification` property 选择 **Replace existing**，并为其他 properties 选择 **Create edit-only property**。

* [Implement the Gaia Geoshape Creatable interface](#implement-the-gaia-geoshape-creatable-interface).
* Search for the `MILSTD 2525C Symbol` instead of the `Gaia Geoshape Creatable` interface.
* When mapping your ontology's shared property types, select **Replace existing** for your `Classification` property and **Create edit-only property** for the others.
## Register your ontology and its types
现在，您已拥有实现了 Gaia Geoshape Creatable、Gaia Geopoint Creatable 和 MILSTD 2525C Symbol interfaces 的 object types，并包含相应的 action types，使用户能够配置从绘制的形状、放置的点和在 Gaia 地图上配置的战术图形创建的对象。接下来，您将根据您的注册情况，在 Gaia 的 admin application 或 [Control Panel](/docs/foundry/administration/control-panel/) extension 中注册您的 ontology、object types 和 action types。

Now, you have object types that implement the Gaia Geoshape Creatable, Gaia Geopoint Creatable, and MILSTD 2525C Symbol interfaces and contain accompanying action types that enable a user to configure objects they create from shapes drawn, points dropped, and tactical graphics configured on a Gaia map. Next, you will register your ontology, object types, and action types either in Gaia's admin application or [Control Panel](/docs/foundry/administration/control-panel/) extension, depending on your enrollment.
> **ℹ️ 注意**

> 要访问 Gaia 的 admin application，您必须是 platform administrator。要访问 Gaia 的 Control Panel extension，您必须被授予 **Organization administrator** 角色。
> 如果您无法访问 admin application 或 Control Panel extension，请联系 Palantir Support 询问有关访问权限的问题。
> **ℹ️ 注意**

> To access Gaia's admin application, you must be a platform administrator. To access Gaia's Control Panel extension, you must be granted the **Organization administrator** role.
> Contact Palantir Support with questions about access to the admin application or Control Panel extension if you are unable to access either.
要注册您的 ontology、object types 和 action types，请启动 Gaia 的 admin application 或 Control Panel extension 并按照以下步骤操作：

To register your ontology, object types, and action types, launch Gaia's admin application or Control Panel extension and follow the steps below:
1. 找到 **Ontology Config** (admin application)/**Ontology** (Control Panel extension) 面板并验证您的 ontology 配置。如果您的 ontology 尚未配置，请选择面板左侧的切换按钮，将 **Ontology Config**/**Ontology** 设置为 `overridden` (admin application)/`Override` (Control Panel extension)。

2. 在 **Ontology RID** 和 **API Name** 文本框中输入您的 ontology 的 RID 和 API 名称。

1. Locate the **Ontology Config** (admin application)/**Ontology** (Control Panel extension) panel and verify your ontology's configuration. If your ontology is not configured, select the toggle on the left side of the panel to set **Ontology Config**/**Ontology** to `overridden` (admin application)/`Override` (Control Panel extension).
2. Enter your ontology's RID and API name into the **Ontology RID** and **API Name** text boxes.
> **✅ 成功**

> 要定位并复制您的 ontology 的 RID 和 API 名称，请导航到 Ontology Manager，并从其左侧面板底部选择 **Ontology configuration** 以启动 **Ontology metadata** 窗口。
> **✅ 成功**

> To locate and copy your ontology's RID and API name, navigate to Ontology Manager and choose **Ontology configuration** from the bottom of its left panel to launch the **Ontology metadata** window.
![The Gaia admin application's and Control Panel extension's Ontology Config panel.](/docs/resources/foundry/object-link-types/gaia-admin-app-ontology-config.png)
3. 找到 **Foundry Object Creation Config** 面板并选择 **Show** (admin application)/**Override** (Control Panel extension)。

4. 在您注册的现有 object 和 action type 列表底部选择 **Add**。

5. 将所有三个 object types 及其支持的 action types 的 RID 分别复制并粘贴到三个单独的 **Object type rid** 和 **Action type rid** 文本框中。

6. 选择右上角功能区中的 **Preview and save** (admin application)/右下角的 **Save for {Organization}** (Control Panel extension)。

3. Locate the **Foundry Object Creation Config** panel and select **Show** (admin application)/**Override** (Control Panel extension).
4. Select **Add** at the bottom of your enrollment's existing object and action type list.
5. Copy and paste the RIDs for all three object types and their supporting action types into three separate **Object type rid** and **Action type rid** text boxes, respectively.
6. Select **Preview and save** in the top right ribbon (admin application)/**Save for {Organization}** in the bottom right corner (Control Panel extension).
![The Gaia admin application's and Control Panel extension's Foundry Object Creation Config panel.](/docs/resources/foundry/object-link-types/gaia-admin-app-foundry-object-creation-config.png)
您可以在 Ontology Manager 的 **Overview** 窗口中访问 object type 的 RID。选择剪贴板图标以复制 RID。此外，您可以通过在 **Overview** 窗口的 **Action types** 部分选择 **Create {object type name}** 来访问 action type 的 RID。Action type 的 RID 也可以通过剪贴板图标进行复制。

You can access your object type's RID from the **Overview** window in Ontology Manager. Select the clipboard icon to copy the RID. Additionally, you can access your action type's RID by selecting **Create {object type name}** in the **Action types** section of the **Overview** window. The action type's RID can also be copied through the clipboard icon.
![You can copy the RID of both your object type and action type from the Overview window of Ontology Manager.](/docs/resources/foundry/object-link-types/combined-object-action-rid-copy.png)
接下来，您将启动 Gotham 的 Gaia 应用程序，通过使用其 **Add to map** 菜单，从您在地图上绘制的形状、放置的点和配置的战术图形创建 object。

Next, you will launch Gotham's Gaia application to create objects from shapes you draw, points you drop, and tactical graphics you configure on a map using its **Add to map** menu.
### Draw a new shape on your Gaia map and tag it to an object type
> **⚠️ 警告: 关于国际日期变更线的当前限制**

> 虽然您可以在 Gaia 地图上创建跨越第 180 度子午线（即反子午线）的地图注释，但您无法绘制以此方式跨越的标记为 Foundry object 的形状。
> 如有关于注释创建、渲染或 Gaia 在 Gotham 中提供的其他文档的问题，请联系 Palantir Support。
> **⚠️ 警告: Current limitations around the International Date Line**

> While you can create map annotations that cross the 180th meridian, or antimeridian, on a Gaia map, you cannot draw shapes tagged as Foundry objects that do so.
> Contact Palantir Support with questions about annotation creation, rendering, or Gaia's additional documentation present in Gotham.
打开 Gaia 地图后，从地图左上角区域的菜单中选择 object 图标，以从 **Draw annotation** 模式切换到 **Create object** 模式。

With your Gaia map open, select the object icon from the menu in the top left region of your map to switch from **Draw annotation** to **Create object** mode.
![Gaia's toolbar is displayed.](/docs/resources/foundry/object-link-types/select-object-map-tool-bar.png)
接下来，从同一菜单的右侧选择要绘制的形状。完成形状绘制后，**Create shape** 窗口将出现在 Gaia 的左侧面板中。请按照以下步骤配置您的形状并将其作为 object 保存到您的 ontology 中：

Next, select a shape to draw from the right side of the same menu. When you finish drawing your shape, the **Create shape** window will appear in Gaia's left panel. Follow the steps below to configure your shape and save it to your ontology as an object:
1. 从 **Object type** 下拉菜单中搜索并选择您的 object。如果您从地图画布上工具栏的下拉菜单中选择了 object type，那么 Gaia 将自动使用该值填充 **Create shape** 的下拉菜单。

2. 在选择 **Finish** 之前，在 action 表单中完成您的 object 的必填字段，例如 `Category` 和 `Name`。

1. Search for and select your object from the **Object type** dropdown menu. If you selected an object type from the tool bar's dropdown menu on your map canvas, then Gaia will automatically populate the **Create shape**'s dropdown menu with that value.
2. Complete the required fields in the action form, such as `Category` and `Name`, for your object before you select **Finish**.
![A polygon is drawn on a Gaia map, where a user can geotag it to an object type.](/docs/resources/foundry/object-link-types/draw-polygon.png)
将形状保存为 object 后，它将作为 Gaia 左侧面板中的 **Layers** 之一进行渲染。您可以选择 object 的名称以在屏幕右侧启动 **Selection** 面板，在该面板中您可以查看其 properties 并自定义其外观。

Once you save your shape as an object, it will render as one of the **Layers** in Gaia's left panel. You can select the object's name to launch the **Selection** panel on the right side of your screen, where you can view its properties and customize its appearance.
![Users can view a shape's object data on a Gaia map after it is drawn.](/docs/resources/foundry/object-link-types/gaia-map-drawn-object-view.png)
您还可以在 Foundry 的 [Object Explorer](/docs/foundry/object-explorer/overview/) 中查看您的 object。

You can also view your object in Foundry's [Object Explorer](/docs/foundry/object-explorer/overview/).
![Users can view their drawn objects within Foundry's Object Explorer.](/docs/resources/foundry/object-link-types/view-drawn-object-in-foundry-oe.png)
#### Edit an existing shape object
要编辑现有的形状 object，请将光标悬停在左侧面板中的 object 上，然后选择 **Edit selection** 以启动 **Edit shape** 窗口，您也可以通过在地图上双击 object 来访问该窗口。

To edit an existing shape object, hover your cursor over the object in the left panel and choose **Edit selection** to launch the **Edit shape** window, which you can also access by double-clicking the object on your map.
![Users can edit an object on their Gaia map by selecting the pencil icon to launch the Edit shape window in the left panel.](/docs/resources/foundry/object-link-types/edit-object.png)
选择并拖动任何顶点以调整形状，或选择形状边界内的点以将形状拖动到地图上的另一个位置。完成更改后，在 **Edit shape** 窗口底部选择 **Finish**。

Select and drag any vertex to adjust the shape, or select a point within the shape's boundary to drag the shape to another location on your map. When you are finished making changes, choose **Finish** at the bottom of the **Edit shape** window.
### Drop a new point on your Gaia map and tag it to an object type
打开 Gaia 地图后，选择向下箭头以渲染 symbol **Search** 菜单，您可以在其中选择可用的 symbol 以放置在地图上的任何位置。如果您选择了一个可用的 **Tactical Graphics** symbol，那么您将只能在实现了 [MILSTD 2525C Symbol interface](#create-an-object-type-that-implements-the-milstd-2525c-symbol-interface) 的 object type 内创建 object。Gaia 将根据您地图的坐标系偏好自动填充 **Coordinates** 输入框。

With your Gaia map open, select the down arrow to render the symbol **Search** menu, where you can choose an available symbol to drop anywhere on your map. If you select one of the available **Tactical Graphics** symbols, then you will only be able to create an object within an object type that implements the [MILSTD 2525C Symbol interface](#create-an-object-type-that-implements-the-milstd-2525c-symbol-interface). Gaia will automatically populate the **Coordinates** input box based on your map's coordinate system preference.
![The symbol selection in Gaia's tool bar is displayed.](/docs/resources/foundry/object-link-types/create-geopoint-from-tool-bar.png)
> **✅ 成功**

> 从 Gaia 顶部功能区选择 **File** > **Preferences** > **Coordinate system** 以更新默认坐标系。
> **✅ 成功**

> Select **File** > **Preferences** > **Coordinate system** from Gaia's top ribbon to update the default coordinate system.
**Create symbol** 窗口将出现在 Gaia 的左侧面板中，您可以在其中搜索并选择实现了 Gaia Geopoint Creatable interface 的 object type。接下来，在为您的 object 输入 **Title** 之前，可选择性地调整您的 geopoint 的 **Bearing (mag)**。选择 **Finish** 以将放置的 symbol 作为 object 保存到您的 ontology 中。

The **Create symbol** window will appear in Gaia's left panel, where you can search for and select your object type that implements the Gaia Geopoint Creatable interface. Next, optionally adjust the **Bearing (mag)** of your geopoint before entering a **Title** for your object. Choose **Finish** to save the dropped symbol to your ontology as an object.
将 geopoint 保存为 object 后，您可以与新的地图图层进行交互，并以[与在地图上绘制的形状相同的方式](#draw-a-new-shape-on-your-gaia-map-and-tag-it-to-an-object-type)在 Foundry 的 Object Explorer 中查看该 object。

Once you save your geopoint as an object, you can interact with the new map layer and view the object in Foundry's Object Explorer [in the same manner you can for a shape drawn on your map](#draw-a-new-shape-on-your-gaia-map-and-tag-it-to-an-object-type).
#### Edit an existing geopoint object
您可以[以与在地图上绘制的形状相同的方式](#edit-an-existing-shape-object)编辑现有的 geopoint object。

You can edit an existing geopoint object [in the same manner you can for a shape drawn on your map](#edit-an-existing-shape-object).
### Configure a tactical graphic on your Gaia map and tag it to an object type
> **⚠️ 警告**

> 您的 Foundry 注册必须包含 MRS 才能将战术图形标记到 object type。有关 MRS 安装或功能的问题，请联系 Palantir Support。
> **⚠️ 警告**

> Your Foundry enrollment must contain MRS to tag a tactical graphic to an object type. Contact Palantir Support with questions about MRS installation or functionality.
[类似于添加新地理点并将其标记为 object](#drop-a-new-point-on-your-gaia-map-and-tag-it-to-an-object-type)，选择向下箭头以渲染 symbol **Search** 菜单，您可以在其中选择可用的战术图形放置在地图上的任意位置。在 **Search symbols...** 输入框中输入您所需的战术图形名称，例如 `Brigade Support Area`。

[Similar to adding a new geopoint to tag as an object](#drop-a-new-point-on-your-gaia-map-and-tag-it-to-an-object-type), select the down arrow to render the symbol **Search** menu, where you can choose an available tactical graphic to drop anywhere on your map. Type the name of your desired tactical graphic in the **Search symbols...** input box, such as `Brigade Support Area`.
![Gaia's symbol search window enables a user to search for a symbol or tactical graphic to add to their map.](/docs/resources/foundry/object-link-types/search-for-tactical-graphic.png)
**Create symbol** 窗口将出现在 Gaia 的左侧面板中，您可以按照上述相同的 [shape creation instructions](#draw-a-new-shape-on-your-gaia-map-and-tag-it-to-an-object-type) 将您的战术图形添加到地图并将其标记到一个 object type。

The **Create symbol** window will appear in Gaia's left panel, and you can follow the same [shape creation instructions](#draw-a-new-shape-on-your-gaia-map-and-tag-it-to-an-object-type) above to add your tactical graphic to the map and tag it to an object type.
![A Gaia map displays a tactical graphic drawn and saved on a map canvas.](/docs/resources/foundry/object-link-types/draw-tactical-graphic.png)
#### Edit an existing tactical graphic object
您可以按照上述 [shape object editing instructions](#edit-an-existing-shape-object) 编辑现有的战术图形 object。

You can edit an existing tactical graphic object by following the [shape object editing instructions above](#edit-an-existing-shape-object).
### Promote an annotation to an object
在 Gaia 中，*annotation* 是本地于您当前地图的 shape、point 或 symbol。您可以将地图上的 annotations 提升为您 ontology 中的 objects，以便在其他用户创建的其他地图上使用，前提是这些用户可以访问其 object type。

In Gaia, an *annotation* is a shape, point, or symbol that is local to your current map. You can promote annotations on your map to objects in your ontology for use on other maps created by other users who can access their object type.
要将现有的 annotation 标记为 object，请在地图上双击该 annotation，或将光标悬停在左侧面板 **Layers** 标签页中 annotation 的铅笔图标上，以启动 shape、point 或 symbol 编辑窗口。接下来，选择 **Promote to object**，从 **Object type** 下拉菜单中选择您的 object type，并在 shape、point 或 symbol 编辑窗口中完成 action form。

To tag an existing annotation as an object, double-click the annotation on your map or hover your cursor over the annotation's pencil icon in the **Layers** tab of the left panel to launch the shape, point, or symbol edit window. Next, select **Promote to object**, choose your object type from the **Object type** dropdown menu, and complete the action form in the shape, point, or symbol edit window.
![A Gaia map displays an annotation that a user promotes to an object through the left panel.](/docs/resources/foundry/object-link-types/promote-annotation.png)
要了解更多关于可用于将数据从您的 ontology 添加 *到* Gotham 的各种方法，请查看现有的 [geospatial data integration documentation](/docs/foundry/geospatial/add-ontology-data-to-gaia/)。

To learn more about the various methods you can use to add data *from* your ontology *to* Gotham, review the existing [geospatial data integration documentation](/docs/foundry/geospatial/add-ontology-data-to-gaia/).