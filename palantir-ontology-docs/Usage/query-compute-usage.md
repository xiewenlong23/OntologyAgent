<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/query-compute-usage/
---
# Compute usage with Ontology queries
Foundry Ontology 是一个数据后端,它将基于文件的数据映射到以组织为中心的对象,并为数据探索、数据分析、运营数据编辑、场景分析等提供高速查询。Ontology 将数据存储在多模态存储后端中,每个后端都有自己的用途,并可以在单个请求中灵活地进行查询。查询 Foundry Ontology 需要了解下面讨论的一些基础概念。

The Foundry Ontology is a data backend that maps file-based data to organization-centric objects and serves high-speed queries for data exploration, data analysis, operational data editing, scenario analysis, and more. The Ontology stores data in multi-modal storage backends that each have their own purposes and can be flexibly queried in a single request. Querying the Foundry Ontology requires knowledge of some foundational concepts discussed below.
> **ℹ️ 注意**

> 如果您与 Palantir 签订了企业合同,请在继续进行计算使用情况计算之前联系您的 Palantir 代表。
> **ℹ️ 注意**

> If you have an enterprise contract with Palantir, contact your Palantir representative before proceeding with compute usage calculations.
## Core concepts: Object types and object sets
第一个重要概念是 **object type** 及其对应的 **object set** 之间的区别。**Object type** 是实体本身的语义表示(例如对象的名称和属性)。

The first important concept is the difference between an **object type** and its corresponding **object set**. An **object type** is the semantic representation of the entity itself (such as the name and properties of the object).
一个 object type 对应一个 **object set**,其中包含对象本身。**Object set** 的大小对应于传入数据集的行数以及通过 Ontology action 创建和删除的对象数量。

An object type has a corresponding **object set**, which contains the objects themselves. The size of the **object set** corresponds to the number of rows of the incoming dataset and the number of objects created and deleted by Ontology actions.
## Core concept: Query types
第二个重要概念是 **query types** 的概念,它包括 filter、aggregation、Search Around 和 writeback operation。每种 query type 都需要计算资源来执行。有关每种 query type 的当前 compute-second 开销,请参阅 [Ontology Query Compute (2026)](#ontology-query-compute-2026)。

The second important concept is the idea of **query types**, which include filters, aggregations, Search Arounds, and writeback operations. Each query type requires compute to execute. See [Ontology Query Compute (2026)](#ontology-query-compute-2026) for the current compute-second overhead per query type.
在使用 Foundry Ontology 时,**query type** 由以下 [Foundry Applications](/docs/foundry/ontology/applications/) 针对 **object set** 执行:

When using the Foundry Ontology, **query types** are executed against **object sets** by the following [Foundry Applications](/docs/foundry/ontology/applications/):
* Object Explorer
* Workshop
* Quiver
* Slate
* Vertex
* Foundry Rules
* Foundry Machinery
* Object APIs (OPIs)
* Object Explorer
* Workshop
* Quiver
* Slate
* Vertex
* Foundry Rules
* Foundry Machinery
* Object APIs (OPIs)
从上述任何来源查询 Ontology 都会使用 compute-seconds 来运行查询。

Querying the ontology from any of these sources will use compute-seconds to run the query.
## Investigating Foundry compute usage from Ontology queries
在 Foundry 中,compute-seconds 归属于平台中的资源,而不是归属于与这些资源交互的用户。

In Foundry, compute-seconds are attributed to resources in the platform rather than to the users that are interacting with those resources.
对于 Ontology 查询,计算资源的归属方式有多种。作为一般规则,计算资源归属于查询发起的资源。但是,如果不存在用于生成计算资源的已保存资源(例如通过 API),则计算资源将归属于被查询的 object type。如果在单个请求中查询了多个对象,则计算资源在这些对象之间平均分配。

When it comes to Ontology queries, there are multiple ways in which compute is attributed. As a general rule, the compute is attached to the resource where the query originated. However, when there is no saved resource that is used to generate the compute (such as via API), the compute will be attached to the object types that are being queried. If multiple objects are queried in a single request, then the compute is attributed via an even split between the objects.
以下资源类型的 Ontology 查询计算归属于资源本身，而非其底层对象：

The following resource types have Ontology query compute attributed to them, rather than the underlying objects:
* Workshop applications
* Carbon pages
* Quiver analyses and dashboards
* Vertex applications
* Slate applications
* Foundry Machinery applications
* Foundry Rules resources
* Foundry Automate
* AIP Logic
* SQL Console worksheets
* OSDK applications
* Workshop applications
* Carbon pages
* Quiver analyses and dashboards
* Vertex applications
* Slate applications
* Foundry Machinery applications
* Foundry Rules resources
* Foundry Automate
* AIP Logic
* SQL Console worksheets
* OSDK applications
由于没有可供归属计算资源的固定对象，以下交互模式将其 Ontology 查询计算直接挂载到所查询的 object type 上。

The following interaction patterns have their Ontology query compute attached directly to the object types that they query, given there is no set resource to which the compute can be attached.
* Object Explorer
* Object APIs（包括 OSDK）

* Object Explorer
* Object APIs (including the OSDK)
## Ontology Query Compute (2026)
> **ℹ️ 注意: 自 2026 年 1 月 1 日起生效**

> 以下计算模型于 2026 年 1 月 1 日生效，并取代下方 [Legacy](#measuring-foundry-compute-with-ontology-object-queries-legacy) 部分中描述的旧版模型。
> **ℹ️ 注意: Effective January 1, 2026**

> The following compute model takes effect on January 1, 2026, and replaces the legacy model described in the [Legacy](#measuring-foundry-compute-with-ontology-object-queries-legacy) section below.
Ontology Query Compute 由用户和 agent 对 Ontology 的使用驱动。决定计算使用的主要因素如下：

Ontology Query Compute is driven by Ontology use by users and agents. Consider the primary factors that determine compute usage:
### Factor 1: Number of users and agents
Compute-seconds 以累计方式计算。针对 ontology 运行的查询和转换越多，整体计算使用量就越高。查询量随用户交互（例如 application 刷新和交互式查询）以及 agentic transformations 线性增长。

Compute-seconds are measured cumulatively. The more queries and transformations run against the ontology, the higher the overall compute usage. Query volume grows linearly with user interactions — such as application refreshes and interactive queries — as well as agentic transformations.
### Factor 2: Query type
用户可以通过以下查询类型访问其 Ontology，每种查询类型都关联一个最低的 compute-second 开销。实际计算使用量可能因查询复杂度和所查询 object set 的大小或 object 数量而更高。

Users can access their Ontology through the following query types, each associated with a minimum compute-second overhead per query. Actual compute usage may be higher depending on query complexity and the size of the object set, or number of objects queried.
* **Base query：** 原样返回 object set，或基于某些 property 进行基础过滤。

* **Search Around query：** 获取一个输入的 object set，并根据该输入集的某个 property，在另一个 object set 上运行二次过滤。

* **Aggregation query：** 获取一个输入的 object set，并对其所有 object 的某个 property 运行聚合 function（例如 `sum` 或 `avg`）。

* **[Ontology SQL query](https://www.palantir.com/docs/foundry/sql-warehousing/ontology-sql)：** 使用标准 Spark SQL 语法针对 object storage 中的 object type、link 和 interface 直接运行 SQL 查询。

* **Advanced query：** 不属于其他查询类型的任何查询。例如，在完整 object set 上对 embeddings 应用 semantic search。

* **Derived Property query：** Derived Property 是指在运行时基于 object 上其他 property 或 link 的值计算得出的 property，包括对 linked object 的 property 进行聚合或选择。Derived property 可用于在同一请求中进一步进行过滤、排序或聚合等操作。

* **Actions：** 用于将 object set 中 object 的 property 值替换为新值的 writeback 操作。Actions 的最低开销为 `18` 个 compute-seconds，并随编辑的 object 数量扩展，第一个 object 之后每编辑一个 object 额外产生 `1` 个 compute-second。

* **Ontology Compute (Phonograph) \[Legacy]：** 针对仍使用 Object Storage V1 (OSv1) 后端的 object 发起的查询。这些查询在 Resource Management Application 中显示为 "Ontology Compute (phonograph)"。针对这些查询保留了 [existing OSv1 compute model](#measuring-compute-with-object-storage-v1-legacy)。

* **Base query:** Returns the object set as-is or with basic filtering on certain properties.
* **Search Around query:** Takes an incoming object set and runs a secondary filter on another object set based on a certain property of the incoming set.
* **Aggregation query:** Takes an input object set and runs an aggregating function (such as `sum` or `avg`) on one of the properties for all objects in the set.
* **[Ontology SQL query](https://www.palantir.com/docs/foundry/sql-warehousing/ontology-sql):** Runs SQL queries directly against object types, links, and interfaces using standard Spark SQL syntax against object storage.
* **Advanced query:** Anything not covered by other query types. For example, applying a semantic search over embeddings across a full object set.
* **Derived Property query:** Derived Properties are properties calculated at runtime based on the values of other properties or links on objects, including aggregating on or selecting properties of linked objects. Derived properties are then available for further operations such as filtering, sorting, or aggregating within the same request.
* **Actions:** Writeback operations that replace the values of properties of objects in a designated object set. Actions have a minimum overhead of `18` compute-seconds and scale with the number of objects edited, incurring an additional `1` compute-second per object edited beyond the first.
* **Ontology Compute (Phonograph) \[Legacy]:** Queries against objects still using the Object Storage V1 (OSv1) backend. These appear as "Ontology Compute (phonograph)" in the Resource Management Application. The [existing OSv1 compute model](#measuring-compute-with-object-storage-v1-legacy) has been retained for these queries.
**下表汇总了每种查询类型的最低 compute-second 开销。**

**The following table summarizes the minimum compute-second overhead per query type.**
| Query Type                  | Minimum compute-seconds overhead |
|-----------------------------|----------------------------------|
| Base query                  | 2                                |
| Search Around query         | 5                                |
| Aggregation query           | 5                                |
| Ontology SQL query          | 5                                |
| Advanced query              | 10                               |
| Derived Property query      | 10                               |
| Actions                     | 18                               |
| Ontology Compute (Phonograph) \[Legacy] | 16                               |
> **ℹ️ 注意**

> 针对 Object Storage V1 (OSv1) 查询的现有计算模型已予以保留。任何针对仍使用 OSv1 后端的 object 发起的查询，其最低开销为每次查询 `16` 个 compute-seconds。
> **ℹ️ 注意**

> The existing compute model for Object Storage V1 (OSv1) queries has been retained. Any queries against objects still using the OSv1 backend carry a minimum compute-second overhead of `16` compute-seconds per query.
***
## Measuring Foundry compute with Ontology object queries \[Legacy]
> **ℹ️ 注意: Legacy**

> 以下部分描述了 2026 年 1 月 1 日之前生效的旧版计算模型，仅供参考。如需了解当前计算模型，请参阅上方的 [Ontology Query Compute (2026)](#ontology-query-compute-2026)。
> **ℹ️ 注意: Legacy**

> The following sections describe the legacy compute model that was in effect before January 1, 2026. It is preserved for reference. For the current compute model, see [Ontology Query Compute (2026)](#ontology-query-compute-2026) above.
在旧版模型下，查询 ontology 的 compute-second 使用方式如下：

Under the legacy model, querying the ontology uses compute-seconds as follows:
* 固定的、用于查询开销的最低 compute-second 数量。

* 额外的、与查询服务所消耗的计算量成比例扩展的 compute-second 数量。

* A fixed, minimum number of compute-seconds for query overhead.
* An additional scaling number of compute-seconds, which are measured by the amount of compute used to service the query.
### Measuring compute with Object Storage V1 \[Legacy]
Object Storage V1 (Phonograph) 将数据存储在一个持久的、可横向扩展的集群中的一组分布式索引中。在这些索引中，数据驻留在大型数据结构中，由 Ontology 查询引擎进行遍历。当执行查询时，引擎可以通过遍历索引避免在搜索过程中处理大量数据。该过程被称为"pruning"（剪枝）。

Object Storage V1 (Phonograph) stores data in a distributed set of indices in a durable, horizontally scalable cluster. In these indices, data sits in large data structures that are traversed by the Ontology query engine. When a query is executed, the engine can avoid processing large swaths of data during its search by traversing the index. This process is known as "pruning".
使用此引擎，您可以通过评估最多减少 1000 倍的记录来搜索数十亿条记录。每一次对记录的物理评估称为一次 "hit"。Object Storage V1 旨在最小化每次查询中的 hit 数量。

Using this engine, you can search through billions of records by evaluating up to 1000x fewer records. Each physical evaluation of a record is called a "hit". Object Storage V1 is designed to minimize the number of hits in each query.
### Measuring compute with Object Storage V2 \[Legacy]
Object Storage V2 (OSv2) 以一种增强的索引格式存储对象，该格式由 Palantir 优化，可实现高速索引、Search Arounds 和 writeback，以及与多个 compute backend 的顺畅交接以完成复杂任务。这包括在查询中使用完全并行化的 Spark compute。

Object Storage V2 (OSv2) stores objects in an enhanced indexing format that is optimized by Palantir for high-speed indexing, Search Arounds, and writeback, as well as smooth hand-offs to multiple compute backends to accomplish complex tasks. This includes a combination of fully parallelized Spark compute as a part of a query.
鉴于 Object Storage V2 也使用了高效的索引结构，Object Storage V1 中关于 **hits** 的相同原理同样适用于基础查询。然而，compute-seconds 也可以被查询中按需启动的 Spark 容器使用。

Given that Object Storage V2 also uses an efficient indexing structure, the same principle of **hits** from Object Storage V1 applies on basic queries. However, compute-seconds can also be used by on-demand Spark containers that are spun up as a part of the query.
对 Object Storage V2 backend 中对象发起的查询按以下模式使用 compute：

Queries made to objects in the Object Storage V2 backend use compute in the following pattern:
* 对于 Object Storage V1 backend 中的对象，每次查询的最低 compute-second 开销为 `16` compute-seconds。

* 对于 Object Storage V2 backend 中的对象，每次查询的最低 compute-second 开销为 `4` compute-seconds。Object Storage V2 优化的结构所需开销比 Object Storage V1 更少，因此具有更低的最低 compute-second 开销。

* 当进程通过查询的剪枝过程执行计算工作时，需要额外的 compute-seconds。额外的 compute-seconds 随索引中的对象数量以及查询类型而变化。

* 在 Object Storage V2 (OSv2) 中，索引剪枝同样需要额外的 compute-seconds。然而，OSv2 还支持在单个请求中对超过 100,000 个对象运行 search-arounds，或对超过 10,000 个对象运行 writeback 操作时，使用按需 Spark 集群搜索。这些 Spark 集群的使用方式与平台上所有其他基于 Spark 的应用相同。有关说明，请参阅 [parallelized compute documentation](/docs/foundry/resource-management/usage-types/)。

* 在 Ontology 中具有 write-back 的 Action 存在最低开销。每个 action 具有 `18` compute-seconds 的 compute-second 开销。Action 的开销也会随 write-back 请求中编辑的对象数量而变化，除第一个对象外，每编辑一个对象会产生额外的 `1` compute-second。

* 通过 Functions on Objects 运行的 Function 存在最低开销。具体而言，每个 function execution 具有 `4` compute-seconds 的固定开销。

* A minimum compute-second overhead of `16` compute-seconds per query for objects in the Object Storage V1 backend.
* A minimum compute-second overhead of `4` compute-seconds per query for objects in the Object Storage V2 backend. The optimized structure of Object Storage V2 requires less overhead than Object Storage V1 and therefore has a reduced minimum compute-second overhead.
* Additional compute-seconds are required when the process does computational work through the pruning process of the query. The additional compute-seconds scale with the number of objects in the index as well as the type of query.
* In Object Storage V2 (OSv2), the index pruning similarly requires additional compute seconds. However, OSv2 supports also on-demand Spark cluster searches when running search-arounds on over 100,000 objects, or running writeback operations on over 10,000 objects in a single request. These Spark clusters utilize usage in the same way as all other Spark-based applications on the platform. See the [parallelized compute documentation](/docs/foundry/resource-management/usage-types/) for a description.
* Actions with write-back into the Ontology have a minimum overhead. Each action has a compute-second overhead of `18`. Actions also scale with the number of objects that are edited in the write-back request, incurring an additional `1` compute-second per object edited beyond the first.
* Functions run via Functions on Objects have a minimum overhead. Specifically, each function execution has a fixed overhead of `4` compute-seconds.
**下表总结了旧模型下每种查询类型的最低 compute-second 使用量。**

**The following table summarizes the minimum compute-second usage per query type under the legacy model.**
| Query Type          | Minimum compute-seconds          |
|---------------------|----------------------------------|
| Ontology V1 query   | 16                               |
| Ontology V2 query   | 4                                |
| Action on Objects   | 18                               |
| Function on Objects | 4                                |
## Understanding drivers of Foundry compute usage with Ontology queries \[Legacy]
* 作为一个非常简单的规则，每次查询的固定 compute 使用量随查询数量线性增长。执行较少的查询将整体使用更少的 compute。

* 对 object set service 的更复杂的查询（例如通用的多对象搜索）将针对每个 object type 启动多个子查询。将搜索限制在单个 object type 上，以减少您正在使用的查询数量。

* 对较小 object set 的查询使用的 compute 少于对较大 object set 的查询，因为查询中的 **hits** 数量与所查询 object set 的大小成正比。

* 在执行其他操作之前进行前置过滤将利用高度索引化的 backend 结构。这将减少查询中的 **hits** 数量，从而降低总体 compute 使用量。这对于 aggregations 和 Search Arounds 尤为重要，因为经过过滤的 object set 所需的 compute 处理量少于完整的 object set。

* As a very simple rule, the fixed compute-usage per query grows linearly with the number of queries. Performing fewer queries will use less compute in aggregate.
* More complex queries to the object set service, such as generic multi-object searches, will kick off multiple sub-queries to each object type. Limit your search to individual object types to reduce the number of queries you are using.
* Queries on smaller object sets will use less compute than those on larger object sets, as the number of **hits** in a query are proportional to the size of the object set being queried.
* Up-front filtering before performing other operations will take advantage of the highly indexed backend structure. This will reduce the number of **hits** in a query, reducing the overall compute usage. This is especially important with aggregations and Search Arounds, where filtered object sets require less compute to process than full object sets.
## Related resources
有关编写高效 function 和 Automate 配置以最小化 compute 使用量的最佳实践：

For best practices on writing efficient functions and Automate configurations that minimize compute usage:
* [Optimize function performance](/docs/foundry/functions/optimize-performance/)
* [Automate performance best practices](/docs/foundry/automate/performance-best-practices/)
* [Optimize function performance](/docs/foundry/functions/optimize-performance/)
* [Automate performance best practices](/docs/foundry/automate/performance-best-practices/)