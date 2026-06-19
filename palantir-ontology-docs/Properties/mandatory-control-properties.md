<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/mandatory-control-properties/
---
# Mandatory control properties
Mandatory control properties 是 object type properties，允许对存储在 objects 中的数据进行细粒度的访问控制。您可以使用 mandatory control properties 限制对给定 object 同一 datasource 中所有其他 properties 的访问，使这些 properties 仅对满足 mandatory controls 的用户可见。

Mandatory control properties are object type properties that allow for granular access control to the data stored in objects. You can use mandatory control properties to restrict access to all other properties in the same datasource for a given object, making those properties viewable only by users who satisfy the mandatory controls.
**Note：** Mandatory control properties **仅在 Object Storage V2 上可用**。

**Note:** Mandatory control properties are **only available on Object Storage V2**.
## How to use mandatory control properties
1. 首先，创建您的 marking-backed restricted view (RV)。详细了解 [creating marking-backed restricted views](/docs/foundry/security/restricted-views/#create-marking-backed-restricted-views)。

2. 导航至 Ontology Manager。

3. 选择要为其限制 property 访问的 object type，然后创建或选择要设置为 mandatory control property 的 property。

4. 在 property 侧边栏上，确保该 property 已映射到您的 restricted view 上对应的 **marking column**。

5. 将 property type 的 base type 设置为 **Mandatory Control**。

1. 默认情况下，mandatory control property 支持 **markings** 和/或 **organizations** 来限制访问。

2. 如果您已启用 CBAC，您将可以选择基于 **classification** 的 mandatory controls。

6. 在 datasource 上选择 **Allowed markings** 和/或 **Allowed organizations**。对于 classifications，请选择 **Max classification**。

7. 如果 object type 具有多个 datasources，请为每个其他 datasource 选择一个 mandatory control property，以同样保护其 properties。

8. 保存您对 ontology 所做的更改，并等待重新索引完成。

1. First, create your marking-backed restricted view (RV). Learn more about [creating marking-backed restricted views](/docs/foundry/security/restricted-views/#create-marking-backed-restricted-views).
2. Navigate to the Ontology Manager.
3. Choose the object type for which you want to restrict property access, then create or select the property you want to set as a mandatory control property.
4. On the property sidebar, ensure the property is mapped to the corresponding **marking column** on your restricted view.
5. Set the base type of the property type to **Mandatory Control**.
1. By default a mandatory control property supports **markings** and/or **organizations** to restrict access.
2. If you have CBAC enabled, you will have the option to choose **classification** based mandatory controls.
6. Select the **Allowed markings** and/or **Allowed organizations** on the datasource. For classifications, select the **Max classification**.
7. If the object type has multiple datasources, select a mandatory control property for each of the other datasources to secure their properties as well.
8. Save your changes to the ontology and wait for the reindex to be completed.
## Types of mandatory control properties
可以在 property 上设置三种类型的 mandatory controls：

There are three types of mandatory controls that can be set on a property:
* [Markings](#markings)
* [Organizations](#organizations)
* [Classifications](#classifications)
* [Markings](#markings)
* [Organizations](#organizations)
* [Classifications](#classifications)
### Markings
标记（Marking）是强制性控制措施，通过要求用户拥有特定标记来限制对数据的访问。如果资源有多个标记，用户必须拥有所有这些标记才能访问该资源。了解更多关于[标记](/docs/foundry/security/markings/)的信息。

Markings are mandatory controls that restrict access by requiring a user to have a particular Marking in order to access data. If a resource has multiple markings, the user must have all of them to access the resource. Learn more about [markings](/docs/foundry/security/markings/).
要使用标记，您需要提供一组允许的标记。只有此集合中的标记才会被允许用于该数据源上的任何强制性控制属性。

To use markings, you are required to provide a set of allowed markings. Only markings in this set will be permitted on any mandatory control property on the datasource.
### Organizations
组织（Organization）是访问要求，用于在用户组和资源组之间强制实施严格的隔离。每个用户只能是一个组织的*成员*，但可以是多个组织的*来宾成员*。要访问带有组织标记的数据，用户必须是该组织的成员。如果资源有多个组织，用户必须是应用于该资源的至少一个组织的成员。了解更多关于[组织](/docs/foundry/security/orgs-and-spaces/#organizations)的信息。

Organizations are access requirements that enforce strict silos between groups of users and resources. Every user is a *member* of only one organization but can be a *guest member* of multiple organizations. To access data marked with an organization, a user must be a member of that organization. If a resource has multiple organizations, the user must be a member of at least one of the organizations applied to the resource. Learn more about [organizations](/docs/foundry/security/orgs-and-spaces/#organizations).
要使用组织，您需要提供一组允许的组织。只有此集合中的组织才会被允许用于该数据源上的任何强制性控制属性。

To use organizations, you are required to provide a set of allowed organizations. Only organizations in this set will be permitted on any mandatory control property on the datasource.
标记和组织可以在同一个强制性控制属性上一起使用。在这种情况下，用户必须满足所有标记以及至少一个组织的要求，才能访问该资源。

Markings and organizations can be used together on the same mandatory control property. In this case, a user must satisfy all the markings and at least one of the organizations to access the resource.
### Classifications
分类标记（Classification marking）是用于保护敏感政府信息的强制性控制措施。它们用于限制对敏感信息的访问，其中信息的敏感性以分层方式定义。每个用户只能访问其自身分类级别或低于其分类级别的数据。

Classification markings are mandatory controls used to protect sensitive government information. They are used to restrict access to sensitive information where sensitivity of information is defined in a hierarchical way. Every user can only access data that is classified at or below their own classification level.
只有在您的注册（enrollment）上启用了 CBAC 的情况下，才能配置 CBAC 标记。了解更多关于[CBAC（基于分类的访问控制）](/docs/foundry/security/classification-based-access-controls/)的信息。

You can only configure CBAC markings if you have CBAC enabled on your enrollment. Learn more about [CBAC (classification based access controls)](/docs/foundry/security/classification-based-access-controls/).
要使用分类，您需要提供一个最大分类（max classification）。只有满足此最大分类的标记才会被允许用于该数据源上任何基于分类的强制性控制属性。

To use classifications, you need to provide a max classification. Only markings that satisfy this max classification will be permitted on any classificatoin based mandatory control property on the datasource.
分类不能与标记或组织在同一个强制性控制属性上一起使用。

Classifications can not be used together with markings or organizations on the same mandatory control property.
## Datasource-level permissioning
强制性控制属性会保护同一数据源中的所有其他属性。对于使用单一数据源的 Object Type，这意味着用户只有在满足强制性控制属性中的值时才能查看对象。

A mandatory control property secures all other properties in the same datasource. For object types with a single datasource, this means that a user will only be able to view an object if they satisfy the value in the mandatory control property.
然而，对于多数据源支持的 Object Type（MDO），每个数据源可以拥有自己的强制性控制属性。只有由特定数据源支持的属性才会受到该数据源中强制性控制的保护。

However, for multi-datasource-backed object types (MDOs), each datasource could have its own mandatory control property. Only the properties backed by a specific datasource will be secured by the mandatory control in that datasource.
这意味着用户可能只被允许查看对象上的一部分属性，在这种情况下，用户将只能查看从这些数据源映射的属性。在向用户显示 Object 实例时，其他属性将显示为 null。

This means that it is possible for a user to only have permission to see a subset of properties on an object, In this case, the user will only be able to see the properties mapped from those datasources. Other properties will appear as null when displaying an object instance to the user.
为了有效地使用强制性控制属性，底层数据源的结构应使只有应共享同一强制性控制的属性位于同一数据源中。

To use mandatory control properties effectively, the backing datasources should be structured in such a way that only properties that should share a mandatory control are in the same datasource.
## Validations
对强制性控制属性强制执行以下验证：

The following validations are enforced on mandatory control properties:
* 强制性控制属性必须映射到**受限视图（restricted view）**上的**标记列（marking column）**。强制性控制通过使用受限视图支持 Object Type 来强制执行，该受限视图具有一项策略，要求用户必须满足映射列中的标记才能查看行。更多信息请参见[受限视图](/docs/foundry/security/restricted-views/)。

* **强制性控制属性必须是必需的（required）。** 这确保如果数据源上存在具有强制性控制属性的对象，则必须定义强制性控制，以帮助维护数据一致性和完整性。所有强制性控制属性不能为 null。但是，标记和组织值可以设置为空数组。在这种情况下，所有用户都将满足标记要求并能够查看行。了解更多关于[必需属性](/docs/foundry/object-link-types/required-properties/)的信息。

* 如果您想将强制性控制属性添加到已经存在编辑的仅编辑 Object Type，则不能直接创建该属性，因为强制性控制属性不能为空。要解决此问题：
1. 添加一个可空的字符串数组属性。

2. 使用 [Action](/docs/foundry/action-types/overview/) 回填其值。

3. 将属性的基本类型更改为 **Mandatory Control**。
* 包含强制性控制属性的每个数据源必须定义一个关于可添加到这些属性的值的约束。这些约束的形式包括：基于分类的强制性控制的最大分类，或者一组允许的标记和/或允许的组织。对强制性控制属性所做的任何编辑以及从底层数据集获取的值都必须遵守数据源上设置的约束。

* 此约束在对象存储级别强制执行，因此即使您可以使用 Ontology Manager 保存违反此约束的 Object Type，如果数据集中现有的值不满足约束，或者数据集中的值被更新为包含强制性控制的有效值，则该 Object Type 将无法索引。此外，任何尝试将无效值设置到强制性控制属性的编辑都将被拒绝，并且该 Action 将无法提交。

* 这些允许的标记、允许的组织或最大分类将用于标记从该 Object Type 物化（materialized）出的任何导出数据集。这确保只有可以查看 Object Type 上所有行的用户才能查看该物化数据集。

* Mandatory control properties must be mapped to a **marking column** on a **restricted view.** The mandatory controls are enforced by backing the object type with a restricted view which has a policy that requires users to satisfy the markings in the mapped column to be able to view a row. See [Restricted Views](/docs/foundry/security/restricted-views/) for more information.
* **Mandatory control properties must be required.** This ensures that if an object with a mandatory control property is present on a datasource, the mandatory control must be defined to help maintain data consistency and integrity. All mandatory control properties must not be null. However, markings and organization values can be set to an empty array. In such cases, all users will meet the marking requirements and be able to view the row. Learn more about [required properties](/docs/foundry/object-link-types/required-properties/).
* If you want to add a mandatory control property to an edit-only object type that already has edits, you cannot create the property directly because mandatory control properties cannot be empty. To work around this:
1. Add a nullable string array property.
2. Backfill its values using an [Action](/docs/foundry/action-types/overview/).
3. Change the property's base type to **Mandatory Control**.
* Every datasource that contains a mandatory control property must define a constraint on what values can be added to those properties. These constrains come in the form of a max classification for classification based mandatory controls, or a set of allowed markings and/or allowed organizations. Any edits made to the mandatory control properties, as well as the values gotten from the backing dataset, must adhere to the constraint set on the datasource.
* This constraint is enforced on the object storage level, so even though you may be able to use Ontology Manager to save an object type that violates this constraint, the object type will fail to index if existing values in the dataset do not satisfy the constraints, or if the values in the dataset are updated to include invalid values for the mandatory controls. Also, any edits made that try to set an invalid value to the mandatory control property will be rejected and the Action will fail to submit.
* These allowed markings, allowed organizations or max classification will be used to mark any exported dataset that is materialized from this Object type. This ensures that only users who can view all rows on the Object type will be able to view the materialized dataset.
请注意,mandatory control properties 默认设置为 `Hidden`。这是因为 mandatory control properties 旨在用作其他字段的标记,因此通常不需要在 object views 或 tables 中显示 mandatory control properties。但是,如果需要,仍然可以启用 mandatory control property 的可见性。

Note that mandatory control properties are set to `Hidden` by default. This is because mandatory control properties are meant to be used as markings for other fields, so there is usually no need for mandatory control properties to appear in object views or tables. However, mandatory control property visibility can still be enabled if needed.
## Mandatory controls in actions
您可以为您的 action type 添加一个 mandatory control parameter。这可以是 marking parameter,或者在启用 CBAC 时作为 classification parameter。目前不支持 organization parameters。

You can add a mandatory control parameter to your action type. This can be a marking parameter, or a classificaton parameter if CBAC is enabled. Organization parameters are currently not supported.
Mandatory control parameters 通常用于在 action 创建的 object 上设置 mandatory control property。在这种情况下,所提供的值必须遵守该 property 的 allowed values,如果提供了无效的值,action submission 将失败。

Mandatory control parameters are commonly used to set a mandatory control property on an object that the action creates. In this case, the values provided must adhere to the property's allowed values, if an invalid value is provided, action submission will fail.
您还可以在 parameter 级别为基于 classification 的 mandatory control parameters 添加 max classification。这是一个 action type validation,因此如果所提供的值不满足 max classification,将阻止 action 被提交,而不是依赖于 datasource validation(后者允许 action 被提交但无法完成)。

You can also add a max classification at the parameter level, for classification based mandatory control parameters. This is an action type validation, and so will prevent the action from being submitted if the provided value does not satisfy the max classification, as opposed to relying on the datasource validation which will allow the action to be submitted but will fail to complete.
由 action 创建的 objects 将由所提供的 mandatory control property 值进行保护,就像来自 backing datasource 的 objects 一样。

Objects created by actions will be secured by the provided value for the mandatory control property, just like objects derived from a backing datasource.
## Marketplace usage
具有 mandatory control properties 的 object types 和具有 mandatory control parameters 的 action types 可以通过 Marketplace 进行打包和安装。

Object types with mandatory control properties and action types with mandatory control parameters can be packaged and installed through Marketplace.
打包具有 mandatory control properties 的 object type 时,allowed markings 或 max classification 将被声明为该 product 的 installation inputs。

When packaging an object type with mandatory control properties, the allowed markings or max classification are declared as installation inputs for that product.
类似地,如果打包具有设置了 max classification 的、基于 classification 的 mandatory control parameter 的 action type,则 max classification 将被声明为 installation inputs。

Similarly, if packaging an action type with a classification based mandatory control parameter with max classification set, the max classification is declared as installation inputs.
安装 product 时,系统将提示您为每个 mandatory control property 选择 allowed markings 或 max classification。所选值将在安装时设置为 mandatory control properties 的 allowed markings 或 max classification。

When installing the product, you will be prompted to select the allowed markings or max classification for each mandatory control property. The selected values will be set as allowed markings or max classification of the mandatory control properties upon install.

> 📷 **[图片: Selecting mandatory control inputs during Marketplace install]**

> 📷 **[图片: Selecting mandatory control inputs during Marketplace install]**

请注意,打包具有相同值的多个 mandatory control properties 和/或 parameters 将导致仅声明一个 mandatory control input。

Note that packaging multiple mandatory control properties and/or parameters with the same values would results in only one mandatory control input being declared.