<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/annotations/
---
# Annotations
使用 **annotations** 突出显示 map 上的特定区域并添加上下文信息。

Use **annotations** to highlight and add contextual information about specific areas on a map.
![Example annotations](/docs/resources/foundry/map/annotations-example.png)
## Create an annotation
通过在工具栏中选择 **Annotate** 并选择以下方法之一来创建 annotation：

Create an annotation by selecting **Annotate** in the toolbar and choosing one of the following methods:
* **Text:** 在特定位置添加文本。

* **Line:** 通过指定所有点来添加一条线。

* **Polygon:** 通过指定所有点来添加一个多边形。

* **Rectangle:** 通过指定两个角点来添加一个矩形 annotation。

* **Circle:** 通过指定圆心和半径来添加一个圆形 annotation。

* **Text:** Add text at a specific location.
* **Line:** Add a line by specifying all points.
* **Polygon:** Add a polygon by specifying all points.
* **Rectangle:** Add a rectangle annotation by specifying two corners.
* **Circle:** Add a circular annotation by specifying the center and a radius.
![Annotation menu](/docs/resources/foundry/map/annotations-create-menu.png)
选择希望创建的 annotation 类型后，[drawing tools](/docs/foundry/map/shapes/#draw-a-shape) 将会打开，并提供使用该特定绘制模式创建新 annotation 的说明。您的 map 将根据 annotation 的类型将其分组到不同的 layers 中。

After selecting the kind of annotation you wish to create, the [drawing tools](/docs/foundry/map/shapes/#draw-a-shape) will open and provide instructions on using that specific drawing mode to create a new annotation. Your map will group annotations into layers according to their types.
## Edit annotations
选择一个 annotation，然后使用 **Selection** 面板编辑其标题并添加任何注释。对于 text annotation，标题和注释将同时显示在 map 上以及悬停时显示的 tooltip 中。对于 polygon 和 line annotation，标题和注释仅在 tooltip 中显示。

Select an annotation, then use the **Selection** panel to edit its title and add any notes. For text annotations, the title and notes will appear on both the map and in the tooltip that appears on hover. For polygon and line annotations, the title and notes only appear in the tooltip.
使用 **Edit** 按钮调整 annotation 的位置。

Adjust the annotation's placement by using the **Edit** button.
![Edit annotation title](/docs/resources/foundry/map/annotations-modify.png)
## Annotation styling
您可以通过在 **Layers（图层）** 面板中编辑其样式来修改注释的外观。

You can modify the appearance of your annotations by editing their styling in the **Layers** panel.

> 📷 **[图片: Edit annotation styling.]**

> 📷 **[图片: Edit annotation styling.]**

注释样式选项包括：

Annotation styling options include:
* **Text（文本）**

* **Text color（文本颜色）：** 设置注释文本的颜色。

* **Text size（文本大小）：** 以像素为单位设置注释文本的大小。

* **Text value（文本值）：** 配置地图上显示的文本值是否包含注释的备注以及标题。

* **Text outline color（文本轮廓颜色）：** 设置文本背后轮廓的颜色。

* **Show location dot（显示位置点）：** 启用后，将显示一个圆形标记，指示添加注释的具体位置。

* **Show tooltips（显示工具提示）：** 启用后，当用户将鼠标悬停在注释上时，将出现包含注释标题和备注的工具提示。

* **Shapes（形状）**

* **Color（颜色）：** 设置多边形和线条的颜色。

* **Opacity（不透明度）：** 设置多边形和线条的不透明度。

* **Stroke width（描边宽度）：** 设置线条以及 **Fill polygons（填充多边形）** 禁用时多边形轮廓的宽度。

* **Stroke stroke（描边样式）：** 设置线条渲染时使用的虚线模式。

* **Measurements（测量值）：** 控制地图上显示的测量值。

* **Polygon measurements（多边形测量值）**

* **Perimeter（周长）：** 配置多边形周长的测量值显示方式。可选择不显示、显示每个周长段的长度，或显示整个周长的总长度。

* **Area（面积）：** 启用多边形总面积的显示。

* **Line measurements（线条测量值）**

* **Length（长度）：** 配置线条的测量值显示方式。可选择不显示、显示每个线段的长度，或显示整个线条的总长度。

* **Fill polygons（填充多边形）：** 启用后，多边形将以最小的描边渲染，其内部以指定颜色填充。禁用后，仅描出多边形的轮廓。

* **Show tooltips（显示工具提示）：** 启用后，当用户将鼠标悬停在注释上时，将出现包含注释标题和备注的工具提示。

* **Text**
* **Text color:** Sets the color of the annotation text.
* **Text size:** Sets the size of the annotation text in pixels.
* **Text value:** Configures whether the text value shown on the map includes the annotation's notes in addition to the title.
* **Text outline color:** Sets the color of an outline shown behind the text.
* **Show location dot:** When enabled, shows a circular marker indicating the specific location the annotation was added to.
* **Show tooltips:** When enabled, a tooltip containing the annotation's title and notes will appear when the user hovers over the annotation.
* **Shapes**
* **Color:** Sets the color of polygons and lines.
* **Opacity:** Sets the opacity of polygons and lines.
* **Stroke width:** Sets the width used for lines, and polygon outlines when **Fill polygons** is disabled.
* **Stroke stroke:** Sets the dash pattern used when rendering lines.
* **Measurements:** Controls the measurements that appear on the map.
* **Polygon measurements**
* **Perimeter:** Configure how measurements are displayed for polygon perimeters. Choose from no display, length displayed for each perimeter segment, or the total length of the entire perimeter.
* **Area:** Enable the display of the total area for polygons.
* **Line measurements**
* **Length:** Configure how measurements are displayed for lines. Choose from no display, length displayed for each line segment, or the total length for the entire line.
* **Fill polygons:** When enabled, polygons render with a minimal stroke and their interior filled with the specified color. When disabled, only the outline of the polygon is stroked.
* **Show tooltips:** When enabled, a tooltip containing the annotation's title and notes will appear when the user hovers over the annotation.