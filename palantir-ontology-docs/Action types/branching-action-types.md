<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/branching-action-types/
---
# Branching action types
Ontology actions 与 Global Branching 集成，使您能够在 branch 上测试 action types，而不会影响您的生产环境。您可以在隔离的 branch 上下文中运行 actions、验证它们的配置并观察编辑，然后再将更改合并到 `main`。

Ontology actions integrate with Global Branching, enabling you to test action types on a branch without affecting your production environment. You can run actions, validate their configurations, and observe edits in an isolated branch context before merging changes to `main`.
有关 Global Branching 概念和工作流程的一般信息，请参阅 [Global Branching 文档](/docs/foundry/global-branching/overview/)。

For general information on Global Branching concepts and workflows, refer to the [Global Branching documentation](/docs/foundry/global-branching/overview/).
## Running actions on a branch
您可以在 branch 上的 Workshop module 中测试 actions，以验证它们是否已正确配置。当所有相关的 object types 都在 branch 上建立索引后，您就可以运行该 action type 并查看 branch 上的 resulting edits。

You can test actions in a Workshop module on a branch to validate that they have been configured correctly. When all relevant object types are indexed on a branch, you can run the action type and see the resulting edits on the branch.
### Prerequisites
要在 branch 上运行 action，该 action type 编辑的所有 object types 都必须在该 branch 上建立索引。您可以通过单个 object type 页面或通过 Ontology Manager 中的 action type 页面来建立 object types 的索引。

To run an action on a branch, all object types that are edited by the action type must be indexed on that branch. You can index object types through the individual object type page or through the action type page in Ontology Manager.
![Action indexing banner on a branch.](/docs/resources/foundry/action-types/action-indexing-banner.png)
> **ℹ️ 注意**

> 在 branch 上运行 actions 旨在作为一种测试机制。在 branch 上对 action 所做的 edits 不会被合并回 `main`。
> **ℹ️ 注意**

> Running actions on a branch is intended as a testing mechanism. Action edits on a branch will not be merged back into `main`.
### Working with function-backed actions on a branch
branch 上的 function-backed actions 的行为取决于它们是否具有 branch-aware 特性。Branch-aware functions 可以在 branch 上修改并读取其中的 schemas，而非 branch-aware functions 仅从 `main` 读取 schemas。无论是否具有 branch-awareness，所有 function-backed actions 仅在 branch 上执行，不会将更改写回 `main`。有关支持的 function 类型，请参阅 [Global Branching 文档](/docs/foundry/global-branching/integrations/)。

Function-backed actions on a branch behave differently depending on whether they are branch-aware. Branch-aware functions can be modified on the branch and read schemas from it, while non-branch-aware functions only read schemas from `main`. Regardless of branch-awareness, all function-backed actions execute only on the branch and do not write changes back to `main`. See supported function types in the [Global Branching documentation](/docs/foundry/global-branching/integrations/).
## Managing side effects on branches
> **ℹ️ 注意**

> 以下信息专门适用于通过 actions 在 branches 上应用的 webhooks、具有外部调用的 functions 以及 notifications。通过其他方式应用的副作用将按照这些 consumers 的定义行为运行。
> **ℹ️ 注意**

> The following information applies specifically to webhooks, functions with external calls, and notifications that are applied **via actions** on branches. Side effects applied through other means will behave as defined by those consumers.
### Webhooks
默认情况下，当 action 在 branch 上应用时，webhooks 不会执行。此行为是为了防止在测试环境中意外写入外部系统。

By default, webhooks do not execute when an action is applied on a branch. This behavior is to prevent accidentally writing to external systems while in a testing environment.
在这种情况下，您将看到一个 toast notification，指示此行为。

In such cases, you will see a toast notification indicating this behavior.
![A toast notification indicating action applied but webhook not executed.](/docs/resources/foundry/action-types/action-webhook-toast.png)
但是，在某些情况下，在 branch 上测试 webhook 是可取的，例如在访问 READ endpoint 时。

However, there are some cases where testing a webhook on a branch is desirable, for instance when hitting a READ endpoint.
要覆盖默认行为，请在 Ontology Manager 中配置 action type 的 **Security and submission criteria** 选项卡，以在 branches 上启用 webhook executions。

To override the default behavior, configure the action type's **Security and submission criteria** tab in Ontology Manager to enable webhook executions on branches.
![Enable webhooks on branches setting.](/docs/resources/foundry/action-types/action-webhook-setting.png)
> **ℹ️ 注意**

> 如果在 branches 上启用了 webhooks，则 webhook 将按照在 `main` 上完全相同的方式运行。因此，如果 webhook 配置为访问外部生产环境，即使 action 在 branch 上执行，它仍将继续执行此操作。
> **ℹ️ 注意**

> If webhooks on branches are enabled, the webhook will run exactly as it would on `main`. Consequently, if the webhook is configured to hit an external production environment, it will continue to do that even if the action is executed on a branch.
### Functions with external calls
默认情况下，当 action 在 branch 上应用时，具有外部调用的 function-backed action 逻辑不会执行；该 action 会完全失败。此行为是为了防止在测试环境中意外写入外部系统。

By default, function-backed action logic with external calls does not execute when an action is applied on a branch; the action fails entirely. This behavior is to prevent accidentally writing to external systems while in a testing environment.
在这种情况下，您将看到一个 toast notification，指示失败，并附带对此行为的解释。

In such cases, you will see a toast notification indicating failure, with an explanation of the behavior.

> 📷 **[图片: External function call blocked the action.]**

> 📷 **[图片: External function call blocked the action.]**

然而，在分支上进行测试有时是必要的，例如调用 READ endpoints 时。您可以通过在 Ontology Manager 中 action type 的 **Security and submission criteria** 选项卡中启用 functions with external calls on branches 来覆盖此限制。

However, testing on branches is sometimes necessary, for example, when calling READ endpoints. You can override this restriction by enabling functions with external calls on branches in the action type's **Security and submission criteria** tab in Ontology Manager.
![Enable functions with external calls on branches setting.](/docs/resources/foundry/action-types/action-function-setting.png)
> **ℹ️ 注意**

> 如果在分支上启用了 functions with external calls on branches，该 function 将发出与在 `main` 上相同的 external calls。因此，如果该 function 配置为访问外部生产环境，即使该 action 在分支上执行，它也会继续访问该环境。
> **ℹ️ 注意**

> If functions with external calls on branches are enabled, the function will make the same external calls as it would on `main`. Consequently, if the function is configured to hit an external production environment, it will continue to do that even if the action is executed on a branch.
### Notifications
默认情况下，当 action 在分支上应用时，notifications 不会执行。此行为是为了防止在测试环境中意外通知收件人。

By default, notifications do not execute when an action is applied on a branch. This behavior is to prevent accidentally notifying recipients while in a testing environment.
在这种情况下，您将看到一个指示此行为的 toast notification。

In such cases, you will see a toast notification indicating this behavior.
![Toast notification indicating action applied but notification not executed.](/docs/resources/foundry/action-types/action-notification-toast.png)
但是，在某些情况下，在分支上测试 notifications 是可取的。

However, there are some cases where testing notifications on a branch is desirable.
要覆盖默认行为，您可以在 Ontology Manager 中 action type 的 **Security and submission criteria** 选项卡中启用分支上的 notifications。

To override the default behavior, you can enable notifications on branches in the action type's **Security and submission criteria** tab in Ontology Manager.
此外，您可以指定 action 在分支上运行时的 notification recipients：

Additionally, you can specify the notification recipients when the action runs on a branch:
* **Branch owner：** 将所有 notifications 发送给 branch owner。

* **Default recipients：** 通知原始 notifications 上配置的 recipients。

* **Branch owner:** Send all notifications to the branch owner.
* **Default recipients:** Notify the recipients configured on the original notifications.
![Enable notifications on branches setting.](/docs/resources/foundry/action-types/action-notification-setting.png)
## Known limitations
* 分支上的 action 编辑仅用于测试，不会合并回 `main`。

* 默认情况下，在分支上运行 action 时，webhooks 和 email notifications 不会执行。

* 默认情况下，对外部系统进行调用的 functions 在分支上运行 action 时会失败。

* Action edits on a branch are for testing only and will not be merged back into `main`.
* Webhooks and email notifications are not executed by default when an action is run on a branch.
* Functions that make calls to external systems will fail by default when an action is run on a branch.