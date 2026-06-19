<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/view-results/
---
# View results
Results View（结果视图）以表格形式展示您探索中的对象。若要加载更多对象到表格中，请向下滚动。

The Results View displays objects from your exploration in a tabular view. To load more objects into the table, scroll down.
![Results View](/docs/resources/foundry/object-explorer/results_view.png)
## Sorting Table by Column
结果表格可以按照应用了 `Sortable` renderHint 的 Property（属性）进行排序。若要按特定列排序，请点击列标题中的下拉箭头。

The results table can be sorted by properties with the `Sortable` renderHint applied. To sort by a specific column, click the dropdown arrow in the column header.
![Column Options](/docs/resources/foundry/object-explorer/results_column_options.png)
一旦某列被用于排序，其标题中将显示一个排序图标。如果选择了多个列进行排序，则最后选择的列优先。之前的排序在其排序图标旁边会带有一个数字，以显示排序顺序，如下所示。

Once a column is used for sorting, it will display a sorting icon in its header. If multiple columns are chosen for sorting, the last one selected takes precedence. Previous sorts have a number next to their sorting icon to show the sort order, as below.

> 📷 **[图片: Column Sorting]**

> 📷 **[图片: Column Sorting]**

从下拉菜单中选择 "Clear All Sorts"（清除所有排序）以将排序重置为初始状态。

Select “Clear All Sorts” from the dropdown to reset your sorts to their original state.
## Configuring Columns
### Changing Column Order
可以通过拖动列标题上的手柄图标来重新排序列。

Columns can be re-ordered by dragging the handle icon on column headers.

> 📷 **[图片: Reordering Columns]**

> 📷 **[图片: Reordering Columns]**

用户可以从列标题下拉菜单中选择 "Freeze X columns" 选项,以便在结果表中向右滚动时保持最左侧的 X 列可见。复选框列包含在计数中。

Users can select the “Freeze X columns” option from a column header dropdown to keep the X leftmost columns visible while scrolling to the right in the results table. The checkbox column is included in the count.
### Resizing Columns
要调整列宽,请将列标题的右侧拖动到所需宽度。此边界(以蓝色高亮显示)正好位于配置下拉菜单的右侧。

To resize a column, drag the right side of the column header to the desired width. This boundary, highlighted blue, is just to the right of the configuration dropdown.

> 📷 **[图片: Resizing Columns]**

> 📷 **[图片: Resizing Columns]**

### Adding and Removing columns
要隐藏单个列,请从列标题下拉菜单中选择 "Hide this column" 选项。

To hide an individual column, select the “Hide this column” option from the column header dropdown.
要一次重新排序和配置多个列,请选择 "Configure columns" 以打开以下菜单。

To reorder and configure multiple columns at once, select “Configure columns” to open the following menu.

> 📷 **[图片: Configuring Columns]**

> 📷 **[图片: Configuring Columns]**

左侧面板显示表的默认列,而右侧面板显示所有可能列的当前顺序和可见性。使用快捷按钮隐藏或添加所有列,或使用顶部的搜索栏搜索特定列以切换其可见性。

The left-hand panel shows default columns for the table, while the right-hand panel displays the current order and visibility for all possible columns. Hide or add all columns using the shortcut buttons, or search for a specific column with the search bar at the top to toggle visibility.
通过将列拖动到所需位置来更改列顺序,或使用下面的菜单将列移动到顶部或底部。

Change column order by dragging the columns to the desired locations, or move the columns to top or bottom using the menu below.

> 📷 **[图片: Column Menu]**

> 📷 **[图片: Column Menu]**

选择 "don't truncate text in this table" 将导致文本 Property 如果无法在现有列宽中显示,则换行到下一行。

Selecting “don’t truncate text in this table” will cause text properties to wrap to the next line if they cannot be displayed in the existing column width.
使用右下角的按钮保存您的配置。管理员可以通过将当前视图另存为新布局并将其设置为所有用户的默认布局来更新此表的默认配置。[了解有关更新默认配置的更多信息。](/docs/foundry/object-explorer/configure/#default-layout-administrative-users)

Save your configuration with the button in the bottom right. Administrators can update the default configuration for this table by saving the current view as a new layout and setting it as the default for all users. [Learn more about updating the default configuration.](/docs/foundry/object-explorer/configure/#default-layout-administrative-users)
## Previewing Results
要在新的 Object Explorer 选项卡中打开某个 Object 的对象视图,请单击该 Object 所在行的 Title 列。要在 Results 选项卡中打开对象视图的预览,请通过单击复选框或相应行中的任何其他列来选择一个或多个 Object。

To open the object view for an object in a new Object Explorer tab, click the Title column for that object’s row. To open a preview of the object view in your Results tab, select one or more objects by clicking the checkbox or any other column in the corresponding row.
选择 Object 后,Selection Preview 面板将从右侧打开。要关闭此面板以查看完整表格,请使用面板左上角的 "collapse" 图标 (

> 📷 **[图片: Collapse icon]**

)。
After selecting an object, the Selection Preview panel will open from the right. To close this panel for a full table view, use the "collapse" icon (

> 📷 **[图片: Collapse icon]**

) on the top left of the panel.
![Results Preview](/docs/resources/foundry/object-explorer/results_results_preview.png)
如果选择了多个 object，则前二十个 object 中任何一个的 object view 都可以进行预览，显示在 object view 上方的卡片列表中。

If multiple objects are selected, the object view for any of the first twenty is available for previewing, displayed in a list of cards above the object view.
![Results Preview](/docs/resources/foundry/object-explorer/results_results_preview_multiselect.png)
要同时比较两个 object 的 object view，请选择右上角的下拉菜单并选择"Compare objects"。

To compare object views for two objects at once, select the top right dropdown and choose “Compare objects”.
![Results Comparison](/docs/resources/foundry/object-explorer/results_results_preview_compare.png)
### Viewing time series properties
Time series property 可以与常规 property 一起在 Results View 中查看。Time series property 是一种 object property，用于存储带时间戳的值的历史记录。[了解更多关于 time series property 的信息。](/docs/foundry/time-series/time-series-concepts-glossary/#time-series-property-tsp)

Time series properties can be viewed alongside regular properties in the Results View. A time series property is an object property which stores a history of timestamped values. [Learn more about time series properties.](/docs/foundry/time-series/time-series-concepts-glossary/#time-series-property-tsp)
在下面的示例中，Results View 显示了 `Country` object，它包含三个 time series property：`COVID19 New Tests`、`COVID19 New Deaths` 和 `COVID19 New Cases`。每一列在左侧显示 time series 中最新的观测值，在右侧显示可视化 time series 历史的迷你图。

In the example below, the Results View displays the `Country` object, which contains three time series properties: `COVID19 New Tests`, `COVID19 New Deaths`, and `COVID19 New Cases`. Each column displays the most recent observation in the time series on the left, and a sparkline visualizing the history of the time series on the right.
![Time-dependent property in Results View](/docs/resources/foundry/object-explorer/results_time-dependent-property-hubble-results-view.png)
## Inline edits
![Inline edit in results view](/docs/resources/foundry/object-explorer/results_view_inline_edit.png)
配置了 inline edit action 的 property 可以在 Object Explorer results 页面中直接编辑。一旦用户满足 inline edit action 的提交条件，鼠标悬停时值旁边会出现一个笔形图标。单击该值会启用可编辑字段，具体取决于 property 的类型。提交时，需要再次通过提交条件，否则提交按钮不可选。

Properties that are configured with an inline edit action can be directly edited in the Object Explorer results page. Once a user meets the submission criteria of the inline edit action, a pen appears next to the value on hover. Clicking on the value enables an editable field, depending on the type of the property. To submit, the submission criteria need to be passed again, otherwise the submission button is not selectable.