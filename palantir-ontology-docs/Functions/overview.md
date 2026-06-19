<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/overview/
---
# Functions
**Function** 使代码作者能够编写可在操作上下文中快速执行的逻辑，例如用于支持决策过程的仪表板和应用程序。此逻辑在服务器端的隔离环境中执行。

**Functions** enable code authors to write logic that can be executed quickly in operational contexts, such as dashboards and applications designed to empower decision-making processes. This logic is executed on the server side in an isolated environment.
值得注意的是，Function 包括对基于 Ontology 编写的逻辑的一流支持。这包括对读取各种 Object Type 的 Property、遍历 Link 以及灵活进行 Ontology 编辑的支持。

Notably, functions include first-class support for authoring logic based on the Ontology. This includes support for reading the properties of various object types, traversing links, and flexibly making Ontology edits.
Function 的常见用例包括：

Common use cases for functions include:
* 返回 object set 或 variable 值以供 [Workshop](/docs/foundry/workshop/functions-use/) 使用。

* 在 derived table column 中使用 [Workshop 的 function-backed column](/docs/foundry/workshop/derived-properties/) 显示转换后的值。

* 聚合 Object Type 值以显示为 [Workshop 图表](/docs/foundry/workshop/widgets-chart/#function-aggregations-function-backed-layers)。

* 通过 [function backed action](/docs/foundry/action-types/function-actions-overview/) 表达更新多个对象的 Ontology 复杂编辑。

* 在后端运行逻辑，将返回的信息显示在 [Slate](/docs/foundry/slate/overview/) 前端。

* 计算自定义 metric 或聚合以在 [Quiver](/docs/foundry/quiver/overview/) 中显示。

* 通过 [external function](/docs/foundry/functions/webhooks/) 查询外部系统以丰富 Ontology 中的 object。

* 在 [Pipeline Builder](/docs/foundry/functions/python-functions-builder/) 中将 Python function 用作 sidecar 容器。

* Returning object sets or variable values for use in [Workshop](/docs/foundry/workshop/functions-use/).
* Displaying transformed values in a derived table column using [Workshop's function-backed columns](/docs/foundry/workshop/derived-properties/).
* Aggregating object type values to display as [Workshop charts](/docs/foundry/workshop/widgets-chart/#function-aggregations-function-backed-layers).
* Expressing a complex edit to the Ontology that updates many objects through a [function backed action](/docs/foundry/action-types/function-actions-overview/).
* Running logic in the backend to return information to be displayed in the frontend in [Slate](/docs/foundry/slate/overview/).
* Computing custom metrics or aggregations for display in [Quiver](/docs/foundry/quiver/overview/).
* Querying external systems to enrich objects in the Ontology through [external functions](/docs/foundry/functions/webhooks/).
* Using Python functions as a sidecar container in [Pipeline Builder](/docs/foundry/functions/python-functions-builder/).
Function 支持的语言包括 [TypeScript ↗](https://www.typescriptlang.org/docs/handbook/basic-types.html) 和 [Python ↗](https://www.python.org/)。

The languages supported by functions are [TypeScript ↗](https://www.typescriptlang.org/docs/handbook/basic-types.html) and [Python ↗](https://www.python.org/).
有关按语言划分的功能支持以及选择语言或语言版本的更多信息，请参阅 [language feature support specifications](/docs/foundry/functions/language-feature-support/)。

For more information on feature support by language and choosing a language or language version, refer to the [language feature support specifications](/docs/foundry/functions/language-feature-support/).
要开始在 Foundry 中使用 function，我们推荐以下教程：

To get started using functions in Foundry, we recommend the following tutorials:
* [TypeScript v1 function 入门](/docs/foundry/functions/typescript-v1-getting-started/)

* [TypeScript v2 function 入门](/docs/foundry/functions/typescript-v2-getting-started/)

* [Python function 入门](/docs/foundry/functions/python-getting-started/)

* [Getting started with TypeScript v1 functions](/docs/foundry/functions/typescript-v1-getting-started/)
* [Getting started with TypeScript v2 functions](/docs/foundry/functions/typescript-v2-getting-started/)
* [Getting started with Python functions](/docs/foundry/functions/python-getting-started/)
> **✅ 成功: Palantir Learning portal**

> 在我们的 learn.palantir.com 上尝试 ["Speedrun: Your first Ontology function" 课程 ↗](https://learn.palantir.com/speedrun-your-first-ontology-function)。
> **✅ 成功: Palantir Learning portal**

> Try our ["Speedrun: Your first Ontology function" course ↗](https://learn.palantir.com/speedrun-your-first-ontology-function) on learn.palantir.com.