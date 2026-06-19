<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/permissions/
---
# Permissions
Permissions 以以下方式应用于 action types:

Permissions apply to action types in the following ways:
* 谁可以查看给定的 action type?

* 谁可以编辑给定的 action type?

* 谁可以使用给定的 parameters 集合来应用 action type?

* Who can view a given action type?
* Who can edit a given action type?
* Who can apply an action type with a given set of parameters?
## Apply action
应用 action type 的能力取决于它正在编辑的 object types 和 link types 的配置。在所有情况下,提交 action 的用户必须能够查看被编辑的 object types 和 link types 及其 datasources,并通过 [submission criteria](/docs/foundry/action-types/submission-criteria/)。如果 object type 仅允许通过 actions 进行编辑,则用户可以对其可查看的所有 objects 进行编辑。对于允许通过 actions 之外的方式进行编辑的 object types 和 link types,如果 object type 或 link type 由 dataset 支持,则用户还需要具有 writeback dataset 的编辑权限。如果 object type 或 link type 由 [Restricted View](/docs/foundry/security/restricted-views/) 支持,则用户需要通过 edit policy。

The ability to apply an action type depends on the configuration of the object types and link types it is editing. In all cases, the user submitting the action must be able to view the edited object types and link types and their datasources, and pass the [submission criteria](/docs/foundry/action-types/submission-criteria/). If the object type only allows edits via actions, users can make edits for all the objects they can view. For object types and link types allowing edits beyond actions, the user also needs edit permissions on the writeback dataset if the object type or link type is backed by a dataset. If the object type or link type is backed by a [Restricted View](/docs/foundry/security/restricted-views/), the user needs to pass the edit policy.
> **ℹ️ 注意**

> 使用侧边栏中的 **Check access** 面板检查用户对 Workshop 模块的访问权限,包括对相关 action types 及其 submission criteria 的访问权限。有关更多信息,请参阅 [check access panel documentation](/docs/foundry/security/checking-permissions/)。
> **ℹ️ 注意**

> Use the **Check access** panel in the sidebar to check a user's access to a Workshop module, including access to dependent action types and their submission criteria. For more information, review the [check access panel documentation](/docs/foundry/security/checking-permissions/).
### Submission criteria
Action submission criteria 允许对谁可以运行 action 进行细粒度控制。简单的 submission criteria 可以要求特定的用户 ID 或 group ID,并可以与 parameters 中的信息结合使用。有关更多信息,请参阅 [submission criteria documentation](/docs/foundry/action-types/submission-criteria/)。

Action submission criteria allow for fine-grained control over who can run an action. Simple submission criteria can require a specific user ID or group ID and can be combined with information from parameters. For more information see the [submission criteria documentation](/docs/foundry/action-types/submission-criteria/).
### Object edits permissions
Object 编辑可以设置为锁定模式（即仅允许通过 Action 进行编辑），也可以重新打开（允许通过 Action、Foundry Forms、直接的 Object Explorer 编辑以及 API 调用进行编辑）。为了在多个工作流中强制执行一致的安全范式，默认情况下，新创建的 Object Type 仅允许通过 Action 进行编辑。不建议在其他新场景中使用其他编辑方式。

Object edits can either be locked down so that edits are only allowed via actions, or reopened so that edits are allowed via actions, Foundry Forms, direct Object Explorer edits, and API calls. To enforce a consistent security paradigm across many workflows, by default, new object types only allow edits via actions. Other forms of edits are not recommended for new usage.
对于仅允许通过 Action 进行编辑的 Object Type，提交 Action 的用户仅需对正在被编辑的 Object 拥有 `Read` 访问权限即可。这意味着用户可以创建他们自己无法查看的 Object。

For object types that only allow edits via actions, the user submitting the action will only need `Read` access on the objects that are being edited. This means that it is possible for users to create objects that they cannot view.
相比之下，当一个由 dataset 支持的 Object Type 允许通过 Action、Foundry Forms、直接的 Object Explorer 编辑以及 API 调用进行编辑时，提交 Action 的用户必须对所有被编辑 Object 的 writeback dataset 拥有 `Edit` 权限。拥有 `Edit` 权限的用户将能够查看 writeback dataset 中的所有数据。

By contrast, when an object type backed by a dataset can be edited by actions, Foundry Forms, direct Object Explorer edits, and API calls, the user submitting the action must have `Edit` permissions on the writeback datasets of all objects being edited. A user with `Edit` permissions will be able to view all data in a writeback dataset.
因此，不建议将 Object Type 设置为允许通过 Action、Foundry Forms、直接的 Object Explorer 编辑以及 API 调用进行编辑，因为仅为 Object 编辑授予 `Edit` 权限可能会向用户暴露比完成 Ontology 编辑工作流所需更多的数据。

Therefore, setting an object type to be edited by actions, Foundry Forms, direct Object Explorer edits, and API calls is discouraged since granting `Edit` permissions simply for object editing may expose more data to a user than is required to complete the Ontology editing workflow.
无论使用哪种 writeback 设置，Action Type 的配置中都不会显示受影响底层 Object Type 的权限设置；配置 Action Type 的人员必须确保这些权限设置正确无误。

With either writeback setting, an action type's configuration does not display permission settings on affected underlying object types; the person configuring the action type must ensure that these permissions are correct.
将 Object Type 的编辑权限更新为"仅允许通过 Action 进行编辑"不会删除历史记录中的非 Action 编辑，但会阻止通过 Foundry Forms、直接的 Object Explorer 编辑以及 API 调用进行的进一步编辑。

Updating edit permissions on an object type to "Only allow edits via actions" will not remove historical, non-action edits, but they will prevent further edits from Foundry Forms, direct Object Explorer edits, and API calls.
![Only allow edits via actions is recommended.](/docs/resources/foundry/action-types/recommended-writeback-setting.png)
[详细了解 writeback 权限。](/docs/foundry/object-permissioning/configuring-rv-access-controls/)

[Learn more about writeback permissions.](/docs/foundry/object-permissioning/configuring-rv-access-controls/)
## Side effect permissions
任何能够创建 Action 的用户都可以配置 side effect。

Any user who can set up an action may configure side effects.
* 默认情况下未启用 Webhook side effect。在 Action 配置页面中使用 webhook 插件之前，需要额外的权限在 Data Connection 应用中对其进行配置。如有关于在 Foundry 实例中使用 webhook 的任何问题，请联系您的 Palantir 代表。

* Webhook side effects are not enabled by default. Additional permissions are required to configure a webhook plugin in the Data Connection app before it can be used in the actions setup page. Contact your Palantir representative with any questions about using webhooks on your Foundry instance.
提交条件必须正常通过；如果 Action 的提交条件未通过，则不会触发 side effect。

Submission criteria must pass as normal; if the action submission criteria fail, then side effects will not be triggered.
收件人必须拥有访问通知中包含的任何 Object 数据的权限。

Recipients must have access to any object data included in the notifications.
* 如果用户没有访问通知内容中包含的所有数据的权限，则不会向其发送通知。
* 如果存在多个收件人，且其中部分用户缺少访问通知中包含的数据所需的正确权限，则仅会向具有足够权限的用户发送通知。
* 如果通知因任何原因发送失败，编辑操作仍可能成功。

* If a user does not have access to all data included in the notification content, the notification will not be sent to them.
* If there are multiple recipients and some are missing the correct permissions data included in the notification, only the users with sufficient permissions will be notified.
* If notifications fail to send for whatever reason, edits may still succeed.
执行 Action 的用户必须能够查看将接收通知的用户和/或用户组。

The user executing the Action must be able to view the users and/or groups that will be receiving a notification.