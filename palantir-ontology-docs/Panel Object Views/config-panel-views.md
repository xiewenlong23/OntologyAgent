<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/config-panel-views/
---
# Configured panel Object View
有两种类型的已配置面板 Object View，可用于显示一个 object type 的一个或多个 object：[*object instance panels*](#object-instance-panels) 显示单个 object，而 [*object set panels*](#object-set-panels) 将多个 object 作为 object set 进行显示。两种类型的已配置 Object View 共享相同的 [edit entry points](/docs/foundry/object-views/config-overview/#edit-configured-object-views) 和配置体验。

There are two types of configured panel Object Views you can build to display one or multiple objects of an object type: [*object instance panels*](#object-instance-panels) display individual objects, while [*object set panels*](#object-set-panels) display multiple objects as an object set. Both types of configured Object Views share the same [edit entry points](/docs/foundry/object-views/config-overview/#edit-configured-object-views) and configuration experience.
## Object instance panels
默认的 object instance panel view 显示一个 [Property List widget](/docs/foundry/workshop/widgets-property-list/)，该 widget 显示 object type 单个 instance 的 [prominent properties](/docs/foundry/object-link-types/property-metadata/#metadata-reference)。

The default object instance panel view shows a single [Property List widget](/docs/foundry/workshop/widgets-property-list/) that displays [prominent properties](/docs/foundry/object-link-types/property-metadata/#metadata-reference) of a single instance of the object type.
## Object set panels
Object set panel 显示同一 object type 的多个 instance 的聚合视图。默认的 object set panel 提供一个选项卡式布局，其中包含两个 interfaces 用于探索 object 集合：

The object set panel displays an aggregated view of multiple instances of the same object type. The default object set panel provides a tabbed layout with two interfaces to explore object collections:
* **Charts** 选项卡最多显示五个 [XY Charts](/docs/foundry/workshop/widgets-chart/)，可视化按 property 值分组的 object 聚合。

* **List** 选项卡显示一个 [Object List widget](/docs/foundry/workshop/widgets-object-list/)，每个 object 最多显示三个 properties，包括 object 的 title、prominent properties 以及存在的媒体内容。

* The **Charts** tab displays up to five [XY Charts](/docs/foundry/workshop/widgets-chart/) that visualize object aggregations grouped by property values.
* The **List** tab shows an [Object List widget](/docs/foundry/workshop/widgets-object-list/) displaying up to three properties per object, including the object's title, prominent properties, and media when present.
## Edit configured panel Object Views
要修改任一类型的已配置面板 Object View，请使用其中一个 [edit entry points](/docs/foundry/object-views/config-overview/#edit-configured-object-views) 导航到已配置 Object View 编辑器。进入编辑器后，您可以像自定义 [Workshop module](/docs/foundry/workshop/overview/) 一样来自定义已配置面板 Object View 的内容。

To make changes to either type of configured panel Object View, use one of the [edit entry points](/docs/foundry/object-views/config-overview/#edit-configured-object-views) to navigate to the configured Object View editor. Once in the editor, you can customize the configured panel Object View's content as you would customize a [Workshop module](/docs/foundry/workshop/overview/).
如果您正在配置 object instance panel view 但希望切换到 object set，请先从顶部功能区中选择 **Object instance**，然后从下拉菜单中选择 **Object set**。您也可以使用同一菜单从 **Object set** *切换到* **Object instance**。

If you are configuring an object instance panel view but want to switch to an object set, select **Object instance** from the top ribbon before choosing **Object set** from the dropdown menu. You can use the same menu to switch *from* **Object set** *to* **Object instance**, as well.
![Panel object view type switching.](/docs/resources/foundry/object-views/panel-object-view-type-switching.png)
在左侧面板的设置部分，**Module Type** 部分允许您配置编辑画布的大小，以便更轻松地构建紧凑的模块。

In the settings section of the left-side panel, the **Module Type** section allows you to configure the size of the editing canvas to ease building a compact module.
* **Edit display size（编辑显示大小）：** 在下拉菜单中选择一个选项将调整面板在画布上的预览大小。面板的实际大小因设备和应用程序而异，因此这只是一个供构建者使用的工具，用于近似估算不同工作流中可用的空间。

* 显示选项包括匹配不同平台应用程序中面板大小的 **application presets（应用程序预设）**、常见的 **resolution presets（分辨率预设）**，以及以像素为单位对模块的高度和宽度进行 **manual entry（手动输入）**。

* **Show resolution picker in canvas（在画布中显示分辨率选择器）：** 启用后，分辨率选择器将显示在编辑器的左下角，允许构建者直接在画布上编辑模块的显示大小。

* **Fit to canvas（适应画布）：** 当分辨率大小超过画布大小时，分辨率选择器旁边会出现一个按钮，用于在完整查看整个面板和以标准缩放比例查看面板之间切换。

* **Edit display size:** Selecting an option in the dropdown will adjust the preview size of the panel on the canvas. The actual size of the panel will vary between devices and applications, so this is just a tool for builders to use to approximate the available space within different workflows.
* Display options include **application presets** that match the size of the panel in different platform applications, common **resolution presets**, and **manual entry** of the module's height and width in pixels.
* **Show resolution picker in canvas:** When enabled, a resolution picker will be shown in the bottom left corner of the editor, allowing builders to edit the display size of the module directly on the canvas.
* **Fit to canvas:** When the resolution size exceeds the canvas size, a button will appear next to the resolution picker that toggles between fitting the entire panel in view or viewing the panel at standard zoom.
![Panel object view configuration options.](/docs/resources/foundry/object-views/panel-object-view-configuration.gif)