<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/ontology-augmented-generation/
---
# Ontology-augmented generation
LLMs 在应用于特定业务场景时具有强大的能力。当面对某个任务时,第一步几乎总是找到应提供给 LLM 的相关上下文。找到相关上下文通常是设计检索增强生成系统中最具挑战性的部分。本节概述了一些常见的上下文检索方法。请注意,并不存在单一的"最佳方法",因为最佳解决方案在很大程度上取决于数据的具体情况。然而,这里概述的主题是一个很好的起点,可以根据需要进行修改和组合。

[PARA_1]
随着新模型代际的上下文长度增加,你可能根本不需要使用语义搜索,而是可以在 prompt 中直接传入完整上下文。例如,GPT-4o 的 128k 上下文窗口对应 300 多页文本。如果你应用程序的完整上下文在此限制范围内,我们建议你从不使用搜索开始。

[PARA_2]
要创建基本的语义搜索,请执行以下操作:

[PARA_3]
1. 遵循 [chunking](/docs/foundry/ontology/document-processing/#chunking) 策略。

2. 使用 [media reference](/docs/foundry/data-integration/media-sets/) property 创建 chunk 对象。

3. 作为 [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) 的一部分搜索 chunk。

4. 在 Workshop 中使用 [PDF Viewer widget](/docs/foundry/workshop/widgets-pdf-viewer/),并注意其配置选项。

[PARA_4]
有关 embeddings 的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type)

[PARA_5]
有关检索的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

[PARA_6]
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

LLMs are immensely powerful when applied to business-specific context. When presented with a certain task, the first step is almost always to find the relevant context that should be given to the LLM. Finding the relevant context is often the most challenging part of designing a retrieval augmented generation system. This section outlines some common approaches for context retrieval. Note there is no singular "best approach", as the best solution will be highly dependent on the specifics of the data. However, the themes outlined here are a good starting point and can be modified and combined as appropriate.
随着新模型代际的上下文长度增加,你可能根本不需要使用语义搜索,而是可以在 prompt 中直接传入完整上下文。例如,GPT-4o 的 128k 上下文窗口对应 300 多页文本。如果你应用程序的完整上下文在此限制范围内,我们建议你从不使用搜索开始。

[PARA_2]
要创建基本的语义搜索,请执行以下操作:

[PARA_3]
1. 遵循 [chunking](/docs/foundry/ontology/document-processing/#chunking) 策略。

2. 使用 [media reference](/docs/foundry/data-integration/media-sets/) property 创建 chunk 对象。

3. 作为 [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) 的一部分搜索 chunk。

4. 在 Workshop 中使用 [PDF Viewer widget](/docs/foundry/workshop/widgets-pdf-viewer/),并注意其配置选项。

[PARA_4]
有关 embeddings 的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type)

[PARA_5]
有关检索的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

[PARA_6]
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

With new model generations' increased context lengths, you may not need to use semantic search at all and can instead pass the full context in the prompt. For example, GPT-4o's 128k context window corresponds to 300+ pages of text. If your application's full context is within this limit, we recommend you start without search.
## Basic semantic search
要创建基本的语义搜索,请执行以下操作:

[PARA_3]
1. 遵循 [chunking](/docs/foundry/ontology/document-processing/#chunking) 策略。

2. 使用 [media reference](/docs/foundry/data-integration/media-sets/) property 创建 chunk 对象。

3. 作为 [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) 的一部分搜索 chunk。

4. 在 Workshop 中使用 [PDF Viewer widget](/docs/foundry/workshop/widgets-pdf-viewer/),并注意其配置选项。

[PARA_4]
有关 embeddings 的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type)

[PARA_5]
有关检索的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

[PARA_6]
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

To create a basic semantic search, do the following:
1. 遵循 [chunking](/docs/foundry/ontology/document-processing/#chunking) 策略。

2. 使用 [media reference](/docs/foundry/data-integration/media-sets/) property 创建 chunk 对象。

3. 作为 [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) 的一部分搜索 chunk。

4. 在 Workshop 中使用 [PDF Viewer widget](/docs/foundry/workshop/widgets-pdf-viewer/),并注意其配置选项。

[PARA_4]
有关 embeddings 的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type)

[PARA_5]
有关检索的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

[PARA_6]
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

1. Follow a [chunking](/docs/foundry/ontology/document-processing/#chunking) strategy.
2. Create the chunk objects with a [media reference](/docs/foundry/data-integration/media-sets/) property.
3. Search for the chunk as part of a [semantic search workflow](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/).
4. Use the [PDF Viewer widget](/docs/foundry/workshop/widgets-pdf-viewer/) in Workshop, noting the configuration options.
## Embeddings
有关 embeddings 的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type)

[PARA_5]
有关检索的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

[PARA_6]
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

For more information on embeddings, [review the documentation on using a Palantir-provided model to create a semantic search workflow.](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#generate-embeddings-and-create-object-type)
## Retrieval
有关检索的更多信息,[请查看关于使用 Palantir 提供的模型创建语义搜索工作流的文档。](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

[PARA_6]
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

For more information on retrieval, [review the documentation on using a Palantir-provided model to create a semantic search workflow.](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)
## Advanced retrieval
如果你发现与 AIP 关联的工具无法回答在文档语料库中应该能找到的问题,你首先应该调查是否检索到了相关上下文并将其传递到了 prompt 中。通常情况下,正是检索步骤未能呈现出最相关的上下文,导致 LLM 在后续步骤中给出了相应的响应。

[PARA_7]
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

If you are finding that your AIP-associated tool is failing to answer questions that should be found in the document corpus, you should first investigate whether the relevant context was retrieved and passed into the prompt. Often it is the retrieval step that fails to surface the most relevant context leading the LLM to respond appropriately in the subsequent step.
存在许多方法可以改善检索效果,这取决于数据和查询的内容,以下列出了一些:

[PARA_8]
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

Many approaches exist to improve the retrieval depending on the content of the data and queries, some of which are outlined below:
* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**

[PARA_9]
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

* **HyDE (Hypothetical Document Embeddings)**
* **Ranked keyword-based search**
* **Query augmentation**
* **Hybrid search**
### Technique consideration
这最终取决于你的具体用例要求以及你愿意投入多少时间。根据你的用例,可能最初简单的设置对你来说就足够好。否则,你可能只需添加 HyDE 和 semantic chunking,其余保持不变即可。我们的建议是从基础实现开始,然后根据需要添加功能。

[PARA_10]
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

This will ultimately depend on your specific use case requirements and how much time you are willing to invest. Depending on your use case, it could be that the original simple setup works well enough for you. Otherwise, you may just need to add HyDE and semantic chunking and leave the rest as it is. Our recommendation would be to start with the basic implementation, and then add features as it becomes necessary.
### HyDE (Hypothetical document embeddings)
改善检索性能的一种方法是 HyDE,即 Hypothetical document embeddings(假设性文档嵌入)。其核心思想是,不是直接对查询进行嵌入,而是先让 LLM 生成一个回答该问题的假设性 chunk,然后再对其进行嵌入。直观上,这有助于平衡查询和其答案之间的不对称性。你也可以阅读相关的学术论文 ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)。

[PARA_11]
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

One approach to improve retrieval performance is HyDE - otherwise known as Hypothetical document embeddings. The principle idea is that instead of embedding the query directly, you first ask an LLM to produce a hypothetical chunk that answers this question, which you then embed. Intuitively, this helps balance out the asymmetry between a query and its answer. You can also review the related academic journal titled ["Precise Zero-Shot Dense Retrieval without Relevance Labels" ↗](https://arxiv.org/abs/2212.10496)
在 chunk 以特定方式格式化以编码 [源文档和章节](/docs/foundry/ontology/document-processing/#chunking) 的特定情况下,这特别有用。

[PARA_12]
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

This can be particularly helpful in specific cases where chunks are formatted in a particular way to encode the [origin document and chapter](/docs/foundry/ontology/document-processing/#chunking).
举例来说,考虑以下 chunk 作为对问题"我们如何处理动物碰撞?"的适当回答:

[PARA_13]
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

As an example, consider the following chunk as an appropriate answer to the question: “How do we deal with animal collisions?”:
```
Claim Management - Motor: Animal Collision:
Animal collision claims are generally covered in type A, B, D policies. However,
exclusions apply...
```
我们将首先 prompt LLM 生成一个类似这样的假设性 chunk:

[PARA_14]
该 prompt 将返回类似下面的响应:

We would first prompt an LLM to generate a hypothetical chunk like so:
```
You are an insurance specialist assistant tasked to assist your colleagues with
finding relevant documents for their queries.

Given the following user query:
{query}

Produce a hypothetical paragraph answering it. Give your response in the following
format:
{Document Name}: {Chapter name}: {Section} > ...
{Content}

where {Document Name} is the name of the document that contains the passage,
{Chapter name} is the name of the chapter, {Section} is the name of the section
and {Content} is the content of the section.
```
该 prompt 将返回类似下面的响应:

This prompt would return us a response such as the following:
```
Animal Claims Management: General Terms:
Animal collision is commonly insured in fully comprehensive packages...
```
由于 LLM 的响应在结构上已经“更接近”真实答案，这使得其 embedding 更接近包含该真实答案的 chunk。我们在 function 中进行的 semantic search 看起来如下：

As the LLMs response is already “closer” to the real answer (structurally), it makes its embedding closer to the chunk that contains this real answer. Our semantic search in a function would then look like the following:
```TypeScript
async searchChunksByEmbedding(query: string, k: Integer): Promise<Chunk[]>> {
// create the full prompt for the hypothetical
const prompt = `...`

// generate hypothetical chunk
const hypothetical = await GPT_4o.createChatCompletion({messages: [{"role": "user", "contents": [{"text": prompt}]}]})
// embed the result
const embedding = await TextEmbeddingAda_002.createEmbeddings({inputs: [hypothetical]})
// use the embedding in the nearest neighbor search
const docs = Objects.search()
.chunks()
.nearestNeighbors(chunk => chunk.vectorProperty.near(embedding, {kValue: k})
.orderByRelevance()
.takeAsync(k)
return docs
```
### Ranked keyword-based search
诸如 OpenAI Ada 之类的通用 embedding 模型是在大量多样化数据上训练的。如果您的用例需要在特定领域语料库（例如制造业）上进行搜索，您可能会发现检索效果不如预期。这是由于通用 embedding 模型仅使用 embedding 空间的一小部分来表示特定领域。

Generic embedding models such as OpenAI Ada are trained on a large corpus of diverse data. If your use case requires search on a domain-specific corpus (for example, manufacturing), you may find that the retrieval does not work as well as expected. This is due to the generic embedding model only using a small part of the embedding space for a specific domain.
在这些情况下，fine-tuning 自定义模型是一种提升检索效果的方法，然而，一个更简单的开箱即用解决方案是使用 ranked keyword search，并可能结合一些 LLM 预处理。

Fine-tuning a custom model is one approach to improve retrieval in these cases, however, a much simpler out-of-the-box solution is to use a ranked keyword search, with potentially some LLM preprocessing.
这是因为 Object Storage v2 运行的 index 在给定查询时已经具备“relevance”的概念。这种 relevance 是相对于其他 chunks 的，这意味着它会自动考虑 chunk 的领域特定上下文。

This is because the index that Object Storage v2 runs on already comes with a notion of “relevance” when given a query. This relevance is *relative to other chunks*, meaning it automatically considers the domain-specific context of a chunk.
Objects 上的 Functions 支持按所述 relevance 对 Object 查询的结果进行排序，因此您可以编写如下 function：

Functions on Objects support ordering the results of Object queries by said relevance, so you can write a function like the following:
```TypeScript
async searchChunksByKeywords(query: string, k: Integer): Promise<Chunk[]> {
const chunks = Objects.search()
.chunks()
.filter(chunk => chunk.text.matchAnyToken(query))
.orderByRelevance()
.takeAsync(k)
return chunks
}

```
然而，这种方法抽象掉了 semantic search 中的 semantic 元素。例如，如果用户问“我们如何处理 **deer** collisions?”，而我们直接将该问题输入到 function 中，我们将找不到那些讨论一般 **animal** collision 的 chunks。LLM 可以通过 [query augmentation](#query-augmentation) 将 semantic 元素重新引入，如下所述。

However, this method abstracts away the semantic element of a semantic search. For example, if a user asks “How do we deal with **deer** collisions?” and we just input that directly into the function, we would not find chunks that talk about **animal** collision in general. LLMs can bring the semantic element back in through [query augmentation](#query-augmentation), described below.
### Query augmentation
Query 预处理是最大化返回结果相关性（relevancy）的重要步骤。本质上，您希望根据搜索类型将用户查询提炼为其核心组件。您可以考虑 [query enriching](#query-enriching)，另一个是 [query extraction](#query-extraction)。

Query pre-processing is an important step to maximize relevancy of returned results. In essence, you want to distill the user query into its core components dependent on the type of search. You can consider [query enriching](#query-enriching) and the other is [query extraction](#query-extraction).
#### Query enriching
在用户查询和传递给 keyword search 的内容之间注入一个 LLM 步骤，可以实现提炼查询以使其更具相关性的可能性：可以通过 prompt 让 LLM 去除停用词和无关的填充短语（如“Help me find ...”），并添加其他相关词汇或同义词。

Injecting an LLM step between the user query and what is passed to the keyword search allows the possibility of distilling the query to make it more relevant: the LLM can be prompted to remove stopwords and irrelevant filler phrases (“Help me find ...”), and add other related words or synonyms.
您可以设置如下 prompt：

You can set up a prompt like the following:
```
You are an insurance AI assistant tasked to help users find relevant documents.
To do so, you can use keyword-search in the company's internal database.

Given the following user query: {query}

Give a list of search terms that would find relevant results. Be sure to remove stop words,
and add synonyms and related terms to the most important terms.
Give your answer as a list of comma-separated values.
```
对于我们的示例问题 "How do we deal with animal collisions?"，LLM 的响应将是：

For our example question of "How do we deal with animal collisions?", the LLM's response would be:
```
deer, animal, collision, claims, wildlife, accidents, vehicle, damage, car, insurance, policy, coverage, comprehensive, reimbursement
```
这将允许用户找到那些从未提及 "deer collisions" 的文档，也能找到那些一般性地讨论 "animal"、"wildlife" 和 "accidents" 的文档。

This would allow users to find documents that never mention "deer collisions", but also those that talk about “animal", "wildlife", and "accidents" in general.
In code:
```TypeScript
async searchChunksByAugmentedKeywords(query: string, k: Integer): Promise<Chunk[]> {
// create the full prompt for the query augmentation
const prompt = `...`

const augmentedQuery = await GPT_4o.createChatCompletion({messages: [{"role": "user", "contents": [{"text": prompt}]}]})

const chunks = Objects.search()
.chunks()
.filter(chunk => chunk.text.matchAnyToken(augmentedQuery))
.orderByRelevance()
.takeAsync(k)
return chunks
}
```
#### Query extraction
Query augmentation 在 relevance-ordered keyword search 中效果良好。然而，对于 semantic search，您需要提取用户查询的核心诉求，并通过这样做，去除那些不提供 semantic 含义的额外词汇（例如停用词），并可能对查询词进行 [lemmatizing or stemming ↗](https://keremkargin.medium.com/nlp-tokenization-stemming-lemmatization-and-part-of-speech-tagging-9088ac068768)。

Query augmentation works well for relevance-ordered keyword search. For semantic search, however, you need to extract the core ask of the user query, and by doing so, remove extra terms that provide no semantic meaning such as stop words, and potentially [lemmatizing or stemming ↗](https://keremkargin.medium.com/nlp-tokenization-stemming-lemmatization-and-part-of-speech-tagging-9088ac068768) query terms.
为此，执行 query extraction，将问题转换为用户的核心诉求。

To do so, conduct query extraction to convert a question to the key ask of the user.
示例 prompt 如下：

An example prompt could be:
```
You are preparing a user-given query in order to perform a semantic search.
Extract the key user actions from the given query, removing unnecessary stop words
in the process.

Given the following user query: {query}

Return concatanated actions delimeted by full stops.
```
对于我们的示例问题 "How do we deal with animal collisions?"，LLM 将返回：

For our example question of “How do we deal with animal collisions?”, the LLM would return:
```
Deal with animal collisions.
```
此响应最大化了查询的语义内容，并增加了在运行语义搜索时获得更强匹配的下游可能性。上面的示例也可以通过仅移除停用词来解决。

This response maximizes the semantic content of our query and increasing likelihood of stronger matching downstream once we run a semantic search. The above example could also be solved by removing stopwords only.
```TypeScript
async searchChunksByExtractedQuery(query: string, k: Integer): Promise<Chunk[]> {
// create the full prompt for the query augmentation
const prompt = `...`

const augmentedQuery = await GPT_4o.createChatCompletion({messages: [{"role": "user", "contents": [{"text": prompt}]}]})
const embedding = await TextEmbeddingAda_002.createEmbeddings({inputs: [augmentedQuery]})

const chunks = Objects.search()
.chunks()
.nearestNeighbors(obj =>obj.embeddingProperty
.near(embedding, { kValue: k }))
.allAsync()
return chunks
}
```
#### Hybrid search: Combining semantic and keyword search with reciprocal rank fusion (RRF)
倒数排名融合 (RRF) 是一种简单的算法，用于将多种搜索类型的结果合并到单个列表中。本质上，它会给在给定列表中排名越高的文档越高的分数。总分数是各列表分数的总和。

Reciprocal rank fusion (RRF) is a simple algorithm to combine results from multiple search types into a single list. In essence, it gives a document a higher score the higher it is ranked in a given list. The total score is the sum of scores across lists.
`k` 起到正则化器的作用——k 越高，文档在列表中出现的*位置*就越不重要，而仅仅*出现在*列表中这一事实才重要。

`k` acts as a regularizer - the higher k, the less it matters *where* a document appears in a list, but merely *that* it appears in the list at all.
```
`RRFscore(d ∈ D) = Σ [1 / (k + r(d))]`

`# k is a constant that helps to balance between high and low ranking.`
`# r(d)is the rank/position of the document`
```
```TypeScript
public combineResultsWithRRF(vectorSearchResults: Chunk[], keywordSearchResults: Chunk[], k: Integer = 60): Chunk[] {

// define the RRF scoring function
const RRF = (r: number, k: number) => 1 / (r + k);

// initialize a map to keep track of the scores of each chunk
// note we assume later that each Chunk has a string primary key property "id"
const resultMap: Map<string, {chunk: Chunk, score: number}> = new Map();
const combinedResults: Chunk[] = [];

const searchResultsList = [vectorSearchResults, keywordSearchResults];

searchResultsList.forEach((searchResults) => {
searchResults.forEach((chunk, rank) => {
// calculate the score for each Chunk in the list
// and add it to the Chunk's total in the map
const rrfScore = RRF(rank, k);
const chunkData = resultMap.get(chunk.id) || {chunk: chunk, score: 0};

chunkData.score += rrfScore;
resultMap.set(chunk.id, chunkData);
});
});

// get all Chunks into a list
resultMap.forEach((chunkData) => {
combinedResults.push(chunkData.chunk);
});

// sort them by their score in the resultMap, in descending order
combinedResults.sort((a, b) => resultMap.get(b.id).score - resultMap.get(a.id).score);

return combinedResults;
}
```
一个完整的 hybrid search 实现如下所示：

A full hybrid search implementation would then look like the following:
```TypeScript
async hybridSearch(query: string, k: Integer, n1: Integer, n2: Integer): Promise<Chunk[]> {

// Start the keyword and vector searches in parallel
const keywordSearchResultsPromise = searchChunksByKeywords(query, n1)
const vectorSearchResultsPromise = searchChunksByEmbedding(query, n2)

const [keywordSearchResults, vectorSearchResults] = await Promise.all([keywordSearchResultsPromise, vectorSearchResultsPromise])

const rerankedResults = combineResultsWithRRF(vectorSearchResults, keywordSearchResults)

return rerankedResults.slice(0, k)
```