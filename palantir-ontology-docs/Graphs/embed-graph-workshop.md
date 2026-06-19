<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/embed-graph-workshop/
---
# Embed a graph in a Workshop module
Graph、graph template 和 diagram 可以嵌入到 Workshop 模块中，允许用户在 Workshop 工作流中直接与 Vertex 可视化进行交互。这种集成使强大且更广泛的数据探索和可视化体验成为 Workshop 模块的一部分。

Graphs, graph templates, and diagrams can be embedded in Workshop modules, allowing users to interact with Vertex visualizations directly within Workshop workflows. This integration enables powerful data exploration and visualization experiences as part of broader Workshop modules.
Graph template 可以直接从 Workshop variables 接收参数值，从而实现基于数据的动态可视化体验，这些体验会根据用户交互或工作流状态进行更新。

Graph templates can be passed parameter values directly from Workshop variables, enabling dynamic data-driven visualization experiences that update based on user interactions or workflow state.
在 Workshop 模块中嵌入 template 主要有三个步骤：

There are three main steps to embed a template in a Workshop module:
1. [在 Workshop 中添加 Vertex graph widget](#add-a-vertex-graph-widget-in-workshop)

2. [选择 resource](#choose-a-resource)

3. [配置 widget](#configure-the-widget)

1. [Add a Vertex graph widget in Workshop](#add-a-vertex-graph-widget-in-workshop)
2. [Choose a resource](#choose-a-resource)
3. [Configure the widget](#configure-the-widget)
## Add a Vertex graph widget in Workshop
在 Workshop 模块中您选择的某个 section 中，点击 **+** 图标或 **+Add widget** 按钮以打开 widget 菜单，然后搜索 **Vertex Graph** widget。

In a section of your choice in the Workshop module, click the **+** icon or the **+Add widget** button to open the widget menu, and search for the **Vertex Graph** widget.
![Adding the Vertex graph widget](/docs/resources/foundry/vertex/workshop-adding-widget.png)
## Choose a resource
在 widget 编辑器中，点击 **Select** 选择您要嵌入的 graph、graph template 或 diagram resource。资源选择器中只会显示兼容的资源。

In the widget editor, choose the graph, graph template or diagram resource you want to embed by clicking **Select**. Only compatible resources will show in the resource selector.
## Configure the widget
对于 **Vertex graph** widget，配置被组织为多个 section。每个 section 控制 widget 行为和外观的不同方面。

For the **Vertex graph** widget, configuration is organized into several sections. Each section controls different aspects of the widget's behavior and appearance.
### Input
**Input** section 控制显示的 graph 或 template 以及其接收数据的方式。

The **Input** section controls the displayed graph or template and how it receives data.
![The input section.](/docs/resources/foundry/vertex/workshop-input-section.png)
* **Resource**
* **Static:** 当选择此 resource 模式时，使用 resource picker 选择单个输入 resource。这可以是 graph、graph template 或 diagram。

* **Variable:** 当选择此 resource 模式时，输入 resource 由 string variable 提供，其中应包含 graph、graph pointer 或 graph template RID。

* **Override graph RID:** (Optional) 如果所选 resource 是 graph template，则可以提供一个 graph RID 以代替使用 template 及其参数生成 graph 来显示。这允许从对象属性中保存的 RID 加载现有 graph。有关更多详细信息，请参阅 [saving and sharing graph explorations](#save-and-share-graph-explorations) 部分。

* **Parameters**
* 嵌入 graph template 时，可以使用 Workshop variables 为 template 参数提供值。template 中定义的每个 parameter 将在此处显示以供配置。

* 对于 object type parameters，请从 Workshop 选择一个 object set variable。

* 对于非 object parameters，请根据 parameter type 提供适当的值。

* **Sub-graph**
* 嵌入具有多个 sub-graphs 的现有 graph 或 diagram resource 时，可以从 Workshop 中选择一个包含该 sub-graph 任意 object 的 object set variable，以选择要显示的 sub-graph。

* **Refresh key**
* 每当此 variable 的值更改时，widget 将执行 graph 的完整重新加载。这对于根据 workflow 状态更改触发刷新非常有用。

* **Append on parameter change**
* 启用后，更改 parameters 将把新 objects 追加到现有 graph，而不是从头重新生成。

* **Scenario**
* **Load data from scenario:** 启用此 toggle 以使用 scenario 而非 base Ontology 来加载给定的 resource。

* **Regenerate graph after applying scenario:** 设置后，graph 将在每次 scenario 修改后刷新。

* **Resource**
* **Static:** When this resource mode is selected, a single input resource is chosen using a resource picker. This can be a graph, graph template, or diagram.
* **Variable:** When this resource mode is selected, the input resource is provided by a string variable which should contain a graph, graph pointer or graph template RID.
* **Override graph RID:** (Optional) If the chosen resource is a graph template, you can provide a graph RID to display instead of generating a graph using the template and its parameters. This allows loading an existing graph from an RID saved in a property on an object. Refer to the [saving and sharing graph explorations](#save-and-share-graph-explorations) section for more details.
* **Parameters**
* When embedding a graph template, you can supply values for template parameters using Workshop variables. Each parameter defined in the template will appear here for configuration.
* For object type parameters, select an object set variable from Workshop.
* For non-object parameters, provide appropriate values based on the parameter type.
* **Sub-graph**
* When embedding an existing graph or diagram resource with multiple sub-graphs, you can choose which sub-graph to display by selecting an object set variable from Workshop that contains any object from that sub-graph.
* **Refresh key**
* Whenever this variable's value changes, the widget will perform a complete reload of the graph. This is useful for triggering refreshes based on workflow state changes.
* **Append on parameter change**
* When enabled, changing the parameters will append new objects to the existing graph instead of regenerating it from scratch.
* **Scenario**
* **Load data from scenario:** Enable this toggle to load the given resource using a scenario instead of the base Ontology.
* **Regenerate graph after applying scenario:** When set, the graph will be refreshed after each scenario modification.
> **ℹ️ 注意**

> 以前，template inputs 是使用单个 input object set variable 提供的，其中包含 graph template 中定义的所有必需 object types。现在不推荐这样做，因为它仅适用于没有非 object parameters 且每个 object type 仅一个 object parameter 的 templates。如果希望使用此功能，请选中 **Use legacy input object set** 复选框并提供一个 object set variable。
> **ℹ️ 注意**

> Previously, template inputs were supplied using a single input object set variable that contained all of the required object types defined in the graph template. This is now discouraged, as it only works for templates without non-object parameters and one object parameter per object type. If you wish to use this feature, select the **Use legacy input object set** checkbox and supply an object set variable.
### Interaction
**Interaction** 部分配置用户如何与 graph 交互以及 graph 如何与其他 Workshop 组件交互。

The **Interaction** section configures how users interact with the graph and how the graph interacts with other Workshop components.
![The interaction section.](/docs/resources/foundry/vertex/workshop-interaction-section.png)
* **Selected objects**
* 此选项输出当前所选 object(s) 的 object set。然后可以在当前 module 内的下游 widgets 中使用此 object set。

* 当用户在 graph 中选择 objects 时，此 variable 将自动填充所选内容。

* **On selected objects change**
* 配置 Workshop events 以在 graph 上的所选 objects 更改时触发。

* 这可用于打开一个 drawer 以更详细地查看所选 objects、触发另一个 widget 的刷新，或任何其他 Workshop event action。

* **On successful action application**
* 配置 Workshop events 以在用户成功应用 graph 中的 action 时触发。

* 此 event 在底层 action 成功执行后触发。

* **Zoom to object set**
* 只要 inputs 发生变化，就将 viewport 设置为显示给定 object set 中的 objects。

* 这允许以编程方式将 graph 聚焦于特定 objects。

* **Objects on subgraph**
* 输出一个 object set，其中包含当前所选 subgraph 上的所有 objects。

* 这对于捕获当前视图上可见的所有 objects 以供其他 widgets 使用非常有用。

* **Add objects to subgraph**
* 将给定的 objects 添加到当前所选 subgraph。

* 这允许以编程方式从其他 widgets 向 graph 添加 objects。

* **Available actions**
* 控制用户可直接在 graph interface 中使用的 actions。
* 选项包括：

* **All:** graph 上任何 object 上的所有 actions 均可用。

* **Some:** 仅特定选择的 actions 可用。

* **None:** 没有可用的 actions。

* **Selected objects**
* This option outputs an object set of the currently selected object(s). This object set can then be used in downstream widgets within the current module.
* When a user selects objects in the graph, this variable will be automatically populated with the selection.
* **On selected objects change**
* Configure Workshop events to trigger when the selected objects on the graphs change.
* This can be used to open a drawer with a more detailed view of the selected objects, trigger a refresh of another widget, or any other Workshop event action.
* **On successful action application**
* Configure Workshop events to trigger when a user successfully applies an action in the graph.
* This event fires after the underlying action is executed successfully.
* **Zoom to object set**
* Sets the viewport to display the objects in the given object set whenever the inputs change.
* This allows you to programmatically focus the graph on specific objects.
* **Objects on subgraph**
* Outputs an object set containing all the objects on the currently selected subgraph.
* This is useful for capturing all objects visible on the current view for use in other widgets.
* **Add objects to subgraph**
* Adds the given objects to the currently selected subgraph.
* This allows you to programmatically add objects to the graph from other widgets.
* **Available actions**
* Controls which actions are available to users directly within the graph interface.
* Options include:
* **All:** All actions on any object on the graph are available.
* **Some:** Only the specifically selected actions are available.
* **None:** No actions are available.
### Time Configuration
**Time configuration** 部分控制 graph 中时间的表示方式和交互方式。

The **Time configuration** section controls how time is represented and interacted with in the graph.
![The time Configuration section.](/docs/resources/foundry/vertex/workshop-time-configuration.png)
* **Selected time**
* 控制 graph 上所选的时间。

* 所选时间决定 graph 上或选择面板中显示的时间数据的任何读数。

* 仅当启用 timeline、time selection panel 或 series panel 之一时，才可选择时间。

* 所选时间默认为 graph 加载时的时间。
* 选项：

* **Default:** 时间选择未使用 variable 进行同步。

* **Timestamp variable:** 使用类型为 `Timestamp` 的 Workshop variable 同步 graph 视觉。

* **Date variable:** 使用类型为 `Date` 的 Workshop variable 同步 graph 视觉。

* **Time window**
* 控制 graph 上使用的时间窗口。时间窗口决定任何时间图表上显示的数据范围。

* 仅当启用 timeline、time selection panel 或 series panel 之一时，才可选择时间窗口。

* 默认时间窗口在 Control Panel 中配置。
* 选项：

* **Default:** 时间窗口未与 variable 同步。

* **Timestamp:** 使用两个类型为 `Timestamp` 的 Workshop variables 定义时间窗口。

* **Start:** 时间窗口的开始。

* **End:** 时间窗口的结束。

* **Date:** 使用两个类型为 `Date` 的 Workshop variables 定义时间窗口。

* **Start:** 时间窗口的开始。

* **End:** 时间窗口的结束。

* **Selected time**
* Controls the selected time on the graph.
* The selected time determines any readouts from temporal data displayed on the graph or in the selection panel.
* Selecting a time is only available when one of the timeline, the time selection panel or the series panel are enabled.
* The selected time defaults to the time the graph is loaded.
* Options:
* **Default:** Time selection is not synchronized using a variable.
* **Timestamp variable:** Synchronize graph visuals with a Workshop variable of type `Timestamp`.
* **Date variable:** Synchronize graph visuals with a Workshop variable of type `Date`.
* **Time window**
* Controls the time window used on the graph. The time window determines the range of data displayed on any temporal charts.
* Selecting a time window is only available when one of the timeline, the time selection panel or the series panel are enabled.
* The default time window is configured in Control Panel.
* Options:
* **Default:** The time window is not synchronized with a variable.
* **Timestamp:** Define a time window using two Workshop variables of type `Timestamp`.
* **Start:** The beginning of the time window.
* **End:** The end of the time window.
* **Date:** Define a time window using two Workshop variables of type `Date`.
* **Start:** The beginning of the time window.
* **End:** The end of the time window.
### Capabilities
**Capabilities** 部分控制 widget 用户可用的功能特性。

The **Capabilities** section controls the functional features that are available to users of the widget.
![The capabilities section.](/docs/resources/foundry/vertex/workshop-capabilities-section.png)
* **Read-only mode**
* 启用后，此设置将移除编辑功能并隐藏编辑 toolbar。

* 这对于创建仅供查看的可视化非常有用，在这种情况下用户不应能够修改 graph。

* **Enable transition to Vertex application**
* 启用后，将显示一个按钮，允许用户使用其当前 graph state 打开 Vertex application。

* 这提供了从 Workshop 中的嵌入式 graph 到完整 Vertex application 的无缝过渡，以执行更高级的操作。

* **Enable export as PNG**
* 启用后，允许用户将当前 graph 导出为 PNG 图像。

* 用户需要具有嵌入式 resource 的 frontend export 权限才能使用此功能。

* **Saving settings**
* 控制用户是否可以保存当前 graph state。
* 选项：

* **Disabled:** 用户无法保存 graph。

* **Enabled:** 用户可以保存 graph 并进行其他配置：

* **Default resource name:** 指定新保存 graphs 的名称。

* **Static:** 使用固定 text string 作为名称。

* **Variable:** 使用 Workshop string variable 作为名称。

* **Default folder:** 指定新保存 graphs 的存储位置。

* **Folder reference:** 选择特定 folder。

* **Static RID:** 使用特定 folder RID。

* **Variable:** 使用包含 folder RID 或 path 的 Workshop variable。

* **On create new graph:** 配置保存 graph 时发生的情况。

* **Event:** 保存 graph 时触发 Workshop event。

* **Action:** 保存 graph 时执行 Foundry action。

* 已保存 graph RID、已保存 graph 名称以及当前用户的 ID 可作为特殊 inputs 提供给 action。

* 所有必需的 parameters 必须配置 default values。

* **Show save dialog:** 控制保存时是否显示 resource dialog。

* **None:** 不显示 dialog；使用默认名称和位置保存 resource。

* **Resource dialog:** 提示用户选择名称和位置。

* **Save as versioned graph:** 启用后，即使 graph 之前未版本化，也将其保存为 versioned graph。Versioned graphs 允许自动保存和版本历史记录。

* **Read-only mode**
* When enabled, this setting removes editing capabilities and hides the editing toolbar.
* This is useful for creating view-only visualizations where users should not be able to modify the graph.
* **Enable transition to Vertex application**
* When enabled, this displays a button allowing users to open the Vertex application with their current graph state.
* This provides a seamless transition from the embedded graph in Workshop to the full Vertex application for more advanced operations.
* **Enable export as PNG**
* When enabled, this allows users to export the current graph as a PNG image.
* Users need to have frontend export permissions on the embedded resource to use this feature.
* **Saving settings**
* Controls whether users can save the current graph state.
* Options:
* **Disabled:** Users cannot save the graph.
* **Enabled:** Users can save the graph with additional configuration:
* **Default resource name:** Specifies the name for newly saved graphs.
* **Static:** Use a fixed text string as the name.
* **Variable:** Use a Workshop string variable as the name.
* **Default folder:** Specifies where newly saved graphs will be stored.
* **Folder reference:** Select a specific folder.
* **Static RID:** Use a specific folder RID.
* **Variable:** Use a Workshop variable containing a folder RID or path.
* **On create new graph:** Configure what happens when a graph is saved.
* **Event:** Trigger a Workshop event when a graph is saved.
* **Action:** Execute a Foundry action when a graph is saved.
* The saved graph RID, saved graph name, and the current user's ID are available as a special inputs to the action.
* All required parameters must have default values configured.
* **Show save dialog:** Controls whether a resource dialog is shown when saving.
* **None:** No dialog is shown; save the resource using the default name and location.
* **Resource dialog:** User is prompted to choose a name and location.
* **Save as versioned graph:** When enabled, saves the graph as a versioned graph even if it was previously unversioned. Versioned graphs allow autosaving and version history.
### Interface
**Interface** 部分控制 widget 用户可见的 UI 元素和面板。

The **Interface** section controls the UI elements and panels that are visible to users of the widget.
![The interface section.](/docs/resources/foundry/vertex/workshop-interface-section.png)
* **Legend/objects panel**
* 启用后，此 toggle 将显示左侧面板，其中包含启用时显示的 layers、selection、search、histogram 和 info 面板。

* **Series panel**
* 启用后，此 toggle 将在 widget 底部显示 series 面板。

* series 面板显示与所选 objects 相关的时间序列数据。

* **Time selection panel**
* 启用后，此 toggle 将在 widget 右上方显示 time scrubber。
* 此面板允许用户与时间数据交互并选择特定时间点。

* **Enable timeline**
* 启用后，此 toggle 将显示数据的 timeline 视图。
* 这提供了事件和数据点的时间顺序视图。

* **Is timeline open**
* 控制 module 首次加载时 timeline 是打开还是关闭。

* **Enable layers panel**
* 启用后，此 toggle 允许显示 layers 面板。

* layers 面板提供用于切换不同数据层可见性的控件。

* **Enable selection panel**
* 启用后，此 toggle 允许显示 selection 面板。

* selection 面板显示当前所选 objects 的详细信息。

* **Enable search panel**
* 启用后，此 toggle 允许显示 search 面板。

* search 面板提供在 graph 中查找 objects 的功能。

* **Enable histogram panel**
* 启用后，此 toggle 允许显示 histogram 面板。

* histogram 面板显示 graph 上 objects 的 property values 分布。

* **Enable info panel**
* 启用后，此 toggle 允许显示 information 面板。

* info 面板提供有关 graph 的高级概述元数据，包括其 layers 的 legend。

* **Enable version history panel**
* 启用后，此 toggle 允许显示 version history 面板。

* version history 面板显示 versioned graphs 的先前版本。

* **Enable add object**
* 启用后，此 toggle 允许用户将新 objects 添加到 graph。

* **Is legend/objects panel collapsed**
* 控制 module 首次加载时 legend/objects 面板是折叠还是展开。

* 这有助于管理 widget 中的初始可视空间分配。

* **Enable subgraph navigation menu**
* 启用后，此 toggle 允许用户在 subgraphs 之间导航并创建新的 subgraphs。

* 如果 graph 包含多个 subgraphs，则无论此设置如何，导航菜单都将始终显示。

* **Incomplete inputs message**
* 当 graph template 因缺少必需 inputs 而无法运行时，此 message 将在 dialog 中显示给用户。

* 使用此字段可自定义在未提供必需 template parameters 时向用户显示的 message。

* **Legend/objects panel**
* When enabled, this toggle will display the left-side panel, containing the layers, selection, search, histogram and info panels when enabled below.
* **Series panel**
* When enabled, this toggle will display the series panel on the bottom of the widget.
* The series panel shows time series data related to selected objects.
* **Time selection panel**
* When enabled, this toggle will display the time scrubber on the top-right of the widget.
* This panel allows users to interact with temporal data and select specific time points.
* **Enable timeline**
* When enabled, this toggle will display the timeline view of the data.
* This provides a chronological view of events and data points.
* **Is timeline open**
* Controls whether the timeline is open or closed on first load of the module.
* **Enable layers panel**
* When enabled, this toggle allows the layers panel to be displayed.
* The layers panel provides controls for toggling visibility of different data layers.
* **Enable selection panel**
* When enabled, this toggle allows the selection panel to be displayed.
* The selection panel shows details about currently selected objects.
* **Enable search panel**
* When enabled, this toggle allows the search panel to be displayed.
* The search panel provides functionality to find objects in the graph.
* **Enable histogram panel**
* When enabled, this toggle allows the histogram panel to be displayed.
* The histogram panel shows distributions of property values across objects on the graph.
* **Enable info panel**
* When enabled, this toggle allows the information panel to be displayed.
* The info panel provides a high-level overview metadata about the graph, including a legend for its layers.
* **Enable version history panel**
* When enabled, this toggle allows the version history panel to be displayed.
* The version history panel shows previous versions of versioned graphs.
* **Enable add object**
* When enabled, this toggle allows users to add new objects to the graph.
* **Is legend/objects panel collapsed**
* Controls whether the legend/objects panel is collapsed or expanded on first load of the module.
* This helps manage the initial visual space allocation in the widget.
* **Enable subgraph navigation menu**
* When enabled, this toggle allows users to navigate between and create new subgraphs.
* If the graph contains multiple subgraphs, the navigation menu will always appear regardless of this setting.
* **Incomplete inputs message**
* When a graph template cannot run due to missing required inputs, this message is displayed to the user in a dialog.
* Use this field to customize the message shown to users when required template parameters are not provided.
## Patterns
### Graph template parameterization
嵌入 graph template 时，可以使用 Workshop variables 对其进行参数化。这允许您创建根据用户输入或 workflow 中的其他数据更新的动态可视化。

When embedding a graph template, you can parameterize it using Workshop variables. This allows you to create dynamic visualizations that update based on user inputs or other data in the workflow.
### Save and share graph explorations
一种常见的模式是拥有一个 graph template，用户可以将其应用于某个初始 object，然后保存其当前探索结果以便稍后继续探索。

这允许用户从模板化的 workflow 开始，执行一些额外的调查，并捕获与 graph 交互时发现的有趣见解或关系。

然后可以将保存的 graph 作为引用添加到 object，从而便于与他人共享或稍后重新访问。

A common pattern is to have a graph template that users can apply to some initial object, and then save their current exploration to continue exploration later.
This allows users to start from a templatized workflow, perform some additional investigation, and capture interesting insights or relationships discovered while interacting with the graph.
The saved graph can then be added as a reference to an object, allowing it to be easily shared with others or revisited later.
要实现此模式，请使用以下步骤：

To implement this pattern, use the following steps:
1. **向 object type 添加一个 property** 用于保存已保存 graph 的 RID。

* 此 property 必须是使用 **Resource RID** 选项的 **Value Formatting** 的 string。

* 此 property 必须具有关联的 **Action** 用于设置值，该 Action 将在将 graph 保存为 resource 后使用。

* 此 object 通常与作为 parameter 传递给 graph template 的 object 相同，但也可能是一个用于保存 graphs 的单独特定 object type，通常链接到正在被探索的 object。

2. **创建一个 graph template**，配置为执行初始探索。

3. **使用 Vertex graph widget 将 graph template 嵌入到 Workshop module 中**。

1. 使用 **Static** 选项在 **Resource** 部分中选择 graph template。

2. 配置 template 的任何 parameters。

3. 使用 **Override graph RID** 选项指定保存已保存 graph RID 的 object property。

* 这可以与传递给 template 的 object 相同，或者在 graphs 在 linked object 上被引用的情况下，通过搜索 links 或单独的已保存 graphs 列表中的 Workshop variable 发现。

4. **在 widget 配置中启用 saving settings**，以允许用户保存其当前 graph state。

* 使用 **On create new graph** 选项运行将 property 值设置为已保存 graph RID 的 action。

* 配置 action parameters 时，请确保将特殊的 **Saved graph RID** 值传递给相应的 parameter。

1. **Add a property to the object type** that will hold the saved graph RID.
* This property must be a string with **Value Formatting** using the **Resource RID** option.
* This property must have an associated **Action** for setting the value, which will be used after saving the graph as a resource.
* This object is typically the same object being passed as parameter to the graph template, but it could also be a separate specific object type that is used to hold saved graphs, often linked to the object being explored.
2. **Create a graph template** configured to perform the initial exploration.
3. **Embed the graph template in a Workshop module** using the Vertex graph widget.
1. Select the graph template in the **Resource** section using the **Static** option.
2. Configure any parameters to the template.
3. Use the **Override graph RID** option to specify the object property that holds the saved graph RID.
* This could be the same object as the one passed to the template, or in the case where the graphs are referenced on a linked object, discovered using a Workshop variable from searching links or a separate list of saved graphs.
4. **Enable saving settings** in the widget configuration to allow users to save their current graph state.
* Use the **On create new graph** option to run the action that sets the property value to the saved graph RID.
* When configuring the action parameters, make sure to pass the special **Saved graph RID** value to the appropriate parameter.
按照此模式，当用户选择 save icon 时，当前 graph state 将保存为 resource，并且 object 上的 property 将更新为已保存 graph 的 RID。当用户重新访问该 object 时，将使用 **Override graph RID** 选项加载已保存的 graph。

Following this pattern, when a user selects the save icon, the current graph state will be saved as a resource, and the property on the object will be updated with the RID of the saved graph. When the user revisits the object, the saved graph will be loaded using the **Override graph RID** option.