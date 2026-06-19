<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/submission-criteria/
---
# Submission criteria
**Submission criteria** (以前称为 validations) 是决定 Action 能否提交的条件。Submission criteria 支持将业务逻辑编码到数据编辑权限中,从而确保 Ontology 的数据质量和编辑治理。

**Submission criteria** (formerly known as validations) are the conditions that determine whether an action can be submitted. Submission criteria support encoding business logic into data editing permissions, ensuring Ontology data quality and editing governance.
Submission criteria 通过将基于上下文 (如用户或参数) 的条件与静态信息相结合来创建逻辑语句。Submission criteria 可以将 Object、Link,甚至是用户信息整合到逻辑语句中,以决定 Action 能否被提交。

Submission criteria are created by combining conditions based on the context (like a user or a parameter) and static information to create a logical statement. Submission criteria can incorporate object, relation, and even user information into a logical statement to determine whether an action can be submitted.
> **ℹ️ 注意: 示例**

> 例如,一家航空公司可能希望更改特定航班所列的飞机。配置的 Action 允许用户更改链接到 `Flight` Object 的 `Aircraft` Object。但是,航空公司只希望选定的用户 (如航班调度员) 能够使用此 Action,以确保仅使用仍在运营中的飞机。通过使用 submission criteria,builders 可以确保更改航班上飞机的 Action 仅在满足条件时才能提交,方法是将用户的组成员身份与飞机在提交 Action 时的状态相结合。
> **ℹ️ 注意: Example**

> For example, an airline might want to change the airplanes listed for a specific flight. The configured action allows users to change the `Aircraft` object linked to a `Flight` object. However, the airline only wants selected users (like a flight controller) to be able to use this action, in order to ensure that only aircraft which are still in operation are used. Using submission criteria, builders can ensure that an action which changes the airplane on a flight can only be submitted when the criteria are met by combining the user's membership to a group with the airplane's status at the moment that the action is submitted.
![Example: Submission criteria overview](/docs/resources/foundry/action-types/submission_criteria_overview.png)
Submission criteria 由条件和运算符组成。条件是关于参数值或用户属性的单个语句。运算符用于组合和嵌套不同的条件。

Submission criteria consist of conditions and operators. Conditions are single statements governing the values of parameters or user properties. Operators are used to combine and nest different conditions.
通过使用不同类型的运算符,我们可以创建更复杂的语句,以反映其业务流程和需求。Action 仅在满足所有 submission criteria 时才能提交。这与控制用户是否可以编辑 Action Type 本身的权限无关。虽然 Object Type 可以具有多个用于添加、修改和删除 Object 的 Action Type,但每个 Action Type 都有独立的 submission criteria。

Using the different types of operators, we can create more sophisticated statements, mirroring their business processes and requirements. Actions can only be submitted if all the submission criteria are met. This is independent from the permissions that govern whether a user can edit the action type itself. While an object type can have several action types adding, modifying, and removing objects, each action type has independent submission criteria.
## Conditions
条件是两个值之间的单个比较检查。每个条件根据其参数或用户输入而通过或失败。可以使用两种条件模板之一来配置条件:"based on current user" 或 "based on parameter"。这些模板为条件的其余部分提供了一个框架。每个条件都是使用中间运算符对两个值进行的简单比较。

A condition is a single comparison check between two values. Each condition either passes or fails based on its parameter or user inputs. A condition can be configured using one of two condition templates: “based on current user” or “based on parameter”. These templates provide a framework for the rest of the condition. Every condition is a simple comparison between two values using an operator in the middle.

> 📷 **[图片: 示例:选择条件模板]**

> 📷 **[图片: Example: Select Condition Template]**

> **ℹ️ 注意: 示例**

> 继续我们的示例,航班调度员的要求可以使用 `Current User` 模板设置,因为它需要提交 Action 的人员的上下文。要知道飞机是否仍在运营,需要通过 `Parameter` 模板使用 `Aircraft` Object。
> **ℹ️ 注意: Example**

> Continuing with our example, the flight controller requirement can be set using the `Current User` template, as it requires the context of the person submitting the action. To know whether an aircraft is still in operation, the `Aircraft` object needs to be used via the `Parameter` template.
### Current user
`Current User` 模板根据提交 Action 的用户定义权限。`Current User` 输入可用于检查用户的 ID、通过组 ID 进行的组成员关系,或任何其他可用的 multipass 属性 (例如用户的 Organization)。Foundry 将用户 ID 评估为字符串,可以将其与静态定义的用户 ID 列表或存储用户 ID 的任何字符串参数进行比较。

The `Current User` template defines permissions based on the user submitting the action. The `Current User` input can be used to check a user's ID, group memberships via group IDs, or any other multipass attribute available (such as the user's Organization). Foundry evaluates user IDs as strings, which can be compared against either a statically defined list of user IDs or any string parameter that stores a user ID.
组 ID 选项允许您使用 Action 用户所属的组 (无论是直接成员关系还是继承成员关系) 创建条件。可以将这些组与静态选择的组或其他参数提供的组 ID 进行比较。

The group IDs option allows you to create conditions using the groups for which the action's user is a member (whether direct or inherited membership). The groups can be compared against a static selection of groups or the group ID provided by other parameters.
Multipass 属性被视为字符串列表,只能与其他字符串或字符串列表进行比较。用户将拥有其有权访问的建议 multipass 属性列表。使用 `Other user attribute` 字段,可以针对用户无权访问的属性配置条件。如果用户无权访问某个属性,他们将无法通过该条件。

Multipass attributes are treated as string lists and can only be compared against other strings or string lists. A user will have a list of proposed multipass attributes that the user has access to. Using the `Other user attribute` field, conditions can be configured against attributes the user does not have access to. If a user does not have access to an attribute, they will fail the condition.
> **ℹ️ 注意: 示例**

> 要知道我们示例中的用户是否是 flight controller，我们需要检查该用户是否是 flight controller 组的成员。
> **ℹ️ 注意: Example**

> To know whether a user in our example is a flight controller, we need to check if the user is a member of the flight controller group.
### Parameter
Submission criteria 也可以使用 parameter 部分中定义的参数。Parameters 从其他应用程序或用户自身传递到 action type 中。在 parameters 上使用条件允许 builders 将业务逻辑嵌入到 action type 中，并防止用户对不符合业务要求的数据提交 actions。

Submission criteria can also use parameters defined in the parameter section. Parameters are passed into an action type from other apps or users themselves. Using conditions on parameters allows builders to embed business logic into the action type and prevent users from submitting actions on data that do not conform with business requirements.
> **ℹ️ 注意: 示例**

> 在我们的示例中，运行状态通过 `Aircraft` object 提供，并且每架飞机可能不同。该条件需要基于 `Aircraft` object type 参数构建。
> **ℹ️ 注意: Example**

> In our example, the operating status is given via the `Aircraft` object and can change with every aircraft. The condition needs to be built on top of the `Aircraft` object type parameter.
Submission criteria 不支持 attachment 和 object set parameters。这些 parameter 类型会从选择面板中移除。

Submission criteria do not support attachment and object set parameters. These parameter types are removed from the selection panel.
### Select a value
选择 condition template 后，选择要比较的值。某些 parameters（例如 lists 或 object parameters）需要对比较中使用哪个值进行更细粒度的选择。我们也可以选择比较 list 的长度而不是其内容。

After selecting the condition template, choose what value to compare. Some parameters (like lists or object parameters) require a more granular selection of what value should be used in the comparison. We can also choose to compare the length of a list instead of its content.

> 📷 **[图片: 示例：选择一个值]**

> 📷 **[图片: Example: Select a value]**

> **ℹ️ 注意: 示例**

> 在飞机示例中，飞机的运行状态存储在 `Aircraft` object 的 property 中。
> **ℹ️ 注意: Example**

> In the aircraft example, the operating status of an aircraft is stored in the property on the `Aircraft` object.
### Operators
Operators 定义两个值之间的比较。为了简化配置工作流程，operators 会被预过滤，仅显示对该 parameter 有效的 operators 集合。当 parameter 发生更改时，使用该 parameter 的所有 conditions 都需要重新配置。

Operators define the comparison between the two values. To simplify the configuration workflow, operators are pre-filtered to only show a selection of operators valid for the parameter. When a parameter is changed, all conditions using this parameter need to be reconfigured.

> 📷 **[图片: 示例：选择一个 operator]**

> 📷 **[图片: Example: Select an operator]**

根据所选 parameters 的不同，有多个 operators 可用。对于单值 parameters，以下 operators 可用：

There are multiple operators available depending on the selected parameters. For single value parameters, the following operators are available:
|Operator	|Example	|Data Example	|Description	|
|---	|---	|---	|---	|
|is	|name *is* John Doe	|"John Doe" is "John Doe" = TRUE	|The left value exactly matches the right value.	|
|is not	|**Current User** *is not* John Doe	|“John Doe" is not "Maria Smith" = TRUE	|The left value and right value do not match.	|
|matches	|name *matches* ^\[A|E|I|O|U]\*	|"John Doe" matches	|The left value matches the Regular Expression.	|
|is less than	|Aircraft > Engine Count *is less than* 2	|4 is less than 2 = TRUE	|The left value is smaller than the right value.	|
|is greater than or equals	|Aircraft > Engine Count *is greater than or equals* 2	|4 is greater than or equals 2 = TRUE	|The left value is greater than the right value.	|
对于具有多个值的 parameters，以下 operators 可用。Object reference lists 会被转换为值列表（可以是 object 值，也可以是已定义 property 的值）：

|Operator	|Example	|Data Example	|Description	|
|---	|---	|---	|---	|
|includes	|Aircrafts > Pilot Name *includes* "John Doe"	|\[ "John Doe", "Maria Smith" ] includes "John Doe" = TRUE	|左侧值中至少有一个与右侧值完全匹配。	|

|includes any	|name 列表 *includes any* Aircrafts > Pilot Name	|\["King Louis", "John Doe"] 包含于 \[ "John Doe", "Maria Smith" ] = TRUE	|左侧值中至少有一个与右侧值中的至少一个完全匹配。	|

|is included in	|name *is included in* \[ "John Doe", "Maria Smith" ]	|  "John Doe" 包含于 \[ "John Doe", "Maria Smith" ] = TRUE	|左侧值与右侧值中的至少一个完全匹配。	|

|each is	|Aircrafts > Pilot Name *each is* "John Doe"	|\[ "John Doe", "Maria Smith" ] each is "John Doe" = FALSE	|所有左侧值都与右侧值完全匹配。	|

|each is not	|Aircrafts > Pilot Name *each is not* "John Doe"	|\[ "John Doe", "Maria Smith" ] each is not "King Louis" = TRUE	|所有左侧值都不与右侧值完全匹配。	|

For parameters with multiple values, the following operators are available. Object reference lists are turned into a list of values (either the object value or the value of the defined property):
|Operator	|Example	|Data Example	|Description	|
|---	|---	|---	|---	|
|includes	|Aircrafts > Pilot Name *includes* "John Doe"	|\[ "John Doe", "Maria Smith" ] includes "John Doe" = TRUE	|At least one of the left values exactly matches the right value.	|
|includes any	|List of names *includes any* Aircrafts > Pilot Name	|\["King Louis", "John Doe"] is included in \[ "John Doe", "Maria Smith" ] = TRUE	|At least one of the left values exactly matches at least one of the right values.	|
|is included in	|name *is included in* \[ "John Doe", "Maria Smith" ]	|  "John Doe" is included in \[ "John Doe", "Maria Smith" ] = TRUE	|The left value exactly matches at least one of the right values.	|
|each is	|Aircrafts > Pilot Name *each is* "John Doe"	|\[ "John Doe", "Maria Smith" ] each is "John Doe" = FALSE	|All left values exactly match the right value.	|
|each is not	|Aircrafts > Pilot Name *each is not* "John Doe"	|\[ "John Doe", "Maria Smith" ] each is not "King Louis" = TRUE	|All left values do not exactly match the right value.	|
> **ℹ️ 注意: 示例**

> 由于我们示例中的用户是多个组的成员，但比较的对象是单个组，因此我们需要选择 `includes` operator 来检查是否存在重叠。但是，运行状态需要与预期状态完全匹配，因此必须使用 `is` operator。
> **ℹ️ 注意: Example**

> Since a user in our example is a member of many groups but the comparison is to a single group, we need to select the `includes` operator to check for an overlap. However, the operating status needs to exactly match an expected status, so the `is` operator must be set.
### Value
该值表示比较的另一端。该值可以基于现有 parameter、static value，或者没有值。No value 检查第一个值是否为空（或 null）。与 operator 一样，可用选项取决于第一个值的类型。

The value represents the other side of the comparison. The value can either be based on an existing parameter, a static value, or no value. No value checks whether the first value is empty (or null). Like the operator, the available options depend on the first value type.

> 📷 **[图片: 示例：选择一个值]**

> 📷 **[图片: Example: Select a value]**

> **ℹ️ 注意: 示例**

> 我们现在可以完成飞机示例中所需的两个 conditions。对于 flight controllers，需要将正确的组选择为 static parameter。这是因为该组不应更改，而是在每次提交 Action 时保持不变，无论上下文如何。因此使用 `specific value`，并通过下拉菜单选择所需的组。当运行状态 property 为 `Yes` 时，飞机被视为可运行，这也可以使用 specific value 选项进行设置。
> **ℹ️ 注意: Example**

> We can now finalize the two conditions needed in the aircraft example. For flight controllers, the correct group needs to be selected as a static parameter. This is because the group should not change, but should stay the same every time an Action is submitted, regardless of the context. Hence the `specific value` is used and the desired group is selected via the dropdown. An aircraft is considered operational when the operating status property is `Yes`, which can be set using the specific value option again.
## Logical operators
逻辑运算符可用于组合不同的条件。逻辑运算符也可以嵌套使用，以创建更复杂的逻辑，并可以要求其下方的所有条件、任意条件或无条件满足才能通过。

A logical operator can be used to combine different conditions. Logical operators can also be nested to create even more complex logic and can require either all, any, or no conditions underneath it to be met to pass.
## Failure message
失败消息支持定义在 Action 无法提交时应显示的错误。根级别的每个条件和逻辑运算符都有自己的失败消息。如果较低层级的条件未满足，则显示相应根级别（父级）的失败消息。当条件未满足时，失败消息将向最终用户显示在 Foundry（Object Explorer、Workshop 或 Quiver）中。失败消息告知用户他们无法提交 Action 的原因。

Failure messages support defining what error should be displayed whenever the Action cannot be submitted. Every condition and logical operator on the root level has its own failure message. If conditions of lower levels are not met, the failure message of the corresponding root level (parent) is displayed. The failure message will be displayed to the end user across Foundry (Object Explorer, Workshop, or Quiver) whenever a condition is not met. The failure message informs the user about why they are blocked from submitting an Action.