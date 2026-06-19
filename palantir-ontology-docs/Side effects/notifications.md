<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/notifications/
---
# Notifications
可以通过 **Add new rule** 下拉菜单向 action 添加 notification。[了解更多关于如何添加 notification 的信息。](/docs/foundry/action-types/set-up-notification/)

Notifications can be added to an action through the **Add new rule** dropdown menu. [Learn more about how to add a notification.](/docs/foundry/action-types/set-up-notification/)

> 📷 **[图片: Dropdown menu for Add new rule]**

> 📷 **[图片: Dropdown menu for Add new rule]**

配置 notification 需要指定 [recipients](#recipients) 和 [content](#content)。以下部分将详细介绍这些选项。

Configuring a notification requires specification of [recipients](#recipients) and [content](#content). The following sections provide more detail on these options.
## Recipients
配置 notification 的 **Recipients** 选项允许您指定一组 Foundry 用户，这些用户将在 action 运行时收到 notification。Notification 将分别发送给每个 recipient。在 email notification 中不支持将用户添加为 CC（抄送）recipient。

Configuring the **Recipients** option of a notification allows you to specify the set of Foundry users who will receive a notification when the action runs. Notifications will be sent to each recipient individually. Adding users as CC (carbon copy) recipients to email notifications is not supported.
指定 recipients 有以下几种支持的方式：

There are several supported ways of specifying recipients:

> 📷 **[图片: Recipients Dropdown]**

> 📷 **[图片: Recipients Dropdown]**

* **Static：** 在配置中，您可以选择一组用户或群组，当 action 运行时将始终通知他们。

* **From a parameter：** 如果您有一个作为 Foundry user 或 group ID 的 action 参数，您可以将其指定为 notification 的 recipient。

* 这可以用于允许发送者在使用此 action 的 application 或 module 的用户界面中选择一个或多个 recipients，或者自动检测并将 notification 发送给运行该 action 的用户。

* **From an attribute of an object parameter：** 如果您有一个 object 参数，并且该 object 的某个 property 包含 Foundry user 或 group ID，您可以将该参数的 property 指定为 recipient。对于 Foundry user 和 group ID 的列表也可以使用此方式。

* **From a function：** 如果您的使用场景未被上述选项覆盖，您可以编写一个自定义 function，接收 action 参数并返回应被通知的用户或群组列表。[了解更多关于如何编写返回用户或群组列表的 function 的信息。](/docs/foundry/functions/types-reference/#users-groups-and-principals)

* **Static:** In the configuration, you may select a set of users or groups who will always be notified when the action runs.
* **From a parameter:** If you have a parameter to the action that is a Foundry user or group ID, you may specify this as your recipient for a notification.
* This can be used to allow the sender to select one or more recipients in the user interface of an application or module that uses this action, or to automatically detect and send a notification to the user running the action.
* **From an attribute of an object parameter:** If you have an object parameter to the action, and one of the properties of that object contains a Foundry user or group ID, you may specify that property of a parameter as the recipient. This is also possible for lists of Foundry user and group IDs.
* **From a function:** If your use case is not covered by the above options, you may write a custom function which takes in action parameters and will return the list of users or groups who should be notified. [Learn more about how to write a function that returns a list of users or groups.](/docs/foundry/functions/types-reference/#users-groups-and-principals)
基于 function 的 recipients 的使用场景示例包括：

Examples of use cases for recipients based on a function include:
* 组合其他 recipients 选项；例如，通知从 object 参数的 attribute 指定的 `assignee`，并始终通知一组额外的静态 recipients。

* 基于其他参数或参数 property 值的 recipient 选择；例如，每当 EMEA 出现新任务时，通知一组用户；每当北美出现新任务时，通知另一组用户。
* 任何其他不适合结构化选项的自定义逻辑。

* Combining the other options for recipients; for example, notifying the `assignee` specified from an attribute of an object parameter and also always notifying a static set of additional recipients.
* Recipient selection based on other parameters or property values of parameters; for example, whenever there is a new task in EMEA, notify one set of users; whenever there is a new task in North America, notify a different set of users.
* Any other custom logic which does not fit into the structured options.
> **ℹ️ 注意**

> Recipients 可以更改其 notification 传递方式的偏好设置。例如，一个用户可能选择仅通过 web 浏览器接收 notification，而另一个用户可能选择同时接收平台内 toast 和 email。如果用户在个人偏好设置中关闭了 action notification，他们将不会收到通知。但是，他们仍可在登录 Foundry 后通过进入 Workspace 中的 "Notifications" 然后点击 "See All" 来查看他们的 notification。
> **ℹ️ 注意**

> Recipients may change their preferences for how notifications are delivered to them. For example, one user may choose to only have notifications delivered in their web browser, while another user may choose to receive both in-platform toasts and emails. If a user has action notifications turned off in their personal preferences, they will not be notified. However, they may still view their notifications when logged into Foundry by going to "Notifications" and then "See All" in the Workspace.
## Content
有多种选项可用于自定义 notification 的内容。内容可以通过 *Template* 进行配置，也可以通过自定义 *function* 提供。选择 template 内容将允许您直接在配置对话框中配置完整内容。Function 内容将要求您拥有一个已发布的 function，该 function 返回适当的 notification 类型。

There are a number of options for customizing the content of notifications. Content may be configured via *Template* or provided via a custom *function*. Selecting template content will allow you to configure the full content directly in the configuration dialog. Function content will require you to have a published function, which returns the appropriate notification type.
![Content Type Dropdown](/docs/resources/foundry/action-types/side_effects_content_selection_dropdown.png)
### Content components
1. **Subject：** 通常，内容会包含一个 subject line。默认情况下，所有传递机制将使用相同的内容。

1. **Subject:** Usually, content will include a subject line. By default, this will be the same for all delivery mechanisms.
2. **Body：** Notification 的 body。对于平台内 notification，这将显示在 notification toast 内。对于 email，这将在 email 的 body 内呈现。

2. **Body:** The body of the notification. For in-platform notifications, this will display inside the notification toast. For email, this will be rendered inside the body of the email.
3. **Link：** 您可以指定一个 link。这将以按钮的形式显示在 notification body 内容的下方。按钮的文本可以自定义。

* 配置 link 时可使用以下选项：

* 链接到现有 object 参数

* 链接到 Workshop app

* 链接到 Carbon workspace

* 链接到新创建的 object

3. **Link:** You may specify a link. This will appear as a button just below the body content of the notification. The text of the button can be customized.
* The following options are available for configuring a link:
* Link to an existing object parameter
* Link to a Workshop app
* Link to a Carbon workspace
* Link to a newly created object
4. **Advanced Email Configuration：** 配置 notification 时，您可以指定一个自定义 content body，用于通过 email 传递 notification。该选项允许您使用 HTML 进行更高级的格式化，这是平台内 notification 不支持的。预览将向您展示 notification 的呈现效果，但不包括任何参数引用。Recipients 仅在其偏好设置为通过 email 接收 notification 时才会收到此内容。

4. **Advanced Email Configuration:** When configuring a notification, you may specify a custom content body to use when delivering a notification via email. This option allows you use HTML for more advanced formatting which is not supported for in-platform notifications. The preview will show you how your notification will look, excluding any parameter references. Recipients will only receive this content if they set their preference to receive notifications via email.
> **ℹ️ 注意**

> 三重大括号可用于引用上述 Subject、Body 和 Link 中的参数和用户属性。编辑某个部分时，点击可用参数之一将自动为该参数或用户属性生成正确的大括号引用。
> **ℹ️ 注意**

> Triple handlebars may be used to reference parameters and user attributes in the Subject, Body, and Link mentioned above. When editing a section, clicking on one of the available parameters will auto-generate the correct handlebar reference for that parameter or user attribute.
5. **来自 Function：**当选择 "From a Function" 时，您无需配置上述部分。相反，您必须提供一个 Function，该 Function 返回一个 `Notification` 对象，其属性指定自定义内容的每个部分。如果出现以下任何情况，您可能需要使用 Function：

* 通知内容根据收件人或 Action 的输入参数完全不同。
* 您希望为电子邮件和平台内通知使用不同的主题行。

* 您希望使用完整的链接 URL，包括指向 Foundry 外部系统或应用程序的链接。

* 您希望执行 Search Around、聚合或查询渲染内容时通过参数提供之外的数据。
* 您有任何其他无法通过模板内容选项实现的自定义需求。

5. **From a Function:** When selecting "From a Function", you do not configure the sections listed above. Instead, you must provide a Function that returns a `Notification` object with the appropriate properties specifying each section of your custom content. You may need to use a Function if any of the following applies:
* The notification content is completely different depending on the recipient or input parameters to the Action.
* You want to have a different subject line for email and in-platform notifications.
* You want to use full link URLs, including links to external systems or applications that live outside of Foundry.
* You want to perform Search Arounds, aggregations, or query data beyond what is provided via parameters when rendering the content.
* You have any other custom requirements that are not possible via the template content options.
有关 Notification 返回类型的更多信息，请参阅 [Functions 文档](/docs/foundry/functions/configure-notifications/)。

More information on the Notification return type can be found in the [Functions documentation](/docs/foundry/functions/configure-notifications/).
> **ℹ️ 注意**

> 用于生成通知内容的任何 Ontology 数据都将反映应用当前 Action 编辑之前的 Ontology 状态。为了让通知收件人能够访问特定对象的最新状态，可以在通知中嵌入指向通过对象参数引用的对象的链接，或指向新创建对象的链接（如果这些对象是通过 "create object" 规则而非通过 function 创建的）。
> **ℹ️ 注意**

> Any Ontology data used for generating notification content will reflect the state of the Ontology before edits of the current Action are applied. To give notification recipients access to the latest state of specific objects, it is possible to embed links to objects referenced via object parameters, or links to newly created objects (if those objects are created via a "create object" rule and not via a function) in the notification.
***
## Example configuration
这是一个通知的配置示例。

This is an example configuration for a notification.

> 📷 **[图片: 标记的示例通知配置]**

> 📷 **[图片: Example notification Configuration Labelled]**

1. **Recipients** 配置

2. **Content** 配置

* 从模板（在 Ontology 应用对话框中直接配置）或 Function（指定一个返回完整 `Notification` 对象的 Function）中进行选择。

3. 模板通知的 **Subject** 行。

4. 基于 Action 可用参数的 **parameters**。点击某个参数可生成引用该参数的 `{{{}}}` 语法。

5. 模板通知的 **Body** 内容。

6. 模板通知的 **Link** 配置（可选）。

7. 模板通知的 **自定义电子邮件 HTML 内容**（可选）。

1. **Recipients** configuration
2. **Content** configuration
* Choose from template (configure directly in the Ontology app dialog) or Function (specify a Function that returns a fully-formed `Notification` object).
3. **Subject** line for template notification.
4. Available **parameters** based on the available parameters to the Action. Click on a parameter to generate the `{{{}}}` syntax to reference that parameter.
5. **Body** content for template notification.
6. **Link** configuration for template notification (optional).
7. **Custom HTML content for email** with template notification (optional).
***
## Other key information
### Maximum recipient limits
* 使用 "From a Function" 选项渲染通知内容时，最多可有 50 个收件人。在内容配置选项下选择 "From a Function" 时，配置面板中会显示警告，并且每次运行 Action 时都会检查收件人数量。如果收件人数量超过限制，将显示红色错误提示，并且 Action 将无法运行。

* 当使用 "Template" 选项在配置对话框中直接配置内容时，单个 Action 通知最多可有 500 个收件人。

* There is a maximum of 50 recipients when using the "From a Function" option to render the notification content. There will be a warning in the configuration panel when selecting "From a Function" under the content configuration options, and the number of recipients will be checked each time the Action is run. If the number of recipients is over the limit, a red error toast will be displayed and the Action will fail to run.
* There is a maximum of 500 recipients for a single Action notification when the content is configured directly in the configuration dialog using the "Template" option.
![Function-rendered Content max-recipients warning](/docs/resources/foundry/action-types/side_effects_function_content_max_recipients.png)
### Content length limits
* 主题的最大长度为 250 个字符。

* 正文的最大长度为 1,000 个字符。当渲染电子邮件的自定义 HTML 内容时，最大长度为 51,200 个字符。

* The maximum subject length is 250 characters.
* The maximum body length is 1,000 characters. When rendering custom HTML content for email, the maximum length is 51,200 characters.
请注意，这些最大内容长度会在通知渲染时进行验证和截断。这意味着，如果渲染的内容是动态的（例如，通知内容包含对象数据），任何超过允许最大长度的内容都将被截断，并以尾部 `...` 表示。

Keep in mind that these maximum content lengths are validated and truncated when notifications are rendered. This means that if the rendered content is dynamic (for example, if the notification content includes object data), any content longer than the allowed maximum lengths will be truncated and indicated by trailing `...`.
### Strict redaction
如果为您的 Foundry 实例启用了出站电子邮件通知的 "Strict Redaction" 或 "Group Redaction"，则不会渲染自定义通知内容。相反，用户将收到如下所示的通用消息。选择 "View" 将引导他们进入 Foundry，在那里他们可以查看完整的通知内容。[详细了解 Foundry 中的电子邮件内容编辑。](/docs/foundry/email/email-content-redaction/)

If "Strict Redaction" or "Group Redaction" on outbound email notifications is enabled for your Foundry instance, custom notification content will not be rendered. Instead, users will receive the generic message shown below. Selecting "View" will direct them into Foundry where they can view the full notification content. [Learn more about email content redaction in Foundry.](/docs/foundry/email/email-content-redaction/)
![Strict redaction email content default](/docs/resources/foundry/action-types/side_effects_redacted_email_content.png)
### Recipient user accounts
* 将解析 Groups 为单个用户，以便在发送通知之前检查数据权限。

* Foundry 用户和组 ID 可通过 Settings 下的 Account 找到。通知的配置界面在选择一组静态收件人时提供用户和组的选择器。这将仅显示配置 Action 的人员具有足够权限的用户和组。

* 如果收件人是通过引用对象属性配置的，请确保该属性将 Foundry 用户或组 ID 存储为字符串。您可以使用条件格式来显示关联的用户或组显示名称（有关更多详细信息，请参阅 [value formatting 文档](/docs/foundry/object-link-types/value-formatting/)）。
* 不支持直接发送到电子邮件地址。

* Groups will be resolved to individual users in order to check permissions on the data before sending the notifications.
* Foundry user and group IDs can be found via Settings under Account. The configuration interface for notifications provides selectors for users and groups when choosing a static set of recipients. This will only display users and groups for which the person configuring the Action has adequate permissions.
* If recipient(s) are configured via reference to an object property, make sure the property stores the Foundry user or group ID as a string. You can use conditional formatting to display the associated user or group display name (for more detail, see the [value formatting documentation](/docs/foundry/object-link-types/value-formatting/)).
* Sending directly to email addresses is not supported.
### Links to newly-created objects
链接新对象时，必须引用新对象的主键，因为在通知渲染时尚未生成对象 RID。

You must reference the primary key of a new object when linking it, since an object RID is not generated by time the notification is rendered.
**示例：**您有一个 Action，用于创建一个新的 `task` 对象，并在创建任务时生成唯一 ID。在您的 Action 通知中，您使用 [Object Explorer 提供的参数选项](/docs/foundry/object-explorer/generate-urls/) 渲染指向新创建对象的链接。

**Example:** You have an Action that creates a new `task` object, and will be generating a unique ID when creating the task. Inside your Action notification you render a link to the newly created object using the [parameter options provided by Object Explorer](/docs/foundry/object-explorer/generate-urls/).
* 使用 Function 生成内容时，有两种支持的指定 URL 链接的方式：

* 完整链接示例：`https://<your-foundry-instance>.com/workspace/module/view/latest/<module-rid>`

* 相对链接示例：`/module/view/latest/<module-rid>`

* There are two supported ways of specifying URL links when using Function generated content:
* Full link example: `https://<your-foundry-instance>.com/workspace/module/view/latest/<module-rid>`
* Relative link example: `/module/view/latest/<module-rid>`
### Required data access for recipients
* 用户只能接收包含其有权查看数据的通知。

* 在存在多个接收者的情况下，所有接收者都必须有权访问通知内容中渲染的 object 数据。

* 配置 Action 时，在侧边栏的 **Security & Submission Criteria** 选项卡底部有两种处理通知失败的方法可供选择：

* **要求所有用户都具有权限（默认）：** 如果任何接收者没有所需的访问权限，在尝试应用该 Action 时将显示错误。如果发生这种情况，将不会编辑任何数据，也不会发送任何通知。

* **要求任何用户具有权限：** 如果至少有一个用户可以查看该 object，则该 Action 将成功。只有具有权限的用户才会收到通知。

* Users may only receive notifications containing data which they are allowed to view.
* In cases where there are multiple recipients, all recipients must have access to the object data rendered in the notification content.
* When configuring your Action, two methods of handling notification failures are available at the bottom of the **Security & Submission Criteria** tab in the sidebar:
* **Require all users to have permissions (default):** If any recipients do not have the required access, an error will be shown when attempting to apply the Action. If this happens, no data will be edited and no notifications will be sent.
* **Require any user to have permissions:** If at least one user can see the object, the Action will succeed. Only users with permissions will receive notifications.
### Override and disable email content redaction
[如果组织设置允许](/docs/foundry/email/email-content-redaction/#disable-email-redaction-in-action-types)，您可以绕过组织级别为特定 action type 设置的其他严格 redaction 设置，并使用一个发送未经编辑内容的 action type。

[If the organization settings allow](/docs/foundry/email/email-content-redaction/#disable-email-redaction-in-action-types), you can bypass other strict redaction settings set at the organization level for particular action types and have an action type that sends non-redacted content.
要覆盖电子邮件通知的 redaction，请导航至 **Security & Submission** 选项卡，然后选择 **Notification settings > Disable notification redaction**。

To override redaction for email notifications, navigate to the **Security & Submission** tab, then **Notification settings > Disable notification redaction**.
![Notifications settings with disable notification redaction option.](/docs/resources/foundry/action-types/notification_settings.png)
要了解如何为组织启用此功能，请参阅[电子邮件 redaction 文档页面](/docs/foundry/email/email-content-redaction/#disable-email-redaction-in-action-types)。

To learn how to enable this for the organization, refer to [the email redaction documentation page](/docs/foundry/email/email-content-redaction/#disable-email-redaction-in-action-types).