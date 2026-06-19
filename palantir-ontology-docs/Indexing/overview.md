<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-indexing/overview/
---
# Indexing
在 Ontology 中,**indexing** 是将 Foundry datasource 中的表格或其他形式的数据通过专用数据库使其可用于更快的数据检索操作的过程。

In the Ontology, **indexing** is the process of making tabular or other forms of data in Foundry datasources available for faster data retrieval operations through specialized databases.
本文档的这一部分描述了 Object Storage V2 的 indexing 过程,其中 indexing 由 Object Data Funnel 服务("Funnel")负责管理。Funnel 服务负责编排 Funnel pipelines,以在 Ontology 中创建和修改 object instances,并确保数据和 metadata 是最新的。

This section of documentation describes the indexing process for Object Storage V2, in which indexing is overseen by the Object Data Funnel service ("Funnel"). The Funnel service is responsible for orchestrating Funnel pipelines that create and modify object instances in the Ontology and ensure up-to-date data and metadata.
Funnel pipelines 主要有两种类型,**funnel batch pipelines** 和 **funnel streaming pipelines**,用户可以根据其 datasource 情况、延迟和工作流要求以及成本考虑,选择其中一种 indexing 机制。

There are two main types of funnel pipelines, **funnel batch pipelines** and **funnel streaming pipelines**, which allow users to adopt one or the other indexing mechanism depending on their datasource landscape, latency and workflow requirements, and cost considerations.
[了解更多关于 Funnel batch pipelines 的信息。](/docs/foundry/object-indexing/funnel-batch-pipelines/)

[Learn more about Funnel batch pipelines.](/docs/foundry/object-indexing/funnel-batch-pipelines/)
[了解更多关于 Funnel streaming pipelines 的信息。](/docs/foundry/object-indexing/funnel-streaming-pipelines/)

[Learn more about Funnel streaming pipelines.](/docs/foundry/object-indexing/funnel-streaming-pipelines/)
有关 Object Storage V1 (Phonograph) indexing 的信息,请查阅 [legacy documentation](/docs/foundry/object-databases/object-storage-v1/)。

For information about Object Storage V1 (Phonograph) indexing, review the [legacy documentation](/docs/foundry/object-databases/object-storage-v1/).