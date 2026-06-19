<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/graphs-display-options/
---
# Object and edge display options
Vertex 允许您为图上的 object 和边配置动态样式。在设置样式并配置关键 property 的读数后，您可以使用时间选择窗口查看这些关键 property 随时间的变化。

Vertex allows you to configure dynamic styling for the objects and edges on your graph. After setting styling and configuring key property readouts, you can see how these key properties change over time by using the time selection windows.
## Graph layout
### Automatic layout options
您将在工作区顶部的工具栏中找到多个预定义的 layout 选项。一旦选择，object 和边将自动移动，使您可以在探索关系时对图进行排序。许多这些 layout 包含用于修改其行为的高级参数。可通过选择相应 layout 旁边的齿轮图标访问这些参数。

You will find a number of predefined layout options in the toolbar at the top of the workspace. Once selected, objects and edges will automatically move, allowing you to order the graph as you explore relations. Many of these layouts contain advanced parameters for modifying their behavior. These parameters can be accessed by selecting the gear icon next to the respective layout.
![The "Layout" dropdown containing layout options with a gear icon to the right.](/docs/resources/foundry/vertex/styling_layout_1.png)
以下是每个 layout 的高级参数。请注意，**Auto** 和 **Circular** layout 没有高级参数。

Below are the advanced parameters for each layout. Note that **Auto** and **Circular** layouts do not have advanced parameters.
#### Hierarchy (Left to Right/Top to Bottom)
* **Reverse：** 反转层次的顺序；左右变为右左，上下变为下上。

* **Root nodes：** 选择一个节点占据层次的根。如果选择 `Automatic`，将根据边的方向为您自动选择一个根节点。

* **Reverse:** Inverts the order of the hierarchy; left-right becomes right-left and top-bottom becomes bottom-top.
* **Root nodes:** Choose a node to occupy the root of the hierarchy. If `Automatic` is selected, a root node will be selected for you based on edge directions.
#### Grid
* **Staggered（交错排列）：** 提供偏移元素奇数行的选项。

* **Grid dimensions（网格尺寸）：** 指定对网格中行数或列数的约束。`Automatic` 模式将尝试使用相等数量的行和列。

* **Staggered:** Provides the option to offset odd rows of elements.
* **Grid dimensions:** Specify a constraint on the number of rows or columns in the grid. `Automatic` mode will attempt to use an equal number of rows and columns.
#### Horizontal Row/Vertical Column
* **Order by（排序依据）：** 用于对节点进行排序的 Object Property。
* 默认使用升序。

* 如果未选择 `Order by` property，则布局将保持行预先存在的水平节点顺序，或列的垂直节点顺序。

* 已分组的节点以及由不包含指定 property 的 objects 所支持的任何节点将在升序时放置在开头，在降序时放置在末尾。

* 只有 numeric properties 会出现在此选择列表中。

* 不同 objects 上匹配的 property 名称将一起排序。

* **Reverse（反转）：** 在升序和降序之间切换排序顺序。此选项仅在选择了 `Order by` property 时才会出现。

* **Order by:** An object property by which to sort nodes.
* Uses ascending order by default.
* If no `Order by` property is selected, the layout will maintain the pre-existing horizontal node order for rows, or vertical node order for columns.
* Grouped nodes and any nodes backed by objects that do not contain the specified property will be placed at the beginning when ascending and at the end when descending.
* Only numeric properties will appear in this select list.
* Matching property names on different objects will be sorted together.
* **Reverse:** Toggle the sort order between ascending and descending. This option will only appear if an `Order by` property is selected.
#### Radial
* **Central node（中心节点）：** 指定应出现在布局中心的节点。

* **Density（密度）：** 一到五（含）之间的值，用于确定节点之间的间距。

* **Central node:** Specify the node that should appear at the center of the layout.
* **Density:** A value between one and five (inclusive) that determines spacing between nodes.
#### Cluster
* **Cluster by（聚类依据）：** 指定节点应按其进行聚类的 property。

* 如果未选择 property，此布局将按 object type 进行聚类。

* 已分组的节点以及由不具有所选 property 的 objects 所支持的任何节点将被聚类在一起。

* 只有具有 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) `Selectable` 或 `Low Cardinality` 的 properties 才会出现在此下拉列表中。

* 不同 objects 的匹配 property 名称将被聚类在一起。

* **Cluster by:** Specify a property by which nodes should be clustered.
* If no property is selected, this layout will cluster by object type.
* Grouped nodes and any nodes backed by objects that do not have the selected property will be clustered together.
* Only properties that have the [render hints](/docs/foundry/object-link-types/metadata-render-hints/) `Selectable` or `Low Cardinality` will appear in this dropdown.
* Matching property names of different objects will be clustered together.
#### Cartesian
* **X/Y property（X/Y property）：** 用作布局中节点 x 和 y 坐标的 properties。
* 坐标将被归一化，以便节点在执行布局时适合视口范围。

* 除非选择了 x property、y property 或两者，否则不会执行 cartesian 布局。

* 已分组的节点以及由不具有所选 property 的 objects 所支持的任何节点将保持在其布局前的位置。

* 只有具有 [render hints](/docs/foundry/object-link-types/metadata-render-hints/) `Selectable` 或 `Low Cardinality` 的 properties 才会出现在此下拉列表中。

* 不同 objects 上匹配的 property 名称将一起排序。

* **X/Y reverse（X/Y 反转）：** 反转 x 和 y 坐标。reverse 切换控件仅在进行 property 选择后才会出现。

* **X/Y property:** Properties to use as the x and y coordinates of the nodes in the layout.
* Coordinates will be normalized so that nodes fit within the viewport when the layout is executed.
* The cartesian layout will not be executed unless an x property, y property, or both are selected.
* Grouped nodes and any nodes backed by objects that do not have the selected property will remain in their pre-layout locations.
* Only properties that have the [render hints](/docs/foundry/object-link-types/metadata-render-hints/) `Selectable` or `Low Cardinality` will appear in this dropdown.
* Matching property names on different objects will be sorted together.
* **X/Y reverse:** Invert x and y coordinates. The reverse toggle will only appear after a property selection is made.
### Group nodes by object type
随着您添加更多相关 objects，您可能希望开始将 objects 分组为图上的单个节点。选择要分组的 objects 后，使用 Workspace 顶部的 layout 工具栏对所选 objects 进行分组或取消分组。

As you add more related objects, you may want to begin grouping objects into a single node on the graph. Once you have selected the objects you wish to group, use the layout toolbar at the top of the Workspace to group or ungroup the selected objects.
一旦您将多个 objects 分组到一个节点中，您将在 workspace 左侧的选择面板中看到已分组的 objects 的完整列表。如果您只想取消分组节点中的一部分 objects，请使用选择面板选择这些 objects，然后选择 **Ungroup**，如下图所示。这也可以使用 histogram 中的 **Filter to** 功能来完成。

Once you have grouped a number of objects into a single node, you will see the full list of objects that have been grouped in the selection panel at the left of the workspace. If you only want to ungroup a subset of the objects in a node, use the selection panel to select those objects and choose **Ungroup** as seen below. This can also be done using the **Filter to** functionality in the histogram.
![styling\_group\_nodes\_1](/docs/resources/foundry/vertex/styling_group_nodes_1.jpg)
### Group by a property of the object type
使用 histogram，您可以浏览所选 objects 的 properties，并通过显示的值对 objects 进行分组。这将更改图上的 object 布局以反映新的分组。

Using the histogram, you can explore the properties of selected objects as well as group objects by the values displayed. This will change the object layout on your graph to reflect the new groupings.
![styling\_group\_by\_property](/docs/resources/foundry/vertex/styling_group_by_property.jpg)
### Group nodes into edge
某些 objects 是事务性的，会在系统中的其他节点/objects 之间移动。例如，Flight 作为事务性 object 在 `Departure Airport` 和 `Destination Airport` 之间移动。在这种情况下，您可以将 order objects 分组到 edge 上，并能够根据关键 properties/metrics 来设置 edge 的样式。

Some objects are transactional and move between other nodes/objects in your system. For example, a Flight moves between a `Departure Airport` and a `Destination Airport` as a transactional object. In this instance, you can group the order objects onto the edge, with the ability to style edges based on key properties/metrics.
选择 edge 并从右键菜单中选择 **Ungroup**，以显示先前在该 edge 中分组的所有 objects。或者，您也可以先使用 histogram 或选择面板选择要取消分组的 objects，从而取消分组的子集。

Select the edge and choose **Ungroup** from the right-click menu to show all objects previously grouped in the edge. Alternatively, you can ungroup a subset by first selecting objects to ungroup using the histogram or selection panel.
![styling\_group\_edge](/docs/resources/foundry/vertex/styling_group_edge.jpg)
> **ℹ️ 注意**

> 您可以在 Ontology Manager → Capabilities 选项卡中自动将事务性 objects 分组到相关的 edge 中。[详细了解 link merging。](/docs/foundry/vertex/link-merging/)
> **ℹ️ 注意**

> You can automatically group transactional objects into the related edge in the Ontology Manager → Capabilities tab. [Learn more about link merging.](/docs/foundry/vertex/link-merging/)
## Layer styling options
Layers 指的是相同 object type 的对象节点或节点之间的 edge 关系。可以使用多种 layout 选项单独配置这些，以允许灵活的可视化以及与系统的数字孪生进行直观的交互。

Layers refer to the object node(s) of the same object type or the edge relationships between nodes. These can be configured individually with a number of layout options to allow flexible visualization and intuitive interaction with the digital twin of your system.
使用左侧边栏中的 layer styling panel，您可以单独为节点和 edges 设置样式，或根据 object 的 properties 以及相关的时间序列/测量值设置样式。Layer styling 允许您可视化关键信息、计算 metrics，并通过参数化条件设置样式以显示当前或模拟的系统状态。

Using the layer styling panel in the left sidebar, you can style nodes and edges individually or style by properties of the object and related time series/measured values. Layer styling allows you to visualize key information, calculate metrics, and style by parameterized conditions to show current or simulated system state.
### Object styling
选择要配置的 object type 旁边的 **Styling Options**，以打开 styling 菜单。

Select **Styling Options** next to the object type you wish to configure to open the styling menu.
![styling\_object\_styling\_panel](/docs/resources/foundry/vertex/styling_object_styling_panel.jpg)
#### Color by
选择 **Fill Color** 下拉菜单，以选择设置样式所依据的参数以及此 layer 中所有 objects 的颜色选择。您可以选择时间序列度量作为 **Color by** 参数，这将根据所选时间窗口动态更新样式。您还可以使用 [derived property functions](/docs/foundry/vertex/derive-property-functions/) 为节点着色。

Select the **Fill Color** dropdown to choose the parameter by which to style as well as the color selection for all objects in this layer. You can select a time series measure as the **Color by** parameter, which will dynamically update the styling based on the selected time window. You can also color nodes using [derived property functions](/docs/foundry/vertex/derive-property-functions/).
![styling\_color\_by](/docs/resources/foundry/vertex/styling_color_by.jpg)
#### Subtitle
您可以为 object type 上的每个 object 或 object 的选定 property 添加副标题。副标题将在 graph 上同一类型的所有 object 上显示。

You can add subtitles to each object on the object type or a selected property of the object. Subtitles will display on all objects of the same type on the graph.
![styling\_subtitle](/docs/resources/foundry/vertex/styling_subtitle.jpg)
#### Extended labels
选择 **Extended Labels** 允许您向选定的 object 节点添加特定的读数。您可以从实时 time series 读数或模拟值中进行选择，以便在单个视图中比较当前条件和建模条件。

Selecting **Extended Labels** allows you to add specific readouts to the object nodes selected. You can select from real-world time series readings or simulated values to allow you to compare current and modeled conditions in a single view.
![styling\_extended\_labels\_1](/docs/resources/foundry/vertex/styling_extended_labels_1.jpg)
设置完 extended label 样式后，您可以从工作区左侧的 object 选择面板中选择要显示的 property 或 time series。

Once you have set the extended label styling, you can select the properties or time series to display from the object selection panel at the left of the workspace.
![styling\_extended\_labels\_1](/docs/resources/foundry/vertex/styling_extended_labels_1.jpg)
#### Badges
添加 badges 以指示链接到特定 object type 的事件数量。在下方截图中，您可以看到存在一个航班延误事件。

Add badges to indicate the number of linked events to a specific object type. In the screenshot below, you can see that there is one delayed flight event.
![styling\_badges](/docs/resources/foundry/vertex/styling_badges.jpg)
#### Node style
您可以选择将 object 显示为默认节点或完整的 object card。

You can choose to display objects as the default node or as a full object card.
![styling\_node\_type](/docs/resources/foundry/vertex/styling_node_type.jpg)
### Edge styling
edge 表示 object 之间的关系，可以对其进行样式设置以可视化系统或流程中节点之间的交互。

The edge represents the relationship between objects and can be styled to visualize the interactions between nodes in your system or process.
从您要配置的 edge 中选择 **Styling Options**。

Select the **Styling Options** from the edge you would like to configure.
![styling\_edge\_styling](/docs/resources/foundry/vertex/styling_edge_styling.jpg)
#### Line color
您可以根据 object type 或相关 object 的公共 property 来设置 edge 的颜色。

You can set the color of edges based on object types or a common property of related objects.
![styling\_line\_color](/docs/resources/foundry/vertex/styling_line_color.jpg)
#### Line type
您可以将绘制的线条格式设置为直线、曲线或正交线。

You can format the lines drawn to be straight, curved, or orthogonal.
![styling\_line\_type](/docs/resources/foundry/vertex/styling_line_type.jpg)
#### Labels
对于 edge 中分组的 object，您可以根据 object 的单个或聚合 property 配置标签，以显示关键 metrics。

Where there are objects grouped in the edges, you can configure labels based on individual or aggregated properties of the object to show key metrics.
![styling\_label](/docs/resources/foundry/vertex/styling_label.jpg)
#### Line width
您可以根据 object 的 property 为 edge 应用不同的宽度。应用不同的线宽可以让您指示 object（例如机场）之间事务（例如航班）的流动和数量。

You can apply a different width to the edges based on properties of the objects. Applying different line widths allows you to indicate the movement and volume of transactions (such as flights) between objects (such as airports).
![styling\_width](/docs/resources/foundry/vertex/styling_width.png)
#### Badges
与 object 节点一样，您可以添加 badges 以指示链接到特定 edge 关系的事件数量。在这里您可以看到存在一个航班延误事件。

As with the object nodes, you can add badges to indicate the number of linked events to a specific edge relation. Here you can see there is one delayed flight event.
![styling\_edge\_badges](/docs/resources/foundry/vertex/styling_edge_badges.jpg)
#### Ontology-level edge direction configuration
向 graph 添加 link 时，默认情况下，edge 箭头从 link 的右侧指向左侧。例如，对于在 Ontology 中配置为多对一 link type 的 link，箭头将从一端指向多端。可以使用以下 Ontology type classes 按 link type 进行配置：

When adding links to the graph, by default the edge arrows are shown from the right side of the link pointing to the left. For example, for a link configured in the Ontology as a many-to-one link type, the arrows will point from the one side to the many side. This can be configured per link type using the following Ontology type classes:
* Primary Direction: `kind`: `vertex`, `name`: `link_primary_direction`
* 当放置在 link 的一侧时，指示 edge 箭头应指向 link 此侧的 object。

* Undirectional: `kind`: `vertex`, `name`: `link_undirectional`
* 当放置在 link 的任一侧时，指示 edge 上不应显示任何箭头。

* Bidirectional: `kind`: `vertex`, `name`: `link_bidirectional`
* 当放置在 link 的任一侧时，指示 edge 的两侧都应显示箭头。

* Primary Direction: `kind`: `vertex`, `name`: `link_primary_direction`
* When placed on one side of a link, indicates that the edge arrow should point towards the object on this side of the link.
* Undirectional: `kind`: `vertex`, `name`: `link_undirectional`
* When placed on either side of a link, indicates that no arrows should be shown on an edge.
* Bidirectional: `kind`: `vertex`, `name`: `link_bidirectional`
* When placed on either side of a link, indicates that arrows should be shown on both sides of an edge.
Edge 箭头也可以使用 layer styling options 按 graph 进行隐藏或反转。

Edge arrows can also be hidden or reversed per-graph using the layer styling options.
![Edge direction styling options](/docs/resources/foundry/vertex/optional_ontology_config-edge-direction.jpg)
### Saved styles
配置完成后，您可以为同一个图保存不同的样式选项，以提供系统不同的视图。例如，您可以配置一个机场之间航班的视图，按航空公司的关键性能指标（Metric）进行样式设置。然后，您可以使用同一个图配合不同的样式来展示相同航线上的客户满意度。

Once configured, you can save different styling options for the same graph to provide different views of your system. For example, you could configure a view of flights between a set of airports to be styled by the key performance metrics of airline carriers. You can then use the same graph with different styling to show customer satisfaction over the same routes.
![styling\_saved\_styles](/docs/resources/foundry/vertex/styling_saved_styles.jpg)
## Saved selections
您也可以将图中选中的对象组保存为已保存的选择。为此，请选择任意数量的包含所需对象的节点和边，然后在右键菜单或工具栏的 **Selection** 菜单中选择 **Save objects in current selection**。

You can also save groups of objects that you have selected on the graph in a saved selection. To do this, select any number of nodes and edges that contain the desired objects and choose **Save objects in current selection** in the right-click menu or in the **Selection** menu in the toolbar.
![Save objects in current selection](/docs/resources/foundry/vertex/saved-selection-save-objects-in-selection.png)
每个已保存的选择都有一个关联的名称和颜色，该颜色显示在图层面板的 **Saved selections** 部分。图中的每个对象（表示为边或节点）周围都会以分色边框显示，颜色对应于该对象所属的已保存选择。每个对象可以根据需要属于任意数量的已保存选择，但边框只会显示前三个已保存选择的颜色。

Each saved selection has an associated name and color which appears in the **Saved selections** section of the layers panel. Each object on the graph, represented as either an edge or a node, will have a split border around it in the colors of the saved selections to which the object belongs. Each object can be part of as many saved selections as needed, but the border will only show the color of the first three saved selections.
![Saved selection in Layers panel](/docs/resources/foundry/vertex/saved-selection-layers-panel-and-borders.png)
要快速选择已保存选择中存储的所有对象，请在悬停于该已保存选择时选择快速选择操作。

To quickly select all the objects stored in a saved selection, choose the quick select action when hovering over the saved selection.
![Quick select for saved selection](/docs/resources/foundry/vertex/saved-selection-quick-select.png)
您可以在图层面板中编辑已保存的选择。要编辑已保存选择的名称，只需选中名称，输入新名称，然后按 Enter 键。要删除或编辑已保存选择的颜色，请在悬停于该已保存选择时选择 **...** 图标（

> 📷 **[图片: Three dots icon]**

）。您也可以使用眼睛图标（

> 📷 **[图片: Eye icon]**

）切换每个已保存选择的边框显示。

You can edit a saved selection in the layers panel. To edit the name of a saved selection, simply select the name, input a new name, and use the Enter key. To delete or edit the color of a saved selection, choose the **...** icon (

> 📷 **[图片: Three dots icon]**

) when hovering over the saved selection. You can also toggle borders on and off for each saved selection with the eye icon (

> 📷 **[图片: Eye icon]**

).
![More actions for saved selection](/docs/resources/foundry/vertex/saved-selection-more-actions.png)
您可以通过在图中选择对象，点击 **...** （

> 📷 **[图片: Three dots icon]**

）按钮，然后使用 **Add selected objects** 或 **Remove selected objects** 选项来编辑已保存选择中的对象。

The objects in a saved selection can be edited by choosing objects on the graph, selecting the **...** (

> 📷 **[图片: Three dots icon]**

) button, then using the **Add selected objects** or **Remove selected objects** options.
![Edit objects option for saved selection](/docs/resources/foundry/vertex/saved-selection-edit-objects.png)