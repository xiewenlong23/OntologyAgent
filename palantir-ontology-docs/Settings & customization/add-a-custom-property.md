<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/add-a-custom-property/
---
# Add a custom property
Foundry Rules 中一个常见的自定义操作是向 rule 和 proposal object 添加自定义 property。通过自定义 property，您可以跟踪超出默认配置的额外元数据。要添加自定义 property，请按照以下步骤操作：

A common customization in Foundry Rules is adding custom properties to your rule and proposal objects. Custom properties can let you track additional metadata beyond the default configuration. To add a custom property, follow these steps:
1. 在 Ontology Manager 中，将 property（例如 `severity`）添加到 rule object。

1. In the Ontology Manager, add the property (e.g. `severity`) to the rule object.
> **ℹ️ 注意**

> Object property 必须由输入 dataset 中的某一列支持（backed by a column）。
> **ℹ️ 注意**

> Object properties must be backed by a column in the input dataset.
> 对于空的、自动生成的输入 dataset，请直接通过复制和修改现有列定义，在 **Details** 标签页中编辑 schema。
> In the case of an empty, auto-generated input dataset, edit the schema directly in the **Details** tab by copying and modifying an existing column definition.
> 对于来自现有 pipeline 的 rules，请在 transform 中添加新列。
> For rules coming from an existing pipeline, add the new columns in a transform.
2. 向 proposal object 添加对应的 `current_<PROPERTY>` 和 `new_<PROPERTY>` property（例如 `current_severity` 和 `new_severity`）。

3. 使用 type class `foundry-rules.property-diff-for:new_<PROPERTY>`（例如 `foundry-rules.property-diff-for:new_severity`）对 `current_<PROPERTY>` proposal object property 进行标注（annotate）。

2. Add corresponding `current_<PROPERTY>` and `new_<PROPERTY>` properties (e.g. `current_severity` and `new_severity`) to the proposal object.
3. Annotate the `current_<PROPERTY>` proposal object property with the type class `foundry-rules.property-diff-for:new_<PROPERTY>` (e.g. `foundry-rules.property-diff-for:new_severity`).
> **ℹ️ 注意**

> Type class 由 *kind* 和 *name* 组成，写法为 `kind.name`。以 `foundry-rules.property-diff-for:new_<PROPERTY>` 为例，kind 为 `foundry-rules`，name 为 `property-diff-for:new_<PROPERTY>`。
> **ℹ️ 注意**

> Type classes are characterized by a *kind* and a *name*, written out as `kind.name`. In the case of `foundry-rules.property-diff-for:new_<PROPERTY>`, the kind is `foundry-rules` and the name is `property-diff-for:new_<PROPERTY>`.
4. 编辑 Foundry Rules 设置中每一个用于修改或创建 rule 或 proposal object 的 action type，为其添加新自定义 property 的 parameter。请参考另一个类似 property（例如 *rule_name*）的示例，以了解所需的添加内容。

4. Edit every action type in the Foundry Rules setup which modifies or creates a rule or proposal object by adding a parameter of the new custom property. Follow the example of another similar property such as *rule\_name* to see the required additions.
5. 在 Workshop application 中，添加一个 Workshop variable，用于获取所选 rule 的自定义 property。您可以通过定义一个新的 objectProperty variable 并将现有的 `selectedRule` variable 作为其 object set 输入来实现此操作。

5. In the Workshop application, add a Workshop variable that takes the custom property of the selected rule. You can do this by defining a new objectProperty variable with the existing `selectedRule` variable as the object set input.

> 📷 **[图片: Define a variable]**

> 📷 **[图片: Define a variable]**

在 Rule Editor 配置侧边栏中，将此 Workshop variable 设置为 "Create a proposal to edit rule" Action 的默认值。

Set this Workshop variable as the default value for the "Create a proposal to edit rule" Action in the Rule Editor's configuration sidebar.

> 📷 **[图片: 将 Workshop 变量设置为默认值]**

> 📷 **[图片: Set Workshop variable as default value]**

6. 如果 proposal widget 未正确显示 diff，请按照以下步骤操作：

6. If the proposal widget is not displaying diffs correctly, follow these steps:
* 在 Workshop 应用中，将 `new_<PROPERTY>` property 添加到 Proposal Reviewer widget 配置中的 **Properties grouped by section**。此处无需选择 "current" 值。

* 如果需要，可编辑 property 名称以删除 "new" 前缀。

* 将 `foundry-rules.property-diff-for:ID_OF_NEW_PROPERTY` type class 添加到 **proposal object** 的 **current** property。

* In the Workshop app, add the `new_<PROPERTY>` property to **Properties grouped by section** in the Proposal Reviewer widget configuration. It is not necessary to select the "current" value here.
* If desired, edit the property name to remove the ”new“ prefix.
* Add the `foundry-rules.property-diff-for:ID_OF_NEW_PROPERTY` type class to the **current** property of the **proposal object**.

> 📷 **[图片: Alert Recipient property 已添加到 proposal reviewer 配置侧边栏，其中 'New' 前缀被高亮显示以表明可以将其移除]**

> 📷 **[图片: Alert Recipient property added to the proposal reviewer configuration sidebar with the 'New' prefix highlighted to indicate it can be removed]**

