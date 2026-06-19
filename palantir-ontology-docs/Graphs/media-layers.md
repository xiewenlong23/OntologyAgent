<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/media-layers/
---
# Media layers and image annotations
Vertex 中的 media layers（媒体图层）允许您在地图或图像上可视化和标注对象，从而实现空间分析和对数据的上下文理解。您可以添加对象作为叠加层，根据 properties（属性）进行过滤，并创建交互式标注。

Media layers in Vertex allow you to visualize and annotate objects on maps or images, enabling spatial analysis and contextual understanding of your data. You can add objects as overlays, filter them based on properties, and create interactive annotations.
本部分文档使用 [来自 Wikimedia Commons 的公共领域图像 ↗](https://commons.wikimedia.org/wiki/File:%22B%22_Deck_and_%22C%22_Deck_Plans_-_General_Edwin_D._Patrick,_Suisun_Bay_Reserve_Fleet,_Benicia,_Solano_County,_CA_HAER_CA-344_\(sheet_6_of_8\).png) 作为示例，通过在 Vertex 中叠加对象的示意图来概念化构建一艘二战时期的海军舰艇。

This section of documentation uses [public domain images from Wikimedia Commons ↗](https://commons.wikimedia.org/wiki/File:%22B%22_Deck_and_%22C%22_Deck_Plans_-_General_Edwin_D._Patrick,_Suisun_Bay_Reserve_Fleet,_Benicia,_Solano_County,_CA_HAER_CA-344_\(sheet_6_of_8\).png) as an example to notionally construct a World War II-era naval ship via schematics overlaid with objects in Vertex.
在本示例结束时，我们将在 Vertex 中拥有一个交互式舰艇图，其中包含一些叠加在图像上的房间标注。

By the end of this example we will have an interactive ship diagram in Vertex with annotations that show a few of the rooms overlaid on the image.
![The end result of a Vertex graph example with a media reference and image annotations.](/docs/resources/foundry/vertex/media-layers-end-result.png)
## Configuration
### Pipeline Builder configuration
要开始使用 Vertex 中的 media（媒体），请确保您至少有一个具有 [media reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) 的 object type。在我们的示例中，我们使用了一个由图像 media set 创建的 object type。我们还有两个 object type，将用于在 Vertex 图形中创建标注。

To get started using media in Vertex, ensure you have at least one object type with a [media reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references). For our example, we are using one object type created from a media set of images. We also have two object types that we will use to create annotations in our Vertex graph.
在下面的 Pipeline Builder 图形中，`Wikipedia commons...` media set 输出 `[Ships] Ship diagram` object type。`Text - Ship annotations` dataset 输出 `[Ship] Text Annotations` object type。最后，`Ship annotations` dataset 输出 `[Ships] Annotation` object type。

In the Pipeline Builder graph below, the `Wikipedia commons...` media set outputs the `[Ships] Ship diagram` object type. The `Text - Ship annotations` dataset outputs the `[Ship] Text Annotations` object type. Finally, the `Ship annotations` dataset outputs the `[Ships] Annotation` object type.
![A Pipeline Builder graph displaying the data and media sets that output object types.](/docs/resources/foundry/vertex/media-layers-ontology-overview.png)
选中后，您可以在预览面板中查看构成 `Wikipedia commons...` media set 的各个 PNG 图像。

When selected, you can view the individual PNG images that make up the `Wikipedia commons...` media set in the preview panel.
![The preview of the PNG images in the example media set.](/docs/resources/foundry/vertex/media-layers-media-example-data.png)
选择 `[Ships] Ship diagram` object type 会显示图像 media references 和 RIDs 的预览。

Selecting the `[Ships] Ship diagram` object type reveals a preview of the image media references and RIDs.
![The preview of the media set with the image media references and RIDs.](/docs/resources/foundry/vertex/media-layers-diagram-example-data.png)
通过双击同一节点，我们可以查看从源 dataset 的列派生的 `[Ships] Ship diagram` object type 的 properties（属性）。

By double-clicking the same node, we can view the properties of the `[Ships] Ship diagram` object type that are derived from the columns of the source dataset.
![The properties of the Ship diagram object type, viewed in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-diagram-properties.png)
我们可以选择 `[Ships] Annotation` object type 来查看源 dataset 的预览，其中包含 `annotation`、`coordinates` 和 `hexcolor` 列。

We can select the `[Ships] Annotation` object type to view a preview of the source dataset, which includes `annotation`, `coordinates`, and `hexcolor` columns.
![The preview of the annotation dataset.](/docs/resources/foundry/vertex/media-layers-annotation-example-data.png)
双击同一节点将显示从源数据集列派生的 `[Ships] Annotation` object type 的 properties。

Double-clicking the same node will display the properties of the `[Ships] Annotation` object type that are derived from the columns of the source dataset.
![The properties of the annotation object type, viewed in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-ship-annotation-properties.png)
我们使用 `File Name` [foreign key property](/docs/foundry/object-link-types/create-link-type/#foreign-key-relationship-type) 将 `Annotation` 和 `Text annotation` object types 链接到它们相关的 `Ship diagram` object types。

We linked the `Annotation` and `Text annotation` object types to their related `Ship diagram` object types with the `File Name` [foreign key property](/docs/foundry/object-link-types/create-link-type/#foreign-key-relationship-type).
![The link type foreign key configuration in Pipeline Builder.](/docs/resources/foundry/vertex/media-layers-link-key.png)
现在我们了解了基于媒体的 object type 和 annotation object types 之间的关系，我们可以继续在 Ontology Manager 中进行配置，以设置这些 object types 在 Vertex graph 中使用时的默认行为。

Now that we understand the relationship between our media-based object type and annotation object types, we can continue configurations in Ontology Manager to set default behaviors for our object types when used in a Vertex graph.
### Ontology Manager configuration
在 Ontology Manager 中导航到您基于媒体的 object type。从 **Capabilities** 选项卡中，选择要用作媒体层中默认 image 的 image reference。从 **Image reference property** 下拉菜单中选择一个选项。

Navigate to your media-based object type in Ontology Manager. From the **Capabilities** tab, choose which image reference to use as the default image in a media layer. Select an option from the **Image reference property** dropdown menu.
![The media reference configuration for the Ship object type in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-config-ship-diagram.png)
现在我们可以配置 `Annotation` object type 来定义其在 Vertex 中使用时的行为。

Now we can configure the `Annotation` object type to define its behavior when used in Vertex.
![The Annotation object type overview page in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-oma-annotation.png)
从概览页面中，我们可以查看我们创建的两个用于 `Annotation` object type 的 [action types](/docs/foundry/action-types/overview/)：`Create [Ships] Annotation` 和 `Edit annotation coordinates`。我们可以在 Vertex graph 中使用这些 action types 来创建或编辑 image annotation。

From the overview page, we can view two [action types](/docs/foundry/action-types/overview/) that we created to use on the `Annotation` object type: `Create [Ships] Annotation` and `Edit annotation coordinates`. We can use these action types in our Vertex graph to create or edit an image annotation.
![The action types on the Annotation object type in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-oma-annotation-action-types.png)
选择该 action type 以查看其概览页面。我们可以看到，例如 `Create [Ships] Annotation` action type 在运行时被设置为使用 `Annotation name`、`Coordinates`、`Hexcolor` 和 `File Name` properties。

Select the action type to view its overview page. We can see that the `Create [Ships] Annotation` action type, for example, is set up to use the `Annotation name`, `Coordinates`, `Hexcolor`, and `File Name` properties when run.
![The create annotation action type configuration in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-oma-create-annotation-action.png)
您可以配置默认使用哪个 object type property 作为 image annotations 的像素空间边界框坐标。在同一 **Capabilities** 选项卡中，从 **Image annotation coordinate property** 下拉菜单中的可用 properties 中进行选择。在我们的示例中，我们选择 `Coordinates` property。

You can configure which of the object type properties is used by default as the pixel space bounding box coordinates of your image annotations. In the same **Capabilities** tab, choose from the properties available in the **Image annotation coordinate property** dropdown menu. For our example, we are choosing the `Coordinates` property.
![The coordinates property configuration for the Ship object type in Ontology Manager.](/docs/resources/foundry/vertex/media-layers-config-annotation.png)
## Add objects as media layers
在确认 Ontology Manager 中的配置后，您可以将 objects 添加到您的 Vertex graph 中。选择 **+ Add object** 以打开 object 搜索界面。

After confirming your configurations in Ontology Manager, you can add objects to your Vertex graph. Select **+ Add object** to open the object search interface.
![Add an object to the Vertex graph.](/docs/resources/foundry/vertex/media-layers-add-object.png)
您可以按名称、类型或其他标识性 properties 进行搜索。您还可以使用下拉菜单筛选仅包含 media references 的 object types。

You can search by name, type, or other identifying properties. You can also filter down to object types that only contain media references using the dropdown menu.
![The search dialog for adding objects to the Vertex graph.](/docs/resources/foundry/vertex/media-layers-search-dialog.png)
在对话框的右下角，使用下拉菜单指定如何将 object 添加到 Vertex。**Object** 是默认选项，将使用其配置的 Ontology Manager object type 图标和颜色将 objects 添加到 graph 中。选择 **Object with media** 选项可在 object 上添加和查看 annotations。

In the bottom right corner of the dialog, use the dropdown menu to specify how to add the object to Vertex. **Object** is the default option and will add the objects to the graph with their configured Ontology Manager object type icon and color. Choose the **Object with media** option to add and view annotations on the object.
![Choose how the object will display in Vertex.](/docs/resources/foundry/vertex/media-layers-filter-object.png)
选择完所有要添加到 Vertex 的 objects 后，选择 **Add all** 或 **+ Add selected** 将它们添加到您的 graph 中，它们将在其中显示为媒体层。

Once you have selected all the objects you wish to add to Vertex, choose to **Add all** or **+ Add selected** to add them to your graph where they will be displayed as a media layer.
![Add the selected objects to your Vertex graph.](/docs/resources/foundry/vertex/media-layers-add-to-graph.png)
## Style and explore media layers
除非[在 Ontology Manager 中另有配置](#ontology-manager-configuration)，否则媒体层默认将使用第一个 media reference 显示 object。但是，您也可以使用从左侧 **Layers** 面板访问的图标样式选项来自定义媒体层 objects 的视觉外观。如果您要显示的 object 具有多个 media references，您可以选择要使用的哪一个。

Unless [otherwise configured in Ontology Manager](#ontology-manager-configuration), media layers will, by default, display the object using the first media reference. However, you can also customize the visual appearance of your media layer objects using the icon style options accessed from the **Layers** panel to the left. If the object you want to display has multiple media references, you can select which one to use.
![Modify the icon used for the object in the Vertex media layer.](/docs/resources/foundry/vertex/media-layers-style-icon.png)
右键单击 graph 以使用 Search Around 功能来探索相关的 objects，并通过连接的数据扩展您的媒体层可视化。

Right-click on the graph to use the Search Around functionality to explore related objects and expand your media layer visualization with connected data.
![The Search Around feature on a Vertex graph.](/docs/resources/foundry/vertex/media-layers-search-around.png)
如果您没有在 Ontology Manager 中为 object[配置 image annotation coordinate property](#ontology-manager-configuration)，您也可以使用样式选项来选择哪个 property 用作 image annotations 的像素空间边界框坐标。

If you did not [configure the image annotation coordinate property](#ontology-manager-configuration) for the object in Ontology Manager, you can also use the style options to choose which property is used as the pixel-space bounding box coordinates of your image annotations.
![Configure the pixel space bounding box coordinates of the media in Vertex.](/docs/resources/foundry/vertex/media-layers-bounding-box.png)
选择 media layer 中的对象以查看并交互其 properties。selection 将高亮所选对象并显示相关信息。

Select objects within your media layer to view and interact with their properties. The selection will highlight the chosen object and display relevant information.
![Selected objects in the Vertex media layer.](/docs/resources/foundry/vertex/media-layers-selected-object.png)
使用 annotation layer 样式菜单为 annotation 设置样式，包括 fill 和 outline 颜色。

Style the annotations, including the fill and outline colors, using the annotation layer style menu.
![Modify the fill color of an annotation in the media layer.](/docs/resources/foundry/vertex/media-layers-style-option.png)
![Image annotations after modifying styling.](/docs/resources/foundry/vertex/media-layers-style-result.png)
## Create image annotations
Annotation 允许您在 media layer 中标记特定的区域或特征。要创建新的 annotation,请右键单击 media layer 对象以打开上下文菜单,然后选择 **Create Annotation**。

Annotations allow you to mark specific areas or features within your media layer. To create a new annotation, right-click on a media layer object to open the context menu and select **Create Annotation**.
![Right-click on the graph to add an annotation to the media layer.](/docs/resources/foundry/vertex/media-layers-create-annotation.png)
直接在图像上绘制 annotation,拖动以定义形状。绘制完成后,您可以调整 annotation 的大小和位置。

Draw your annotation directly on the image, dragging to define the shape. You can resize and move the annotation after you draw it.
![A drawn annotation on the graph media layer.](/docs/resources/foundry/vertex/media-layers-draw-annotation.png)
如果您配置了 action types 来为链接到 media 的 object type 的对象创建 annotation,您将在下拉菜单中看到运行这些 action 的选项。在我们的示例中,可以看到 `Create [Ships] Annotation` 和 `Create [Ships] Text annotation` 两个选项。

If you configured action types to create annotations for objects linked to the object type of the media, you will see the options to run those actions in a dropdown menu. In our example, we can see both the `Create [Ships] Annotation` and a `Create [Ships] Text annotation`.
![Available action type options for the object type of the selected image.](/docs/resources/foundry/vertex/media-layers-action-options.png)
选择要运行的 action type,然后填写表单以命名您的新 annotation 对象。请注意,annotation 的坐标将用作新对象的 bounding box 坐标,具体取决于您如何为 object type 配置 action。

Select the action type you want to run, then fill out the form to name your new annotation object. Notice that the coordinates of the annotation will be used as the bounding box coordinates for the new object, which will vary depending on how you configured the action for your object type.
![The action form for the new annotation object.](/docs/resources/foundry/vertex/media-layers-action-form.png)
您现在可以在 graph 的 media layer 中查看带有其关联 annotation 的对象。

You can now view the object with its associated annotation in the media layer of your graph.
![The annotation object in the graph media layer, connected to the image object type.](/docs/resources/foundry/vertex/media-layers-add-object-result.png)
## Modify existing annotations
要修改现有的 annotation,请找到并选择要编辑的对象。在本例中,我们使用一个先前已添加 annotation 的 `Linen locker` 对象。

To modify an existing annotation, locate and select the object you want to edit. In this example, we are working with a `Linen locker` object that was previously annotated.
![A Linen locker object on the Vertex graph.](/docs/resources/foundry/vertex/media-layers-linen-locker-existing-object.png)
当您移动或调整 annotation 的大小时,任何可以修改 object type 的 action types 将出现在 annotation 下方。在我们的示例中,我们可以运行 `Edit annotation coordinates` action type 来更新 annotation 的新位置。

When you move or resize an annotation, any action types that can modify the object type will appear below the annotation. In our example, we can run an `Edit annotation coordinates` action type to update the new location of the annotation.
![The option to run the Edit annotation coordinates action type.](/docs/resources/foundry/vertex/media-layers-linen-locker-edit.png)
使用编辑表单更新对象的 pixel space bounding box 坐标,该坐标由我们刚刚绘制的形状填充。

Use the edit form to update the object's pixel space bounding box coordinates, which is populated by the shape we just drew.
![The form to edit the coordinates of the Annotation object.](/docs/resources/foundry/vertex/media-layers-edit-form.png)
完成更改后,请检查更新后的对象以确保您的修改已正确应用。编辑后的 annotation 将在 media layer 中反映您的更改。

After making your changes, review the updated object to ensure your modifications were applied correctly. The edited annotation will reflect your changes in the media layer.
![The updated properties of the edited annotation.](/docs/resources/foundry/vertex/media-layers-edit-result.png)