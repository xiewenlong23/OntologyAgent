<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/machinery/analyze-and-monitor/
---
# Analyze and monitor a process
Machinery widget 为您配置的 Machinery processes 提供操作洞察和监控能力。

The Machinery widget provides operational insights and monitoring capabilities for your configured Machinery processes.
* 在用户积极操作 processes 时，获得对 process 操作的可见性。
* 识别分析和工作流监控的瓶颈。

* 通过可配置的视图可视化 process flows 和 metrics。

* Gain visibility into process operations when users are actively working within processes.
* Identify bottlenecks for analytical and monitoring workflows.
* Visualize process flows and metrics through configurable views.
![Image of the Machinery widget.](/docs/resources/foundry/machinery/widget.png)
该 widget 在 Workshop 应用程序中以可视化的形式渲染您的 Machinery graph，可显示 metrics、process flows 和 object distributions。

The widget renders your Machinery graph in Workshop applications as a visualization that can display metrics, process flows, and object distributions.
Machinery widget 可以在 Workshop modules 中使用，也可以在 Machinery 应用程序中作为具有有限功能的独立视图模式使用。

The Machinery widget is available in Workshop modules or as a stand-alone view mode in the Machinery application with limited features.
## Widget configuration
创建或打开一个 Workshop module，然后选择 Machinery Overview widget。默认选择 widget 版本 v2，并支持 Machinery v2 resources。在 widget 配置的顶部，选择您的 Machinery graph resource。

Create or open a Workshop module and select the Machinery Overview widget. The widget version v2 is selected by default and supports Machinery v2 resources. At the top of the widget configuration, select your Machinery graph resource.
### Upgrade existing applications
新的 Machinery widgets 将默认创建为 v2 widgets。已有的 widgets 需要升级到 v2。

New Machinery widgets will be created as v2 widgets by default. Existing widgets will need to be upgraded to v2.
1. 要将旧版 widget 升级到 v2，请通过 **...** 下拉菜单打开 **Workshop** 编辑模式。

2. 在 graph 中的任意位置选择，并在 **Widget setup** 菜单下选择 **Use Machinery v2**。

3. 相应地更新您的 [inputs](#inputs)。

1. To upgrade a legacy widget to v2, open **Workshop** edit mode with the **...** dropdown menu.
2. Select anywhere in the graph, and under the **Widget setup** menu, select **Use Machinery v2**.
3. Update your [inputs](#inputs) appropriately.

> 📷 **[图片: Machinery version selector.]**

> 📷 **[图片: Machinery version selector.]**

### Inputs
为 graph 中的每个 root process 配置一个 input object set。Machinery widget 会根据 Link Type 设置自动派生子 process 的 object sets，子 processes 通过 **Object type** 下配置的 Link Types 与其父 objects 相关联。

Configure an input object set for each root process in your graph. The Machinery widget automatically derives subprocess object sets from the link type setup, and subprocesses have link types to their parent objects, as configured under **Object type**.
**示例：** 如果您提供 100 个 application objects，并且每个 application 链接到多个 review objects，则该 widget 会通过配置的 link types 自动识别所有相关的 reviews。这意味着您只需要为 graph 的每个 root process（通常为 1 个 object input）配置 object input。

**Example:** If you provide 100 application objects, and each application is linked to multiple review objects, the widget automatically identifies all related reviews through the configured link types. This means that you only need to configure the object input for each root process of the graph (typically 1 object input).
### Metric views
Machinery widget 在实例化时附带以下预配置的 metric views：

The Machinery widget is instantiated with the following pre-configured metric views:
* **Historical count:** 显示历史计数 metrics。

* **Current count:** 显示 state 中的当前计数。

* **Historical duration:** 显示 state 中的历史持续时间。

* **Current duration:** 显示 state 中的当前持续时间。

* **Historical count:** Show ever count metrics.
* **Current count:** Show current count in state.
* **Historical duration:** Show historical duration in the state.
* **Current duration:** Show current duration in the state.
Application builders can add, remove, reorganize or customize these metrics views.
Application builders can add, remove, reorganize or customize these metrics views.

> 📷 **[图片: 在 Workshop 的编辑模式中编辑预配置的视图，或使用“添加项”选项添加您自己的视图。]**

> 📷 **[图片: Edit pre-configured views in Workshop's Edit mode or add your own with the Add item option.]**

Custom views may also be added using the **+ Add item** option. For each view, a builder can define one node metric with numerical formatting and conditional coloring, an optional edge metric, and enable Sankey diagram edge thickness settings.
Custom views may also be added using the **+ Add item** option. For each view, a builder can define one node metric with numerical formatting and conditional coloring, an optional edge metric, and enable Sankey diagram edge thickness settings.
### Outputs
Output datasets can be used for further analysis within the Workshop module. Configure output object sets to capture filtered results based on graph interactions:
Output datasets can be used for further analysis within the Workshop module. Configure output object sets to capture filtered results based on graph interactions:
* Create one output per process in the graph (optional)
* The output object set applies filters defined on the process level in the Machinery application as well as search arounds from parent to child processes.
* Outputs respond dynamically to node/edge selection
* Path explorer and distribution charts provide additional means of affecting the output
* Create one output per process in the graph (optional)
* The output object set applies filters defined on the process level in the Machinery application as well as search arounds from parent to child processes.
* Outputs respond dynamically to node/edge selection
* Path explorer and distribution charts provide additional means of affecting the output
#### Node and edge selection
You can change how node selection affects the object output by toggling either of the options:
You can change how node selection affects the object output by toggling either of the options:
* Processes currently in selected states
* Processes ever in selected states
* Processes currently in selected states
* Processes ever in selected states
Edge selection can be configured to show objects that ever went through a transition or just the last transition.
Edge selection can be configured to show objects that ever went through a transition or just the last transition.
### Configure views
Views determine what metrics and visualizations appear in the widget. See the metric views section below for details.
Views determine what metrics and visualizations appear in the widget. See the metric views section below for details.
## Widget features
A user viewing a graph in the Machinery widget can benefit from features including metric cycling and pinning, various usage modes, and filters.
A user viewing a graph in the Machinery widget can benefit from features including metric cycling and pinning, various usage modes, and filters.
### Metric views, cycling, and pinning
The widget displays metrics in a space-efficient manner. On the graph, one node metric is visible at a time, as well as one optional edge metric if selected. If the viewport is sufficiently zoomed in, the graph will show node cards with 3 metrics, starting with the active view. If Sankey diagram edges have been configured, edge thickness is used to represent flow frequency on the Transitions view.
The widget displays metrics in a space-efficient manner. On the graph, one node metric is visible at a time, as well as one optional edge metric if selected. If the viewport is sufficiently zoomed in, the graph will show node cards with 3 metrics, starting with the active view. If Sankey diagram edges have been configured, edge thickness is used to represent flow frequency on the Transitions view.
![Nodes showing metric cards when graph is zoomed-in.](/docs/resources/foundry/machinery/widget-contextual-zoom.png)
#### Preconfigured views
Users of the widget can cycle through preconfigured [metric views](#metric-views), including historical count, current count, historical duration, and current duration. Once a view is selected, hover over any node to reveal all available metrics.
Users of the widget can cycle through preconfigured [metric views](#metric-views), including historical count, current count, historical duration, and current duration. Once a view is selected, hover over any node to reveal all available metrics.
![Widget views selector at the bottom of the graph.](/docs/resources/foundry/machinery/widget-views.png)
Additionally, select a node metric to pin it and keep the metrics visible for review, or select again to unpin.
Additionally, select a node metric to pin it and keep the metrics visible for review, or select again to unpin.
![Select a node metric to pin it. To unpin, select the pin icon.](/docs/resources/foundry/machinery/node-pinning.png)
### Process-conformance filtering
By default, the widget only displays processes that conform to your process definition:
By default, the widget only displays processes that conform to your process definition:
* States and transitions that are not present in Machinery are excluded.
* Metrics are computed only over conforming processes.
* If any log object type on the graph contains more than 1M objects, conformance filtering is disabled and the graph will cover all input objects including metrics computation and output object sets.
* States and transitions that are not present in Machinery are excluded.
* Metrics are computed only over conforming processes.
* If any log object type on the graph contains more than 1M objects, conformance filtering is disabled and the graph will cover all input objects including metrics computation and output object sets.
### Focus into a parent process
在图表上，您可以聚焦到所需的父级 process 以缩小视图范围。

On a graph, you may focus into a desired parent process to narrow your view.
### Graph selection and outputs
与图表交互以筛选输出 object 集合：

Interact with the graph to filter output object sets:
* 选择节点以按 state 筛选 object。

* 选择边以按 transition 筛选 object。

* 输出 object 集合会根据您的选择自动更新。

* Select nodes to filter objects by state.
* Select edges to filter objects by transitions.
* Output object sets update automatically based on your selection.
### Graph features
以下图表功能可以在 widget 头部单独启用或禁用。

The following graph features may be enabled or disabled individually in the widget header.
* **Transition 节点：** 当您的图表包含在 Machinery 应用程序中配置的 action 或 automation 时，Machinery widget 将把它们替换为隐式的 state transition，以帮助您从 state-transition 的角度理解该 process。您可以选择显示 transition 节点，并可以在 widget 配置中配置默认行为。

* **Subprocess：** 如果图表包含 subprocess，您可以将这些 subprocess 替换为其隐式的 state transition，以便您可以在当前聚焦的 process 上查看 transition 指标。

* **Deviation：** 如果您当前的数据包含偏离的 object，则默认情况下它们是隐藏的。偏离的 object 是指那些采用了 process 定义中未包含的 state 或 transition 的 object。您可以将它们设置为不可见，并独立选择是否将它们包含在 widget 输出中。

* **Transition nodes:** When your graph includes actions or automations as configured in the Machinery application, the Machinery widget will replace them with implicit state transitions to help you understand the process from a state-transition perspective. You can choose to show the transition nodes instead, and configure default behavior in the widget configuration.
* **Subprocesses:** If the graph has subprocesses, you can replace these subprocesses with their implicit state transitions to allow you to see transition metrics on the currently focused process.
* **Deviations:** If your current data has deviating objects, they are hidden by default. Deviating objects are those that take any states or transitions that are not included in the process definition. You can make them invisible and independently choose whether they are included in the widget output.
### Analysis modes
打开 Machinery 图表后，您可以在位于图表右侧的 path explorer 功能和 duration distribution 功能之间切换。所选功能将在右侧打开。

With the Machinery graph open, you can toggle between the path explorer feature and the duration distribution feature located on the right side of the graph. The selected feature will open on the right side.
![From the right side of your graph, choose between the path explorer or duration distribution filter.](/docs/resources/foundry/machinery/widget-filtering-views.png)
#### Path explorer
使用 path explorer 功能一次分析一个 process 的各个 process 路径及其频率。要打开 path explorer，请选择位于图表右侧的 path explorer 图标。

Analyze individual process paths and their frequency using the path explorer feature for one process at a time. To open path explorer, select the path explorer icon located on the right side of the graph.
Path explorer 显示当前聚焦的 process 所采用的所有路径，并显示路径频率分布（完成该路径的 object 频率）。

Path explorer displays all paths taken by the currently focused process, and shows the path frequency distribution (the frequency of objects completing the path).
将鼠标悬停在窗口中的某条路径上，可在图表上将其高亮显示。您也可以选择一条或多条路径以筛选输出。

Hover over a path in the window to see it highlighted on your graph. You may also select one or more paths to filter the output.
![Path explorer pane on the right side of the graph.](/docs/resources/foundry/machinery/widget-path-explorer.png)
请注意，当 path explorer 打开时，路径选择将控制 widget 输出，并覆盖先前的节点/边选择。

Note that when path explorer is open, path selection controls the widget output and overrides previous node/edge selection.
#### Duration distribution
使用 duration distribution 筛选器来识别性能异常值并分析在 state 中花费的时间。

Use the duration distribution filter to identify performance outliers and analyze time spent in states.
持续时间图表会响应图表上的选择，并遵循配置的节点和边选择选项。

The duration chart responds to selection on the graph and follows configured node and edge selection options.
选择单个 bucket 或一段 bucket 范围将筛选输出 object 集合。您可以将图表选择与图表选择相结合，以查找具有不良行为的 object，例如在单个 transition 或 state 中耗时过长。

Selecting individual buckets or a range of buckets will filter the output object set. You can combine chart selection with graph selection to find objects with undesirable behavior, such as taking too long in an individual transition or state.
![View the duration distribution to learn how long it takes objects to pass through between states.](/docs/resources/foundry/machinery/widget-duration-distribution.png)