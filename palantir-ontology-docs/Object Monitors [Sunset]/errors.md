<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/errors/
---
# Error reference
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一款完全向后兼容的产品，为平台中的所有业务自动化提供单一入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
本页描述了在使用 Object Monitors 应用或 Object Explorer 中的 **Monitors** 视图时可能遇到的一些常见错误类别。

This page describes some of the common error categories that may be encountered when using the Object Monitors application or the **Monitors** view in Object Explorer.
## Evaluation errors
Monitor 可能会由于底层数据的问题而无法评估。Monitors 会自动重试，但某些错误可能需要人工干预。例如，如果被监控的 object type 被删除，则使用包含该类型对象的输入的 monitors 将无法评估。

A monitor may fail to evaluate due to problems with the underlying data. Monitors are automatically retried, but some errors may require manual intervention. For example, if the object type being monitored is deleted, monitors using inputs containing objects of that type will fail to evaluate.
### Monitor out of sync
Object monitors 使用对 [saved exploration](/docs/foundry/object-explorer/save-explorations/) 的引用来定义输入。该引用不是动态的，而是根据 monitor 保存时 exploration 的状态进行存储。如果 exploration 发生变化，monitor 将继续使用 exploration 的旧状态进行评估，除非更新该 monitor。在这种情况下，monitor 上会显示一个警告横幅：

Object monitors use a reference to a [saved exploration](/docs/foundry/object-explorer/save-explorations/) to define the input. This reference is not dynamic, but instead is stored according to the exploration as it exists when the monitor is saved. If the exploration changes, the monitor will continue to evaluate using the exploration's old state unless the monitor is updated. In this case, a warning banner is displayed on the monitor:
![Warning banner for out of sync monitor](/docs/resources/foundry/object-monitors/monitor_out_of_sync_banner.png)
## Notification effect errors
在 monitor 评估成功后，通知可能无法发送。如果发生这种情况，history event 将显示一个标签，指示该 event 的通知未发送给订阅者，并提供其他详细信息，例如错误标识符和错误消息。

After a successful monitor evaluation, notifications may fail to send. If this occurs, the history event will show a tag indicating that notifications for that event were not sent to subscribers, along with additional details such as an error identifier and error message.
## Action effect errors
在 monitor 评估成功后，Action 效果可能无法执行。此失败可能由多种原因造成，包括 Action 逻辑的更改导致其与 monitor 上保存的输入配置不兼容，或未满足 Action 的 [submission criteria](/docs/foundry/action-types/submission-criteria/)。如果发生此失败，history event 时间线将显示一个标签，指示该 event 的一个或多个 Actions 执行失败，并提供相关的错误详细信息。

After a successful monitor evaluation, Action effects may fail to execute. This failure could happen for a variety of reasons, including changes to the Action logic that make it incompatible with the saved input configuration on the monitor, or because the [submission criteria](/docs/foundry/action-types/submission-criteria/) for the Action is not met. If this failure occurs, the history event timeline will show a tag indicating that one or more Actions failed to execute for that event, along with relevant error details.
## Permissions
Monitor 评估使用各个订阅者的权限。这是为了确保 monitor 评估及任何后续的 Action 或通知效果始终反映用户在 monitor 评估时可访问的数据。如果用户缺少查看输入 object type、saved exploration 和/或 object monitor 的权限，他们可能会看到与权限相关的错误消息，而不是成功的评估结果。我们强烈建议将 monitors 及其输入存储在共享的 [Projects](/docs/foundry/security/projects-and-roles/) 中。

Monitor evaluation uses the permissions of the individual subscribers. This is to ensure that monitor evaluation and any subsequent Action or notification effects will always reflect data that the user may access at the time the monitor is evaluated. If a user is missing permission to view the input object type(s), saved exploration(s), and/or the object monitor, they may see a permission-related error message instead of successful evaluation. We strongly recommend storing monitors and their inputs in shared [Projects](/docs/foundry/security/projects-and-roles/).