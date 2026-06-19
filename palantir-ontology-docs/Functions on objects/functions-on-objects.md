<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/functions-on-objects/
---
# Functions on objects (FOO)
Foundry 中的 functions 原生支持访问和修改 Ontology 中 objects 和 links 的数据。在 Ontology 中定义 object 和 link types 后,你可以将这些 types 导入 functions 仓库,以自动生成 code bindings。这些 code bindings 包括对以下内容的支持:

Functions in Foundry natively support accessing and modifying data from objects and links in the Ontology. After defining object and link types in the Ontology, you can import these types into a functions repository to have code bindings automatically generated. These code bindings include support for:
* 将 object 和 object set types 作为 [parameters](/docs/foundry/functions/types-reference/#ontology-types) 传递给 function

* 使用 [Object set APIs](/docs/foundry/functions/api-object-sets/) 按需搜索 object sets

* 使用 [OntologyEditFunctions](/docs/foundry/functions/edits-overview/) 修改 objects

* Passing object and object set types into a function as [parameters](/docs/foundry/functions/types-reference/#ontology-types)
* Searching for object sets on demand using the [Object set APIs](/docs/foundry/functions/api-object-sets/)
* Modifying objects using [OntologyEditFunctions](/docs/foundry/functions/edits-overview/)
由于对 Ontology 的这种原生支持,Foundry 中的 functions 远远超越了常用的 Functions-as-a-Service (FaaS) 平台,提供了对数据存储、检索和修改的原生支持——所有这些都受 Foundry 对数据安全、lineage 和透明度的保证约束。

Because of this native support for the Ontology, functions in Foundry go far beyond commonly used Functions-as-a-Service (FaaS) platforms by providing native support for data storage, retrieval, and modification—all subject to Foundry's guarantees for data security, lineage, and transparency.
[了解如何开始使用 object functions。](/docs/foundry/functions/foo-getting-started/)

[Learn how to get started with functions on objects.](/docs/foundry/functions/foo-getting-started/)
> **ℹ️ 注意**

> 术语 "functions on objects"(有时称为 "FOO")被宽泛地用于指代读取 object 数据的 functions,无论是作为 parameter 还是使用 object search,但在 Foundry 中并没有正式的 "function on objects" 概念区别于任何其他 function。
> **ℹ️ 注意**

> The term "functions on objects" (sometimes referred to as "FOO") is used loosely to refer to functions that read object data, either as a parameter or using an object search, but there is no formal notion of a "function on objects" in Foundry as being distinct from any other function.