<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/
---
# Using Palantir-provided models to create a semantic search workflow
> **ℹ️ 注意**

> 要使用 Palantir 提供的语言模型，必须先[在您的 enrollment 上启用 AIP](/docs/foundry/aip/enable-aip-features/)。您还必须拥有使用 [AIP developer capabilities](/docs/foundry/platform-overview/aip-capabilities/) 的权限。使用自定义模型？请查看[使用自定义模型创建语义搜索 workflow](/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow/)。
> **ℹ️ 注意**

> To use Palantir-provided language models, [AIP must first be enabled on your enrollment](/docs/foundry/aip/enable-aip-features/). You also must have permissions to use [AIP developer capabilities](/docs/foundry/platform-overview/aip-capabilities/). Using a custom model? Review [Using custom models to create a semantic search workflow](/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow/) instead.
本页面说明了使用[Palantir 提供的 embedding model](/docs/foundry/aip/supported-llms/)构建一个概念性的端到端 semantic search workflow 的过程。

This page illustrates the process of building a notional end-to-end semantic search workflow using a [Palantir-provided embedding model](/docs/foundry/aip/supported-llms/).
## Instructions
首先，您需要生成 embeddings 并将其存储在具有 [`vector` type](/docs/foundry/object-link-types/property-metadata/#property-base-types-with-limited-support) 的 object type 中。然后，您可以在 [Workshop](/docs/foundry/workshop/overview/) 中设置一个 semantic search workflow，构建一个 [AIP Chatbot Workshop widget](/docs/foundry/workshop/widgets-aip-chatbot/) 解决方案，或者创建一个自定义的 semantic search function 以在 [Workshop](/docs/foundry/workshop/overview/) 和 [AIP Logic](/docs/foundry/logic/overview/) 中使用。

To begin, you need to generate embeddings and store them in an object type with a [`vector` type](/docs/foundry/object-link-types/property-metadata/#property-base-types-with-limited-support). Then, you can set up a semantic search workflow in [Workshop](/docs/foundry/workshop/overview/), build an [AIP Chatbot Workshop widget](/docs/foundry/workshop/widgets-aip-chatbot/) solution, or create a custom semantic search function for use in [Workshop](/docs/foundry/workshop/overview/) and [AIP Logic](/docs/foundry/logic/overview/).
Prerequisite:
* [生成 embeddings 并创建 object type](#generate-embeddings-and-create-object-type)

* [Generate embeddings and create object type](#generate-embeddings-and-create-object-type)
Options:
* [使用 KNN object set 在 Workshop 中创建一个简单的 semantic search workflow（无需代码）](#create-a-simple-semantic-search-workflow-within-workshop-using-a-knn-object-set-no-code)

* [使 AIP Chatbot 能够对 objects 进行 semantic search（无需代码）](#use-aip-chatbot-no-code)

* [创建一个 function 以在 Workshop 和/或 AIP Logic 中跨 objects 进行 semantic search](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)

* [Create a simple semantic search workflow within workshop using a KNN object set (no-code)](#create-a-simple-semantic-search-workflow-within-workshop-using-a-knn-object-set-no-code)
* [Enable an AIP Chatbot to semantic search for objects (no-code)](#use-aip-chatbot-no-code)
* [Create a function to semantically search across objects for use in Workshop and/or AIP Logic](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)
## Generate embeddings and create object type
我们将使用 [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) 通过 [**Text to Embeddings** expression](/docs/foundry/pipeline-builder/pipeline-builder-aip/#text-to-embeddings) 将数据集中的文本嵌入为 vectors。该 expression 接收一个字符串，并使用其中一个 Palantir 提供的模型将其转换为 vector —— 在我们的例子中是 `text-embedding-ada-002` embedding model。

We will use [Pipeline Builder](/docs/foundry/pipeline-builder/overview/) to embed text in the dataset as vectors with the [**Text to Embeddings** expression](/docs/foundry/pipeline-builder/pipeline-builder-aip/#text-to-embeddings). The expression takes a string and converts it to a vector using one of the Palantir-provided models - in our case the `text-embedding-ada-002` embedding model.
![Text to Embedding](/docs/resources/foundry/ontology/text-to-embedding.png)
这些嵌入随后可以作为 vector property 添加到 Ontology 中。

These embeddings can then be added to the Ontology as a vector property.
![Configuring a vector property in a Pipeline Builder output object property](/docs/resources/foundry/ontology/embeddings-as-pipeline-builder-output-object-property.png)
如果您希望对使用 Palantir 提供的模型生成 embeddings 的过程进行更精细的控制,请参阅 [Python Transforms 中的语言模型](/docs/foundry/transforms-python-spark/palantir-provided-models/#embeddings)。

If you would like more control around the generation of embeddings using Palantir-provided models, see [Language models within Python Transforms](/docs/foundry/transforms-python-spark/palantir-provided-models/#embeddings).
## Create a simple semantic search workflow within workshop using a KNN object set (no-code)
> **ℹ️ 注意**

> KNN object set 无法按相关性排序。如果您需要有序的结果,请使用 [function approach](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)。
> **ℹ️ 注意**

> The KNN object set cannot be sorted by relevancy. If you need ordered results, use the [function approach](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic).
在 [Workshop](/docs/foundry/workshop/overview/) 中配置 [KNN object set](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) 是一种无需编写代码即可构建语义搜索工作流的简便方式。

Configuring a [KNN object set](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) within [Workshop](/docs/foundry/workshop/overview/) is an easy no-code way to build a semantic search workflow.
1. 创建一个 object set [variable](/docs/foundry/workshop/concepts-variables/),并选择包含 embedding property 的 object type。

2. 选择 filter `+ On a property` 选项,然后从菜单的 property 列表中选择您的 embedding property。

3. 选择后,应出现 K-nearest-neighbors 配置。如果未出现此配置,请验证您选择的 property 是否为 embedding property。

1. Create an object set [variable](/docs/foundry/workshop/concepts-variables/) and select the object type that contains an embedding property.
2. Select the filter `+ On a property` option, then from the list of properties in the menu, select your embedding property.
3. Once selected, the K-nearest-neighbors configuration should appear. If this configuration does not appear, verify that the property you selected is an embedding property.
![Workshop KNN config](/docs/resources/foundry/ontology/knn-config-workshop.png)
在此面板中,您可以配置:

Within this panel, you can configure:
* K-value:介于 1-100 之间的数字,用于指定语义搜索中返回的 object 数量。

* Query:用作执行语义搜索时查询字符串的 string variable。

* K-value: A number between 1-100 for how many objects to return in the semantic search.
* Query: The string variable to use as a query when performing the semantic search.
4. 接下来,创建一个 [string selector](/docs/foundry/workshop/widgets-string-selector/) widget,并将其输出 variable 添加到上面看到的 KNN query 选项中。

5. 最后,添加一个 [object table](/docs/foundry/workshop/widgets-object-table/) widget,并将其输入 variable 配置为新创建的 [KNN object set](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn)。

4. Next, create a [string selector](/docs/foundry/workshop/widgets-string-selector/) widget and add its output variable to the KNN query option seen above.
5. Lastly, add an [object table](/docs/foundry/workshop/widgets-object-table/) widget and configure its input variable to be the newly created [KNN object set](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn).
![Workshop KNN semantic search](/docs/resources/foundry/ontology/knn-workshop-semantic.png)
如需更自定义的语义搜索逻辑,请参阅 [functions 部分](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic)。

For more customized semantic search logic, see the [section on functions](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic).
## Use AIP Chatbot (no-code)
在 [AIP Chatbot Studio](/docs/foundry/chatbot-studio/overview/) 中创建的 AIP Chatbots(原 AIP Agents)非常适合在 object 上进行初步的语义搜索,因为它们不需要任何代码。了解更多关于 [以更可控的功能方式集成语义搜索](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic) 的信息。

AIP Chatbots (formerly AIP Agents) created in [AIP Chatbot Studio](/docs/foundry/chatbot-studio/overview/) are good for beginning semantic searches across your objects because they do not require any code. Learn more about [incorporating semantic search with more control over the functionality](#create-a-function-to-semantically-search-across-objects-for-use-in-workshop-andor-aip-logic).
按照 [getting started](/docs/foundry/chatbot-studio/getting-started/) 指南中的说明创建一个 AIP Chatbot,并添加 [Ontology context](/docs/foundry/chatbot-studio/retrieval-context/#ontology-context) 或 **Ontology semantic search** [tool](/docs/foundry/chatbot-studio/tools/#types-of-tools)。此初始设置将使您能够要求 AIP Chatbot 对 object 进行语义搜索。

Follow the instructions on the [getting started](/docs/foundry/chatbot-studio/getting-started/) guide to create an AIP Chatbot and either add [Ontology context](/docs/foundry/chatbot-studio/retrieval-context/#ontology-context) or an **Ontology semantic search** [tool](/docs/foundry/chatbot-studio/tools/#types-of-tools). This initial setup will enable you to ask the AIP Chatbot to semantically search the objects.
## Create a function to semantically search across objects for use in Workshop and/or AIP Logic
我们可以 [创建一个 typescript 仓库](/docs/foundry/functions/getting-started/) 并创建一个 function 来查询我们的 object type。总体目标是能够接收一些用户输入,使用与之前相同的 Palantir 提供的模型 [used earlier](#generate-embeddings-and-create-object-type) 生成一个向量,然后对我们的 object type 执行 [KNN search](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn)。有关如何导入 Palantir 提供的模型的更多信息,请参阅 [Functions 中的语言模型](/docs/foundry/functions/language-models/#embeddings)。

We can [create a typescript repository](/docs/foundry/functions/getting-started/) and create a function to query our object type. The overall goal is to be able to take some user input, generate a vector using the same Palantir-provided model [used earlier](#generate-embeddings-and-create-object-type), and then do a [KNN search](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn) over our object type. For more information on how to import Palantir-provided models, review [Language models within Functions](/docs/foundry/functions/language-models/#embeddings).
> **✅ 成功: Substitutions**

> 在下面的代码片段中,请将每个 `ObjectApiName` 实例替换为您唯一的 ObjectType。请注意,标识符有时可能以首字母小写的形式出现为 `objectApiName`。
> **✅ 成功: Substitutions**

> In the code snippet below, replace every instance of `ObjectApiName` for your unique ObjectType. Note that the identifier may sometimes appear as `objectApiName` with the first letter in lowercase.
> **⚠️ 警告: 为 functions 启用 vector properties**

> 在继续之前,请确保您的 Functions 代码仓库中的 `functions.json` 文件中存在条目 `"enableVectorProperties": true`。如果不存在该条目,请将其添加到 `functions.json` 中并提交更改以继续。如果您需要进一步的帮助,请联系您的 Palantir 代表。
> **⚠️ 警告: Enabling vector properties for functions**

> Before proceeding, ensure that the entry `"enableVectorProperties": true` is present in the `functions.json` file in your Functions code repository. If this entry is not present, add it to `functions.json` and commit the change to proceed. Contact your Palantir representative if you need further assistance.
### functions-typescript/src/index.ts
```typescript
import { Function, Integer } from "@foundry/functions-api";
import { Objects, ObjectApiName } from "@foundry/ontology-api";
import { TextEmbeddingAda_002 } from "@foundry/models-api/language-models"

export class MyFunctions {
@Function()
public async findRelevantObjects(
query: string,
kValue: Integer,
): Promise<ObjectApiName[]> {
if (query.length < 1) {
return []
}
const embedding = await TextEmbeddingAda_002.createEmbeddings({inputs: [query]}).then(r => r.embeddings[0]);

return Objects.search()
.objectApiName()
.nearestNeighbors(obj => obj.embeddings.near(embedding, {kValue: kValue}))
.orderByRelevance()
.take(kValue);
}
}
```
此时,我们有了一个可以通过自然语言查询 object 来运行语义搜索的 function。请记得 [发布该 function](/docs/foundry/functions/getting-started/#publish-your-functions),以便该 function 可以在 Foundry 中的任何位置使用。

At this point, we have a function that can run semantic search to query objects with natural language. Remember to [publish the function](/docs/foundry/functions/getting-started/#publish-your-functions) so the function can be used anywhere within Foundry.
### Use semantic search functions in Workshop
1. 首先[创建一个 Workshop application](/docs/foundry/workshop/getting-started/)。

2. 添加一个[文本输入 widget](/docs/foundry/workshop/widgets-text-input/)，用作已发布 KNN document fetch function 的输入。

3. 添加一个[object list widget](/docs/foundry/workshop/widgets-object-list/)，其输入为[由 function 生成的 object set](/docs/foundry/workshop/functions-use/#function-backed-variables-in-workshop) 以及所选输入，如下所示：

1. Start by [creating a Workshop application](/docs/foundry/workshop/getting-started/).
2. Add a [text input widget](/docs/foundry/workshop/widgets-text-input/), which will be used as an input to the published KNN document fetch function.
3. Add an [object list widget](/docs/foundry/workshop/widgets-object-list/) with an input [object set generated from the function](/docs/foundry/workshop/functions-use/#function-backed-variables-in-workshop) and the selected inputs as shown below:

> 📷 **[图片: KNN Function to generate object set]**

> 📷 **[图片: KNN Function to generate object set]**

4. 将 `kValue` 设置为您希望返回的结果数量，但不得超过[指定的限制](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn)。

4. Set the `kValue` to however many results you want returned, subject to the [specified limits](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn).
### Use Semantic Search functions in AIP Logic
将已发布的 function 添加为 AIP Logic 中的一个 [tool](/docs/foundry/logic/getting-started/#use-a-logic-function)。使用与以下类似的 prompt 指示语言模型使用该 tool：

Add the published function as a [tool](/docs/foundry/logic/getting-started/#use-a-logic-function) within AIP Logic. Instruct the language model to use the tool with a prompt similar to this:
> Use the fetchRelevantObjects tool with a kValue of 5 to find the most related objects. Remember to add quotes around query when using the tool.