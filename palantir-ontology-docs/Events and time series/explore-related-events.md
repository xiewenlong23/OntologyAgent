<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/explore-related-events/
---
# Explore related events
**event** 在 Ontology 中定义和配置。所有 events 必须具有不同的开始和结束时间，并可以配置特定的 thresholds 来定义 event 所显示的颜色。[Read more about setting up and configuring events](/docs/foundry/vertex/configure-events/)。

An **event** is defined and configured within the Ontology. All events must have a distinct start and end time and can be configured with specific thresholds to define the color shown for the event. [Read more about setting up and configuring events](/docs/foundry/vertex/configure-events/).
创建并配置 event objects 后，您可以通过 system graph 动态地与它们进行交互。

Once you create and configure your event objects, you can interact with them dynamically through your system graph.
### View events
链接到所选 object 的 events 将显示在 selection 面板中，并在 event 持续期间作为 badges 显示在该 object 上。

Events linked to a selected object will show up in the selection panel and as badges on the object for the duration of the event.
![explore-events-1](/docs/resources/foundry/vertex/explore-events-1.jpg)
### Event badges
Event badges 在 layer styling options 中配置。选择要显示 event badges 的 object type，并选择 **linked events** 选项以将 badges 添加到 graph 上的 nodes 或 edges。

Event badges are configured within the layer styling options. Select the object type for which you want to show event badges, and choose the **linked events** option to add badges to nodes or edges on the graph.
![explore-events-2](/docs/resources/foundry/vertex/explore-events-2.jpg)
### Event objects
要查看 event 的完整详细信息，可以将关联的 object 添加到 graph。右键单击与 event 相关的 object，然后选择 **Search Around** 选项以查找 event object（在本例中为 Flight Delay event）。

To see the full detail of the event, you can add the associated object to the graph. Right-click on the object to which the event is related, and select the **Search Around** option to find the event object (in this case, a Flight Delay event).
![explore-events-3](/docs/resources/foundry/vertex/explore-events-3.jpg)
添加到 graph 后，您可以选择 event object 以在 selection 面板中查看完整的详细信息和 properties。

Once added to the graph, you can select the event object to see the full details and properties in the selection panel.
![explore-events-4](/docs/resources/foundry/vertex/explore-events-4.jpg)
### Events in the series panel
右键单击一个 object 并选择 **Open linked events** 以打开 event 并将其添加到 series 面板中。从这里，您可以使用 time selection 来浏览时间并遍历多个 events。

Right-click on an object and select **Open linked events** to open and add the event to the series panel. From here, you can use the time selection to scrub through time and move through multiple events.
![explore-events-5](/docs/resources/foundry/vertex/explore-events-5.jpg)