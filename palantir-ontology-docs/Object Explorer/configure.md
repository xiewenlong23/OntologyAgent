<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/configure/
---
# Configure Object Explorer
### Customizable object type Groupings on Home Page
要创建 object type 并将其添加到 group，请访问 Ontology Manager 中该 object type 的 [metadata widget](/docs/foundry/object-link-types/create-object-type/#add-metadata-for-a-new-object-type)。请注意，您必须拥有该 Ontology 的 editor 权限才能创建 object type 并将其添加到 group。

To create and add an object type to a group, visit the object type's [metadata widget](/docs/foundry/object-link-types/create-object-type/#add-metadata-for-a-new-object-type) in the Ontology Manager. Note that you must have editor permission on the Ontology to create and add an object type to a group.
如果配置了自定义 groups，则任何不属于某个 group 的非隐藏 object types 将被放置在页面底部名为 "Other" 的 group 中。

If there are custom groups configured, any non-hidden object types that do not belong to a group will be placed in a group at the bottom of the page called “Other”.
### Linking to object view from Actions success toast
Action 成功应用后，可以配置 success toast（弹出确认消息），使其显示指向已创建或修改的 object instance 的 object view 的超链接。这为新创建或修改的 objects 提供了快速访问 object view 的途径。

Once an Action has been successfully applied, the success toast (pop-up confirmation message) can be configured to display a hyperlink to the object view for the object instance that has been created or modified. This provides quick access to the object view for newly-created or modified objects.
要以此方式配置 success toast，您需要将一个新的 type class（见下方代码）添加到相关 *create object* Action 的 Primary Key 参数，或添加到相关 *modify object* Action 的 Object Reference List 参数。可以使用 Ontology Editor app 添加该 type class，这需要您拥有 ontology 编辑权限。

To configure the success toast in this way, you will need to add a new type class (see code below) to the Primary Key parameter of the relevant *create object* Action or to the Object Reference List parameter of the relevant *modify object* Action. The type class can be added using the Ontology Editor app, which requires you to have ontology editing permissions.
```yaml
kind: "actions"
name: "view_object_with_type:<OBJECT_TYPE_ID>"
```
让我们通过一个示例来演示如何添加一个 success toast，链接到新创建 object instance 的 object view。

Let’s walk through an example of adding a success toast that links to the object view for a newly-created object instance.
1. Ontology Action "Create New Aircraft" 允许我们创建一个新的 Aircraft object instance。

1. The Ontology Action “Create New Aircraft” allows us to create a new Aircraft object instance.

> 📷 **[图片: Action Success Toast Typeclass]**

> 📷 **[图片: Action Success Toast Typeclass]**

2. 在弹出菜单中，输入相关信息，然后选择 "Submit"。在这种情况下，将创建一个 Id 为 `187`、Aircraft Registration 为 `Q-AHE` 的 Aircraft object instance。

2. In the pop-up menu, input the relevant information and then select “Submit”. In this case, an Aircraft object instance with Id of `187` and Aircraft Registration of `Q-AHE` will be created.

> 📷 **[图片: Apply Action]**

> 📷 **[图片: Apply Action]**

3. 既然我们已在 Primary Key 参数上添加了上述 type class，success toast 将显示指向新创建 object instance `Q-AHE` 的超链接。点击该超链接将跳转到该 object instance 的 object view。

3. Now that we have added the type class described above on the Primary Key parameter, the success toast will display a hyperlink to the newly-created object instance `Q-AHE`. Clicking on the hyperlink will bring us to the object view of this object instance.

> 📷 **[图片: Success Toast]**

> 📷 **[图片: Success Toast]**

### Hiding Actions in Object Explorer
Actions 将按照 [action type documentation](/docs/foundry/action-types/use-actions/) 中的描述，自动显示在 Object Explorer 中的三个位置。要隐藏 object type 的某个 Action，请将 `hubble-oe:hide-action` type class 添加到 Ontology Editor app 中的 Object Reference List 参数。您需要拥有编辑该 ontology 的权限才能执行此操作。

Actions will automatically be shown in three places across Object Explorer as described in the [action type documentation](/docs/foundry/action-types/use-actions/). To hide an Action of an object type, add the `hubble-oe:hide-action` type class to the Object Reference List parameter in Ontology Editor app. You will need to have access to edit the ontology to do this.

> 📷 **[图片: Hide Actions Typeclass]**

> 📷 **[图片: Hide Actions Typeclass]**

## Actions on a Dynamic Object Set
> **⚠️ 警告**

> 此功能仍在开发中，*可能*会被弃用，且不会提供自动迁移。因此，使用此功能意味着您需要承担将来手动迁移 Action 的风险。如果您计划使用此特定功能，请先联系您的 Palantir 代表。
> **⚠️ 警告**

> This feature is still in development and is subject to deprecation *without* an automatic migration. Thus, using it means taking a risk that you will need to manually migrate your actions in the future. If you plan to use this particular feature, contact your Palantir representative before doing so.
在某些情况下，您可能希望将探索的结果用作动态 object set，而非静态 object set。动态 object set 以所应用筛选条件的表示形式保存。因此，当有新数据匹配（或不匹配）这些筛选条件时，object set 将自动更新。

In some cases, you may want to use the results of an exploration as a dynamic object set, rather than a static object set. Dynamic object sets are saved as the representation of the filters applied. As such, when new data matches (or does not match) those filters, the object set will be updated.
此功能最典型的用例是将动态 object set 的引用作为 property 值添加到 object instance 上。

The most typical use case of this feature is to add a reference to a dynamic object set as a property value on an object instance.
让我们通过一个示例来演示如何创建一个 action，使我们能够根据飞机制造商序列号（MSN）将一组动态的 `Aircraft` object 分配给 `Airline` object。

Let's walk through an example of creating an action that allows us to assign a dynamic set of `Aircraft` objects to an `Airline` object, based on the Aircraft Manufacturer's Serial Numbers (MSNs).
1. 确保 `Airline` object type 拥有一个 `String` property（本例中为 `Aircraft Set`），您可以在其中添加对一组 "Aircraft" object 的引用作为值。为此 property 启用值格式化（value formatting），并从下拉菜单中选择 **Resource RID**。这样，分配给此 property 的 object set RID 将在 Object Explorer 中以 object set 链接的形式显示。

1. Ensure that the `Airline` object type has a `String` property (in this case `Aircraft Set`) where you can add a reference to a set of "Aircraft" objects as a value. Enable value formatting for this property, and select **Resource RID** from the dropdown. This way, the object set RIDs assigned to this property will appear as a link to the object set in Object Explorer.

> 📷 **[图片: Value Formatting]**

> 📷 **[图片: Value Formatting]**

2. 现在您可以创建 action 了。在 action 上，在 `Airline` object type 的 `Aircraft Set` property 上添加一个 **Modify Object** rule。

2. Now you're ready to create the action. On the action, add a **Modify Object** rule on the `Airline` object type's `Aircraft Set` property.

> 📷 **[图片: Modify Object Rule]**

> 📷 **[图片: Modify Object Rule]**

3. 在 `Aircraft Set` parameter 上添加以下 type class，其中 `<OBJECT_TYPE_ID>` 是您希望此 action 在探索视图中作为可用选项出现的 object type 的 object type ID（本例中为 `Aircraft` object type）。

3. On the `Aircraft Set` parameter, add the following type class, where `<OBJECT_TYPE_ID>` is the object type ID of the object type you want this action to appear as an option for in the exploration view (in this case, the `Aircraft` object type).
```yaml
kind: "hubble-oe-object-set-rid"
name: <OBJECT_TYPE_ID>
```
4. 同样在 `Aircraft Set` parameter 上添加以下 type class，其中 `<RESOURCE_RID>` 是包含您希望授予动态 object set 的正确权限的文件夹的 RID。请注意，这些 object set 不会在 Project 中公开，也无法被搜索——此 RID 仅用于指定已保存的 object set 应获得的权限。

4. Also on the `Aircraft Set` parameter, add the following type class, where `<RESOURCE_RID>` is the RID of a folder that contains the correct permissions you want to grant to the dynamic object sets. Note that the object sets are not exposed in a Project and are not searchable - this RID is only used to specify what permissions the saved object sets should receive.
```yaml
kind: "hubble-oe-security-rid"
name: <RESOURCE_RID>
```
5. 创建 action 后，导航到针对 `Aircraft` object 的 exploration。例如，我们可能希望将所有 MSN 在 5,025 到 5,050 之间的 `Aircraft` 分配给 Frontier Airlines。为此，请筛选出这些 object，然后从 Actions 下拉菜单中选择新创建的 action。

5. Once the action has been created, navigate to an exploration on `Aircraft` objects. As an example, we might want to assign all `Aircraft` with an MSN between 5,025 and 5,050 to Frontier Airlines. To do so, filter down to those objects and select the newly created action from the Actions dropdown.

> 📷 **[图片: Assign Aircraft]**

> 📷 **[图片: Assign Aircraft]**

这将自动为当前 exploration 创建一个动态 object set，并将其分配给您从下拉菜单中选择的 `Airline` object 上的 `Aircraft Set` property。

This will automatically create a dynamic object set for your current exploration and assign it to the `Aircraft Set` property on the `Airline` object you select from the dropdown.

> 📷 **[图片: Choose Airline]**

> 📷 **[图片: Choose Airline]**

6. 现在，在 "Frontier Airlines Inc." object 的 `Aircraft Set` property 中将出现一个指向 MSN 在 5,025 到 5,050 之间的 `Aircraft` 集合的链接。如果 ontology 中新增了任何 MSN 处于该范围内的 `Aircraft`，或者当前集合中的任何 `Aircraft` 从 ontology 中被移除，该集合将自动更新。

6. Now, a link to the set of `Aircraft` with an MSN between 5,025 and 5,050 will appear in the `Aircraft Set` property on the "Frontier Airlines Inc." object. If any new `Aircraft` with an MSN in this range are added to the ontology or any of the `Aircraft` currently in the set are removed from the ontology, the set will automatically be updated.

> 📷 **[图片: Airline Exploration]**

> 📷 **[图片: Airline Exploration]**

7. 使用 Linked Objects Exploration widget，你可以通过访问 "Frontier Airlines Inc." 的 Object View 来查看此动态 object set 的内容：

7. Using a Linked Objects Exploration widget, you can see the contents of this dynamic object set by visiting the Object View for "Frontier Airlines Inc.":

> 📷 **[图片: Linked Objects Exploration]**

> 📷 **[图片: Linked Objects Exploration]**

配置此 widget 时，将 `Initial Exploration` 设置为 **From Object Set RID Property**，并将 `Object Set RID Property` 设置为 **Aircraft Set**。

When configuring this widget, set the `Initial Exploration` to **From Object Set RID Property** and the `Object Set RID Property` to **Aircraft Set**.

> 📷 **[图片: Linked Objects Exploration Configuration]**

> 📷 **[图片: Linked Objects Exploration Configuration]**

### Default Layout Administrative Users
属于 `hubble-exploration-admins` multipass 组的用户，或在 Control Panel 中拥有 `Object Exploration Admin` 应用程序权限的用户，可以对 object type 进行重命名、删除或保存默认布局。布局包括对结果表配置所做的任何更改。如果你是一名 admin 用户，并希望为所有用户将布局设置为默认布局，请在保存布局时在 **Set as default layout** 下勾选 **For all users** 复选框，如下图所示。

A user who belongs to the `hubble-exploration-admins` multipass group, or who has the `Object Exploration Admin` application permission in Control Panel, can rename, delete, or save default layouts for object types. The layout includes any changes that have been made to the results table configuration. If you are an admin user and wish to set a layout as default for all users, under **Set as default layout** tick the **For all users** checkbox when saving the layout, as seen in the image below.

> 📷 **[图片: Edit Default Layout]**

> 📷 **[图片: Edit Default Layout]**

