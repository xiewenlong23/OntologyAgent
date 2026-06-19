<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/shapes/
---
# Shapes
使用形状在地图上选择一个地理空间区域，以搜索对象、选择地图上已有的对象、执行操作或创建注释。

Use shapes to select a geospatial area on your map in which to search for objects, select objects already on your map, take actions, or create annotations.
## Create a shape
所有可用于形状的操作首先需要一个处于活动状态的形状。通过以下任一方式创建形状：

All operations available on shapes first require an active shape. Create a shape in one of the ways below:
* 使用[绘图工具](#draw-a-shape)自行构建形状。

* 使用当前选中的对象和注释来创建覆盖[与所选内容相同的地理空间区域](#from-selection)的形状。

* Construct a shape yourself using the [drawing tools](#draw-a-shape).
* Use the currently selected objects and annotations to create shapes that cover the [same geospatial area as your selection](#from-selection).
### Draw a shape
在工具栏中选择 **Drawing method** 选项之一，或按键盘上的 `D` 键在地图上手动绘制形状。

Choose one of the **Drawing method** options in the toolbar or press `D` on your keyboard to manually draw a shape on the map.
![Open drawing tools](/docs/resources/foundry/map/shapes-draw-button.png)
通过单击当前绘图模式打开下拉菜单，从各种可用模式中进行选择：

Select from the various modes available using the dropdown accessible by clicking on the current drawing mode:
![Select drawing mode](/docs/resources/foundry/map/shapes-draw-modes.png)
### From selection
您还可以从地图上的活动选择创建形状。右键单击任何选中的对象，并使用 **Create shape from selection** 菜单选项。

You can also create shapes from the active selection on the map. Right-click on any selected object and use the **Create shape from selection** menu entry.
![Create shape from selection](/docs/resources/foundry/map/shapes-from-selection.png)
## Modify a shape
您可以使用形状工具栏中的 **Modify** 按钮来编辑地图上处于活动状态的形状。

You can edit active shapes on your map by using the **Modify** button in the shapes toolbar.
![Modify button](/docs/resources/foundry/map/shapes-modify-button.png)
提供了多种修改工具：

There are a number of modification tools available:
![Modify toolbar](/docs/resources/foundry/map/shapes-modify-modes.png)
* **Edit points:** 允许拖动各个顶点以修改多边形、线或点。

* **Buffer:** 允许输入特定距离，以扩大或缩小形状的周长。

* **Translate:** 通过拖动来移动整个形状。

* **Replace:** 丢弃当前绘制的形状并打开绘图工具以绘制新形状。

* **Edit points:** Lets you drag individual vertices to modify polygons, lines, or points.
* **Buffer:** Allows entering a specific distance by which to grow or shrink the perimeter of shapes.
* **Translate:** Enables moving an entire shape by dragging it.
* **Replace:** Discards the currently drawn shape and opens the drawing tools to draw a new shape.
完成修改后，使用 **Done** 按钮返回 shapes toolbar。

Once finished applying modifications, use the **Done** button to return the shapes toolbar.
## Perform operations with an active shape
当 shape 处于激活状态时，使用 **Shapes** toolbar 执行各种操作：

With an active shape, use the **Shapes** toolbar to perform various operations:
![Shapes toolbar](/docs/resources/foundry/map/shapes-toolbar.png)
* **Select intersecting（选择相交对象）：** 选择地图上位于可见 layer 中且与当前 shape 相交的所有 object。

* **Search within（在范围内搜索）：** 打开 **Add objects** 面板，并将结果筛选为仅包含那些具有与当前 shape 相交的地理空间数据的 object。请注意，只能搜索具有 [`geohash` 或 `geoshape` property](/docs/foundry/map/integrate-objects/) 的 object。

* **Actions（操作）：** 显示所有可消费 shape 的 ontology action。有关配置地理空间操作的更多信息，请参阅 [Actions](/docs/foundry/map/actions/)。请注意，只有在 ontology 中配置了地理空间操作时，操作按钮才会出现。

* **Delete（删除）：** 从 map interface 中移除所选的 shape。

* **Select intersecting:** Selects every object on your map that is in a visible layer and that intersects the current shape.
* **Search within:** Opens the **Add objects** panel and filters the results to only include objects that have geospatial data that intersects the current shape. Note that only objects with [`geohash` or `geoshape` properties](/docs/foundry/map/integrate-objects/) can be searched.
* **Actions:** Shows every available ontology action that consumes shapes. Read more about configuring geospatial actions at [Actions](/docs/foundry/map/actions/). Note that the actions button will only appear if geospatial actions have been configured in the ontology.
* **Delete:** Removes the selected shapes from the map interface.