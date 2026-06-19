<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/oss-limitations/
---
# Object Set Service limitations
Object Set Service (OSS) 是负责从 Ontology 中查询和检索对象的服务。OSS 使用分层执行策略来平衡性能和规模，根据查询的大小和复杂度自动选择最佳方案。

The Object Set Service (OSS) is the service responsible for querying and retrieving objects from the Ontology. OSS uses a tiered execution strategy to balance performance and scale, automatically selecting the optimal approach based on the size and complexity of your query.
本页说明了 OSS 如何处理不同大小的查询，以及在使用 object set 时应注意的限制。

This page explains how OSS handles queries of different sizes and the limitations you should be aware of when working with object sets.
## Query execution strategies
OSS 使用分层执行策略，自动选择处理查询的最佳方案：

OSS uses a tiered execution strategy that automatically selects the optimal approach for processing your query:
1. **下推到存储层（Pushdown to storage layer）：** 对于简单查询，OSS 将操作直接下推到存储层，以利用索引化的数据结构。这是最快的执行路径，并且只需要最少的计算开销。

1. **Pushdown to storage layer:** For simple queries, OSS pushes operations directly to the storage layer to take advantage of indexed data structures. This is the fastest execution path and requires minimal compute overhead.
2. **内存中执行（In-memory execution）：** 对于具有更复杂操作的查询，OSS 将数据加载到内存中以进行快速处理，但存在一定的容量上限。这对于中等规模的查询是最优的。

2. **In-memory execution:** For queries with more complex operations, OSS loads data into memory for fast processing up to a certain capacity. This is optimal for moderate-scale queries.
3. **基于 Spark 的执行（Spark-based execution）：** 对于超过内存容量的大规模查询，OSS 会自动回退到基于 Spark 的分布式计算。这使得处理更大的 object set 成为代价是额外的延迟和计算资源使用。

3. **Spark-based execution:** For large-scale queries that exceed in-memory capacity, OSS automatically falls back to Spark-based distributed compute. This enables processing of much larger object sets at the cost of additional latency and compute usage.
这些执行策略之间的转换是自动的，并基于多种因素：

The transition between these execution strategies is automatic and based on multiple factors:
* **Object set 大小：** 较大的集合会触发 Spark 执行

* **查询复杂度：** 某些高级功能（derived properties、中间 link types、interface Search Arounds）无论大小如何都需要 Spark 执行

* **可用计算资源：** OSS 会平衡性能和资源利用率

* **Object set size:** Larger sets trigger Spark execution
* **Query complexity:** Certain advanced features (derived properties, intermediary link types, interface Search Arounds) require Spark execution regardless of size
* **Available compute resources:** OSS balances performance and resource utilization
在单个复杂查询的不同执行阶段中，OSS 可能会使用多种执行策略。了解每种方法的阈值和限制将帮助您设计高效的查询并理解性能特征。

OSS may use multiple execution strategies within a single complex query for different stages of execution. Understanding the thresholds and limitations of each approach will help you design efficient queries and understand performance characteristics.
### OSS execution flow for Object Storage V2
下图说明了 OSS 如何根据您的查询选择适当的执行策略。根据每个阶段的复杂度，此决策过程可能在单个查询中执行多次：

The following diagram illustrates how OSS selects the appropriate execution strategy based on your query. This decision process may be executed multiple times within a single query, depending on the complexity of each stage:
![OSS execution flow diagram showing decision points and execution strategies.](/docs/resources/foundry/ontologies/oss-execution-flow.png)
**关键阈值：**

**Key thresholds:**
* **100,000 个对象（默认阈值）：** Search Arounds 和 derived properties 从内存执行切换到基于 Spark 的执行的阈值。

* **内部分页阈值：** 如果任何数据加载步骤需要从 Object Storage V2 加载超过 25 页数据，OSS 会回退到 Spark。

* **10,000,000 个对象（默认阈值）：** Search Around 操作的最大结果集大小（leaf limit）。

* **100,000 个对象（默认阈值）：** 使用 `.all()` 或 `.allAsync()` 将对象加载到内存的最大数量（OSDK 限制；`getAllObjects` API 可以加载更多）。

* **100,000 objects (default threshold):** Threshold for switching from in-memory to Spark-based execution for Search Arounds and derived properties.
* **Internal pagination threshold:** If any data loading step requires more than 25 pages of data from Object Storage V2, OSS falls back to Spark.
* **10,000,000 objects (default threshold):** Maximum result set size for Search Around operations (leaf limit).
* **100,000 objects (default threshold):** Maximum for loading objects into memory using `.all()` or `.allAsync()` (OSDK limitation; `getAllObjects` API can load more).
### Execution strategy comparison
| Strategy | When Used | Performance | Compute Cost | Use Cases |
|----------|-----------|-------------|--------------|-----------|
| **Pushdown to storage** | Simple filters and aggregations | Fastest | Lowest | Basic queries that can be resolved by indexed lookups |
| **In-memory execution** | Object sets ≤100k | Fast | Moderate | Most Search Arounds, moderate-scale queries |
| **Spark-based execution** | Object sets >100k | Slower (higher latency) | Higher | Large-scale Search Arounds, complex multi-step queries |
## Object set size limitations
OSS 根据存储后端和操作类型强制执行不同的大小限制。这些限制确保了系统稳定性和可预测的性能。

OSS enforces different size limits depending on the storage backend and operation type. These limits ensure system stability and predictable performance.
### Object Storage V1 (Phonograph) \[Planned deprecation]
> **⚠️ 警告: 计划中的弃用**

> Object Storage V1 (Phonograph) 处于[计划弃用](/docs/foundry/platform-overview/development-life-cycle/)阶段，将于 2026 年 6 月 30 日之后不可用。请将您的 [Object Type 和 Link Type](/docs/foundry/object-backend/osv1-osv2-migration/) 迁移至 Object Storage V2。
> **⚠️ 警告: Planned deprecation**

> Object Storage V1 (Phonograph) is in the [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be unavailable after June 30, 2026. [Migrate your object types and link types](/docs/foundry/object-backend/osv1-osv2-migration/) to Object Storage V2.
Object Storage V1 具有以下限制：

Object Storage V1 has the following limitations:
* **将 Object 加载到内存中：** 使用 [Functions on Objects](/docs/foundry/functions/overview/) 中的 `.all()` 或 `.allAsync()` 方法最多可加载 **100,000 个 Object**。

* **Search Around 操作：** 当从 Object Set A 执行 Search Around 到 Object Set B 时，结果集（Object Set B）不能超过 **100,000 个 Object**。

* **Loading objects into memory:** Maximum of **100,000 objects** can be loaded using `.all()` or `.allAsync()` methods in [Functions on Objects](/docs/foundry/functions/overview/).
* **Search Around operations:** When performing a Search Around from object set A to object set B, the result set (object set B) cannot exceed **100,000 objects**.
这些限制适用于 Object Storage V1 中的所有操作。对于较大的查询，不会自动回退到基于 Spark 的执行。

These limits apply to all operations in Object Storage V1. There is no automatic fallback to Spark-based execution for larger queries.
### Object Storage V2
Object Storage V2 通过其混合执行模型提供更大的灵活性和可扩展性：

Object Storage V2 provides greater flexibility and scale through its hybrid execution model:
* **内存执行：** 默认情况下，OSS 在内存中处理查询，最多支持 **100,000 个 Object** 的 Object Set。

* **基于 Spark 的执行：** 当 Search Around 操作涉及的 Object 超过 **100,000 个**时，OSS 会自动切换到基于 Spark 的分布式计算。

* **Search Around 结果限制：** 来自 Search Around 操作的结果集（从单个数据源加载的"叶子"Object Set）在每次单独的 Search Around 操作中不能超过 **1,000 万个 Object**。此外，查询执行期间跨所有数据集加载的 Object 总数不能超过 **3,000 万个 Object**。

* **将 Object 加载到内存中（OSDK 限制）：** 使用 Ontology SDK 中的 `.all()` 或 `.allAsync()` 方法加载 Object 时，最大限制为 **100,000 个 Object**，以防止内存耗尽和 Function 超时。您可以使用 `getAllObjects` API endpoints 加载更多 Object。

* **In-memory execution:** By default, OSS processes queries in-memory for object sets up to **100,000 objects**.
* **Spark-based execution:** When a Search Around operation involves more than **100,000 objects**, OSS automatically transitions to Spark-based distributed compute.
* **Search Around result limits:** The result set from a Search Around operation (the "leaf" object set being loaded from a single datasource) cannot exceed **10 million objects** per individual Search Around operation. Additionally, the total number of objects across all datasets loaded during query execution cannot exceed **30 million objects**.
* **Loading objects into memory (OSDK limitation):** When loading objects using `.all()` or `.allAsync()` methods in the Ontology SDK, the maximum is **100,000 objects** to prevent memory exhaustion and function timeouts. You can load more objects using the `getAllObjects` API endpoints.
> **ℹ️ 注意**

> 在 Functions on Objects 中加载超过 10,000 个 Object 可能会根据 Function 逻辑的复杂性导致执行超时。请考虑使用分页或过滤来减少 Object Set 大小。
> **ℹ️ 注意**

> Loading more than 10,000 objects in Functions on Objects may cause execution timeouts depending on the complexity of your function logic. Consider using pagination or filtering to reduce the object set size.
## Understanding Search Around result sets
当您执行 Search Around 操作以遍历 Object 之间的 Link 关系时，OSS 使用一种特殊类型的 join 操作来高效地查找相关 Object。

When you perform a Search Around operation to traverse a link relationship between objects, OSS uses a specialized type of join operation to efficiently find related objects.
例如，当您从一组 customer Object 搜索以查找通过 Link 关系关联的所有 order Object 时：

For example, when you search from a set of customer objects to find all related order objects through a link relationship:
* **起始 Set** 是您的 customer Object（您搜索的起点）

* **结果 Set** 是与这些 customer 关联的 order Object（您搜索的目标）

* The **starting set** is your customer objects (the objects you're searching from)
* The **result set** is the order objects that are linked to those customers (the objects you're searching to)
OSS 使用 left-semi join 来实现 Search Around 操作，该操作仅返回结果集中具有匹配 Link 的 Object，而不会复制起始 Set 中的数据。1,000 万 Object 的限制适用于此结果集——即遍历 Link 关系后返回的不同 Object 的总集合。

OSS implements Search Around operations using a left-semi join, which returns only the objects from the result set that have matching links, without duplicating data from the starting set. The 10 million object limit applies to this result set — the total collection of distinct objects returned after traversing the link relationship.
## Best practices for working within OSS limitations
为确保最佳性能并避免达到大小限制：

To ensure optimal performance and avoid hitting size limitations:
* **尽早过滤：** 在执行 join 或将 Object 加载到内存之前，应用过滤器以减少 Object Set 大小。OSS 利用索引数据结构使过滤查询更高效。

* **Filter early:** Apply filters to reduce object set sizes before performing joins or loading objects into memory. OSS takes advantage of indexed data structures to make filtered queries more efficient.
* **避免无法利用索引的操作：** 对派生 Property 和计算 SQL 列进行过滤、聚合、排序以及其他操作时，需要评估所有行且无法使用内部索引。这些操作不会使用快速下推路径，即使对于小型 Object Set 也可能触发内存或 Spark 执行。例如，如果您想要过滤发生在 2026 年 5 月的所有 order，请避免使用 `(MONTH FROM order_date) = 'May' AND (YEAR FROM order_date) = '2026'`。相反，请使用范围过滤：`order_date > '2026-05-01' && order_date < '2026-06-01'`。

* **Avoid operations that cannot leverage indexes:** Filtering, aggregations, sorting, and other operations on derived properties and computed SQL columns require evaluation of all rows and cannot use internal indexes. These operations will not use the fast pushdown path and may trigger in-memory or Spark execution even for small object sets. For example, if you want to filter for all orders that happened in May 2026, avoid using `(MONTH FROM order_date) = 'May' AND (YEAR FROM order_date) = '2026'`. Instead, use a range filter: `order_date > '2026-05-01' && order_date < '2026-06-01'`.
* **使用分页：** 在 Functions on Objects 中处理大型 Object Set 时，请使用分页模式以批量方式处理 Object，而不是一次性加载所有 Object。

* **Use pagination:** When working with large object sets in Functions on Objects, use pagination patterns to process objects in batches rather than loading all objects at once.
* **监控对象集大小：** 在执行诸如 Search Around 等开销较大的操作之前,使用聚合查询来了解对象集的大小。Search Around 操作的计算开销很大,这正是 OSS 强制实施这些大小限制的原因。

* **Monitor object set sizes:** Use aggregation queries to understand the size of your object sets before performing expensive operations like Search Arounds. Search Around operations are computationally expensive, which is why OSS enforces these size limits.
* **优化数据模型：** 如果您经常遇到大小限制,请考虑使用传统数据建模原则重构您的 Ontology。通过将相关数据整合到对象属性中来对 Ontology 进行反规范化,可以减少对开销较大的 Search Around 操作的需求,并使查询更加高效。您还可以创建更有针对性的 object type 或 link relationship,从而自然地产生更小的结果集。

* **Optimize data models:** If you frequently hit size limitations, consider restructuring your Ontology using traditional data modeling principles. Denormalizing your Ontology by consolidating related data into object properties can reduce the need for expensive Search Around operations and make queries more efficient. You can also create more targeted object types or link relationships that naturally produce smaller result sets.
* **考虑计算成本：** 基于 Spark 的执行比内存执行消耗更多的计算资源。触发 Spark 回退的查询将消耗额外的 [compute-seconds](/docs/foundry/ontologies/query-compute-usage/)。

* **Consider compute costs:** Spark-based execution uses more compute resources than in-memory execution. Queries that trigger Spark fallback will consume additional [compute-seconds](/docs/foundry/ontologies/query-compute-usage/).
> **ℹ️ 注意**

> OSS 使用大小估计来决定是否执行查询。如果估计的大小显著超过限制(超过 2 倍),查询可能会在达到确切阈值之前失败。这是一种性能优化措施,可以避免开销较大的精确计数操作。
> **ℹ️ 注意**

> OSS uses size estimation to determine whether to execute queries. If the estimated size significantly exceeds the limit (more than 2x), the query may fail before reaching the exact threshold. This is a performance optimization to avoid expensive exact counting operations.
## Related resources
* [Ontology 架构](/docs/foundry/object-backend/overview/)：了解更多关于 Object Set Service 及 Ontology 后端其他组件的信息。

* [Ontology 查询的计算使用情况](/docs/foundry/ontologies/query-compute-usage/)：了解不同的查询模式如何影响计算使用情况。

* [Functions on Objects](/docs/foundry/functions/overview/)：学习如何编写与对象集高效协作的 function。

* [Object sets API 参考](/docs/foundry/functions/api-object-sets/)：用于处理对象集的详细 API 文档。

* [Ontology architecture](/docs/foundry/object-backend/overview/): Learn more about the Object Set Service and other components of the Ontology backend.
* [Compute usage with Ontology queries](/docs/foundry/ontologies/query-compute-usage/): Understand how different query patterns affect compute usage.
* [Functions on Objects](/docs/foundry/functions/overview/): Learn how to write efficient functions that work with object sets.
* [Object sets API reference](/docs/foundry/functions/api-object-sets/): Detailed API documentation for working with object sets.