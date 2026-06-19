<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/activity/
---
# Activity
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品，为平台中所有业务自动化提供单一入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
Object monitor 活动根据 condition 以及某些 metadata properties 发生更改或更新时进行记录。

Object monitor activity is recorded based on the condition and when certain metadata properties are changed or updated.
用户订阅的所有 monitors 的活动时间线显示在 Object Monitors 应用程序的 **Overview** 页面上。

The activity timeline for all monitors subscribed to by a user is displayed on the **Overview** page of the Object Monitors application.
![Object Monitors app Overview page](/docs/resources/foundry/object-monitors/object_monitors_app_overview.png)
单个 monitor 的活动时间线显示在各个 monitor 概览面板的 **History** 标签页下。

The activity timeline for a single monitor is displayed under the **History** tab in the individual monitor overview panel.
![Objects Monitors app activity timeline](/docs/resources/foundry/object-monitors/object_monitors_app_activity_timeline.png)
## Activity event types
### `Monitor triggered`
当 threshold condition 的状态从 `false` 变为 `true` 时，以及当 event condition 检测到事件时，会记录 `Monitor triggered`。

`Monitor triggered` is recorded when a threshold condition changes status from `false` to `true` and when there are events detected for an event condition.
### `Monitor recovered`
当 threshold condition 的状态从 `true` 变为 `false` 时，会记录 `Monitor recovered`。Event conditions 永远不会产生 `monitor recovered` 活动。

`Monitor recovered` is recorded when a threshold condition changes status from `true` to `false`. Event conditions never result in `monitor recovered` activity.
### `Condition edited`
`Condition edited` 会在 Monitor Condition 被任何用户更新时记录。

`Condition edited` is recorded when the monitor condition is updated by any user.
### `Subscribed`
`Subscribed` 会在您订阅一个 monitor 时记录。未订阅期间的 Activity 将不会被记录或显示。

`Subscribed` is recorded when you subscribe to a monitor. Activity from periods where you are not subscribed will not be recorded or displayed.
### `Unsubscribed`
`Unsubscribed` 会在您取消订阅一个 monitor 时记录。未订阅期间的 Activity 将不会被记录或显示。

`Unsubscribed` is recorded when you unsubscribe from a monitor. Activity from periods where you are not subscribed will not be recorded or displayed.
### `Evaluation failed`
`Evaluation failed` 会在 monitor 因任何原因未能执行评估时记录。关于失败原因的详细信息可以从该 monitor 的 Activity **History** 视图中查看。即使 monitor condition 已成功评估,但通知或 Actions 失败时,也可能会显示 `Evaluation failed`。

`Evaluation failed` is recorded when a monitor fails to evaluate for any reason. Details about the failure can be viewed from the activity **History** view for that monitor. `Evaluation failed` may also be shown in cases where the monitor condition was successfully evaluated, but the notifications or Actions failed.
### `Muted`
`Muted` 会在 monitor 被任何用户静音时记录。静音操作对所有订阅者生效。被静音的 monitor 仍会被评估,但不会触发任何副作用(例如通知或 Actions)。

`Muted` is recorded when a monitor is muted by any user. Muting applies to all subscribers. Muted monitors will still be evaluated, but no side effects (e.g. notifications or Actions) will be triggered.
### `Unmuted`
`Unmuted` 会在 monitor 停止被静音时记录。静音操作对所有订阅者生效,并且 monitor 在静音期结束后会自动解除静音。

`Unmuted` is recorded when a monitor stops being muted. Muting applies to all subscribers, and monitors will be automatically unmuted after the mute time period expires.
### `Disabled`
`Disabled` 会在 monitor 被任何用户禁用,或由于活动过多而被自动禁用时记录。禁用操作对所有订阅者生效。被禁用的 monitor 不会被评估。

`Disabled` is recorded when a monitor is disabled by any user or when a monitor is automatically disabled due to excessive activity. Disabling applies to all subscribers. Disabled monitors are not evaluated.
### `Enabled`
`Enabled` 会在 monitor 停止被禁用时记录。启用操作对所有订阅者生效,并且 monitor 在禁用期结束后会被重新启用。

`Enabled` is recorded when a monitor stops being disabled. Enabling applies to all subscribers, and monitors are re-enabled after the disabled time period expires.