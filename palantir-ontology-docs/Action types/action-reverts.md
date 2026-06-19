<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/action-reverts/
---
# Revert or undo actions
[Ontology Manager](/docs/foundry/ontology-manager/overview/) 中的 Action 撤销（Action reverts）允许在 Action 应用后立即将其撤销（即撤消）。您可以通过在任何成功的 Action 应用后的成功消息中选择 **Undo（撤销）** 来撤销该 Action。

Action reverts in [Ontology Manager](/docs/foundry/ontology-manager/overview/) allow an action to be reverted (that is, undone) immediately after the action has been applied. You can revert an action by selecting **Undo** in the success message after any successful action application.
新创建的 Action 默认是可撤销的。

New actions are revertible by default.
> **ℹ️ 注意**

> Action 撤销仅适用于 Object Storage V2；这意味着只有修改或在 [OSv2](/docs/foundry/object-backend/object-storage-v2-breaking-changes/) 中创建 Object Type 的 Action 才能被撤销。如果您的 Object Type 当前未存储在 Object Storage V2 中，您可以按照本 [guide](/docs/foundry/object-backend/osv1-osv2-migration/#migrate-from-object-storage-v1-phonograph-to-object-storage-v2) 进行迁移。
> **ℹ️ 注意**

> Action reverts are only available for Object Storage V2; meaning that only actions that modify or create an object type in [OSv2](/docs/foundry/object-backend/object-storage-v2-breaking-changes/) can be reverted. If your object types are not currently stored in Object Storage V2, you can migrate by following this [guide](/docs/foundry/object-backend/osv1-osv2-migration/#migrate-from-object-storage-v1-phonograph-to-object-storage-v2).
## Configure a revertible action
目前，Action 只能由应用该 Action 的用户撤销。

Currently, actions can only be reverted by the user who applied the action.
在 Action 的 **Form（表单）** 选项卡中，开启 **Allow revert after action submission（允许在 Action 提交后撤销）** 按钮。一旦此开关被正确配置并保存到 Ontology，您的 Action 即可被撤销。

In the **Form** tab of an action, toggle on the **Allow revert after action submission** button. Once this toggle is correctly configured and saved to the Ontology, your action can be reverted.
![Screenshot of action reverts in the Form section](/docs/resources/foundry/action-types/action-reverts-form-button.png)
对于 2024 年 5 月之后创建且仅修改 OSv2 Object Type 的 Action，**Form（表单）** 选项卡中的 **Allow revert after action submission（允许在 Action 提交后撤销）** 开关将默认启用。如果 Action 创建于 2024 年 5 月之前并修改 OSv2 中的 Object Type，则 Action 撤销不会默认开启，但可以手动启用。

The **Allow revert after action submission** toggle in the **Form** tab will be enabled by default for actions created after May 2024 that only modify OSv2 object types.
If an action existed before May 2024 and modifies an object type in OSv2, action reverts will not be toggled on by default but can be manually enabled.
如果 Action 仅修改 OSv1 Object Type，则您将无法撤销该 Action。

You will not be able to revert an action if it only modifies OSv1 object types.
## Revert an action
> **ℹ️ 注意: 撤销 Action**

> 以下提示框是您撤销 Action 的唯一机会。在执行删除操作时，这一点尤为重要。
> **ℹ️ 注意: Revert action**

> The toast below is your only opportunity to revert the action. This is especially important to note when performing delete actions.
成功撤销后，用户将看到与原始操作成功时类似的提示，如下所示。

Once reverted successfully, users will see a similar toast to the original action success as shown below.
Edits applied:
![Toast notification stating: "Edits successfully reverted".](/docs/resources/foundry/action-types/action-reverts-revert-action.png)
Edits reverted:
![Toast notification stating: "Edits successfully applied".](/docs/resources/foundry/action-types/action-reverts-edits-reverted.png)
## Caveats
在某些情况下，操作撤销可能会失败：

An action revert may fail in some cases:
* 一旦对对象进行了任何后续编辑，即使编辑的是不同的 property，也无法撤销该对象上的操作。换句话说，只有当操作是对象上最近的编辑时，才能撤销该对象上的操作。
* 如果在操作提交后关闭了操作撤销功能，则无法撤销该操作，即使之后再次开启了操作撤销功能。

* An action on an object cannot be reverted once any subsequent edit has been made to the object, even if the edit is on a different property. In other words, an action on an object can only be reverted if the action is the most recent edit to an object.
* An action cannot be reverted if action reverts has been toggled off after action submission, even if action reverts have been toggled on again.
操作撤销仅撤销对对象实例的编辑，但不会撤销副作用，例如 notifications 或 webhooks，也不会以与应用操作相同的方式调用它们。

An action revert only reverts the edits to the object instance, but it will not revert side effects, such as notifications or webhooks, nor will it call them in the same way that the applied action would have.
### Undoing a delete action without the revert action toast
如果执行了 delete 操作并希望撤销该删除，但撤销操作提示已不再可用，则唯一的补救措施是：

If a delete action is performed and you wish to undo the deletion, but the revert action toast is no longer available, the only remediation options available are to:
* 迁移到新的 object type，并使用 functions 复制所需的编辑；或

* 删除该 object type 上的所有编辑。

* Migrate to a new object type and copy over the desired edits using functions; or
* Drop all edits on the object type.