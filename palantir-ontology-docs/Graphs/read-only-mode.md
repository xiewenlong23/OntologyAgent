<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/read-only-mode/
---
# Read-only mode
在某些情况下,Vertex graphs 可以以 read-only 模式打开。

在 read-only 模式下,将应用以下限制:

In certain situations, Vertex graphs can be opened in read-only mode.
In read-only mode, the following restrictions are applied:
* 无法向 graph 添加新对象(包括通过 Search Around 添加的对象)。

* 无法重新排列 graph 节点(无论是通过拖放还是其他方法)。
* 页面顶部的工具栏被隐藏。

* New objects cannot be added to the graph (including via Search Around).
* Graph nodes cannot be re-arranged (whether by drag-and-drop or other methods).
* The toolbar at the top of the page is hidden.
## When are Vertex graphs opened in read-only mode?
以下是以 read-only 模式打开 graph 的情况的非详尽列表。

Below is a non-exhaustive list of the situations where a graph is opened in read-only mode.
* 当 graph 嵌入在 Workshop 中,并且在 [widget configuration](/docs/foundry/vertex/embed-graph-workshop/#configure-the-widget) 中明确启用了 read-only 模式设置时。

* 当 graph 在 [Carbon](/docs/foundry/carbon/overview/) 中打开时。

* 当 graph 嵌入在 [Notepad](/docs/foundry/notepad/widgets-vertex-graph/) 中时。

* When a graph is embedded in Workshop and the read-only mode setting is explicitly enabled in the [widget configuration](/docs/foundry/vertex/embed-graph-workshop/#configure-the-widget).
* When a graph is opened in [Carbon](/docs/foundry/carbon/overview/).
* When a graph is embedded in [Notepad](/docs/foundry/notepad/widgets-vertex-graph/).