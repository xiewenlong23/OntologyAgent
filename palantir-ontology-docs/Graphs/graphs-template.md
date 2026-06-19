<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/graphs-template/
---
# Create a graph template
Vertex graph templates 是根据 parameters 生成具有已定义样式的 graphs 的资源。它们支持以下工作流：

Vertex graph templates are resources that generate graphs with a defined styling based on parameters. They enable workflows such as:
* 将对一个 object/object set 的 graph 分析转移到另一个 object/object set。

* 创建一个可重用的资源，为使用者编码 graph 生成工作流。

* 将 graph template 嵌入到其他 Foundry 应用程序中，例如 Object View 或 Workshop 应用程序。

* Pivoting a graph analysis on one object/object set to another object/object set.
* Creating a reusable resource encoding a graph generation workflow for consumers.
* Embedding a graph template in another Foundry application, such as an Object View or a Workshop application.
任何 Vertex analysis 都可以转换为 graph template。将 analysis 转换为 template 可以更轻松地进行未来相同性质的分析。

Any Vertex analysis can be converted into a graph template. Transforming an analysis into a template makes it easier to conduct future analyses of the same nature.
在此示例中，我们正在探索航班延误情况，通过使用 Search Around function 分析链接到 `Aircrafts` 以及同一天（在 `Airports`）其他延误 `Flights` 的 `Delay Event`。生成下面所示的航班延误调查 graph 的 analysis 是以自由形式执行的，没有强加结构。通过从该 analysis 创建一个 graph template，我们可以在未来的调查中重用此 analysis template。

In this example, we are exploring airline delays with an analysis of a flight `Delay Event` linked to `Aircrafts` and other delayed `Flights` (at `Airports`) on the same day using a Search Around function. The analysis that generated the flight delay investigation graph shown below was performed in a free-form way without an imposed structure. By creating a graph template from the analysis, we enable reuse of this analysis template in future investigations.
![Graph analysis for template](/docs/resources/foundry/vertex/template-source-graph.png)
要将此 analysis 转换为 graph template，请打开右上角工具栏中的保存选项，然后选择 **Save as Template...**。

To convert this analysis into a graph template, open the save options in the top-right toolbar and select **Save as Template...**.
![Opening the Template helper](/docs/resources/foundry/vertex/template-helper.png)
这将打开一个辅助工具，其中提供 **Configure parameters** 选项。Graph template parameters 有两种类型：**object parameters** 和 **non-object parameters**。

This will open a helper with the option to **Configure parameters**. There are two kinds of graph template parameters: **object parameters** and **non-object parameters**.
Object parameters 是 template 的 object 输入，将在 template 被使用时添加到 graph 中。添加 object parameters 还允许您对 graph template 用户提供的 objects 执行 Search Arounds 和 functions。

Object parameters are object inputs to your template which will be added to the graph when the template is used. Adding object parameters also allows you to perform Search Arounds and functions on the objects provided by the graph template user.
Non-object parameters 是可用作自定义 Search Around functions 或 saved Search Arounds 参数的其他 parameters。Non-object parameters 支持的类型与 Search Around functions 支持的 non-object 参数相一致。

Non-object parameters are additional parameters that can be used as arguments to custom Search Around functions or saved Search Arounds. The supported types for non-object parameters mirror the non-object arguments supported by Search Around functions.
![Configuring Template parameters](/docs/resources/foundry/vertex/template-configure-parameters.png)
接下来，您可以 **configure Search Arounds** 与您的 template 相关联。每个 object parameter 都可以与 Search Arounds 相关联，这些 Search Arounds 可以是使用 Ontology links 的简单 Search Arounds、Search Around functions，或使用 Search Around 侧边栏构建的 saved Search Arounds。Search Around functions 或 saved Search Arounds 的任何 non-object 参数都可以映射到一个值，该值可以是常量或 parameter。要将输入映射到 parameter，请选择输入框左侧的 parameter 按钮，然后从下拉列表中选择一个 parameter。

Next, you can **configure Search Arounds** associated with your template. Each object parameter can be associated with Search Arounds, which can be either simple Search Arounds using Ontology links, Search Around functions, or saved Search Arounds which were built using the Search Around sidebar. Any non-object arguments to Search Around functions or saved Search Arounds can be mapped to a value, which can be either a constant or a parameter. To map an input to a parameter, choose the parameter button on the left side of the input box and select a parameter from the dropdown.
![Configuring Template parameters](/docs/resources/foundry/vertex/template-configure-search-arounds.png)
添加任何所需的 parameters 和 Search Arounds 后，您可以 **configure layers** 以及与 template 相关的 layer styling。对 styling layers 的更改将保存 graph 上现有的当前样式。Excluded layers 将在保存的 template 中省略 layer style。

After adding any desired parameters and Search Arounds, you can **configure layers** and layer styling associated with your template. Styling layers will save the current styling as it exists on your graph. Excluded layers will leave out the layer style in the saved template.
![Configuring Template parameters](/docs/resources/foundry/vertex/template-configure-layers.png)
最后，在选择要应用的布局以及要保留的当前分析中的图形设置后，您可以查看 **template summary（模板摘要）** 并选择保存您的模板。

Lastly, after choosing a layout to apply and which graph settings from your current analysis to keep, you can view a **template summary** and choose to save your template.
![Template summary](/docs/resources/foundry/vertex/template-summary.png)
## Use a graph template
模板打开后，系统将提示您提供模板参数的值。

Once the template is opened, you will be prompted to supply values for the template parameters.
对象或对象集也可以通过 URL query parameters 预加载到模板中：

An object or an object set can also be preloaded into a template using URL query parameters:
* **Object：** 使用 query parameter `objectRid=<your_object_rid_here>`

* **Object set：** 使用 query parameter `objectSetRid=<your_object_set_rid_here>`

* **Object:** Use query parameter `objectRid=<your_object_rid_here>`
* **Object set:** Use query parameter `objectSetRid=<your_object_set_rid_here>`
要与给定的参数值进行交互，请使用顶部工具栏中的 **Parameters（参数）** 按钮。这将允许您选择用作给定对象参数值的所有对象，或更改参数值以重新生成您的图形。

To interact with the given parameter values, use the **Parameters** button in the top toolbar. This will allow you to select all the objects used as values for a given object parameter, or change the parameter values to regenerate your graph.
![Using a template](/docs/resources/foundry/vertex/template-usage.gif)
> **ℹ️ 注意**

> 模板也可以使用 [Vertex widget](/docs/foundry/vertex/embed-graph-workshop/) 嵌入到 Workshop 中。
> **ℹ️ 注意**

> Templates can also be embedded in Workshop using the [Vertex widget](/docs/foundry/vertex/embed-graph-workshop/).