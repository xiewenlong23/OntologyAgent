<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/overview/
---
# Object Monitors \[Sunset]
> **⚠️ 警告: Sunset**

> Object Monitors 处于开发生命周期的 [sunset](/docs/foundry/platform-overview/development-life-cycle/) 阶段，将在未来的某个日期被弃用。仍提供全面支持。我们建议您将工作流迁移到 [Automate](/docs/foundry/automate/overview/)。Automate 是一款完全向后兼容的产品，为平台中的所有业务自动化提供单一入口。
> **⚠️ 警告: Sunset**

> Object Monitors are in the [sunset](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be deprecated at a future date. Full support remains available. We recommend migrating your workflows to [Automate](/docs/foundry/automate/overview/). Automate is a fully backwards-compatible product that offers a single entry point for all business automation in the platform.
**Object Monitors** 应用允许最终用户和应用构建者查看 Foundry Ontology 中的数据何时发生变化。当发生变化时，object monitors 可以在满足指定条件时自动发送通知或提交 Actions。Object monitors 在您的数据之上运行，旨在帮助用户跟踪各个搜索和对象。Object monitors 还充当应用构建者在 Foundry 中构建的应用中包含监控和告警功能的工具。

The **Object Monitors** application allows end users and application builders to see when data in the Foundry Ontology changes. When a change occurs, object monitors can automatically send notifications or submit Actions when specified conditions are met. Object monitors run on top of your data and are designed to help users track individual searches and objects. Object monitors also serve as a tool for application builders to include monitoring and alerting functionality as part of applications built in Foundry.
Object monitoring 是 Foundry 中对象层的一项功能，可用于各种工作流，包括：

Object monitoring is a feature of the objects layer in Foundry and can be used for a variety of workflows, including:
* **Watched searches（关注的搜索）：** 用户可以配置 object monitors，以便在 saved object explorations 出现新结果或搜索的所有结果满足聚合条件时发出通知。

* **Automated notifications（自动通知）：** 工作流构建者和自助数据使用者可以配置 object monitors，以便在数据发生变化时发送通知。通知可以通过以下方式发送：

* 平台内弹窗，显示在 Foundry 通知中心
* 电子邮件

* 短信（使用 [webhooks](/docs/foundry/data-connection/webhooks-overview/) 连接到第三方服务，例如 [Twilio ↗](https://www.twilio.com/)）

* 即时消息（使用 webhooks 连接到第三方服务，例如 [Slack ↗](https://slack.com/) 或 [Microsoft Teams ↗](https://www.microsoft.com/microsoft-teams/group-chat-software)）
* 自定义或专有消息系统

* **Workflow automation（工作流自动化）：** Object monitors 可用于对满足特定条件的对象数据自动执行 Actions。可以使用 object monitors 自动执行的一些任务包括：

* 检查数据异常并将那些对象自动传递给包含修复问题逻辑的 Action。

* 关注建议或潜在的 Actions，并在满足预配置的 event 和时间条件时自动应用它们。此类 Actions 可以包括通过 webhooks 向外部系统发起 API 调用，以直接在外部系统中应用更改。

* **Watched searches:** Users may configure object monitors to notify when saved object explorations have new results or when an aggregate criteria is met across all results from a search.
* **Automated notifications:** Workflow builders and self-service data consumers may configure object monitors to send notifications in response to data changes. Notifications may be sent via:
* In-platform pop-up in the Foundry notifications center
* Email
* SMS (using [webhooks](/docs/foundry/data-connection/webhooks-overview/) to a third-party service such as [Twilio ↗](https://www.twilio.com/))
* Instant message (using webhooks to a third-party service such as [Slack ↗](https://slack.com/) or [Microsoft Teams ↗](https://www.microsoft.com/microsoft-teams/group-chat-software))
* Bespoke or proprietary messaging systems
* **Workflow automation:** Object monitors may be used to automatically perform Actions on object data that meet a specific criteria. Some tasks that can be automated with object monitors include:
* Checking for data anomalies and automatically passing those objects into an Action with logic to remediate the issue.
* Watching for suggestions or potential Actions and automatically applying them when pre-configured event and time conditions are met. Such Actions could include making an API call to an external system via webhooks to apply a change directly in the external system.
## Access Object Monitors
要访问 Object Monitors 应用程序，请点击浏览器左侧 Foundry 导航侧边栏中的名称或图标。**Overview** 页面将显示您最近的 monitor 活动列表，以及 monitor 总数、已订阅或已静音的 monitor，以及存在错误或即将过期的 monitor 的数量。

To access the Object Monitors application, click on the name or icon in your Foundry navigation sidebar to the left of your browser. The **Overview** page will show a list of your recent monitor activity along with counts of total monitors, subscribed or muted monitors, and monitors that have errors or will be expiring soon.
**Monitors** 页面显示您可用的 monitor 完整列表。您可以按活动状态、通知和 Action 设置、创建者、过期日期、monitor 类型或条件状态筛选该列表。点击某个 monitor 即可打开 monitor 概览面板，查看历史活动、订阅者及其他详细信息。

The **Monitors** page shows a full list of the monitors available to you. Filter this list by activity status, notification and Action settings, creator, expiration date, monitor type, or condition status. Click on a monitor to open the monitor overview panel and view historical activity, subscribers, and other details.
通过[创建新的 object monitor](/docs/foundry/object-monitors/create_new_object_monitor/) 了解有关 object monitoring 的更多信息。

Learn more about object monitoring by [creating a new object monitor](/docs/foundry/object-monitors/create_new_object_monitor/).
> **ℹ️ 注意**

> Object monitoring 旨在监控您的数据内容。如果您正在寻找针对 data connection 和 pipeline build 的健康监控，请参阅 [Health checks](/docs/foundry/health-checks/overview/) 文档。
> **ℹ️ 注意**

> Object monitoring is designed to monitor the content of your data. If you are looking for health monitoring for data connections and pipeline builds, review the [Health checks](/docs/foundry/health-checks/overview/) documentation.