<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/manage-versions/
---
# Object View versioning
对 Object View 的已保存编辑将作为新版本进行存储。一个版本可以包含多项更改,例如添加、编辑和删除 tabs。版本管理使您能够:

Saved edits to an Object View will be stored as a new version. A version can contain several changes, such as adding, editing, and deleting tabs. Versioning enables you to:
* 通过增量保存更改来安全地迭代 Object Views
* 控制发布和向用户展示的版本
* 在新版本包含错误时重新发布旧版本
* 通过为版本添加描述来与其他编辑者协作

* Iterate on Object Views safely by saving your changes incrementally
* Control which version is published and visible to users
* Republish older versions in case newer versions contain errors
* Collaborate with other editors by adding descriptions to versions
Object View 中包含的每个 Workshop module 都有其独立的[版本](/docs/foundry/workshop/versions/)。两个版本号都会显示在 [Object View editor header](/docs/foundry/object-views/config-object-views/#use-the-object-view-editor)中。

There are separate [versions for each Workshop module](/docs/foundry/workshop/versions/) included in the Object View. Both version numbers appear in the [Object View editor header](/docs/foundry/object-views/config-object-views/#use-the-object-view-editor).
## Save new versions
编辑 Object View 后,您可以通过选择 Object View editor header 中的 **Save** 按钮来保存更改。如果启用了 **Automatically publish new versions**,此按钮将显示为 **Save and publish**,并且会同时发布 tab 更改以及对当前 Workshop module 所做的任何更改。默认情况下,自动发布是启用的。

After editing the Object View, you can save changes by selecting the **Save** button in the Object View editor header. If **Automatically publish new versions** is enabled, this button will display **Save and publish** instead, and will publish both tab changes and any changes to the current Workshop module. Automatic publishing is enabled by default.
禁用 **Automatically publish new versions** 后,将显示两个独立的按钮,分别用于保存和发布。**Save** 按钮将保存 tab 和 workshop module 的更改,**Publish** 按钮会将这两项更改发布给用户。

Disabling **Automatically publish new versions** will display two separate buttons for saving and publishing. The **Save** button will save both tab and workshop module changes, and the **Publish** button will publish both of these changes to the user.

> 📷 **[图片: The 'Save and publish' Object View button.]**

> 📷 **[图片: The 'Save and publish' Object View button.]**

当您编辑 Workshop module 时,它会像其他 Workshop module 一样定期自动保存,但这些更改在 Object View 发布之前对用户不可见。

As you edit the Workshop module, it will be periodically auto-saved like any other Workshop module, but these changes will not be visible to users until the Object View is published.
> **ℹ️ 注意**

> 如果您的 Object View 正被大量用户积极使用,或者有多个编辑者在协作编辑该 view,我们建议禁用自动发布。这可以改善协作,并降低破坏用户工作流的可能性。
> **ℹ️ 注意**

> If your Object View is actively used by many users or there are multiple editors collaborating on the view, we recommend disabling automatic publishing. This improves collaboration and lowers the chances of breaking user workflows.
## Access prior versions
要查看 Object View 的先前版本列表,请选择 Object View editor header 中的蓝色 Object View 版本号。这将打开一个对话框,显示所有先前版本的日期、作者和描述。在该对话框中,可以预览所有版本。

To view a list of prior versions of the Object View, select the blue Object View version number in the Object View editor header. This will open a dialog displaying the date, author, and description of all prior versions. From this dialog, all versions can be previewed.
* 当前已发布的版本会标有绿色对勾。
* 之前已发布的版本会显示为灰色对勾。
* 从未发布过的版本则没有对勾。

* The currently published version will be marked with a green checkmark.
* Prior published versions will show a grey checkmark.
* Versions that were never published will not have a checkmark.

> 📷 **[图片: Object View 编辑历史记录面板。]**

> 📷 **[图片: The Object View edit history panel.]**

