<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/webhooks/
---
# Webhooks
[Webhook](/docs/foundry/data-connection/webhooks-overview/) 是 Data Connection 中的一个概念，用于向外部系统（例如 Salesforce、SAP 或任何已配置的 HTTP 服务器）发送请求，通常用于修改该外部系统中的数据。

A [webhook](/docs/foundry/data-connection/webhooks-overview/) is a concept in Data Connection that enables sending a request to an external system, such as Salesforce, SAP, or any configured HTTP server, typically to modify data in that external system.
通过设置 webhook 并将其配置为在 action 中使用，您可以在最终用户在 Foundry 中应用 action 时将数据发送到外部系统。这使得 Foundry 中的工作流能够直接与源系统连接，并将数据和决策写回这些系统。

By setting up a webhook and then configuring it for use in an action, you can send data to an external system when end users apply an action in Foundry. This enables workflows in Foundry to connect directly with source systems and write back data and decisions into those systems.
本节详细介绍了在 action 中配置 webhook 的各种选项。有关分步教程，请参阅关于[如何在 action 中添加 webhook](/docs/foundry/action-types/set-up-webhook/) 的文档。

This section details the various options available for configuring webhooks in an action. For a step-by-step tutorial, see the documentation on [how to add a webhook in an action](/docs/foundry/action-types/set-up-webhook/).
## Webhooks: Writeback vs. side effect
在 action 中使用 webhook 有两种配置方式：作为 **writeback** 或作为 **side effect**。

There are two ways that webhooks can be configured for use in an action: as a **writeback** or as a **side effect**.

> 📷 **[图片: 添加 webhook]**

> 📷 **[图片: Add webhook]**

为方便起见，下面提供一个表格，比较 writeback 和 side effect webhook 的行为。

For convenience, below is a table comparing the behavior of writeback and side effect webhooks.
| Type | When applied | Failure shown to end user? | Timing |
|--- |--- |--- |--- |
| **Writeback** | Before object changes | Yes | Before user sees success or failure |
| **Side effect** | After object changes | No | May be after user sees success message |
以下各节将更详细地介绍 writeback webhook 和 side effect webhook。

The following sections describe writeback webhooks and side effect webhooks in more detail.
### Writeback webhooks
当配置为 **writeback** 时,webhook 将在任何其他规则评估之前执行;如果 webhook 执行失败,则不会进行任何其他更改。如果您希望确保在外部系统更新后再对 Foundry 进行更改,则应将 webhook 设置为 writeback。

When configured as a **writeback**, the webhook will be executed *before* any other rules are evaluated; if the webhook execution fails, no other changes will be made. If you want to ensure that changes are not made in Foundry before the external system, you should set up your webhook as a writeback.
此行为在 Foundry 和外部系统之间提供了一定程度的事务性。使用 writeback webhook 可以保证如果对外部系统的请求失败,则不会对 Foundry Ontology 应用任何更改。然而,仍然可能出现外部请求成功但 Ontology 更改失败的情况。

This behavior enables some degree of transactionality between Foundry and the external system. Using a writeback webhook guarantees that if the request to the external system fails, no changes will be applied to the Foundry Ontology. However, it is still possible that the external request may succeed but Ontology changes could fail.
由于当 writeback webhook 失败时 Action 将停止应用,因此您只能将单个 webhook 配置为 writeback。如果在应用 Action 时该 webhook 失败,则会向最终用户显示一条错误,描述失败原因。

Because the action stops being applied when a writeback webhook fails, you can only configure a single webhook as a writeback. If this webhook fails when the action is applied, an error will be shown to the end user describing the failure.
当 webhook 配置为 writeback 时,其输出参数可在后续规则中使用。更多详细信息,请参阅下面的 [output parameters](#output-parameters) 部分。

When a webhook is configured as a writeback, its output parameters can be used in subsequent rules. See the [output parameters](#output-parameters) section below for more details.
### Side effect webhooks
当配置为 **side effect** 时,webhook 将在其他规则评估*之后*执行。这意味着对 Foundry objects 的修改将先于 side effects 应用。您可以在单个 Action 中配置多个 side effect webhook,且它们将以无特定顺序执行。在包含 side effect webhook 的 Action 中,最终用户将在 Foundry objects 修改完成后看到成功消息;side effects 的执行可能发生在成功消息显示之后。

When configured as a **side effect**, a webhook will be executed *after* other rules are evaluated. This means that modifications to Foundry objects will occur before side effects are applied. You can configure multiple side effect webhooks in a single action, and they will be executed in no particular order. In an action with side effect webhooks, the end user will see a success message after Foundry objects are modified; executing the side effects may happen after the success message is shown.
如果您需要从单个 Action 中多次调用某个 webhook,可以通过提供作为输入的 payload 列表来使用 side effect webhook 实现。这将根据列表中 payload 的数量触发相应次数的 webhook,且处理顺序不作保证。相关示例可在下面的 [input parameters](#input-parameters) 部分中找到。

If you need to call a webhook multiple times from a single action, this can be achieved with a side effect webhook by providing a list of payloads as an input. This will trigger the webhook as many times as there are payloads in the list provided and will be processed in no guaranteed order. An example of this can be found below in the [input parameters](#input-parameters) section.
当您希望发送尽力而为的通知或回写到多个外部系统时,应使用 side effect webhook。

You should use side effect webhooks when you want to send best-effort notifications or write back to multiple external systems.
## Input parameters
要在 Action 中配置 Webhook,必须填充其所有必需的输入参数。有关 Webhook 输入参数的一般参考信息,请参阅 [Data Connection 文档](/docs/foundry/data-connection/webhooks-reference/#input-parameters)。

In order to configure a Webhook in an Action, you must populate all of its required input parameters. General reference material about Webhook input parameters is available in the [Data Connection documentation](/docs/foundry/data-connection/webhooks-reference/#input-parameters).
配置 Webhook 输入参数有两种方式:映射到 Action parameters,或使用 Function。

There are two ways to configure Webhook input parameters: by mapping to Action parameters, or by using a Function.
当映射到 **Action parameters** 时,每个必需的 Webhook input 必须设置为相同类型的 Action parameter、静态值,或 object parameter 的 property。

When mapping to **Action parameters**, each required Webhook input must be set to either an Action parameter of the same type, a static value, or a property of an object parameter.

> 📷 **[图片: Input parameters]**

> 📷 **[图片: Input parameters]**

当使用 [Function](/docs/foundry/functions/overview/) 时,您必须选择一个返回包含所有必需 Webhook 输入参数的自定义类型且与 Webhook 类型强匹配的 Function,否则您将收到 `OntologyMetadata:ActionWebhookInputsDoNotHaveExpectedType` 错误。当您希望使用逻辑来填充 inputs 时,使用 Function 填充 Webhook 输入参数会非常有用,尤其是当该逻辑基于 Ontology objects 时。例如,您可以检索 linked objects 并从这些 objects 中提取 property 值以预填充 Webhook inputs。

When using a [Function](/docs/foundry/functions/overview/), you must select a Function that returns a custom type that includes all of the required Webhook input parameters and strongly matches the Webhook type, otherwise you will receive an `OntologyMetadata:ActionWebhookInputsDoNotHaveExpectedType` error. Using a Function to populate Webhook input parameters can be useful when you want to use logic to populate inputs, especially if this logic is based on Ontology objects. For example, you can retrieve linked objects and pull property values from those objects to prepopulate Webhook inputs.
举个例子,假设您有一个 Webhook,它接受三个 ID 分别为 `name`、`industry` 和 `country` 的输入参数:

As an example, suppose you have a Webhook which takes three input parameters with IDs `name`, `industry`, and `country`:

> 📷 **[图片: Input parameters example]**

> 📷 **[图片: Input parameters example]**

您可以编写一个 Function,返回具有相同结构的自定义 interface:

You can write a Function that returns a custom interface of the same structure:
```typescript
export interface MyWebhookInput {
name: string;
industry: string;
country: string;
}
```
然后，您可以在配置 Action 中的 Webhook 输入时选择此 Function，将 Action 参数映射到该 Function 所需的参数：

Then, you can select this Function when configuring Webhook inputs in an Action, mapping Action parameters to the parameters required by the Function:

> 📷 **[图片: 将 Action 参数映射到 Function 所需的参数]**

> 📷 **[图片: Mapping Action parameters to the parameters required by a Function]**

下面是一个完整的 Function 代码示例，该 Function 从 Ontology object 加载数据并将其用于填充 Webhook 输入。

Below is a full code example of a Function that loads data from an Ontology object and uses it to populate Webhook inputs.
```typescript
import { Function, UserFacingError } from "@foundry/functions-api";
import { Company } from "@foundry/ontology-api";

export interface MyWebhookInput {
name: string;
industry: string;
country: string;
}

export class MyWebhookFunctions {
@Function()
public returnWebhookInput(company: Company): MyWebhookInput {
if (!company.name || !company.industry || !company.country) {
throw new UserFacingError("Some required fields are not set.");
}
return {
name: company.name,
industry: company.industry,
country: company.country,
}
}
}
```
通过从 Function 返回 payload 列表，副作用 Webhook 可以被调用多次。下面是一个示例 Function，它接收两个 companies 作为输入，并返回一个包含两个 payload 的列表，这些 payload 与 Webhook 期望的输入参数相匹配。如果在 Action 中使用此 Function 来返回副作用 Webhook 的输入，将导致两次单独的 Webhook 执行。

A side effect Webhook may be called multiple times by returning a list of payloads from a Function. Below is an example Function which takes two companies as inputs, and returns a list containing two payloads matching the input parameters expected by a Webhook. If this Function is used from Actions to return the inputs for a side effect Webhook, it will result in two separate Webhook executions.
```typescript
import { Function } from "@foundry/functions-api";
import { Company } from "@foundry/ontology-api";

export interface MyWebhookInput {
arg1: string;
arg2: string;
}

export class MyFunctions {
@Function()
public createWebhookRequest(company1: Company, company2: Company): MyWebhookInput[] {
return [
{
arg1: company1.someProperty,
arg2: company1.someOtherProperty,
},
{
arg1: company2.someProperty,
arg2: company2.someOtherProperty,
}
];
}
}
```
## Output parameters
当 Webhook 配置为 [writeback Webhook](#writeback-webhooks) 时，您可以在后续规则中使用其输出参数。当外部系统返回您希望立即写入 Foundry object 或用于后续 [notification](/docs/foundry/action-types/notifications/) 或 [side effect Webhook](#side-effect-webhooks) 的数据时，这非常有用。

When a Webhook is configured as a [writeback Webhook](#writeback-webhooks), you can use its output parameters in subsequent rules. This is useful when the external system returns data that you want to immediately write into a Foundry object or use in a subsequent [notification](/docs/foundry/action-types/notifications/) or [side effect Webhook](#side-effect-webhooks).
有关 Webhook 输出参数的一般参考材料，请参阅 [Data Connection 文档](/docs/foundry/data-connection/webhooks-reference/#output-parameters)。

General reference material about Webhook output parameters is available in the [Data Connection documentation](/docs/foundry/data-connection/webhooks-reference/#output-parameters).
要在后续逻辑规则中使用输出参数，请在为逻辑规则填充值时选择 **Writeback response**，然后选择您希望使用的特定输出：

To use an output parameter in a subsequent logic rule, select **Writeback response** when populating the value for a logic rule, then select the specific output you wish to use:

> 📷 **[图片: 在 Logic Rule 中使用输出参数]**

> 📷 **[图片: Using an output parameters in a Logic Rule]**

## OAuth 2.0 authentication
当 Webhook 配置在使用 [outbound application](/docs/foundry/administration/configure-outbound-applications/) 进行身份验证的 REST API source 上时，Foundry 代表用户管理 OAuth 2.0 授权流程。开发人员无需处理 token 获取或刷新。Foundry 在每次 Webhook 调用时都会传递正确的 access token。

When a webhook is configured on a REST API source that uses an [outbound application](/docs/foundry/administration/configure-outbound-applications/) for authentication, Foundry manages the OAuth 2.0 authorization flow on behalf of the user. Developers do not need to handle token acquisition or refresh. Foundry passes the correct access token with every webhook call.
有关 Foundry 工作流中 OAuth 2.0 outbound application 支持的完整概述，请参阅 [OAuth 2.0 outbound applications](/docs/foundry/administration/configure-outbound-applications/) 文档。

For a full overview of OAuth 2.0 outbound application support across Foundry workflows, see the [OAuth 2.0 outbound applications](/docs/foundry/administration/configure-outbound-applications/) documentation.