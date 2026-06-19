<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/config-legacy-object-views/
---
# Configure legacy Object Views
> **ℹ️ 注意**

> 要访问旧版 Object View 配置，请导航到 object type 的 Object View editor，选择 **Manage tabs** 齿轮图标，然后将鼠标悬停在选项卡上以选择 **Open in legacy editor** 图标。
> **ℹ️ 注意**

> To access legacy Object View configuration, navigate to the Object View editor for an object type, select the **Manage tabs** cog icon, and hover over a tab to select the **Open in legacy editor** icon.
## Configure tabs
基于旧版 widget 的标签页显示按 sections 组织的 widgets 列表。您可以在标签页设置中添加、删除和重新排序 widgets，或导航到其他设置。

A legacy widget-based tab displays a list of widgets organized into sections. You can add, delete, and re-order widgets or navigate to other settings from within the tab settings.
![Configure legacy widget-based tabs in Object View.](/docs/resources/foundry/object-views/configure-widgets.png)
## Configure widgets
旧版 Object View 标签页的构建块称为 **widgets**。Widgets 有时被称为 *Sections* 或 *Plugins*。Widgets 是在 Object View 上显示某种数据的主要方式。使用它们可以将数据可视化为 KPI 或图表，布置整个 Object View 的布局，以及操作显示的数据。

The building blocks of legacy Object View tabs are called **widgets**. Widgets are sometimes referred to as *Sections* or *Plugins*. Widgets are the primary way to display some form of data on an Object View. Use them to visualize data as KPIs or charts, arrange the layout of an entire Object View, and manipulate displayed data.
Object View 中有几种可用的 widget 类型：

There are a several widget types available in Object View:
* [Properties 和 links](/docs/foundry/object-views/widgets-properties-links/)

* [Visualize](/docs/foundry/object-views/widgets-visualization/)
* [Filters](/docs/foundry/object-views/widgets-filtering/)
* [Layout](/docs/foundry/object-views/widgets-layout/)
* [嵌入其他 applications 和文件](/docs/foundry/object-views/widgets-apps-files/)

* [Properties and links](/docs/foundry/object-views/widgets-properties-links/)
* [Visualize](/docs/foundry/object-views/widgets-visualization/)
* [Filters](/docs/foundry/object-views/widgets-filtering/)
* [Layout](/docs/foundry/object-views/widgets-layout/)
* [Embed other applications and files](/docs/foundry/object-views/widgets-apps-files/)
## Widget-specific settings
Widgets 用于可视化或操作与对象相关的数据。

Widgets 通常访问以下内容之一：

Widgets are used to visualize or manipulate data related to an object.
Widgets typically access one of the following:
* 当前对象的 properties

* 链接到当前对象的 objects

* 链接到当前对象的 objects 的 properties 上的 aggregations

* Properties of the current object
* Objects linked to the current object
* Aggregations on properties of objects linked to the current object
当您在 Object View 上配置 widget 时，确定要可视化哪个 object 以及什么 property。您必须预先在 Ontology metadata 中设置相关的 objects 并定义 links。

When you configure a widget on an Object View, determine which object and what property you want to visualize. You must set up the relevant objects and define links in advance within the Ontology metadata.
每个 widget 的具体设置对于其提供的功能是唯一的。一般来说，widget 特定配置有两个主要组成部分：

The specific settings for each widget are unique to the functionality it provides. In general, there are two major components to widget-specific configuration:
* **object model** 配置需要选择 object 或 linked object 以及应使用哪些 properties。例如，在配置图表时，您可能需要按 Destination 聚合 Airport 中的所有 Flights。

* **visual** 配置需要选择图表类型、颜色、格式、文本标签等选项。

* The **object model** configuration requires selecting the object or linked object and which properties should be used. For example, when configuring a chart, you may need to aggregate all Flights in an Airport per Destination.
* The **visual** configuration requires selecting options such as chart types, colors, formats, text labels, etc.
## Widget format settings
所有 widget 都具有默认的格式设置：

All widgets have default format settings:
**General**
* **Title（标题）：** 在 widget 头部添加要显示的标题。默认情况下,这是 widget 名称加一个空格的组合。您必须为 widget 添加标题才能保存它。

* **Icon（图标）：** 选择一个图标,显示在 widget 头部的左上角。每个 widget 都有一个默认图标。

* **Help Info（帮助信息）：** 默认为空,您可以添加文本以向用户说明该 widget。

* **Title:** Add a title to display in the widget header. By default, this is either the widget name an empty space. You must add a title to the widget to save it.
* **Icon:** Choose an icon to display in the top left of the widget header. Each widget has a default icon.
* **Help Info:** Empty by default, you can add text to explain the widget to users.
![Edit general format settings in Object View](/docs/resources/foundry/object-views/widget-general-format-settings.png)
**Layout**
* **Alignment（对齐方式）：** 您可以选择 widget 是占据 Object View 的整个宽度,还是采用右对齐或左对齐以并排放置两个 widget。默认情况下,对齐方式设置为全宽。

* **Sizing（尺寸）：** 并非所有 widget 都存在尺寸设置。当该设置可用时,您可以控制 Object View 内该 section 的最小和最大高度。

* **Alignment:** You can choose whether a widget should be the full width of the Object View or have a right or left alignment to place two widgets side-by-side. Alignment is set to full width by default.
* **Sizing:** The sizing setting does not exist on all widgets. When it is available, you can control the minimum and maximum height of the section within the Object View.
## Reuse widget configurations
您可以通过复制 YAML 配置来复用先前创建的 widget 的配置。在 Object View 编辑屏幕的右上角选择代码图标以访问配置。然后,将该配置复制并粘贴到新 widget 的 YAML 配置中。

You can reuse the configuration of a previously created widget by copying the YAML configuration. Access the configuration by selecting the code icon in the upper right corner of the Object View editing screen. Then, copy and paste the configuration into the YAML configuration of a new widget.
![Open the YAML configuration to reuse widget configurations](/docs/resources/foundry/object-views/access-yaml-config.png)