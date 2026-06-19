<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-indexing/faq/
---
# FAQ
## How do I know when an object type has been indexed into OSv2?
Ontology Manager 应用程序具有一个专用的 pipeline graph，用于显示 Funnel pipeline 中各种 job 的状态。graph 中 Object Storage V2 节点上的绿色对勾表示 indexing 已完成，并且 object type 已准备好可以从 OSv2 进行查询。

The Ontology Manager application has a dedicated pipeline graph that shows the status of various jobs in a Funnel pipeline. A green tick in the Object Storage V2 node in the graph indicates that the indexing is complete and the object type is ready to be queried from OSv2.
![Indexing Status v2](/docs/resources/foundry/object-indexing/faq_indexing.png)
## Why might an indexing job fail even though it was successfully registered with Object Storage V1 (Phonograph) before?
OSv1 和 OSv2 中的 data validation 略有不同。

Data validations in OSv1 and OSv2 differ slightly.
OSv1 的行为通常由底层 data store 的行为决定，因为它与底层分布式文档存储和搜索引擎紧密耦合。OSv2 具有更严格的 validation，以确保进入 Ontology 的数据质量，并与 OSv1 相比提供更具确定性的行为和更高的系统可读性。

OSv1 behavior is generally dictated by the behavior of the underlying data store, given its tight coupling with the underlying distributed document store and search engine. OSv2 has stricter validations to ensure the quality of data going into the Ontology, and to provide more deterministic behavior and increased legibility across the system compared to OSv1.
因此，某些 indexing pipeline 在使用 OSv2 时可能会遇到 validation error，而这些 error 以前在 OSv1 中是可以接受的。有关此类 breaking change 的详细列表，请参阅关于 [OSv1 和 OSv2 之间 Ontology breaking change](/docs/foundry/object-backend/object-storage-v2-breaking-changes/) 的文档。

Therefore, some indexing pipelines may encounter validation errors when using OSv2 that were previously accepted by OSv1. For a detailed list of such breaking changes, see the documentation on [Ontology breaking changes between OSv1 and OSv2](/docs/foundry/object-backend/object-storage-v2-breaking-changes/).
## One of the jobs failed but might succeed if I retry. How do I trigger a rebuild?
OSv2 管理 job 的所有方面，包括 job 重试。如果 job 由于可能在重新构建后解决的暂时性错误而失败，OSv2 将在大约五分钟后自动重试该 job。如果 OSv2 检测到 job 发生终止性失败（例如由于数据格式无效），则仅在有新数据可用时才会自动重试。在 object type 由 restricted view datasource 支持的情况下，当数据或 policy 发生变化时，job 就会被触发。

OSv2 manages all aspects of jobs, including job retries. If a job fails due to a transient error that might be resolved by rebuilding the job, OSv2 will automatically retry the job after approximately five minutes. If OSv2 detects that the job failed terminally (due to an invalid data format, for example), it will automatically retry only when new data is available. In cases where object types are backed by restricted view datasources, jobs are triggered when either the data or the policy changes.
## Is there a limit to the size of data that can be indexed?
index 大小主要受给定 object type 索引到的 object database 中存储空间的限制。例如，在 OSv2 data store 中，这将是 search node 的磁盘空间。

The index size is mainly limited by the storage space in the object databases into which a given object type is indexed. For example, in the OSv2 data store this would be the disk space of the search nodes.
如果没有足够的磁盘空间，indexing job 将无法成功，并会在 Ontology Manager 应用程序的 pipeline graph 中报告底层问题。如果遇到磁盘空间错误，请联系您的 Palantir 代表。

If there is not enough disk space, indexing jobs will not succeed and will report the underlying problem in the pipeline graph in the Ontology Manager application. If you encounter disk space errors, contact your Palantir representative.
## Can I backfill large scale historical data for [object types with streaming datasources](/docs/foundry/object-indexing/funnel-streaming-pipelines/)?
同步由 streaming datasource 支持的 object type 时有两个阶段：内部流创建（internal stream creation）和 indexing。Streaming indexing job 的 indexing 延迟与 [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) 相当，使用 Spark 来高度并行化历史 streaming 数据的初始处理。此 indexing 延迟与 [live Ontology data 上的 user edit](/docs/foundry/object-edits/how-edits-applied/#user-edits-on-live-data) 相当。Internal stream creation 通常是限制因素；它利用我们的流式基础架构按记录处理 datasource。

There are two phases when syncing object types backed by streaming datasources; internal stream creation, and indexing. Streaming indexing jobs have comparable indexing latency to [Funnel batch pipelines](/docs/foundry/object-indexing/funnel-batch-pipelines/), using Spark to heavily parallelize the initial processing of historical streaming data. This indexing latency is comparable to [user edits on live Ontology data](/docs/foundry/object-edits/how-edits-applied/#user-edits-on-live-data). Internal stream creation is typically the limiting factor; it utilizes our streaming infrastructure to process the datasource on a per-record basis.
## What is the expected latency for streaming into the Ontology?
[Funnel streaming pipeline](/docs/foundry/object-indexing/funnel-streaming-pipelines/) 中最耗时的部分是 Flink checkpointing，以实现"恰好一次"（exactly once）的流式一致性。默认的 checkpoint 频率是每秒一次，因此这是数据到达输入流和索引到 Ontology 之间的主要延迟来源。我们持续进行实验，通过降低 checkpoint 频率甚至完全移除它来评估成本/性能/延迟的权衡。

The most time-consuming part of [Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) is Flink checkpointing to allow for "exactly once" streaming consistency. The default checkpoint frequency is once every second, so that is the dominating latency between the data arriving in the input stream and being indexed into the Ontology. We perform continuous experiments to evaluate cost/performance/latency tradeoffs by reducing the frequency and even removing it all together.
如有必要，请联系 Palantir Support 来配置相关行为。

Contact Palantir Support to configure the behavior where necessary.
## What is the expected throughput for streaming into Ontology?
每个 object type 到 [Object Storage v2 object database](/docs/foundry/object-backend/overview/#object-storage-v2-architecture) 的 indexing throughput 限制为 2 MB/s。如果您需要更高的 indexing throughput，请联系 Palantir Support。

Indexing throughput is limited to 2 MB/s per object type into the [Object Storage v2 object database](/docs/foundry/object-backend/overview/#object-storage-v2-architecture). Contact Palantir Support if you need a higher indexing throughput.
## Can I specify a timestamp that my objects will be deduplicated by when using stream datasources in the Ontology?
不可以，[Funnel streaming pipeline](/docs/foundry/object-indexing/funnel-streaming-pipelines/) 在 indexing 时会保留输入流的顺序。数据应按顺序写入流中。这可以在上游 streaming pipeline 中通过按事件时间戳对数据进行 windowing 并指定 primary key 来实现，从而使数据进行 hash partition。

No, [Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) preserve the ordering of the input stream when indexing. Data should be written to the stream in order. This can be done in the upstream streaming pipeline by windowing the data by the event timestamp and specifying the primary keys such that the data is hash partitioned.
## Does Ontology streaming support change data capture (CDC) workflows?
[Funnel streaming pipeline](/docs/foundry/object-indexing/funnel-streaming-pipelines/) 支持 create、update 和 deletion workflow。您可以在 [change data capture](/docs/foundry/data-integration/change-data-capture/) 文档中找到有关如何设置 deletion metadata 的更多文档。

[Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) supports create, update, and deletion workflows. You can find more documentation on how to set up deletion metadata in the [change data capture](/docs/foundry/data-integration/change-data-capture/) documentation.
## Can I write partial rows to the Ontology when using stream datasources? Can I update a few properties at a time instead of providing the entire object?
目前不可以。整个 object 的解析应在上游 pipeline 中完成。如果 [stateful streaming](/docs/foundry/building-pipelines/stream-vs-batch/#state-management) 由于规模问题无法为您解决此问题，请联系 Palantir Support。

Currently, no. Resolving the entire object should be done in an upstream pipeline. If [stateful streaming](/docs/foundry/building-pipelines/stream-vs-batch/#state-management) does not solve this problem for you due to scale issues, contact Palantir Support.
## Can I use Ontology streaming for [many-to-many link types](/docs/foundry/object-link-types/create-link-type/)?
是的，该功能受支持。在我们的文档中了解更多关于如何配置流式数据源的本体类型的信息 [in our documentation](/docs/foundry/object-indexing/funnel-streaming-pipelines/#configuring-streaming-object-types)。

Yes, it is supported. Learn more about how to configure ontology types with streaming datasources [in our documentation](/docs/foundry/object-indexing/funnel-streaming-pipelines/#configuring-streaming-object-types).
## Is streaming supported for [object databases](../object-databases/) other than [Object Storage v2](/docs/foundry/object-backend/overview/#object-storage-v2-architecture) ([materializations](/docs/foundry/object-edits/materializations/) or [Automate](/docs/foundry/automate/overview/), for example)?
Ontology streaming 目前仅受 Object Storage v2 object database 支持。如果您需要在其他 object databases 中使用此功能，请联系 Palantir Support。

Ontology streaming is currently only supported by the Object Storage v2 object database. Contact Palantir Support if you need this functionality in other object databases.
## Are [materializations](/docs/foundry/object-edits/materializations/) supported for object types with stream datasources?
不支持；由于具有 stream datasources 的 object types 不支持用户编辑，materialized dataset 与 stream 中的 archive dataset 不会有任何区别。在当前架构下，无法提供 dataset 中的去重视图。

No; given user edits are not supported for object types with stream datasources, a materialized dataset would be no different than the archive dataset in the stream. With the current architecture, the deduplicated view in a dataset cannot be provided.
## My [Funnel streaming pipeline](funnel-streaming-pipelines.md) is always running. How can I cancel it?
Funnel streaming pipelines 无法被用户取消。Funnel 始终保持 streams 处于活跃状态，因为生产环境中的 object types 需要高可用性。在原型设计阶段，这种设置可能会产生不必要的费用。如果这成为您用例的重大阻碍，请联系 Palantir Support。或者，您可以在原型设计阶段将 object type 切换为 batch 模式。

Funnel streaming pipelines cannot be cancelled by users. Funnel keeps streams alive always because production object types require high availability. This setup may potentially incur unwanted cost when prototyping. Contact Palantir Support if this becomes a significant deterrent for your use case. Alternatively, you can try switching the object type to a batch one during the prototyping phase.
## How can I cut over my stream datasource from one stream to another without downtime?
[Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) 拥有一个启发式机制，用于在切换到新 stream 之前判断其 pipeline 是否与替换 stream "保持同步"。您可以通过以下步骤更改 datasource 以指向不同的 stream 或 stream 的分支：

[Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) have a heuristic to determine if its pipeline is “up to date” with a replacement stream before switching over to the new one. You can change the datasource to point to a different stream or branch of your stream with the following steps:
1. 在单独的 stream（或另一个分支）上运行您的新逻辑。

2. 等待新 stream 完成 replay，例如在所有历史记录处理完毕之后。

3. 将您的 object type input datasource 更改为新的 stream。

4. Funnel streaming pipelines 将保持原始 stream 上的 live pipeline 运行，直到新 stream 上的替换 pipeline 完全索引完毕。

5. Funnel 完成切换后，您可以关闭原始 stream。

1. Run your new logic on a separate stream (or another branch).
2. Wait for the new stream to finish the replay, such as after all historical records are processed.
3. Change your object type input datasource to the new stream.
4. Funnel streaming pipelines will keep the live pipeline on the original stream up until the replacement pipeline on the new stream is fully indexed.
5. Once the Funnel has finished the cutover, you can turn off the original stream.
## What are some common mistakes that may lead to unintended consequences?
1. 如果您的数据与预期不符，请确保您的 input stream 按预期排序。

2. [Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) 执行与 [Funnel batch pipelines](/docs/foundry/object-indexing/funnel-batch-pipelines/#) 相同的验证。但是，对于流式 pipeline，由于 stream processing 无法暂停，user transform 中没有抛出错误的机制，因此无效的记录将被丢弃。

1. If your data is inconsistent with what you expect, ensure that your input stream is ordered the way you expect.
2. [Funnel streaming pipelines](/docs/foundry/object-indexing/funnel-streaming-pipelines/) perform the same validations as [Funnel batch pipelines](/docs/foundry/object-indexing/funnel-batch-pipelines/#). However, for streaming pipelines, there is no mechanism to throw an error in the user transform because the stream processing cannot be paused, so the invalid records are dropped.
## What is the cost of Ontology streaming?
[Funnel streaming pipeline](/docs/foundry/object-indexing/funnel-streaming-pipelines/) 的 compute 计算方式与普通流式资源相同。请参阅我们的 [streaming compute usage](/docs/foundry/building-pipelines/streaming-compute-usage/#calculating-usage) 文档，了解有关流式资源成本的更多信息。

[Funnel streaming pipeline](/docs/foundry/object-indexing/funnel-streaming-pipelines/) compute is calculated the same way as normal streaming resources. Review our [streaming compute usage](/docs/foundry/building-pipelines/streaming-compute-usage/#calculating-usage) documentation for more information on streaming resource costs.
## How do retention windows work?
Retention windows 最初是在 beta 版本中作为一种数据大小限制机制开发的。因此，它仅作为尽力而为的实现。这意味着 retention window 内的 objects 是可查询的，但超出该范围的 objects 最终将被删除。例如，如果 retention window 设置为两周，而 stream datasource 的某个 object 上次由 input stream 更新是在三周前，则该 object 可能会从该 object type 中删除。但是，该 object 也可能在 Ontology 中保留更多天，并且不保证在任何特定时间范围内被删除。

Retention windows were initially developed as a data size limiting mechanism during a beta release. Therefore, it is only implemented as a best effort. This means objects within the retention window will be queryable, but objects outside of it will be eventually deleted. For example, if the retention window is set to two weeks, and an object of the stream datasource was last updated by the input stream three weeks ago, that object may be deleted from that object type. However, that object may also stay in the Ontology for many more days and is never guaranteed to be removed within any specific timeframe.
当前从 Ontology 中"清理"旧数据的机制是通过 [pipeline replacement](/docs/foundry/object-indexing/funnel-batch-pipelines/#replacement-pipelines)，默认每两周运行一次。在 replacement 时，Funnel streaming pipeline 会从 retention window 的开始处 replay 该 stream，从而从 Ontology 中移除较旧的 objects。如果您需要更频繁地删除旧 objects，请联系 Palantir Support。

The current mechanism for "cleaning up" old data from the Ontology is through [pipeline replacement](/docs/foundry/object-indexing/funnel-batch-pipelines/#replacement-pipelines) which, by default, runs every two weeks. On replacement, the Funnel streaming pipeline replays the stream from the beginning of the retention window, thereby removing older objects from the Ontology. Contact Palantir Support if you have a need to delete old objects more regularly.
如果未设置 retention window，则 input stream source 中的所有数据都将被导入到 Ontology 中。

If no retention window is set, then all data from the input stream source will be ingested into the Ontology.
## Why is my stream source being indexed in batch or failing with duplicate errors?
在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中，您必须始终明确将 input data source 指定为 stream；这同时适用于具有流式 datasources 的 object types 以及由 streams 支持的 [restricted views](/docs/foundry/object-permissioning/configuring-rv-access-controls/)。否则，您的 data source 将回退为以标准的 [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) 方式进行索引。有关更多详细信息，请参阅我们关于 [configuring streaming object types](/docs/foundry/object-indexing/funnel-streaming-pipelines/#configuring-streaming-object-types) 的文档。

In [Ontology Manager](/docs/foundry/ontology-manager/overview/), you must always explicitly specify your input data source as a stream; this applies for both object types with streaming datasources and [restricted views](/docs/foundry/object-permissioning/configuring-rv-access-controls/) backed by streams. Otherwise, your data source will fall back to indexing as a standard [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/). Review our documentation on [configuring streaming object types](/docs/foundry/object-indexing/funnel-streaming-pipelines/#configuring-streaming-object-types) for more details.
## Can I query object types with streaming datasources through [Ontology functions](/docs/foundry/functions/functions-on-objects/)?
是的，[querying the Ontology](/docs/foundry/object-backend/overview/#object-set-service-oss) 对 streaming object types 和 batch object types 的工作方式相同。

Yes, [querying the Ontology](/docs/foundry/object-backend/overview/#object-set-service-oss) work the same way for streaming object types and batch object types.