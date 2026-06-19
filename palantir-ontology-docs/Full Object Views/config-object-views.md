<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/config-object-views/
---
# Configured full Object View
## Edit configured full Object Views
为所有 Object Type 配置的默认完整 Object View 显示一个 [Property List widget](/docs/foundry/workshop/widgets-property-list/)，展示该 Object Type 的主要 Property，以及一个 [Links widget](/docs/foundry/workshop/widgets-links/)，展示该 Object 的 Link（如果存在）。要修改配置的完整 Object View，请使用 [edit entry points](/docs/foundry/object-views/config-overview/#edit-configured-object-views) 之一导航到配置的 Object View 编辑器。进入编辑器后，可以像配置常规 Workshop 模块一样配置完整 Object View 每个选项卡的内容。

The default configured full Object View for all object types shows a single [Property List widget](/docs/foundry/workshop/widgets-property-list/) displaying prominent properties of the object type, and a [Links widget](/docs/foundry/workshop/widgets-links/) that displays the object's links, if any exist. To make changes to the configured full Object View, use one of the [edit entry points](/docs/foundry/object-views/config-overview/#edit-configured-object-views) to navigate to the configured Object View editor. Once in the editor, the content of each tab of a configured full Object View can be configured just like a regular Workshop module.
### Edit Object View tabs
完整 Object View 有两个可编辑的部分：选项卡和选项卡内容。每个 Object View 选项卡都由一个 Workshop 模块支持，这使您能够使用 [Workshop](/docs/foundry/workshop/overview/) 创建具有高级功能和特性的 Object View 内容。您可以使用 Workshop 选项卡来：

There are two parts of a full Object View that can be edited: the tabs and the tab content. Each Object View tab is backed by a Workshop module, which enables you to use [Workshop](/docs/foundry/workshop/overview/) to create Object View content with advanced capabilities and features. You can use Workshop tabs to:
* 完全灵活地控制 [layout](/docs/foundry/workshop/concepts-layouts/)

* 使用 Workshop [variables](/docs/foundry/workshop/concepts-variables/) 灵活且动态地加载信息

* 使用 [Scenarios](/docs/foundry/workshop/scenarios-overview/) 显示模拟或 Model-backed 的结果

* Have full flexibility over the [layout](/docs/foundry/workshop/concepts-layouts/)
* Flexibly and dynamically load information using Workshop [variables](/docs/foundry/workshop/concepts-variables/)
* Display simulations or model-backed results using [Scenarios](/docs/foundry/workshop/scenarios-overview/)
### Use the Object View editor
Object View 编辑器内有三个主要部分：**header（页眉）**、**object title bar（对象标题栏）** 和 **Workshop module（Workshop 模块）**。

There are three main sections within the Object View editor: the **header**, the **object title bar**, and the **Workshop module**.
header 中的面包屑导航显示 Ontology 名称、Object Type 和 form factor。form factor 是一个下拉菜单，可用于在编辑完整和面板 Object View 之间进行切换。在此下方，显示 Object View 和当前 workshop module 的版本号。在右侧，您可以选择不同的 Object 进行预览、保存和发布编辑内容，以及在 Object Explorer 中打开该 Object。

The breadcrumbs in the header display the Ontology name, object type, and form factor. The form factor is a dropdown that can be used to switch between editing the full and panel Object View. Below this, version numbers are displayed for the Object View and the current workshop module. On the right, you can select different objects to preview, save and publish your edits, and open the object in Object Explorer.
![The Object View header diagram.](/docs/resources/foundry/object-views/object-view-header-diagram.png)
在 object title bar 中，您可以通过选择齿轮图标来管理选项卡。每个选项卡对应一个 workshop module。如果仅配置了一个选项卡，则在查看 Object View 时该选项卡标题将被隐藏，即使它在编辑模式下显示。

In the object title bar, you can manage tabs by selecting the gear icon. Each tab corresponds to a single workshop module. If only one tab is configured, the tab title will be hidden when viewing the Object View, even though it appears in edit mode.
选择齿轮图标会打开一个对话框，允许您添加、重新排序、重命名和删除 Object View 选项卡。删除选项卡也会删除该选项卡所包含的 Workshop module。

Selecting the gear icon opens a dialog that allows you to add, reorder, rename, and delete Object View tabs. Deleting a tab also deletes the Workshop module that the tab contains.
此对话框还允许您配置选项卡的 [visibility settings](/docs/foundry/object-views/config-tabs/#tab-visibility)，或在您需要编辑其他 [legacy configuration options](/docs/foundry/object-views/config-legacy-object-views/) 时访问旧版 Object View 编辑器。

This dialog also allows you to configure a tab's [visibility settings](/docs/foundry/object-views/config-tabs/#tab-visibility), or access the legacy Object View editor if you need to edit other [legacy configuration options](/docs/foundry/object-views/config-legacy-object-views/).
![The "Manage tabs" dialog.](/docs/resources/foundry/object-views/manage-tabs.gif)
选项卡的内容可以像常规 Workshop 模块一样进行编辑。编辑完成后，**Save and publish** 按钮将保存并发布选项卡编辑以及当前模块的编辑，[除非已禁用 automatic publishing](/docs/foundry/object-views/manage-versions/#save-new-versions)。

The content of the tab can be edited just like a regular Workshop module. Once edits are complete, the **Save and publish** button will save and publish both tab edits and edits to the current module, [unless automatic publishing is disabled](/docs/foundry/object-views/manage-versions/#save-new-versions).