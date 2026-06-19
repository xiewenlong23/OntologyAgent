<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/language-feature-support/
---
# Feature support by language
并非所有 features 都受所有语言支持。有关按语言划分的 feature 支持情况，请参阅下表。

Not all features are supported by all languages. Refer to the chart below for feature support by language.
| Functions capability by language | AIP Logic | TypeScript v1 | TypeScript v2 | Python | Description                                                                                                                                       |
|----------------------------------|-----------|---------------|---------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Ontology object support          | Yes       | Yes           | Yes           | Yes    | The ability to [access Ontology objects](/docs/foundry/functions/foo-getting-started/) in your function.                                                              |
| Ontology interfaces support      | No        | No            | Yes           | No     | The ability to access and edit Ontology interfaces in your function.                                                   |
| Ontology edits support           | Yes       | Yes           | Yes           | Yes    | The ability to [edit Ontology objects](/docs/foundry/functions/edits-overview/) in your function.                                                                     |
| Queryable in Workshop            | Yes       | Yes           | Yes           | Yes    | Invoking a function from a [Workshop application](/docs/foundry/workshop/functions-use/).                                                                  |
| Usable in Pipeline Builder       | No        | No            | No            | Yes    | Calling a function from [Pipeline Builder pipelines](/docs/foundry/functions/python-functions-builder/).                                                              |
| Functions on models support      | Yes       | Yes           | No            | No     | Executing live deployment models [from a function](/docs/foundry/functions/functions-on-models/).                                                                     |
| Semantic search support          | Yes       | Yes           | Yes            | Yes     | Use functions to create vectors for [semantic search](/docs/foundry/ontology/overview-semantic-search/).                                                   |
| Webhook support                  | No        | Yes           | No            | No     | The ability to call [webhooks from functions](/docs/foundry/functions/webhooks/).                                                                                     |
| External API call support        | No        | Yes           | Yes           | Yes    | Querying external services from [within functions](/docs/foundry/functions/api-calls/).                                                                               |
| Serverless execution support     | Yes       | Yes           | Yes           | Yes    | A serverless function will be spun up on demand when invoked.  Refer to [serverless functions](#serverless-functions) below for more information. |
| Deployed execution support       | No        | No            | Yes            | Yes    | A deployed function will have dedicated resources allocated to it, ready to serve requests.                                                       |
| Call function from API gateway   | Yes       | Yes           | Yes           | Yes    | The ability to hit a [query function](/docs/foundry/functions/query-functions/) from the API gateway.                                                                 |
| Marketplace support              | Yes       | Yes           | Yes           | Yes    | The ability to package and ship functions in [Marketplace](/docs/foundry/marketplace/overview/).                                                           |
| Bring-your-own-model             | Yes       | Yes           | No            | No     | The ability to register a function [as a model](/docs/foundry/aip/bring-your-own-model/). The [function interface method](/docs/foundry/aip/chat-completion-function-interface-quickstart/) is a legacy approach that applies to TypeScript v1 only.                                                                  |
## Ontology SDK support
Python 和 TypeScript v2 functions 支持 [Ontology SDK](/docs/foundry/ontology-sdk/overview/)（OSDK）。OSDK 允许你直接从开发环境中利用 Ontology，并提供多种 [benefits](/docs/foundry/ontology-sdk/overview/#osdk-benefits)，例如与 Developer Console 的兼容性以及 OSDK 版本管理。我们建议使用 Python 或 TypeScript v2 来在 functions 仓库中获取这些 benefits。

Python and TypeScript v2 functions support the [Ontology SDK](/docs/foundry/ontology-sdk/overview/) (OSDK). The OSDK allows you to leverage the Ontology directly from your development environment and provides [benefits](/docs/foundry/ontology-sdk/overview/#osdk-benefits) such as compatibility with Developer Console and OSDK versioning. We recommend using Python or TypeScript v2 to access these benefits in your functions repository.
## TypeScript v1 vs. TypeScript v2
TypeScript v1 和 TypeScript v2 都允许用户利用 TypeScript 的核心语言特性，但在支持的平台 features 方面存在差异，如上面的 feature 支持表所示。我们建议使用 TypeScript v2 functions 构建工作流，以利用相对于 TypeScript v1 的几项关键改进：

Both TypeScript v1 and TypeScript v2 allow users to leverage TypeScript's core language features, but there are differences in supported platform features, as shown in the feature support table above. We recommend building workflows using TypeScript v2 functions to take advantage of several key improvements over TypeScript v1:
* **在完整 Node.js 运行时中的 serverless 执行：** TypeScript v2 functions 在 Node.js 环境中运行，支持 `fs`、`child_process` 和 `crypto` 等核心模块。这使得与文件交互、并行执行 CPU 密集型任务或需要其他系统级操作的 NPM 库具有更好的兼容性。

* **一流的 OSDK 支持：** OSDK 现在可以在 TypeScript v2 functions 中无缝使用，使得在平台内外都能轻松重用代码。它还为处理大规模 Ontology 数据提供了更高效的 API。

* **可配置的资源请求：** TypeScript v2 functions 允许你请求最多 8 个 vCPU 和 5GB 内存，从而对性能和可扩展性提供更大的控制。

* **Serverless execution in a full Node.js runtime:** TypeScript v2 functions run in a Node.js environment, supporting core modules like `fs`, `child_process`, and `crypto`. This enables greater compatibility with NPM libraries that interact with the file system, perform CPU-intensive tasks in parallel, or require other system-level operations.
* **First-class OSDK support:** The OSDK can now be used seamlessly in TypeScript v2 functions, making it easy to reuse code, both in and out of the platform. It also provides more efficient APIs for working with large-scale Ontology data.
* **Configurable resource requests:** TypeScript v2 functions allow you to request up to 8 vCPUs and 5GB of memory, offering greater control over performance and scalability.
## Serverless functions
如果为你的注册启用了 serverless functions，则新仓库默认将使用 serverless functions。对于大多数使用场景，我们建议使用 serverless functions 而不是 deployed functions。使用 serverless functions，你可以按需提供单个 function 的多个版本，使升级更安全。

If serverless functions are enabled for your enrollment, new repositories will use serverless functions by default. We recommend using serverless functions instead of deployed functions for most use cases. With serverless functions, you can have multiple versions of a single function available on demand, making upgrades safer.
在使用 Python 或 TypeScript v2 functions 时，也有 [一些情况下更推荐使用 deployed functions](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) 或必须使用 deployed functions 而非 serverless functions，但这些情况并不常见。如果可用，出于以下几个原因，更推荐使用 serverless functions：

When using Python or TypeScript v2 functions, there are also [some cases where deployed functions are preferred](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) or must be used instead of serverless, but these are not common. If available, serverless functions are preferred for several reasons:
* Serverless functions 支持按需执行单个 function 的不同版本，使升级更安全。对于 deployed functions，你一次只能运行单个 function 版本。

* Serverless functions 仅在执行时产生费用，而 deployed functions 只要 deployment 正在运行就会产生费用。

* Serverless functions 需要较少的前期设置和长期维护，因为基础设施是自动管理的。

* Serverless functions enable different versions of a single function to be executed on demand, making upgrades safer. With deployed functions, you can only run a single function version at a time.
* Serverless functions only incur costs when executed, while deployed functions incur costs as long as the deployment is running.
* Serverless functions require less upfront setup and long-term maintenance, as the infrastructure is managed automatically.