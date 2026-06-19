<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/actions/
---
# Actions
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品，为平台中所有业务自动化提供单一入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
当 object monitor 触发或恢复时，[Actions](/docs/foundry/action-types/overview/) 可能会自动运行。

[Actions](/docs/foundry/action-types/overview/) may be automatically run when an object monitor triggers or recovers.
## Configuring Actions
订阅者可以配置 Actions，使其在出现新的 [monitor triggered](/docs/foundry/object-monitors/activity/#monitor-triggered) 活动事件时运行。Action 将在评估完成后由 monitor 自动提交。如果多个用户配置了 Actions，则 Actions 将针对每个用户分别运行。

Subscribers may configure Actions to run when there is a new [monitor triggered](/docs/foundry/object-monitors/activity/#monitor-triggered) activity event. The Action will be submitted automatically by the monitor as soon as the evaluation completes. If multiple users have configured Actions, Actions will be run separately for each user.
![action\_visibility\_settings\_monitoring](/docs/resources/foundry/object-monitors/action_visibility_settings_monitoring.png)
## Affected objects
对于事件条件，monitor 检测到的 object 集合可以作为 object set parameter 传递给 Action。在 [monitor configuration](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-monitors-application) 页面的 **Actions** 标签页中，应将该 parameter 配置为接受与所监控 object type 相同的 `ObjectSet<>`。系统将提供用于选择 object 集合的选项。

For event conditions, the set of objects detected by the monitor can be passed into the Action as an object set parameter. In the **Actions** tab of the [monitor configuration](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-monitors-application) page, the parameter should be configured to accept an `ObjectSet<>` of the same object type that is being monitored. An option to provide the set of objects will become available for selection.
![Configure Actions in Object Monitors app](/docs/resources/foundry/object-monitors/management_app_configure_actions.png)
> **⚠️ 警告**

> 该 object set 不能用作 Action 通知的输入；只有配置该 Action effect 的用户才能访问该 monitor 执行中受影响 object 的集合。
> **⚠️ 警告**

> This object set cannot be used as an input to Action notifications; only the user who configured the Action effect will have access to the set of affected objects for that monitor execution.
## Action visibility settings
并非所有 Actions 都适合与 object monitors 一起使用。在 Ontology Manager 中配置 Action type 后，可以禁用某个 Action 使其不显示在 object monitoring 中。创建 Action type 后，从 **Action type** 列表中点击该 Action type 以查看其详细信息，然后在左侧面板中点击 **Security & Submission Criteria** 标签页。接着，找到 **Frontend consumers** 部分，关闭 "Allow An Object Monitor To Submit This Action" 的开关。

Not all Actions may be appropriate to use with object monitors. You can disable an Action from appearing in object monitoring once you configure the Action type in the Ontology Manager. After creating an Action type, view its details by clicking on the Action type from the **Action type** list, then click on the **Security & Submission Criteria** tab in the left side panel. Then, find the **Frontend consumers** section and toggle off the switch to "Allow An Object Monitor To Submit This Action".
![Disable Action visibility in Ontology Manager](/docs/resources/foundry/object-monitors/disable_action_visability@2x.png)
## Permissions
Actions 与订阅该 monitor 的特定用户相关联。这意味着，配置 Action 的订阅者必须通过该 Action 的 [submission criteria](/docs/foundry/action-types/submission-criteria/)。

Actions are associated with a specific user subscribed to the monitor. This means that a subscriber configuring an Action must pass the [submission criteria](/docs/foundry/action-types/submission-criteria/) for that Action.
Actions 不能代表其他订阅者进行配置。

Actions may not be configured on behalf of other subscribers.
> **⚠️ 警告**

> 由于 Actions 代表特定用户运行，如果该用户取消订阅，或者该用户账户被禁用或删除，Action 将不再运行。
> **⚠️ 警告**

> As Actions run on behalf of a specific user, the Action will no longer run if that user unsubscribes or if that user account is disabled or deleted.