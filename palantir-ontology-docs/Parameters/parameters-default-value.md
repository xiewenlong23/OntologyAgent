<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/parameters-default-value/
---
# Set parameter default value
Action type parameters 的 default values 用于在 action 表单中预填 parameters。Default values 在 parameter 级别进行配置,并在 Workshop、Object Explorer、Object Views、Quiver 和 Slate 中受支持。它们可以部署以在多个消费应用程序之间标准化 action 逻辑,从而无需在每个应用程序中单独添加 default values。

Default values for action type parameters are used to prefill parameters in the action form. Default values are configured at the parameter level and are supported in Workshop, Object Explorer, Object Views, Quiver, and Slate. They can be deployed to standardize action logic across multiple consuming applications, eliminating the need to add default values in each application individually.
Parameters 可以设置为 default values,以显示固定值或所选 object 的 property。

Parameters can be set to default values to display either a fixed value or a property of the selected object.
## Default value interaction with local variables
本地 default values(例如 Workshop 变量)始终优先于全局 default values。当将任何 Workshop 变量传递给具有 default value 的 action 时,action 表单将使用 Workshop 变量中的值进行预填。Object Views 中的环境变量和 Slate 中的 defaults 也适用相同的模式。每个 action 实例中提供的 defaults 优先。因此,任何向 default values 的迁移都需要移除本地 overrides。

Local default values (for example, Workshop variables) always take precedence over global default values. When passing any Workshop variable to an action with a default value, the action form will prefill with the values from the Workshop variables. The same pattern applies with environment variables from Object Views and defaults from Slate. Defaults provided in each instance of an action take precedence. Any migration to default values will therefore require removing local overrides.
## Configuring default values
选择任何参数都会打开该参数的配置视图。选择该参数是应默认为固定值，还是应使用来自对象参数的 Property 的值。

Selecting any parameter opens the parameter configuration view for that parameter. Select whether the parameter should default to a fixed value or with a value from the property of an object parameter.
### Static default value
假设有一个 Action Type 示例，用于将所选 `Aircraft` 对象的 `Type` Property 修改为 `A320`。要进行配置，请点击 `Type` 参数并添加一个静态默认值。

Imagine an example action type that modifies the `Type` property of a selected `Aircraft` object to become `A320`. To configure, click into the `Type` parameter and add a static default value.
![Configuring a static default value](/docs/resources/foundry/action-types/default_value_static_configuration.png)
如果要在不使用默认值的情况下实现类似的用户体验，则需要在使用该参数的每个 Application 中配置输入值。要更新此行为（例如，将其更改为 `A380`），则需要手动修改该行为，可能涉及多个 Application。

To achieve a similar user experience without default values, input values would need to be configured in each application that uses the parameter. Updating this behavior (for instance, to `A380`) would require manually modifying the behavior, possibly across multiple applications.
![Static default value example](/docs/resources/foundry/action-types/default_value_static_example.png)
### Object property default values
要将对象 Property 设置为参数的默认值，首先需要选择一个对象参数进行配置。假设有一个更通用的 Action Type，称为 `Change Airplane Details`，例如，用户在进行编辑之前需要知道某个 Property 的当前值。这可以通过将每个参数的值配置为从当前所选对象（在本例中为要修改的 `Plane` 对象）预填来实现。只有位于输入列表中该参数上方的 Object Reference 参数才可用作默认值。

To set an object property as the default value for a parameter, begin by selecting an object parameter to configure. Let's assume a more generic action type called `Change Airplane Details` where, for example, users need to know the current value of a property before making edits. This can be achieved by configuring the value of each parameter to be prefilled from the currently selected object (in our case, the `Plane` object to modify). Only object reference parameters that are placed above the parameter in the input list are available to be used as a default value.
![Configuring a property default value](/docs/resources/foundry/action-types/default_value_object_configuration.png)
在 Object Explorer 中，`Change Airplane Details` Action 将使用当前值进行预填。在这种情况下，用户可以选择仅修改一个 Property 而保持其他 Property 不变。此相同的默认逻辑将出现在提交该 Action 的任何位置。请注意，一旦 Action 用户更新了此默认值，`Lifetime Hours` 值就会显示为已编辑状态。

In Object Explorer, the `Change Airplane Details` action will be prefilled with current values. In this case, users could choose to modify just one property and keep the rest the same. This same default logic will be present anywhere the action is submitted. Note that the `Lifetime Hours` value shows as edited once this default value is updated by the action user.
![Object default value](/docs/resources/foundry/action-types/default_value_object_example.png)
### Type class prefills
Action 参数可以使用 Type Classes 进行标注，从而预填特殊值（例如自动生成的 UUID 或当前用户的 ID）。Ontology 文档中提供了 [可用 Type Classes 的完整列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

Action parameters can be prefilled with special values (such as automatically-generated UUIDs or the current user's ID) by annotating them with type classes. The Ontology documentation has [a complete list of the available type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
![Configuring a type class prefill](/docs/resources/foundry/action-types/default_value_type_class_configuration.png)
在大多数情况下，应将参数的可见性设置为 `hidden`，以防止用户手动更改这些特殊的预填值。

In most cases, you should set the parameter visibility to `hidden`, so that users do not manually change these special prefilled values.