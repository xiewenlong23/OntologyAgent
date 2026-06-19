<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/widget/
---
# Embed a map template in a Workshop module
[地图模板](/docs/foundry/map/templates/) 可以嵌入到 Workshop 模块中。其参数值可以直接从 Workshop 变量传递。

[Map templates](/docs/foundry/map/templates/) can be embedded in Workshop modules. Their parameter values can be passed directly from Workshop variables.
将地图模板嵌入 Workshop 模块需要三个步骤：

There are three steps to embed a map template in a Workshop module:
1. [在 Workshop 中添加 Map widget](#add-a-map-widget-in-workshop)

2. [选择资源](#choose-a-resource)

3. [配置 widget](#configure-the-widget)

1. [Add a Map widget in Workshop](#add-a-map-widget-in-workshop)
2. [Choose a resource](#choose-a-resource)
3. [Configure the widget](#configure-the-widget)
## Add a Map widget in Workshop
在 Workshop 模块中您选择的部分，点击 **+** 图标或 **+ Add widget** 以打开 widget 菜单，然后搜索 [Map widget](/docs/foundry/workshop/widgets-map/)。

In a section of your choice in the Workshop module, select the **+** icon or **+ Add widget** to open the widget menu, and search for the [Map widget](/docs/foundry/workshop/widgets-map/).
## Choose a resource
在 widget 编辑器的 **Layers** 部分，选择 **Import map template** 而不是默认的 **Local configuration**。在 **Resource** 设置下，选择 **Select** 以查看兼容资源的列表，然后选择要嵌入的地图模板资源。

In the **Layers** section of the widget editor, select **Import map template** instead of the default **Local configuration**. Under the **Resource** setting, choose **Select** to see a list of compatible resources and select the map template resource you want to embed.
## Configure the widget
对于 **Map** widget，大多数配置选项在本地配置和嵌入模板中是相同的。有关一般配置，请参阅 [Map widget 文档](/docs/foundry/workshop/widgets-map/#interactions)。某些 widget 设置仅适用于嵌入模板配置：

For the **Map** widget, most of the configuration options are the same for local configuration and embedded templates. For general configuration, refer to the [Map widget documentation](/docs/foundry/workshop/widgets-map/#interactions). Some widget settings only apply to the embedded template configuration:
* **Layers**
* **Resource：** 选择要嵌入的地图模板资源。可选地提供 **Override map RID**。如果提供，将显示现有地图，而不是使用模板及其参数生成的默认地图。这允许执行诸如从保存在对象属性中的 RID 加载现有地图等操作。

* **Parameters：** 使用 Workshop 变量为模板参数提供值。

* **Refresh key：** 每当此变量的值更改时，widget 将执行地图的完整重新加载。

* **Base layer picker：** 控制默认的背景地图图像。当启用 **Show base layer picker** 切换时，用户可以从地图 widget 界面编辑底图。

* **Load data from scenario：** 使用 scenario 而不是基础 Ontology 加载给定资源。

* **Regenerate map after applying scenario：** 设置后，地图将在每次 scenario 修改后刷新。

* **Layers**
* **Resource:** Choose the map template resource to embed. Optionally provide an **Override map RID**. If provided, an existing map will be displayed instead of the default map that is generated using the template and its parameters. This allows actions such as loading an existing map from an RID saved in an object property.
* **Parameters:** Supply values for template parameters using Workshop variables.
* **Refresh key:** Whenever this variable's value changes, the widget will perform a complete reload of the map.
* **Base layer picker:** Controls the default background map imagery. When the **Show base layer picker** toggle is enabled, users can edit the base map from the map widget interface.
* **Load data from scenario:** Load the given resource using a scenario instead of the base Ontology.
* **Regenerate map after applying scenario:** When set, the map will be refreshed after each scenario modification.
* **Interaction**
* **Selected objects：** 输出当前所选对象的对象集。然后可以在当前模块的下游 widget 中使用此对象集。

* **On selected objects change：** 配置 Workshop 事件以在地图上的所选对象更改时触发。例如，触发器可以打开一个包含所选对象更详细视图的抽屉。

* **All visible objects on map：** 输出当前地图中可见对象的对象集。

* **Available actions：** 控制可从 widget 提交的操作。选择 **Some** 选项以手动指定可用的操作，以及可以利用模块变量作为默认参数值的操作配置。

* **On selected action application：** 配置 Workshop 事件以在任何操作成功应用于 widget 内时触发。

* **Interaction**
* **Selected objects:** Output an object set of the currently selected object(s). This object set can then be used in downstream widgets in the current module.
* **On selected objects change:** Configure Workshop events to trigger when the selected objects on the map change. For example, the trigger could open a drawer with a more detailed view of the selected objects.
* **All visible objects on map:** Output an object set of the visible objects in the current map.
* **Available actions:** Controls the actions that will be available for submission from the widget. Choose the **Some** option to manually specify the available actions, along with an action config that can leverage module variables as default parameter values.
* **On selected action application:** Configure Workshop events to trigger when any action is successfully applied within the widget.
* **Interface**
* **Show layers panel：** 在地图 widget 界面中显示图层面板。

* **Show histogram：** 显示直方图面板，以便能够按对象类型或属性过滤地图。

* **Show series panel：** 在地图界面的底部显示 series 面板。

* **Incomplete inputs message：** 当地图模板由于缺少必需的输入而无法运行时，此消息将在对话框中显示给用户。

* **Enable image export to clipboard：** 允许用户将地图图像导出到剪贴板。

* **Filter rendered objects：** 设置后，允许用户通过 **Object set filter** 变量过滤地图上显示的对象。

* **Saving settings：** 启用以允许用户保存当前地图。
* 当嵌入的资源是地图模板时，保存将创建一个新的地图资源。

* 此地图将使用 **Default resource name** 指定的名称命名，并放置在 **Default folder** 给出的文件夹中。如果启用了 **Show resource dialog**，将提示用户选择资源名称和位置，所配置的名称和文件夹将作为起始点显示在资源对话框中。

* 如果成功创建地图，则 **On create new map** 中定义的事件和/或 ontology Action 将被触发。如果您希望将创建的地图 RID 用作 Action 参数的输入，请在参数输入选择器中使用特殊的 **Saved map RID** 选项。请注意，所有必需的参数必须配置已定义的默认值，因为不会向用户显示任何 Action 表单。
* 当嵌入的资源是地图时，保存将仅更新嵌入的地图资源，而不是创建新资源。

* **Interface**
* **Show layers panel:** Display the layers panel within the map widget interface.
* **Show histogram:** Display the histogram panel to enable filtering the map by object type or property.
* **Show series panel:** Display the series panel on the bottom of the map interface.
* **Incomplete inputs message:** When a map template cannot run due to missing required inputs, this message is displayed to the user in a dialog.
* **Enable image export to clipboard:** Allow users to export an image of the map to their clipboard.
* **Filter rendered objects:** When set, allow users to filter the displayed objects on the Map via an **Object set filter** variable.
* **Saving settings:** Enable to allow the user to save the current map.
* When the embedded resource is a map template, saving will create a new map resource.
* This map will be given the name specified by **Default resource name** and be placed in the folder given by **Default folder**. If **Show resource dialog** is enabled, the user will be prompted to pick a resource name and location, with the configured name and folder being shown as a starting point in the resource dialog.
* If a map is successfully created, the events and/or ontology Action defined in **On create new map** will be triggered. If you wish to use the created map RID as an input to an Action parameter, use the special **Saved map RID** option in the parameter input picker. Note that all required parameters must be configured with a defined default value, as no Action form will be shown to the user.
* When the embedded resource is a map, saving will simply update the embedded map resource, rather than creating a new resource.
> **ℹ️ 注意**

> 以前，模板输入是使用单个 input object set 变量提供的，该变量包含地图模板中定义的所有必需对象类型。现在不鼓励这种做法，因为它仅适用于没有非对象参数且每个对象类型只有一个对象参数的模板。如果您仍然希望使用此功能，请选择 **Use legacy input object set** 复选框并提供 object set 变量。
> **ℹ️ 注意**

> Previously, template inputs were supplied using a single input object set variable that contained all the required object types defined in the map template. This is now discouraged as it only works for templates without non-object parameters and one object parameter per object type. If you wish to use this feature regardless, select the **Use legacy input object set** checkbox and supply an object set variable.