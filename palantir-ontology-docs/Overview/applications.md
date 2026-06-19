<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/applications/
---
# Ontology-aware applications
Foundry 包含许多原生运行于 Ontology 之上的应用程序。这些 object-aware 应用程序共同提供了一个强大的分析和运营平台，支持广泛的用例和用户角色。

Foundry contains a number of applications developed to operate natively on top of the Ontology. Together, these object-aware applications deliver a powerful analytical and operational platform that supports a range of use cases and user profiles.
要了解更多关于为何设置 Ontology 以及使用 object-aware 应用程序具有价值的信息，请参阅 [此页面](/docs/foundry/ontology/why-ontology/)。

To learn more about why setting up an Ontology and using object-aware applications is valuable, see [this page](/docs/foundry/ontology/why-ontology/).
此页面提供可用应用程序的参考，并说明应在何时使用每个应用程序：

This page provides a reference to the available applications, and explains when you should use each:
* [Application 参考](#application-reference)

* [Application 对比](#application-comparison)

* [Application reference](#application-reference)
* [Application comparison](#application-comparison)
## Application reference
### Object Views
[**Object Views**](/docs/foundry/object-views/overview/) 是与特定 object 相关的所有信息和 workflows 的中心枢纽。它包括关于 object 的关键"biographical data"、任何 linked objects、关键相关 metrics，以及指向（或嵌入的）与该 object 相关的关键分析、dashboards 和应用程序的链接。

[**Object Views**](/docs/foundry/object-views/overview/) are a central hub for all information and workflows related to a particular object. This includes key "biographical data" about an object, any linked objects, key related metrics, and links to (or embedding of) key analyses, dashboards, and applications related to the object.
例如，`Airport` Object Type 的 object view 可能为每个 `Airport` object 提供以下信息：

For example, the `Airport` object type object view might provide the following information for each `Airport` object:
* Biographical data，例如 `country`、`city`、`longitude`、`latitude` 等。

* 与该 `Airport` 关联的所有 `Aircraft` objects 和 `Flight` objects 的 360-degree view。

* 嵌入的 `Airport Covid Response` workflow。

* 指向与该 `Airport` 相关的 `Flight delay` 事件的 `Root-Cause Analysis` 的链接。

* Biographical data such as `country`, `city`, `longitude`, `latitude`, etc.
* 360-degree view of all `Aircraft` objects and `Flight` objects linked to the `Airport`
* Embedded `Airport Covid Response` workflow
* Link to a `Root-Cause Analysis` of a `Flight delay` event related to the `Airport`
![Object View Hub Example](/docs/resources/foundry/ontology/object-apps-object-view-hub.png)
### Object Explorer
[**Object Explorer**](/docs/foundry/object-explorer/overview/) 是一个用于回答 Ontology 层中任何问题的搜索和分析工具。用户可以通过可视化方式构建从简单 filters 到 Search Arounds 的 search queries，以查找感兴趣的 objects。然后，他们可以使用 exploration view 探索所得到的 object sets，或将其作为结果表格查看。此外，用户可以对比和比较 object sets，并对 object set 执行批量 Actions（例如 writeback）。随后，用户可以导出 object sets 或在兼容的应用程序（如 Workshop）中将其打开。

[**Object Explorer**](/docs/foundry/object-explorer/overview/) is a search and analysis tool for answering questions about anything in the Ontology layer. Users can visually compose search queries ranging from simple filters to Search Arounds to find objects of interest. From there, they can explore the resulting object sets using the exploration view or view them as a table of results. Additionally, users can compare and contrast object sets and take bulk Actions (for example, writeback) on the object set. Then, users can export the object sets or open them in compatible applications, such as Workshop.
Exploration 视图是一组预设且可配置的可视化（如图表或地图），用户可以进一步利用它深入查看特定的对象子集。Object Explorer 无需预配置，面向技术程度较低的用户。

The exploration view is a set of preset and configurable visualizations (such as charts or maps) that the user can further leverage to drill-down into specific subsets of objects. Object Explorer requires no pre-configuration and is geared towards less technical users.
![Object Explorer](/docs/resources/foundry/ontology/object-apps-oe.png)
### Quiver
[**Quiver**](/docs/foundry/quiver/overview/) 通过可视化点击式界面和强大的图表库，在 Ontology 层启用高级分析工作流。Quiver 可用于支持从简单的线性下钻分析到具有聚合和统计函数的、高度分支且复杂的分析等各种场景。Quiver 还支持原生时间序列分析。Quiver 分析可以被模板化为只读仪表板，以便更广泛的消费使用。

[**Quiver**](/docs/foundry/quiver/overview/) enables advanced analytical workflows in the Ontology layer through a visual point-and-click interface and a powerful charting library. Quiver can be used to support anything from simple linear drill-down analyses to highly-branched and complex analyses with aggregations and statistical functions. Quiver also supports native time series analysis. Quiver analyses can be templatized into read-only dashboards for broader consumption.
![Quiver](/docs/resources/foundry/ontology/object-apps-quiver.png)
### Workshop
[**Workshop**](/docs/foundry/workshop/overview/) 能够在 Ontology 层上以点击方式、无需代码地构建应用程序。在 Workshop 中构建的应用程序比在其他点击式工具中创建的典型仪表板更具动态性和交互性。

[**Workshop**](/docs/foundry/workshop/overview/) enables point-and-click code-less application-building natively on the Ontology layer. Applications built in Workshop are more dynamic and interactive than typical dashboards created in other point-and-click tools.
通过利用高质量的 [Layouts](/docs/foundry/workshop/concepts-layouts/) 以及易于使用但功能强大的 [Events system](/docs/foundry/workshop/concepts-events/)，Workshop 应用程序的目标是像自定义 React 应用程序一样用户友好且高质量。

By leveraging high-quality [Layouts](/docs/foundry/workshop/concepts-layouts/) and an easy-to-use but sophisticated [Events system](/docs/foundry/workshop/concepts-events/), Workshop applications aim to be as user-friendly and high-quality as custom React applications.
*Workshop 编辑器视图*

*Workshop Editor View*
![Workshop Editor View](/docs/resources/foundry/ontology/object-apps-workshop-editor-view.png)
*最终 Workshop 模块*

*Final Workshop Module*
![Final Workshop Module](/docs/resources/foundry/ontology/object-apps-workshop-module.png)
### Slate
[**Slate**](/docs/foundry/slate/overview/) 是 Foundry 中的一款灵活的应用程序构建器，比 Workshop 需要更多的技术配置和代码。Slate 应用程序与 Ontology 层交互，也可以直接与 Foundry datasets 交互。Slate 基于 Web 开发范式实现显著的可视化定制，并具有广泛的可使用功能，但相比 Workshop，其应用程序的构建和维护也需要更多的技术知识。

[**Slate**](/docs/foundry/slate/overview/) is a flexible application builder for Foundry that requires more technical configuration and code than Workshop. Slate applications interact with the Ontology layer, but can also interact directly with Foundry datasets. Slate enables significant visual customization based on web development paradigms and has a wide range of available features, but also requires more technical knowledge to build and maintain applications than Workshop.
*Slate 编辑器视图*

*Slate Editor View*
![Slate Editor View](/docs/resources/foundry/ontology/object-apps-slate-editor-view.png)
*Slate 应用程序视图*

*Slate Application View*
![Slate Application View](/docs/resources/foundry/ontology/object-apps-slate-app-view.png)
### Carbon
[**Carbon**](/docs/foundry/carbon/overview/) 能够在 Foundry 中组合多个资源或应用程序，以为运营用户创建高度策划的 *workspaces*。通过允许您组合分析结果（如仪表板、在 Workshop 或 Slate 中构建的应用程序）以及开箱即用的功能（如 Object Views 和 Object Explorer），Carbon 使工作流构建者能够执行"最后一英里"的定制，从而为最终用户创造高度量身定制且易用的体验。

[**Carbon**](/docs/foundry/carbon/overview/) enables combining multiple resources or applications in Foundry to create highly curated *workspaces* for operational users. By allowing you to combine analytical results such as dashboards, applications built in Workshop or Slate, and out-of-the-box capabilities such as Object Views and Object Explorer, Carbon enables workflow builders to perform the "last mile" of customization to create a highly tailored and usable experience for end users.
![Carbon workspace](/docs/resources/foundry/ontology/carbon-workspace.png)
### Map
[**Map**](/docs/foundry/map/overview/) 应用程序允许您在地理空间环境中整合和分析 objects 以及其他数据。

The [**Map**](/docs/foundry/map/overview/) application allows you to bring together and analyze objects and other data in a geospatial context.
![Map Application](/docs/resources/foundry/ontology/map-overview.png)
## Application comparison
每个 object-aware 应用程序在几个维度上有所不同。三个特别重要的维度是：

Each object-aware application varies on a few dimensions. Three particularly important dimensions are:
* 主要 [use case(s)](#use-cases)，

* [workflow style](#workflow-style)，以及

* 应用程序的 [configuration model](#configuration-model)。

* the [primary use case(s)](#use-cases),
* the [workflow style](#workflow-style), and
* the [configuration model](#configuration-model) of the application.
| Foundry Application | [Primary use case](#use-cases) | [Workflow Style](#workflow-style) | [Configuration Model](#configuration-model) | Objects or Datasets |
| --- | --- | --- | --- | --- |
|[Object Views](#object-views) | Discovery | Workflow-specific | Walk-up usable | Objects |
|[Object Explorer](#object-explorer) | Discovery & Analysis | Exploratory | Walk-up usable | Objects |
|[Quiver](#quiver) | Analysis & Dashboards | Exploratory (for Analytical mode); workflow-specific (for Dashboard mode) | Walk-up usable (for Analytical mode); customizable (for Dashboard mode) | Objects |
|[Workshop](#workshop) | Applications & Dashboards | Workflow-specific | Customizable | Objects |
|[Slate](#slate) | Applications & Dashboards (complex) | Workflow-specific | Customizable | Objects (recommended) and Datasets |
|[Map](#map) | Geospatial | Exploratory or Workflow-specific | Walk-up usable | Objects |
### Use cases
object-aware 应用程序支持的主要用例包括 **Discovery**、**Analysis**、**Dashboards** 和 **Applications**。

The main use cases supported by object-aware applications are **Discovery**, **Analysis**, **Dashboards**, and **Applications**.
* **Discovery** 使用户能够找到正确的信息或工作流。Discovery 主要通过两个核心功能实现：策划的内容中心和搜索。策划的内容中心（有时称为登陆页面或"360 视图"）的范围从任何用户都可以使用的综合标准视图到针对特定用户集或用例的定向视图。搜索功能通过对关键词的自由文本搜索以及通过 link traversals 或 drill-downs 的迭代搜索来支持 Discovery。

* **Analysis** 使用户能够回答广泛的问题。这些问题从简单的（*特定产品的平均客户保留率是多少？*）到非常复杂的（*三个不同的客户群在所有产品以及每个单独产品中，在保留率和总体收入方面随着时间的推移如何比较？*）不等。分析路径是探索性的，这意味着它由最终用户自己定义，并且通常是高度迭代的；随着初始问题得到解答，新问题会被提出并纳入分析路径中。

* **Dashboards** 是一组预配置的可视化，主要以只读方式被更广泛的消费用户使用。Dashboards 通常用于将富有意义的 *Analyses* 转化为经常性报告或运营监控。Dashboards 的特点是包含大量图表和其他可视化，但不像 *Applications* 那样可定制或具有交互性（见下文）。Dashboards 通常是参数化的，以便用户可以将可视化过滤到不同的数据子集。

* **Applications** 是为特定用户群体解决特定问题而设计的交互式自定义操作界面。Applications 通常比 dashboards 更复杂，旨在使用户能够遵循特定的、按轨道运行的工作流。虽然应用程序可能包含一些策划的分析内容（例如统计数据、图表、图形等）以辅助决策，但它通常还包含若干工作流元素，并且经常捕获用户输入（例如 writeback）。

* **Discovery** enables users to find the right information or workflow. Discovery is primarily enabled through two core features: curated content hubs and search. Curated content hubs (sometimes called landing pages or "360 views") range from a comprehensive standard view for any user to targeted views for a specific set of users or use case. Search functionality supports discovery through free-text search of key words as well as more iterative search through link traversals or drill-downs.
* **Analysis** enables users to answer a broad range of questions. These range from the simple (*what is the average customer retention for a given product?*) to the very complex (*how do three different customer cohorts compare in terms of retention and overall revenue over time, across all products and for each individual product?*). The analytical path is exploratory, meaning that it is defined by the end user themselves and is often highly iterative; as the initial questions are answered, new questions are developed and incorporated into the analysis path.
* **Dashboards** are sets of pre-configured visualizations consumed primarily in a read-only fashion by a broader set of consumer users. Dashboards are often used to turn meaningful *Analyses* into recurring reporting or operational monitoring. Dashboards are characterized by a large number of charts and other visualizations, but are not as customizable or interactive as *Applications* (see below). Dashboards are often parameterized such that users can filter down the visualizations to different subsets of data.
* **Applications** are interactive custom operational interfaces intended for a specific user group to solve a specific problem. Applications are often more complex than dashboards and are oriented at enabling users to follow a specific and on-rails workflow. While the application may contain some curated analytical content (e.g. statistics, charts, graphs, etc.) required to perform a decision, it also typically has several workflow elements and often captures user input (for example, writeback).
### Workflow style
Object-aware applications are optimized for primary workflow styles.
Object-aware applications are optimized for primary workflow styles.
* **Exploratory applications** do not need to be pre-configured by a "builder" user and are used out-of-the-box by end users as soon as data has been modeled into the Ontology. In exploratory applications, the end-user defines their analytical path, and can answer a wide range of questions that are not pre-determined. Exploratory applications typically contain a set of search, visualization, and transformation features to enable this. Object-aware applications that are primarily exploratory include Object Explorer and Quiver.
* **Workflow-specific applications** require pre-configuration by a "builder" user before an end user can actually use them. This is typical of Dashboards or Applications that have two primary user groups: (1) the builder group configuring the specific dashboard or application and (2) the downstream end users for whom the applications are built. Workshop and Slate modules both need to be pre-configured by a "Builder" user in edit mode.
* **Exploratory applications** do not need to be pre-configured by a "builder" user and are used out-of-the-box by end users as soon as data has been modeled into the Ontology. In exploratory applications, the end-user defines their analytical path, and can answer a wide range of questions that are not pre-determined. Exploratory applications typically contain a set of search, visualization, and transformation features to enable this. Object-aware applications that are primarily exploratory include Object Explorer and Quiver.
* **Workflow-specific applications** require pre-configuration by a "builder" user before an end user can actually use them. This is typical of Dashboards or Applications that have two primary user groups: (1) the builder group configuring the specific dashboard or application and (2) the downstream end users for whom the applications are built. Workshop and Slate modules both need to be pre-configured by a "Builder" user in edit mode.
Certain applications like Quiver accommodate both workflow styles because while their primary mode is exploratory, the outputs can be configured into a more broadly consumed workflow-specific artifact. While Quiver Analyses are highly exploratory, they can be published as Quiver Dashboards that are pre-configured analytical views accessible to a broader audience.
Certain applications like Quiver accommodate both workflow styles because while their primary mode is exploratory, the outputs can be configured into a more broadly consumed workflow-specific artifact. While Quiver Analyses are highly exploratory, they can be published as Quiver Dashboards that are pre-configured analytical views accessible to a broader audience.
### Configuration model
The configuration model describes the extent to which the user interface must be configured before it can be leveraged by an end user.
The configuration model describes the extent to which the user interface must be configured before it can be leveraged by an end user.
* **Walk-up usable** applications can be employed effectively and immediately by users, with little to no configuration requirement or maintenance burden. For example, Object Explorer has minimal-to-no configuration requirement, making it immediately usable for end users once an Ontology is defined.
* **Customizable** applications require an upfront investment (often by a separate "builder" user) to implement an interface that solves a particular problem for an end user. It also implies a higher ongoing maintenance cost. However, the resulting application is typically a fit-for-purpose interface that exactly meets the need of the specific workflow. Workshop and Slate are examples of this type of customization.
* **Walk-up usable** applications can be employed effectively and immediately by users, with little to no configuration requirement or maintenance burden. For example, Object Explorer has minimal-to-no configuration requirement, making it immediately usable for end users once an Ontology is defined.
* **Customizable** applications require an upfront investment (often by a separate "builder" user) to implement an interface that solves a particular problem for an end user. It also implies a higher ongoing maintenance cost. However, the resulting application is typically a fit-for-purpose interface that exactly meets the need of the specific workflow. Workshop and Slate are examples of this type of customization.