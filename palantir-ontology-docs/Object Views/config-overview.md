<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/config-overview/
---
# Configured Object View overview
已配置的 Object View 是 object 数据的可定制、可复用的呈现方式。您可以通过 [Workshop modules](/docs/foundry/workshop/overview/) 为 object type 构建 [full](/docs/foundry/object-views/use-full-views-in-platform/) 和 [panel](/docs/foundry/object-views/use-panel-views-in-platform/) 两种 Object View，从而灵活地在整个平台中以不同方式呈现 object。

Configured Object Views are customizable, reusable representations of object data. You can build both [full](/docs/foundry/object-views/use-full-views-in-platform/) and [panel](/docs/foundry/object-views/use-panel-views-in-platform/) Object Views for an object type through [Workshop modules](/docs/foundry/workshop/overview/), enabling flexibility in how objects are represented across the platform.
Foundry 默认会为所有 Object Type 创建一个 [standard Object View](/docs/foundry/object-views/standard-object-views/)。当您创建一个已配置的 Object View 时，它将成为用户的默认视图，不过用户可以通过 Object View 自带的切换按钮切换回 standard Object View。此外，在使用自定义 header 的 Palantir 应用程序（例如 Gaia 或 Vertex）中，用户可以将鼠标悬停在 Object View 渲染界面中的省略号抽屉图标上，在 standard 视图和已配置视图之间进行切换。

Foundry creates a [standard Object View](/docs/foundry/object-views/standard-object-views/) for all object types by default. When you create a configured Object View, it becomes the default view for users, though they can switch back to the standard Object View through a toggle button packaged with the Object View. Additionally, users can hover over the ellipsis drawer icon in an Object View rendered in Palantir applications that use their own custom header, such as Gaia or Vertex, to toggle between standard and configured views.
![The standard and configured Object View toggle in an application is displayed.](/docs/resources/foundry/object-views/toggle-core-custom-view-in-selection.png)
> **ℹ️ 注意**

> 在 Workshop 中暂时还无法在 standard 和已配置的 Object View 之间进行切换。
> **ℹ️ 注意**

> The ability to toggle between standard and configured Object Views is not yet available in Workshop.
## Default configurations
默认的已配置 Object View 会针对每个 Object Type 自动创建。默认的完整 Object View 包含一个突出 Property 列表（如果没有突出 Property，则包含所有未隐藏的 Property）以及 Object 的 Link 列表。默认面板包含相同的 Property 列表。默认视图会自动更新以反映对 Object Type 所做的更改（例如新增 Property 或 Property 重命名），但一旦 Object View 被编辑，它就会变成用户管理（user-managed）的模式，所有后续更新都必须手动完成。

Default configured Object Views are automatically created for each object type. The default full Object View contains a list of prominent properties, or all non-hidden properties if none are prominent, and a list of the object's links. The default panel contains the same list of properties. The default views will dynamically update to reflect changes made to the object type, such as new properties or property renames, but once an Object View is edited it becomes user-managed and all further updates must be made manually.
### Permissions
编辑 Object Type 的 Object View 所需的权限，取决于该 Object Type 是否使用 [Ontology roles](/docs/foundry/ontology-manager/ontology-roles-migration/)：

The permissions required to edit the Object View for an object type depend on whether the object type uses [Ontology roles](/docs/foundry/ontology-manager/ontology-roles-migration/):
* 如果该 Object Type 未使用 Ontology roles，则用户必须拥有 [Control Panel](/docs/foundry/administration/enrollments-and-organizations-permissions/) 中的 `Object View Admin` 应用程序权限，以及 Object Type 任何输入 datasource 上的 `Editor` role。

* 如果该 Object Type 使用 Ontology roles，则用户仅需拥有该 Object Type 的 `Ontology Editor` role 即可。

* If the object type does not use Ontology roles, a user must have the `Object View Admin` application permission in [Control Panel](/docs/foundry/administration/enrollments-and-organizations-permissions/), as well as the `Editor` role on any of the object type's input datasources.
* If the object type uses Ontology roles, the user only requires the `Ontology Editor` role on the object type.
除非您通过 legacy configuration options 手动将 Object View 标签页的 Workshop module 转换为 standalone module，否则该 Workshop module 的权限将由 Object Type 管理。这可以确保 module 与 Object Type 之间的权限保持一致，从而拥有编辑或查看该 Object Type 权限的用户，也能够编辑或查看 Object View 中的所有 module。

Unless you manually convert the Workshop module for an Object View tab to a standalone module through legacy configuration options, the Workshop module's permissions will be managed by the object type. This ensures that permissions between the module and the object type are kept aligned, so users with permission to edit or view the object type will also be able to edit or view all modules inside the Object View.
### Edit configured Object Views
可以通过多种方式访问已配置 Object View 的配置。

There are many ways to access configured Object View configuration.
可以在 Ontology Manager 的 **Object views** 标签页中预览 Object Type 的 Object View。在 header 中，您可以选择并固定一个默认展示对象以进行预览。您还可以预览完整和面板形式的 form factor，并测试 Object View 在浅色和深色模式下的显示效果。可以通过点击 header 右侧的 **Edit** 选项来访问已配置 Object View 的编辑。

The Object Views for an object type can be previewed in the **Object views** tab in Ontology Manager. In the header, you can select and pin a default display object to preview. You can also preview the full and panel form factors, and test how the Object View appears in light and dark mode. Editing the configured Object View can be accessed using the **Edit** option in the right side of the header.
![Editing an Object View from Ontology Manager.](/docs/resources/foundry/object-views/ontology-manager-object-view-edit.png)
在 Object Explorer 中，查看某个对象时，可以通过选择 **More > Advanced > Edit object view** 来访问该 Object Type 的已配置 Object View。

In Object Explorer, an object type's configured Object View can be accessed when viewing an object by selecting **More > Advanced > Edit object view**.
![Editing an Object View from Object Explorer.](/docs/resources/foundry/object-views/object-explorer-object-view-edit.png)
在应用程序中查看面板 Object View 时，可以通过将鼠标悬停在省略号下拉菜单上并选择 **Edit** 来访问配置。该下拉菜单仅对拥有 Object View 编辑权限的用户显示。

When viewing a panel Object View within an application, configuration can be accessed by hovering over the dropdown ellipsis and selecting **Edit**. The dropdown only appears for users with permission to edit the Object View.

> 📷 **[图片: Editing a panel Object View.]**

> 📷 **[图片: Editing a panel Object View.]**

这些编辑入口将引导您进入已配置 Object View 的编辑器，在那里您可以管理 Object View 的标签页，并使用 Workshop module 的所有标准功能编辑内容。发布后，所做的编辑将应用于该 Object Type 的所有对象。有关编辑的更多信息，请参考 [完整 Object View 配置](/docs/foundry/object-views/config-object-views/) 和 [面板 Object View 配置](/docs/foundry/object-views/config-panel-views/)。

These edit entry points lead to the configured Object View editor, where the Object View tabs can be managed, and content can be edited with all the standard features of a Workshop module. Once published, edits will apply to all objects of the object type. For more editing information, refer to the [full Object View configuration](/docs/foundry/object-views/config-object-views/) and [panel Object View configuration](/docs/foundry/object-views/config-panel-views/).