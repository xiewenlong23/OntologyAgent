<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/histogram/
---
# Histogram
**Histogram（直方图）** 面板允许对地图上的对象数据进行选择和过滤。面板的第一部分 **Object types（对象类型）** 显示地图上按对象类型分类的对象计数。下方为每个属性类型对应的一个部分，涵盖地图上出现的所有对象类型。面板顶部的过滤框允许您将结果过滤为名称匹配的属性。

The **Histogram** panel allows for the selection and filtering of objects data on your map. The first section of the panel **Object types** shows the counts of objects by object type on your map. Below, there is one section per property type, across all object types present on your map. The filter box at the top of the panel allows you to filter results to properties with matching names.
## Use the histogram
展开直方图部分以显示给定属性的每个不同值的行，默认情况下按值的计数排序后限制为前五行。单击 **Show more（显示更多）** 以显示接下来的五行。

Expand a histogram section to show a row for each distinct value of the given property, limited by default to the top five sorted by the count of values. Click **Show more** to display the next five rows.
单击 **Value（值）** 标题可在 **Value（值）**（升序）或 **Value（值）**（降序）之间切换排序方式。单击 **Count（计数）** 标题可在 **Count（计数）**（降序）、**Count（计数）**（升序）、**Selected Count（已选计数）**（降序）或 **Selected Count（已选计数）**（升序）之间切换排序方式。

Click the **Value** heading to toggle the sort method to **Value** (ascending) or **Value** (descending). Click the **Count** heading to toggle the sort method to **Count** (descending), **Count** (ascending), **Selected Count** (descending) or **Selected Count** (ascending).
| Value                                                                  | Count                                                     | Selected count                                                              |
|------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| ![Histogram sorted by value alphabetical](/docs/resources/foundry/map/histogram-value.png) | ![Histogram sorted by count](/docs/resources/foundry/map/histogram-count.png) | ![Histogram sorted by selected count](/docs/resources/foundry/map/histogram-selected-count.png) |
对于日期和数值属性，提供了一个用于控制 **Binning（分箱）** 的附加选项。

For date and numeric properties, an additional option to control the **Binning** is available.
对于日期属性，通过单击此标题，您可以在 **Year（年）**、**Year and month（年和月）**、**Quarter（季度）**、**Month（月）** 和 **Day（日）** 之间切换分箱方法。单击示例图片可将其展开。

For date properties, by clicking on this heading you can toggle the binning method between **Year**, **Year and month**, **Quarter**, **Month**, and **Day**. Click an example image to expand it.
| Year                                                            | Year and month                                                             | Quarter                                                               | Month                                                                     | Day                                                                   |
|-----------------------------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------|
| ![Histogram binned by year](/docs/resources/foundry/map/histogram-binning-year.png) | ![Histogram binned by month](/docs/resources/foundry/map/histogram-binning-year-and-month.png) | ![Histogram binned by quarter](/docs/resources/foundry/map/histogram-binning-quarter.png) | ![Histogram binned by month of year](/docs/resources/foundry/map/histogram-binning-month.png) | ![Histogram binned by day of week](/docs/resources/foundry/map/histogram-binning-day.png) |
对于数值属性，通过单击此标题，您可以在 **No binning（不分箱）**、**Equal size（等距分箱）**（将自动将数值分组为大小相等的分箱）和 **Logarithmic（对数分箱）**（将按数值的数量级对数值进行分组）之间切换分箱方法。

For numeric properties, by clicking on this heading you can toggle the binning method between **No binning**, **Equal size** which will automatically group the numeric values into equally sized bins, and **Logarithmic** which will group the numeric values by their order of magnitude.
| No binning                                               | Equal size                                                                        | Logarithmic                                                                           |
|----------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| ![Numeric histogram](/docs/resources/foundry/map/histogram-binning-none.png) | ![Numeric histogram in equal size bins](/docs/resources/foundry/map/histogram-binning-equal-size.png) | ![Numeric histogram in logarithmically sized bins](/docs/resources/foundry/map/histogram-binning-log.png) |
## Selection
单击 **Histogram（直方图）** 面板中的某一行将选择所有匹配的对象。在选择第二行时按住 Shift 将选择一个范围内的行。按住 Ctrl（Windows）或 Cmd（Mac）会将该行添加到现有选择中。这使您能够跨直方图的多个部分选择行。

Clicking on a row within the **Histogram** panel will select all matching objects. Holding Shift while selecting a second row will select a range of rows. Holding Ctrl (Windows) or Cmd (Mac) will add the row to the existing selection. This enables you to select rows across multiple sections of the histogram.
![Map application with histogram row selected](/docs/resources/foundry/map/histogram-filters-selected.png)
## Filtering
当 histogram 中的行被选中时，您可以使用 **Filter to** 或 **Filter out** 按钮来创建过滤器。过滤器会临时降低与过滤器不匹配的 object 的不透明度。这些 object 将变为不可交互的，并且不会参与 histogram 统计。当过滤器存在时，它们会显示在主应用程序工具栏上方的一个条形区域中。可以通过过滤器上的 **x** 按钮移除过滤器，或使用 **Clear filters** 按钮移除所有过滤器。过滤器不会随您的 map 一起保存。

When histogram rows are selected, you can use the **Filter to** or **Filter out** buttons to create filters. Filters temporarily reduce the opacity of objects that do not match the filters. These objects will become uninteractive and will not contribute to the histogram statistics. When present, filters are visible in a bar above the main application toolbar. Filters can be removed using the **x** button on the filter, or by using the **Clear filters** button to remove all filters. Filters are not saved with your map.
选择 **Filter to** 将过滤您的 map，仅显示与所选行匹配的 object。

Selecting **Filter to** will filter your map to only objects matching the selected rows.
![Map application with objects filtered in](/docs/resources/foundry/map/histogram-filtered-in.png)
选择 **Filter out** 将过滤您的 map，仅显示与所选行不匹配的 object。

Selecting **Filter out** will filter your map to only objects that do not match the selected rows.
![Map application with objects filtered out](/docs/resources/foundry/map/histogram-filtered-out.png)
除了 **Filter to** 和 **Filter out** 按钮之外，您还可以通过双击单个 histogram 行来过滤到该行。要过滤到所有当前选中的 object，您可以在 map 的右键菜单中使用 **Filter to selected objects** 菜单项。

In addition to the **Filter to** and \**Filter out* buttons, you can also filter to an individual histogram row by double-clicking on it. To filter to all currently selected objects, you can use the **Filter to selected objects** menu item from the right click menu on your map.