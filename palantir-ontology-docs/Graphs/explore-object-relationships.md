<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/explore-object-relationships/
---
# Explore object relationships
Vertex 允许您在整个现实世界组织的数字孪生中可视化并量化因果关系。通过使用 Vertex，您可以访问和探索由您组织发布的已有 Graph，或构建新的 Graph。

Vertex allows you to visualize and quantify cause and effect across the digital twin of your real-world organization. Using Vertex, you can access and explore existing graphs that have been published by your organization or build new graphs.
## Start a new exploration
Vertex 可以从 Foundry 工作区侧边栏 **Apps** 部分下的 **Operational Applications** 标题中启动。要启动新的探索，请从应用程序列表中选择 **Vertex**，然后点击 **+ New Graph** 图标。

Vertex can be launched from the Foundry workspace sidebar's **Apps** section, under the **Operational Applications** header. To launch a new exploration, select **Vertex** from the list of applications and click on the **+ New Graph** icon.
在开始新的探索时，将打开一个空白工作区，您可以在其中选择 **+ add objects** 来开始。从对象搜索弹窗中，选择您感兴趣探索的对象以开始创建您的 Graph。

When starting a new exploration, a blank workspace will open where you can choose to **+ add objects** to get started. From the object search pop-up, select the object(s) you are interested in exploring to begin creating your graph.
![Event Badges](/docs/resources/foundry/vertex/explore_objects_1.jpg)
### Object selection panel
当您点击 Graph 上的一个对象时，选择面板将自动打开以显示该对象的 Property。

When you click on an object on the graph, the selection panel will automatically open to display the properties of the object.
![Selection Panel](/docs/resources/foundry/vertex/explore_objects_2.jpg)
选择选择面板右下角的 **(+)** 符号将允许您添加 [derived property functions](/docs/foundry/vertex/derive-property-functions/)。在本例中，一个简单的 Function 用于计算与该机场相关的航线上的告警总数。Derived Property 显示在选择面板的顶部。

Selecting the **(+)** symbol at the bottom right corner of the selection panel will allow you to add [derived property functions](/docs/foundry/vertex/derive-property-functions/). In this case, a simple function calculates the total number of alerts on routes related to the airport. Derived properties are shown at the top of the selection panel.
![Derived Properties](/docs/resources/foundry/vertex/explore_objects_3.jpg)
## Explore related objects
Vertex 允许您遍历 Operation 关系来构建 Graph 可视化。从单个节点或一组节点，您可以右键单击以查看您的选择、布局和探索选项。

Vertex allows you to traverse operational relationships to build out your graph visualization. From an individual node or group of nodes, you can right-click to see your selection, layout, and exploration options.
### Search Around
从相关对象列表中进行选择以将它们添加到 Graph 中。每种类型的对象总数显示在下拉列表内。如果对象数量较多，您应考虑使用对象数量旁边的筛选图标以添加额外的筛选条件。这将打开 **Search Around** 面板，您可以在其中添加筛选条件并跨多个步骤进行搜索。

Select from the list of related objects to add them to the graph. The total number of objects of each type is shown within the dropdown list. With a large number of objects, you should consider using the filter icon next to the number of objects to include additional filters. This will open the **Search Around** panel where you can add filters and search across multiple steps.
![Basic Search Around](/docs/resources/foundry/vertex/explore_objects_4.jpg)
### Build multi-step Search Arounds
从 Graph 上的对象运行基本的 Search Around 是探索您的 Ontology 并快速将相关的相关对象添加到 Graph 的好方法。在您希望创建跨不同 Object Type 的多步骤、已筛选 Graph 的情况下，**Search Around** 面板提供了一个 point-and-click Interface，使您可以在生成新 Graph 时构建逻辑。

Running basic Search Arounds from objects on your graph can be a great way to explore your Ontology and quickly add relevant related objects to the graph. In cases where you want to create a multi-step, filtered graph that crosses different object types, the **Search Around** panel provides a point-and-click interface to build out logic as you generate a new graph.
您可以通过在基本 **Search Around** 下拉列表中选择筛选图标，或通过工作区右侧可用的标签页，访问 **Search Around** 面板。要开始 Search Around，请选择单个对象或同类型的对象；然后，您可以通过选择 Link 从所选对象创建 Search Around。

You can access the **Search Around** panel by selecting the filter icon within the basic **Search Around** dropdown list or through the tabs available on the right side of the workspace. To start the Search Around, select a single object or objects of the same type; then, you will be able to create a Search Around from your selection by choosing a link.
![Multi Step Search Around](/docs/resources/foundry/vertex/explore_objects_5.png)
如果您希望更新起始对象集，请选择一个新对象（或一组对象），然后点击将鼠标悬停在起始对象框上时出现的 **Set starting objects** 选项。

If you would like to update your starting set of objects, select a new object (or group of objects) and click the **Set starting objects** option which appears when hovering over the starting objects box.
### Find related objects
一旦选择了要添加的相关对象，找到的对象数量将显示在结果对象类型旁边。要进一步筛选返回的对象，请点击 **Add filter** 按钮并选择您希望用于筛选结果对象集的 Property。

Once you have selected the related object(s) to add, the number of objects found will be shown next to the resulting object type. To further filter the returned objects, click the **Add filter** button and select the property you wish to use to filter the resulting object set.
![Filter](/docs/resources/foundry/vertex/explore_objects_6.png)
一旦筛选了您的对象集，您可以选择立即将其添加到 Graph，或使用 **Add link** 按钮继续在多个对象之间构建多步骤 Search Around。

Once you have filtered your object set, you can choose to add this to your graph immediately, or continue building a multi-step Search Around across multiple objects using the **Add link** button.
Search Around 中的下一个 Link 将以前一个 Link 的结果对象集作为其起始对象集。使用此新 Search Around 生成的对象集，您可以找到其他相关对象以添加到 Graph；在本例中，是在 Link 1 中生成的航班的目的地机场。

The next link in the Search Around will take the resulting object set from the previous link as its starting object set. Using the object set resulting from this new Search Around, you can find additional related objects to add to the graph; in this case, the destination airport for the flights generated in Link 1.
![Link 2](/docs/resources/foundry/vertex/explore_objects_7.png)
一旦添加了新的相关对象集，您可以进一步筛选该对象集。一旦应用了筛选，起始对象集将被筛选为与筛选后的结果对象集相关联的对象。在本例中，有 157 个航班正在飞往纽约州的某个机场。

Once you have added the new related object set, you can filter this object set further. Once a filter has been applied, the starting object set will be filtered to those objects connected to the filtered resulting object set. In this case, 157 flights are departing to a NY state airport.
![Add to Graph](/docs/resources/foundry/vertex/explore_objects_8.png)
选择 **Add to graph** 以根据 Search Around 面板中定义的遍历生成新 Graph。根据 Search Around 的复杂程度，生成 Graph 可能需要一些时间。

Select **Add to graph** to generate a new graph based on the traversals defined in the Search Around panel. It may take some time to generate the graph, depending on the complexity of the Search Around.
### Add parameters
为了增强 Search Around 的可复用性，您可以定义在整个 Search Around 中使用的参数。选择面板右上角的 **View parameters** 按钮以查看任何现有参数或创建新参数。选择 **Add parameter** 按钮以选择要添加的参数类型。

To enhance reusability of Search Arounds, you can define parameters which can be used throughout the Search Around. Select the **View parameters** button in the top right corner of the panel to view any existing parameters or create new ones. Select the **Add parameter** button to choose the type of parameter to add.
![Add parameter](/docs/resources/foundry/vertex/explore_objects_9.png)
添加参数后，您可以为其赋值或选择编辑按钮以更改其名称、描述和默认值，该默认值将在加载此 Search Around 时使用。

Once you add a parameter, you can give it a value or select the edit button to change its name, description, and default value which will be used when loading this Search Around.
![Edit parameter](/docs/resources/foundry/vertex/explore_objects_10.png)
然后您可以在任何适当类型的 filter 字段中使用该参数。要使用参数，请选择 filter 字段旁边的参数开关，然后从下拉菜单中选择一个参数。更改参数值时，Search Around 将更新以反映该参数使用的任何位置的新值。

You can then use this parameter in any filter field of an appropriate type. To use a parameter, select the parameter toggle next to the filter field and then choose a parameter from the dropdown. When changing the value of the parameter, the Search Around will be updated to reflect the new value in any spot where that parameter is used.
![Use parameter](/docs/resources/foundry/vertex/explore_objects_11.png)
### Save and load
如果您想在其他 graphs 或 graph templates 中复用此 Search Around，您可以将其保存为 resource。为此，请选择要保存的 Search Around 选项卡旁边的下拉菜单。这将打开一个模态框，您可以在其中选择保存 Search Around 的名称和位置。

If you would like to reuse this Search Around in other graphs or within graph templates, you can save it as a resource. To do this, select the dropdown next to the tab for the Search Around you would like to save. This will open a modal where you can choose the name and location to save the Search Around.
![Save Search Around](/docs/resources/foundry/vertex/explore_objects_12.png)
通过 Search Around 选项卡标题中的 **+** 图标添加新的 Search Around 时，选择 **Load Search Around** 选项将打开一个 resource 选择器，允许您选择要打开的 Search Around。加载 Search Around 后，系统将提示您从 graph 中选择要用作 search around 起始 object set 的 objects。只能选择适当类型的 objects。

When adding a new Search Around through the **+** icon in the Search Around tab header, selecting the **Load Search Around** option will open a resource picker to allow you to choose the Search Around to open. Upon loading the Search Around, you will be prompted to select objects from the graph to be used as the starting object set for the search around. Only objects of the appropriate type can be selected.
![Load Search Around](/docs/resources/foundry/vertex/explore_objects_13.png)
## Histogram filters
构建好 object graph 后，您可以使用直方图过滤器来探索和过滤 graph。直方图显示所选 objects 的 properties 并提供每个 property 的总值。在直方图中所做的选择将反映在 graph 中，为您的探索提供额外的粒度。

Once you have built your object graph, you can explore and filter the graph using the histogram filters. The histogram displays the properties for selected objects and provides the total values for each. Selections made in the histogram will be reflected in the graph, giving you additional granularity in exploration.
![Histogram filter](/docs/resources/foundry/vertex/explore_objects_14.jpg)