<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/overview/
---
![Ontology overview header image.](/docs/resources/foundry/ontology/ontology-overview-header.png)
# Ontology building
Palantir **Ontology** 是组织的运营层。Ontology 位于集成到 Palantir 平台的数字资产（[数据集](/docs/foundry/data-integration/datasets/)、[虚拟表](/docs/foundry/data-integration/virtual-tables/) 和[模型](/docs/foundry/integrate-models/integrate-overview/)）之上，并将它们连接到现实世界的对应实体，范围从厂房、设备和产品等物理资产，到客户订单或金融交易等概念。在许多场景中，Ontology 充当组织的数字孪生，包含支持各类用例所需的语义元素（objects、properties、links）和动态元素（actions、functions、dynamic security）。

The Palantir **Ontology** is an operational layer for the organization. The Ontology sits on top of the digital assets integrated into the Palantir platform ([datasets](/docs/foundry/data-integration/datasets/), [virtual tables](/docs/foundry/data-integration/virtual-tables/), and [models](/docs/foundry/integrate-models/integrate-overview/)) and connects them to their real-world counterparts, ranging from physical assets like plants, equipment, and products to concepts like customer orders or financial transactions. In many settings, the Ontology serves as a digital twin of the organization, containing both the semantic elements (objects, properties, links) and kinetic elements (actions, functions, dynamic security) needed to enable use cases of all types.
## Object and link types
通过将现有数据源映射到 Ontology 中的 **objects、properties 和 links**，即可定义您组织的语义。Ontology 远不止数据目录或 Schema 设计解决方案，它允许您为最终用户工作流定义坚实的基础，包括所有字段的丰富元数据，并配备针对所有变更的精细安全和治理机制。

Defining the semantics of your organization happens by mapping existing datasources into **objects, properties, and links** in the Ontology. Far beyond data cataloging or schema design solutions, the Ontology allows you to define a robust foundation for end-user workflows, including rich metadata for all fields and complete with granular security and governance for all changes.
了解如何创建 Ontology 的语义元素：[object types](/docs/foundry/object-link-types/object-types-overview/) 和 [link types](/docs/foundry/object-link-types/link-types-overview/)。

Learn about creating the semantic elements of the Ontology: [object types](/docs/foundry/object-link-types/object-types-overview/) and [link types](/docs/foundry/object-link-types/link-types-overview/).
## Action types and functions
组织的动态要素——在遵守组织控制和治理的同时实现变更——在 Ontology 中使用 **action types** 和 **functions** 来定义。Action types 使您能够从组织中的操作员那里捕获数据，或编排连接到现有系统的决策过程；而 functions 则提供了一种以任意复杂度编写和演进业务逻辑的方式。

The kinetics of the organization—enabling change while complying with organizational controls and governance—are defined in the Ontology using **action types** and **functions**. Action types enable you to capture data from operators in your organization or orchestrate decision-making processes that connect to your existing systems, while functions provide a way to author and evolve business logic with arbitrary complexity.
了解如何创建 Ontology 的动态元素：[action types](/docs/foundry/action-types/overview/) 和 [functions](/docs/foundry/functions/overview/)。

Learn about creating the kinetic elements of the Ontology: [action types](/docs/foundry/action-types/overview/) and [functions](/docs/foundry/functions/overview/).
## Interfaces
**Interface** 是一种 Ontology 类型，用于描述 object type 的形态及其能力。Interfaces 提供了 object type 的多态性，允许对共享公共形态的 object type 进行一致的建模和交互。

An **interface** is an Ontology type that describes the shape of an object type and its capabilities. Interfaces provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape.
了解更多关于 [interfaces](/docs/foundry/interfaces/interface-overview/) 的信息。

Learn more about [interfaces](/docs/foundry/interfaces/interface-overview/).
## Powering decision-making
投资建设 Ontology 的目标是促进组织在规模化条件下做出更好的决策。为实现这一目标，Ontology 与 Palantir 面向用户的分析和运营工具深度集成：用户可以创建可复用的 Object Views、在 Object Explorer 中搜索感兴趣的对象、在 Quiver 中执行复杂分析、在 Workshop 中构建高质量的应用程序，等等。

The goal of investing in the Ontology is to facilitate better decision-making in an organization at scale. To achieve this, the Ontology is deeply integrated into Palantir's user-facing analytical and operational tools: users can create reusable Object Views, search for objects of interest in Object Explorer, perform complex analyses in Quiver, build high-quality applications in Workshop, and more.
[了解更多有关如何在面向用户的应用程序中利用 Ontology 的信息。](/docs/foundry/ontology/applications/)

[Learn more about how to leverage the Ontology in user-facing applications.](/docs/foundry/ontology/applications/)
> **✅ 成功: Palantir Learning portal**

> 既然你已经掌握了理论，就通过我们的课程开始构建你的第一个 Ontology 吧：[learn.palantir.com ↗](http://learn.palantir.com/deep-dive-creating-your-first-ontology)。
> **✅ 成功: Palantir Learning portal**

> Now that you know the theory, get started on building your first Ontology with our course on [learn.palantir.com ↗](http://learn.palantir.com/deep-dive-creating-your-first-ontology).