<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/parameter-overview/
---
# Parameters
**Parameters(参数)**是 action type 的输入。它们是 **Rules(规则)** 与其他 Foundry 应用程序之间的 interface,例如 [Workshop](/docs/foundry/workshop/overview/)、[Slate](/docs/foundry/slate/overview/) 和 [Object Views](/docs/foundry/object-views/overview/)。Parameters 被视为包含外部值的变量。每个 parameter 由一个 type 定义,该 type 决定了它可以接受的值类型。除了其 type 之外,parameters 还有各种其他潜在配置。每个 parameter 都可以单独配置是否在表单中暴露,或是否允许用户修改。

**Parameters** are the inputs of an action type. They are the interface between the **Rules** and other Foundry applications, such as [Workshop](/docs/foundry/workshop/overview/), [Slate](/docs/foundry/slate/overview/), and [Object Views](/docs/foundry/object-views/overview/). Parameters are treated like variables that contain external values. Each parameter is defined by a type, which dictates what kind of values it can take. Beyond its type, parameters have a variety of other potential configurations. Each parameter can be individually configured as to whether they are exposed in the form or not, or whether they can be changed by the user or not.
Parameters 在 action type 中传递值,并可以在 rules 中被引用,以将该值传递回 object、link 或 side effect;在提交条件中使用以检查 action 是否可以提交;用于在 action 更改 object property 当前值之前访问其值;或在 overrides 中用于更改后续 parameter 的配置。

Parameters transport values across the action type and can be referenced in rules to pass the value back on an object, link, or side effect, in submission criteria, to check if an action can be submitted, to access the current value of an object property before it is changed by the action or in overrides to change the configuration of a following parameter.
> **ℹ️ 注意: 示例**

> 在允许用户修改所选 ticket 状态的 action type 中,parameter 可以采用 `Ticket` object type 的形式。`Status` parameter 被定义为 string 类型。在提交 action 时,object type parameter 将获取所选 `Ticket` object 的值,而 `Status` parameter 包含未来的状态。然后,action type 将这两个 parameter 值传递给 rules 并执行它们以编辑该 object。
> **ℹ️ 注意: Example**

> A parameter can take the form of a `Ticket` object type in an action type which allows users to modify the status of a selected ticket. A `Status` parameter is defined as a string. When submitting the action, the object type parameter will take the value of a selected `Ticket` object and the `Status` parameter contains the future status. The action type then passes both parameter values to the rules and executes them to edit the object.
> **ℹ️ 注意: 示例**

> 作为 Workshop 中的变量,`previous_status` 可以获取所选 `Ticket` object 的 `Status` property 的当前值。这可以传递给 action 中的一个隐藏 parameter `Previous Status`,而 `Status` parameter 可以包含更新后的状态。提交 action 后,action type 会将 `Previous Status` 和 `Status` 这两个值都传递给 rules 并执行它们以编辑该 object。
> **ℹ️ 注意: Example**

> As a variable in Workshop, `previous_status` can take the current value of the `Status` property of the selected `Ticket` object. This can be passed to a hidden parameter in the action, `Previous Status`, and the `Status` parameter can contain the updated status. Upon submitting the action, the action type then passes both the `Previous Stats` and the `Status` values to the rules and executes them to edit the object.