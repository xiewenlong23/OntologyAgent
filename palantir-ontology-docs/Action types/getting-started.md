<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/getting-started/
---
# Getting started
在本指南中,我们将创建一个用于更改 ticket priority 的简单 action type。

In this guide, we will create a simple action type for changing the priority on a ticket.
我们将配置 submission criteria,以确保 priority 为 `P0`、`P1` 或 `P2`,并且 ticket status 为 `Open`。

We will configure submission criteria to make sure that the priority is `P0`, `P1` or `P2`, and that the ticket status is `Open`.
## Prerequisites
对于本指南,我们将使用一个 `Demo Ticket` object type,它具有四个 properties:

For this guide, we will use a `Demo Ticket` object type, which has four properties:
* `Ticket ID`
* `Title`
* `Priority`
* `Status`
* `Ticket ID`
* `Title`
* `Priority`
* `Status`
我们还有两个可用的 demo objects:

We also have two demo objects available:
|Ticket ID|Title          |Status|Priority|
|---------|---------------|------|--------|
|PDS-123  |Demo Ticket One|Open  |P2      |
|PDS-124  |Demo Ticket Two|Closed|P1      |
如果您愿意,可以在您的 Ontology 中重新创建这些内容,但这并不是必需的。

You can recreate these in your Ontology if desired, but it is not essential.
请注意,要使用户能够执行 action type configuration 中定义的 action,[需要额外配置](/docs/foundry/object-link-types/allow-editing/#set-up-the-prerequisites)。如果运行 Object Storage V2,用户必须通过 toggle 启用 edits。如果运行 Object Storage V1 (Phonograph),必须创建一个 writeback dataset。请注意,[Object Storage V1](/docs/foundry/object-databases/object-storage-v1/) 处于[计划弃用](/docs/foundry/platform-overview/development-life-cycle/)阶段;[迁移到 Object Storage V2](/docs/foundry/object-backend/osv1-osv2-migration/)。

Note that for a user to be able to take an action defined in an action type configuration, [additional configuration is required](/docs/foundry/object-link-types/allow-editing/#set-up-the-prerequisites). If running Object Storage V2, the user must enable edits with a toggle. If running Object Storage V1 (Phonograph), a writeback dataset must be created. Note that [Object Storage V1](/docs/foundry/object-databases/object-storage-v1/) is in a [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) phase of development; [migrate to Object Storage V2](/docs/foundry/object-backend/osv1-osv2-migration/).
## Create a new action type
我们首先创建一个用于更改 ticket priority 的新 action type。在 Ontology Manager 中,选择左侧边栏上的 **Action type**,然后在视图右上角选择 **New Action type**。

We start by creating a new action type for changing the ticket's priority. In the Ontology Manager, select **Action type** on the left sidebar, then choose **New Action type** at the top right of the view.
![Create a new action type](/docs/resources/foundry/action-types/actions_wizard.png)
创建向导允许您配置 action type 最重要的 features。为您的 action type 输入一个 **Display name**。接下来,选择 **Change object(s)** 选项并将其设置为 **Modify**。从后续的下拉菜单中,选择 `Demo Ticket` object type,并通过选择 **Add property** 添加 `Priority` property。最后,在右下角选择 **Create**。

The creation wizard allows you to configure the most important features of an action type. Enter a **Display name** for your action type. Next, select the **Change object(s)** option and set it to **Modify**. From the following dropdown, select the `Demo Ticket` object type and add the `Priority` property by selecting **Add property**. Finally, select **Create** in the bottom right.
现在,您可以看到 action type 的完整详细视图。您可以进行其他调整,例如在 **Overview** tab 中添加 **Description**,或在 **Rules** tab 中添加要修改的其他 properties。

You can now see the full detailed view of your action type. You can make additional adjustments, like adding a **Description** in the **Overview** tab or adding additional properties to modify in the **Rules** tab.
## Edit parameters
选择 **Forms** tab 以查看参数概览。`Ticket` 和 `Priority` 参数已由 **Rule** 创建完成。

Select the **Forms** tab to get an overview of the parameters. The `Ticket` and `Priority` parameter have already been created based by the **Rule**.
![Actions form](/docs/resources/foundry/action-types/actions_form.png)
选择 `Priority` 参数来限制它可以接受的值。将约束从 **User input** 更改为 **Multiple choice**。这将允许你为此参数挑选可选的值。添加 `P0`、`P1` 和 `P2` 作为选项。如果现在将你的 action 应用到一个 object 上，你就可以将 ticket 的 priority 更改为 `P0`、`P1` 或 `P2`。接下来，你将添加 submission criteria，将其限制为只能更改 open ticket 的 priority。

Select the `Priority` parameter to limit the values it can take on. Change the constraints from **User input** to **Multiple choice**. This will allow you to pick what values can be chosen for this parameter. Add `P0`, `P1` and `P2` as options. If you applied your action to an object now, you could change the priority of a ticket to `P0`, `P1`, or `P2`. You will now add submission criteria that will restrict you to only changing the priority for open tickets.
![Priority parameter](/docs/resources/foundry/action-types/actions_constraints.png)
## Add submission criteria
从侧边栏打开 **Security & Submission Criteria** 标签页中的 submission criteria 部分。在 **Execution** 部分选择 **Condition** 来创建一个新条件。使用 **Parameter** 条件模板，对 `Ticket Status` object parameter 的 `Ticket` property 设置一个条件。使用 `is` 运算符，你可以在 ticket status 与特定值 `Open` 之间进行精确的字符串比较。

Open the submission criteria section in the **Security & Submission Criteria** tab from the sidebar. Create a new condition by selecting **Condition** in the **Execution** section. Using the **Parameter** condition template, set a condition on the `Ticket Status` object parameter's `Ticket` property. Using the `is` operator, you can then do an exact string comparison between the ticket status and the specific value `Open`.
![Submission criteria](/docs/resources/foundry/action-types/actions_submission_criteria.png)
添加一条 failure message，以便用户可以看到 action 失败的原因。你的 action 定义现在已完成，可以将其配置为显示在 Object Explorer 中 Object View 的旁边。

Add a failure message so users can see why an action has failed. Your action definition is now complete, and you can configure it to show up next to the Object View in Object Explorer.
## Add the action to an Object View
前往 **Demo Ticket One** 并编辑其 Object View。在顶部添加一个新 widget，并选择 **Actions** widget。在侧边栏中选择 **Add Item。** 从 Ontology Manager 复制并粘贴 action RID，然后将其粘贴到 Action RID 字段中。将 label 命名为 "Change Ticket Priority"。

Go to **Demo Ticket One** and edit its Object View. Add a new widget to the top, and choose the **Actions** widget. In the sidebar, select **Add Item.** Copy and paste the action RID from the Ontology Manager and paste it into the Action RID field. Name the label "Change Ticket Priority".
![Add the action to an Object View](/docs/resources/foundry/action-types/getting_started_add_RID.png)
默认情况下，action form 会将每个 parameter 显示为 action form 中的一个字段，包括 `Ticket` parameter。此外，action 不知道应该将当前 object 填入 `Ticket` parameter。我们将配置 action form 以隐藏 ticket 字段（这样用户就无法更改其他 ticket 的 status），并将其值设置为当前 object。

在 **Default value** 下，选择 **Add Item**。输入 `Ticket` parameter 的 parameter ID——在本教程中，我们将其设置为 `ticket`。将 value type 更改为 **Environment variable**，然后选择 **Current object**。最后，将 display option 更改为 **Hidden**。

By default, the action form will show every parameter as a field in the action form, including the `Ticket` parameter. Additionally, an action does not know that it should fill the current object in for the `Ticket` parameter. We will configure the action form to hide the ticket field (so the user cannot change the status of a different ticket), and set its value to the current object.
Under **Default value**, select **Add Item**. Type the parameter ID for the `Ticket` parameter—in this tutorial, we set it to `ticket`. Change the value type to **Environment variable** and select **Current object**. Finally, change the display option to **Hidden**.
![Configure the action form](/docs/resources/foundry/action-types/getting_started_configure_action_form.png)
你现在将在预览页面上看到 action button：

You will now see the action button on the preview page:
![Action button on Preview page](/docs/resources/foundry/action-types/getting_started_preview_page.png)
现在你可以保存并发布 Object View。

You can now save and publish the Object View.
## Apply the action
访问一个 open ticket 并选择我们配置的 **Change Ticket Priority** button。你应该会看到 action form 出现在视图上方。点击 **Priority** 字段将显示我们在该 parameter 上配置的单个所选 submission criterion：

Visit an open ticket and select the **Change Ticket Priority** button we configured. You should see the action form appear over the view. Clicking into the **Priority** field will show the single selected submission criterion we configured on the parameter:
![Changing ticket priority with action](/docs/resources/foundry/action-types/getting_started_apply_action.png)
选择一个 priority 并选择 submit。form 将消失，object view 将更新为新的 priority。我们的 submission criteria 规定，不应该对 closed ticket 运行此 action——如果我们打开已关闭的 Demo Ticket Two，我们会看到以下内容：

Pick a priority and select submit. The form will disappear and the object view will update with the new priority. Our submission criteria said that it should not be possible to run this action on a closed ticket—if we open Demo Ticket Two, which is closed, we see the following:
![Submission criteria prevents action from running on closed ticket](/docs/resources/foundry/action-types/getting_started_testing_validation.png)
## Resolve conflicting user edits (actions) and datasource updates
Foundry Ontology 中的 object instances 既可以通过 input datasource 创建和修改，也可以通过用户编辑/操作进行修改。当单个 object instance（即具有特定主键值的行或 object）同时从 input datasource 和用户编辑接收数据时，必须使用 conflict resolution strategy 透明地解析这些接收到的值。

Object instances in the Foundry Ontology can be created and modified by both input datasources and user edits/actions. When a single object instance (that is, a row or object with a specific primary key value) receives data from both the input datasource and user edits, these received values must be transparently resolved with a conflict resolution strategy.
有两种解决冲突的策略：

There are two strategies for resolving conflicts:
* 策略一：应用用户编辑（默认）
* 策略二：应用最新值（在你的注册中可能不可用）

* Strategy 1: Apply user edits (default)
* Strategy 2: Apply most recent value (may not be available on your enrollment)
[了解更多关于如何解决冲突的用户编辑和 datasource 更新的信息。](/docs/foundry/object-edits/how-edits-applied/#resolve-conflicting-user-edits-and-datasource-updates)

[Learn more about how to resolve conflicting user edits and datasource updates.](/docs/foundry/object-edits/how-edits-applied/#resolve-conflicting-user-edits-and-datasource-updates)
## Next steps
* [了解更多关于 action 权限的信息。](/docs/foundry/action-types/permissions/)

* [创建一个 function-backed action。](/docs/foundry/action-types/function-actions-getting-started/)

* [在平台的其他地方使用 action。](/docs/foundry/action-types/use-actions/)

* [解决冲突的用户编辑（actions）和 datasource 更新](/docs/foundry/object-edits/how-edits-applied/#resolve-conflicting-user-edits-and-datasource-updates)

* [Learn more about action permissions.](/docs/foundry/action-types/permissions/)
* [Create a function-backed action.](/docs/foundry/action-types/function-actions-getting-started/)
* [Use an action elsewhere in the platform.](/docs/foundry/action-types/use-actions/)
* [Resolve conflicting user edits (actions) and datasource updates](/docs/foundry/object-edits/how-edits-applied/#resolve-conflicting-user-edits-and-datasource-updates)