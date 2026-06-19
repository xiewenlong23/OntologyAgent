<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/object-security-policies/
---
# Object and property security policies
Object security policy 允许您通过在 object type 上配置 security policy 来配置对象实例的查看权限，这些策略独立于底层 datasource 的权限。它们用于实现 *行级安全控制（row-level security）*。

Object security policies allow you to configure view permissions on an object instance by configuring security policies on the object type, independently of the permissions on the backing data source. These are used to achieve *row-level security*.
可以使用额外的 *property security policy* 来保护特定 property 的可见性。这些策略与 object security policy 相同，只是它们仅应用于所选 property 的子集。它们用于实现 *列级安全控制（column-level security）*。

The visibility of specific properties can be guarded using additional *property security policies*. These are identical to object security policies, except they only apply to a selection of properties. These are used to achieve *column-level security*.
默认情况下，object security policy 应用于所有 property。当 property security policy 包含某个 property 时，用户必须同时通过 object security policy 和 property security policy 才能查看该 property 的值。object security policy 和 property security policy 的组合用于实现 *单元格级安全控制（cell-level security）*。如果用户未通过 object security policy，则该对象实例对该用户不可见。如果用户通过了 object security policy 但未通过 property security policy，他们将在该 property 值的位置看到一个 *null* 值。

By default, object security policies are applied to all properties. When a property security policy includes a property, the user must pass both the object security policy and the property security policy to view the property value. The combination of object and property security policies is used to achieve *cell-level security*. If a user does not pass the object security policy, the object instance will not be viewable to that user. If they pass the object security policy but do not pass the property security policy, they will see a *null* value in place of the property value.
## Configure object and property security policies
对对象实例及其 property 的访问由以下条件决定：

Access to an object instance and its properties is determined by the following conditions:
* 对 object type 拥有 `Viewer` 访问权限。

* 通过已配置的细粒度 policy（如果已配置）。

* 通过任何 [marking](/docs/foundry/security/markings/)、[organization](/docs/foundry/security/orgs-and-spaces/#organizations) 或 [classification](/docs/foundry/security/classification-based-access-controls/) 检查。

* `Viewer` access to the object type.
* Passing a granular policy, if configured.
* Passing any [marking](/docs/foundry/security/markings/), [organization](/docs/foundry/security/orgs-and-spaces/#organizations), or [classification](/docs/foundry/security/classification-based-access-controls/) checks.
当配置了 Object 或 Property 安全策略时，用户无需拥有对 Object Type 底层数据源的 `Viewer` 权限即可查看 object 实例。

When an object or property security policy is configured, users do not need `Viewer` permissions to the object type's backing data sources to view object instances.
考虑这样一个示例：`Passenger` Object Type 包含 `User ID`、`Flight Number`、`Seat Assignment`、`Name`、`Address` 和 `Phone Number` 等 Property。其中部分乘客是 VIP，其信息仅可被拥有 `VIP` 标记访问权限的用户查看。此外，某些 Property（例如 `Name`、`Address` 和 `Phone Number`）应仅对拥有 `PII` 标记且被授权查看个人身份信息的用户可见。由于底层数据集包含敏感数据，应为其标记 `PII` 和 `VIP`。然而，不具有敏感标记的用户仍应能够访问乘客的航班详情。

Consider an example where a `Passenger` object type has the properties `User ID`, `Flight Number`, `Seat Assignment`, `Name`, `Address`, and `Phone Number`. Some passengers are VIPs, whose information can only be seen by users who have access to a `VIP` marking. Additionally, some properties, such as `Name`, `Address`, and `Phone Number`, should be visible only to users who have the `PII` marking, and are authorized to view personally identifiable information. Since the backing dataset consists of sensitive data, it should be marked with `PII` and `VIP`. However, users without sensitive markings should still be able to access a passenger’s flight details.
可采取以下步骤来使用 object 安全策略保护 `Passenger` Object Type。

The following steps can be taken to secure the `Passenger` object type using object security policies.
1. 导航至 Object Type 的 **Security** 选项卡。

> 📷 **[图片: Ontology Manager 中 Object Type 的 'Security' 选项卡。]**

2. 在 **Security policies** 区域下选择 **Create**，以使用 object 安全策略覆盖数据源策略。

![“Security policies”区域下的 “Create” 选项。](/docs/resources/foundry/object-permissioning/osp-override-datasource-policy.png)

3. 创建用于编辑 object 实例查看权限的 object 安全策略。您可以选择添加细粒度策略并编辑组织和标记。

![Object 安全策略概览。](/docs/resources/foundry/object-permissioning/osp-permissions-ui-overview.png)

4. 在 **Markings** 配置中，停止继承 `PII` 和 `VIP` 标记，以便不具有这些标记的用户能够查看 object 实例。

![访问要求下列出的标记，以及启动和停止继承标记的选项。](/docs/resources/foundry/object-permissioning/osp-stop-inheriting-markings.png)

5. 添加 **Granular policy** 以限制对 VIP 的访问。`VIP` 标记被添加为 [mandatory control property](/docs/foundry/object-link-types/mandatory-control-properties/)。每一行在 mandatory control property 中都有一组标记，用户必须满足这些标记才能访问该 object 实例。

![“Compose granular policy” 视图，其中包含在 VIP mandatory control property 上添加条件的选项。](/docs/resources/foundry/object-permissioning/osp-add-granular-policy.png)

6. 这将创建 object 安全策略。现在，我们需要使用 `PII` 标记保护 `PII` Property。我们可以通过添加 property 安全策略来实现这一点。

![“Security policies”区域中添加 property 安全策略的选项。](/docs/resources/foundry/object-permissioning/osp-add-property-security-policy.png)

7. 选择需要保护的 property 并为该策略命名。然后，在 **Manage markings** 设置中添加 `PII` 标记。property 安全策略的配置设置与 object 安全策略完全相同。

![Property 安全策略概览，其中包含策略名称和 property。](/docs/resources/foundry/object-permissioning/osp-select-properties-for-policy.png)

为 property 安全策略选择 **Manage markings** 并添加 `PII` 标记。

![“Access requirements”区域列出继承的标记。](/docs/resources/foundry/object-permissioning/osp-add-marking-property-security-policy.png)

8. 这将创建 property 安全策略。策略中包含的 property 现在由 object 安全策略和新的 property 安全策略共同保护。未包含在任何 property 安全策略中的 property 仍由 object 安全策略保护。

![Object 安全策略覆盖的 property。](/docs/resources/foundry/object-permissioning/osp-object-security-policy-properties.png)

![Property 安全策略覆盖的 property。](/docs/resources/foundry/object-permissioning/osp-property-security-policy-properties.png)
1. Navigate to the **Security** tab of the object type.

> 📷 **[图片: The 'Security' tab for an object type in Ontology Manager.]**

2. Select **Create** under the **Security policies** section to override data source policies with object security policies.

![The "Create" option under the "Security policies" section.](/docs/resources/foundry/object-permissioning/osp-override-datasource-policy.png)

3. Create the object security policy that edits view permissions for object instances. You have the option to add a granular policy and edit the organization and markings.

![The object security policy overview.](/docs/resources/foundry/object-permissioning/osp-permissions-ui-overview.png)

4. In the **Markings** configuration, stop inheriting the `PII` and `VIP` markings so that users without those markings can see object instances.

![Markings listed under access requirements with the option to start and stop inheriting markings.](/docs/resources/foundry/object-permissioning/osp-stop-inheriting-markings.png)

5. Add a **Granular policy** to limit access to VIPs. The `VIP` marking is added as a [mandatory control property](/docs/foundry/object-link-types/mandatory-control-properties/). Every row has a set of markings in the mandatory control property that need to be satisfied by a user to access that object instance.

![The "Compose granular policy" view, with the option to add a condition on the VIP mandatory control property.](/docs/resources/foundry/object-permissioning/osp-add-granular-policy.png)

6. This creates the object security policy. Now, we need to secure the `PII` properties with the `PII` marking. We can do this by adding a property security policy.

![The option to add a property security policy in the "Security policies" section.](/docs/resources/foundry/object-permissioning/osp-add-property-security-policy.png)

7. Select the properties that need to be secured and give the policy a name. Then, add the `PII` marking in the **Manage markings** setting. The configuration settings for property security policies are identical to object security policies.

![The property security policy overview with the policy name and properties.](/docs/resources/foundry/object-permissioning/osp-select-properties-for-policy.png)

Select **Manage markings** for the property security policy and add the `PII` marking.

![The "Access requirements" section listing inherited markings.](/docs/resources/foundry/object-permissioning/osp-add-marking-property-security-policy.png)

8. This will create the property security policy. The properties included in the policy are now secured by the object security policy and the new property security policy. Properties not included in any property security policy will still be secured by the object security policy.

![The properties covered by the object security policy.](/docs/resources/foundry/object-permissioning/osp-object-security-policy-properties.png)

![The properties covered by the property security policy.](/docs/resources/foundry/object-permissioning/osp-property-security-policy-properties.png)
### Permissions to edit security policies
要创建或编辑 object 或 property 安全策略，您必须是该 Object Type 的 **Owner**。如果您的 enrollment 使用 [project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/)，则这意味着您必须在包含该 Object Type 的项目上拥有 `Owner` 角色。

To create or edit an object or property security policy, you must be an **Owner** of the object type. If your enrollment uses [project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/), this means you must hold the `Owner` role on the project that contains the object type.
### Property security policy restrictions
配置一个或多个 property 安全策略时，以下限制适用：

The following restrictions apply when configuring one or more property security policies:
* 必须已配置 object 安全策略。

* 主键 property 不能是任何 property 安全策略的成员。

* 非主键 property 最多可成为一个 property 安全策略的成员。

* An object security policy must already be configured.
* The primary key property cannot be a member of any property security policy.
* A non-primary key property can be a member of at most one property security policy.
## Configure access to object types
对 Object Type 的访问可在 [ontology metadata permissions](/docs/foundry/object-permissioning/ontology-permissions/) 中进行配置。用户需要能够 [查看 Object Type 定义和实例](/docs/foundry/object-permissioning/ontology-permissions/#viewing-object-types-and-objects)。

Access to object types can be configured in the [ontology metadata permissions](/docs/foundry/object-permissioning/ontology-permissions/). The user needs to be able to [view the object type definition and instances](/docs/foundry/object-permissioning/ontology-permissions/#viewing-object-types-and-objects).
## Configure a granular policy
[了解更多关于为行级安全配置细粒度策略的信息](/docs/foundry/platform-security-management/manage-granular-policies/)。

[Learn more about configuring granular policies for row-level security](/docs/foundry/platform-security-management/manage-granular-policies/).
## Configure mandatory controls
默认情况下，object 安全策略将从其数据源继承所有 mandatory controls。这些包括 [markings](/docs/foundry/security/markings/)、[organizations](/docs/foundry/security/orgs-and-spaces/#organizations) 和 [classifications](/docs/foundry/security/classification-based-access-controls/)。

By default, an object security policy will inherit all mandatory controls from its data sources. These include [markings](/docs/foundry/security/markings/), [organizations](/docs/foundry/security/orgs-and-spaces/#organizations), and [classifications](/docs/foundry/security/classification-based-access-controls/).
然后可以进一步自定义 object 安全策略，以添加新的 mandatory controls 并移除不再必要的已继承 mandatory controls。

The object security policy can then be further customized to add new mandatory controls and remove inherited mandatory controls that are no longer necessary.
## Materializations with object security policies
Object 安全策略还决定查看 Object Type 中 [materialized](/docs/foundry/object-edits/materializations/) 数据的权限。

Object security policies also determine the permissions for viewing [materialized](/docs/foundry/object-edits/materializations/) data in the object type.
目前，具有 object 安全策略的 Object Type 只能 materialize 到 Foundry 数据集。最严格的权限将应用于 materialized 数据。这包括以下内容：

Currently, object types with object security policies can only be materialized to Foundry datasets. The most restrictive permissions are applied to materialized data. This includes the following:
* 来自底层数据源的所有标记。

* 在 object 或 property 安全策略上应用的附加标记。

* 所有 object 和 property 安全策略的细粒度策略中使用的 mandatory controls properties 的所有标记。

* All markings from the backing data sources.
* Additional markings applied on object or property security policies.
* Markings from all mandatory controls properties used in the granular policies of all object and property security policies.
> **⚠️ 警告**

> Materialized 数据集上的事务由 materialized 数据集构建时生成的安全策略进行保护。当用户在其 object 或 property 安全策略中添加或移除标记时，该标记将仅反映在该标记存在时所提交的事务中。事务在 materialization [按计划构建](/docs/foundry/object-edits/materializations/#build-schedules-in-writeback-and-materialized-datasets) 时提交，该计划由用户配置。
> 在向 object 或 property 安全策略添加标记后，请确保执行以下操作：
> **⚠️ 警告**

> Transactions on materialized datasets are secured by the security policies generated at the time of the materialized dataset build. When users add or remove a marking in their object or property security policies, the marking will only be reflected in the transactions committed at the time that the marking is present. Transactions are committed when the materialization is [scheduled to build](/docs/foundry/object-edits/materializations/#build-schedules-in-writeback-and-materialized-datasets), which is configured by the user.
> After adding a marking to an object or property security policy, make sure to do the following:
> * 如果 markings 需要立即传播到 materialization dataset，则构建 materialization dataset。
> * 在 materialization 或 backing dataset 上标记 marking，以保护 materialization dataset 上的所有历史事务。
> * Build the materialization dataset if the markings need to propagate to the materialization dataset immediately.
> * Mark the materialization or backing dataset with the marking to secure all historical transactions on the materialization dataset.
## Migrate from restricted views to object security policies
对于大多数基于 Ontology 构建的使用场景，推荐使用 object security policies 而非 [restricted views](/docs/foundry/security/restricted-views/)。它们提供统一的 cell 级安全策略、近乎即时的策略更新，并支持 streaming 和 branching。[了解 object and property security policies 的更多优势。](/docs/foundry/object-permissioning/managing-object-security/#benefits-of-object-and-property-security-policies)

Object security policies are recommended over [restricted views](/docs/foundry/security/restricted-views/) for most use cases built on the Ontology. They provide unified cell-level security, near-instantaneous policy updates, and support for streaming and branching. [Learn more about the benefits of object and property security policies.](/docs/foundry/object-permissioning/managing-object-security/#benefits-of-object-and-property-security-policies)
如果您之前设置了由 restricted views 支持的 object types，并希望迁移到 object security policies，可以使用下文介绍的迁移工具。[了解 object and property policies 与 data source policies 的对比。](/docs/foundry/object-permissioning/managing-object-security/#object-and-property-policies-vs-data-source-policies)

If you previously set up object types backed by restricted views and want to migrate to object security policies, you can use the migration tool described below. [Learn more about object and property policies versus data source policies.](/docs/foundry/object-permissioning/managing-object-security/#object-and-property-policies-vs-data-source-policies)
您可以使用 **Security** 选项卡中的迁移工具，将 object type 的数据源从 restricted view 迁移到该 restricted view 的 backing dataset，并通过 object security policies 进行保护。该工具会配置 security policies 以匹配 restricted view 上定义的策略。

You can migrate an object type's data source from a restricted view to the backing dataset of the restricted view, secured by object security policies, using the migration tool in the **Security** tab. The tool configures security policies to match the policies defined on the restricted view.
![The entry point for migrating from restricted views to object security policies in the Security tab.](/docs/resources/foundry/object-permissioning/rv-to-psg-migration-entry-point.png)
### Limitations
> **⚠️ 警告**

> 迁移工具并不支持所有 restricted view 配置。以下配置不受支持：
> **⚠️ 警告**

> The migration tool does not support all restricted view configurations. The following configurations are not supported:
> * 带有多个数据源 (MDOs) 的 object types。
> * 带有多个 materializations 或单个 restricted view materialization 的 object types。
> * 带有 [granular policies](/docs/foundry/platform-security-management/manage-granular-policies/) 的 restricted views，这些策略使用不受支持的比较运算符，包括 greater than、greater than or equal、less than 和 less than or equal。
> * 引用数值常量值（例如 integer、long 或 double）的带有 granular policies 的 restricted views。
> * 引用 authorized group IDs、organization marking IDs 或 static marking IDs 作为 user properties 的带有 granular policies 的 restricted views。建议使用 [mandatory control property](/docs/foundry/object-link-types/mandatory-control-properties/) 来实现等效的安全性。
> * Object types with multiple data sources (MDOs).
> * Object types with multiple materializations or a single restricted view materialization.
> * Restricted views with [granular policies](/docs/foundry/platform-security-management/manage-granular-policies/) that use unsupported comparison operators, including greater than, greater than or equal, less than, and less than or equal.
> * Restricted views with granular policies that reference numeric constant values, such as integer, long, or double.
> * Restricted views with granular policies that reference authorized group IDs, organization marking IDs, or static marking IDs as user properties. Consider using a [mandatory control property](/docs/foundry/object-link-types/mandatory-control-properties/) to achieve equivalent security.
### Preserve discretionary security
为了保留项目对数据的查看约束（从 restricted view 所在项目继承的安全配置），您可以使用迁移工具将 object type 移动到与 restricted view 相同的项目中。

To preserve project viewing constraints on the data (security configurations inherited from the project the restricted view is in), you can move the object type into the same project as the restricted view using the migration tool.
![The restricted view to object security policy migration tool.](/docs/resources/foundry/object-permissioning/rv-to-psg-migration-tool.png)