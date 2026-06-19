<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/parameters-override/
---
# Overrides
Overrides 用于在特定情况下更改 parameter 的行为和配置。通过使用 overrides，parameters 和 forms 可以变得更加灵活，从而无需配置仅有微小差异的独立 action types。合理使用 overrides 可以通过引导用户完成 action 提交流程来改善用户体验。

Overrides are used to change a parameter's behavior and configuration under specific circumstances. Using overrides, parameters and forms can become more flexible, removing the need to configure separate action types with only minor variations. Appropriate use of overrides can improve the user experience by guiding users through an action submission.
例如，假设您有一个用于更改 support ticket object 状态的 action type，并且希望将 action 提交限制为 managers 和 assignees。assignees 可以更改状态，但 managers 必须提供 justification reason。通过使用 overrides，`Justification reason` parameter 可以设置为对 managers 必填且可见，而对 assignees 隐藏且可选。

For example, let's assume that you have an action type which changes the status of a support ticket object and you want to restrict action submission to managers and assignees. While assignees can change the status, managers will have to provide a justification. Using overrides, the `Justification reason` parameter can be made required and visible for managers, while it is hidden and optional for the assignee.
## Add and edit overrides
您可以在 parameter 视图的不同位置添加和编辑 overrides。添加新 override 最简单的方法是直接从 **General** 部分中的 **Value** 选项卡。点击三个选项之一的 **Add override**，您可以通过弹出窗口轻松创建一个 override，它会根据所选选项自动配置该 override。**General** 部分还会显示已为某个选项配置了 overrides 的时间和数量。要编辑现有的 overrides，请选择 override 按钮。

You can add and edit overrides from different places on the parameter view. The easiest way to add a new override is directly from the **Value** tab in the **General** section. By clicking **Add override** on one of the three options, you can easily create an override via the pop-up, which now automatically configured the override based on the selected option. The **General** section also shows when and how many overrides have already been configured for one of the options. To edit existing overrides, select the override button.
![Override pop up](/docs/resources/foundry/action-types/override_pop_up.png)
您也可以通过 **Overrides** 选项卡手动添加 override。overrides 选项卡显示了该 parameter 配置的所有 overrides 的概览。您可以从此处添加 override 块，或者向现有块添加新的 conditions 或 overrides。

You can also add an override manually via the **Overrides** tab. The overrides tab shows an overview of all overrides configured for the parameter. You can add override blocks from here or add new conditions or overrides to existing blocks.
![Override tab](/docs/resources/foundry/action-types/override_tab.png)
## Override block
一个 override 块构成了 overrides 的基础。它同时定义了 conditions（显示在 "if" 部分）和 overrides（显示在 "then" 部分）。每个块的标题显示逻辑的摘要。每个 parameter 可以包含多个 override 块，但是，如果多个块同时为 true，则只会执行第一个块。

An override block presents the basis for overrides. It defines both the conditions (shown in the "if" part) and the overrides (shown in the "then" part). Each block's header shows a summary of the logic. Every parameter can contain multiple override blocks, however, if more than one is true, only the first one will be executed.
![Override block](/docs/resources/foundry/action-types/override_block.png)
### "If" and conditions
每个块可以包含一个或多个 conditions。要了解更多关于 conditions 及其配置方法的信息，请参阅 [submission criteria 文档中的 conditions](/docs/foundry/action-types/submission-criteria/#conditions)。override conditions 与 submission criteria conditions 之间的唯一区别在于，在 override conditions 中只能引用在 form 层级中出现在当前 parameter 上方的 parameters。

Each block can contain one or multiple conditions. To read more about conditions and how to configure them, see the [submission criteria documentation on conditions](/docs/foundry/action-types/submission-criteria/#conditions). The only difference between override conditions and submission criteria conditions is that only parameters which appear above the current parameter in the form hierarchy can be referenced in override conditions.
### "Then" and overrides
**Then** 部分定义了当块的条件满足时将应用的 overrides。每个块的 **Then** 部分可以包含多个 overrides，这些 overrides 会同时应用。一个 override 可以更改 parameter 的 constraints、visibility、requiredness 以及 default values 的配置。如果一个 override 配置为采用与 parameter 上已设置的默认值相同的值，则该 override 上将显示一个警告。

The **Then** section defines the overrides which will be applied when the conditions of the block are met. Each block can contain multiple overrides in its **Then** section, which are all be applied together. An override can change the configuration of the parameter's constraints, visibility, requiredness, and default values. If an override is configured to take on the same value as the default already set on the parameter, a warning will be shown on the override itself.
### Multiple override blocks
您可以为单个 parameter 添加多个 override 块。如果多个块同时为 true，则只会执行第一个 override。

You can add multiple override blocks to a single parameter. If more than one block is true, only the first override is executed.