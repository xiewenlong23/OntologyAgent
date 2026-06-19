<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-edits/materializations/
---
# Materializations
最新的数据对于许多 Foundry 工作流至关重要。Ontology 用户可以基于 Ontology 中的索引数据创建**物化（materializations）**,通过结合输入 datasource 和用户编辑的数据来包含每个 Object 的最新状态。

Up-to-date data is critical to many Foundry workflows. Ontology users can create **materializations** of indexed data from the Ontology that contains the latest state of each object by combining data from both input datasources and user edits.
## Use cases for materializations
物化的两个主要用例如下:

The two main use cases for materializations are:
* 构建需要每个 Object 最新状态(包括用户编辑)的下游 Foundry pipeline。

* 支持下载包含某个 Object Type 所有 Object 最新状态的 Ontology 数据。

* Building downstream Foundry pipelines that require the latest state of each object including user edits.
* Enabling downloads of Ontology data containing the latest state of all objects for an object type.
> **ℹ️ 注意**

> 我们建议通过创建物化数据集,并通过其他 Foundry 数据集现有的下载工作流来发起下载,从而在 Foundry 中协调批量下载,例如 [data exports](/docs/foundry/analytics/exporting-outputs/#data-export) 以及通过 [Foundry transforms](/docs/foundry/code-repositories/prepare-datasets-download/#prepare-datasets-for-download) 进行的导出。
> **ℹ️ 注意**

> We recommend orchestrating bulk downloads in Foundry by creating materialized datasets and initiating the downloads through existing download workflows for other Foundry datasets, such as [data exports](/docs/foundry/analytics/exporting-outputs/#data-export) and exports through [Foundry transforms](/docs/foundry/code-repositories/prepare-datasets-download/#prepare-datasets-for-download).
## Create a materialized dataset
通过在 Ontology Manager 的 **Datasources** 选项卡中切换 [**Edits** 配置](/docs/foundry/object-edits/how-edits-applied/),导航至 **Materializations** 选项卡。在 **Materializations** 选项卡中,您可以根据 [input datasource types](/docs/foundry/object-permissioning/managing-object-security/#object-input-data-sources) 创建具有各种配置的物化 Object 数据集或 Object 受限视图。请注意,物化将自动更新,无法从 Dataset Preview 手动构建。

Navigate to the **Materializations** tab by toggling the [**Edits** configuration](/docs/foundry/object-edits/how-edits-applied/) in the **Datasources** tab in Ontology Manager. On the **Materializations** tab, you can create materialized object datasets or object restricted views with various configurations depending on [input datasource types](/docs/foundry/object-permissioning/managing-object-security/#object-input-data-sources). Note that Materializations will update automatically and cannot be built manually from Dataset Preview.
![Materializations landing page](/docs/resources/foundry/object-edits/materializations.png)
## Comparison of writeback datasets and materialized datasets
在 Object storage v1 (OSv1)(也称为 phonograph)中,[writeback datasets](/docs/foundry/slate/references-writeback/) 等同于物化数据集。在 OSv1 中,要对 Object Type 或带有连接表的多对多 Link Type 启用用户编辑,需要 writeback datasets。

In object storage v1 (OSv1), also known as phonograph, [writeback datasets](/docs/foundry/slate/references-writeback/) are the equivalent of materialized datasets. Writeback datasets are required in OSv1 to enable user edits on an object type or a many-to-many link type with a join table.
Object storage v2 (OSv2) 不需要物化数据集来启用用户编辑。用户可以通过在 Ontology Manager 的 **Datasources** 选项卡中切换 **Edits** 配置来为 Object Type 启用用户编辑。这使得物化在 OSv2 中变为可选项,因此用户仅在上述两个主要用例需要时才需要创建物化。如果用户希望仅物化 Object Type 的部分 Property,OSv2 还允许创建多个物化数据集。

Object storage v2 (OSv2) does not require materialized datasets to enable user edits. Instead, users can enable user edits for an object type by toggling the **Edits** configuration in the **Datasources** tab in Ontology Manager. This makes materializations optional in OSv2 such that users would only need to create materializations if needed for the two main use cases mentioned above. OSv2 also allows multiple materialized datasets to be created, in case users want to materialize only a subset of the properties from an object type.
OSv1 writeback datasets 和 OSv2 物化数据集之间的其他行为差异描述如下。

Other behavior differences between OSv1 writeback datasets and OSv2 materialized datasets are described below.
### Build schedules in writeback and materialized datasets
OSv1 (Phonograph) writeback datasets 和 OSv2 物化数据集的构建调度处理方式不同。

OSv1 (Phonograph) writeback datasets and OSv2 materialized datasets handle build schedules differently.
* 在 OSv1 中,当出现新的用户编辑时,没有机制可以触发 writeback datasets 的构建。相反,用户可以创建 [schedules](/docs/foundry/building-pipelines/create-schedule/) 来按需频繁构建其 writeback datasets。当没有新数据时,这些构建会自动中止,以避免使用任何额外的算力。如果未设置 schedule 且 writeback dataset 未被构建,则 writeback dataset 中的数据可能无法准确反映 Ontology。

* OSv2 被设计为以不同方式应对两个独立的用例。

* 为了让用户编辑在 [edits are applied](/docs/foundry/object-edits/how-edits-applied/) 后尽快反映在物化数据集中,用户可以启用用户编辑的**自动（automatic）**传播。此模式会自动将用户编辑传播到已配置的物化数据集(延迟为几分钟)。由于构建频率可能会根据新用户编辑的频率而增加,因此可能会产生额外的成本。

* 如果用户编辑传播到物化数据集的延迟并不重要,用户可以通过配置**周期性（periodic）**构建来降低成本。在此模式下,每当输入 datasource 有新数据时或每 6 小时,物化数据集就会被重建。

* In OSv1, there is no mechanism to trigger builds for writeback datasets when there are new user edits. Instead, users can create [schedules](/docs/foundry/building-pipelines/create-schedule/) for building their writeback datasets as often as they want. When there is no new data, these builds are automatically aborted to avoid using any additional compute. If no schedule is set up and the writeback dataset is not being built, the data in the writeback dataset may not be an accurate representation of the Ontology.
* OSv2 is designed to address two separate use cases differently.
* To have user edits reflected in the materialized datasets as soon as [edits are applied](/docs/foundry/object-edits/how-edits-applied/), users can enable **automatic** propagation of user edits. This mode propagates user edits to the configured materialized datasets automatically (with a latency of a few minutes). This may incur additional cost as more frequent builds may occur depending on the frequency of new user edits.
* If the latency of user edit propagation to materialized datasets is not critical, users can reduce costs by configuring **periodic** builds. In this mode, materialized datasets are rebuilt whenever the input datasources have new data or every 6 hours.
![Creating a new output dataset](/docs/resources/foundry/object-edits/materializations-2.png)
![Existing output datasets](/docs/resources/foundry/object-edits/materializations-3.png)
### Retention of writeback and materialized datasets
writeback 和物化数据集的保留机制工作方式不同。

The retention of writeback and materialized datasets do not work the same.
* 在 OSv1 中,writeback dataset 的行为类似于常规数据集,因为它可以应用平台上指定的特定 [retention policies](/docs/foundry/retention/overview/)。如果 writeback dataset 被定期构建,这使用户能够回溯查看 Object Type 状态的历史快照。

* In OSv1, the writeback dataset acts like a regular dataset in the sense that it can be put on specific [retention policies](/docs/foundry/retention/overview/) that can be specified within the platform. This enables users to look back at the historical snapshots of the object type state if the writeback dataset is built regularly.
* 在 OSv2 中,物化数据集受不可自定义的保留策略约束。历史事务会被持续删除,仅保证最新的快照可用。在这种情况下,如果需要保留 Object Type 状态的历史快照,用户必须设置下游 transform。此保留策略同样适用于 Object Type 删除的情况,在这种情况下,也需要通过下游 transform 来保留已删除 Object Type 的物化数据集。

* In OSv2, materialized datasets are subject to a retention that is not customizable. Historical transactions are constantly deleted and only the latest snapshot is guaranteed to be available. In this case, users will have to set up a transform downstream if it is important to keep historical snapshots of object type states. This retention policy also applies in the case of object type deletion, where a downstream transform is also required to keep a materialized dataset of a deleted object type.
### Dataset schema in writeback and materialized datasets
OSv1 (Phonograph) writeback datasets 和 OSv2 物化数据集与输入 datasource schema 的关联方式不同。

OSv1 (Phonograph) writeback datasets and OSv2 materialized datasets relate to input datasource schemas differently.
* 在 OSv1 中，输入数据源的 schema 会被复制并用作 writeback 数据集的 schema。

* OSv2 更改了此行为，以提高 Foundry Ontology 的可读性。由于用户正在从 Ontology 物化数据，因此用于物化数据集的 schema 是从 Ontology 定义中复制的，而不是依赖于底层数据源配置。具体而言，每个 property 的 [API Name](/docs/foundry/object-link-types/property-metadata/#metadata-reference) metadata 被用作物化数据集的 schema。如果您希望在 [从 OSv1 迁移到 OSv2](/docs/foundry/object-backend/osv1-osv2-migration/) 期间继续使用输入数据源的 schema（例如，为了保证现有 writeback 数据集的向后兼容性），请联系您的 Palantir 代表。

* In OSv1, the schema of the input datasource is copied and used as the schema of the writeback dataset.
* OSv2 changes this behavior to increase the legibility of the Foundry Ontology. Since users are materializing data from the Ontology, the schema used for materialized datasets is copied from the Ontology definitions instead of relying on the backing datasource configuration. Specifically, the [API Name](/docs/foundry/object-link-types/property-metadata/#metadata-reference) metadata of each property is used as the schema of the materialized dataset. Contact your Palantir representative if you want to continue using the schema of the input datasource while [migrating from OSv1 to OSv2](/docs/foundry/object-backend/osv1-osv2-migration/) (for example, to guarantee backward compatibility for existing writeback datasets).
> **⚠️ 警告**

> 物化数据集中以 `__` 为前缀的列（例如 `__is_deleted`、`__patch_offset`）是 Foundry 用于去重目的的 metadata 列，并不表示 object type 状态的任何信息。这些列可能会在未来版本中被重命名或移除，恕不另行通知，不应在生产工作流中使用。
> **⚠️ 警告**

> `__` prefixed columns (e.g. `__is_deleted`, `__patch_offset`) in the materialized dataset are metadata columns used by Foundry for deduplication purposes and do not represent any information on the state of the object type. These columns could be renamed or removed from future releases without prior warning and should not be used in production workflows.
### Restricted view materialization options
OSv1 (Phonograph) 不允许将 [restricted views](/docs/foundry/security/restricted-views/) 物化为 object type，因为这些 object type 使用 restricted views 作为输入数据源进行细粒度权限控制。用户只能物化包含来自 restricted view 输入数据源底层数据集中所有行的 writeback 数据集。然后，用户有责任根据其访问限制妥善保护对 writeback 数据集的访问。

OSv1 (Phonograph) does not allow materializing [restricted views](/docs/foundry/security/restricted-views/) for object types that are granularly permissioned using restricted views as an input datasource. Users can only materialize writeback datasets that contain all the rows from the backing dataset of the restricted view input datasource. Users are then responsible for properly securing access to the writeback dataset based on their access restrictions.
在 OSv2 中，对于使用 restricted views 作为输入数据源进行 [细粒度权限控制](/docs/foundry/object-permissioning/configuring-rv-access-controls/#use-restricted-views-to-back-object-types) 的 object type，用户可以将常规数据集或 restricted views 配置为物化资源，如下所示。

In OSv2, users can configure both regular datasets or restricted views as materialized resources for object types that are [granularly permissioned](/docs/foundry/object-permissioning/configuring-rv-access-controls/#use-restricted-views-to-back-object-types) using restricted views as an input datasource, as shown below.
![Materialized resource type selection](/docs/resources/foundry/object-edits/materializations-4.png)
对于具有 [多个输入数据源](/docs/foundry/object-permissioning/multi-datasource-objects/) 的 object type，用户可以通过选择他们希望从中物化数据的输入数据源来配置其物化数据集。如果未选择某个输入数据源，则从该输入数据源映射的 object type properties 将不会反映在物化数据集中。如果某些输入数据源是 restricted views，则用户有两种选择：

In the case of an object type having [multiple input datasources](/docs/foundry/object-permissioning/multi-datasource-objects/), users can configure their materialized datasets by selecting which input datasources they would like to materialize data from. If an input datasource is not selected, object type properties mapped from that input datasource will not be reflected in the materialized dataset. If some of the input datasources are restricted views, users have two options:
* 用户可以选择其中一个 restricted view 资源，将其物化为 [restricted view](/docs/foundry/security/restricted-views/#restricted-views)。示例配置如下所示。

* Users can select one of the restricted view resources to materialize as a [restricted view](/docs/foundry/security/restricted-views/#restricted-views). An example configuration is shown below.
![Materialized restricted views](/docs/resources/foundry/object-edits/materializations-5.png)
* 用户可以选择多个输入数据源，但在这种情况下，他们只能将 ontology 数据物化为 [Foundry dataset](/docs/foundry/data-integration/datasets/)。此限制存在的原因是不同的 restricted view 输入数据源可能具有 [不同的策略配置](/docs/foundry/security/restricted-views/#restricted-view-policies)，而 restricted views 目前不支持设置列级策略。示例配置如下所示。

* Users can select multiple input datasources, but in that case they can only materialize ontology data as a [Foundry dataset](/docs/foundry/data-integration/datasets/). This limitation exists because different restricted view input datasources can have [different policy configurations](/docs/foundry/security/restricted-views/#restricted-view-policies), and restricted views do not currently support setting column-level policies. An example configuration is shown below.
![Materialized datasets with RV source](/docs/resources/foundry/object-edits/materializations-6.png)
### Materializing datasets from restricted views
如上所述，OSv1 和 OSv2 都允许将使用 restricted views 作为输入数据源的 object type 物化为常规数据集。请注意，这是平台中用户可以将 restricted view 转换为 dataset 的唯一位置，因为 [restricted views 不能用作 transform 输入](/docs/foundry/security/restricted-views/)。物化数据集不携带 restricted view 策略，因此创建和可视化物化数据集需要一组提升的权限。

As stated above, both OSv1 and OSv2 allow object types with restricted views as input datasources to be materialized as regular datasets. Note that this is the only place in the platform where users can convert a restricted view to a dataset, since [restricted views cannot be used as transform inputs](/docs/foundry/security/restricted-views/). Materialized datasets do not carry restricted view policies, so creating and visualizing materialized datasets requires an elevated set of permissions.
为便于说明，我们将使用以下术语：

We will use the following terms for explanatory purposes:
* **Object type：** 所讨论的 object type。

* **Restricted view：** 支持 object type 的 restricted view。

* **Backing dataset：** restricted view 的 backing dataset。

* **Object type:** The object type at hand.
* **Restricted view:** The restricted view backing the object type.
* **Backing dataset:** The backing dataset of the restricted view.
下图展示了 backing dataset、restricted view 和 object type 之间的关系。

The diagram below demonstrates the relationship between the backing dataset, restricted view, and object type.
![An example of a backing dataset with discretionary controls.](/docs/resources/foundry/object-edits/materializing-from-rv-term-definition.png)
考虑到这些定义，我们现在将介绍用户创建新物化数据集并查看其事务所需的条件。请注意，这是两个独立的步骤。

With these definitions in mind, we will now cover what a user requires to create a new materialized dataset and view its transaction. Note that these are two separate steps.
为了创建新的物化数据集，用户需要拥有执行从 backing dataset 到新数据集的身份转换的权限。在安全方面，这意味着用户需要同时满足 backing dataset 和 restricted view 上的自由访问控制（DAC）和强制访问控制（MAC）。

In order to create a new materialized dataset, the user requires permission to perform an identity transformation from the backing dataset to a new dataset. Security-wise, this means that a user needs to satisfy discretionary and mandatory controls on both the backing dataset and the restricted view.
如果满足这些条件，用户将可以选择创建新的物化数据集，如下例所示。

If these conditions are met, the user will have the option to create a new materialized dataset, as shown in the example below.

> 📷 **[图片: 示例设置，其中用户拥有自由访问控制并且能够创建物化数据集。]**

> 📷 **[图片: An example setup where the user has discretionary controls and is able to create a materialized dataset.]**

如果不满足这些条件，用户将无法使用此选项。在以下示例中，用户没有必要的自主控制权限，因此无法创建物化数据集。

If these conditions are not met, the user will not have this option. In the following example, the user does not have the necessary discretionary controls and therefore cannot create a materialized dataset.

> 📷 **[图片: An example setup where the user does not have discretionary controls.]**

> 📷 **[图片: An example setup where the user does not have discretionary controls.]**

要查看物化数据集的事务，用户必须能够查看 backing dataset 的事务。换句话说，用户还必须满足 backing dataset 事务的强制控制要求。

To view the materialized dataset's transaction, the user must be able to view the transaction of the backing dataset. In other words, the user must satisfy the mandatory controls of the backing dataset's transaction as well.
如下图所示，我们可以看到 backing dataset、受限视图、Object Type 和物化数据集。Backing dataset 中的标记在受限视图中被切断，但会传播到物化数据集。这意味着用户需要满足此标记才能查看事务。

This is demonstrated in the following diagram, where we can see the backing dataset, restricted view, the object type, and the materialized dataset. The markings from the backing dataset, which are severed in the restricted view, get propagated to the materialized dataset. This means that the user needs to satisfy this marking to view the transaction.
![An example of a materialized dataset carrying provenance from the backing dataset.](/docs/resources/foundry/object-edits/materialized-dataset-carrying-provenance-from-backing-dataset.png)
对于 OSv2 Object Type，如果该 Object Type 包含类型为 [mandatory control](/docs/foundry/object-link-types/mandatory-control-properties/) 的 Property，则物化数据集还要求用户满足 `Allowed markings`、`Allowed organizations` 和 `Max classification` 上的所有强制控制。如上所述，Provenance 从 backing dataset 继承，并且对于包含类型为 mandatory control 的 Property 的 Object Type，也会强制执行在 Object Type 上定义的强制控制。

For OSv2 object types, if the object type contains properties of type [mandatory control](/docs/foundry/object-link-types/mandatory-control-properties/), the materialized dataset also requires the user to satisfy all mandatory controls on `Allowed markings`, `Allowed organizations` and `Max classification`. Provenance is carried over from the backing dataset as described above, and the mandatory controls defined at the object type are also enforced for object types containing properties of type mandatory control.
下图显示了一个带有一个标记的 backing dataset、一个带有两个标记（来自 backing dataset）的物化数据集，以及一个在 Object Type 中配置的标记。

Below is a diagram of a backing dataset with one marking, a materialized dataset with two markings coming from the backing dataset, and a marking that is configured in the object type.
![picture of lineage to demonstrate object type mandatory controls propagation](/docs/resources/foundry/object-edits/materialized-dataset-with-object-type-provenance.png)
Backing dataset 包含以下标记：

The backing dataset contains the following marking:

> 📷 **[图片: picture of backing dataset with a marking]**

> 📷 **[图片: picture of backing dataset with a marking]**

在 Object Type 配置中，我们可以配置一个类型为 mandatory control 的 Property，并附带另一个标记，如下所示。

In the object type configuration, we can configure a property of type mandatory control with another marking, as shown below.

> 📷 **[图片: An example of an object type property of type mandatory control.]**

> 📷 **[图片: An example of an object type property of type mandatory control.]**

作为此配置的结果，物化数据集将携带来自 backing dataset 和 Object Type（包含类型为 mandatory control 的 Property）的 Provenance。

As a result of this configuration, the materialized dataset will carry provenance from both the backing dataset and the object type, which contains a property of type mandatory control.

> 📷 **[图片: An example of a materialized dataset carrying provenance from the backing dataset.]**

> 📷 **[图片: An example of a materialized dataset carrying provenance from the backing dataset.]**

### Materializing datasets from restricted view restrictions
如果 OSv2 中的受限视图包含以下任何策略，则无法配置物化数据集：

You cannot configure a materialization dataset if a restricted view in OSv2 contains any of the following policies:
1. 如果受限视图包含引用用户强制控制的条件，并应用于 string Property。您必须将 Ontology 中的 string Property 转换为 [mandatory control property](/docs/foundry/object-link-types/mandatory-control-properties/)，确保可以配置最大 [Classification-based Access Control](/docs/foundry/security/classification-based-access-controls/) 或 [mandatory marking](/docs/foundry/security/markings/) 集。

2. 如果受限视图具有 authorized group ID 条件。

3. 如果受限视图 datasource 包含直接引用 [organizations](/docs/foundry/security/orgs-and-spaces/#organizations) 或 markings 作为静态值的条件。您必须确保组织和标记的细粒度条件引用 mandatory control properties，而不是 string properties 或静态值。

1. If the restricted view contains a condition that references a user's mandatory controls and is applied to a string property. Instead, you must convert the string property in your ontology to a [mandatory control property](/docs/foundry/object-link-types/mandatory-control-properties/), ensuring that you can configure a maximum [Classification-based Access Control](/docs/foundry/security/classification-based-access-controls/) or [mandatory marking](/docs/foundry/security/markings/) set.
2. If the restricted view has authorized group ID conditions.
3. If the restricted view datasource has conditions that directly reference [organizations](/docs/foundry/security/orgs-and-spaces/#organizations) or markings as static values. Instead, you must ensure that the organization and marking granular conditions reference mandatory control properties and not string properties or static values.
### Branching
Materializations 可以与 Global Branches 一起使用，但有以下限制：

Materializations can be used with Global Branches with the following limitations:
* 无法在 Branch 上创建 Materializations。

* 无法在 Branch 上编辑 Materializations。

* Materializations cannot be created on a branch.
* Materializations cannot be edited on a branch.
对具有关联 materialization 的 object type 所做的更改将在 branch 中建立索引。该 branch 的任何更新都将写入物化数据集或 restricted view。删除 object type 或将其从 branch 中移除也会删除物化数据集中的 branch。由于 restricted view 的限制，物化的 restricted view branch 将不会被删除。此限制的解决方案目前正在开发中。

Changes made to an object type that has an associated materialization will be indexed in a branch. Any updates from that branch will be written to the materialized dataset or restricted view. Deleting an object type or removing it from a branch will also delete the branch in the materialized dataset. Due to limitations with restricted views, materialized restricted view branches will not be deleted. A solution to this limitation is currently under development.