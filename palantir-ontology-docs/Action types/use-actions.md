<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/use-actions/
---
# Use actions in the platform
Action types 可以在 Foundry 的各应用间无缝集成。继续阅读以了解如何从 [Object Explorer](/docs/foundry/object-explorer/overview/) 和 [Workshop](/docs/foundry/workshop/overview/) 配置并应用 action。

Action types can be seamlessly integrated across applications in Foundry. Read on to learn how to configure and apply an action from [Object Explorer](/docs/foundry/object-explorer/overview/) and [Workshop](/docs/foundry/workshop/overview/).
在以下示例中，我们使用术语 **single action type** 来指代使用 object reference parameter 的 action type，使用 **bulk action type** 来指代使用 object reference list parameter 的 action。

In the examples below, we use the term **single action type** to refer to an action type using an object reference parameter, and **bulk action type** to refer to an action using an object reference list parameter.
## Object views
可以通过 **Actions section** 将 Action 添加到 [Object View](/docs/foundry/object-views/overview/) 中。

Actions can be added to an [Object View](/docs/foundry/object-views/overview/) using the **Actions section**.
![The Actions section of the Object View](/docs/resources/foundry/action-types/integrate_actions_object_explorer_object_view_actions_section.png)
在配置 **Actions section** 时，您可以选择：

When configuring the **Actions section** you have the option to:
* 将任何 action 作为按钮添加到此 section 中。

* 为每个按钮设置自己的 label 和 color。

* 将默认的 on-click 行为从打开表单更改为使用默认值立即应用该 action（如果有效）。
* 指定当不可见参数无效时，按钮是应隐藏还是应禁用（其思路是可见参数可以在打开表单时进行更正）。

* 为每个参数提供默认值；这可以是当前对象的 property value，也可以是"local" value（当前用户、当前时间戳、当前对象或手动输入的值）。
* 覆盖每个参数的可见性。

* Add any action as a button in the section.
* Give each button its own label and color.
* Change the default on-click behavior from opening the form to applying the action immediately using the default values (if valid).
* Specify whether the button should be hidden or disabled if a non-visible parameter is invalid (the idea being that visible parameters could be corrected upon opening the form).
* Provide a default value for each parameter; this can be a property value of the current object or a "local" value (current user, current timestamp, current object, or a manually entered value).
* Override the visibility of each parameter.
如上所示，您因此可以使用此 section 来提供同一通用 action 的多个结构化版本（"Delay 10 minutes"、"Delay 30 minutes" 等）。

As shown above, you can therefore use this section to offer multiple structured versions of the same generic action ("Delay 10 minutes", "Delay 30 minutes", etc.).
## Object Explorer
Action 将自动显示在 [Object Explorer](/docs/foundry/object-explorer/overview/) 中的三个位置：

Actions will automatically be shown in three places across [Object Explorer](/docs/foundry/object-explorer/overview/):
1. 在 Exploration View 右上角的 **Actions** 下拉菜单中。

1. From the **Actions** dropdown in the Exploration View (top right).
![The Actions dropdown in the Exploration View](/docs/resources/foundry/action-types/integrate_actions_object_explorer_exploration_view_actions_dropdown.png)
使用当前对象集，此下拉菜单会自动填充适用的 bulk action。

Using the current set of objects, this dropdown is automatically populated with applicable bulk actions.
2. 在 Object View 右上角的 **Object Actions** 下拉菜单中。

2. From the **Object Actions** dropdown menu in the Object View (top right).
![The Object Actions dropdown in the Object View](/docs/resources/foundry/action-types/integrate_actions_object_explorer_object_view_object_actions_dropdown.png)
使用当前对象，此下拉菜单会自动填充适用的 single 和 bulk action type。

Using the current object, this dropdown menu is automatically populated with applicable single and bulk action types.
3. 在 Object View 顶部的 **Linked objects view section** 中。

3. From the **Linked objects view section** in the Object View (top).
![The Linked objects view section in the Object View](/docs/resources/foundry/action-types/integrate_actions_object_explorer_object_view_linked_objects_view_section.png)
使用所选对象，此下拉菜单会自动填充适用的 single 和/或 bulk action type。

Using the selected object(s), this dropdown is automatically populated with applicable single and/or bulk action types.
> **ℹ️ 注意**

> 在 "bulk" 上下文中（在列表视图中显示多个对象的位置），仅会显示接受正确类型的 object list parameter 的 action。
> **ℹ️ 注意**

> In "bulk" contexts (where multiple objects are shown in a list view), only actions that accept object list parameters of the correct type will be shown.
## Workshop
在 [Workshop](/docs/foundry/workshop/overview/) 中，可以使用 [**Button group** widget](/docs/foundry/workshop/widgets-button-group/) 来配置和应用 Action。

In [Workshop](/docs/foundry/workshop/overview/), Actions can be configured and applied using the [**Button group** widget](/docs/foundry/workshop/widgets-button-group/).
![Button group widget in Workshop](/docs/resources/foundry/action-types/integrate_actions_workshop_button_group_widget.png)
此 widget 具有与 Object View 中的 [Actions section](#object-views) 相同的配置选项，但有一些值得注意的扩展：

This widget has the same configuration options as the [Actions section](#object-views) in an Object View, with a few notable extensions:
* 有三种可能的布局,均如上所示。
* 按钮具有其他显示选项,包括左/右图标、极简样式和标签样式。

* 除了 Action 之外,单个按钮还可以触发 Workshop event、URL 或 object set export。

* There are three possible layouts, all of which are shown above.
* The buttons have additional display options, including left/right icons, minimal styles, and tag styles.
* In addition to an Action, an individual button can trigger a Workshop event, URL, or object set export.
还有一个区别:

And one difference:
* 默认值可以是 [variable](/docs/foundry/workshop/concepts-variables/)、current user 或 current timestamp

* A default value can be a [variable](/docs/foundry/workshop/concepts-variables/), the current user, or the current timestamp
阅读有关 [Workshop 中的 Actions](/docs/foundry/workshop/actions-overview/) 的更多信息,或阅读 [Button Group widget](/docs/foundry/workshop/widgets-button-group/) 的完整参考文档以了解所有可用的配置选项。

Read more about [Actions in Workshop](/docs/foundry/workshop/actions-overview/), or read the full reference for the [Button Group widget](/docs/foundry/workshop/widgets-button-group/) to learn about all available configuration options.