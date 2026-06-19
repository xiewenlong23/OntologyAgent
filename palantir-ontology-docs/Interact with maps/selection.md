<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/selection/
---
# Selection
Map 应用程序提供了多种选择 object 和标注的方法。

The Map application has a variety of methods for selecting objects and annotations.
## Select items on the map
* **选择项（Select items）：** 单击某个 object 或标注以选择它。如果光标下有多个项，则所有项都将被选中。

* **将项添加到现有选择（Add items to existing selection）：** 在单击时按住 Ctrl（Windows）或 Cmd（macOS），可将光标下的项添加到选择中。

* **选择矩形区域中的所有项（Select all items in a rectangular region）：** 在按住 Shift 的同时单击并拖动光标，以选择矩形区域中的所有项。

* **清除选择（Clear selection）：** 单击地图上的空白区域。

* **Select items:** Click on an object or annotation to select it. If there are multiple items under the cursor, all items will be selected.
* **Add items to existing selection:** Hold Ctrl (Windows) or Cmd (macOS) while clicking to add the items under the cursor to the selection.
* **Select all items in a rectangular region:** Hold Shift while clicking and dragging the cursor to select all items in a rectangular region.
* **Clear selection:** Click on an empty space on the map.
**Select** 工具栏菜单中提供了其他选择选项。这些选项包括：

Additional selection options are available in the **Select** toolbar menu. These are:
* **Select All（全选）：** 选择地图上的所有项目。

* 也可以通过 Ctrl+A (Windows) 或 Cmd+A (macOS) 键盘快捷键使用。

* **Select All of "Type"（选择所有"类型"）：** 选择与当前所选对象的 Object Type 匹配的所有项目。
* 仅当存在包含单一类型对象的现有选择时可用。

* **Invert Selection（反选）：** 将选择切换到当前未选择的所有项目。

* 也可以通过 Ctrl+I (Windows) 或 Cmd+I (macOS) 键盘快捷键使用。

* **Select intersecting objects（选择相交对象）：** 选择与所有当前所选项目相交的所有对象。
* 仅当存在现有选择时可用。

* **Select intersecting a shape...（选择与形状相交的对象...）：** 允许您绘制一个形状，并选择与之相交的所有对象。
* 仅当不存在现有选择时可用。

* **Select All:** Select all items on your map.
* Also available via the Ctrl+A (Windows) or Cmd+A (macOS) keyboard shortcut.
* **Select All of "Type":** Select all items matching the object type of the currently selected object.
* Only available when there is an existing selection that contains a single type of object.
* **Invert Selection:** Swap the selection to all items that are not currently selected.
* Also available via the Ctrl+I (Windows) or Cmd+I (macOS) keyboard shortcut.
* **Select intersecting objects:** Select all objects that intersect with all currently selected items.
* Only available when there is an existing selection.
* **Select intersecting a shape...:** Allows you to draw a shape and select all objects that intersect with it.
* Only available when there is no existing selection.
这些 Function 也可以在右键菜单中使用。

These functions are also available in the right-click menu.
| **Select** menu                                            | **Select** menu with existing selection                                                   | Right click menu for a shape                                                      |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| ![Toolbar select menu](/docs/resources/foundry/map/selection-toolbar-menu.png) | ![Toolbar select menu when items are selected](/docs/resources/foundry/map/selection-toolbar-menu-active.png) | ![Right click menu on shape](/docs/resources/foundry/map/selection-right-click-menu-intersecting.png) |
您可以使用 **Layer Actions（图层操作）** 菜单中的 **Select objects in layer（选择图层中的对象）** 菜单项来选择给定图层中的所有对象。

You can select all the objects in a given layer using the **Select objects in layer** menu item from the **Layer Actions** menu.

> 📷 **[图片: Layers panel with layer actions menu open]**

> 📷 **[图片: Layers panel with layer actions menu open]**

## Select items using the histogram
单击 **Histogram（直方图）** 面板中的某一行以选择所有匹配的对象。在选择第二行时按住 Shift 键可选择一个范围内的行。按住 Ctrl (Windows) 或 Cmd (macOS) 可将该行添加到现有选择中。您可以在 [直方图和筛选文档](/docs/foundry/map/histogram/) 中找到更多详细信息。

Click on a row within the **Histogram** panel to select all matching objects. Hold Shift while selecting a second row to select a range of rows. Holding Ctrl (Windows) or Cmd (macOS) will add the row to the existing selection. You can find more details in the [histogram and filtering documentation](/docs/foundry/map/histogram/).
![Map application with histogram row selected](/docs/resources/foundry/map/selection-histogram-row.png)
## Locking objects on the map
通过选择 "Objects（对象）" 部分下 **Layers（图层）** 面板中的 **…** 选项来锁定图层中的对象：

Lock the objects in a layer by selecting the **…** option, located in the **Layers** panel under the "Objects" section:

> 📷 **[图片: Lock objects in layer.]**

> 📷 **[图片: Lock objects in layer.]**

这将锁定图层中的对象，使其在地图上不可选择。仍然可以从左侧的 **Layers（图层）**、**Find（查找）** 和 **Histogram（直方图）** 面板中选择这些对象，但您无法使用光标、选择快捷键或相交形状在地图上与它们进行交互。您仍然可以通过 **…** 菜单按钮编辑图层的样式。

This will lock the objects of a layer so that they will not be selectable on the map. The objects can still be selected from the left **Layers**, **Find**, and **Histogram** Panel, but you cannot interact with them on the map with your cursor, selection shortcuts, or intersecting shapes. You can still edit the styling of a layer from the **…** menu button.
要解锁图层中的对象，请在 **Layers（图层）** 面板中选择图层旁边的锁图标，或通过 **…** 下拉菜单进行访问。

To unlock the objects in a layer, select the lock icon next to a layer in the **Layers** panel or access via the **…** dropdown menu.
## Selection Panel
如果选择了多个对象，则 **Selection（选择）** 面板将列出这些对象。通过此列表，您可以单击单个对象以将选择范围缩小到该对象。选择单个对象后，右侧的 **Selection（选择）** 面板将显示该对象的详细信息。

If there are multiple objects selected, the **Selection** panel will list these objects. From this list, you can click a single object to narrow down your selection to that object. With a single object selected, the **Selection** panel on the right will show the details of the object.

> 📷 **[图片: Selection panel showing a single object]**

> 📷 **[图片: Selection panel showing a single object]**

如果该对象有 Action Type，可以通过单击 ![hammer icon](/docs/resources/foundry/map/selection-hammer-icon.png) 图标来访问它们。其他操作（例如将地图居中到该对象、从地图中删除该对象以及在其他应用程序中打开该对象）可从 **...** 菜单中获得。

If the object has actions, these can be accessed by clicking the ![hammer icon](/docs/resources/foundry/map/selection-hammer-icon.png) icon. Additional actions such as centering the map on the object, deleting the object from the map, and opening the object in other applications are available from the **...** menu.
此面板有四个选项卡。

This panel has four tabs.
* **Properties（属性）** 选项卡将显示对象的属性。

* 您可以通过右键单击并选择 **Pin property（固定属性）** 来固定属性，这将使属性显示在顶部并允许您隐藏其他属性。

* 如果有任何可用的 [functions（Function）](/docs/foundry/map/integrate-functions/)，可以通过在右下角选择 ![plus icon](/docs/resources/foundry/map/selection-plus-icon.png) 来添加这些 Function。选择一个 Function 将把该 Function 返回的值添加到属性列表中。

* **Series（数据系列）** 选项卡将显示链接到该对象的任何数据系列。

* **Events（事件）** 选项卡将显示在当前所选时间窗口内链接到该对象的任何事件。

* **Object view（对象视图）** 选项卡将显示 [在 Ontology Manager 的 **Object Views（对象视图）** 选项卡中](/docs/foundry/object-views/overview/) 配置的对象视图。

* The **Properties** tab will show the properties of the object.
* You can pin properties by right-clicking and selecting **Pin property** which will cause the properties to be shown at the top and allow you to hide the other properties.
* If there are any [functions](/docs/foundry/map/integrate-functions/) available, these can be added by selecting ![plus icon](/docs/resources/foundry/map/selection-plus-icon.png) in the bottom right. Selecting a function will add the value returned by that function to the properties list.
* The **Series** tab will show any series linked to the object.
* The **Events** tab will show any events linked to the object in the currently selected time window.
* The **Object view** tab will show the object view configured [in the Ontology Manager's **Object Views** tab](/docs/foundry/object-views/overview/).
您可以在 Ontology Manager 的 **Capabilities** 选项卡中更改对象的默认选项卡。

You can change the default tab for an object in Ontology Manager's **Capabilities** tab.
![A section in Ontology Manager labeled "Default Object Selection Panel" and captioned "Sets the default panel to show in the object selection view" with the dropdown options of "Property list", "Series list", "Events list" and "Object view panel"](/docs/resources/foundry/map/oma-capabilities-default-selection-tab.png)
| Adding a function                                                                                                                              | Showing a function value                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
|

> 📷 **[图片: Selection panel with open functions menu]**

|

> 📷 **[图片: Selection panel containing a function]**

|
## Remove items from the map
要从地图中移除所选的对象和注释，请执行以下操作之一：

To remove selected objects and annotations from your map, do one of the following:
* 单击工具栏中的 **Delete**

* 在右键菜单中选择 **Delete selection** 选项

* 按键盘上的 Delete 键。

* Click **Delete** in the toolbar
* Select the **Delete selection** entry in the right-click menu
* Press the delete key on your keyboard.
将出现一个 toast 通知，确认已删除项目的数量，并提供 **Undo** 选项以撤销此操作。

A toast will appear confirming the number of items that were deleted, with an **Undo** option to revert this action.
要移除单个 Layer 中的所有对象，请使用 **Layer actions** 菜单中的 **Delete layer** 选项。

To remove all objects within a single layer, use the **Delete layer** item in the **Layer actions** menu.

> 📷 **[图片: Map application with layer actions menu open]**

> 📷 **[图片: Map application with layer actions menu open]**

