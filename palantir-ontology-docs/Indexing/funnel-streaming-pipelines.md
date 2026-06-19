<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-indexing/funnel-streaming-pipelines/
---
# Funnel streaming pipelines
除了 [batch Ontology data indexing](/docs/foundry/object-indexing/funnel-batch-pipelines/) 之外，Object Storage V2 还支持通过使用 [Foundry streams](/docs/foundry/data-integration/streams/) 作为 [input datasources](/docs/foundry/object-permissioning/managing-object-security/#object-input-data-sources) 将低延迟流式数据索引到 Ontology 中。通过摆脱用于非流式 Foundry datasets 的批处理基础设施，streams 能够实现以秒或分钟为单位将数据索引到 Foundry Ontology，从而支持对延迟敏感的运营工作流。

In addition to [batch Ontology data indexing](/docs/foundry/object-indexing/funnel-batch-pipelines/), Object Storage V2 supports low-latency streaming data indexing into the Ontology by using [Foundry streams](/docs/foundry/data-integration/streams/) as [input datasources](/docs/foundry/object-permissioning/managing-object-security/#object-input-data-sources). By departing from the batch infrastructure used for non-streaming Foundry datasets, streams enable indexing of data into Foundry Ontology on the order of seconds or minutes to support latency sensitive operational workflows.
> **ℹ️ 注意**

> 如果您对 Ontology streaming behavior 有更多疑问，请查看我们的 [frequently asked questions](/docs/foundry/object-indexing/faq/#can-i-backfill-large-scale-historical-data-for-object-types-with-streaming-datasources) 文档。
> **ℹ️ 注意**

> If you have more questions about Ontology streaming behavior, review our [frequently asked questions](/docs/foundry/object-indexing/faq/#can-i-backfill-large-scale-historical-data-for-object-types-with-streaming-datasources) documentation.
> 有关 streaming pipeline 的性能和延迟方面的指导，请查看我们的 [streaming performance considerations](/docs/foundry/building-pipelines/streaming-performance-considerations/) 文档。
> For guidance on the performance and the latency of streaming pipelines, review our [streaming performance considerations](/docs/foundry/building-pipelines/streaming-performance-considerations/) documentation.
## Current product limitations of streaming object types
Object Storage V2 中的 streaming 采用"最新更新优先"（most recent update wins）策略，其中每个 stream 都被视为 changelog stream。如果您的 events 从源头传入时乱序，则最终会导致 Ontology 中的数据不正确。如果您能保证输入 stream 的顺序，Object Storage V2 streaming 将以相同的顺序处理您的更新。

Streaming in Object Storage V2 uses a “most recent update wins” strategy, where every stream is treated like a changelog stream. If your events are coming from your source out of order, you will end up with incorrect data in your Ontology. If you can guarantee order in your input stream, Object Storage V2 streaming will handle your updates with the same order.
Ontology streaming behavior 及其功能集仍在积极开发中；以下是使用 Ontology streaming 之前需要考虑的一些当前产品限制：

Ontology streaming behavior and its feature set is still actively developed; below are some of the current product limitations to consider before using Ontology streaming:
* streaming object types 不支持用户编辑。作为变通方案，您可以将用户编辑作为数据变更推送到输入 stream 中，或者配置一个带有非 streaming input datasource 的额外 object type，以便用户在该辅助 object type 上进行编辑。

* streaming object types 不支持 [Multi-datasource object types (MDOs)](/docs/foundry/object-permissioning/multi-datasource-objects/)。

* 除了 [Workshop](/docs/foundry/workshop/overview/) 之外，没有其他 Foundry 前端应用程序支持 live data refresh，因为从历史上看，它们不期望有 streaming updates。尽管对于 streaming object types 来说，底层的 Ontology 数据不断变化，但在 Workshop 之外的场景中，您需要在希望获取新数据时手动刷新。

* 在 Ontology Manager 中 object type 的 **Datasources** 选项卡中，用户可以为 Funnel 批处理 pipeline 失败和无效记录配置 [monitors](/docs/foundry/object-indexing/funnel-batch-pipelines/#monitor-funnel-pipelines)。目前，对于带有 stream datasources 的 object types，不支持 monitors 或 metrics（例如 pipeline latency）。

* record 大小不能超过 1MB，且 object type 不能包含超过 250 个 properties。如果您需要将更大的 records stream 到 ontology 中，您应考虑使用更小 object types 的不同 ontology model。

* User edits are not supported on streaming object types. As a workaround, you can either push user edits as a data change into the input stream or configure an additional object type with a non-streaming input datasource to let users make their edits on that auxiliary object type.
* [Multi-datasource object types (MDOs)](/docs/foundry/object-permissioning/multi-datasource-objects/) are not supported on streaming object types.
* Outside of [Workshop](/docs/foundry/workshop/overview/), no other Foundry frontend application supports live data refresh because, historically, they do not expect streaming updates. Although the underlying Ontology data is changing constantly for streaming object types, you will need to refresh whenever you want new data outside Workshop.
* In the **Datasources** tab of an object type in Ontology Manager, users are able to configure [monitors](/docs/foundry/object-indexing/funnel-batch-pipelines/#monitor-funnel-pipelines) for Funnel batch pipeline failures and invalid records. Currently, there is no support for monitors or metrics for object types with stream datasources (for example, pipeline latency).
* Record size cannot exceed 1MB, and the object type cannot contain more than 250 properties. You should consider a different ontology model with smaller object types if you need to stream larger records into your ontology.
## Configuring streaming object types
带有 stream input datasources 的 object types 直接在 [Pipeline Builder](/docs/foundry/pipeline-builder/outputs-add-ontology-output/) 或 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中进行配置，类似于任何其他 Foundry Ontology object type。

Object types with stream input datasources are configured directly in [Pipeline Builder](/docs/foundry/pipeline-builder/outputs-add-ontology-output/) or the [Ontology Manager](/docs/foundry/ontology-manager/overview/), similar to any other Foundry Ontology object type.
> **ℹ️ 注意**

> 如果您尚未配置 input stream，可以通过 [integrating with an existing stream in the Data Connection application](/docs/foundry/data-connection/set-up-streaming-sync/) 或 [building a stream pipeline in Pipeline Builder](/docs/foundry/building-pipelines/create-stream-pipeline-pb/) 来创建一个。
> **ℹ️ 注意**

> If you do not yet have an input stream configured, you can create one through [integrating with an existing stream in the Data Connection application](/docs/foundry/data-connection/set-up-streaming-sync/) or by [building a stream pipeline in Pipeline Builder](/docs/foundry/building-pipelines/create-stream-pipeline-pb/).
创建新的 object type（或使用现有的 object type）后，导航到 Ontology Manager 中的 **Datasources** 选项卡，在 **Backing datasource** 部分选择一个 stream input datasource（如下所示），然后将您的更改保存到 Foundry Ontology 中。

After creating a new object type (or using an existing object type), navigate to the **Datasources** tab in Ontology Manager, select a stream input datasource in the **Backing datasource** section as shown below, and save your changes into the Foundry Ontology.
![An Ontology streaming configuration](/docs/resources/foundry/object-indexing/stream_pipeline.png)
如需对 input datasource stream 进行其他配置，请选择省略号按钮以查看更多选项，如下所示。

For additional configurations over the input datasource stream, select the ellipses button for more options as shown below.
![Additional streaming configurations](/docs/resources/foundry/object-indexing/stream_config.png)
![Additional streaming configurations](/docs/resources/foundry/object-indexing/stream_datasource_configuration.png)
> **ℹ️ 注意**

> Stream datasources 也可以为 [many-to-many link types](/docs/foundry/object-link-types/create-link-type/) 进行配置。
> **ℹ️ 注意**

> Stream datasources can also be configured for [many-to-many link types](/docs/foundry/object-link-types/create-link-type/).
**Stream configuration** 部分提供了优化您的 object type streaming 任务的选项。

The **Stream configuration** section provides options to optimize your object type's streaming job.
* **Stream compute profile：** 默认情况下，object type 的 streaming 任务使用适合大多数 input streams 的 compute profile。然而，由非常高吞吐量 streams 支持的 object types 可能需要更多资源，以防止 pipeline 滞后。或者，由低吞吐量 streams 支持的 object types 可以使用较小的 profile 以节省 compute resource 成本。如果现有选项均不适用，请联系您的 Palantir 代表。

* **Stream consistency guarantee：** 默认情况下，object type 的 streaming 任务使用 exactly-once consistency guarantee，与 at-least-once 相比，这会带来额外的延迟，但可确保 Foundry applications 仅接收一次 object set updates。启用 at-least-once consistency guarantee 可以减少延迟；然而，在极少数情况下，当 object set 发生变化时，Foundry applications 可能会接收到重复的 updates。例如，基于 object set 的 automation 可能会被触发多次。对于延迟敏感的 object types，请考虑启用 at-least-once。

* **Stream compute profile:** By default, an object type's streaming job uses a compute profile suitable for most input streams. However, object types backed by very high-throughput streams may require more resources to prevent the pipeline from lagging. Alternatively, object types backed by low-throughput streams can use a smaller profile to save on compute resource cost. If none of the available options are suitable, contact your Palantir representative.
* **Stream consistency guarantee:** By default, an object type's streaming job uses the exactly-once consistency guarantee, which results in additional latency compared to at-least-once but ensures Foundry applications receive object set updates exactly once. Enabling the at-least-once consistency guarantee reduces latency; however, in rare cases, Foundry applications may receive duplicate updates when an object set changes. For example, an object set-based automation could trigger multiple times. Consider enabling at-least-once for latency-sensitive object types.
![The Stream configuration section.](/docs/resources/foundry/object-indexing/stream-configuration.png)
> **ℹ️ 注意**

> 修改 object type 的 stream 配置将重启其关联的流式处理任务，导致新流式记录的处理出现短暂延迟。
> **ℹ️ 注意**

> Modifying an object type's stream configuration will restart its associated streaming job, causing a temporary delay for new streaming records to be processed.
## Debugging streaming pipelines
Stream 与 Ontology 之间的 interface 在概念上可以类比为 [changelog datasets](/docs/foundry/object-indexing/funnel-batch-pipelines/#changelog)。输入 stream 中的每条记录都将包含要写入 Ontology 的每个 property 的数据。每条记录将通过 primary key 更新给定 object 的所有 properties。删除操作可以通过在输入 stream 上设置 metadata 来在输入记录上指定。

The interface between streams and the Ontology can be considered conceptually similar to [changelog datasets](/docs/foundry/object-indexing/funnel-batch-pipelines/#changelog). Each record in the input stream will contain the data for each property being written into the Ontology. Each record will update all of the properties for a given object, specified by primary key. Deletions can be specified on the input record by setting metadata on the input stream.
Funnel 将按照数据写入 datasource stream 的顺序对记录进行 indexing，因此这些 stream 应按 primary key 进行分区,并按事件时间戳进行排序,这可以在上游的 [Pipeline Builder](/docs/foundry/pipeline-builder/core-concepts/#pipeline-outputs) pipeline 中完成。

Funnel will index records in the order that they are written to the datasource stream, so those streams should be partitioned by primary key and ordered by event timestamp which can be done in the upstream [Pipeline Builder](/docs/foundry/pipeline-builder/core-concepts/#pipeline-outputs) pipeline.
如果您在使用 stream pipelines 时遇到问题,请查阅 [debug a failing stream](/docs/foundry/optimizing-pipelines/debug-stream/) 文档。

If you are having issues with your stream pipelines, review the [debug a failing stream](/docs/foundry/optimizing-pipelines/debug-stream/) documentation.
要查看 object type 流式任务的详细信息和 metrics,请在 pipeline 图中选择 **Stream** bubble。

To view details and metrics for an object type's streaming job, select the **Stream** bubble in the pipeline diagram.
![Access streaming job details and metrics.](/docs/resources/foundry/object-indexing/stream-details-metrics.gif)