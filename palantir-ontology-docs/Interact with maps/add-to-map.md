<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/add-to-map/
---
# Add data to a map
通过向地图添加数据开始您的地理空间分析。您可以从 Foundry 平台向地图添加两种地理空间数据：Ontology 对象和地图叠加层。

Begin your geospatial analysis by adding data to your map. There are two kinds of geospatial data you can add to your map from the Foundry platform: Ontology objects and map overlays.
在 **Layers** 面板中，单击 **+ Add to map**，使用搜索对话框将这些数据中的任意一种添加到您的地图。

From the **Layers** panel, click **+ Add to map** to add either of these kinds of data to your map using the search dialog.

> 📷 **[图片: Add to map button]**

> 📷 **[图片: Add to map button]**

## Add Ontology objects
在搜索对话框中，**Objects** 选项卡允许您将[具有地理空间数据的 Ontology 对象](/docs/foundry/map/integrate-objects/)添加到地图。

In the search dialog, the **Objects** tab allows you to add [Ontology objects that have geospatial data](/docs/foundry/map/integrate-objects/) to your map.
![Object search dialog](/docs/resources/foundry/map/add-to-map-objects-dialog.png)
在对话框中，您可以在顶部的 **Search...** 主字段中输入任何问题来搜索对象，也可以使用左侧的过滤器面板筛选要搜索的对象。

In the dialog, you can search for objects by entering any question into the primary **Search...** field at the top, or filter down the objects being searched using the filters panel on the left.
您也可以在 Control Panel 中[配置对象搜索限制](/docs/foundry/map/control-panel/#data-loading)。

You can also [configure object search limits in Control Panel](/docs/foundry/map/control-panel/#data-loading).
### Filter objects
选择一个 object type 以将结果过滤为仅包含该类型的对象。选择 object type 后，您可以使用 **Filters** 选项进一步细化搜索：

Select an object type to filter results to only include objects of that type. After selecting an object type, you can further refine your search using the **Filters** option:
![Object type filtered.](/docs/resources/foundry/map/objects-add-type-selected.png)
一些最常用的属性将自动显示在过滤器区域中，允许您通过选择感兴趣属性的值来缩小对象结果范围。

Some of the most commonly-used properties will automatically appear in the filters area, allowing you to narrow down the object results by selecting the values for properties of interest.
![Object type filtered.](/docs/resources/foundry/map/objects-add-filters.png)
您可以通过选择 **+ Add filter** 并添加所需的属性，按 object type 上的任何属性进行过滤。选择 **Back** 以使您选择的属性显示在过滤器区域中。

You can filter by any property on the object type by selecting **+ Add filter** and adding the desired properties. Select **Back** to have your chosen properties appear in the filter area.
![Add filter.](/docs/resources/foundry/map/objects-add-filter-selector.png)
### Select and add results
在结果表格中选择一个对象。要切换任何对象的选择状态，请按住 `Cmd`（macOS）或 `Ctrl`（Windows）键，或另外使用 `Shift` 键选择一定范围的对象。使用 **+ Add selected** 将所选对象添加到地图，或使用 **Add all** 将与搜索匹配的所有对象添加到地图。

Select an object in the results table. To toggle selection of any object, hold the `Cmd` (macOS) or `Ctrl` (Windows) key, or additionally use the `Shift` key to select a range of objects. Add your selected objects to the map by using **+ Add selected**, or add all objects that matched your search with **Add all**.
地图限制您可以从搜索对话框中添加的对象数量。默认情况下，您可以添加 1000 个对象。当达到此限制时，**Add all** 选项将被禁用，您需要[过滤结果](#filter-objects)以减少对象数量，然后该选项才会重新启用。

Maps limit how many objects you can add from the search dialog. By default, you can add 1000 objects. When this limit is reached, the **Add all** option is disabled and you will need to [filter your results](#filter-objects) to reduce the number of objects before the option is re-enabled.
![Add all disabled.](/docs/resources/foundry/map/objects-add-add-all-disabled.png)
## Search for objects geospatially
您可以在特定的地理空间感兴趣区域内搜索对象。从 **Add to map** 下拉菜单中，选择 **Search for objects that intersect a shape...**：

You can search for objects in a particular geospatial area of interest. From the **Add to map** dropdown, select **Search for objects that intersect a shape...**:
![Search for objects that intersect a shape.](/docs/resources/foundry/map/objects-add-search-shape.png)
然后系统会提示您在要搜索的地理空间区域周围绘制一个 [shape](/docs/foundry/map/shapes/)：

You will then be prompted to draw a [shape](/docs/foundry/map/shapes/) around the geospatial area you want to search within:
![Search for objects that intersect a shape.](/docs/resources/foundry/map/objects-add-draw-shape.png)
完成绘制 shape 后，object search 对话框将会打开，并且只显示包含与您所绘制 shape 相交的地理空间数据的对象：

After you finish drawing a shape, the objects search dialog will open and only show objects that contain geospatial data which intersects with the shape you drew:
![Search dialog filtered to intersecting objects.](/docs/resources/foundry/map/objects-add-dialog-intersecting.png)
## Add map overlays
search 对话框的 **Overlays** 选项卡允许您添加通过 [Map Layer Editor](/docs/foundry/map/layer-editor/) 创建的图层。这些图层包含可重用的、预配置的地理空间数据集视图，可在多个 map 之间共享使用。

The **Overlays** tab of the search dialog allows you to add layers created in the [Map Layer Editor](/docs/foundry/map/layer-editor/). These layers contain pre-configured views of geospatial datasets that can be reused across maps.
![Overlays dialog](/docs/resources/foundry/map/add-to-map-overlays.png)
该对话框提供了多种查找图层的方式：

The dialog contains multiple ways for you to find layers:
* 在顶部的 **Search...** 字段中输入文本，按名称查找图层。

* 使用侧边栏的 **Tags** 部分，将图层结果缩小到特定主题。

* 通过在 **In path** 输入框中输入文件夹路径，查找特定文件夹或项目中的图层。

* 通过在 **Created by** 中选择用户，查找由特定用户创建的图层。

* Enter text in the **Search...** field at the top to find layers by name.
* Use the **Tags** section of the sidebar to narrow layer results to specific topics.
* Find layers in a specific folder or project by typing the folder's path in the **In path** input.
* Look for layers created by a specific user by selecting the user in **Created by**.
选择一个图层。按住 `Cmd` (macOS) 或 `Ctrl` (Windows) 键可切换图层选择状态，使用 Shift 键可选择一个范围内的图层。点击 **Add layers** 将所选图层添加到 map 中。

Select a layer. Hold the `Cmd` (macOS) or `Ctrl` (Windows) key to toggle selection of a layer, or use the Shift key to select a range of layers. Add your selected layers to the map with **Add layers**.
## Search Around
从 map 上已有的 objects 出发，您可以通过使用 **Search Around** 来遍历 Ontology relationships，并将相关 objects 添加到您的 map 中。首先，在 map 上选择一些 objects，然后选择 **Search Around**：

Starting from objects already on your map, you can traverse Ontology relationships and add related objects to your map by using a **Search Around**. First, select some objects on the map, and then select **Search Around**:
![Search around menu](/docs/resources/foundry/map/objects-add-search-around-menu.png)
从相关 objects 列表中进行选择，将其添加到您的 map 中。如果相关 objects 显示为点，map 将在相关 objects 之间渲染一条可视化 link：

Select from the list of related objects to add them to your map. If the related objects display as points, the map will render a visual link between the related objects:
![Search around links](/docs/resources/foundry/map/objects-add-search-around-links.png)