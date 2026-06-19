<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/dropdown-security/
---
# Object dropdown security considerations
对象下拉验证中的 static value filters 会暴露给所有可以查看该 Action Type 的用户。使用这些过滤器存在将属性值组合暴露给无权查看已过滤对象的用户的风险。此风险可以通过依赖 object properties 或 parameters 来过滤 object set 来缓解。这些值不会直接在 Interface 中显示。

Static value filters in object dropdown validations are exposed to all users who can view the action type. Use of these filters risks exposing property value combinations to users without permissions to view the filtered objects. This risk is mitigated by relying on object properties or parameters to filter the object set. The values are not directly visible in the interface.
## Example: Data privacy issue
举个例子，假设我们有一个 `Document` 对象，具有一个 `Investigation Name` 属性。在我们的 Action Type 中，我们对 object reference parameter 添加一个过滤器，仅显示 **Investigation Name** 为 `Area 51 Investigation` 的 **Documents**。

As an example, imagine we have a `Document` object with an `Investigation Name` property. In our action type, we add a filter on the object reference parameter to only show **Documents** where **Investigation Name** is `Area 51 Investigation`.
![Object Dropdown Security Concern](/docs/resources/foundry/action-types/objectDropdownSecurityFilter.png)
在这里，我们可能会向无法查看这些文档的用户泄露 `Area 51 Investigation` 是某些 `Document` 对象的属性值这一信息。

Here, we would potentially be revealing that `Area 51 Investigation` is a property value of some `Document` objects to users who cannot view those documents.
这仅适用于 **static value filters**。当通过 parameter 或另一个对象的属性过滤 `Investigation Name` 属性时，不会引用 `Area 51 Investigation`，原因如下：

This only applies to **static value filters**. There is no reference to the `Area 51 Investigation` when filtering the `Investigation Name` property by a parameter or by the property of another object because:
* `Investigation Name` parameter 是用户提供的。关于底层数据的信息不会暴露给 Action Type 查看者。

* `Investigation Object` parameter 将遵守该用户现有的对象可见性限制。

* The `Investigation Name` parameter is user-provided. No information about the underlying data is exposed to the action type viewer.
* The `Investigation Object` parameter will respect existing restrictions on object visibility for this user.
因此，这些搜索查询都不存在数据隐私问题。

Therefore, neither of these search queries represents a data privacy concern.
![Object Dropdown Property Filters](/docs/resources/foundry/action-types/objectDropdownSecurityProperty.png)
## Technical details
在大多数情况下,actions 后端会在 action type 定义中编辑敏感信息,以避免暴露敏感的 property 值。例如,action 提交条件对无法编辑 action type 的用户隐藏。同样,用户也无法在 interface 中的 action type 定义里看到新的 object 下拉筛选器,也无法在后端检查响应时看到它们。

In most cases, the actions backend redacts sensitive information in the action type definition to avoid exposing sensitive property values. For example, action submission criteria are hidden from users who cannot edit action types. Similarly, a user will not be able to see the new object dropdown filters in the action type definition in the interface or while inspecting the response in the backend.
然而,在查看 action 表单时,object 下拉验证会被转换为一个 object set。这意味着用户可以查看包含此 object set 的网络请求。在上述示例中,用户将收到一个 object set RID,其中包含 `Investigation Name = 'Area 51 Investigation'` 筛选器,从而泄露该 property 值的存在,即使他们无法查看任何对应的 object。

However, when viewing the action form, the object dropdown validation is converted into an object set. This means that users could review the network request containing this object set. In the example above, the user would receive an object set RID containing the `Investigation Name = 'Area 51 Investigation'` filter, revealing the existence of that property value even if they could not view any of its corresponding objects.
这意味着这些值对任何用户都**在 interface 中不可见**。如果可见性比安全性更值得关注,则可以忽略此警告。

This means that these values will **not be visible in the interface** for any users. If visibility is a greater concern than security, this warning can be ignored.