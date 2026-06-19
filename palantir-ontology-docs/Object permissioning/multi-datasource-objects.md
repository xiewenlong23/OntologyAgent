<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/multi-datasource-objects/
---
# Multi-datasource object types (MDOs)
> **ℹ️ 注意**

> 多数据源 Object Type（MDO）仅在 Object Storage V2 中可用。
> **ℹ️ 注意**

> Multi-datasource object types (MDOs) are only available in Object Storage V2.
多数据源 Object Type（MDO）由 Ontology 中的多个数据源支撑。目前，只有 [Foundry datasets](/docs/foundry/data-integration/datasets/) 或 [restricted views](/docs/foundry/security/restricted-views/) 可用于 MDO。暂不支持流式数据源。

A multi-datasource object type (MDO) is backed by multiple datasources in the Ontology. At this time, only [Foundry datasets](/docs/foundry/data-integration/datasets/) or [restricted views](/docs/foundry/security/restricted-views/) can be used for MDOs. Streaming souces are not supported.
## Types of multi-datasource object types (MDOs)
MDO 分为两个不同的类别：

There are two distinct categories of MDOs:
* **Column-wise MDO：** 类 join 操作的 MDO 场景，其中 Object Type 的不同属性子集可以来自不同的数据源集成。Column-wise MDO 可用于支持需要列级访问控制的使用场景。

* **Row-wise MDO：** 类 union 操作的 MDO 场景，其中完整的 Object（包含其所有属性的 Object）可以从共享相同 schema 的多个数据源集成。Row-wise MDO 可用于支持需要行级访问控制的使用场景。在 Foundry 中，[restricted views](/docs/foundry/object-permissioning/configuring-rv-access-controls/) 可为可能使用 Row-wise MDO 的使用场景提供支持。Row-wise MDO 本身并不可用。

* **Column-wise MDO:** A join-like MDO case where distinct subsets of properties for an object type can be integrated from different datasources. Column-wise MDOs can be used to support use cases where there is a need for column-level access controls.
* **Row-wise MDO:** A union-like MDO case where full objects (an object with all of its properties) can be integrated from multiple datasources sharing the same schema. Row-wise MDOs can be used to support use cases where there is a need for row-level access controls. In Foundry, [restricted views](/docs/foundry/object-permissioning/configuring-rv-access-controls/) provide support for use cases in which you might use row-wise MDOs. Row-wise MDOs themselves are not available.
> **⚠️ 警告**

> Foundry 仅支持 Column-wise MDO，不支持 Row-wise MDO。大多数 Row-wise MDO 的使用场景都可以通过 [restricted views](/docs/foundry/object-permissioning/configuring-rv-access-controls/) 实现。如果您有**无法**通过 restricted views 实现的 Row-wise MDO 使用场景，请联系您的 Palantir 代表寻求帮助。
> **⚠️ 警告**

> Foundry only supports column-wise MDOs and does not support row-wise MDOs. Most row-wise MDO use cases can be accomplished with [restricted views](/docs/foundry/object-permissioning/configuring-rv-access-controls/). If you have a use case for row-wise MDOs that **cannot** be enabled via restricted views, contact your Palantir representative for assistance.
## Configure a multi-datasource object type
在 Ontology Manager 中使用 Object Storage V2 [创建 Object Type](/docs/foundry/object-link-types/create-object-type/#create-a-new-object-type-manually) 后，从左侧边栏导航到该 Object Type 的 **Datasource** 元数据部分。然后，选择 **Add new backing datasource** 以选择数据集。

After [creating an object type](/docs/foundry/object-link-types/create-object-type/#create-a-new-object-type-manually) in Ontology Manager using Object Storage V2, navigate to the **Datasource** metadata section of the object type from the left sidebar. Then, select **Add new backing datasource** to choose a dataset.

> 📷 **[图片: New object type]**

> 📷 **[图片: New object type]**

**Map primary key** 帮助程序将出现，并提示您选择一个与 Object Type 主键值匹配的列。选择列后，多个支撑数据集将出现在 **Backing datasource** 部分下。

The **Map primary key** helper will appear and prompt you for a column with values matching the primary key of the object type. Once you choose a column, multiple backing datasets will appear under the **Backing datasource** section.

> 📷 **[图片: New object type]**

> 📷 **[图片: New object type]**

从左侧边栏导航到 **Properties** 元数据部分，以向新添加的数据集添加新字段。

Navigate to the **Properties** metadata section from the left sidebar to add new fields to the newly added dataset.
## FAQ
### Are multi-datasource object types available for an object type indexed into Object Storage V1 (Phonograph)?
不可以。MDO 仅在 Object Storage V2 中受支持，Object Storage V1（Phonograph）不可用。

No. MDOs are only supported in Object Storage V2 and are not available for Object Storage V1 (Phonograph).
### Are both column-wise MDO and row-wise MDO supported?
目前仅支持列式 MDO。如果您有无法通过 restricted view 实现的行式 MDO 用例，请联系您的 Palantir 代表寻求帮助。

Only column-wise MDOs are currently available. If you have a use case for row-wise MDOs that cannot be enabled via restricted views, contact your Palantir representative for assistance.
### Are user edits and materializations supported for MDO?
是的，MDO 支持 [user edits](/docs/foundry/object-edits/overview/) 和 [materializations](/docs/foundry/object-edits/materializations/)。

Yes, [user edits](/docs/foundry/object-edits/overview/) and [materializations](/docs/foundry/object-edits/materializations/) are supported for MDO.
### What happens if a user cannot view some of the input datasources for a given object type? What will the user experience be like?
如果用户对某些输入 datasource 缺少 `Viewer` 权限，则在向该用户展示对象时，从这些 datasource 映射的 property 将显示为 `null`。但是，用户仍然能够查看该 object type 的 schema（例如查看 property 名称），因为对 object type 的访问与对输入 datasource 的访问是分开控制的。

If a user lacks `Viewer` permission on some of the input datasources, the properties mapped from those datasources will appear as `null` when displaying an object to the user. However, the user will still be able to view the schema of that object type (such as seeing property names), since access to the object type is controlled separately from the input datasource.
[详细了解 object type 的权限配置。](/docs/foundry/object-permissioning/ontology-permissions/)

[Learn more about permissions for object types.](/docs/foundry/object-permissioning/ontology-permissions/)
### Is property multiplicity supported?
Property multiplicity 指的是在列式 MDO 的情况下，多个输入 datasource 向 object type 的同一列/property 提供数据。目前不支持 property multiplicity。这意味着 object type 的特定 property 必须来自——且仅来自——某一个输入 datasource（主键 property 除外，它必须存在于每个输入 datasource 中以用于 join 所有 datasource）。

Property multiplicity refers to multiple input datasources feeding overlapping columns/properties of an object type in the column-wise MDO case. Property multiplicity is currently not supported. This means that a specific property of an object type must come from one—and only one—of the input datasources (except for the primary key property, which must exist in every input datasource to join all datasources).
### Can a property corresponding to a restricted view policy be mapped to multiple restricted view datasources if they share the same policy?
不支持这种做法；每个 restricted view datasource 应在 object type 上配置一个独立的 policy property。其中一些 property 可以在 [Ontology Manager](/docs/foundry/ontology-manager/overview/#property-editor-view) 中标记为 hidden，以避免前端应用界面杂乱。

No, this is not supported; each restricted view datasource should have a separate policy property on the object type. Some of these properties can be marked as hidden in the [Ontology Manager](/docs/foundry/ontology-manager/overview/#property-editor-view) to avoid cluttering front-end applications.
### What is the difference between MDOs and linking two distinct object types with a foreign key relation? How should users decide between these options?
MDO 旨在提供一种用户友好的方式来配置与单个 object type 相同的设置，以构建组织的数字孪生。多个相互之间通过 link 关联的 object type 也可用于符合用户对数据的理解和交互方式的场景。请注意，跨多个 object type 的 link 查询和遍历操作比在同一 object type 上按 property 过滤的开销更大。

MDOs are intended to provide a user-friendly way to configure the same setup as a single object type to build an organization's digital twin. Multiple object types with links between them can also be used for cases in which that is how users understand and interact with their data. Note that querying and traversing links between multiple object types is a more expensive operation than filtering on a property on the same object type.
### Which objects appear if two column-wise datasources for an object have different sets of primary keys?
如果一个 object 的两个列式 datasource 具有不同的主键集合，其行为将与某些用户无法访问某些输入 datasource 的情况类似。在这些情况下，在某个 datasource 中不存在的主键对应的从该特定输入 datasource 映射而来的 property 将显示为 `null`。

If two column-wise datasources for an object have different sets of primary keys, the behavior will be similar to the case in which some users do not have access to some input datasources. In these cases, primary keys that do not exist in a datasource will have the properties that are mapped from that particular input datasource displayed as `null`.
### Is there a limit to the number of datasources an object type can have?
Object type 最多支持 70 个 datasource。只有同步至 object storage 的 datasource 会计入此限额，因此不包括 media set 或 time series sync。

Object types are limited to a maximum of 70 datasources. Only datasources that are synced to object storage count towards this limit, so it does not include media sets or time series syncs.
### Can I used MDOs with streaming object types?
不支持，MDO 不能与流式 object type 一起使用。这是 Object Storage V2 的一个已知限制。

No, MDOs are not supported with streaming object types. This is a known limitation of Object Storage V2.