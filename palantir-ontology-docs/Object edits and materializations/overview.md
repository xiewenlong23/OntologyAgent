<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-edits/overview/
---
# Object edits and materializations
Foundry Ontology 通过将来自各种数据源的数据与来自用户对 object 驱动编辑的数据相结合，为操作型 workflow 提供支持，帮助生成洞察，并维护与您息息相关内容的最新表示。在 Foundry Ontology 中，用户可以通过应用 [Actions](/docs/foundry/action-types/overview/) 来编辑 property 值、添加和删除 link，以及创建和删除 object。

The Foundry Ontology powers operational workflows, helps generate insights, and maintains an up-to-date representation of what matters to you by combining data from a variety of datasources with data coming from user-driven edits to objects. In the Foundry Ontology, users can edit property values, add and remove links, and create and delete objects by applying [Actions](/docs/foundry/action-types/overview/).
Foundry 中的 Action 是基于用户定义逻辑更改一个或多个 object 的 property 的单个事务。Action 使您能够在思考整体目标的同时使用和管理数据，而不是追逐特定的 property 编辑。Action 可以从 Foundry 应用程序（如 [Workshop](/docs/foundry/workshop/actions-use/) 和 [Object Views](/docs/foundry/object-views/overview/)）触发，也可以通过 [Foundry APIs](/docs/foundry/action-types/use-actions/) 从外部应用程序触发。有关如何配置和应用 Action 的更多信息，请参阅 [Actions documentation](/docs/foundry/action-types/overview/)。

An Action in Foundry is a single transaction that changes the properties of one or more objects, based on user-defined logic. Actions enable you to use and manage data while thinking about your overall objectives, rather than chasing specific property edits. Actions can be triggered from Foundry applications (like [Workshop](/docs/foundry/workshop/actions-use/) and [Object Views](/docs/foundry/object-views/overview/)) or from external applications with [Foundry APIs](/docs/foundry/action-types/use-actions/). For more information about how to configure and apply actions, see the [Actions documentation](/docs/foundry/action-types/overview/).
本节中的其他页面讨论了为 object type 和 link type 启用 Action 所需的配置，以及支持 Ontology 中用户驱动编辑的底层机制。

The other pages in this section discuss the necessary configuration for object types and link types to enable Actions, as well as the underlying mechanisms that enable user-driven edits in the Ontology.
> **⚠️ 警告**

> [具有 Foundry stream 数据源的 object type](/docs/foundry/object-permissioning/managing-object-security/#object-input-data-sources) 尚不支持 Action。
> **⚠️ 警告**

> Actions are not yet supported on [object types with Foundry stream datasources](/docs/foundry/object-permissioning/managing-object-security/#object-input-data-sources)