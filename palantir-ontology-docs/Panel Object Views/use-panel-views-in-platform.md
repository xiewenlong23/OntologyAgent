<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/use-panel-views-in-platform/
---
# Use panel Object Views
Panel Object Views 嵌入到 Palantir 平台的各个应用程序中，以便为用户提供跨工作流的一致对象数据体验。所有 Object Type 默认都有一个 [standard Object View](/docs/foundry/object-views/standard-object-views/) 面板可用，您可以构建 [configured panel Object Views](/docs/foundry/object-views/config-panel-views/) 来显示 *object instance* 或 *object set*。

Panel Object Views are embedded into applications across the Palantir platform to provide users with a consistent experience of object data across workflows. All object types have a [standard Object View](/docs/foundry/object-views/standard-object-views/) panel available by default, and you can build [configured panel Object Views](/docs/foundry/object-views/config-panel-views/) to display either an *object instance* or an *object set*.
## Panel Object Views in platform applications
Panel Object Views 可以出现在 Palantir 平台应用程序中，例如 [Vertex](/docs/foundry/vertex/overview/)、[Map](/docs/foundry/map/overview/) 和 Gaia。

Panel object views can appear across Palantir platform applications, such as [Vertex](/docs/foundry/vertex/overview/), [Map](/docs/foundry/map/overview/), and Gaia.
### Object instance panels
Object Instance 面板显示单个 Object Type 的一个实例，并出现在应用程序的选择面板中。

Object instance panels display a single instance of an object type and appear in an application's selection panel.

> 📷 **[图片: Panel object view embedded in Vertex.]**

> 📷 **[图片: Panel object view embedded in Maps.]**

> 📷 **[图片: Panel object view embedded in Gaia.]**

> 📷 **[图片: Panel object view embedded in Vertex.]**

> 📷 **[图片: Panel object view embedded in Maps.]**

> 📷 **[图片: Panel object view embedded in Gaia.]**

### Object set panels
Object Set 面板显示单个 Object Type 多个实例的聚合视图。当您选择由同一 Object Type 的多个实例组成的 object set 时，它们会出现在应用程序中。

Object set panels display an aggregated view of multiple instances of a single object type. They appear in applications when you select an object set comprised of several instances of the same object type.

> 📷 **[图片: Object set view panel embedded in Gaia, Maps, and Vertex.]**

> 📷 **[图片: Object set view panel embedded in Gaia, Maps, and Vertex.]**

## Panels in Workshop applications
Panels 可用于自定义 Workshop 应用程序中，以提供对象数据的紧凑视图。要启用此功能，请使用 Workshop 的 [Object View widget](/docs/foundry/workshop/widgets-object-view/)，并将其配置为显示 panel form factor。

Panels can be used in custom Workshop applications to provide a compact view of object data. To enable this, use Workshop's [Object View widget](/docs/foundry/workshop/widgets-object-view/), configured to show the panel form factor.
![Panel object view embedded in Workshop.](/docs/resources/foundry/object-views/panel-object-view-in-workshop.gif)