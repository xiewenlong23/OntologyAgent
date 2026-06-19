<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/parameters-filter/
---
# Filter results of a parameter dropdown
为非 Object Reference 的 multiple choice 或 single object reference 参数添加 Filters，将决定在该参数的下拉菜单中可选择的允许值。

Adding filters to non-object reference multiple choice or single object reference parameters will determine the allowed values that are selectable in the parameter's dropdown.
## Multiple choice parameter dropdowns
在配置 multiple choice 参数的下拉菜单时，Action Editor 可以将允许的值限制为仅为某个对象集的 Property。这可用于根据 Link 对象 的 Property 来显示或预填值。为此，请确保该参数设置为显示 multiple choice，选择 **Get options from an object set**，配置所需的对象集，然后选择包含该参数下拉菜单所有允许值的 Property。如果结果对象集中只有一个 Link 对象 并且该参数是必填项，则该参数的下拉菜单将自动预填相应的 Property 值。生成的 multiple choice 选项将派生自用户有权查看的对象集。换言之，当从对象集派生 multiple choice 选项时，用户将无法查看其无权访问的对象的 Property。

When configuring multiple choice parameter dropdown menus, action editors can reduce allowed values to just those that are properties of an object set. This can be leveraged to display or prefill values based on properties of a linked object. To accomplish this, ensure the parameter is set to display multiple choices, select **Get options from an object set**, configure the desired object set, and select the property that includes all allowed values for the parameter dropdown. If only one linked object is available in the resulting object set and the parameter is required, the parameter dropdown will automatically prefill with the corresponding property value. The resulting multiple choice options will be derived from the set of objects that the user has permission to view. In other words, when deriving multiple choice options from an object set, users will not see properties of objects to which they do not have access.
![Property Dropdown Configuration](/docs/resources/foundry/action-types/property_dropdown_configuration.png)
## Object dropdowns
在参数配置视图中，Action Editor 可以指定 Filters 和 Search Arounds，以限制在所有 Action Interface 中下拉菜单中显示的对象。配置 Filters 后，Action Form 将渲染一个仅包含与 Filter 匹配的对象的下拉菜单。所选的值也会在 Action 执行之前进行验证。

Within the parameter configuration view, action editors can specify filters and Search Arounds to limit the objects that show up in the dropdown across all action interfaces. After configuring the filters, the action form will render a dropdown with only objects that match the filter. The value selected is also validated before the action is executed.
例如，一个对象下拉菜单被配置为仅显示 **Name** 等于 `Name` 参数中值的 **Stock Series**。

For example, an object dropdown configured to only show **Stock Series** where the **Name** is equal to the value in the `Name` parameter.
![Object Dropdown Starting Set](/docs/resources/foundry/action-types/objectDropdownStartingSet.png)
下图显示了 `Name` 参数的可能值：

The image below shows the possible values for the `Name` parameter:
![Object Dropdown Resulting Form](/docs/resources/foundry/action-types/objectDropdownResultingForm.png)
### Data privacy implications
当对对象参数使用新的验证时，所有能够查看该 Action Type 的人都可以查看这些数据。如果参数 Filters 中存在敏感的静态值，即使用户无法查看正在被过滤的底层对象，他们也能够查看这些值。[详细了解数据隐私方面的影响。](/docs/foundry/action-types/dropdown-security/)

When using the new validation on an object parameter, it's possible for data to be viewed by everyone who can view the action type. If there are sensitive static values in the parameter filters, users will be able to view those values even if they cannot view the underlying objects that are being filtered. [Learn more about the data privacy implications.](/docs/foundry/action-types/dropdown-security/)
## Supported operations
### Filtering on a property
对象下拉菜单仅显示指定 Property 与所提供的任何值匹配的对象。

The object dropdown only shows objects where the specified property matches any of the provided values.
![Object Dropdown Filtering on Property](/docs/resources/foundry/action-types/object_dropdown_filtering_on_property.png)
该值可以由用户静态定义、从另一个参数推断得出，或是某个 `Object Reference` 参数的 Property。如果提供了多个值进行比较，则结果将是一个 **OR** 运算。

The value can be statically defined by the user, inferred from another parameter, or a property of an `Object Reference` parameter. If more than one value is provided to compare against, the result will be an **OR** operation.
### Changing the starting object set
查询的**起始集合**默认设置为该 object type 的所有 objects，但也可以更改为任何其他类型。起始集合也可以设置为一个 `ObjectReference` 列表参数。

The **starting set** for the query is set to all objects of the object type by default, but this can be changed to any other type. The starting set could also be set to an `ObjectReference` list parameter.
![Object Dropdown Changing Starting Set](/docs/resources/foundry/action-types/object_dropdown_changing_starting_set.png)
### Search Arounds
Search Around 会通过遍历当前集合中每个 object 的一个 link 来创建一个新的集合。例如，`Github Issue of Current Employee` 会获取当前集合中的 `Employees`，并创建一个由链接到这些 `Employees` 的 `Github Issues` 组成的结果集合。

A Search Around would create a new set by traversing a link on every object in the current set. For example, `Github Issue of Current Employee` would take the `Employees` in the current set and create a resulting set of `Github Issues` linked to those `Employees`.
![Object Dropdown Search Around](/docs/resources/foundry/action-types/object_dropdown_search_around.png)