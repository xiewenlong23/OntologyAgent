<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/upload-attachments/
---
# Upload attachments
Actions 支持从 Workshop、Object Explorer、Object Views、Quiver 和 Slate 上传附件。查看、编辑和删除附件的权限与它们所上传到的对象一致。例如，如果用户对某个对象拥有查看权限，他们将能够查看和下载存储在该对象上的附件。替换现有附件将需要该对象的编辑权限。

Actions support uploading attachments from Workshop, Object Explorer, Object Views, Quiver, and Slate. Permissions to view, edit, and delete an attachment are consistent with the object to which they are uploaded. For example, if a user has view permissions to an object, they will be able to view and download attachments stored on this object. Replacing an existing attachment would require edit permissions on the object.
您可以上传单个附件或附件列表。要使用 actions 上传附件，请按照 action types 和 object types 的配置步骤进行操作。

You can upload a single attachment or a list of attachments. To upload an attachment using actions, follow the configuration steps for both action types and object types.
## Configuring action types
在参数配置视图中，选择 **Attachment** 作为参数类型。附件只能使用附件参数类型上传。对象支持数据集中对应的列必须是 **String**，并且所编辑的对象 property 必须是 **Attachment** 类型。

In the parameter configuration view, select **Attachment** as the parameter type. Attachments can only be uploaded using attachment parameter types. The corresponding column in the object-backing dataset must be a **String** and the edited object property must be of type **Attachment**.
若要一次上传多个媒体文件，请选择 **Allow multiple values**。请注意，要在单个 action 中支持多个媒体文件，需要在 [object type configuration](#configuring-object-types) 中额外切换 **Allow multiple**，具体说明见下文。

To upload several media files at once, select **Allow multiple values**. Note that support for several media files in one action requires an additional toggle during [object type configuration](#configuring-object-types) to **Allow multiple**, as described below.
## Configuring object types
在 object 详情视图中，将 property 类型选择为 **Attachment**。附件只能上传到 attachment 类型的 property。

In the object detail view, select **Attachment** as the property type. Attachments can only be uploaded to attachment property types.
若要向一个 property 上传多个媒体文件，请切换 **Allow multiple**。在这种情况下，对象后备数据集中的 property 必须是 **Array** 类型。

To upload several media files to one property, toggle **Allow multiple**. In this case, the property in the object-backing dataset must be an **Array**.
## Architecture and limits
附件一旦添加到 action 表单中，就会立即上传到 Foundry。提交表单后，查看、编辑和删除附件的权限将根据用户对底层 object type 的权限进行推断。如果表单提交失败或被取消，未关联的附件将不再可直接访问，并将在一定时间后自动永久删除。同样，属于已删除 object 的附件或不再映射到 object 的附件（当对应的 property 被删除时会发生这种情况）也将不再可直接访问，并最终自动永久删除。

Attachments are immediately uploaded to Foundry once they are added to an action form. Upon form submission, permissions to view, edit, and delete an attachment are inferred from the user's permissions on the underlying object type. If form submission fails or is cancelled, the outstanding attachment is no longer directly reachable and will automatically be permanently deleted after some time. Similarly, attachments that belong to deleted objects or are no longer mapped to an object (which occurs when the corresponding property is deleted) are no longer directly reachable and will eventually automatically be permanently deleted.
附件功能同时支持 logic-backed 和 function-backed action。全局固定文件大小限制为 200MB。

Attachments are supported for both logic-backed and function-backed actions. There is a global, fixed file size limit of 200MB.
* 每个附件在其生命周期内最多可链接到十个 object。如果一个附件已经链接到十个 object，则即使其中一个或多个原始链接的 object 已被删除，也无法再将其链接到其他 object。达到十个链接 object 的上限后，您可以再次将该文件作为新附件上传，以链接到更多 object。

* Each attachment can be linked to a maximum of ten objects in its lifetime. If an attachment has been linked to ten objects, it cannot be linked to any other objects even if one or more of the original linked objects has been deleted. After reaching this limit of ten linked objects, you can upload the file again as a new attachment to link it to more objects.