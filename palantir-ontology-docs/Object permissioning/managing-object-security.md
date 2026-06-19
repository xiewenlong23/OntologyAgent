<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/managing-object-security/
---
# Manage object security
Ontology 数据可以通过 [object and property policies](#object-and-property-security-policies) 或 [data source policies](#data-source-policies) 来保护。两种方法都支持 *cell-level security*，它是行级和列级安全性的组合。

Ontology data can be secured using [object and property policies](#object-and-property-security-policies) or [data source policies](#data-source-policies). Both approaches support *cell-level security*, which is a combination of row and column level security.
举个例子，考虑一个航空管理平台中的 `Passenger` object type，其 properties 包括 `User ID`、`Flight Number`、`Seat Assignment`、`Name`、`Address` 和 `Phone Number`。

As an example, consider a `Passenger` object type in an airline management platform with the properties `User ID`, `Flight Number`, `Seat Assignment`, `Name`, `Address`, and `Phone Number`.
* **Row-level security（行级安全）：** 某些用户是 VIP，其 object instances（对应于 backing dataset 中的行）只有当用户具有 `VIP` 标记时才能被查看。

* **Column-level security（列级安全）：** `Name`、`Address` 和 `Phone number` properties 包含用户数据，只有具有 `PII` 标记的用户才能访问。

* **Row-level security:** Certain users are VIPs and their object instances, corresponding to rows in the backing dataset, can only be seen if a user has the `VIP` marking.
* **Column-level security:** The properties `Name`, `Address` and `Phone number` contain user data, and can only be accessed by users that have the `PII` marking.
> **ℹ️ 注意**

> 侧边栏中的 **Check access** 面板可用于检查某人对 Workshop 或 Slate 应用程序的访问权限，包括对依赖的 object types、其数据源以及 granular access controls 的访问权限。有关更多信息，请参阅 [check access panel documentation](/docs/foundry/security/checking-permissions/)。
> **ℹ️ 注意**

> The **Check access** panel in the sidebar can be used to check someone's access to a Workshop or Slate application, including access to dependent object types, their data sources, and granular access controls. For more information, see the [check access panel documentation](/docs/foundry/security/checking-permissions/).
> **⚠️ 警告**

> 某些 property 值引用存储在 Ontology 之外的其他资源中的数据。本节中描述的访问控制机制仅控制 property 值的可见性，但不控制这些其他资源的可见性。例如，media reference property 可以引用存储在 media set 中的 media item。如果 media set 与 object type 具有不同的权限，则用户可能无法访问 media reference property，但仍能够直接从 media set 获取 media item。因此，在 Ontology 中使用这些其他资源时，确保为其配置适当的权限非常重要。
> **⚠️ 警告**

> Some property values refer to data stored in additional resources outside of the Ontology. The access control mechanisms described in this section only control the visibility of the property values, but not the visibility of those additional resources. For example, a media reference property can refer to a media item stored in a media set. If the media set has different permissions from the object type, then it is possible for a user to not have access to a media reference property, but still be able to fetch the media item directly from the media set. Therefore, it is important to ensure that the additional resources are configured with the appropriate permissions when using them in the Ontology.
## Object and property security policies
Object and property security policies 允许您在 object instances 及其 properties 上设置 view 权限，以实现 cell-level permissions。这些策略可以直接在 object type 的 Ontology Manager 视图中进行管理，并且独立于 backing data sources 上的权限。

Object and property security policies allow you to set view permissions on object instances and their properties to achieve cell-level permissions. These can be directly managed in the object type’s Ontology Manager view and are independent of the permissions on the backing data sources.
object instance 的可见性由其 object security policy 控制，而 property 值的可见性由其 property security policy 控制。强制性的和基于分类的访问控制，以及 granular access controls，可以应用于 object and property security policies。它们共同实现了 Ontology 中的 cell-level security。

The visibility of an object instance is governed by its object security policy, whereas the visibility of a property value is governed by its property security policy. Mandatory and classification based access controls, as well as granular access controls, can be applied to object and property security policies. Together, they allow for cell-level security in the Ontology.
[详细了解如何设置 object and property security policies。](/docs/foundry/object-permissioning/object-security-policies/)

[Learn more about setting up object and property security policies.](/docs/foundry/object-permissioning/object-security-policies/)
## Data source policies
object types 的数据权限由应用于该 object type 输入数据源的权限隐式控制。

Data permissions for object types are implicitly controlled by the permissions applied to the input data sources of the object type.
### Object and property policies vs. data source policies
Object and property security policies 在大多数情况下被推荐用于管理 object security。它们提供了一种统一的方法来实现 cell-level security（行级、列级和单元格级权限），直接作用于 object type。这使得与 data source policies 相比，它们更易于配置和维护。

Object and property security policies are recommended for managing object security in most cases. They provide a unified approach to cell-level security (row, column, and cell-level permissions) directly on the object type. This makes them simpler to configure and maintain compared to data source policies.
#### Benefits of object and property security policies
Object and property security policies 解决了使用 data source policies 时出现的几个挑战：

Object and property security policies address several challenges that arise when using data source policies:
* **统一的单元级安全：** 单一特性即可提供行级（object security policies）、列级（property security policies）和单元级权限，而无需结合使用 restricted views (RVs) 和 multi-data source object types (MDOs)。

* **简化的配置：** 安全策略直接在 Ontology Manager 中的 object type 上管理，独立于底层数据源。这降低了复杂性并减轻了维护负担。

* **近乎即时的策略更新：** 对 object 和 property security policies 的更改几乎立即生效。使用 RVs 时，策略更改需要重新构建 pipeline 后，读取操作才会遵循新策略。请注意，Multipass 中的组成员资格或其他用户属性等更改仍会被短暂缓存。

* **流式支持：** Object security policies 可应用于由流（stream）支持的 object types，从而为流式数据启用行级和列级权限。

* **分支兼容性：** Object security policies 与 [Global Branching](/docs/foundry/global-branching/overview/) 集成，支持在合并前在分支上测试安全配置的开发工作流。

* **Unified cell-level security:** A single feature provides row-level (object security policies), column-level (property security policies), and cell-level permissions, rather than requiring a combination of restricted views (RVs) and multi-data source object types (MDOs).
* **Simplified configuration:** Security is managed directly on the object type in Ontology Manager, independent of the backing data sources. This reduces complexity and maintenance burden.
* **Near-instantaneous policy updates:** Changes to object and property security policies take effect almost immediately. With RVs, policy changes require a pipeline rebuild before reads respect the new policies. Note that changes in Multipass such as group membershisp or other user attributes are still cached for a short period of time.
* **Streaming support:** Object security policies can be applied to object types backed by streams, enabling row-level and column-level permissions for streaming data.
* **Branching compatibility:** Object security policies integrate with [Global Branching](/docs/foundry/global-branching/overview/), supporting development workflows where you need to test security configurations on branches before merging.
#### When to use data source policies
依赖于 RVs 和 MDOs 的 data source policies 适用于以下情况：

Data source policies, which rely on RVs and MDOs, are appropriate in the following cases:
1. **Ontology 之外的细粒度访问控制：** 如果底层 dataset 在 Ontology 之外也被使用，并且需要在这些场景中进行细粒度的访问控制，RVs 仍然是合适的解决方案。例如，RVs 可以在 [Code Workspaces](/docs/foundry/code-workspaces/overview/) 中为具有不同访问级别的用户保护对底层 dataset 的读取。Object 和 property security policies 的作用域限定在 Ontology 内部，不控制非 Ontology 场景中对原始 datasets 的访问。

2. **具有特定要求的 MDOs：** 如果您的 object types 由于不同的解析策略或每个数据源不同的构建计划等原因而需要 MDOs，则可能需要使用 data source policies。[了解有关此配置的更多信息](/docs/foundry/object-edits/how-edits-applied/#configuration)。

1. **Granular access control outside of the Ontology:** If the backing dataset is used outside of the Ontology and requires granular access control in those contexts, RVs remain the appropriate solution. For example, RVs can secure reads on the backing dataset for users with different access levels in [Code Workspaces](/docs/foundry/code-workspaces/overview/). Object and property security policies are scoped to the Ontology and do not control access to raw datasets in non-Ontology contexts.
2. **MDOs with specific requirements:** If your object types require MDOs for reasons such as different resolution strategies or different build schedules per data source, data source policies may be required. [Learn more about this configuration](/docs/foundry/object-edits/how-edits-applied/#configuration).
### Object input data sources
Datasets 和 streams 是用作 [object types](/docs/foundry/object-link-types/object-types-overview/) 输入数据源最广泛使用的资源。这些数据源的数据权限确定如下：

Datasets and streams are the most widely used resources as input data sources for [object types](/docs/foundry/object-link-types/object-types-overview/). Data permissions for these data sources are determined as follows:
* **[Datasets](/docs/foundry/data-integration/datasets/)：** 数据集中的每一行对应 Ontology 中的一个 object instance，任何对数据集及其 transactions 拥有至少 `Viewer` 权限的用户都将有权访问从该数据集创建的所有 object instances。

* **[Streams](/docs/foundry/data-integration/streams/)：** Streams 是用于 Ontology 中低延迟流式数据的输入数据源。任何对 stream 数据源拥有至少 `Viewer` 权限的用户都可访问从该 stream 数据源创建的所有 object instances。

* **[Datasets](/docs/foundry/data-integration/datasets/):** Each row in the dataset corresponds to an object instance in the Ontology, and any user that has at least `Viewer` permissions on the dataset and its transactions will have access to all object instances created from that dataset.
* **[Streams](/docs/foundry/data-integration/streams/):** Streams are input data sources used for low-latency streaming data in the Ontology. Any user that has at least `Viewer` permissions on the stream data source has access to all object instances created from that stream data source.
如果您需要使用 data source policies 实现行级或列级权限控制，可以使用 [restricted views (RVs)](#restricted-views) 和 [multi-data source object types (MDOs)](#multi-data-source-object-types)。

If you need row-level or column-level permissioning using data source policies, you can use [restricted views (RVs)](#restricted-views) and [multi-data source object types (MDOs)](#multi-data-source-object-types).
### Configure data source policies with RVs and MDOs
#### Restricted views
> **ℹ️ 注意**

> Restricted views 只能在 datasets 之上构建。不支持其他数据源类型。
> **ℹ️ 注意**

> Restricted views can only be built on top of datasets. No other data source types are supported.
Restricted views 允许对数据集中的特定行以及从这些行创建的对应 object instances 进行 *行级访问控制*。对具有特定主键的 object instance 的访问权限由能够访问 restricted view 输入数据源中该特定行的用户决定。

Restricted views enable *row-level access control* to certain rows in a dataset and the corresponding object instances created from those rows. Access to an object instance with a specific primary key is governed by who can access that specific row in the restricted view's input data source.
例如，医疗机构的员工可能能够查看其所在护理中心就诊患者的 dataset 行和 object instances，但可能被限制无法查看仅在其他护理中心就诊的患者数据，即使这两种类型的数据存在于同一 dataset 和 object type 中。

For example, a healthcare employee may be allowed to view dataset rows and object instances for patients that visit their care center, but they may be restricted from viewing data for patients that only visit other care centers, even if both types of data exist in the same dataset and object type.
如果给定 dataset `care_event_info` 包含 `patient_id`、`doctor_id` 和 `care_center` 列，则可以在其之上构建一个 restricted view，策略为 `user.userAttribute('care_center') == care_center`。该 restricted view 将仅允许访问 `care_event_info` 中与用户所属护理中心相同的行。

If a given dataset, `care_event_info`, has `patient_id`, `doctor_id`, and `care_center` columns, a restricted view can be built on top of it with the policy `user.userAttribute('care_center') == care_center`. The restricted view will only allow access to rows in `care_event_info` that have the same care center as the user.
使用 Ontology Manager，可以按照与 dataset 相同的方式将 restricted views 选择为 object type 的输入数据源。

Using Ontology Manager, restricted views can be selected as the input data source of an object type in the same way as a dataset.
[了解有关设置 restricted views 和管理 object 行级权限的更多信息。](/docs/foundry/object-permissioning/configuring-rv-access-controls/)

[Learn more about setting up restricted views and governing row-level permission for objects.](/docs/foundry/object-permissioning/configuring-rv-access-controls/)
#### Multi-data source object types
> **ℹ️ 注意**

> Multi-data source object types 仅在 object storage v2 中可用。
> **ℹ️ 注意**

> Multi-data source object types are only available in object storage v2.
Ontology 支持将多个输入数据源映射到单个 object type。这种 object types 被称为 multi-data source object types (MDOs)。

The Ontology offers support for mapping multiple input data sources to a single object type. Such object types are referred to as multi-data source object types (MDOs).
MDOs 使您能够将不同数据源的列映射到 object type 的各个 properties。这使您能够将对应于各个输入数据源的多个访问控制应用于单个 object type。这些输入数据源可以是 datasets 或 restricted views 的任意组合。

MDOs enable you to map columns from different data sources to the various properties of an object type. This enables you to apply multiple access controls corresponding to separate input data sources, to a single object type. These input data sources can be any combination of datasets or restricted views.
例如，对于给定的诊疗事件 Object Type，一些医疗保健员工可能需要访问包含个人健康信息（`PHI`）的 Object 属性，而其他员工则不应有访问权限。可以通过使用两个独立的输入数据源来支撑 `Care Event` Object Type，并在每个输入数据源上应用不同的访问控制和权限，从而支持这种访问控制。`Care Event` Object Type 将 `Patient ID` 作为其主键，并由数据源 `patient_info` 和 `care_event_info` 支撑。

For example, for a given care event object type, some healthcare employees may require access to object properties containing personal health information (`PHI`), while other employees should not have access. This access control can be supported by backing the `Care Event` object type with two separate input data sources and applying different access controls and permissions on each input data source. The `Care Event` object type has `Patient ID` as its primary key and is backed by data sources `patient_info` and `care_event_info`.
* `patient_info` 包含列 `patient_id`、`name`、`address`、`contact_number` 和 `age`。该数据集具有 `PHI` 标记。只有具有 `PHI` 标记访问权限的用户才能访问来自 `patient_info` 的属性值。

* `care_event_info` 包含列 `patient_id`、`doctor_id` 和 `care_center`。该数据集未标记。用户无需任何标记的访问权限即可访问此数据集中的属性值。

* `patient_info` has the columns `patient_id`, `name`, `address`, `contact_number`, and `age`. This dataset has the `PHI` marking. Only users with access to the `PHI` marking will have access to the property values from `patient_info`.
* `care_event_info` has columns `patient_id`, `doctor_id`, and `care_center`. This dataset is unmarked. Users do not need access to any markings to access the property values from this dataset.
这些不同的权限将被遵守并应用于 Object 实例。除非用户具有 `PHI` 标记的访问权限，否则他们将无法访问从 `patient_info` 映射的属性，例如 `name`、`address`、`contact_number` 和 `age`。

These different permissions will be respected and applied to the object instance. A user will not have access to the properties mapped from `patient_info`, such as `name`, `address`, `contact_number`, and `age`, unless they have the `PHI` marking.
[了解更多关于设置 MDO 以及管理 Object 的列级权限的信息。](/docs/foundry/object-permissioning/multi-datasource-objects/)

[Learn more about setting up MDOs and governing column-level permissions for objects.](/docs/foundry/object-permissioning/multi-datasource-objects/)