<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow/
---
# Using custom models to create a semantic search workflow
> **⚠️ 警告**

> 本教程适用于使用非 Palantir 提供的 embedding model 的用户，该工作流已不再被推荐。请参阅 [Palantir 提供的模型](/docs/foundry/aip/supported-llms/) 列表以及 [Palantir 提供模型的 semantic search 教程](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/)。
> **⚠️ 警告**

> This tutorial is for those using an embedding model not supplied by Palantir, which is no longer a recommended workflow. See the list of [Palantir-provided models](/docs/foundry/aip/supported-llms/) and the [Palantir-provided model semantic search tutorial](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/).
本页面说明了构建一个概念性的端到端文档搜索服务的过程，该服务能够在给定 prompt 时检索相关文档。该服务将使用 [Foundry modeling objective](/docs/foundry/model-integration/objectives/) 来嵌入文档并将其特征提取到向量中。这些文档和 embeddings 将存储在一个具有向量 property 的 object type 中。

This page illustrates the process of building a notional end-to-end documentation search service that is capable of retrieving relevant docs when given a prompt. The service will use a [Foundry modeling objective](/docs/foundry/model-integration/objectives/) to embed documents and extract their features into a vector. These documents and embeddings will be stored in an object type with the vector property.
在本例中，我们首先在 Foundry 中设置一个模型并创建一个 pipeline 来生成 embeddings。然后，我们将创建一个新的 object type 和一个 function，以通过自然语言对其进行查询。

For this example, we begin by setting up a model in Foundry and creating a pipeline to generate embeddings. Then, we will create a new object type and a function to query it through natural language.
我们从一个当前包含已解析文档和元数据（例如 `Document_Content` 和 `Link`）的数据集开始。接下来，我们将从 `Document_Content` 生成 embeddings，以便能够通过 semantic search 对其进行查询。

We begin with a dataset that currently has our parsed documents and metadata, such as `Document_Content` and `Link`. Next, we will generate embeddings from the `Document_Content` to enable us to query them via semantic search.
![Dataset to generate embeddings](/docs/resources/foundry/ontology/dataset-to-generate-embeddings.png)
要了解 KNN 功能的详细信息，请参阅 Foundry 文档中的 [KNN Functions on Objects](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) 部分。

To understand the details of the KNN feature, review [KNN Functions on Objects](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) section in the Foundry documentation.
> **✅ 成功: 值替换**

> 在整个工作流中，您可以替换为您选择的任何值，只要每个实例保持一致即可。例如，每个 `ObjectApiName` 实例始终替换为 `Document`。
> **ℹ️ 注意**

> **✅ 成功: Value substitution**
