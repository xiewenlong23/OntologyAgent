<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/conditional-formatting/
---
**条件格式（Conditional formatting）** 允许为任何 property 配置规则，并决定该 property 的值在面向用户的应用程序中如何呈现（例如着色、对齐方式等）。当您在 Ontology Manager 中配置条件格式时，格式规则将应用于 Object Explorer、Object Views、Quiver 和 Workshop。

**Conditional formatting** enables the configuration of rules for any property and dictates how that property’s values will be rendered (e.g. coloring, alignment, etc.) in user facing applications. When you configure conditional formatting in the Ontology Manager, the formatting rules will apply in Object Explorer, Object Views, Quiver, and Workshop.

> 📷 **[图片: Example]**

> 📷 **[图片: Example]**

对于上图中 Object Explorer 中的 `Aircraft` object type 示例，`type` 和 `wifi` 属性的值显示在带颜色的框中，这些颜色是根据特定条件应用的。添加这些条件格式的主要好处是使信息更易于快速理解。如果分析人员正在查找所有在 "JFK" 且没有 wifi 的 "A320" 飞机，只需扫一眼上面的结果，就可以判断 "Q-AAY" 就是我们要找的飞机。

For the example `Aircraft` object type in Object Explorer, pictured above, the `type` and `wifi` properties have their values in colored boxes that are applied based on certain conditions. The main benefit of adding these is to make information easier to understand quickly. If an analyst was looking for all “A320” planes without wifi in “JFK”, just by glancing at the results above, we could tell that “Q-AAY” is the plane we’re after.
让我们来看看这些条件是如何应用的。

Let’s take a look at how these conditions are applied.
* 对于属性 `wifi`，如果表中每个 object 的属性值为 "true"，则分配绿色；如果为 "false"，则分配红色。

* For property `wifi`, we assign green if the value of the property is “true” for each object in the table, and red if it is “false."

> 📷 **[图片: Example rules]**

> 📷 **[图片: Example rules]**

* 对于属性 `type`，我们根据 "A320"、"A321" 和 "A330" 之间的精确匹配来分配颜色。

* For property `type`, we assign colors based on exact match between “A320”, “A321” and “A330”.

> 📷 **[图片: Example type colors]**

> 📷 **[图片: Example type colors]**

## Add conditional formatting
在 property 编辑器中：

In the property editor:
1. 选择要向其添加条件格式的 property。

2. 您将在属性窗格中看到条件格式；选择 **Add a rule** 按钮。

1. Select the property to which you want to add conditional formatting.
2. You will see conditional formatting on the properties pane; select the **Add a rule** button.

> 📷 **[图片: Add a rule]**

> 📷 **[图片: Add a rule]**

1. 单击新创建的默认规则以打开 **Edit conditional formatting rule** 编辑器。[继续阅读以获取有关 Rule 编辑器各组件的更多信息](#edit-rules-using-the-rule-editor)。
2. 修改规则。

1. Click on the newly created default rule to open the **Edit conditional formatting rule** editor. [Read on for more information about the components of the Rule editor](#edit-rules-using-the-rule-editor).
2. Modify the rule.

> 📷 **[图片: Modifying a rule]**

> 📷 **[图片: Modifying a rule]**

## Edit rules using the Rule editor

> 📷 **[图片: Rule editor]**

> 📷 **[图片: Rule editor]**

|Label   |Description    |Usage  |
|---    |---    |---    |
|A  |Switch between a **Standard** rule, an **Always true** rule, or a **Math** rule.    |Use **Always true** as a fallback in case your other rules don't match. In the example above, we could have grey as the fallback case when neither of the `type` values match.

Use a **Math** rule when you want to run math operators on some of your properties.  |
|B  |The rule will always be applied to the property from which you selected **Add a rule**; however, this dropdown allows you to choose to apply the rule based on the value of another property.   |In the case above, assume we want to color the value for `Type` in red when the value of `Performance factor` drops underneath a certain threshold. We would choose `Performance factor` in our logic instead of `Type`; however, the color would still show on `Type`. |
|C  |Types of comparisons available are based on the type of the property. For example, for strings **String comparison** and **Is null** are available. For numeric types, **Numeric range** or **Exact numeric match** are available.     |To color the `type` in grey if the value is null, select this dropdown and choose **Is null** instead of **String comparison**. |
|D  |Subtypes of comparisons, **String comparison** has **Is exactly**, **Contains**, **Starts with**, etc. |Use this to color all plane `type` values that **Start with** "A32".    |
|E  |Compare against a constant or a property reference.    |In this case, we are specifically looking for the constant "A320", but we could also add a reference from another property from the same object type.  |
|F  |Toggle between a **True** or **False** rule.   |To color all planes in blue that are **not** A320, switch this to **False**.   |
|Formatting |Use Blueprint colors and intents or add your own custom color. You can also switch alignment.  |Switch between hex, RGB or Blueprint colors based on need; you can also align the boxes on the right hand side for easier readability for numbers. |
|Preview    |View how conditional formatting appears in various contexts.   |Preview an **Objects table** or a **Property card.**   |
## Copy rules
在 property editor 中：

In the property editor:
1. 从您要复制 conditional formatting 规则的 property 中选择。

1. Select the property from which you want to copy the conditional formatting rule.
2. 您将在 properties 窗格中看到 conditional formatting；选择 **Copy rules** 按钮以打开 **Copy rule** 对话框。

2. You will see conditional formatting on the properties pane; select the **Copy rules** button to open the **Copy rule** dialog.

> 📷 **[图片: Property editor]**

> 📷 **[图片: Property editor]**

3. 选择您要将 conditional formatting 规则复制到的 properties。

3. Select the properties to which you want to copy the conditional formatting rules.
> **ℹ️ 注意**

> 如果您要复制到的 properties 已有自己的 conditional formatting 规则，则这些规则将被新规则覆盖。
> **ℹ️ 注意**

> If the properties you are copying to already have their own conditional formatting rules, they will be overwritten by the new rules.

> 📷 **[图片: Copy rule]**

> 📷 **[图片: Copy rule]**

已复制的规则将继续引用其原始的 properties。例如，如果某条规则规定 `wifi` 值为 "true" 时应显示为绿色，并且该规则被复制到 `customer experience` property，那么当对象的 `wifi` 值为 "true" 时，`customer experience` property 的值也会显示为绿色。要更改规则所引用的 property，只需选择该规则，然后在规则编辑器中的 **Property** 下拉菜单中选择一个新的 property 即可。

Copied rules will continue referencing their original properties. For example, if a rule states that `wifi` values should appear green when “true,” and that rule is copied to the `customer experience` property, values of the `customer experience` property will also be green when the object’s `wifi` value is “true.” To change the property a rule references, simply select the rule and choose a new property from the **Property** dropdown in the rule editor.
## FAQ
### Will this work with existing type classes?
Conditional formatting 优先于现有的 type classes（[以下问题](#will-this-work-with-editable-properties-in-object-views)中详细说明了一个例外情况）。如果您同时配置了两者，则将显示 conditional formatting。但是，您可以在一个 property 上使用 conditional formatting，而在另一个 property 上使用 type classes。

Conditional formatting takes precedence over existing type classes (with one exception detailed in the [following question](#will-this-work-with-editable-properties-in-object-views)). If you have both configured, conditional formatting will be displayed. You can however, use conditional formatting on one property and type classes on another.
### Will this work with editable properties in Object Views?
Conditional formatting 支持为 [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits) 配置的 properties。对于具有旧版 `hubble:editable` property type class 的 properties，conditional formatting 被禁用。

Conditional formatting is supported for properties configured for [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits). Conditional formatting is disabled for properties with the legacy `hubble:editable` property type class.