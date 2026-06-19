<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/use-functions/
---
# Use functions in the platform
本节记录了您可以在 Foundry 平台各处使用 functions 的各种方式。此列表基本上保持最新，但可能还有其他使用 functions 的方式未在此处列出。

This section documents various ways that you can use functions throughout the Foundry platform. This list is kept mostly up to date, but there may be additional ways to use functions that are not captured here.
## Workshop
[Workshop](/docs/foundry/workshop/overview/) 通过多种方式支持与 functions 的集成，从而可以在 Workshop 中构建的各个模块中使用自定义逻辑。

[Workshop](/docs/foundry/workshop/overview/) supports integration with functions in a variety of ways, enabling the use of custom logic throughout modules built in Workshop.
### Variables
大多数 Workshop [Variables](/docs/foundry/workshop/concepts-variables/) 可以是 Function-backed，允许 application builder 使用 functions 来计算值，然后在整个 Workshop 中使用这些值。默认情况下，当 Variable 所依赖的另一个 Variable 更新时，该 Variable 的值将重新计算。这使得能够灵活地根据用户反馈重新计算值——例如，当用户编辑 input component 时，依赖的 Function-backed Object Set Variable 将自动重新计算。

Most Workshop [Variables](/docs/foundry/workshop/concepts-variables/) can be Function-backed, allowing an application builder to use functions to compute values that can then be used throughout Workshop. By default, the value for a variable is recomputed when another variable it depends on is updated. This enables flexible recomputation of values in response to user feedback—for example, when a user edits an input component, a dependent Function-backed Object Set variable will be recomputed automatically.
要了解更多信息，请查看 [关于如何使用 functions 支持 Workshop variables 的教程](/docs/foundry/workshop/functions-use/#function-backed-variables-in-workshop)。

To learn more, take a look at the [tutorial on how to use functions to back Workshop variables](/docs/foundry/workshop/functions-use/#function-backed-variables-in-workshop).
下面是 Workshop Variable 类型与它们在 TypeScript 中的对应类型之间的映射关系。每种给定类型的 Workshop Variable 都可以由一个 Function 支持，该 Function 返回所列有效类型之一。[了解更多关于可用的 Function types 的文档。](/docs/foundry/functions/types-reference/)

Below is the mapping between Workshop variable types and their equivalents in TypeScript. A Workshop variable of each given type can be backed by a Function that returns one of the valid types listed. [Learn more about the available Function types are documented.](/docs/foundry/functions/types-reference/)
* Boolean：`boolean`
* String：`string`
* Numeric：`Integer`、`Long`、`Float`、`Double`
* Date：`LocalDate`
* Timestamp：`Timestamp`
* Array：`BaseType[]` 或 `Set<BaseType>`

* Object Set：`ObjectSet<ObjectType>`（推荐）、`ObjectType[]` 或 `Set<ObjectType>`

* Boolean: `boolean`
* String: `string`
* Numeric: `Integer`, `Long`, `Float`, `Double`
* Date: `LocalDate`
* Timestamp: `Timestamp`
* Array: `BaseType[]` or `Set<BaseType>`
* Object Set: `ObjectSet<ObjectType>` (recommended), `ObjectType[]`, or `Set<ObjectType>`
### Object Table: Derived properties
Workshop 的 **Object Table** widget 可以配置为计算 Function-backed 列，该列可以根据用户输入进行更新，并且会在最终用户滚动浏览表格时动态重新计算。您可以查看 [使用此功能的完整教程](/docs/foundry/workshop/widgets-object-table/#function-backed-columns)。

Workshop’s **Object Table** widget can be configured to compute a Function-backed column, which can update based on user input and will be recomputed on the fly as end users scroll through the table. You can see a [full tutorial for using this functionality](/docs/foundry/workshop/widgets-object-table/#function-backed-columns).
### Chart: Derived aggregations
Workshop 的 **Chart: XY** widget 支持使用 Function-backed aggregation 按需派生聚合值。如果您希望聚合数据基于用户选择，这将非常有用。要在 Chart widget 中使用 functions，只需点击配置 chart layer，然后选择 *Function aggregation*。

Workshop’s **Chart: XY** widget supports using a Function-backed aggregation to derive aggregated values on demand. This can be useful if you want to have aggregation data be based on user selection. To use functions in a Chart widget, simply click to configure a chart layer and select *Function aggregation*.
![use-functions-chart](/docs/resources/foundry/functions/use-functions-chart.png)
[Aggregation API 的参考](/docs/foundry/functions/types-reference/#aggregation-types) 可供查阅。对于更高级的用例，您可能需要阅读有关 [如何计算自定义 aggregations](/docs/foundry/functions/create-custom-aggregation/) 的文档。

A [reference for the Aggregation API](/docs/foundry/functions/types-reference/#aggregation-types) is available. For more advanced use cases, you may want to read the documentation about [how to compute custom aggregations](/docs/foundry/functions/create-custom-aggregation/).
## Actions
[Action types](/docs/foundry/action-types/overview/) 使应用程序能够以灵活且安全的方式更改 Foundry ontology 中的对象，并调度外部 notifications 和 side effects。在 Actions 中，functions 提供了完全的灵活性，使代码作者能够定义对象的更新方式或 side effects 的配置方式。

[Action types](/docs/foundry/action-types/overview/) enable applications to make changes to the objects in the Foundry ontology and to dispatch external notifications and side effects in a way that is flexible and secure. Within Actions, functions provide complete flexibility, enabling code authors to define how objects should be updated or how side effects should be configured.
### Function-backed Actions
Function-backed Actions 使用 [Ontology edits](/docs/foundry/functions/api-ontology-edits/) API 来定义对象更新的逻辑。这允许您在代码中表达复杂的编辑——例如，更新链接到某个起始对象的每个对象。[查看关于如何端到端使用 Function-backed Actions 的教程。](/docs/foundry/action-types/function-actions-getting-started/)

Function-backed Actions use the [Ontology edits](/docs/foundry/functions/api-ontology-edits/) API to define the logic for how objects should be updated. This allows you to express complex edits in code—for example, updating every objected linked to some starting object. [See a tutorial for how to use Function-backed Actions end-to-end.](/docs/foundry/action-types/function-actions-getting-started/)
### Side effects: Notifications
Action 可以配置为向指定用户发送 Notification。您可以使用 functions 来计算哪些用户应接收 Notification，以及 Notification 的内容本身。这提供了灵活性，例如加载存储在对象中的收件人用户 ID，或根据对象数据呈现电子邮件内容。要了解更多信息，请参阅 [关于 Notifications 的完整文档](/docs/foundry/action-types/notifications/) 以及 [关于如何使用 functions 配置 Notifications 的指南](/docs/foundry/functions/configure-notifications/)。

An Action can be configured to send a Notification to a specified user. You can use functions to compute which users should receive a Notification, as well as the contents of the Notification itself. This provides flexibility such as loading recipient user IDs that are stored within objects, or rendering email content based on object data. To learn more, consult the [full documentation about Notifications](/docs/foundry/action-types/notifications/) and a [guide for how to use functions to configure Notifications](/docs/foundry/functions/configure-notifications/).
### Side effects: Webhooks
Action 还可以配置为在应用时触发 Webhook。Webhooks 实现了 Foundry 与其他系统的集成，使用户应用的 Actions 能够回写到 Foundry 之外的 API。您可以使用 functions 来计算应发送给将执行的 Webhook 的 parameters，从而实现基于对象数据填充 Webhook parameters 之类的工作流。[查看关于 Webhooks 的完整文档。](/docs/foundry/action-types/webhooks/)

An Action can also be configured to trigger a Webhook when it is applied. Webhooks enable integration of Foundry with other systems, enabling user-applied Actions to write back to APIs outside of Foundry. You can use functions to compute the parameters that should be sent to the Webhook that will be executed, enabling workflows like populating Webhook parameters based on object data. [View full documentation about Webhooks.](/docs/foundry/action-types/webhooks/)
## Slate
[Slate](/docs/foundry/slate/overview/) 原生支持在 **Platform** 标签页中查找和使用 Function。编辑 Slate 文档时，打开 Platform 标签页并在左下角添加一个 **Foundry Function**。现在，你可以搜索 Function、配置参数，并在 Slate 文档中使用其结果。

[Slate](/docs/foundry/slate/overview/) includes native support for finding and using functions within the **Platform** tab. When editing a Slate document, open the Platform tab and add a **Foundry Function** in the bottom-left. Now, you can search for a Function, configure parameters, and use the result in your Slate document.
![use-functions-slate](/docs/resources/foundry/functions/use-functions-slate.png)
请注意，由于历史原因，Slate 产品有其自身的"functions"概念，这些是位于每个 Slate 文档中的 JavaScript 逻辑片段。这就是为什么 functions 产品被称为"Foundry functions"并位于 **Platform** 标签页下的原因。Slate 的 functions 功能允许在文档中进行快速、简单的数据操作，但不支持 objects。

Note that for historical reasons, the Slate product has its own notion of "functions", which are snippets of JavaScript logic located within each Slate document. This is why the functions product is called "Foundry functions" and is located under the **Platform** tab. Slate's functions capability allows for quick, easy data manipulation within a document, but do not have native support for objects.
你可以将 Slate functions 和 Foundry functions 结合使用——例如，你可以从 Foundry Function 返回数据，然后在 Slate Function 中对其进行操作，或者使用 Slate Function 计算应传递给 Foundry Function 的参数。

You can use Slate's functions and Foundry functions in combination with each other—for example, you could return data from a Foundry Function and manipulate it in a Slate Function, or use a Slate Function to compute parameters that should be passed into a Foundry Function.
## Quiver
Quiver 中的 [Object set 图表](/docs/foundry/quiver/objects-chart-drilldown/#code-function-categorical-plot) 使用与 Workshop 的 Chart: XY widget 相同的底层组件。因此，你也可以在 Quiver 分析中使用 Function-backed Aggregations。

[Object set plots](/docs/foundry/quiver/objects-chart-drilldown/#code-function-categorical-plot) in Quiver use the same underlying component as Workshop's Chart: XY widget. As such, you can use Function-backed Aggregations in Quiver analyses as well.
## Automate
[Automate](/docs/foundry/automate/overview/) 允许你创建 function-backed automations，当满足指定条件时自动执行 functions。

[Automate](/docs/foundry/automate/overview/) allows you to create function-backed automations, which automatically execute functions when a specified condition is met.
配置 Function effect 时，你可以选择一个 function 并指定其版本。对于稳定版本（1.0.0 及以上），你可以启用自动升级到兼容版本。Automate 中的 Functions 异步执行，最长可运行 4 小时。

When configuring a Function effect, you can select a function and specify its version. For stable versions (1.0.0 and greater), you can enable automatic upgrades to compatible versions. Functions in Automate execute asynchronously and can run for up to 4 hours.
请注意，具有 ontology edit 返回类型的 functions 在作为 Automate 中的 effects 使用时，所做的编辑将不会被应用。要了解更多信息，请参阅 [Function effects 文档](/docs/foundry/automate/effect-function/)。

Note that functions with ontology edit return types will not have the edits applied when used as effects in Automate. To learn more, see the [Function effects documentation](/docs/foundry/automate/effect-function/).