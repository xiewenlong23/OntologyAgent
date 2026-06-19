<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-row-level-triggering-actions-and-events/
---
# Triggering actions and events on a row
Ontology actions 使您能够在 Ontology 中创建、修改和删除对象。Workshop events 使您能够触发弹出窗口、切换部分、切换选项卡、更新变量值等。在每一行上，您可以配置可由最终用户触发的 actions 和 events。

Ontology actions enable you to create, modify, and delete objects in the Ontology. Workshop events enable you to trigger pop-ups, toggle sections, switch tabs, update variable values, and more. On each row, you can configure actions and events that can be triggered by the end user.
可以通过以下方式触发 actions 和 events：

Actions and events can be triggered by:
* **行右键菜单**

* **"On row select" 事件**

* **Row right-click menus**
* **"On row select" events**

> 📷 **[图片: 右键菜单和行选择事件配置。]**

> 📷 **[图片: Right click menu and row select event configuration.]**

## Row right-click menu
行级别的右键菜单可以在 **Row Configuration > Right Click Menu** 下配置。菜单选项可以通过拖动菜单项来重新排序。可用的右键菜单选项将在以下部分中详细说明：

A row-level right-click menu can be configured under **Row Configuration > Right Click Menu**. Menu options can be reordered by dragging the menu item. The available right-click menu options are detailed in the following sections:
* [Action types](#action-types)
* [Workshop events](#workshop-events)
* [Action types](#action-types)
* [Workshop events](#workshop-events)
### Action types
Common uses:
* 编辑行对象上的 property；

* 在您右键单击 Gantt 图表中的时间点创建一个新对象。

* Edit a property on the row object;
* Create a new object at the point in time that you right-click in the Gantt chart.
1. 为此菜单选项提供一个自定义名称。

2. 选择任何 ontology action type 在点击时触发。这可以与 `resource object type` 相关，但不是必需的。

3. 使用 Workshop 变量或 Scheduling Gantt 图表特定变量预填 action type 的参数：

* **Resource object：** 自动填充您右键单击的行对象。

* **Selected start timestamp：** 自动填充您右键单击的行中该时间点的时间戳。在行的空白区域右键单击时非常有用。

1. Provide a custom name for this menu option.
2. Select any ontology action type to trigger on click. This can be related to the `resource object type` but is not required.
3. Prefill the parameters of your action type with Workshop variables or Scheduling Gantt chart-specific variables:
* **Resource object:** Auto-fills with the row object you right-click on.
* **Selected start timestamp:** Auto-fills with the timestamp of the point in the row you right-clicked. Useful when right-clicking in the whitespace of the row.
### Workshop events
Common uses:
* 触发一个弹出窗口，显示有关所选行的更多详细信息

* 打开另一个 Workshop application 或页面，其中所选行作为输入预填充。

* Trigger a popover with more details about the selected row
* Open a different Workshop application or page, with the selected row pre-populated as an input.
1. 为此菜单选项提供一个自定义名称。

2. 选择一个 Workshop event 在点击时触发。通常使用 Gantt 图表的 selection output variable 作为对所选行的引用。

1. Provide a custom name for this menu option.
2. Select a Workshop event to trigger on click. Often uses the Gantt chart's selection output variable as a reference to the selected row.

> 📷 **[图片: 行右键菜单示例。]**

> 📷 **[图片: Example of Row Right Click Menu.]**

## "On row select" event
"on row select" 事件可以在配置中右键菜单下方进行配置。当切换开启时，这些事件会在用户选择（单击）行 header 时触发。Events 可以是任何 Workshop event。

The "on row select" event can be configured below the right-click menu in the configuration. When toggled on, these events trigger when the user selects (clicks on) a row header. Events can be any Workshop event.