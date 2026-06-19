<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/standard-object-views/
---
# Standard Object Views
当您在 Ontology 中创建并配置 [object type](/docs/foundry/object-link-types/object-types-overview/) 时，Foundry 会自动创建一个标准的 Object View，以为其所有对象提供标准化表示，确保其他用户能够全面理解其 schema 和 link。标准 Object View 通过突出显示重要 property 来匹配 object type 的配置，无论是以专用表格形式，还是在 property 的 [base type](/docs/foundry/object-link-types/base-types/) 为 time series、media reference 或 geospatial property 时以其他可视化格式呈现。常规 property 显示在普通表格中，hidden property 则不可见。

When you create and configure an [object type](/docs/foundry/object-link-types/object-types-overview/) in your Ontology, Foundry automatically creates a standard Object View to provide a standardized representation of all its objects, ensuring other users have a holistic understanding of its schema and links. The standard Object View matches the object type's configuration by spotlighting prominent properties in either a dedicated table or in other visual formats if the property's [base type](/docs/foundry/object-link-types/base-types/) is a time series, media reference, or geospatial property. Normal properties are displayed in a regular table, and hidden properties are not visible.
虽然所有 object type 都可以使用标准 Object View，但您可以创建 [configured views](/docs/foundry/object-views/config-object-views/)，以便根据 object type 在您 Ontology 中的功能，为其提供具有上下文和经过精心策划的 Object View 体验。当您创建 configured Object View 时，Foundry 会将其作为用户的默认 view；但用户可以选择切换到标准 view，以标准格式查看 object 数据。

While standard Object Views are available for all object types, you can create [configured views](/docs/foundry/object-views/config-object-views/) to provide a contextualized and curated Object View experience for any object type based on its function in your Ontology. When you create a configured Object View, Foundry makes it available as the default view for a user; however, users can choose to select the standard view to see object data in its standard format.
## Prominent property displays
Foundry 将 [prominent properties](/docs/foundry/object-link-types/property-metadata/#metadata-reference) 显示在标准 Object View 顶部，以立即提供关于对象最重要信息的上下文。

Foundry surfaces [prominent properties](/docs/foundry/object-link-types/property-metadata/#metadata-reference) at the top of the standard Object View to provide immediate context about an object's most important information.
### Display behavior
标记为 prominent 的 property 会根据其类型获得增强的可视化处理：

Properties marked as prominent receive enhanced visual treatment based on their type:
* **[Media reference properties](/docs/foundry/object-link-types/base-types/#media-references)：** 使用专用 media viewer 渲染，以查看所有支持的 media 类型。

* **[Time series properties](/docs/foundry/time-series/time-series-properties/)：** 显示为展示时序数据模式的交互式图表。

* **[Geospatial properties](/docs/foundry/geospatial/ontology/)：** 拥有 prominent geohash、geoshape 或 geotemporal series reference (GTSR) property 的对象将在 [Map](/docs/foundry/map/overview/) 上渲染。[表示对象随时间变化的经纬度](/docs/foundry/map/integrate-objects/#track-objects) 的 time series property 也会显示在 Map 上。

* **其他 property 类型：** 所有其他 prominent property 均使用更大的卡片样式格式显示，并置于展示其余标准 property 的表格上方。

* **[Media reference properties](/docs/foundry/object-link-types/base-types/#media-references):** Rendered with a dedicated media viewer for viewing all supported media types.
* **[Time series properties](/docs/foundry/time-series/time-series-properties/):** Displayed as interactive charts showing temporal data patterns.
* **[Geospatial properties](/docs/foundry/geospatial/ontology/):** Objects with prominent geohash, geoshape, or geotemporal series reference (GTSR) properties will render on a [Map](/docs/foundry/map/overview/). Time series properties that [represent an object's latitude and longitude over time](/docs/foundry/map/integrate-objects/#track-objects) are also displayed on a Map.
* **Other property types:** All other prominent properties are displayed using a larger, card-style format elevated above a table displaying the remaining standard properties.
## Linked objects component
**Linked objects** 组件使您能够直接在标准 Object View 内遍历 [linked objects](/docs/foundry/object-link-types/link-types-overview/)。

The **Linked objects** component enables you to traverse across [linked objects](/docs/foundry/object-link-types/link-types-overview/) directly within the standard Object View.
![The Linked objects component.](/docs/resources/foundry/object-views/linked-objects-component.png)
使用标准 Object View 的 **Linked objects** 组件，您可以：

Use the **Linked objects** component of a standard Object View to:
* 按 link type 查看分组的 linked objects。

* 内联预览 linked objects 的 property，无需离开当前 view。

* 在新标签页中打开 linked objects 的子集以进行进一步探索。

* 在标准 Object View 的侧边 panel 中预览所选的 linked object。

* View linked objects grouped by link type.
* Preview properties of linked objects inline without leaving the current view.
* Open a subset of linked objects in a new tab for further exploration.
* Preview a selected linked object in the side panel of the standard Object View.
## Panel standard Object View display behavior
您还可以通过 [panel](/docs/foundry/object-views/config-panel-views/) 形式与标准 Object View 的所有功能进行交互。

You can also interact with all of a standard Object View's functionality in its [panel](/docs/foundry/object-views/config-panel-views/) form factor.
![The standard Object View panel.](/docs/resources/foundry/object-views/core-object-view-panel.png)