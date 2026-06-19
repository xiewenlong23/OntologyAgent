<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/set-up-notification/
---
# Set up a notification
本教程演示如何设置带有通知的 action。

This tutorial demonstrates how to set up an action with a notification.
我们将使用一个 action，该 action 更新 `Alert` object 的 `Priority` property，同时通知作为该 Alert object 上的 property 存储的 `Assignee`（一个 Foundry 用户）。如果您想跟着操作，您需要预先完成以下设置：

We will be using an action which updates the `Priority` property of an `Alert` object, and also notifies the `Assignee` (a Foundry user) which is stored as a property on that Alert object. If you want to follow along, you'll need to have the following already set up:
* 一个具有正确 properties 并配置为可通过 actions 进行编辑的 object

* 一个 action，它接受您的一个 object 以及包含新优先级的参数，并更新指定 object 上的 priority property。如果您之前已遵循[actions 入门教程](/docs/foundry/action-types/getting-started/)，则应该已经完成了此设置。

* An object with the correct properties and configured to be editable via actions
* An action which takes in one of your objects as well as a parameter containing the new priority and updates the priority property on the specified object. If you previously followed [the tutorial on getting started with actions](/docs/foundry/action-types/getting-started/), you should already have this set up.
如果您不熟悉管理 objects，可以阅读有关[如何设置 object type](/docs/foundry/object-link-types/create-object-type/) 的内容。

If you are new to managing objects, you can read about [how to set up an object type](/docs/foundry/object-link-types/create-object-type/).
## Prerequisites
### Complete the Getting Started tutorial
本教程假定您已经完成了 actions 的 [Getting Started](/docs/foundry/action-types/getting-started/) 教程。

This tutorial assumes you already completed the [Getting Started](/docs/foundry/action-types/getting-started/) tutorial for actions.
### Add the assignee property to your object type
对于本教程，您需要在 `Alert` object 上拥有一个名为 `Case Managers` 的 property，其中包含当前已分配用户的 Foundry user ID。通常，如果您使用 actions 来构建工作流，您将能够使用应用程序中的 user selector 组件捕获和存储 user ID。这些将作为完整的用户名显示在 Foundry 中的任何位置。

For this tutorial, you will need to have a property on the `Alert` object that is called `Case Managers` and contains the Foundry user ID for the currently assigned user. Typically, if you are using actions to construct your workflow, you will be able to capture and store user IDs with the user selector components in your application. These will show up as full usernames wherever they are displayed in Foundry.
## Add a notification
首先，导航至更新工单优先级的 action。在 **Rules** 部分下，选择 **Add new rule**，然后选择 **Notification**。这将打开用于添加通知的配置对话框。

First, navigate to your action that updates the ticket priority. Under the **Rules** section select **Add new rule**, followed by **Notification**. This will open the configuration dialog for adding a notification.

> 📷 **[图片: Recipients configuration]**

> 📷 **[图片: Recipients configuration]**

## Configure recipients
在本例中，您将向 assignee 发送通知，该 assignee 作为正在编辑的 `Alert` object 的 property 存储。为此，请在 **Recipients** 下拉菜单中使用 "Recipient(s) from property of object parameter" 选项。选择作为 action 参数可用的 `Alert` object，然后在提示时选择 `Case managers` property。

For this example, you will send the notification to the assignee, which is stored as a property of the `Alert` object being edited. To do this, use the option "Recipient(s) from property of object parameter" in the **Recipients** dropdown. Select the `Alert` object that is available as a parameter to the action, then select the `Case managers` property when prompted.
您应该在配置的 **Recipients** 部分中看到所选的 object 参数和 property。请记住，接收者必须始终是 Foundry user ID。如果此 property 包含其他内容（例如字符串电子邮件地址），则不会发送任何通知。

You should see the selected object parameter and property displayed in the **Recipients** section of the configuration. Keep in mind that the recipient must always be a Foundry user ID. If this property contains something else such as string email addresses, no notifications will be sent.
> **ℹ️ 注意**

> 为了进行测试，您最初可能希望使用硬编码的接收者来配置 action，以验证逻辑和通知内容是否按预期配置。
> **ℹ️ 注意**

> For testing, you may initially want to configure the action with hardcoded recipient(s) that can be used to validate the logic and notification content is configured as expected.
![hardcoded recipients](/docs/resources/foundry/action-types/side_effects_notification_tutorial_static_test_user.png)
[了解有关其他收件人配置选项的更多信息。](/docs/foundry/action-types/notifications/#recipients)

[Learn more about other recipient configuration options.](/docs/foundry/action-types/notifications/#recipients)
## Configure notification content
接下来，您将通过自定义通知来配置通知内容，以按名称称呼收件人，并在内容中包含 `Alert` object 的旧优先级和新优先级。下面提供了一个通知配置示例。

Next, you will configure the content of the notification by customizing the notification to address the recipient by name and including the old and new priority of the `Alert` object in the content. An example notification configuration is available below.
首先，从内容选项中选择"Template"。这是配置内容最直接的方式，不需要编写任何代码。

First, select "Template" from the content options. This is the most straightforward way to configure the content and does not require writing any code.
对于主题行，输入您所需的消息。要添加参数引用，请添加正斜杠 `/`，然后从下拉列表中选择所需的参数。如果您的选择是 object 参数，系统将要求您选择要引用的 property。

For the subject line, enter your desired message. To add a parameter reference, add a forward slash `/` and select the desired parameter from the dropdown list.  If your selection is an object parameter, you will be asked to select which property you want to reference.
对于正文，输入按名称称呼收件人、标识进行更改的用户以及报告先前和更新后状态的文本。

For the body, enter text that addresses the recipient by name, identifies the user who made a change, and reports the previous and updated status.
与主题中的 object 引用一样，您可以从下拉列表中选择"Recipient"、"Current User"以及任何参数选项，以便生成对这些用户属性的正确引用。

As with the object reference in the subject, you can select the "Recipient", "Current User", and any parameter options from the dropdown list in order to generate the correct reference to those user attributes.
[了解如何使用更复杂的要求生成通知内容。](/docs/foundry/action-types/notifications/#content)

[Learn how to generate notification content with more complex requirements.](/docs/foundry/action-types/notifications/#content)
## Configure a link
最后，您将在 Object Explorer 中为指定的 `Alert` 的 Object View 添加一个 link。选择"Object View"，然后从下拉列表中选择您的工单 object 参数。然后，为 link 按钮添加一个标签，内容为 `View Ticket`。

Finally, you will add a link to the Object View of the specified `Alert` in Object Explorer. Select "Object View" and then select your ticket object parameter from the dropdown. Then, add a label for the link button that reads `View Ticket`.
现在您已准备好保存整个通知配置：

Now you are ready to save your entire notification configuration:

> 📷 **[图片: 完整配置]**

> 📷 **[图片: Full configuration]**

[了解可配置的其他类型 link 的更多信息。](/docs/foundry/action-types/notifications/#content)

[Learn more about other types of links that can be configured.](/docs/foundry/action-types/notifications/#content)
## Send a test notification
要进行验证，请创建一个将您自己作为受让人的测试 alert。为了运行该 action，您需要按照 [actions 文档](/docs/foundry/workshop/actions-overview/) 中的说明，在 Object Explorer 或通过 Workshop module 中的按钮中公开该 action。

To verify, create a test alert with yourself as the assignee. In order to run the action, you will then need to expose the action in Object Explorer or via a button in a Workshop module as described in the [actions documentation](/docs/foundry/workshop/actions-overview/).
完成测试更改后，您应该会同时收到一条平台内推送通知和一条发送至您 Foundry 用户配置文件中指定电子邮件账户的电子邮件通知。平台内和电子邮件通知的预览都显示在通知配置视图中。

Once you've made a test change, you should receive both an in-platform push notification and an email notification to the email account specified on your Foundry user profile. Previews for both in-platform and email notifications are displayed within the notification configuration view.
如果您没有收到电子邮件，可能是因为您已禁用电子邮件和/或平台内通知。您可以在 **User Settings** 下的 **Notifications** 中验证这一点。

If you did not receive an email, it may be because you have email and/or in-platform notifications disabled. You can verify this in **Notifications** under **User Settings**.
## Next steps
* 探索其他可选功能，例如用于收件人选择通过电子邮件接收通知时的 [custom content](/docs/foundry/action-types/notifications/#content-components)。

* 使用 [functions](/docs/foundry/functions/configure-notifications/) 为收件人或内容配置复杂逻辑。

* Explore other optional features, such as [custom content](/docs/foundry/action-types/notifications/#content-components) for when the recipient chooses to receive notifications via email.
* Configure complex logic for recipients or content using [functions](/docs/foundry/functions/configure-notifications/).