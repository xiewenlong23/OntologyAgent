<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/layer-management/
---
# Layer management
您 map 上的所有数据都分组到不同的 [layers 类型](/docs/foundry/map/core-concepts/)，这些类型可以在 **Layers** 面板中进行管理。

All data on your map is grouped into different [types of layers](/docs/foundry/map/core-concepts/), which can be managed in the **Layers** panel.
## Toggle layer visibility
通过使用可见性切换按钮来显示或隐藏 layer 的内容：

Show or hide the contents of a layer by using the visibility toggle:

> 📷 **[图片: Hide layer button]**

> 📷 **[图片: Hide layer button]**

## Rename layers
通过单击当前名称来编辑 layer 的名称。

Edit a layer's name by clicking on the current name.

> 📷 **[图片: Edit layer name]**

> 📷 **[图片: Edit layer name]**

## Reorder layers
通过拖动 layer 的图标来更改 layer 的顺序。重新排序 layer 可能会改变您 map 的渲染效果，因为在列表中位置较高的 layer 会渲染在位置较低的 layer 之上。

Change the order of layers by dragging the layer's icon. Reordering layers can alter the rendering of your map, as layers that appear higher in the list of layers render on top of layers that appear lower in the list.
![Layer ordering and rendering with weather layer on top of snotel layer](/docs/resources/foundry/map/layer-management-ordering-weather-first.png)
![Layer ordering and rendering with snotel layer on top of weather layer](/docs/resources/foundry/map/layer-management-ordering-snotel-first.png)
## Move objects to new or existing layers
Object 可以分散到多个 layer 中，前提是这些内容都属于同一 object type。将选中的一组 object 移动到新 layer 之后，每组中的 object 可以设置不同的样式，如下图所示。

Objects can be spread into multiple layers, as long as the contents are all of the same object type. After moving a selected set into a new layer, the objects in each set can be styled differently, as demonstrated in the images below.
![Creating a new layer with selected set of weather station objects](/docs/resources/foundry/map/layer-management-move-to-new-layer.png)
![Moving weather station objects to an existing layer](/docs/resources/foundry/map/layer-management-move-to-layer.png)