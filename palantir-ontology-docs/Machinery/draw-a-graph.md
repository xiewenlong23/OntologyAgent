<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/machinery/draw-a-graph/
---
# Draw a Machinery process
要使用 Machinery 应用程序创建 Process 的 Model，您可以通过 [process mining](/docs/foundry/machinery/process-mining/) 从历史观测中自动派生 Process Model，也可以通过绘制状态和转换来手动定义 Process。

To create a model of a process using the Machinery application, you can derive a process model automatically from historical observations by [process mining](/docs/foundry/machinery/process-mining/), or you can define a process manually by drawing states and transitions.
在以下情况下，您可能需要使用手动 Process 绘制工具：当您心中有一个想要建模并图形化展示的物理 Process 时，或者当您需要修改和增强现有的 Process Model 时。

You may want to use the manual process drawing tools in situations when you have a physical process in mind that you want to model and visualize graphically, or when you need to modify and enhance an existing process model.
从 Machinery 资源的空白画布开始，手动绘制 Process 的第一步是创建一个 Process container。该 container 用于表示特定类型的实体及其状态；例如，一个 `Claim`。如果存在多个相互作用的实体，您可以添加更多的 Process container，使其并行或嵌套在其他 container 中。

From the blank canvas of a Machinery resource, your first step in manual process drawing is to create a process container. The container is used to represent a specific type of entity and its states; for instance, a `Claim`. If there are multiple entities interacting with each other, you may add further process containers, either in parallel or nested within others.
![Drawing a new process on a blank canvas.](/docs/resources/foundry/machinery/drawing-1.png)
为了获得更好的编辑体验，您可以通过选择全屏选项将视图聚焦于某个 Process container，使其及其子项填满整个画布。要退出全屏聚焦，您可以使用 **Navigation** 面板更改视图。

For a better editing experience, you can focus your view on a process container by selecting the fullscreen option to have the process container and its children fill the entire canvas. To revert from  fullscreen focus, you can change your view by using the **Navigation** panel.
所有绘制交互都可以通过 Process container 上的 actions 或在 Process 处于焦点状态时通过主工具栏进行访问。

All drawing interactions are available through actions on the process container, or from the main toolbar when a process is in focus.
![Process main toolbar.](/docs/resources/foundry/machinery/drawing-2.png)
## Adding states, actions, and automations
构建 Process 的典型模式是从初始状态开始，绘制后续状态，然后在它们之间添加 actions 和 automations。

A typical pattern for building out a process is to start with an initial state, draw subsequent states, and then add actions and automations in between.

> 📷 **[图片: Add a state, action, or automation onto your canvas.]**

> 📷 **[图片: Add a state, action, or automation onto your canvas.]**

或者，您也可以从一系列 actions 开始，然后稍后填充状态。

Alternatively, you can start with a sequence of actions and fill in the states later.
状态之间的边表示状态转换。当将 actions 或 automations 连接到状态时，这些边遵循以下语义：

Edges between states denote state transitions. When connecting actions or automations to states, these edges follow the semantics below:
* **Input States（输入状态）：** Action 之前 Object 允许所处的状态。对于 Foundry actions，可以通过 [submission criteria](/docs/foundry/action-types/submission-criteria/) 来强制执行此条件。您可以在 action 节点的 **Details** 面板中检查现有的 submission criteria。

* **Input States:** Allowed states of objects prior to the action. For Foundry actions, this can be enforced through [submission criteria](/docs/foundry/action-types/submission-criteria/). You can inspect existing submission criteria in the **Details** panel of action nodes.
* **Output States（输出状态）：** Action 之后可能产生的结果状态。例如，一个 *extract entities* 的 action 可以产生 *extraction succeeded* 或 *extraction failed*。Output States 无法被强制执行；但是，可以通过在 Machinery 中查看 action 逻辑来手动验证 output states。

* **Output States:** Possible resulting states after the action. For instance, an action to *extract entities* can result in *extraction succeeded* or *extraction failed*. Output states cannot be enforced; however, output states can be manually validated by reviewing the action logic in Machinery.
* **Automations：** 当达到其某个 input state 时自动触发的 action 表示。Automations 还可以发送 notifications，这些 notifications 描述了状态的 *side effect*（副作用）。

* **Automations:** A representation of an action that is automatically triggered when one of its input states is reached. Automations can also send notifications, which describe a *side effect* of a state.
可以通过选择元素并使用垃圾桶图标或按键盘上的退格键来删除节点和边。

Nodes and edges can be deleted by selecting the element and using the trash can icon or pressing backspace on your keyboard.
一旦你选择了一个 [process ontology](/docs/foundry/machinery/connect-data/)，状态名称就代表你的 Object Type 的 `state` Property 的值。在 Machinery 中更改状态的名称不会更改数据中的值。你还可以将具体的 Action 或自动化链接到图上的元素。通过这样做，你可以逐步将你的 process model 转变为 process implementation。

Once you have chosen a [process ontology](/docs/foundry/machinery/connect-data/), the state names represent values of the `state` property of your object types. Changing the name of a state in Machinery does not change values in your data. You can also link concrete actions or automations to the elements on the graph. In doing so, you can gradually turn your process model into a process implementation.
## Auto-layout feature
Machinery 的 **auto-layout** 功能默认启用。当你添加或连接节点时，它们会自动定位，使图保持从左到右的 process flow 排列。

Machinery’s **auto-layout** feature is enabled by default. Nodes are automatically positioned as you add or connect them, keeping the graph organized in a left-to-right process flow.

> 📷 **[图片: Autolayout option.]**

> 📷 **[图片: Autolayout option.]**

你可以通过上下拖动来影响同一"层"内节点的垂直排序。

You can influence the vertical ordering of nodes of the same “layer” by dragging them up or down.
如果你的过程中存在循环，你可以通过将任意节点向左拖动来选择优先放置哪些节点。其余的布局将相应地进行调整。

If there are loops in your process, you can choose which nodes to place first by dragging any node leftward. The rest of the layout will adapt accordingly.
如果 auto-layout 功能无法产生令人满意的结果，你也可以选择将其关闭。关闭该功能后，你可以在图上自由移动节点。

You may also choose to toggle off the auto-layout feature if it does not produce satisfactory results. Switching off the feature allows you to move nodes freely on the graph.
在手动布局模式下，你可能会用到位于左下角控制栏中的一次性布局选项来重新组织你的图。

During manual layout mode, you may benefit from the one-time layout option accessible in the control bar on the bottom left to reorganize your graph.
## Multiple object types
许多现实世界中的 process 涉及多个实体。你可以使用 process containers 来表示这些实体，并链接它们的状态和 Action。例如，一个 container 中的 Action 可能会影响另一个实体的 state，因此需要作为输出连接到这些 state。我们建议将 Action 放入将其作为输入的 object 所在的 container 中。

Many real-world processes involve multiple entities. You can represent those with process containers and link their states and actions. For instance, an action in one container may affect the state of another entity and therefore be connected to those states as outputs. We recommend placing actions into the container of the object that they take as input.