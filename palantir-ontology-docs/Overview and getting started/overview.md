<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-backend/overview/
---
# Ontology architecture
Foundry Ontology 是组织的运营层。Ontology 位于集成到 Foundry 中的数字资产(datasets 和 models)之上,并将它们连接到现实世界中的对应物,范围从工厂、设备和产品等物理资产到客户订单或金融交易等概念。Ontology 作为组织的数字孪生,包含支持各种用例所需的语义元素(objects、properties、links)和动态元素(actions、functions、dynamic security)。您可以在 [Ontology documentation](/docs/foundry/ontology/overview/) 中了解更多关于 Foundry Ontology 及其如何实现更好决策的信息。

The Foundry Ontology is an operational layer for the organization. The Ontology sits on top of the digital assets integrated into Foundry (datasets and models) and connects them to their real-world counterparts, ranging from physical assets like factories, equipment, and products to concepts like customer orders or financial transactions. The Ontology serves as a digital twin of an organization, containing both the semantic elements (objects, properties, links) and kinetic elements (actions, functions, dynamic security) needed to enable use cases of all types. You can learn more about the Foundry Ontology and how it enables better decision-making in the [Ontology documentation](/docs/foundry/ontology/overview/).
Foundry Ontology 由多个协同工作的服务支持,这些服务共同负责对 Ontology 中的 objects 进行 indexing、storing、querying 和操作。本页提供了 Ontology 后端架构的高层概述。

The Foundry Ontology is backed by multiple services that work together to index, store, query, and manipulate objects in the Ontology. This page provides a high-level overview of the Ontology’s backend architecture.
## Functional components and architecture
Foundry 平台采用微服务架构,多个服务共同构成 Ontology 后端。Ontology 后端负责三个主要功能:

The Foundry platform uses a microservices architecture in which multiple services together comprise the Ontology backend. The Ontology backend is responsible for three main functions:
* **Datasource management**,用于为 Ontology 提供数据源并管理 Ontology 中的 schema 定义。

* 从 Ontology 中 **querying、searching 和 aggregating objects**,并支持特定的过滤和权限控制。

* **Orchestration of writing to the Ontology**,包括对 datasources 的 indexing 以及基于 Foundry 中做出的决策或执行的操作对 Ontology objects 的编辑。

* **Datasource management** to feed the Ontology and manage schema definitions within the Ontology.
* **Querying, searching, and aggregating objects** from the Ontology with support for specific filtering and permissioning.
* **Orchestration of writing to the Ontology**, including indexing of datasources and edits to Ontology objects based on decisions made or actions taken in Foundry.
这些功能由构成 Ontology 后端的服务共同处理,这些服务概述如下:

These functions are handled collectively by the services that make up the Ontology backend, which are summarized below:
* [Ontology Metadata Service (OMS)](#ontology-metadata-service-oms)
* [Object databases](#object-databases)
* [Object Set Service (OSS)](#object-set-service-oss)
* [Actions](#actions)
* [Object Data Funnel](#object-data-funnel)
* [Functions on Objects](#functions-on-objects)
* [Ontology Metadata Service (OMS)](#ontology-metadata-service-oms)
* [Object databases](#object-databases)
* [Object Set Service (OSS)](#object-set-service-oss)
* [Actions](#actions)
* [Object Data Funnel](#object-data-funnel)
* [Functions on Objects](#functions-on-objects)
### Ontology Metadata Service (OMS)
Ontology Metadata Service (OMS) 是一个总体服务,它定义存在的本体实体的集合。该定义包括 object types 的 metadata、描述 object types 之间任何关系的 link types、以结构化和受控方式修改 object data 的 action types 等。

The Ontology Metadata Service (OMS) is an overarching service that defines the set of ontological entities that exist. This definition includes the metadata of object types, the link types that describe any relationships between object types, the action types that can modify object data in a structured and controlled way, and more.
在 [Ontology metadata documentation](/docs/foundry/ontology/core-concepts/) 中了解更多关于 Foundry Ontology 中核心概念的信息。

Learn more about core concepts in the Foundry Ontology in the [Ontology metadata documentation](/docs/foundry/ontology/core-concepts/).
### Object databases
Object databases 是负责在 Ontology 中存储已索引 object data 的服务,旨在为用户应用程序提供快速的数据 querying 和 query computation。除了存储已索引的数据外,object databases 还负责 indexing、querying 和编排用户编辑。

Object databases are the services responsible for storing the indexed object data in the Ontology and are designed to provide fast data querying and query computation for user applications. In addition to storing indexed data, object databases are also responsible for indexing, querying, and orchestrating user edits.
**Object Storage V1 (Phonograph)** 是 Foundry 旧版的 Ontology 后端组件。**Object Storage V2** 是面向 Ontology 的下一代规范化数据存储。有关这些服务的更多信息，请参阅[下文](#evolution-of-the-ontology-backend)。

**Object Storage V1 (Phonograph)** is Foundry's legacy Ontology backend component. **Object Storage V2** is the next-generation canonical data store for backing the Ontology. More information on these services can be found [below](#evolution-of-the-ontology-backend).
### Object Set Service (OSS)
Object Set Service (OSS) 是负责为 Ontology 提供读取服务的服务；OSS 允许其他 Foundry 服务和应用程序查询 Ontology 中的对象数据，从而实现对象的搜索、过滤、聚合和加载。

The Object Set Service (OSS) is the service responsible for serving reads from the Ontology; OSS allows other Foundry services and applications to query objects data from the Ontology, enabling searching, filtering, aggregating, and loading of objects.
#### Object sets
Object set 是现实世界实体的列表，保存供将来参考和使用，并可在支持对象的 Foundry 应用程序中共享。Object set 以 resource 形式保存，便于与协作者共享。

Object sets are lists of real-world entities that are saved for future reference and use across Foundry applications that support objects. Object sets are saved as resources for easy sharing with collaborators.
Object set 可以通过定义方式（静态或动态）以及在对象后端中的当前状态（临时或永久）来描述：

Object sets can be described by definition (static or dynamic) and current state in the object backend (temporary or permanent):
* **Static object sets：** Static object sets 以主键列表的形式保存，无论输入数据如何变化都保持不变。

* **Static object sets:** Static object sets are saved as a list of primary keys, and will stay the same regardless of any changes to the input data.
* **Dynamic object sets：** Dynamic object sets 以应用于创建 object set 的过滤条件的表示形式保存。当新数据匹配这些过滤条件时，object set 将会更新。

* **Dynamic object sets:** Dynamic object sets are saved as a representation of the filters applied to create the object set. When new data matches the filters, the object set will be updated.
* **Temporary object sets：** Temporary object sets 主要用于平台中，将 object set 从一个应用程序或服务传递给另一个应用程序或服务，并且只能由创建它们的用户访问。一个示例 temporary object set RID 形如 `ri.object-set.main.temporary-object-set.37d7e171-2d11-4fcd-b031-9a0863f6f744`，在 24 小时内过期。

* **Temporary object sets:** Temporary object sets are mainly used in the platform to hand object sets from one application or service to another and can only be accessed by the user who created them. A sample temporary object set RID will appear like `ri.object-set.main.temporary-object-set.37d7e171-2d11-4fcd-b031-9a0863f6f744` and expires within 24 hours.
* **Permanent object sets：** Permanent object sets 存储在对象后端中，供将来在平台中参考和使用。

* **Permanent object sets:** Permanent object sets are stored in the object backend for future reference and use across the platform.
### Actions
Actions 服务负责将用户编辑应用于对象数据库。Actions 提供了一种结构化的方式来修改对象的属性值，并为用户编辑启用复杂的权限和条件。此外，Actions 还可用于创建历史 action 日志，以便分析用户决策。

The Actions service is responsible for applying user edits to object databases. Actions provide a structured way to modify property values of an object and enable complex permissions and conditions for user edits. Additionally, Actions can be used to create a historical action log for analysis of user decisions.
### Object Data Funnel
Object Data Funnel（以下简称 "Funnel"）是 Object Storage V2 架构中的微服务，负责将数据写入编排到 Ontology 中。Funnel 从 Foundry 数据源（例如 datasets、restricted views 和 streaming datasources）以及用户编辑（来自 Actions）读取数据，并将这些数据索引到对象数据库中。Funnel 还确保在底层数据源更新时，索引数据保持最新。

The Object Data Funnel ("Funnel") is a microservice in the Object Storage V2 architecture responsible for orchestrating data writes into the Ontology. Funnel reads data from Foundry datasources (such as datasets, restricted views, and streaming datasources) and user edits (from Actions) and indexes these data into object databases. Funnel also ensures that indexed data is kept up-to-date as the underlying datasources update.
### Functions on Objects
Functions 使代码作者能够编写可在操作上下文中快速执行的逻辑，例如用于支持决策过程的 dashboards 和 applications。

Functions enable code authors to write logic that can be executed quickly in operational contexts, such as dashboards and applications designed to power decision-making processes.
有关更多详细信息，请参阅 [Functions](/docs/foundry/functions/overview/) 文档。

See the [Functions](/docs/foundry/functions/overview/) documentation for more details.
## Evolution of the Ontology backend
本节描述了 Object Storage V1 (Phonograph) 的旧版架构以及 Object Storage V2 的更新架构。

This section describes the legacy architecture of Object Storage V1 (Phonograph) and the updated architecture of Object Storage V2.
### Object Storage V1 (Phonograph) architecture \[Planned deprecation]
> **⚠️ 警告: Planned deprecation**

> Object Storage V1 (Phonograph) 处于[计划弃用](/docs/foundry/platform-overview/development-life-cycle/)阶段，将于 2026 年 6 月 30 日之后不可用。请将您的 [Object Types 和 Link Types](/docs/foundry/object-backend/osv1-osv2-migration/) 迁移到 Object Storage V2。有关更多信息，请参考 [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) 中的 `Migrate object types and many-to-many link types from Object Storage v1 to v2` intervention。
> 如果您对工作流中的 OSv1 到 OSv2 迁移有疑问，请联系 Palantir Support。
> **⚠️ 警告: Planned deprecation**

> Object Storage V1 (Phonograph) is in the [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be unavailable after June 30, 2026. [Migrate your object types and link types](/docs/foundry/object-backend/osv1-osv2-migration/) to Object Storage V2. Reference the `Migrate object types and many-to-many link types from Object Storage v1 to v2` intervention in [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) for more information.
> Contact Palantir Support if you have questions about the OSv1 to OSv2 migration in your workflows.
Object Storage V1 (Phonograph) 是 Foundry 最初的对象数据库，旨在对来自各种潜在数据模型的信息进行索引和管理，同时在 Ontology 中的对象数据上维护 Foundry 的安全模型。除了索引和存储数据之外，Object Storage V1 (Phonograph) 还跟踪用户生成编辑的应用情况，通过搜索和聚合响应复杂的用户查询，并协调数据 writeback。

Object Storage V1 (Phonograph) is Foundry's original object database, designed to index and manage information from a wide range of potential data models while maintaining Foundry's security model across object data in the Ontology. Beyond indexing and storing data, Object Storage V1 (Phonograph) tracks the application of user-generated edits, serves complex user queries with searches and aggregations, and orchestrates data writeback.
下面是描述 Object Storage V1 (Phonograph) 架构的示意图。

Below is a diagram describing the architecture for Object Storage V1 (Phonograph).
![Object Storage v1 Architecture](/docs/resources/foundry/object-backend/osv1-arch.png)
### Object Storage V2 architecture
随着 Foundry 获得更多能力并不断发展以满足 Palantir 客户复杂的运营需求和不断增长的规模，Object Storage V2 从第一性原理出发构建而成，以支持下一代由 Ontology 驱动的用例和 workflows。

As Foundry gained more capabilities and evolved to meet the complex operational needs and growing scale of Palantir's customers, Object Storage V2 was built from first principles to enable the next generation of Ontology-driven use cases and workflows.
具体来说，新架构分离了在 Object Storage V1 (Phonograph) 中合并的关注维度，并在系统设计中解耦了职责；通过将负责 indexing 和 querying 数据的子系统分离，Object Storage V2 可以更轻松地进行水平扩展以满足未来的需求。

Specifically, the new architecture separates dimensions of concern that had been consolidated in Object Storage V1 (Phonograph) and decouples responsibilities within the system design; by separating the subsystems responsible for indexing and querying data, Object Storage V2 can scale horizontally more easily to meet future needs.
Object Storage V2 还通过 [Object Data Funnel](#object-data-funnel) 集成了其他服务，例如 [Actions](/docs/foundry/action-types/overview/)。

Object Storage V2 also incorporates additional services like [Actions](/docs/foundry/action-types/overview/) via the [Object Data Funnel](#object-data-funnel).
由 Object Storage V2 启用的新功能包括：

New features and capabilities enabled by Object Storage V2 include:
* 通过对所有 Object Type 默认启用的 incremental object indexing，显著提升 Ontology 数据 indexing 的性能。

* 针对单个 Object Type，indexing 吞吐量提升至数百亿 objects 的量级。

* 通过 multi-datasource Object Types 实现更细粒度的 object permissions，包括 column/property 级别的权限。

* 提升用户编辑吞吐量，允许在单个 Action 中编辑多达 10,000 个 objects。如果您需要启用更高的上限，请联系 Palantir Support 以创建针对您 enrollment 的变更请求。

* 降低用户编辑延迟并加快用户编辑的 observation。

* 支持在 Object Type 发生 breaking schema change 之后迁移现有的用户编辑。

* 通过支持 streaming datasources，实现向 Ontology 的低延迟数据 indexing。

* 每个 Object Type 最多支持 2000 个 properties。

* 通过基于 Spark 的 query 执行层，实现更高规模的 Search Arounds 以及更准确的 aggregations。

* 默认情况下，Search Around 的上限为 100,000 个 objects。如果您的用例需要超过 100,000 个 objects 的更大规模 Search Around，请联系 Palantir Support 以获取启用说明。

* Significantly improved performance for Ontology data indexing through incremental object indexing (enabled by default) for all object types.
* Increased indexing throughput on the order of tens of billions of objects for a single object type.
* More granular object permissions with multi-datasource object types, including column/property level permissions.
* Increased user edit throughput, enabling up to 10,000 objects to be edited in a single Action. If you need to enable a higher limit, contact Palantir Support to create a change request for your enrollment.
* Reduced user edit latency and faster observation of user edits.
* The ability to migrate existing user edits after a breaking schema change in an object type.
* Low-latency data indexing into the Ontology through support of streaming datasources.
* Supports a maximum of 2000 properties per object type.
* Higher-scale Search Arounds and more accurate aggregations through a Spark-based query execution layer.
* By default, the Search Around limit is 100,000 objects. If your use cases require a higher scale Search Around of over 100,000 objects, contact Palantir Support for instructions on how to enable this.
下面是描述 Object Storage V2 如何为 Ontology 提供支持的架构示意图。

Below is an architecture diagram describing how Object Storage V2 powers the Ontology.
![Object Storage v2 Architecture](/docs/resources/foundry/object-backend/osv2-arch.png)