<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/overview/
---
# Ontology Manager
**Ontology Manager**（有时称为 Ontology Management Application 或 OMA）使您能够构建和维护组织的 Ontology。您可以将 Ontology Manager 用于与 Ontology 相关的各种活动，从创建新的 object type 和定义新的 action type，到将数据连接到 Ontology，以及调查数据是否在用户应用程序中更新。

**Ontology Manager** (sometimes called the Ontology Management Application, or OMA) enables you to build and maintain your organization’s Ontology. You can use Ontology Manager for a wide range of activities related to your Ontology, from creating a new object type and defining a new action type, to connecting data to the Ontology, and investigating whether data is updating in user applications.
## Accessing the application
您可以通过以下三种不同的方式访问该应用程序：

You can access the application in three different ways, by either:
* 从 Workspace 侧边栏的 **Apps** 部分选择 **Ontology Manager** 图标；

* 在 Data Lineage 中右键单击 object type，然后选择 **Configure object type**；或者

* 将 `/workspace/ontology` 添加到 Foundry 主页 URL 的末尾（例如，`https://example.website.com/workspace/ontology`）。

* Selecting the **Ontology Manager** icon from the Workspace sidebar’s **Apps** section;
* Right-clicking on an object type in Data Lineage and selecting **Configure object type**; or
* Adding `/workspace/ontology` to the end of your Foundry home page URL (for instance, `https://example.website.com/workspace/ontology`).
## User interface
Ontology Manager 界面分为以下元素，这些元素将在整个文档中被引用：

The Ontology Manager interface is divided into the following elements that you will see referenced throughout the documentation:
* [Ontology Manager navigation](#ontology-manager-navigation)
* [Discover view](#discover)
* [Object type view](#object-type-view)
* [Property editor view](#property-editor-view)
* [Link type view](#link-type-view)
* [Action type view](#action-type-view)
* [Function type view](#function-type-view)
* [Ontology Manager navigation](#ontology-manager-navigation)
* [Discover view](#discover)
* [Object type view](#object-type-view)
* [Property editor view](#property-editor-view)
* [Link type view](#link-type-view)
* [Action type view](#action-type-view)
* [Function type view](#function-type-view)
### Ontology Manager navigation
Ontology Manager 中两个持续存在的元素是顶部栏和侧边栏。顶部栏和侧边栏作为导航元素，提供对应用程序内各种功能、特性和部分的直观访问。

The two persisting elements of Ontology Manager are the top bar and the sidebar. The top bar and sidebar serve as navigation elements, providing intuitive access to various features, functionalities, and sections within the application.
顶部栏具有三个主要功能。它允许用户搜索 Ontology 资源、创建新的 Ontology 资源，以及在分支之间导航或创建新分支。

The top bar has three main functionalities. It allows users to search for Ontology resources, create new Ontology resources, and navigate between or create new branches.
侧边栏提供了对 Ontology Manager 内不同资源、页面或应用程序的便捷导航。

The sidebar provides easy navigation to different resources, pages, or applications within Ontology Manager.
![Ontology Manager annotated view.](/docs/resources/foundry/ontology-manager/oma-navigation-annotated.png)
### Discover
Discover 视图提供了一个高度可自定义的着陆页，可根据您的偏好进行定制。默认情况下，Discover 视图展示收藏的 object types、最近查看的 object types 以及收藏的 groups。

The Discover view offers a highly customizable landing page tailored to your preferences. By default, the Discover view showcases favorite object types, recently-viewed object types, and favorite groups.
![Ontology Manager Discover view.](/docs/resources/foundry/ontology-manager/oma-discover-view.png)
如果用户是初次接触该 Ontology，将展示两个专门的部分：一个显示该 Ontology 中最近修改过的所有 object types，另一个显示所有突出的 object types。

In case the user is new to the Ontology, two specialized sections will be presented: one which displays all object types that were recently modified within that Ontology, and one for all prominent object types.
![Ontology Manager Fallback sections.](/docs/resources/foundry/ontology-manager/oma-fallback-sections.png)
Discover 视图提供了灵活的配置选项，可以配置页面上显示的部分以及控制每个部分中显示的项目数量。可用的部分包括"Recently viewed object types"、"Favorite object types"和"Favorite groups"。此外，您还可以选择为特定 group 添加一个单独的部分，以便浏览该 group 中的所有 object types。

The Discover view provides the flexibility to configure the sections that appear on the page and control the number of items displayed within each section. The available sections include "Recently viewed object types," "Favorite object types," and "Favorite groups." Additionally, you have the option to add a separate section for a specific group, allowing you to explore all object types within that group.
![Ontology Manager Customize homepage feature.](/docs/resources/foundry/ontology-manager/oma-customize-homepage.png)
![Ontology Manager Group section.](/docs/resources/foundry/ontology-manager/oma-type-group-section.png)
### Object type view
选择某个 object type 会打开该 object type 视图，该视图包含以下组件：

Selecting an object type brings up the object type view, which has the following components:
* 包含页面选择的侧边栏（在下图左侧）
* 所选页面（在下图右侧）

* Sidebar with page selections (on the left in the image below)
* Selected page (on the right in the image below)
![Object type view.](/docs/resources/foundry/ontology-manager/oma-user-interface-object-type-view.png)
Object type 的 **Overview** 页面包含以下部分，如下图编号所示：

The **Overview** page of an object type has the following sections, as numbered in the image below:
1. Object type metadata
2. Properties
3. Action types
4. Link type graph
5. Dependents
6. Data
7. Usage
1. Object type metadata
2. Properties
3. Action types
4. Link type graph
5. Dependents
6. Data
7. Usage
![Object type overview page.](/docs/resources/foundry/ontology-manager/oma-user-interface-overview-annotated.png)
### Property editor view
从 object type 的 **Overview** 页面的 **Properties** 部分选择一个 property，以打开应用程序的 property editor 视图。

Select a property from the **Properties** section of an object type’s **Overview** page to open the property editor view of the application.
![Property editor interface.](/docs/resources/foundry/ontology-manager/oma-user-interface-property-editor-v2.png)
### Link type view
从 object type 的 **Overview** 选项卡的 link type graph 中选择一个 link type（见下图），将打开 link type 视图（包含 **Overview** 和 **Datasources** 页面）。

Selecting a link type from the link type graph of an object type’s **Overview** tab (see image below) opens the link type view (with **Overview** and **Datasources** pages).
![Link type view.](/docs/resources/foundry/ontology-manager/oma-user-interface-link-type.png)
### Action type view
从 object type 的 **Overview** 选项卡的 action type 部分选择一个 action type，将打开 action type 视图，可进一步访问 **Overview**、**Logic** 和 **Observability** 页面。

Selecting an action type from the action type section of an object type’s **Overview** tab opens the action type view, with further access to the **Overview**, **Logic** and **Observability** pages.
![Action type view.](/docs/resources/foundry/ontology-manager/oma-user-interface-action-type.png)
#### View action metrics and monitoring rules
**Observability** 选项卡显示过去 30 天内该 action 的近实时 [usage of the action](/docs/foundry/action-types/action-metrics/)，以及为该 action 定义的任何 [monitoring rules](/docs/foundry/monitoring-views/overview/) 及其状态。有关详细的 action 监控规则配置选项，请参阅 [Review action rules](/docs/foundry/monitoring-views/rules-reference/#action-rules)。

The **Observability** tab shows the near real-time [usage of the action](/docs/foundry/action-types/action-metrics/) over the last 30 days as well as any [monitoring rules](/docs/foundry/monitoring-views/overview/) and their status defined for the action. [Review action rules](/docs/foundry/monitoring-views/rules-reference/#action-rules) for detailed action monitoring rule configuration options.
![Action observability tab view.](/docs/resources/foundry/ontology-manager/oma-user-interface-action-type-observability-tab.png)
### Function type view
从 object type 的 **Overview** 选项卡的 function type 部分选择一个 function type，将打开 function type 视图，可进一步访问 **Overview**、**Configuration** 和 **Observability** 页面。

Selecting a function type from the function type section of an object type’s **Overview** tab opens the function type view, with further access to the **Overview**, **Configuration** and **Observability** pages.
#### Usage history of a function
Usage History 面板记录了使用过该 function 任何版本的应用程序以及相应的版本信息。通过此面板，您可以导航到这些应用程序，以便升级该 function 的版本。

The Usage History panel records the applications which have used any version of a function, along with the respective version information. From this panel, you can navigate to these applications in order to upgrade the version of a function.
#### View previous versions of a function
默认情况下，显示该 function 的最新版本。要查看其他版本，请使用位于左侧面板中的版本下拉选择器。

By default, the latest version of the function is displayed. To view other versions, use the version dropdown selector located in the left panel.
#### Navigate to the Functions Code Repository
对 function 的修改只能在 Functions Code Repository 中进行。要导航到该代码仓库，请使用位于 entity 视图右上角的 **Open in Code Repository** 按钮。

Modifications to the function can only be made within the Functions Code Repository. To navigate to the repository, use the **Open in Code Repository** button found in the top right-hand corner of the entity view.
![Function type view.](/docs/resources/foundry/ontology-manager/oma-user-interface-function-type.png)
#### View function metrics and monitoring rules
**Observability** 选项卡显示该 Function 过去 30 天内的准实时 [Function 使用情况](/docs/foundry/functions/function-metrics/)，以及为该 Function 定义的任何 [监控规则](/docs/foundry/monitoring-views/overview/) 及其状态。有关详细的 Function 监控规则配置选项，请参阅 [Function 规则](/docs/foundry/monitoring-views/rules-reference/#function-rules)。

The **Observability** tab shows the near real-time [usage of the function](/docs/foundry/functions/function-metrics/) over the last 30 days as well as any [monitoring rules](/docs/foundry/monitoring-views/overview/) and their status defined for the function. [Review function rules](/docs/foundry/monitoring-views/rules-reference/#function-rules) for detailed function monitoring rule configuration options.
![Function observability tab view.](/docs/resources/foundry/ontology-manager/oma-user-interface-function-type-observability-tab.png)