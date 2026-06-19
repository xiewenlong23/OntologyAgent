<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/config-app-sidebar/
---
# Configure the applications sidebar
**applications sidebar** 用于显示和嵌入与当前 object 相关的 applications、analyses、actions 和其他资源。applications sidebar 在视觉上将这些资源与该 object 的主要内容区分开来。

The **applications sidebar** is used to display and embed applications, analyses, actions, and other resources related to the current object. The applications sidebar visually differentiates these resources from the main content of that object.
applications sidebar 支持嵌入所有基于 object 的 applications,包括 [Workshop](/docs/foundry/workshop/overview/)、[Quiver](/docs/foundry/quiver/overview/)、[Slate](/docs/foundry/slate/overview/)、[Action types](/docs/foundry/action-types/overview/) 等。添加到 sidebar 后,您可以在 object 的上下文中打开这些 applications。sidebar 还支持参数化 URLs,以链接到其他 apps 和外部网站。

The applications sidebar supports embedding all object-based applications, including [Workshop](/docs/foundry/workshop/overview/), [Quiver](/docs/foundry/quiver/overview/), [Slate](/docs/foundry/slate/overview/), [Action types](/docs/foundry/action-types/overview/), and more. Once added to the sidebar, you can open these applications within the context of the object. The sidebar also allows parameterized URLs to link to other apps and external websites.
在下面的示例中,您可以看到一个 `Airport` object。body 选项卡包含有关该 object 的主要信息,而相关 applications 包括:

In the example below, you can see an `Airport` object. The body tab includes primary information about that object, while related applications include:
* 一个用于航班延误的 Workshop Alert Inbox,用于分流交通;

* 一个用于管理机场乘客容量的 Slate application;以及

* 一个用于机场 COVID 响应的专用 application。

* A Workshop Alert Inbox on flights delays, used to triage traffic;
* A Slate application used to manage the airport’s passengers capacity; and
* A dedicated application for airport COVID response.
![Application sidebar in Object View](/docs/resources/foundry/object-views/application-sidebar-object-view.png)
## Set up the applications sidebar
applications sidebar 是每个 Object View 的可选加入式附加项。在您向其添加 group 之前,sidebar 对用户不可见。**Add new group** 选项可以在 **Sidebar** 选项卡下找到,也可以通过展开 sidebar 本身找到(如下图所示)。一旦 builder 添加 applications 和/或 actions 并发布该版本,sidebar 将显示给最终用户。如果 sidebar 仅包含空的 group 或 groups,则不会显示。

The applications sidebar is an optional, opt-in addition per Object View. The sidebar is not visible to users until you add a group to it. The **Add new group** option can be found under the **Sidebar** tab or by expanding the sidebar itself (as shown in the image below). Once a builder adds applications and/or actions and publishes that version, the sidebar will be displayed to end users. The sidebar will not be displayed if it only contains an empty group or groups.
![Add new application sidebar group in Object View](/docs/resources/foundry/object-views/add-application-sidebar-groups.png)
一旦您添加了 applications 和/或 actions 并发布您的更改,sidebar 将向用户显示。如果 sidebar 仅包含空的 group 或 groups,则不会显示。

Once you add applications and/or actions and publish your changes, the sidebar will be displayed to users. The sidebar will not be displayed if it only contains an empty group or groups.
## Edit the Applications Sidebar
applications sidebar 是模块化且可配置的。sidebar 可以拆分为多个 groups,每个 group 中包含不同的 application cards 和 actions。

The applications sidebar is modular and configurable. The sidebar can be split into groups with different application cards and actions in each group.
sidebar 中的每个 group 和 application card 都有专用的配置。如下图所示,选项包括:

The sidebar has a dedicated configuration for each group and application card in the sidebar. As numbered in the images below, options include:
1. 编辑整个 group,具有以下选项:

* (a) 配置 group 标题

* (b) 在 group 内重新排序 application cards 和 actions

* (c) 删除整个 group

* (d) 编辑可见性(使该 group 仅对特定 user profiles 可见)

1. Edit the entire group with the following options:
* (a) Configure the group title
* (b) Reorder application cards and actions within the group
* (c) Remove the entire group
* (d) Edit visibility (make the group visible to only specific user profiles)
2. 编辑特定的 application card,这将打开一个二级菜单,使您能够:

* (A) 添加或更改用于单个 card 的 application 资源(更多详细信息见下文)
* (B) 覆盖标题
* (C) 覆盖图标

* (D) 在 card 上使用 thumbnail;thumbnails 必须上传到 Foundry 并保存在文件夹中

* (E) 选择 Card mode 或 Compact mode

* (F) 添加 parameters

2. Edit a specific application card, which opens up a secondary menu enabling you to:
* (A) Add or change the application resource used for a single card (more details below)
* (B) Override the title
* (C) Override the icon
* (D) Use a thumbnail on the card; thumbnails must be uploaded to Foundry and saved in a folder
* (E) Select Card mode or Compact mode
* (F) Add parameters
3. 编辑 backing application(这将在源 app 中打开特定模块,例如 Workshop 或 Slate)

3. Edit the backing application (this will open the specific module in the source app, such as Workshop or Slate)
4. 向 group 添加新的 application

4. Add a new application to a group
5. 向 group 添加新的 action

5. Add a new action to a group
6. 添加新的 groups

6. Add new groups

> 📷 **[图片: Applications Sidebar Config]**

> 📷 **[图片: Applications Sidebar Config]**

## Add/change an application in the sidebar
有两种主要方式可以将 application 添加到侧边栏：

There are two main ways to add an application to the sidebar:
1. 对于对象 application（Workshop、Quiver、Slate 等）嵌入 Object View：

* 选择 **Add application**，选择一个 application（例如 Workshop）以打开 resource selector，然后选择您想要嵌入的特定 resource（例如 Workshop module）。

* Workshop 和 Slate application 的参数配置允许您将当前对象的 properties、linked objects set 或预定义值的详细信息传递到链接的 resource。

* 参数值在嵌入的 Workshop 或 Slate application 中以与参数名称同名的 variables 形式可访问。在 Workshop 中，这些必须在 variable **Settings** 面板中配置为 module interface variables。

1. For object applications (Workshop, Quiver, Slate, etc.) embedded an Object View:
* Select **Add application**, choose an application (e.g., Workshop) to open a resource selector, and select the specific resource (e.g., Workshop module) you would like to embed.
* The parameter configuration for Workshop and Slate applications allows you to pass details of the current object's properties, linked objects set, or predefined values into the linked resource.
* The parameter values are accessible within the embedded Workshop or Slate application as variables with the same name as the parameter name. In Workshop, these must be configured in the variable **Settings** panel as module interface variables.
2. 对于其他 Foundry applications 和外部网站，在新标签页中打开：

* 添加 **Application link** 以创建一个带有参数化 URL 的新卡片。

* 侧边栏上的所有链接都会在新的浏览器标签页中打开，而不会像上面提到的对象 application 那样被嵌入。

* 这些 URL 既可用于 Foundry applications（例如 Workshop、Vertex、另一个 Object View 或 Foundry documentation），也可用于外部网站。

* URL 卡片需要一个结合地址和/或参数配置中定义的任何参数的模板。要在 URL 中放置参数，请将参数名称包裹如下：`{{parameterName}}`。如果 property 是整个 URL，请选中 **Encode property value** 复选框以将其标记为整个 URL，并在 URL 文本框中仅包含 `{{parameterName}}`。

* 默认情况下，当前对象的详细信息可使用以下参数获取：`{{objectId}}` 和 `{{objectTypeId}}`。

2. For other Foundry applications and external websites to open in a new tab:
* Add an **Application link** to create a new card with a parameterized URL.
* All links on the sidebar are opened in a new browser tab and not embedded like object applications mentioned above.
* These URLs can be used both for Foundry applications (Workshop, Vertex, another Object View, or Foundry documentation, for example) and for external websites.
* The URL card requires a template that combines an address and/or any parameters defined on the parameter configuration. To place parameters in the URL, wrap the parameter name like this: `{{parameterName}}`. If the property is an entire URL, check the box for **Encode property value** to mark it as an entire URL, and include only the `{{parameterName}}` in the URL text box.
* By default, the details of the current object are available using these parameters: `{{objectId}}` & `{{objectTypeId}}`.
> **ℹ️ 注意**

> 如果用户没有嵌入 application 的权限，他们将无法打开该 application，但仍会看到 application 卡片。请确保您在侧边栏中为每个 application 设置了正确的权限。
> **ℹ️ 注意**

> If a user doesn’t have permissions to the embedded application, they would not be able to open it but would still see the application card. Make sure you set up the right permissions on each application in the sidebar.