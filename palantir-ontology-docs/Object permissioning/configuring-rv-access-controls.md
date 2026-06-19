<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/configuring-rv-access-controls/
---
# Configure restricted-view-backed object types
[Restricted views (RVs)](/docs/foundry/platform-security-management/manage-restricted-views/#use-restricted-views-to-back-object-types) 为 ontology 数据启用行级访问控制。与仅授予整个数据集或某一类型的所有对象的访问权限相比，这允许更细粒度的访问控制。

[Restricted views (RVs)](/docs/foundry/platform-security-management/manage-restricted-views/#use-restricted-views-to-back-object-types) enable row-level access controls for ontology data. This allows for finer-grained access control than simply granting access to an entire dataset or all objects of a certain type.
Restricted view 类似于 dataset，但会限制对 dataset 中*特定行*的访问。Restricted view 在 dataset 级别进行配置，ontology 对象将继承 restricted view policy 中定义的细粒度权限。

Restricted views are similar to datasets but restrict access to *specific rows* in datasets. Restricted views are configured at the dataset level, and ontology objects inherit the granular permissions defined in the restricted view policy.
## Use restricted views to back object types
使用 restricted view 作为 object type 的 backing 将控制用户可以查看的特定对象。例如，如果用户满足某项 policy 的要求并能够查看 restricted view 中的特定行，那么他们将能够查看相应的 ontology 对象。

Backing an object type with a restricted view will control the specific objects a user can see. For example, if a user meets the requirements for a policy and can see a specific row in the restricted view, then they will be able to see the corresponding ontology object.
要查看由 dataset 支持的 object type 的对象，您还必须能够查看该 dataset。

To view objects of an object type backed by a dataset, you must also be able to view the dataset.
* 要查看由 Object Storage V1 (Phonograph) 中 restricted view 支持的 object type 的对象，您必须能够查看 object type 本身；您不一定需要查看该 restricted view。相反，您只需要满足该 restricted view 的 [markings](/docs/foundry/security/restricted-views/#create-marking-backed-restricted-views) 及其针对该行的 read policy 即可。

* 在 Object Storage V2 中，您必须能够查看 restricted view，才能查看由该 restricted view 支持的 object type 的对象。

* To view objects of an object type backed by a restricted view in Object Storage V1 (Phonograph), you must be able to view the object type itself; you do not necessarily need to see the restricted view. Rather, you only need to satisfy the restricted view's [markings](/docs/foundry/security/restricted-views/#create-marking-backed-restricted-views) and its read policy for that row.
* In Object Storage V2, you must be able to see a restricted view to see objects of the object type backed by that restricted view.
在限制用户访问特定对象时，请在 Ontology Manager 中仅选择 restricted view 作为 object type 的 backing datasource。

When restricting specific objects from a user, only select restricted views in the Ontology Manager as an object type’s backing datasource.
![Input datasource](/docs/resources/foundry/object-permissioning/object-security-backing-datasource.png)
## Ontology edits
> **⚠️ 警告**

> 由于可能编辑对象安全中所引用的 property，因此对 ontology 对象的访问可能会受到用户编辑的影响。在这种情况下，用户可能能够看到 backing restricted view 中的某一行，但无法在 ontology 中看到相应的对象，反之亦然。
> **⚠️ 警告**

> Access to an ontology object can be affected by user edits, since it is possible to edit a property that is referenced in the object's security. In such cases, a user might be able to see a row in the backing restricted view but not see the corresponding object in the ontology, or vice versa.
例如，考虑一个具有以下数据的 `Ticket` object type，其中 restricted view 上的 policy 要求您必须是 `Assignee` 列中所在组的成员才能查看该行。

For example, consider a `Ticket` object type with the following data, where the policy on the restricted view requires you to be a member of the group in the `Assignee` column to see the row.
| Ticket ID  | Title      | Assignee         |
|------------|------------|------------------|
| 101        | Ticket One | palantir-support |
如果应用一个 action 将此对象上的 `Assignee` 更改为 `customer-support`，那么不是 `customer-support` 成员的 `palantir-support` 成员将失去对 ontology 中该对象的访问权限。但是，他们仍将在 restricted view 中保留对该行的可见性，因为该行不受 action 影响。不是 `palantir-support` 成员的 `customer-support` 成员将获得对 ontology 对象的访问权限，但仍无法查看 restricted view 中的该行。

If an action were applied to change the `Assignee` on this object to `customer-support`, then members of `palantir-support` who are not also members of `customer-support` will lose access to the object within the ontology. However, they will retain visibility of the row in the restricted view, which is unaffected by the action. Members of `customer-support` who are not also members of `palantir-support` would gain access to the ontology object, but still not be able to see the row in the restricted view.
## Security configuration
Ontology Manager 中的 **Datasources** 选项卡将显示用于编辑 **Granular Policies** 的其他配置选项。**Granular Policies** 部分允许您配置用于编辑此类型对象的权限。

The **Datasources** tab in the Ontology Manager will show additional configuration options to edit **Granular Policies**. The **Granular Policies** section allows you to configure permissions for editing objects of this type.
> **⚠️ 警告**

> 编辑的 Granular Policies 只能在使用 Object Storage V1 且未选中 **Only allow edits via actions** 选项的 object type 上进行配置。对于所有其他 object type，编辑权限通过编辑 object type 的 action type 来控制。[了解有关 action 权限的更多信息。](/docs/foundry/action-types/permissions/)
> **⚠️ 警告**

> Granular Policies for edits can only be configured for object types using Object Storage V1 which do not have the **Only allow edits via actions** option selected. For all other object types, edit permissions are controlled via action types editing the object types. [Learn more about action permissions.](/docs/foundry/action-types/permissions/)
您可以配置这些策略以适应您希望用户仅根据其属性（例如对象的某个 property）查看或编辑特定对象的情况。例如，您可能只希望来自 `Europe`（在 `region` 列中）的用户查看和编辑欧洲对象，这可能与 Restricted View 的策略不同。

You can configure these policies to accommodate cases where you want users to view or edit only specific objects based on their attributes (like a property of the object). For example, you may only want users from `Europe` (found in the `region` column) to see and edit European objects, which may differ from the restricted view’s policy.
有三种策略可以定义谁可以访问对象上的 properties：

There are three policies that can define who can access the properties on an object:
* **Read（读取）：** 此策略定义谁可以查看 Restricted View 上的所有 properties。使用上面的示例，这可能是一个将 `region` 列与用户属性中的内容（`Europe`）进行比较的策略，以确定用户可以查看哪些对象。

* **Edit property（编辑 property）：** 此策略定义谁被允许更新任何配置用于 writeback 且未在任何 granular permissions 策略定义中使用的 properties。使用上面的示例，此策略将控制谁可以编辑 `name` property，但不能控制谁可以编辑 `region` property，因为 `region` property 已用于该策略中。

* **Edit policy property（编辑策略 property）：** 此策略定义谁被允许更新任何配置用于 writeback 且也用于任何 granular permissions 策略定义中的 properties。使用上面的示例，此策略将控制谁可以编辑 `region` property。

* **Read:** This policy defines who can view all properties on the Restricted View. Using the example above, this might be a policy that compares the `region` column with what is in the user’s attributes (`Europe`) to determine what objects the user can see.
* **Edit property:** This policy defines who is allowed to update any of the properties configured for writeback that are not used in any granular permissions policy definitions. Using the example above, this policy would control who can edit the `name` property, but not who can edit the `region` property, since the `region` property is used in the policy.
* **Edit policy property:** This policy defines who is allowed to update any of the properties configured for writeback that are also used in any granular permissions policy definitions. Using the example above, this policy would control who can edit the `region` property.
![Granular permissions](/docs/resources/foundry/object-permissioning/object-security-granular-permissions.png)
> **⚠️ 警告**

> 如果在 Object Storage V1 (Phonograph) 中注册 object type 之后更改了 view 策略，则必须通过 **Ontology Manager** 中 object type 的 **Datasources** 选项卡下 Phonograph 部分中的 **Update** 按钮来更新注册。如果未更新注册，则 restricted view 的最新数据可能会根据先前注册的策略变得可用。Object Storage V2 默认支持自动策略传播。
> **⚠️ 警告**

> If view policies are changed after the object type was registered with Object Storage V1 (Phonograph), the registration must be updated through the **Update** button in the Phonograph section of the object type's **Datasources** tab in **Ontology Manager**. If the registration is not updated, the latest data of the restricted view may be made available based on previously registered policies. Automatic policy propagation is available by default in Object Storage V2.