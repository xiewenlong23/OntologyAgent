<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/enable-gotham-integration/
---
# Enable Gotham integration through type mapping
> **ℹ️ 注意: Note**

> 如果您的注册包含 Map Rendering Service (MRS)，则*无需*完成 type mapping 流程即可启用 Gotham 集成。您可以 [从 Gaia 创建新的 ontology 对象](/docs/foundry/object-link-types/create-ontology-objects-from-gaia/) 或 [向 Gotham 添加现有对象](/docs/foundry/geospatial/add-ontology-data-to-gaia/)，无需额外配置。请按照以下说明检查您的注册是否包含 MRS。
> 如有关于 MRS 可用性、安装或其 Gotham 中其他文档的问题，请联系 Palantir Support。
> **ℹ️ 注意: Note**

> If your enrollment contains Map Rendering Service (MRS), then you do *not* need to complete the type mapping process to enable Gotham integration. You can [create new ontology objects from](/docs/foundry/object-link-types/create-ontology-objects-from-gaia/) or [add existing objects to](/docs/foundry/geospatial/add-ontology-data-to-gaia/) Gotham without additional configuration. Follow the instructions below to check if your enrollment contains MRS.
> Contact Palantir Support with questions about MRS availability, installation, or its additional documentation present in Gotham.
## How to check if your enrollment contains MRS
1. 启动 [Quicksearch](/docs/foundry/compass/quicksearch/) 以搜索并选择 **Gaia Home**。

2. 打开现有的或创建一个新的 Gaia map。

3. 从左侧面板中选择 **Data sources**。

4. 在 **Find...** 搜索栏中搜索 `Object search`。

1. Launch [Quicksearch](/docs/foundry/compass/quicksearch/) to search for and select **Gaia Home**.
2. Open an existing or create a new Gaia map.
3. Select **Data sources** from the left panel.
4. Search for `Object search` in the **Find...** search bar.
如果您能够找到并选择 **Object search**，则说明您的注册包含 MRS。

If you are able to locate and select **Object search**, then your enrollment contains MRS.
![The Data sources tab in Gaia's left panel displays Object search as an indicator of MRS installation.](/docs/resources/foundry/object-link-types/gaia-mrs-installation-indicator.png)
***
## Use type mapping to create a unified representation of your ontology
Type mapping 使您的 ontology 在 Foundry 和 Gotham 之间实现统一表示，您可以在 Foundry 的 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 应用中对其进行管理。您可以根据现有的 Foundry object type、property type 和 shared property type 创建新的 Gotham type，这些 type 将随着您的 ontology 发展而保持同步。完成 type mapping 流程后，Gotham 将能够通过 [Object Set Service](/docs/foundry/object-backend/overview/#object-set-service-oss)（一个支持 object data 搜索、过滤、聚合和加载的 Foundry 后端服务）来查询 Foundry object type 及其元数据。

Type mapping enables a unified representation of your ontology across Foundry and Gotham that you manage within Foundry's [Ontology Manager](/docs/foundry/ontology-manager/overview/) application. You can create new Gotham types based on existing Foundry object types, property types, and shared property types which remain synchronized as your ontology evolves over time. After completing the type mapping process, Gotham will be able to query Foundry object types and their metadata through the [Object Set Service](/docs/foundry/object-backend/overview/#object-set-service-oss) - a Foundry backend service which supports object data searching, filtering, aggregating, and loading.
> **ℹ️ 注意: Note**

> Type mapping 仅适用于同时使用 Foundry 和 Gotham 的注册，并且必须由平台管理员启用后才能使用。一旦为某个 Foundry Ontology 启用，type mapping 将无法被禁用。每个 Gotham 安装仅能有一个 Foundry Ontology 启用 type mapping。如需有关 type mapping 启用的帮助，请联系 Palantir Support。
> **ℹ️ 注意: Note**

> Type mapping is only available for enrollments using both Foundry and Gotham and must be enabled by a platform administrator before use. Once enabled for a Foundry Ontology, type mapping cannot be disabled. Only one Foundry Ontology per Gotham install can have type mapping enabled. Contact Palantir Support for assistance with type mapping enablement.
### When to type map object types in your ontology
[请按照以下说明操作](#toggle-on-type-mapping-in-foundrys-ontology-manager)，如果您的注册不 [包含 MRS](#how-to-check-if-your-enrollment-contains-mrs) 且以下任一条件为真，请在 Ontology Manager 中对 object type 进行 type mapping：

[Follow the instructions below](#toggle-on-type-mapping-in-foundrys-ontology-manager) and type map object types in Ontology Manager if your enrollment does not [contain MRS](#how-to-check-if-your-enrollment-contains-mrs) and any of the conditions below are true:
* 您计划使用不属于 [tactical graphic](/docs/foundry/object-link-types/create-ontology-objects-from-gaia/#configure-a-tactical-graphic-on-your-gaia-map-and-tag-it-to-an-object-type) 或 [MIL-STD 2525 symbol](/docs/defense-osdk/api/common/interfaceTypes/com-palantir-ontology-defense-types-mil2525CSymbol/) 的自定义 symbology。是否使用 type mapping，均支持 [Blueprint ↗](https://blueprintjs.com/) symbols。

* 您计划使用 [Geotracker](/docs/foundry/geospatial/types-of-geospatial-and-geotemporal-data/#geotracker) 在 Gaia map 上跟踪实体的位置。

* 您计划配置 [search templates](/docs/foundry/geospatial/add-ontology-data-to-gaia/#create-a-search-template)、[function-backed Enterprise Map Layer (EML)](/docs/foundry/geospatial/add-ontology-data-to-gaia/#use-a-function-backed-enterprise-map-layer) 或 [versioned object set-backed EML](/docs/foundry/geospatial/add-ontology-data-to-gaia/#use-a-versioned-object-set-backed-enterprise-map-layer)，以将来自 ontology 的 data 添加到 Gaia。

* You plan to use custom symbology that is not present as a [tactical graphic](/docs/foundry/object-link-types/create-ontology-objects-from-gaia/#configure-a-tactical-graphic-on-your-gaia-map-and-tag-it-to-an-object-type) or [MIL-STD 2525 symbol](/docs/defense-osdk/api/common/interfaceTypes/com-palantir-ontology-defense-types-mil2525CSymbol/). [Blueprint ↗](https://blueprintjs.com/) symbols are supported with or without type mapping.
* You plan to use [Geotracker](/docs/foundry/geospatial/types-of-geospatial-and-geotemporal-data/#geotracker) to track an entity's location on a Gaia map.
* You plan to configure [search templates](/docs/foundry/geospatial/add-ontology-data-to-gaia/#create-a-search-template), a [function-backed Enterprise Map Layer (EML)](/docs/foundry/geospatial/add-ontology-data-to-gaia/#use-a-function-backed-enterprise-map-layer), or a [versioned object set-backed EML](/docs/foundry/geospatial/add-ontology-data-to-gaia/#use-a-versioned-object-set-backed-enterprise-map-layer) to add data from your ontology to Gaia.
## Toggle on type mapping in Foundry's Ontology Manager
要将 Foundry Ontology 中的 data 与 Gotham 集成，您首先需要按照以下步骤在 Foundry 的 Ontology Manager 中为您感兴趣的 object type 启用 type mapping：

To integrate data in your Foundry Ontology with Gotham, you will first need to toggle on type mapping for your object type of interest within Foundry's Ontology Manager by following the steps below:
1. 从主屏幕启动 Ontology Manager。

2. 找到并选择您需要进行 type mapping 的 object type。

3. 在 object type 左侧面板中选择 **Capabilities**。

4. 向下滚动到 **Gotham Integration** 面板，启用 `Allow objects of this type to be accessed from Gotham applications`。

1. Launch Ontology Manager from your home screen.
2. Locate and select your object type to type map.
3. Select **Capabilities** within the object type's left-hand panel.
4. Scroll down to the **Gotham Integration** panel and toggle on `Allow objects of this type to be accessed from Gotham applications`.
![A user can toggle on Gotham Integration for an Object Type from Foundry's Ontology Manager application.](/docs/resources/foundry/object-link-types/enable-gotham-mapping.png)
> **ℹ️ 注意: Note**

> Type mapped objects 必须包含 `geopoint` property 才能在 Gaia map 上显示。该 property 可以是 object type 底层 dataset 原生的，也可以是通过 Pipeline Builder 的 [create Ontology geopoint](/docs/foundry/pb-functions-expression/createOntologyGeopointV1/) 转换功能从经纬度对或 `geopoint` 派生的。
> **ℹ️ 注意: Note**

> Type mapped objects must contain a `geopoint` property to display on a Gaia map. The property can be native to the object type's backing dataset(s) or derived from a latitude/longitude pair or `geopoint` using Pipeline Builder's [create Ontology geopoint](/docs/foundry/pb-functions-expression/createOntologyGeopointV1/) transform feature.
## Configure an object type's parent category and Gotham property types
启用 **Gotham Integration** 后，您可以按照以下步骤从现有 Foundry object type 创建一个新的 Gotham object type，指定该 object type 的 **Parent category**，并配置其 **Property types**：

Once you toggle on **Gotham Integration**, you can follow the steps below to create a new Gotham object type derived from an existing Foundry object type, specify the object type's **Parent category**, and configure its **Property types**:
1. 在 **Gotham Integration** 的 **Object type** 部分中选择 **Create a new object type**，以根据现有 Foundry object type 在 Gotham 中创建一个新的 object type。

2. 通过在 `Entity`（例如人员、组织或车辆）、`Event`（例如航班、会议或音乐会）或 `Document`（例如 PDF 文件、文本文档或报告）之间进行选择，根据您的用例确定新 object type 在 Gotham 中的 **Parent category**。

3. 使用 **Property types** 部分将 Foundry object type properties 映射到 Gotham — property 可以是 shared 的或 cloned 到 Gotham ontology 的。完成对给定 property 的配置后，您将在该 property 名称旁边看到一个蓝色的 `Mapped` 标签。

* `Do not map property to Gotham` 是默认选项 — 您未映射的 Foundry properties 不会传播到 Gotham ontology。

* `Assign to shared property` 使您能够选择一个*现有* shared property 进行映射。

* `Promote to shared property` 会创建一个供其他 objects 使用的*新* shared property。

* `Create a local clone of the property in Gotham` 在 Gotham 中创建所选 property 的副本，该副本与其应用兼容。

1. Select **Create a new object type** within the **Object type** section of **Gotham Integration** to create a new object type in Gotham from an existing Foundry object type.
2. Identify the **Parent category** of the new object type in Gotham by selecting between `Entity` (such as a person, organization, or vehicle), `Event` (such as a flight, meeting, or concert), or `Document` (such as a PDF file, text document, or report) based on your use case.
3. Use the **Property types** section to map Foundry object type properties to Gotham - a property can be shared or cloned into the Gotham ontology. You will see a blue `Mapped` tag next to the property's name once you complete that configuration on a given property.
* `Do not map property to Gotham` is the default option - Foundry properties you do not map will not propagate in the Gotham ontology.
* `Assign to shared property` enables you to select an *existing* shared property to map against.
* `Promote to shared property` creates a *new* shared property for use by other objects.
* `Create a local clone of the property in Gotham` creates a duplicate of the selected property in Gotham that is compatible with its applications.
> **ℹ️ 注意**

> Foundry 会自动对所有 shared properties 进行 type mapping，以使其在 Gotham 中可用。
> **ℹ️ 注意**

> Foundry automatically type maps all shared properties to make them available in Gotham.
4. 选择屏幕顶部 ribbon 右侧的绿色 **Save** 按钮并进行查看。

5. 查看对您的 object type 所做的更改，然后选择 **Save to ontology**。

4. Select the green **Save** button on the right side of the top ribbon of your screen and review.
5. Review the changes made to your object type and select **Save to ontology**.
![A user can create a new object type or take over an existing when integrating their Foundry and Gotham ontology using a Criteria panel which enables them to select the object type's parent category.](/docs/resources/foundry/object-link-types/ontology-manager-gotham-integration-view.png)
将对 Ontology 所做的更改保存后，向上滚动至 object type **Capabilities** 页面中的 **Gotham Integration** 部分。您现在将看到分配给该 object type 的 `Gotham URI`，并能够查看 Gotham 所报告的 `Installation status`。

After you save your changes to the Ontology, scroll back up to the **Gotham Integration** section of the **Capabilities** page of your object type. You will now see a `Gotham URI` assigned to the object type and be able to view the `Installation status` reported by Gotham.
Foundry 的 Ontology Manager 将显示以下安装状态之一：

Foundry's Ontology Manager will display one of the following installation statuses:
* `Ready to integrate`：Object Type 已准备好进行 type mapping，以启用 Gotham 集成。

* `Installation in progress`：Object Type 的安装过程正在进行中。

* `Installation complete`：安装过程已完成，因此该 Object Type 可在 Gotham 中使用。

* `Installation failed: {failureMessage}`：该 Object Type 的安装至少失败过一次，将在下次安装运行时重试。`{failureMessage}` 概述了失败原因。常见的安装失败包括：

* *Live reindex*：如果 Gotham 上正在运行 live reindex，则无法更新 Ontology。在此期间不会暂存更改，安装将失败，并在 live reindex 完成后自动重新运行。

* *Required types are not installed*：要使 Object Type 成功安装，必须完成所有相关 property 的安装（即 mappings），包括 shared property types。

* *Other ontology updates*：如果有 ontology 更新同时运行，则 type mapper 将无法更新 ontology，并将自动重新运行。

* `Ready to integrate`: An object type is ready for type mapping to enable Gotham integration.
* `Installation in progress`: The object type's installation process is underway.
* `Installation complete`: The installation process is complete, so the object type is available for use in Gotham.
* `Installation failed: {failureMessage}`: The object type's installation failed at least once and will be retried on the next installation run. The `{failureMessage}` outlines the reason for failure. Common installation failures include:
* *Live reindex*: If there is a live reindex running on Gotham, the ontology cannot be updated. Instead of staging changes during this time, the installation will fail and rerun automatically once the live reindex finishes.
* *Required types are not installed*: For an object type's successful installation, all related property installations - or mappings - must be completed, including shared property types.
* *Other ontology updates*: If there are ontology updates running concurrently, then the type mapper will not be able to update the ontology and will rerun automatically.
一旦您的 Object Type 的安装状态显示为 `Installation complete`，您将能够在 Gotham 的 applications 中搜索并使用您的 Object Type。

Once your object type's installation status reads `Installation complete`, you will be able to search for and use your object type in Gotham's applications.
要在 Gotham 中弃用（deprecate）一个 type mapped object type，您可以在 Foundry 的 Ontology Manager 中删除该 Object Type。在 Foundry 中删除后，相应的 Object Type 及其 property types 将无法在 Gotham 中访问，也无法供其 applications 使用。

To deprecate a type mapped object type in Gotham, you can delete the object type in Foundry's Ontology Manager. Once deleted in Foundry, the corresponding object type and its property types will not be accessible in Gotham or available to its applications.
> **ℹ️ 注意**

> Gotham 模拟了 Foundry 数据集的安全性和标记（markings），这意味着通过 type mapping 在 Gotham 中提供的 Foundry 数据将沿用相同的访问控制和分类。
> **ℹ️ 注意**

> Gotham models Foundry dataset security and markings, meaning that Foundry data made available in Gotham through type mapping carries over the same access controls and classification.