<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/document-processing/
---
# Document processing
本页将讨论从 PDF 文档或图像中提取数据的一些实用注意事项。

This page will discuss a few useful considerations for extracting data from a PDF document or image.
## Data extraction
本页提供了一个使用 [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) 解析 PDF 以进行语义搜索的基本指南，并在您仅有文本内容时，提供了在 [Workshop](/docs/foundry/workshop/overview/) 应用中呈现信息的建议。

This page offers a basic guide for using [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) to parse PDFs for semantic search and includes a recommendation for presenting the information in a [Workshop](/docs/foundry/workshop/overview/) application when you just have text content.
Semantic search 是一种与 PDF 配合使用的强大工具，尤其是当内容被拆分为更小的"chunks"并分别进行 embedding 时，它能够帮助用户和工作流找到那些原本难以访问的重要信息。考虑到 PDF 中大量经常被忽视的非结构化知识，这一点尤为有用。

Semantic search is a powerful tool to use with PDFs, particularly if the content is broken down into smaller "chunks" that are embedded separately, helping users and workflows find important information that might otherwise be hard to access. This is especially useful considering the vast amount of unstructured knowledge in PDFs that often goes unnoticed.
使用时，只需将 PDF 上传到 Foundry，提取文本，对相同文本进行 chunking，搜索这些 chunks，并将搜索结果与对应渲染在侧边的 PDF 一起呈现，以便用户进行 source-of-truth 交叉验证。

To use, simply upload your PDFs to Foundry, extract the text, chunk the same text, search for those chunks, and surface the results of that search with the corresponding PDF rendered on the side for source-of-truth cross-validation for the users.
按照以下步骤导入 PDF 并从中提取文本：

Follow the steps outlined below to import PDFs and extract text from PDFs:
1. [将 PDF 作为 media set 导入](/docs/foundry/data-integration/media-sets/)。

2. [将 media set 添加到 Pipeline Builder](/docs/foundry/pipeline-builder/datasets-add/#add-data-from-foundry-to-pipeline-builder)。

3. 使用 **Get Media References** board。

1. [Import the PDFs as a media set](/docs/foundry/data-integration/media-sets/).
2. [Add the media set to Pipeline Builder](/docs/foundry/pipeline-builder/datasets-add/#add-data-from-foundry-to-pipeline-builder).
3. Use the **Get Media References** board.
![Get Media References board](/docs/resources/foundry/ontology/get-media-references.png)
4. 使用 **Text Extraction** board。

4. Use the **Text Extraction** board.
![Text Extraction board](/docs/resources/foundry/ontology/text-extraction.png)
## Chunking
本页面概述了如何将基本的 chunking 策略整合到您的 semantic search 工作流中。此处的 chunking 指的是将较大的文本拆分为较小的文本。这样做是有利的，因为 embedding 模型对文本有最大输入长度的限制，而且更重要的是，更小的文本在搜索时语义上会更加清晰。在解析 [PDF](#data-extraction) 等大型文档时，chunking 经常被使用。

This page outlines how to incorporate a basic chunking strategy into your semantic search workflows. Chunking, in this context, means breaking up larger pieces of text into smaller pieces of text. This is advantageous because embedding models possess a maximum input length for text, and crucially, smaller pieces of text will be more semantically distinct during searches. Chunking is often used when parsing large documents like [PDFs](#data-extraction).
主要目标是将长文本拆分为更小的"chunks"，每个 chunk 与一个关联的 Ontology object，该 object [linked](/docs/foundry/object-link-types/create-link-type/) 回原始 object。

Primarily, the objective is to split long text into smaller "chunks", each with an associated Ontology object [linked](/docs/foundry/object-link-types/create-link-type/) back to the original object.
## Chunking example
作为起点，我们将展示如何在 [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) 中不使用代码完成基本的 chunking 策略。对于更高级的策略，我们建议在 pipeline 中使用 [code repository](/docs/foundry/code-repositories/overview/)。

As a starting point, we will show how a basic chunking strategy can be accomplished without using code in [Pipeline Builder](/docs/foundry/pipeline-builder/overview/). For more advanced strategies, we recommend using a [code repository](/docs/foundry/code-repositories/overview/) as part of your pipeline.
为了便于说明，我们将使用一个简单的两行数据集，包含两列：`object_id` 和 `object_text`。为了便于理解，下面的 `object_text` 示例故意保持简短。

For illustrative purposes, we will use a simple two row dataset with two columns, `object_id` and `object_text`. For ease of understanding, the `object_text` examples below are purposefully short.
|object\_id|object\_text|
|---------|--------|
|abc|gold ring lost|
|xyz|fast cars zoom|
我们首先使用 **Chunk String** board 开始处理流程，它会引入一个额外的列，其中包含被分割为更小片段的 `object_text` array。该 board 支持多种 chunking 方法，例如 overlap 和 separators，以确保每个语义概念保持连贯和唯一。

We initiate the process by employing the **Chunk String** board, which introduces an extra column containing an array of `object_text` segmented into smaller pieces. The board accommodates various chunking approaches, such as overlap and separators, to ensure that each semantic concept remains coherent and unique.
下方 **Chunk String** board 的截图展示了一种简单策略，您可以根据自己的使用场景进行调整。下面的配置将尝试返回大小约为 256 个字符的 chunks。实际上，该 board 会按优先级最高的 separator 对文本进行拆分，直到每个 chunk 等于或小于 chunk size。如果没有更高优先级的 separator 可用于拆分，且某些 chunks 仍然过大，则会使用下一个 separator，直到所有 chunks 等于或小于 chunk size，或者没有更多 separator 可用。最后，该 board 会确保对于每个识别出的 chunk，其后续 chunk 会有一个 overlap，覆盖前一个 chunk 的最后 20 个字符。

The below screenshot of a **Chunk String** board shows a simple strategy which you may alter for use toward your own use case. The below configuration would attempt to return chunks that are roughly 256 characters in size. Effectively, the board splits text on the highest priority separator until each chunk is equal to or smaller than the chunk size. If there are no more highest priority separators to split on and some chunks are still too large, it moves to the next separator until either all the chunks are equal or smaller than the chunk size or there are no more separators to use. Finally, the board will ensure that for each chunk identified, the chunk following has an overlap that covers the last 20 characters of the previous chunk.
![Chunk string board](/docs/resources/foundry/ontology/chunk-string-board.png)
|object\_id|object\_text|chunks|
|---------|--------|-------|
|abc|gold ring lost|\[gold,ring,lost]|
|xyz|fast cars zoom|\[fast,cars,zoom]|
接下来，我们希望 array 中的每个元素都拥有自己的一行。我们将使用 **Explode Array with Position** board 将数据集转换为包含六行的数据集。每一行中的新列（如下所示）是一个 struct（map），包含两个 key-value 对：array 中的 position 和 element。

Next we want each element in the array to have its own row. We will use the **Explode Array with Position** board to transform our dataset to one with six rows. The new column in each of the rows (as seen below) is a struct (map) with two key-value pairs, the position in the array and the element in the array.
![Explode chunks.](/docs/resources/foundry/ontology/explode-chunks.png)
|object\_id|object\_text|chunks|chunks\_with\_position|
|---------|--------|-------|----------------------------------|
|abc|gold ring lost|\[gold,ring,lost]|{position:0, element:gold}|
|abc|gold ring lost|\[gold,ring,lost]|{position:1, element:ring}|
|abc|gold ring lost|\[gold,ring,lost]|{position:2, element:lost}|
|xyz|fast cars zoom|\[fast,cars,zoom]|{position:0, element:fast}|
|xyz|fast cars zoom|\[fast,cars,zoom]|{position:1, element:cars}|
|xyz|fast cars zoom|\[fast,cars,zoom]|{position:2, element:zoom}|
接下来，我们将 position 和 element 提取到它们各自的列中。

From there, we will pull out the position and the element into their own columns.
![Get chunk position.](/docs/resources/foundry/ontology/get-chunk-position.png)
![Get chunk.](/docs/resources/foundry/ontology/get-chunk.png)
|object\_id|object\_text|chunks|chunks\_with\_position|position|chunk|
|---------|--------|-------|----------------------------------|--|--|
|abc|gold ring lost|\[gold,ring,lost]|{position:0, element:gold}|0|gold|
|abc|gold ring lost|\[gold,ring,lost]|{position:1, element:ring}|1|ring|
|abc|gold ring lost|\[gold,ring,lost]|{position:2, element:lost}|2|lost|
|xyz|fast cars zoom|\[fast,cars,zoom]|{position:0, element:fast}|0|fast|
|xyz|fast cars zoom|\[fast,cars,zoom]|{position:1, element:cars}|1|cars|
|xyz|fast cars zoom|\[fast,cars,zoom]|{position:2, element:zoom}|2|zoom|
为了为每个 chunk 创建一个唯一标识符，我们将 chunk 在其 array 中的 position 转换为 string，然后将其拼接到原始 object ID 上。我们还将删除不必要的列。

To create a unique identifier for each chunk, we will convert the chunk position in its array to a string and then concatenate it to the original object ID. We will also drop the unnecessary columns.
![Cast chunk position to string.](/docs/resources/foundry/ontology/cast-chunk-position-to-string.png)
![Create chunk\_id.](/docs/resources/foundry/ontology/create-chunk-id.png)
![Drop unnecessary object\_text, chunks, position, and chunks\_with\_position columns.](/docs/resources/foundry/ontology/drop-unnecessary-columns.png)
|object\_id|chunk|chunk\_id|
|---------|-----|--|
|abc|gold|abc\_0|
|abc|ring|abc\_1|
|abc|lost|abc\_2|
|xyz|fast|xyz\_0|
|xyz|cars|xyz\_1|
|xyz|zoom|xyz\_2|
现在，我们有了六行，分别代表六个不同的 chunks，每个 chunk 都包含 `object_id`（用于 linking）、作为新 primary key 的新 `chunk_id`，以及将要被 embedding 的 `chunk`，如 [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type) 中所述。最终得到如下表格：

Now, we have six rows representing six different chunks, each with the `object_id` (for linking), the new `chunk_id` to be a new primary key, and the `chunk` to be embedded as described in [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type). This results in the table as follows:
|object\_id|chunk|chunk\_id|embedding|
|---------|-----|--|--|
|abc|gold|abc\_0|\[-0.7,...,0.4]
|abc|ring|abc\_1|\[0.6,...,-0.2]
|abc|lost|abc\_2|\[-0.8,...,0.9]
|xyz|fast|xyz\_0|\[0.3,...,-0.5]
|xyz|cars|xyz\_1|\[-0.1,...,0.8]
|xyz|zoom|xyz\_2|\[0.2,...,-0.3]