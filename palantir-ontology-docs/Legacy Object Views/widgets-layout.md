<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/widgets-layout/
---
# Layout
**Layout widgets** 用于在特定 tab 内组织和构建 Object View 页面的布局，方法是将视图安排到不同的容器中。

**Layout widgets** are used to organize and structure the layout of an Object View page within a certain tab, by arranging the view into different containers.
每个 Object View 可以具有三个层级的布局控制：

Each Object View can have three levels of Layout control:
* Tabs，其功能集在 [Configuring Tabs](/docs/foundry/object-views/config-tabs/) 中描述

* Tab 内的 Layout Widgets（也称为 Containers），使您能够在内容框内组织 Object View。

* 所有 content widgets（可视化、properties 和 links、filters 等），它们是 Object View 的构建块。

* Tabs, with a set of functionalities described on [Configuring Tabs](/docs/foundry/object-views/config-tabs/)
* Layout Widgets within a tab (also called Containers), enabling you to organize the Object View within boxes of content.
* All content widgets (visualization, properties and links, filters, etc.), which are the building blocks of the Object View.
以下是 Layout 容器的类型：

These are the types of Layout containers:
* 页面的视觉设计 - [Horizontal Distribution](#horizontal-distribution) 和 [Vertical Stack Container](#vertical-stack-container)。

* 在 tab 内嵌套另一层级的内容 - [Tabbed Container](#tabbed-container)。

* 根据用户交互的 [filters](/docs/foundry/object-views/widgets-filtering/) 启用内容的显示/隐藏 - [Conditional Container](#conditional-container)。

* 显示带有 object 值富集效果的文本 - [Markdown](#markdown) widget。

* Visual design of the page - [Horizontal Distribution](#horizontal-distribution) and [Vertical Stack Container](#vertical-stack-container).
* Add another level of content nested within a tab - [Tabbed Container](#tabbed-container).
* Enable displaying/hiding content according to [filters](/docs/foundry/object-views/widgets-filtering/) that the user interacts with - [Conditional Container](#conditional-container).
* Display text, enriched with object values - [Markdown](#markdown) widget.
## Horizontal Distribution
此 widget 使您能够通过将 widget 水平分布在一个容器中（一个接一个地排列）来以可视化方式组织 Object View 的布局。它只是其他 widget 的容器，本身没有其他功能。

This widget enables you to organize the layout of your Object View visually by displaying widgets distributed horizontally within a container, one next to the other. It is just a container of other widgets, and has no other functionality by itself.
### Configuration
添加 Horizontal Distribution widget 后，配置使您能够通过点击 "Add Item" 在此容器内添加不同的 widget，这将打开 widget 选择器。

Once you add the Horizontal Distribution widget, the configuration enables you to add different widgets within this container, by clicking on “Add Item”, which would open up the widget selector.
有两种选项可以确定容器内每个 widget 将分配多少宽度：

There are two options to determine how much width would be allocated to each widget within the container:
* Relative - 为容器内的每个 widget 选择一个整数。Widget 根据其相对数字进行分布。示例：3 个 widget，大小分别为 A=1，B=3，C=2；Widget A 将占 1/6 的长度，Widget B 将占 3/6 的长度。

* Pixel - 为每个 widget 选择绝对像素数。如果像素总和超过 Object View 限制（约 1150 像素），widget 将 "溢出" 页面。

* Relative - choose an integer number for each widget within the container. Widgets are distributed according to their relative number. Example: 3 widgets of sizes A=1, B=3, C=2; Widget A would take 1/6 of the length and widget B would take 3/6 of the length.
* Pixel - choose an absolute number of pixels to allocate to each widget. If the sum of pixels exceeds Object View limits (about 1150 pixels), widgets will “spill out” of the page.
**常见问题和注意事项：**

**Common Issues and Notes:**
* 确保为 Horizontal Distribution widget 添加标题，这是能够添加它的强制要求。标题将显示在 widget 标头上。

* Make sure to add a title to the Horizontal Distribution widget, which is mandatory to be able to add it. The title will be displayed on the widget header.
## Vertical Stack Container
此 widget 使您能够通过将 widget 垂直分布在一个容器中（堆叠在彼此之上）来以可视化方式组织 Object View 的布局。它只是其他 widget 的容器，本身没有独立的功能。

This widget enables you to organize the layout of your Object View visually by displaying widgets distributed vertically within a container, stacked one on top of the other. It is just a container of other widgets, and has no stand-alone functionality by itself.
### Configuration
添加 Vertical Stack Container widget 后，配置使您能够通过点击 "Add Item" 在此容器内添加不同的 widget，这将打开 widget 选择器。

Once you add the Vertical Stack Container widget, the configuration enables you to add different widgets within this container, by clicking on “Add Item”, which would open up the widget selector.
**常见问题与注意事项：**

**Common Issues and Notes:**
* 请确保为 Vertical Stack Container widget 添加标题,这是添加该 widget 的必要条件。

* 若要将 Vertical Stack Container 与其他 widget 对齐,请在配置中进入 "Format" 选项卡,选择 Left/Right 对齐方式,而不是默认的 "Full Width"。

* 通过配置中 "Settings" 下每个选项卡旁边的上下箭头调整选项卡的顺序。此操作还可用于删除选项卡或替换每个选项卡内的 widget。

* Make sure to add a title to the Vertical Stack Container widget, which is mandatory to be able to add it.
* To align the Vertical Stack Container next to other widgets, go to “Format” tab in the configuration and select a Left/Right alignment, instead of the default “Full Width”.
* Choose the order of the tabs by using the up/down arrows next to each tab under “Settings” in the configuration. This also allows you to delete tabs or replace the widget within each tab.

> 📷 **[图片: Vertical stack container]**

> 📷 **[图片: Vertical stack container]**

## Tabbed Container
通过在当前选项卡内创建一个选项卡容器,为您的 Object View 添加另一层选项卡。用户可以在这些选项卡之间浏览,每个选项卡包含一个 widget(也可以是包含多个 widget 的容器)。

Add another layer of tabs to your Object View, by creating a container of tabs within the current tab. Users can browse between these tabs, each one containing a single widget (which can also be a container of a number of widgets).
Tabbed Container 只是一个包含其他 widget 的容器,本身没有独立的功能。

The Tabbed Container is just a container of other widgets, and has no stand-alone functionality by itself.
### Configuration
* 添加 Tabbed Container widget 后,配置允许您通过点击 "Add Tab" 在此容器内添加不同的 widget 选项卡,这将打开 widget 选择器。

* 每个选项卡的名称就是该选项卡上 widget 的标题,显示在配置中的 "Format" 下。

* 通过配置中 "Settings" 下每个选项卡旁边的上下箭头调整选项卡的顺序。此操作还可用于删除选项卡或替换每个选项卡内的 widget。

* Once you add the Tabbed Container widget, the configuration enables you to add different tabs of widgets within this container, by clicking on “Add Tab”, which would open up the widget selector.
* The name of each tab is the title of the widget on that tab, which appears under “Format” in the configuration.
* Choose the order of the tabs by using the up/down arrows next to each tab under “Settings” in the configuration. This also allows you to delete tabs or replace the widget within each tab.

> 📷 **[图片: tabs]**

> 📷 **[图片: tabs]**

**常见问题与注意事项：**

**Common Issues and Notes:**
* 在 ontology 中的中心对象上有时需要使用此选项卡。但请注意,它会增加用户体验的复杂性,即"选项卡中的选项卡"。

* 请确保为 Tabbed Container widget 添加标题,这是添加该 widget 的必要条件。标题将显示在 widget 头部。

* Using this tab is sometimes necessary in central objects in the ontology. However, be mindful that it adds complexity to the user experience, with “tabs within a tab”.
* Make sure to add a title to the Tabbed Container widget, which is mandatory to be able to add it. The title will be displayed on the widget header.
## Conditional Container
条件容器使内容能够根据条件显示或隐藏。该条件可以基于：

A conditional container enables content to be displayed or hidden according to a condition. This condition can be based on:
* 用户在 Object View 上应用的 Filters

* 对象或 Linked 对象的 Property 值

* 特定类型 Linked 对象的存在

* Filters that the user applies on the Object View
* Property values of the object or a linked object
* The existence of linked objects of a certain type
### Configuration
此 widget 支持添加一个或多个 *conditional sections*(条件部分)。这些部分中的每一个都包含一个 *condition*(条件)和一个或多个根据该条件 *conditionally displayed*(条件显示)的 widget。要设置条件部分,请按以下三个步骤操作：

This widget supports adding one or several *conditional sections*. Each one of these sections includes a *condition* and one or more widgets that are *conditionally displayed* according to that condition. To set up a conditional section, you follow these three steps:
**Step 1 – 设置条件**

**Step 1 – Set the condition**
第一步是根据条件定义容器内容的显示或隐藏。共有三种不同类型的条件：

The first step is to define the condition according to which the contents of the container should be displayed or hidden. There are three different types of conditions:
***条件 1 – Filters***

***Condition 1 – Filters***
*Filters* 条件根据 Object View 上是否应用了筛选条件来显示或隐藏容器的内容。此条件可以通过三种不同的方式进行配置：

The *Filters* condition displays or hides the contents of the container based on whether or not filters are applied to the Object View. This condition can be configured in three different ways:
* **Specific Filter** – 仅当在特定 property 上应用了筛选条件时,才会显示容器的内容。该 property 可以是当前视图中对象的 property,也可以是 linked object 的 property。这意味着要使用此条件,必须存在另一个 Filter Widget,其筛选的对象和 property 与此条件中定义的对象和 property 完全相同。

* *Example*:配置一个 Airport 的 Object View,有一个筛选条件用于仅保留已取消的 Flights(Status = "Cancelled")。一个显示已取消航班详情的 Conditional Container 被配置为仅在应用了此特定筛选条件时才显示。

* *Note*:为了使此条件类型生效,需要在 "Filter linked object" 和 "Filter property" 的下拉列表中选择相同的 object type。

* **No Filter** – 仅当当前 tab 或任何与该 tab 共享 cross-filters 的 tab 中未应用任何筛选条件时,才会显示该容器。可以是任何类型的筛选条件,例如 date filter、dropdown filter、button filter 等。

* **Any Filter** – 仅当当前 tab 或任何与该 tab 共享 cross-filters 的 tab 中至少应用了一个筛选条件时,才会显示该容器。与 *No Filter* 一样,这可以是任何类型的筛选条件,例如 date filter、dropdown filter、button filter 等。

* **Specific Filter** – The contents of the container are displayed only when there is a filter applied on a specific property. That property can either be a property of the current object in view or of a linked object. This means that in order to use this condition, there must be another Filter Widget which filters specifically on the same object and property as defined in this condition.
* *Example*: Configuring an Object View of an Airport, there is a filter to keep only Flights that were cancelled (Status = “Cancelled”). A Conditional Container, showing details on cancelled flights, is configured to be displayed only when such a specific filter is applied.
* *Note*: In order for this condition type to work, the same object type needs to be selected in the dropdowns for "Filter linked object" and "Filter property".
* **No Filter** – The container is displayed only when no filter is applied within the current tab or any tab sharing cross-filters with this tab. This can be any type of filter, e.g. a date filter, a dropdown filter, a button filter, etc.
* **Any Filter** – The container is displayed only when at least one filter is applied within the current tab or any tab sharing cross-filters with this tab. Just as for *No Filter*, this can be any type of filter, e.g. a date filter, a dropdown filter, a button filter, etc.
***Condition 2 – Properties***
***Condition 2 – Properties***
*Properties* 条件根据对象 property 的值来显示或隐藏容器的内容。所讨论的对象可以是当前视图中对象,也可以是 linked object。对于 linked object 的情况,与当前对象的关系必须是 *1-to-1* 或 *many-to-1*,在后一种情况下,当前对象需要位于关系的 "many" 一侧。

The *Properties* condition displays or hides the content of the container based on the value of a property of an object. The object in question can either be the current object in view or a linked object. In the case of a linked object, the relationship to the current object needs to be either *1-to-1* or *many-to-1*, in which case the current object needs to be on the "many" side of the relationship.
要使用此条件类型,首先需要选择要使用的 property。接下来,根据该 property 定义何时应显示 conditional container 的内容。对此有四个选项:

To use this condition type, you first select the property you want to use. Next, you define when the contents of the conditional container should be shown based on that property. There are four options for this:
* **Is defined** – property 的值不是 `null`。

* **Is not defined** – property 的值是 `null`。

* **Is one of** – property 的值与您定义的某个值匹配。

* **Is not one of** – property 的值*不*与您定义的任何值匹配。

* **Is defined** – The value of the property is not `null`.
* **Is not defined** – The value of the property is `null`.
* **Is one of** – The value of the property matches one of the values that you define.
* **Is not one of** – The value of the property *does not* match one of the values that you define.
对于 **is one of** 和 **is not one of**,您定义的值会被转换以匹配 property 类型(如果它是 integer、double、date 或 boolean)。有关此 property 比较如何执行的更多详细信息,请参见下文。

For **is one of** and **is not one of**, the values you define are translated to match the property type (if it’s integer, double, date or boolean). See below for more details on how this property comparison is done.
***Condition 3 – Linked Objects***
***Condition 3 – Linked Objects***
*Linked Objects* 条件根据是否存在某种类型的 linked objects 来显示或隐藏容器的内容。要设置此条件,首先需要选择一个 link path。然后,决定当所选路径的 linked objects *存在* 或 *不存在* 时,是否应显示 conditional container 的内容。

The *Linked Objects* condition displays or hides the contents of the container based on the existence of linked objects of a certain type. To set up this condition, you first select a link path. Then, you decide if the contents of the conditional container should be shown if linked objects of the selected path *exist* or *do not exist*.
可以通过将其与 Linked Objects View 进行比较来推理此条件的逻辑。如果具有相同 link path 的 Linked Objects View 会显示至少一个对象(如果 linked objects 应该*存在*),或不显示任何对象(如果 linked objects 应该*不存在*),则仅应显示具有此条件的容器的内容。

The logic of this condition can be reasoned about by comparing it to a Linked Objects View. The contents of a container with this condition should only be shown if a Linked Objects View with the same link path would show at least one object (if linked objects should *exist*), or no objects (if linked objects should *not exist*).
**Step 2 – Add Widgets**
**Step 2 – Add Widgets**
定义条件之后,第二步是配置要在容器内显示的实际内容。单击 "Add Section" 按钮并根据需要添加任意数量的 widget。请注意,可以使用上下箭头来排列 Conditional Container 中显示的 widget 顺序。

Once a condition has been defined, the second step is to configure the actual content to be displayed within the container. Click on the “Add Section” button and add as many widgets as needed. Note that you can order the widgets displayed within the Conditional Container by using the up/down arrows.
**Step 3 – Choose a Layout**
**Step 3 – Choose a Layout**
最后,第三步也是最后一步,是为容器选择 layout。layout 可以是:

Finally, the third and final step is to choose the layout of the container. The layout can be either:
* **Horizontal** – Widget 从左到右显示,类似于 Horizontal Distribution Container widget

* **Vertical** – Widget 从上到下显示,类似于 Vertical Stack Container widget

* **Horizontal** – Widgets are displayed from left to right, like the Horizontal Distribution Container widget
* **Vertical** – Widgets are displayed from top to bottom, like the Vertical Stack Container widget
完成这三个步骤后，你的 Conditional Container 应该已经设置完成，可以正常使用了！

After completing these three steps, your Conditional Container should be set up and good to go!
**常见问题和注意事项：**

**Common Issues and Notes:**
* 属性值比较是如何进行的？
* 字符串值按常规方式匹配

* 对于数值型 property，widget 中所有输入值都会被转换为数字并与数值型 property 进行比较（例如，输入字符串 3.1415 会被转换为 double 类型）

* 对于 boolean 型 property，如果你在 widget 中使用 "true"、"yes" 和 "1"，它们都被视为真值（truth input values），其余所有值都为假。
* 日期和时间戳值在字符串转换后进行匹配
* 数组类型目前不支持

* 如果添加了多个条件，条件会按照从上到下的顺序进行求值——第一个满足条件的 section 将被渲染，其余的将被忽略。

* 按属性值条件渲染的 conditional container 适用于 1-to-1 或 many-to-1 的关系，其中当前展示的 object 位于关联端（即 "many" 端）。

* 它*不*支持 many-to-many 或 1-to-many 的关系条件（其中当前 object 位于主端），也*不*支持通过 Linked Objects 中值的聚合来进行条件可见性控制。

* *示例*：查看一个 aircraft object 时，我可以添加一个条件，依赖于它所属的航空公司（假设它只属于一个航空公司），但我不能添加一个依赖于"它是否有一个具有 property X 的 linked flight object"这样的条件。

* 该 widget 是 tab 级别可选 "Visibility" 配置的扩展，但位于 widget 级别。然而，它并非完全等价：

* "Visibility" 使你能够根据用户 profile 定义条件性 tab。

* 该 widget 允许你在 (1) 单一 tab 内设置条件视图；(2) 提供基于已应用过滤器的条件可见性选项（取决于用户交互）；(3) 不包含按用户 profile 的条件视图。

* 若要启用条件 section 选项以根据已应用的过滤器进行显示/隐藏，请确保在右侧栏配置编辑器的 "Settings" 下勾选 "cross-filtering" 复选框。

* Conditional Container 只是其他 widget 的容器，可以按水平或垂直方向进行分布。

* How is the property value comparison done?
* String values are matched normally
* For numeric properties, all input values in the widget are turned into numbers and compared to the numeric property (e.g. enter the string 3.1415 and it would turn to a double)
* For boolean properties, if you use “true”, “yes” and “1” in the widget, they are all considered truth input values, all the rest is false.
* Date and timestamp values are matched after string conversion
* Arrays are currently not supported
* If several conditions are added, conditions are evaluated from top to bottom - the sections of the first condition met will be rendered, and the others ignored.
* The conditional container by property value option works on either a 1-to-1 or many-to-1 relationship, where the current object in display is on the related side (the “many”).
* It *does not* allow conditions of many-to-many or 1-to-many where the current objet is on the primary side, and it *does not* allow conditional visibility by aggregations of values in Linked objects.
* *Example*: looking at an aircraft object, I could add a condition dependent on what airline it belongs to (assuming it belongs to only one airline), but I can’t add a condition dependent on “does it have a linked flight object with property X?”
* This widget is an extension of the tab-level optional “Visibility” configuration, but at the widget level. However, it is not a complete equivalent:
* “Visibility” enables you to define conditional tabs according to users profiles.
* This widget allows you to set conditional views (1) within a single tab; (2) option of conditional visibility by applied filters (dependent on user’s interaction); (3) does not include conditional view per users profiles.
* In order to enable the conditional section option to display/hide by filters applied, make sure to mark the checkbox of “cross-filtering” on the right-bar configuration editor, under “Settings”.
* The Conditional Container is only a container of other widgets, distributed either horizontally or vertically.
## Markdown
该 widget 允许将富文本作为 Object View 布局的一部分添加。它提供了一个纯文本编辑器，基于 Markdown 轻量级富文本格式语法（`markdown-it` library）。此外，该 widget 还支持将 object properties 值作为文本的一部分进行模板化。

This widget enables adding rich text as a part of an Object View layout. It provides a plain text editor, based on the Markdown lightweight rich text formatting syntax (`markdown-it` library). As an addition, this widget allows templating of object properties values as part of the text.
![markdown hubble plugin 1](/docs/resources/foundry/object-views/widgets_markdown-hubble-plugin-1.png)
![markdown hubble plugin 2](/docs/resources/foundry/object-views/widgets_markdown-hubble-plugin-2.png)
### Configuration
* 文本框是一个简单的文本编辑器，支持标准的 `markdown-it` library。

* **Object properties 模板化** - 使用 {{propertyName}} 格式（双花括号），用当前 object properties 值为你的 Markdown 内容进行模板化。propertyName 是 [Ontology 中的 property](/docs/foundry/object-link-types/properties-overview/) 精确区分大小写的名称。{{objectId}}、{{objectTypeId}} 和 {{objectTypeRid}} 这些值同样受支持。

* The text box is a simple text editor, and supports the standard `markdown-it` library.
* **Object properties templating** - use the {{propertyName}} format, with double curly brackets, to template your Markdown content with the current object properties values. propertyName is the exact case-sensitive name of the [property in Ontology](/docs/foundry/object-link-types/properties-overview/). The values {{objectId}}, {{objectTypeId}} and {{objectTypeRid}} are also supported.
*其他配置*：

*Additional configurations*:
* 换行，提供 2 个选项：
* 启用换行 - 开启时（默认），编辑器中的单个换行符将作为实际换行生效；关闭时，编辑器中的换行符不会影响结果。使用标题格式仍然有效。

* 将 "\n" 转换为换行 - 将 `\n` 显示为换行（需要开启 "Enable line breaks"）。

* 启用安全 HTML 渲染 - 使用 markdown-it 进行安全 HTML 渲染。来自 object properties 的嵌入 HTML 会被禁用；所有 property 值都会被转义以确保安全。

* Line breaks, with 2 options:
* Enable line breaks - when on (default), a single line breaks in the editor works as an actual line break; when off, line break in the editor doesn’t affect the result. Using headers formats would still serve.
* Convert "\n" to line breaks - shows `\n` as a line-break (requires the "Enable line breaks" to be on).
* Enable sanitized HTML rendering - Safe HTML rendering with markdown-it. Embedding HTML from object properties are disabled; all property values are escaped for security.
**常见问题和注意事项：**

**Common Issues and Notes:**
* 目前，使用 {{propertyName}} 格式包含的长文本和数组可能会溢出文本框，并且默认情况下不会被渲染。

* Currently, long texts and arrays included using the {{propertyName}} format might spill out of the text box and are not rendered by default.