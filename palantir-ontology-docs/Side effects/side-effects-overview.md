<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/side-effects-overview/
---
# Side effects
Action 类型旨在支持组织内各种决策流程。当 Ontology 作为决策流程的记录系统时，使用 [rules](/docs/foundry/action-types/rules/) 来定义 object 修改，使您能够以极大的灵活性表达业务流程。为了支持各种组织流程，action 类型还提供了一些附加功能：

Action types are designed to support the full range of decision-making processes within an organization. When the Ontology serves as the system of record for a decision-making process, using [rules](/docs/foundry/action-types/rules/) to define object modifications allows you to express business processes with great flexibility. In order to support the full range of organizational processes, action types support a few additional features:
* 对于实时流程，您可能需要 *通知（notify）* 用户系统中正在发生的变化，以便他们采取相应的行动。

* 当 Foundry 以外的系统是您组织的 source of truth 时，您可能需要 *集成（integrate）* 其他系统以支持现有业务流程。这种模式有时称为"decision orchestration"。

* For real-time processes, you may need to *notify* users about changes that are happening in the system so they can take action in response.
* In cases when a system besides Foundry is the source of truth for your organization, you may need to *integrate* with the other system to support the existing business process. This pattern is sometimes referred to as "decision orchestration."
Action 类型中的 **Side effects（副作用）** 使您能够将数据从 Foundry 发送出去，以与现有组织流程集成。Side effects 主要有两种类型：

**Side effects** in action types enable you to send data out of Foundry to integrate with existing organizational processes. There are two main types of side effects:
* [Notifications](/docs/foundry/action-types/notifications/) 允许您灵活地配置在 action 被应用时如何通知用户。这包括向平台上的用户发送电子邮件的能力。

* [Webhooks](/docs/foundry/action-types/webhooks/) 允许您以高度灵活的方式连接到 Foundry 之外的系统，包括向 REST API 或 ERP 系统发送请求。这使您能够将数据写入组织中的其他源系统，或通过与消息系统集成，更灵活地向用户发送通知。

* [Notifications](/docs/foundry/action-types/notifications/) allow you to flexibly configure how a user should be notified when an action is applied. This includes the ability to send an email to users on the platform.
* [Webhooks](/docs/foundry/action-types/webhooks/) allow you to connect to systems outside Foundry in a highly flexible way, including sending requests to a REST API or an ERP system. This enables you to write to other sources systems in your organization, or more flexibly send notifications to users by integrating with messaging systems.
您可以使用上面的链接了解有关 notifications 和 webhooks 的更多信息，或查看以下指南以开始使用：

You can learn more about notifications and webhooks using the links above, or review these guides to get started:
* [设置 notifications](/docs/foundry/action-types/set-up-notification/)

* [设置 webhook](/docs/foundry/action-types/set-up-webhook/)

* [Set up notifications](/docs/foundry/action-types/set-up-notification/)
* [Set up a webhook](/docs/foundry/action-types/set-up-webhook/)