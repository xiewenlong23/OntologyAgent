<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-indexing/funnel-batch-pipelines/
---
# Funnel batch pipelines
Funnel batch pipelines 是内部 job pipelines，以批处理方式协调数据的高效索引（来自 Foundry datasources 和用户编辑），将数据索引到 OSv2 中，确保 Ontology 中的数据和元数据保持最新。

Funnel batch pipelines are internal job pipelines that orchestrate the efficient indexing of data (both from Foundry datasources and from user edits) into OSv2 in a batch fashion, ensuring up-to-date data and metadata in the Ontology.
## Components of a Funnel batch pipeline
Funnel batch pipeline 由一系列 [Foundry build jobs](/docs/foundry/data-integration/datasets/) 组成：

A Funnel batch pipeline is comprised of a series of [Foundry build jobs](/docs/foundry/data-integration/datasets/):
* [Changelog](#changelog)
* [Merge changes](#merge-changes)
* [Indexing](#indexing)
* [Hydration](#hydration)
* [Changelog](#changelog)
* [Merge changes](#merge-changes)
* [Indexing](#indexing)
* [Hydration](#hydration)
下面的截图展示了一个 Funnel 批处理管道的示例。

The screenshot below shows an example Funnel batch pipeline.
![pipeline landing page](/docs/resources/foundry/object-indexing/pipeline1.png)
### Changelog
在 changelog 作业中，当 datasources 接收到新数据或 transactions 时，Funnel 会自动计算所有 datasources 的数据差异，然后在 Funnel pipeline 中创建中间 changelog datasets。Changelog datasets 接收 [APPEND transactions](/docs/foundry/data-integration/datasets/#transaction-types)，其中包含每个 transaction 中的数据差异，以提供 [incremental computation semantics](/docs/foundry/data-integration/datasets/#transaction-types)。这些 changelog datasets 由 Funnel 拥有和控制，因此用户无法访问。

In the changelog job, Funnel automatically computes the data difference for all datasources when the datasources receive new data or transactions, then creates intermediate changelog datasets in a Funnel pipeline. Changelog datasets receive [APPEND transactions](/docs/foundry/data-integration/datasets/#transaction-types) that contain the data difference in each transaction to provide [incremental computation semantics](/docs/foundry/data-integration/datasets/#transaction-types). These changelog datasets are owned and controlled by Funnel, and thus are not accessible to users.
### Merge changes
在 merge changes 作业中，来自 changelog 步骤的所有 changelog datasets 以及来自 Actions 的任何最近用户编辑，会通过 object type 的 primary key 进行 join，以合并所有更改并将其存储在另一个 dataset 中。这些合并后的 datasets 由 Funnel 拥有和控制，因此用户无法访问。

In the merge changes job, all changelog datasets from the changelog step and any recent user edits coming from Actions are joined by the object type’s primary key to merge all changes and store them in a separate dataset. These merged datasets are owned and controlled by Funnel, and thus are not accessible to users.
### Indexing
合并更改后，Funnel 会为每个 object database 启动一个 indexing 作业，将最终 dataset 中包含所有合并更改的所有行转换为与为该 object type 配置的 object databases 兼容的格式。例如，对于 canonical OSv2 database，上一步合并更改 dataset 中的所有行都会被转换为 index 文件；这些文件存储在另一个 index dataset 中。这些 index datasets 由 Funnel 拥有和控制，因此用户无法访问。

After changes are merged, Funnel starts an indexing job per object database to convert all rows in the final dataset with all merged changes into a format compatible with the object databases configured for the object type. For example, for the canonical OSv2 database, all of the rows in the merged changes dataset from the previous step are converted to index files; these files are stored in a separate index dataset. These index datasets are owned and controlled by Funnel, and thus are not accessible to users.
### Hydration
indexing 作业完成后，object databases 必须准备已索引的数据以供查询。以 OSv2 为例，此准备步骤涉及将 index 文件从 dataset 下载到 OSv2 database 搜索节点的磁盘中。此过程称为 *hydration*，是我们更新 object type 数据的示例 Funnel 批处理管道的最后一步。

Once the indexing job is complete, object databases must prepare the indexed data for querying. Using OSv2 as an example, this preparation step involves downloading the index files from the dataset into the disks of the OSv2 database search nodes. This process, known as *hydration*, is the final step of our example Funnel batch pipeline for updating the data of an object type.
hydration 作业的进度会在 Ontology Manager 应用程序中报告，如下面的截图所示。

The progress of the hydration job is reported in the Ontology Manager application, as seen in the screenshot below.
![pipeline hydration status](/docs/resources/foundry/object-indexing/pipeline2.png)
完成这些步骤后，object type 即可使用，并可被 Foundry 中的其他服务或外部服务查询。

Once these steps are completed, the object type is ready for use and can be queried by other services, externally or in Foundry.
## Live and replacement Funnel pipelines
当 object type 发生数据更新或 schema 更新时，会涉及两个独立的 Funnel pipelines。下面的截图显示了这两个 Funnel pipelines：

Two separate Funnel pipelines are involved when there is a data update or a schema update to an object type. The screenshot below displays these two Funnel pipelines:
![pipeline landing page](/docs/resources/foundry/object-indexing/pipeline1.png)
### Live pipelines
Funnel *live pipelines* 使用来自 Foundry datasources 的新数据更新生产环境中的 object types。Live pipelines 在其各自的 datasources 更新时运行。此外，如果检测到对 objects 的用户编辑，无论是否有任何显式的 backing dataset 更新，live pipelines 都会每六小时运行一次；这确保了用户编辑在 indexing 的 merge changes 步骤中持久化存储到 Funnel 拥有的 dataset 中。

Funnel *live pipelines* update object types in production with new data from Foundry datasources. Live pipelines run whenever their respective datasources are updated. Additionally, if user edits on objects are detected, live pipelines will run every six hours regardless of any explicit backing dataset update; this ensures that user edits are persisted during the merge changes step of indexing into the Funnel-owned dataset.
请注意，用户编辑会立即应用于 [object databases](/docs/foundry/object-backend/overview/#functional-components-and-architecture) 中的 indexes；常规的六小时间隔提供了一种内置的控制机制，用于将这些数据持久化存储在 Foundry 中。

Note that user edits are applied to indexes in [object databases](/docs/foundry/object-backend/overview/#functional-components-and-architecture) immediately; a regular six-hour job interval allows a built-in control mechanism to persistently store this data in Foundry.
### Replacement pipelines
当 object type 的 schema 发生变化，并且先前 pipeline 的 schema 不再是最新时，必须配置一个新的 *replacement pipeline* 来编排 object type 的更新。Schema 更改可以包括向 object type 添加新的 property type、更改现有的 property type，或将 object type 的 input datasource 替换为另一个 datasource。

When the schema of an object type changes and the previous pipeline’s schema is no longer up-to-date, a new *replacement pipeline* must be provisioned for orchestrating object type updates. Schema changes can include adding a new property type to an object type, changing an existing property type, or replacing the input datasource of an object type with another datasource.
虽然 live pipeline 继续按其通常的节奏运行，但 Funnel 将在后台编排一个 replacement pipeline，而不会影响向用户提供服务的 live 数据。在 replacement pipeline 首次成功运行后，live pipeline 将被丢弃并替换为 replacement pipeline；object type 的 schema 和 data 将相应更新。

While the live pipeline continues to run on its usual cadence, Funnel will orchestrate a replacement pipeline in the background without impacting the live data being served to users. After the replacement pipeline successfully runs for the first time, the live pipeline will be discarded and replaced by the replacement pipeline; the object type’s schema and data will be updated accordingly.
> **ℹ️ 注意**

> 虽然 schema 更改是 Funnel 配置 replacement pipeline 最常见的原因，但 Funnel 有时也会根据各种启发式方法出于性能原因自动配置 replacement pipeline。
> **ℹ️ 注意**

> Although schema changes are the most common reason for Funnel to provision a replacement pipeline, Funnel will sometimes automatically provision a replacement pipeline for performance reasons based on various heuristics.
## Incremental and full reindexing
> **ℹ️ 注意**

> 以下文档特定于 canonical Object Storage V2 data store。有关 Object Storage V1 (Phonograph) 的 indexing 行为的信息，请参阅 [OSv1 文档](/docs/foundry/object-databases/object-storage-v1/#incremental-and-batch-reindexing)。
> **ℹ️ 注意**

> The following documentation is specific to the canonical Object Storage V2 data store. For information on the indexing behavior of Object Storage V1 (Phonograph), see the [OSv1 documentation](/docs/foundry/object-databases/object-storage-v1/#incremental-and-batch-reindexing).
### Incremental indexing (default)
规范化的 Object Storage V2 数据存储会自动计算数据源中每个新事务的数据差异，并仅对新的数据更新进行增量索引。Funnel pipeline 默认对所有 Object Type 使用增量索引。与必须重新索引所有数据相比，增量索引允许 Funnel pipeline 运行得更快。

The canonical Object Storage V2 data store automatically computes the data difference for every new transaction in a datasource and incrementally indexes only new data updates. Funnel pipelines use incremental indexing by default for all object types. Incremental indexing allows the Funnel pipeline to run more quickly than if all data had to be indexed again.
例如，假设您有一个 Object Type，其中包含 100 个 objects，由一个 100 行的数据源支持。如果其中 10 行在新数据更新中发生了变化，[Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) 不会重新索引全部 100 个 objects（无论输入数据源中的 [transaction type](/docs/foundry/data-integration/datasets/#transaction-types) 如何），而会在 changelog dataset 中创建一个仅包含这 10 行已修改数据的新 `APPEND` 事务。

For example, imagine you have an object type with 100 objects, backed by a 100-row datasource. If 10 of those rows change in a new data update, rather than reindexing all 100 objects regardless of the [transaction type](/docs/foundry/data-integration/datasets/#transaction-types) in the input datasource, the [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) will create a new `APPEND` transaction in the changelog dataset that contains only the 10 modified rows.
#### Incremental indexing of incremental datasets
[Object Storage V2](/docs/foundry/object-backend/overview/#object-storage-v2-architecture) 在同步由增量数据集支持的 Object Type 时使用 "most recent transaction wins" 策略。如果数据集中同一主键包含多行，则最新事务中该行的数据将出现在 Ontology 中。单个事务中不能存在重复的主键。请注意，此行为与如何处理 [user edits and datasource update conflicts](/docs/foundry/object-edits/how-edits-applied/#resolve-conflicting-user-edits-and-datasource-updates) 无关。

[Object Storage V2](/docs/foundry/object-backend/overview/#object-storage-v2-architecture) uses a "most recent transaction wins" strategy when syncing object types backed by incremental datasets. If the dataset contains more than one row for the same primary key, the data of the row in the most recent transaction will be present in the Ontology. You may not have duplicate primary keys within a single transaction. Note that this behavior is not related to how [user edits and datasource update conflicts](/docs/foundry/object-edits/how-edits-applied/#resolve-conflicting-user-edits-and-datasource-updates) are handled.
考虑一个通过 `APPEND` 事务接收行更新的增量数据集，通常称为 changelog dataset。同一数据的新版本由一个具有更新值但主键相同的新行表示，并在同一事务中追加到该数据集。Changelog dataset 还可能包含一个 Boolean 类型的 `is_deleted` 列。当 `is_deleted` 列的值为 true 时，该行应被视为已删除。

Consider an incremental dataset that receives updates to rows through `APPEND` transactions, usually called a changelog dataset. A new version of the same data is represented by a new row with an updated value but the same primary key, appended to the dataset in one transaction. Changelog datasets may also have a `is_deleted` column of type Boolean. When the value of the `is_deleted` column is true, the row should be considered deleted.
Object Storage V2 按如下方式同步 changelog dataset：

Object Storage V2 syncs a changelog dataset as follows:
* 如果某个主键出现在多个事务中，则保留来自最近事务的行。
* 每个事务每个主键最多只能包含一行。

* 如果您的数据集是 Object Storage V1 changelog，Object Storage V2 将遵循 `is_deleted` 列，但不遵循 ordering 列。

* If a primary key appears in multiple transactions, the row from the most recent transaction will be kept.
* Each transaction must contain at most one row per primary key.
* If your dataset is a Object Storage V1 changelog, Object Storage V2 will respect the `is_deleted` column but not the ordering column.
您可能需要对 changelog dataset 执行增量窗口转换（incremental window transform），以确保每个事务每个主键最多包含一行。

You will likely need to perform an incremental window transform on your changelog dataset to ensure each transaction contains, at most, one row per primary key.
```python
from pyspark.sql.window import Window
from pyspark.sql import functions as F

ordering_window = Window().partitionBy('primary_key').orderBy(F.col('ordering').desc())
df = df.withColumn('rank', F.row_number().over(ordering_window))
df = df.filter((F.col('rank') == 1) & ~F.col('is_deleted'))
```
#### Views incremental indexing
[Dataset views](/docs/foundry/data-integration/views/) 在增量索引方面存在限制。由于 view 抽象了底层数据结构，Funnel 尝试使用增量构建以节省成本。但是，存在以下限制：

[Dataset views](/docs/foundry/data-integration/views/) have limitations with incremental indexing. Because a view abstracts the underlying data structure, Funnel attempts to use incremental builds to save costs. However, the following limitations apply:
* **带有 deletion 列的 view** 始终会被完全重新索引，因为 Funnel 无法确定哪些行已被删除。

* **当 deduplication 列值与事务顺序冲突时，增量构建可能产生不一致的结果**。Funnel 使用 "last edit wins" 策略：如果 deduplication 列值较大的行落在增量窗口之外，则会被忽略。为避免这种情况，可以添加一个 deletion 列以触发完全重新索引，或者确保 deduplication 列值随每个事务始终递增。

* 对底层数据集应用的 [**Retention policies that delete from the latest view**](/docs/foundry/retention/manage-retention-policies/#latest-view-transaction-deletion) 在删除旧数据时可能导致意外结果。在这种情况下，完全重新索引将产生正确的结果。

* **Views with deletion columns** are always fully reindexed because Funnel cannot determine which rows have been deleted.
* **Incremental builds may produce inconsistent results** when deduplication column values conflict with transaction ordering. Funnel uses a "last edit wins" strategy: rows with larger deduplication column values are ignored if they fall outside the incremental window. To avoid this, either add a deletion column to trigger full reindexes or ensure that deduplication column values always increase with each transaction.
* [**Retention policies that delete from the latest view**](/docs/foundry/retention/manage-retention-policies/#latest-view-transaction-deletion) on the underlying dataset may cause unexpected results if old data is removed. In such cases, a full reindex will produce correct results.
### Full reindexing (special cases)
在这些情况下，Funnel pipeline 将使用批量索引（重新索引所有 objects）：

Funnel pipelines will use batch indexing (in which all objects are reindexed) in these cases:
* 当同一事务中修改的输入数据源行数超过一定百分比时，与计算 changelog 并进行增量索引相比，重新索引的计算开销更小、速度更快。默认阈值设置为同一事务中更改的行数达到 80%。

* 当 Object Type schema 中的某些更改需要 [Funnel replacement pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/#replacement-pipelines) 时，将在后台创建一个全新的 Funnel pipeline（包括 OSv2 indexes）。

* 当用户通过 Ontology Manager 触发完全重新索引时。

* When more than a certain percentage of the rows in the input datasource are modified in the same transaction, reindexing can be computationally less expensive and faster compared to computing a changelog and indexing incrementally. The default threshold is set to 80% of rows changed in the same transaction.
* When certain changes in object type schemas require a [Funnel replacement pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/#replacement-pipelines), which will create an entirely new Funnel pipeline in the background (including OSv2 indexes).
* When user triggers a full reindex through Ontology Manager.
![Reindex option from the ... dropdown menu.](/docs/resources/foundry/object-indexing/reindex.png)
## Monitor Funnel pipelines
Funnel pipeline 由多个 build jobs 组成；[monitoring views](/docs/foundry/monitoring-views/overview/) 使用户能够通过创建一组 [monitoring rules](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule) 来跟踪 Funnel pipeline 中特定 job 的健康状况。

Funnel pipelines are comprised of multiple build jobs; [monitoring views](/docs/foundry/monitoring-views/overview/) enable users to track the health of specific jobs in Funnel pipelines by creating a set of [monitoring rules](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule).
用户可以在 Ontology Manager 中选择 **Monitor the health of this object type** 来创建 monitoring view。这会将用户带到 Data Health 应用程序的 [monitoring views](/docs/foundry/monitoring-views/overview/) 选项卡，如下方截图所示。

Users can create a monitoring view by selecting **Monitor the health of this object type** in the Ontology Manager. This takes users to the [monitoring views](/docs/foundry/monitoring-views/overview/) tab of the Data Health application, as seen in the screenshot below.
![pipeline monitor](/docs/resources/foundry/object-indexing/pipeline_monitor.png)
在 monitoring views 选项卡中，用户可以为 live pipeline 和 replacement pipeline 中的 job 创建监控规则。用户还可以添加 **Sync Propagation Delay** 规则，以便在 object databases 中索引数据的新鲜度超过规则中定义的阈值时收到通知。

From the monitoring views tab, users can create rules for monitoring jobs in both live pipelines and replacement pipelines. Users can also add **Sync Propagation Delay** rules to be notified when the freshness of the indexed data in object databases passes the threshold defined in the rule.
相比之下，Object Storage V1 (Phonograph) 使用 [health checks](/docs/foundry/maintaining-pipelines/recommended-health-checks/#optional-checks) 来监控 Ontology 实体的同步；OSv1 中 Object Type 只有一个 sync job，用户可以直接在这些 sync job 上定义这些 health check。

In contrast, Object Storage V1 (Phonograph) uses [health checks](/docs/foundry/maintaining-pipelines/recommended-health-checks/#optional-checks) to monitor syncs for Ontology entities; there is only a single sync job in OSv1 for object types, and users can define these health checks directly on the sync jobs.
## Debug a pipeline
Foundry 的构建任务可能因多种原因失败。对 object type 备份 datasource 拥有 `View` 权限的用户，可以通过 object type 的 **Datasources** 选项卡中的 **Live pipeline** 仪表板查看 pipeline 错误。在 pipeline 图中选择失败的任务，然后按下方截图所示选择 **Failed job**。

Foundry build jobs may fail for a number of reasons. Users with `View` permissions on the backing datasource of an object type can check the pipeline errors through the **Live pipeline** dashboard in the object type’s **Datasources** tab. Choose the failed job in the pipeline graph, then select **Failed job** as seen in the screenshot below.
![pipeline debugging](/docs/resources/foundry/object-indexing/pipeline3.jpg)
此外，用户也可以通过导航到 [Builds application](/docs/foundry/data-integration/application-reference/#builds) 应用程序并使用左侧面板的搜索筛选器按 object type 进行筛选，从而列出给定 object type 的所有构建任务。

Alternatively, users can list all build jobs for a given object type by navigating to the [Builds application](/docs/foundry/data-integration/application-reference/#builds) application and filtering by object type in the search filters on the left panel.
![builds search](/docs/resources/foundry/object-indexing/pipeline4.png)