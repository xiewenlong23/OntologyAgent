<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/permitted-and-default-output-values/
---
# Permitted and default output values
Workflow outputs 用于指定 workflow 中所有 Foundry rules 输出的目标和格式。在 **rule editor** 中每个 rule 的末尾，在 **rule output [logic block](/docs/foundry/foundry-rules/rule-logic/#logic-blocks)** 中，author 会将一个 column 或一个 static value 分配给每个 workflow output。分配值可以确保在需要 rule output 的值时其已被定义，并且数据能够以正确的数据类型安全地流入 workflow output dataset。

Workflow outputs specify the destination and format for the output of all the Foundry rules in the workflow. At the end of each rule in the **rule editor**, in the **rule output [logic block](/docs/foundry/foundry-rules/rule-logic/#logic-blocks)**, the author will assign a column or a static value to each workflow output. Assigning values ensures that the rule output is defined when its value is required and that the data can safely flow into the workflow output dataset with the correct data type.
**Permitted and default output values** 部分可用于简化分配流程并进一步自定义 rule output logic block。在创建新 rule 时将自动分配 default values，并且可以限制仅允许在 column value 或 static value 中选择其一进行分配。

The **Permitted and default output values** section can be used to streamline the assignment process and to further customize the rule output logic block. Default values will automatically be assigned when a new rule is created, and the option to assign either column or static values can be restricted to allow only one of the two value types.
![Output field configuration](/docs/resources/foundry/foundry-rules/permitted_and_default_values_standard.png)
截图展示的是标准配置，这是最具开放性的配置，不指定任何 default values。除非对标准配置进行了任何更改，否则 **Permitted and default output values** 部分将处于折叠状态。

The screenshot shows the standard configuration, which is the most permissive and does not specify any default values. The **Permitted and default output values** section will be collapsed unless any changes have been made to the standard configuration.
## Behavior and example use case
每个 output field 都可以拥有自己的配置。以下示例最能说明这一点：

Each output field can have its own configuration. This is best illustrated by the following example:
如果 `equipment failure alert` 需要 link 回某个特定的 equipment item，则应将该 field 限制为不允许任何 static values（`None`），并且仅允许来自 object property `Serial Num` 的 column values。

If an `equipment failure alert` should link back to a specific equipment item, the field should be restricted to allow no static values (`None`) and only column values that are derived from the object property `Serial Num`.
Alerts 是 operational workflows 的核心，因此它们通常会与某个 process 相关联。Equipment failure 将需要某种形式的 repair，因此 alert 可能处于多种可能的状态之一。Workflow output 将包含一个 field `Repair Status` (1)，它是一个必填 field (2)，类型为 `String`。假设某些 equipment failures 拥有与 alert 一起触发的 automated service routine，而另一些则需要人工干预。此信息只有 rule author 才能确定，因此来自输入数据的 column values 已被禁用 (3, `None`)。状态需要被设置为多个可能的状态 (4) 之一，并且默认应为 `Not started`。Rule author 将看到的 rule output logic block 反映了此配置。在 static value 和 column value 之间的切换已被禁用，并显示一个包含所有可能状态选项的选择菜单。

Alerts are at the core of operational workflows, so they usually tie into a process. An equipment failure will require some kind of repair, so the alert can be in one of many possible states. The workflow output will have a field `Repair Status` (1), which is a required field (2) of type `String`. Let's assume some equipment failures have an automated service routine that is triggered together with the alert, but others require manual intervention. This information is something only the rule author can determine, so column values from the input data are disabled (3, `None`). The status needs to be set to one of multiple possible states (4) and should be `Not started` by default. The rule output logic block that the rule author will see reflects this configuration. The switch between static and column values is disabled, and a selection menu with all possible status options is shown.
![Permitted values example configuration and rule output block](/docs/resources/foundry/foundry-rules/permitted_and_default_values_example.png)
## Configuration options
该配置分为两个部分：column values 和 static values。这两个部分都取决于 output field 的类型。如果任何配置不完整或无法满足，将通过错误图标指示问题。如果 rule author 提供了不合规的值（例如不在所需范围内的 integer），相同的错误图标也会在 rule output logic block 中指示问题。

对于类型为 `String` 的 output values，提供了一个将该 field 设为 string template 的选项。String template 是 static value 和 column value 的组合。如果选中了 **Field is a string template** 选项，则无法再进行其他配置。

The configuration is split in two sections: column values and static values. Both sections depend on the output field type. If any configuration is incomplete or not satisfiable, an error icon will indicate the issue. The same error icon will indicate issues in the rule output logic block if the rule author provides values that are not compliant, such as an integer that is not within the required range.
For output values of type `String`, an option is available to make the field a string template. A string template is a combination of static and column values. If the **Field is a string template** option is selected, no further configurations are possible.
![Rule editor with string template field](/docs/resources/foundry/foundry-rules/string_template_rule_editor.png)
### Column values
Column values 指的是在应用 rule logic 之后来自底层 dataset 某一 column 的值。当 rule author 编写 rule logic 时，实际数据尚不可知，因此 output column 只能通过类型或 input property name 进行限制。可以为 column values 配置以下选项：

Column values refer to values that come from a column of the underlying dataset after the rule logic has been applied. When the rule author write the rule logic, the actual data is not known and the output column can only be restricted by type or input property name. The following options can be configured for column values:
* **Any:** 任何现有 column 都可以分配给此 output field。

* **None:** 此 output field 将仅接受 static values。不允许 column references。

* **Selection:** 指定 column options 集合中的任何 column 都可以分配给此 field。

* **Any:** Any existing column can be assigned to this output field.
* **None:** This output field will only accept static values. Column references are not allowed.
* **Selection:** Any column of the specified set of column options can be assigned to this field.
### Static values
Static values 指的是 rule author 在创建或编辑 rule 时手动输入的值。可以限制这些值，使其处于某个数值或日期范围内，或使多个值的输入具有正确的长度。用户的输入和值的选择将以 dropdown menus 的形式显示，以便 rule author 更轻松地输入正确的值。可以为 static values 配置以下选项：

Static values refer to values that a rule author enters manually when creating or editing a rule. You can restrict these values so that they are within a number or date range or that inputs for multiple values have the correct length. Inputs for users and selection of values will be shown as dropdown menus so the rule author can enter the correct values more easily. The following options can be configured for static values:
* **Any:** 任何正确 field 类型的值都可以分配给此 output field。

* **None:** 此 output field 将仅接受 column references。不允许 static values。

* **Selection:** 指定值集合中的任何值都可以分配给此 output field。可选地，允许其他值。Options 将以其 label 显示。

* **Range:** 仅允许处于指定范围内的 static values。此选项仅适用于 numeric 和 date 类型。

* **Users:** 指定 Foundry Users 集合中的任何 user 都可以分配给此 field。如果未选择任何 users，则不会应用任何限制。此选项仅适用于 string 类型。

* **Any:** Any value of the correct field type can be assigned to this output field.
* **None:** This output field will only accept column references. No static values are allowed.
* **Selection:** Any value of the specified set of values can be assigned to this output field. Optionally, other values may be allowed. Options will be displayed by their label.
* **Range:** Only static values that are within the specified range will be allowed. This option is available for numeric and date types only.
* **Users:** Any user of the specified set of Foundry Users can be assigned to this field. If no users are chosen, no restrictions will apply. This option is available for string types only.
对于 **allow multiple values** 的类型，限制将应用于输入中的每个 item。例如，输入中的每个 integer 都必须在所需范围内，每个 user 必须是预先选定的 user 之一，或者每个 item 必须是已标记的 selection items 之一。

For types that **allow multiple values**, the restrictions apply for each item in the input. For example, each integer in the input must be within the required range, each user must be one of the pre-selected users, or each item must be one of the labelled selection of items.