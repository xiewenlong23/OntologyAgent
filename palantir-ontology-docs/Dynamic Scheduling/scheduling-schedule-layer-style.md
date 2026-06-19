<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-schedule-layer-style/
---
# Schedule layer (puck) styling
Schedule layer 默认在 Gantt chart 上以 "puck" 形式呈现。这些 puck 可以代表工作流中的不同概念，并可进行自定义以创建一组动态的可视化效果。

Schedule layers are rendered by default as "pucks" on the Gantt chart. These pucks can represent different concepts of your workflow and be customized to create a dynamic set of visualizations.
自定义 schedule layer（或 "puck"）的外观有三种方式：

There are three ways to customize the appearance of your schedule layer (or "pucks"):
1. **Puck Style**
2. **Coloring**
3. **Properties**
1. **Puck Style**
2. **Coloring**
3. **Properties**
您还可以选择 **Puck style** 来更改 schedule layer 中 puck 的可视化呈现方式。

You can also select a **Puck style** to change the visual representation of the pucks in your schedule layer.
## 1. Puck style
选择 **Puck style** 可以更改 layer 中 puck 的可视化呈现方式。共有三种 puck style 可供配置：

Selecting a **Puck style** allows you to change the visual representation of pucks in your layer. Three puck styles are available for configuration:

> 📷 **[图片: Schedule layer example styling.]**

> 📷 **[图片: Schedule layer example styling.]**

* **Standard：**
* Standard 样式在 Gantt chart 上呈现为矩形 puck，可通过鼠标交互进行操作。

* 您可以选择性地提供 puck 高度，以确定 puck 的厚度。由于该高度由 Workshop variable 支持，您还可以将该 variable 暴露给终端用户，使其能够按需更改 puck 高度。

* puck 高度的常见用途包括：

* 使用 "thin" puck 表示随时间变化的状态。

* 使用 "thin" puck 表示较不重要或次要的信息集合。

* 使用 "thick" puck 表示关于相应事件的 "card" 信息。

* **Standard:**
* Standard styling renders a rectangular puck on your Gantt chart that can be interacted with via mouse interactions.
* Optionally, you can provide a puck height to determine the thickness of your puck. As this is backed by a Workshop variable, you can also expose this variable to end users and enable them to change the puck height on demand.
* Common uses of puck height include:
* Using a "thin" puck to represent a status over time.
* Using a "thin" puck to represent a less important or secondary set of information.
* Using a "thick" puck to represent a "card" of information about the respective event.
* **Background：**
* Background 样式在 Gantt chart 上呈现为略带透明的 puck，无法通过鼠标交互进行操作。

* Background puck 不支持 Rules。

* Background puck 的常见用途包括：

* 使用 background puck 表示可用性（例如：以绿色和红色进行颜色编码）。

* 使用 background puck 表示阶段或状态。

* 使用 background puck 表示偏好设置。

* **Background:**
* Background styling renders a slightly transparent puck on your Gantt chart that cannot be interacted with via mouse interactions.
* Background pucks do not support Rules.
* Common uses of background pucks include:
* Using a background puck to represent availability (for example: green and red color-coded).
* Using a background puck to represent phases or statuses.
* Using a background puck to represent preferences.
* **事件 (Event):**

* 事件样式在 Gantt 图表上渲染一个时间点标记，表示单个时间戳而不是时间范围。

* 事件 puck 不支持拖放或 Rules。
* 以下选项可用：

* **Is global（是否全局）：** 启用后，事件将延伸至图表中的所有行。

* **Always open（始终展开）：** 启用后，事件标志将始终处于展开状态。

* **Icon（图标）：** 选择一个标准图标或由 Media Reference property 支持的自定义图标。

* **Event:**
* Event styling renders a point-in-time marker on the Gantt chart, representing a single timestamp rather than a time range.
* Event pucks do not support drag-and-drop or Rules.
* The following options are available:
* **Is global:** When enabled, the event extends across all rows in the chart.
* **Always open:** When enabled, event flags are always expanded.
* **Icon:** Select a standard icon or a custom icon backed by a Media Reference property.
## 2. Coloring
您可以为每个 schedule layer 定义颜色定义。选项包括：**Static（静态）**、**Segmented by（按...分段）** 和 **Conditional（条件）** 着色。

You can define the color definition for each schedule layer. Options include: **Static**, **Segmented by**, and **Conditional** coloring.
## 3. Properties
对于每个 schedule layer，您可以定义来自 ontology 的 properties，这些 properties 将直接显示在 puck 上或 popover 卡片上。

For each schedule layer, you can define the properties from the ontology that will appear directly on the puck or on the popover card.
* Popover properties（弹出框属性）：

* 从您的 schedule layer 的 object、其 linked objects 中选择 properties，或使用 function-backed property。

* 您可以选择重命名或删除显示名称。Property formatting 与 Ontology Manager 中的 property configuration 一同配置。

* 这些 properties 将显示在 popover 卡片上。当鼠标悬停在 puck 上时，会出现 popover 卡片。

* Popover properties:
* Select properties from your schedule layer's object, its linked objects, or use a function-backed property.
* You can choose to rename or remove the display name. Property formatting is configured alongside the property configuration in Ontology Manager.
* These properties will appear on the popover card. The popover card appears when a puck is hovered-over.
* Puck properties（Puck 属性）：

* 从您的 schedule layer 的 object、其 linked objects 中选择 properties，或使用 function-backed property。

* 您可以选择重命名或删除显示名称。Property formatting 与 Ontology Manager 中的 property configuration 一同配置。

* 这些 properties 将直接显示在 puck 上。如果所有选定的 properties 无法全部放入 puck 中，您可能需要使用上述 **Puck styling > Standard > Variable height** 选项来调整 puck 的高度。

* Puck properties:
* Select properties from your schedule layer's object, its linked objects, or use a function-backed property.
* You can choose to rename or remove the display name. Property formatting is configured alongside the property configuration in Ontology Manager.
* These properties will appear directly on the puck. If all selected properties cannot fit on the puck, you may need to adjust the height of your puck using the **Puck styling > Standard > Variable height** option described above.