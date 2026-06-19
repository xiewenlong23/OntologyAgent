<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/aip-multimodal-and-embedding-models/
---
# Process multimodal and embedding models
本页讨论了您可用来处理多模态和嵌入模型的一些方法。

This page discusses some methods you can use to process multimodal and embedding models.
## Multimodal models
如果您想根据图表回答问题，具有 text-in-text-out 架构的 LLM 将毫无帮助。虽然 GPT-4o 和 GPT-4o mini 能够接受图像输入，但还有其他开源选项可供您考虑。

If you want to answer questions based on diagrams, LLMs with the text-in-text-out architecture will be of no help. While GPT-4o and GPT-4o mini are able to take image inputs, there are other open-source options available for your consideration.
* **[Pix2Struct ↗](https://proceedings.mlr.press/v202/lee23g/lee23g.pdf)：** 在对德语表格进行质量保证的初步测试中表现相当不错。您可以在 [huggingface ↗](https://huggingface.co/docs/transformers/main/en/model_doc/pix2struct) 上试用。

* **[Microsoft UDOP (Universal document processing) ↗](https://github.com/microsoft/UDOP)：** 开源，但在 huggingface 上不可用。

* **[Pix2Struct ↗](https://proceedings.mlr.press/v202/lee23g/lee23g.pdf):** Performed quite well during initial tests on quality assurance for a table in German. You can try it on [huggingface ↗](https://huggingface.co/docs/transformers/main/en/model_doc/pix2struct).
* **[Microsoft UDOP (Universal document processing) ↗](https://github.com/microsoft/UDOP):** Open source, but not available on huggingface.
在此设置中，您可以仅将初始文本提取用作（语义）搜索的内容，但随后在原始源页面（图像）之上运行多模态模型。

In this setup, you can use the initial text extraction just to have something to (semantic-)search for, but then later run the multimodal model on top of the raw source page (image).
## Embedding models
如果您使用英语工作，可以尝试 [**sentence-transformers docs** ↗](https://www.sbert.net/docs/pretrained-models/msmarco-v3.html) 中的 MSMARCO 模型。

If you are working in English, you can try MSMARCO models from the [**sentence-transformers docs** ↗](https://www.sbert.net/docs/pretrained-models/msmarco-v3.html).
[MS MARCO ↗](https://microsoft.github.io/msmarco/) 是基于使用 Bing 搜索引擎的真实用户搜索查询而创建的大规模信息检索数据集集合。所提供的模型可用于语义搜索，即给定关键词、搜索短语或问题，模型将找到与搜索查询相关的段落。

[MS MARCO ↗](https://microsoft.github.io/msmarco/) is a collection of large scale information retrieval datasets that were created based on real user search queries using the Bing search engine. The provided models can be used for semantic search, in that given keywords, a search phrase, or a question, the model will find passages that are relevant for the search query.
这意味着这些模型经过**专门训练，可以在嵌入空间中将查询和相关段落拉近距离**。

This means these models were **specifically trained to put queries and relevant passages close together in embedding space.**
根据这个定义，嵌入模型可能比通用的 OpenAI Ada 更适合从用户查询开始的语义搜索工作流。当您使用 Ada 直接嵌入查询并将其与 chunk 嵌入进行比较时，您比较的并非同一概念，因此可以使用非对称嵌入模型来弥补这一差距。或者，您可以尝试先使用 [LLM 生成一个假设 chunk](/docs/foundry/ontology/ontology-augmented-generation/#hyde-hypothetical-document-embeddings)。

By this definition, embedding models may be a better fit for semantic search workflows that start from a user query than general-purpose OpenAI Ada. When you use Ada to embed a query directly and compare that to chunk embeddings, you are not comparing the same concept and may instead use asymmetric embedding models to bridge that gap. Alternatively, you can attempt using an [LLM to get generate a hypothetical chunk](/docs/foundry/ontology/ontology-augmented-generation/#hyde-hypothetical-document-embeddings) first.
当您的起点是一个 chunk 并且正在搜索相似的 chunk 时，Ada 会更有意义。请注意，大多数非 Ada 嵌入模型仅支持 512 个 token，因此您需要相应地调整 chunking 策略。

Ada, in turn would make more sense when your starting point is a chunk, and you are searching for similar chunks. Note that most non-ada embedding models only support 512 tokens, so you need to adapt your chunking strategy accordingly.
例如，如果您使用德语工作，GPT 目前是唯一对该语言表现尚可的 LLM。对于德语文档语料库，请尝试 ada。

If you are working in German, for example, GPT is currently the only LLM that performs decently for the language. With a German document corpus, try ada.