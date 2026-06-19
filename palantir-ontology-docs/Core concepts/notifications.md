<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/notifications/
---
# Notifications
Object Monitor 的订阅者可以选择在 monitor 出现新活动时接收通知。

Subscribers to an object monitor may choose to receive notifications when there is new activity for a monitor.
通知默认对所有订阅者启用,但可以为单个订阅者禁用。要禁用通知,请在 Object Monitors 应用程序中配置或编辑 monitor 时,点击 **Subscribers**(订阅者)选项卡中的铃铛图标。

Notifications are enabled by default for all subscribers but may be disabled for individual subscribers. To disable notifications, click the bell icon in the **Subscribers** tab when configuring or editing a monitor in the Object Monitors application.
![Disable notifications in Subscribers tab](/docs/resources/foundry/object-monitors/monitor_subscriber_notifications_configuration.png)
各个用户也可以配置他们希望如何接收来自 Object Monitors 的通知。您可以在 monitor 配置模态框的 **Notification**(通知)选项卡中配置通知,这些偏好设置将全局适用于该用户订阅的所有 monitor。

Individual users may also configure how they wish to receive notifications from Object Monitors. You can configure notifications in the **Notification** tab of the monitor configuration modal, and preferences apply globally for any monitors to which that user is subscribed.
![Configure notification settings](/docs/resources/foundry/object-monitors/monitor_notifications_settings.png)
| Category      | Activity types          |
| ------------- | ----------------------- |
| `Triggered`   | [Monitor triggered](/docs/foundry/object-monitors/activity/#monitor-triggered) |
| `Recovered`   | [Monitor recovered](/docs/foundry/object-monitors/activity/#monitor-recovered) |
| `Errors`      | [Evaluation failed](/docs/foundry/object-monitors/activity/#evaluation-failed) |
| `Other info`  | [Condition edited](/docs/foundry/object-monitors/activity/#condition-edited), [Subscribed](/docs/foundry/object-monitors/activity/#subscribed), [Unsubscribed](/docs/foundry/object-monitors/activity/#unsubscribed), [Muted](/docs/foundry/object-monitors/activity/#muted), [Unmuted](/docs/foundry/object-monitors/activity/#unmuted), [Disabled](/docs/foundry/object-monitors/activity/#disabled), or [Enabled](/docs/foundry/object-monitors/activity/#enabled) |
## Custom notification content
可以为 [monitor triggered](/docs/foundry/object-monitors/activity/#monitor-triggered) 和 [monitor recovered](/docs/foundry/object-monitors/activity/#monitor-recovered) 活动发出的通知进行自定义。您可以在 Object Monitors 应用程序中配置或编辑 monitor 时,在 **Notifications**(通知)选项卡中提供自定义通知配置。

The notifications emitted for [monitor triggered](/docs/foundry/object-monitors/activity/#monitor-triggered) and [monitor recovered](/docs/foundry/object-monitors/activity/#monitor-recovered) activity may be customized. You can provide a custom notification configuration in the **Notifications** tab when configuring or editing a monitor in the Object Monitors application.
### Templated rendering
当使用模板化渲染时,自定义内容(包括主题、正文、链接标签和链接目标)会直接显示在所提供的表单中。如果需要,还可以在高级电子邮件配置中使用 HTML。平台内和电子邮件通知的预览可以在表单右侧查看。

When using templated rendering, the custom content (including subject, body, link label, and link destination) is shown directly in the provided form. HTML can also be used in the advanced email configuration if desired. A preview of the in-platform and email notifications can be seen on the right side of the form.
![monitor\_custom\_notifications\_templated](/docs/resources/foundry/object-monitors/monitor_custom_notifications_templated.png)
### Function-backed rendering
当使用 Function-backed 渲染时,自定义内容由 Function 使用所提供的通知返回类型返回。对于具有事件条件的 monitor,该 Function 可以接受被监控 Object Type 的 `ObjectSet<>`,从而可以提取并渲染关于被 monitor 检测到的 Object 的数据,直接整合到通知内容中。

When using Function-backed rendering, the custom content is returned from a Function using the provided notification return type. For monitors with event conditions, the Function may accept an `ObjectSet<>` of the object type being monitored, making it possible to extract and render data about the objects that were detected by the monitor directly into the notification content.