<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/save-changes/
---
# Save changes to the Ontology
## Save your changes
您在 Ontology Manager 中所做的任何更改都会在本地以 work-in-progress 状态存储。为了使这些 Ontology 更改可供其他人使用并反映在面向用户的应用程序中，您必须保存您的更改。要保存更改：

Any changes you make in the Ontology Manager are stored locally in a work-in-progress state. For these Ontology changes to be available for others and reflected in user-facing applications, you must save your changes. To save changes:
1. 从应用程序右上角的 Application header 中选择 **Save**。

1. Select **Save** from the Application header at the top-right corner of the application.

> 📷 **[图片: Save button]**

> 📷 **[图片: Save button]**

2. 打开 **Review edits** 对话框以查看您的所有更改。

3. 最后，选择 **Save** 以更新 Ontology。

2. Open the **Review edits** dialog to review all your changes.
3. Finally, select **Save** to update the Ontology.

> 📷 **[图片: Save button in review dialog]**

> 📷 **[图片: Save button in review dialog]**

## Handle errors and warnings
如果 **Save** 按钮呈灰色显示，可能是存在阻止您保存的错误。要解决此问题，您可以：

If the **Save** button is grayed out, you may have an error that is stopping you from saving. To resolve this, you can:
* 滚动浏览您的更改并查看内联的错误消息，或

* 选择 **Review edits** 对话框顶部的 **Errors** 选项卡，以查看阻止您保存的错误。

* Scroll through your changes and view the error messages in line, or
* Select the **Errors** tab at the top of the **Review edits** dialog to see the errors preventing you from saving.
**Review edits** 对话框还会在内联和 **Warnings** 选项卡中显示建议您进行的更改的警告。错误必须先处理才能保存，而警告不会阻止您保存。

The **Review edits** dialog will also show you warnings in-line and in the **Warnings** tab for changes you are encouraged to make. While errors need to be handled in order to save, warnings will not prevent you from saving.

> 📷 **[图片: Review errors]**

> 📷 **[图片: Review errors]**

如果您收到错误，可以使用打开快捷方式导航到您在保存前需要编辑的资源。

If you receive an error, you can use the open shortcut to navigate to a resource you need to edit before saving.

> 📷 **[图片: Navigate to a resource to edit]**

> 📷 **[图片: Navigate to a resource to edit]**

> **ℹ️ 注意**

> 对 Function 的更改只能在 Functions 仓库中进行，而不能在 Ontology Manager 中进行。您可以从 Ontology Manager 中的 Functions Entity 视图导航到 Functions Repository。
> **ℹ️ 注意**

> Changes to Functions can only be made in the Functions repository, and not in the Ontology Manager. You can navigate to the Functions Repository from the Functions Entity view in the Ontology Manager.
## Handle updates and merge conflicts
如果自您开始进行更改以来 Ontology 已被其他用户保存，则 **Save** 按钮也可能呈灰色显示。您需要从 Review edits 对话框顶部选择 **Update** 以将其他用户的更改与您自己的更改合并。

The **Save** button may also be grayed out if the Ontology has been saved by another user since you began making your changes. You will need to select **Update** from the top of the Review edits dialog to merge the other user’s changes with your own.

> 📷 **[图片: Update Ontology with other edits]**

> 📷 **[图片: Update Ontology with other edits]**

其他用户所做的更改与您工作状态中的更改之间可能存在合并冲突。系统将提示您解决这些冲突。您可以选择保留 Ontology 最新版本中的更改，或使用您工作状态中的更改覆盖它们。

It is possible that there are merge conflicts between changes another user has made and the changes in your working state. You will be prompted to resolve them. You can choose between keeping the changes in the latest version of the Ontology or overriding them with the changes in your working state.

> 📷 **[图片: Merge conflict in Ontology edits]**

> 📷 **[图片: Merge conflict in Ontology edits]**

## Discard your changes
您编辑的 Ontology 中的每个资源在 **Review edits** 对话框中都会有自己的条目。您可以将鼠标悬停在 **Review edits** 对话框中的条目上，然后选择垃圾桶图标，以丢弃您对该资源所做的更改。

Each resource in the Ontology that you edit will have its own entry in the **Review edits** dialog. You can discard the changes you made to a resource by hovering over the entry in the **Review edits** dialog and selecting the trash icon.

> 📷 **[图片: Discard edits]**

> 📷 **[图片: Discard edits]**

您可以随时通过选择应用程序右上角标题中的 **Discard** 按钮，或通过选择 **Review edits** 对话框底部的 **Discard** 来丢弃您对 Ontology 所做的所有未保存更改。

You can discard all unsaved changes you made to the Ontology at any point by selecting the **Discard** button in the header at the top right of the application, or by selecting **Discard** at the bottom of the **Review edits** dialog.

> 📷 **[图片: Discard all edits]**

> 📷 **[图片: Discard all edits]**

## Respond to a warning message
当您在 **Review edits** 对话框中查看更改时，可能会收到一条警告消息，提示您在保存之前确认该警告。

As you review your changes in the **Review edits** dialog, you may get a warning message that prompts you to confirm the warning before saving.
对 Object Type 及其 Property 的编辑可能会对依赖这些 Object Type 的应用程序产生破坏性影响。此外，如果 Object Type 启用了 writeback，则在对该 Object Type 进行编辑时应格外小心，以确保不会删除对该类型 Object 所做编辑的历史记录。

Edits to object types and their properties can have an application-breaking impact on applications relying on those object types. Furthermore, if an object type has writeback enabled, extra caution should be taken when making edits to that object type to ensure that the history of edits made to objects of that type is not removed.
有关哪些更改可能具有破坏性的完整描述，请阅读有关 [potential breaking changes](/docs/foundry/object-link-types/edit-object-type/) 的更多信息。

For a full description of which changes can be destructive, read more about [potential breaking changes](/docs/foundry/object-link-types/edit-object-type/).
在阅读完警告消息中详述的更改影响并理解这些更改的含义后，您可以输入您编辑的实体的名称以继续保存。

Once you have read through the impact of your changes detailed in the warning message and understand the implications of those changes, you can type in the name of the entity you edited to proceed with saving.

> 📷 **[图片: Warning message for edits]**

> 📷 **[图片: Warning message for edits]**

## Troubleshooting when a save fails
如果您在保存时，为 Ontology 提供支持的后端服务遇到问题，您将收到一条错误消息 "toast"（弹出通知），如下图所示。在说明您无法保存的原因的文字末尾，将打印错误消息的名称。错误消息名称将以 `OntologyMetadata:` 或 `Phonograph2:` 前缀开头。

If the backend services powering the Ontology encounter a problem when you save, you will receive an error message "toast" (pop-up), as in the image below. At the end of the text explaining why you can’t save, the name of the error message will be printed. The error message name will begin with the prefix `OntologyMetadata:` or `Phonograph2:`.

> 📷 **[图片: Error message]**

> 📷 **[图片: Error message]**

在整个 Ontology 文档中，都引用了与对 Ontology 所做的不同更改相关的最常见错误。如果您看到错误消息，请在文档中搜索它，以查看该错误及其补救措施是否已有记录。

Throughout the Ontology documentation, there are references to the most common errors associated with different changes made to the Ontology. If you see an error message, search for it in the documentation to see if the error and its remediation are documented.