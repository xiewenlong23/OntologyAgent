<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-edits/user-edit-history/
---
# Enable user edit history
跟踪已索引到 Object Storage V2 中的 object 的用户编辑历史记录。可通过 Ontology Manager 的 **Datasources** 选项卡中的 **Track user edit history** 切换按钮启用或禁用此功能，如下方截图所示。

Tracking the history of user edits to objects indexed into Object Storage V2. Enable or disable this feature using the **Track user edit history** toggle in the **Datasources** tab of the Ontology Manager, as shown in the screenshot below.
![Track user edit history toggle](/docs/resources/foundry/object-edits/track-user-edits-history.png)
要允许用户编辑，必须启用 [Edits toggle](/docs/foundry/object-edits/how-edits-applied/)。

To allow user edits, the [Edits toggle](/docs/foundry/object-edits/how-edits-applied/) must be enabled.
## Common issues and notes
* 编辑历史记录反映的是在启用 **Track user edit history** 之后对 object 所做的更改。启用此功能之前的任何更改都不会被跟踪。

* 启用 **Track user edit history** 后，需要几分钟时间进行初始化。在此短暂的初始化期间，用户无法对这些 object 执行操作。

* 如果您正在从 Object Storage V1 迁移到 Object Storage V2，并且希望保留编辑历史记录，请确保在迁移过程中勾选 `preserve edit history`。

* 可以访问 object 当前状态（具有相同主键的 object）的用户可以访问该 object 的全部历史记录。这意味着，如果某个 object 被删除并重新创建，用户仍然可以查看删除操作发生之前的历史记录。

* The edit history reflects the changes made to objects after enabling the **Track user edit history**. Any changes prior to the activation of this feature will not be tracked.
* Once you enable the **Track user edit history**, it takes a few minutes to initialize. During this short period, users can't perform actions on these objects.
* If you are migrating from Object Storage V1 to Object Storage V2, ensure that `preserve edit history` is checked during the migration if you want to retain the edit history.
* Users who have access to the current state of an object (object with the same primary key) can access the entire history of the object. This implies that if an object is deleted and recreated, users can still see the history that occurred prior to the deletion action.
启用 **Track user edit history**（追踪用户编辑历史）后，可以将 [Edit History widget](/docs/foundry/workshop/widgets-edits-history/) 添加到 Workshop modules 或 Workshop-backed object views 中，以显示编辑历史。

After enabling **Track user edit history**, the [Edit History widget](/docs/foundry/workshop/widgets-edits-history/) can be added to Workshop modules or Workshop-backed object views to display edit histories.
## Disable edit history
禁用 **Track user edit history** 将永久删除该 object type 的所有现有编辑历史。在保存 ontology 之前，用户将收到警告，并必须确认已了解编辑历史将被删除。

Disabling **Track user edit history** permanently deletes all existing edit histories for this object type. Before saving the ontology, users will receive a warning and must confirm an acknowledgment that edit history will be deleted.
![Disable user edit history toggle](/docs/resources/foundry/object-edits/disable-edits-history.png)