<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/use-full-views-in-platform/
---
# Use full Object Views
完整 Object View 提供了对 Object 数据的全面展示。它们是 Object 在平台内的主要视图，可以在平台应用程序中访问，也可以嵌入到自定义 Workshop 应用程序中。

Full Object Views provide comprehensive displays of an object's data. They are the primary view for the object in-platform and can be accessed within platform applications or embedded into custom Workshop applications.
完整的 `Patient` Object View 示例：

An example of a full `Patient` Object View:
![Full patient Object View example.](/docs/resources/foundry/object-views/overview-full-object-view.png)
完整的 `Rental` Object View 示例：

An example of a full `Rental` Object View:
![Full rental Object View example.](/docs/resources/foundry/object-views/full-object-view-airport-example.png)
## Workshop
[Workshop 的 Object View widget](/docs/foundry/workshop/widgets-object-view/) 可以在自定义的 Workshop 应用程序中显示详细的 Object View。当配置为显示完整的 Object View 时，此 widget 通常在浮层或模态框中使用，以适应完整的页面分辨率。

[Workshop’s Object View widget](/docs/foundry/workshop/widgets-object-view/) can display a detailed Object View inside custom Workshop applications. When configured to display the full Object View, this widget is often used within an overlay or modal to accommodate the full page resolution.
![A Workshop Object View widget example.](/docs/resources/foundry/object-views/workshop-object-view-widget-example.gif)
## Object Explorer
在 [Object Explorer](/docs/foundry/object-explorer/overview/) 中，您可以搜索一个 object，然后选择它以打开完整的 Object View，从而提供有关 Ontology 中定义的 object 的详细信息。

In [Object Explorer](/docs/foundry/object-explorer/overview/), you can search for an object, then select it to open the full Object View, providing detailed information about the objects defined in the Ontology.
![Full Object View in Object Explorer](/docs/resources/foundry/object-views/object-explorer-full-object-view.png)
## Platform applications
Vertex、Maps 和 Gaia 等应用程序使用面板式 Object View，为所选 object 提供可定制的紧凑视图。在面板内，选择 object 的标题将在可移动且可调整大小的模态框中打开完整的 Object View。

Applications like Vertex, Maps, and Gaia use panel Object Views to provide a customizable, compact view of the selected object. Within the panel, selecting the object’s title will open the full Object View in a moveable and resizable modal.
![A full Object View displayed in a modal within the Vertex application.](/docs/resources/foundry/object-views/vertex-full-object-view.gif)