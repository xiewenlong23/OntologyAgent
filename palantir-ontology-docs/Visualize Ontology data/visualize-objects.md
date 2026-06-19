<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/visualize-objects/
---
# Visualize Ontology data
地图的主要功能是支持对来自您 Ontology 的地理空间数据进行可视化和分析。一旦您 [将对象添加到地图](/docs/foundry/map/add-to-map/) 中，您可以配置样式以表示对象的各种 property。在较高层面上，一个 object layer 包含多个 display（例如，icon、line、polygon），它们在地图上表示这些对象。每个 display 都可以设置样式以表示对象的不同 property，例如颜色、大小和不透明度。

A map's primary capability is to enable visualization and analysis on geospatial data from your Ontology. Once you have [added objects to your map](/docs/foundry/map/add-to-map/), you can configure styling configuration to represent various properties of your objects. At a high level, an object layer contains multiple displays (for example, icons, lines, polygons) that represent the objects on the map. Each display can be styled to represent different properties of the objects, such as color, size, and opacity.
## Edit layer styling
要编辑 layer 的样式，请从 Layers 面板中选择一个 layer 条目。layer 详细信息面板将打开，并包含以选项卡形式呈现的多个部分：

To edit the style of a layer, select a layer entry from the Layers panel. The layer details panel will open with multiple sections as tabs:
* **Style：** 配置各个 display 的外观，或定义可应用于多个 display 的默认设置。

* **Legend：** 控制此 layer 的样式信息在 Legend 面板中的显示方式。

* **Style:** Configure the appearance of individual displays, or define default settings that can be applied to multiple displays.
* **Legend:** Control how the style information for this layer is displayed in the Legend panel.

> 📷 **[图片: Edit styling button.]**

> 📷 **[图片: Edit styling button.]**

> 📷 **[图片: Layer details panel showing Style and Legend tabs.]**

> 📷 **[图片: Layer details panel showing Style and Legend tabs.]**

## Layer style
**Style** 部分允许您配置适用于层中所有 [displays](#displays) 的 **Shared Defaults**。默认颜色和不透明度可以链接到特定的 [displays](#displays) 以共享一致的样式。有关如何配置颜色和不透明度的更多信息，请参阅 [Value based styling](#value-based-styling) 和 [Opacity styling](#opacity-styling) 部分。

The **Style** section allows you to configure **Shared Defaults** that apply to all [displays](#displays) in a layer. The default color and opacity can be linked to specific [displays](#displays) to share consistent styling. See the [Value based styling](#value-based-styling) and [Opacity styling](#opacity-styling) sections for more information on how to configure the color and opacity.
## Displays
一个对象层可以包含许多 **displays**，每个 display 都是一种在地图上或时间线中表示该层对象的不同方式。通过组合多个 displays，您可以创建复杂的可视化效果以同时表示多个属性，并在放大时提供更详细的视图。可用的各种 display 类型包括：

An object layer can contain many **displays**, each of which is a different way of representing the layer's objects on the map or in the timeline. By combining multiple displays, you can create complex visualizations to represent multiple properties at once and provide a more detailed view as you zoom in. The various display types available are:
* [**Icons and circles:**](/docs/foundry/map/visualize-points/) 根据 geopoint property 放置。

* [**Lines and polygons:**](/docs/foundry/map/visualize-polygons-lines/) 基于 geoshape property 或多个 geopoint properties。

* [**Track lines, breadcrumbs, and heatmaps:**](/docs/foundry/map/visualize-tracks/) 帮助可视化随时间移动的对象。

* [**Icons and circles:**](/docs/foundry/map/visualize-points/) Placed according to a geopoint property.
* [**Lines and polygons:**](/docs/foundry/map/visualize-polygons-lines/) Based on a geoshape property or multiple geopoint properties.
* [**Track lines, breadcrumbs, and heatmaps:**](/docs/foundry/map/visualize-tracks/) Helps visualize objects that move over time.
您可以使用 **Style** 部分下方的 **Add display** 选项添加新的 display。

You can add a new display using the **Add display** option below the **Style** section.
![Add display option.](/docs/resources/foundry/map/styling-add-display.png)
add display 菜单包含两个部分：

The add display menu has two sections:
* **Display presets:** 选择 object type 上可用于该层的 property，并将配置为使用该 property 的 display 添加到地图。

* **Available displays:** 从 Map 可以渲染的所有各种 display 类型中进行选择。只有那些可以完全针对该层 object type 进行配置的 displays 才会被启用。

* **Display presets:** Choose a property available on the object type for the layer, and add a display configured to use that property to the map.
* **Available displays:** Select from all the various display types that can be rendered by the Map. Only those displays which can be fully configured for the layer's object type are enabled.
每个 display 包含许多可自定义的属性，这些属性在每个 display 各自的页面中有详细介绍。大多数 display 上的属性遵循下一节中描述的 value-based styling 范式。

Each display contains many customizable attributes which are covered in detail on each display's respective page. Most attributes on displays follow the value-based styling paradigm described in the following section.
## Value-based styling
使用 **Value-based styling** 来控制由与对象关联的值所渲染的 display 的外观。例如，您可以配置图标的颜色以表示气象站的温度，或配置圆形的大小以表示公司的员工数量。使用 value-based styling 的最常见属性类型是颜色和数值属性（例如，line width、icon size、circle radius 等）。

Use **Value-based styling** to control the appearance of a display rendered for an object by a value associated with that object. For example, you can configure the color of an icon to represent the temperature of a weather station, or the size of a circle to represent the number of employees at a company. The most common types of attributes that use value-based styling are colors and numeric attributes (for example, line width, icon size, circle radius, etc.).
其思路是，对于正在渲染的每个对象，您指定一个 **value source**，它决定从每个正在渲染的对象中获取用于样式的值。然后，指定将值转换为 style attribute（例如，颜色、大小、不透明度）的某种方式。每个可样式化属性通常可用的 value sources 包括：

The idea is that for each object being rendered, you specify a **value source**, which determines the a value to use for styling from each object being rendered. Then, specify some way of converting a value into the style attribute (for example, color, size, opacity). The value sources typically available for each stylable attribute are:
* **Fixed:** 明确选择将统一应用于该层所有对象的单一 style value。

* **Property:** 根据对象上的 property 对每个对象进行样式设置。

* **Function:** 根据由 [function.](/docs/foundry/map/integrate-functions/) 计算的值对每个对象进行样式设置。

* **Measure:**  根据 [time series measure.](/docs/foundry/map/integrate-objects/#track-objects) 对每个对象进行样式设置。

* **Fixed:** Explicitly select a single style value that will be applied uniformly to all objects in the layer.
* **Property:** Style each object according to a property on the object.
* **Function:** Style each object according to a value computed by a [function.](/docs/foundry/map/integrate-functions/)
* **Measure:**  Style each object according to a [time series measure.](/docs/foundry/map/integrate-objects/#track-objects)
一旦选择了您希望使用的值，将其转换为 style value（颜色、line width、circle radius 等）的配置取决于您正在进行样式设置的属性类型。

Once you have selected the value you wish to use, the configuration for converting it into a style value (a color, line width, circle radius, and so on) depends on the type of attribute you are styling.
## Color styling
以下各节描述了适用于每种属性类型的颜色样式选项。

The following sections describe the color-styling options available for each type of attribute.
### Fixed
使用 fixed color style 时，使用颜色选择器选择将统一应用于该层所有对象的单一颜色。

When using a fixed color style, select a single color that will be applied uniformly to all objects in the layer, by using the color picker.
### Value-based
当根据具有数值的 function、property 或 time series 进行着色时，使用 gradient editor 将值映射到输出颜色。渐变中使用的颜色可以通过选择渐变条上的点来进行编辑。color gradient 的数值范围（min/max）会被自动推断，但可以将其关闭以手动设置范围。

When coloring by a function, property, or time series that has numeric values, use the gradient editor to map values to output colors. The colors used in the gradients can be edited by selecting points the gradient bar. The numerical range (min/max) for the color gradient is automatically inferred, but this can be toggled off to set the range manually.
![Gradient styling panel.](/docs/resources/foundry/map/styling-gradient-editor.png)
当根据具有字符串值的 function、property 或 time series 进行着色时，**Color mapping** 下拉菜单包含将值映射到颜色的方法：

When coloring by a function, property, or time series that has string values, the **Color mapping** dropdown menu contains methods for mapping values to colors:
* **Manual（手动）：** 为每个值显式指定要使用的颜色。

* **Automatic（自动）：** 从配色方案中自动分配颜色，以区分不同值，无需配置特定值。

* **None（无）：** 尝试将每个值直接应用为十六进制颜色。

* **Manual:** Explicitly specify colors to use per-value.
* **Automatic:** Assign colors from a color scheme automatically to differentiate between different values without having to configure specific values.
* **None:** Attempt to apply each value directly as a hex color.
## Numeric styling
以下各节描述了每种属性类型可用的数值样式选项。

The following sections describe the numeric-styling options available for each type of attribute.
### Fixed
使用固定数值样式时，可通过滑块指定数值，或在输入框中输入精确数值。

When using a fixed numeric style, specify the numeric value by using the slider or entering an exact number in the input field.
![Fixed numeric styling.](/docs/resources/foundry/map/styling-numeric-fixed.png)
### Value-based
在为数值属性（例如线宽或图标大小）设置样式时，只有具有数值的 Property 才能用作 Value Source。通过选择 **Numeric mapping（数值映射）** 选项来配置从所选 Value Source 到样式属性的映射：

When styling a numeric attribute (for example, line width or icon size), only properties that have numeric values can be used as a value source. Configure a mapping from your selected value source to the style attribute by selecting a **Numeric mapping** option:
* **Scaled（缩放）：** 定义线性 scale 以将对象的值转换为用于样式的数值。

![Scaled numeric styling.（数值缩放样式）](/docs/resources/foundry/map/styling-numeric-mapping.png)

* **Scaled:** Define a linear scale to convert a value from the object to the number used for styling.

![Scaled numeric styling.](/docs/resources/foundry/map/styling-numeric-mapping.png)

* 顶行控制样式属性的最小值和最大值，底行确定与这些最小/最大值相对应的对象值范围。

* 在此示例中，对于 "Departing Flights" Property 值为 `20` 的对象，线宽将为 `1` 像素；当 Property 值为 `500` 时，线宽则为 `10` 像素。

* **None（无）：** Property 的值将直接用作样式属性，不进行任何缩放或转换。

* The top row controls the minimum and maximum values for the styling attribute, while the bottom row determines the range of values that will correspond to those min/max values.
* In this example, the line width will be `1` pixel for an object that has a "Departing Flights" property value of `20`, and `10` pixels when the property value is `500`.
* **None:** The value of the property will be used directly as the style attribute, without any scaling or transformation.
## Opacity styling
使用 **Opacity（不透明度）** 部分来控制图层中对象的透明度。

Use the **Opacity** section to control the transparency for objects in the layer.
**Value from（值来源）** 下拉菜单包含可用来指定不透明度的各种方式：

The **Value from** dropdown menu contains the various ways in which you can specify opacity:
* **Fixed（固定）：** 选择应用于图层中所有对象的单一不透明度。

* **By time（按时间）：** 当渲染 [tracks（轨迹）](/docs/foundry/map/integrate-objects/#track-objects) 或 [events（事件）](/docs/foundry/map/integrate-objects/#event-objects) 对象时，根据全局 [time selection（时间选择）](/docs/foundry/map/time-overview/#selected-time-and-time-range) 控制其不透明度。

![Opacity by time options（按时间设置不透明度选项）](/docs/resources/foundry/map/styling-opacity-time.png)

* **Fixed:** Select a single opacity that uniformly applies to all objects in the layer.
* **By time:** When rendering [tracks](/docs/foundry/map/integrate-objects/#track-objects) or objects that are [events](/docs/foundry/map/integrate-objects/#event-objects), control their opacity based on the global [time selection](/docs/foundry/map/time-overview/#selected-time-and-time-range).

![Opacity by time options](/docs/resources/foundry/map/styling-opacity-time.png)

* **Active opacity（活动不透明度）：** 设置对象或点处于活动状态时的不透明度。

* **Inactive opacity（非活动不透明度）：** 设置对象或点未处于活动状态时的不透明度。

* **Active time buffer（活动时间缓冲）：** 设置事件或轨迹点的时间戳与当前时间光标的接近程度，以判定其是否处于活动状态。

* **Fade duration（淡出持续时间）：** 设置对象变为非活动状态后，其不透明度从活动不透明度淡出至非活动不透明度所需的时间段。

* **Hide until occurred（发生前隐藏）：** 启用后，在时间光标通过事件开始时间或轨迹点时间戳之前，对象将被完全隐藏。

* **Active opacity:** Sets the opacity when the object or point is considered active.
* **Inactive opacity:** Sets the opacity when the object or point is not considered active.
* **Active time buffer:** Sets how temporally close an event or track point's timestamp must be to the current time cursor for it to be considered active.
* **Fade duration:** Sets the time period over which an object's opacity fades from the active to inactive opacity, once it becomes inactive.
* **Hide until occurred:** If enabled, an object will be fully hidden until the time cursor has passed the start of the event or a track point's timestamp.
> **ℹ️ 注意**

> **Value from** 下拉菜单和 **By time** 不透明度选项仅在为 [tracks（轨迹）](/docs/foundry/map/integrate-objects/#track-objects) 或具有 [event data（事件数据）](/docs/foundry/map/integrate-objects/#event-objects) 的对象设置样式时才会出现。否则，不透明度部分将仅显示固定不透明度选项。
> **ℹ️ 注意**

> The **Value from** dropdown and **By time** opacity options will only appear when styling [tracks](/docs/foundry/map/integrate-objects/#track-objects) or objects with [event data](/docs/foundry/map/integrate-objects/#event-objects). Otherwise, the opacity section will only display the fixed opacity option.
### Labels
定义自定义标签以在地图上以文本形式展示重要信息。使用以下属性来控制每个 Display 中标签的显示方式：

Define custom labels to showcase important information as text on the map. Use the following attributes to control how labels appear for each display:
* **Visibility（可见性）：** 配置标签在地图上的显示时机。

* **Always visible（始终可见）：** 为父 Display 所表示的每个对象显示标签。

* **Only on hover（仅在悬停时显示）：** 当用户将光标悬停在一个或多个对象上时，以弹出框形式显示标签。

* **Hidden（隐藏）：** 不显示任何标签信息。

* **Style（样式）：** 对于始终可见的标签，使用以下选项控制标签内容的外观。

* **Card（卡片）：** 标签显示在实心背景上，以确保高对比度和可读性。

* **Minimal（极简）：** 标签内容仅以文本形式显示，外观更简洁、低干扰。

* **Enable Header（启用标题）：** 以粗体文本和更不透明的背景显示第一个标签行项，使关键信息一目了然。

* **Show Missing Data（显示缺失数据）：** 在标签中包含值为 null 或空的行条目。

* **Visibility:** Configure when labels are shown on the map.
* **Always visible:** Labels are shown for every object represented by the parent display.
* **Only on hover:** Labels are shown as a cursor pop-up when a user hovers over one or more objects.
* **Hidden:** No label information is shown.
* **Style:** For always-visible labels, control the appearance of the label content with the following options.
* **Card:** Labels are shown on a solid background to ensure high contrast and readability.
* **Minimal:** Label content is displayed only as text for a cleaner, less obtrusive appearance.
* **Enable Header:** Display the first label row item with bold text and a more opaque background, making key information immediately recognizable.
* **Show Missing Data:** Include row entries with null or empty values in the label.
![Labels example.](/docs/resources/foundry/map/styling-labels.png)
> **ℹ️ 注意**

> 请注意，使用 [tile-based loading methods（基于瓦片的加载方法）](/docs/foundry/map/objects-loading-methods/) 的 Layer 不支持标签和其他自定义 tooltip 内容。如果您需要标签或自定义 tooltip 内容，请确保使用 "Object" 加载方法。
> **ℹ️ 注意**

> Note that labels and additional tooltip contents are not supported for layers using [tile-based loading methods](/docs/foundry/map/objects-loading-methods/). If you need labels or custom tooltip contents, ensure you are using the "Object" loading method.
#### Label content for object layers
对于 object-backed Layer，标签可包含以下内容：

For object-backed layers, labels may contain the following:
* Properties（包括 [time-series properties](/docs/foundry/map/integrate-objects/#track-objects)）

* [Functions](/docs/foundry/map/integrate-functions/)
* [Series](/docs/foundry/time-series/time-series-overview/)
* Linked object counts
* Properties (including [time-series properties](/docs/foundry/map/integrate-objects/#track-objects))
* [Functions](/docs/foundry/map/integrate-functions/)
* [Series](/docs/foundry/time-series/time-series-overview/)
* Linked object counts
![Label content example for airport objects.](/docs/resources/foundry/map/styling-labels-content.png)
添加后，单个标签行还支持以下操作：

Once added, individual label rows also support the following operations:
* 拖动以重新排序
* 编辑显示名称
* 显示/隐藏行标题

* Drag to reorder
* Edit display name
* Show/hide row title
也可以从选择面板中使用 **…** 菜单添加 Properties 或 Series，该菜单在悬停在 property 或 series 上时出现，如下图所示。

Properties or series can also be added from the selection panel using the **…** menu that appears when hovering on a property or series, as pictured below.
![Add pinned property.](/docs/resources/foundry/map/styling-add-to-label.png)
## Display visibility by zoom level
使用 **Zoom levels** 部分来控制图层中对象的可见范围。插入符号表示您当前的缩放级别。

Use the **Zoom levels** section to control the visibility range of the objects in the layer. The caret symbol indicates your current zoom level.
当视口处于活动范围内的缩放级别时，相应的 display 将在地图上呈现。当超出该范围时，相应的 display 将被隐藏。

When the viewport is at a zoom level within the active range, the corresponding display will be rendered on the map. When outside the range, the corresponding display will be hidden.
缩放级别配置仅适用于已切换为 [visible](/docs/foundry/map/layer-management/#toggle-layer-visibility) 的图层。

The zoom level configuration only applies to layers that are toggled to be [visible](/docs/foundry/map/layer-management/#toggle-layer-visibility).
![Zoom levels.](/docs/resources/foundry/map/zoom-levels.png)
## Legend
在 **Layers** 详细信息面板中，使用 **Legend** 选项卡预览和控制图层的表示方式。图层 displays 中的样式信息默认包含在此选项卡中。标题开关决定此图层及其关联 displays 是否会出现在 **Legend** 面板中。切换行级别的复选框以隐藏或显示各个条目。

From the **Layers** details panel, use the **Legend** tab to preview and control how the layer will be represented. Style information from the layer's displays are included by default in this tab. The title switch determines whether this layer and its associated displays will appear in the **Legend** panel. Toggle the checkboxes at the row level to hide or show individual entries.

> 📷 **[图片: Legend configuration with options.]**

> 📷 **[图片: Legend configuration with options.]**

