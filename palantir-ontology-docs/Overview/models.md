<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/models/
---
# Models in the Ontology
各组织正在寻求利用人工智能 (AI) 和机器学习 (ML) 来加速和改进决策。但 AI/ML 落地的现实情况非常复杂，典型的投资回报率很少能达到预期。

Organizations are looking to leverage artificial intelligence (AI) and machine learning (ML) to accelerate and improve decision-making. But the reality of operationalizing AI/ML is complex, and the typical return on investment rarely lives up to expectations.
Foundry 提供了弥合这一差距所需的关键能力：值得信赖的数据基础、用于根据组织目标评估和比较模型的工具，以及将模型部署到面向用户的运营工作流中的功能。本页面重点介绍最后一步：将经过评估的模型部署到生产环境。

Foundry provides the key capabilities necessary to bridge this gap: a trustworthy data foundation, tools for evaluating and comparing models against organizational objectives, and functionality for deploying models into user-facing operational workflows. This page focuses on the last step: deploying an evaluated model into production.
## End-to-end workflow
从宏观层面来看，以下是在 Foundry 中通过 Ontology 实现 AI/ML 在线推理的端到端操作步骤：

At a high level, these are the end-to-end steps required to operationalize AI/ML in Foundry for live inference with the Ontology:
1. 在 Foundry 中[创建模型](/docs/foundry/integrate-models/integrate-overview/)。

2. 配置一个[直接模型部署](/docs/foundry/manage-models/create-a-model-deployment/)。

3. [为您的模型发布一个简单的包装 function](/docs/foundry/model-integration/model-functions-guide/)，并[可选择从另一个 function 调用它](/docs/foundry/functions/functions-on-models/)，以编排围绕模型的复杂逻辑。

4. 在 [Workshop](/docs/foundry/workshop/functions-use/)、[Vertex](/docs/foundry/vertex/overview/) 和其他面向终端用户的应用程序中使用该 function 进行在线推理。

1. [Create a model](/docs/foundry/integrate-models/integrate-overview/) in Foundry.
2. Configure a [direct model deployment](/docs/foundry/manage-models/create-a-model-deployment/).
3. [Publish a simple wrapper function for your model](/docs/foundry/model-integration/model-functions-guide/) and [optionally call it from another function](/docs/foundry/functions/functions-on-models/) to orchestrate complex logic around your model.
4. Use that function for live inference in [Workshop](/docs/foundry/workshop/functions-use/), [Vertex](/docs/foundry/vertex/overview/) and other end-user facing applications.
Ontology Object 也可以由利用模型进行批量推理的数据集支持——[了解如何在 Code Repositories 中使用模型](/docs/foundry/model-integration/tutorial-train-code-repositories/)。

Ontology Objects can also be backed with datasets that leverage a model for batch inference - [learn how to use a model in Code Repositories](/docs/foundry/model-integration/tutorial-train-code-repositories/).
## Benefits
正如将数据集映射到 Ontology 概念可为工作流开发和决策制定带来[好处](/docs/foundry/ontology/why-ontology/)一样，将模型映射到 Ontology 同样具有诸多优势：

Just like mapping datasets to Ontology concepts provides [benefits](/docs/foundry/ontology/why-ontology/) for workflow development and decision-making, mapping models to the Ontology provides a number of benefits:
* **可解释性**。由于所有建模结果都是根据现实世界的概念（object type 的 property）来定义的，因此最终用户无需了解机器学习即可使用建模结果。相反，用户只需与简单的概念进行交互，例如 *forecast*、*estimate* 或 *classification*。

* **规模经济**。建模工作不再是针对特定用例创建的定制化项目，而是可以随着时间的推移相互借鉴。例如，为某个用例生成的 forecast 可以立即被用于后续用例，从而减少重复工作，并随着时间的推移更快地为最终用户创造价值。

* **大规模连通性**。通过纳入 ML 模型，Ontology 成为组织的单一可信数据源，不仅涵盖数据层面，还涵盖 *逻辑* 层面。模型编码了组织对未来变化的预期。通过这种方式，Ontology 成为了整个企业的"数字孪生"，从而解锁了以各种分散的建模工作永远无法实现的方式来模拟组织内变更的能力。

* **Interpretability**. Because all modeling results are defined in terms of real-world concepts (properties of an object type), end users do not need to understand machine learning in order to use modeling results. Instead, users simply interact with simple concepts such as a *forecast*, *estimate*, or *classification*.
* **Economies of scale**. Instead of each modeling project being a bespoke effort created in service of a specific use case, modeling efforts can build on each other over time. For example, a forecast produced for one use case can immediately be used for subsequent use cases as well, reducing duplicated effort and providing end-user value more quickly over time.
* **Connectivity at scale**. By incorporating ML models, the Ontology becomes a single source of truth for the organization, not just in terms of data, but also in terms of *logic*. Models encode the organization's expectations for how things may change in the future. In this way, the Ontology becomes a "digital twin" for the entire enterprise, which unlocks the ability to simulate changes across the organization in ways that would never be possible with a wide array of disparate modeling efforts.