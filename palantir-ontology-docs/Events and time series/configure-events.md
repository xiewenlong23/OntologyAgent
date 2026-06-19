<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/configure-events/
---
# Configure events
## Event configuration
要在 Vertex 中使用事件,请创建一个 time series event Object Type,并添加一个额外的 Vertex type class 来设置告警的颜色和/或严重性(这可以在任何列上,但通常是 primary key):

To use events in Vertex, create a time series event object type and add one additional Vertex type class to set the color and/or severity of the alert (this can be on any column, but typically the primary key):
* 橙色: `kind`: `vertex`, `name`: `event_intent.warning`

* 红色: `kind`: `vertex`, `name`: `event_intent.danger`

* 蓝色: `kind`: `vertex`, `name`: `event_intent.primary`

* 绿色: `kind`: `vertex`, `name`: `event_intent.success`

* Orange: `kind`: `vertex`, `name`: `event_intent.warning`
* Red: `kind`: `vertex`, `name`: `event_intent.danger`
* Blue: `kind`: `vertex`, `name`: `event_intent.primary`
* Green: `kind`: `vertex`, `name`: `event_intent.success`
您可以在 Ontology Manager 中事件 Object 的 **Capabilities** 选项卡中,或者直接在 Object 的 Property 的 type classes 中配置这些 type classes。

You can configure these type classes in the **Capabilities** tab for the event object in the Ontology Manager or directly in the type classes for the properties of the object.
![Capabilities tab](/docs/resources/foundry/vertex/optional_ontology_config-event.jpg)