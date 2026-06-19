<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/overview-semantic-search/
---
# Semantic search
Semantic search 是一种基于固有含义或上下文来搜索文本的方法，而不是仅仅依赖关键字或其他传统搜索方法。

Semantic search is a way to search for text based on the inherent meaning or context, rather than relying solely on keywords or other traditional search methods.
Semantic search 通过使用 AI 模型将文本转换为向量（数字数组）来实现，这些向量称为"embeddings"。如果模型是有效的，那么在 N 维空间中彼此接近的向量（每个大小为 N）就是那些具有相似潜在或语义含义的向量。例如，"face mask" 的 embedding 向量将比 "respirator" 更接近 "face covering" 的 embedding 向量。

Semantic search is accomplished using AI models to transform the text into vectors, which are arrays of numbers, and are called "embeddings". If the model is effective, the vectors, each of size N, that are close to each other in N-dimensional space are the ones that have similar underlying or semantic meaning. For example, the embedding vector of “face mask” will be closer to the embedding vector of “face covering” than it is to “respirator.”
![Embeddings visualization.](/docs/resources/foundry/ontology/aip-embeddings-visualization.png)
如果嵌入的文本随后与 [Ontology](/docs/foundry/ontology/overview/) 中的特定对象相关联，那么您由搜索驱动的运营工作流将变得更加有用。查找相关实体或与特定搜索查询相关的实体，就是简单地在 N 维空间中找到最近的向量。

If the embedded text is then associated with a particular object in the [Ontology](/docs/foundry/ontology/overview/), then your search-driven operational workflows become much more useful. Finding related entities or entities related to a particular search query is simply finding the nearest vectors in N-dimensional space.
请查看以下文档页面以获取与 semantic search 相关的主题：

Review the following documentation pages for topics related to semantic search:
* [了解如何使用 Palantir 提供的模型创建 semantic search 工作流](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/)

* [了解如何使用自定义模型创建 semantic search 工作流](/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow/)

* [了解如何将 chunking 纳入您的 semantic search 工作流](/docs/foundry/ontology/document-processing/#chunking)

* [了解如何在 semantic search 工作流中使用 PDF](/docs/foundry/ontology/ontology-augmented-generation/)

* 有关其他学习材料，请参阅我们的 [YouTube 视频 "Building with Palantir AIP: Semantic Search" ↗](https://youtu.be/7rRLOTXe60Q) 和 [博客文章 "Building with Palantir AIP: Semantic Search" ↗](https://blog.palantir.com/building-with-palantir-aip-semantic-search-dc3adf40f6a6)。

* [Learn how to create a semantic search workflow using a Palantir-provided model](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/)
* [Learn how to create a semantic search workflow using a custom model](/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow/)
* [Learn how to incorporate chunking into your semantic search workflow](/docs/foundry/ontology/document-processing/#chunking)
* [Learn how to use PDFs in your semantic search workflow](/docs/foundry/ontology/ontology-augmented-generation/)
* For additional learning materials, see our [YouTube video on "Building with Palantir AIP: Semantic Search" ↗](https://youtu.be/7rRLOTXe60Q) and [blog on "Building with Palantir AIP: Semantic Search" ↗](https://blog.palantir.com/building-with-palantir-aip-semantic-search-dc3adf40f6a6).