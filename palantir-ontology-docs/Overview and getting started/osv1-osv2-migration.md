<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-backend/osv1-osv2-migration/
---
# Migrate from Object Storage V1 (Phonograph) to Object Storage V2
Object Storage V2 (OSv2) 的 [improvements](/docs/foundry/object-backend/overview/) 所需的架构变更，需要将 Object Storage V1 (Phonograph) 中的 Object Type 和带有 join tables 的 many-to-many Link Type 迁移到 Object Storage V2 (OSv2)。

The architecture changes necessary for the [improvements](/docs/foundry/object-backend/overview/) in Object Storage V2 (OSv2) require a migration of object types and many-to-many link types with join tables in Object Storage V1 (Phonograph) to Object Storage V2 (OSv2).
> **⚠️ 警告**

> 从 Object Storage V1 迁移到 V2 对所有 Object Type 都是**强制性的**。[Ontology Manager](/docs/foundry/ontology-manager/overview/) 提供了一个用于迁移 Object Type 和 many-to-many Link Type 的集成框架。
> **⚠️ 警告**

> Migration from Object Storage V1 to V2 is **mandatory** for all object types. [Ontology Manager](/docs/foundry/ontology-manager/overview/) provides an integrated framework for the migration of object types and many-to-many link types.
Foundry Ontology 不要求一次性迁移所有 Object Type 和 many-to-many Link Type。它将在部分 Object Type 位于 Object Storage V1 (Phonograph) 而部分位于 Object Storage V2 (OSv2) 的情况下继续正常运行。Foundry 的 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 也支持 [bulk migrations](#bulk-migrations)。

The Foundry Ontology does not require migrating all object types and many-to-many link types at once. It will continue its normal operation with some of the object types being in Object Storage V1 (Phonograph) and some in Object Storage V2 (OSv2). Foundry's [Ontology Manager](/docs/foundry/ontology-manager/overview/) also supports [migrating ontology types in bulk](#bulk-migrations).
## Considerations before running a migration
### Migration behavior
* 对 Object Type 上 Ontology 定义的任何更改，如果导致 [Funnel replacement pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/)，将中止任何正在进行的迁移。为避免这种情况，请确保 Object Type schema 在整个迁移期间（包括 soaking period）保持稳定，并在*启动*迁移之前执行任何 schema 更改。

* Object Storage V1 (Phonograph) 注册会同步更新在 Ontology Manager 中保存的任何更改。但是，Funnel 异步记录 Ontology 定义更改，从而导致在 Ontology Manager 中保存 Ontology 更改与 Funnel 检测到该更改之间存在延迟。因此，诸如 `start` 或 `abort` 等迁移事件可能会在 Ontology 保存后数秒钟延迟显示在 Ontology Manager 中。

* Object Storage V1 (Phonograph) 支持直接通过 Object Storage V1 (Phonograph) 编辑 APIs 编辑 Object Type 和 Link Type。此交互已弃用，与 OSv2 不兼容。在启动具有 user edits 的 Object Type 的迁移之前，请确保您的 [usage is compatible](#incompatible-usage)。然后，在 Ontology Manager 中找到该 Object Type 并导航至 **Datasources** 选项卡。开启 `Only allow edits via actions` 以解除该 Object Type 迁移的阻塞。

* 在整个迁移期间（包括 soak period），从迁移定义时刻起，将自动禁用 user edits。在迁移过程中无法发布新的 user edits，但 Object 读取将保持可用而不受干扰。

* 迁移提供保留 Object Type 的 edit history 和 attribution 的选项。

* 启用此选项将在迁移过程中包含 edit history。请注意，这会产生额外的计算和存储成本。

* 如果未启用保留 edit history 的选项，则 Object Type 的 edit history 和 attribution 在迁移期间将不会被保留，来自 Object Storage V1 (Phonograph) 的每个 Object 实例的最新状态将被迁移到 Object Storage V2。迁移完成后，将无法从 Object Storage V1 (Phonograph) 恢复完整的 edit history。用户需要确认，在迁移到 Object Storage V2 时，user edits (Actions) 的历史记录将不会被保留，但 Action Logs 除外。

* 迁移具有 decimal properties 的 Object Type 时，可能需要执行其他操作来设置 decimal precision 或 scale。如果 Object 包含 decimal property，或者该 property 需要设置 precision 或 scale，则可能发生以下错误：

* 错误：在配置向 Object Storage V2 的迁移时出现 `The current version of the object type has an invalid definition which Object Storage V2 is unable to index. ObjectsDataFunnel:DecimalPropertyTypeMissingPrecisionOrScale`

* 错误：`Precision does not match backing column.`

* 错误：`Scale does not match backing column.`

* 要解决与具有 decimal properties 的 Object Type 相关的这些错误，请按照以下步骤操作：

1. 导航至 Ontology Manager 中的 **Properties** 选项卡。

2. 选择出现错误的 property。

3. 为该 property 设置所需的 Precision 和 Scale 值。使用 **Fix** 按钮将根据您的 backing data 自动设置 Precision 和 Scale 值。

* Any changes to Ontology definitions on object types that would result in a [Funnel replacement pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) will abort any ongoing migrations. To avoid this, ensure that the object type schema remains stable for the entire migration (including soaking period), and perform any schema changes *before* initiating the migration.
* Object Storage V1 (Phonograph) registrations are updated synchronously for any changes saved in Ontology Manager. However, Funnel records ontology definition changes asynchronously, resulting in a delay between saving an ontology change in Ontology Manager and that change being detected by Funnel. Because of this, migration events like `start` or `abort` may appear in Ontology Manager with a delay of several seconds after the ontology is saved.
* Object Storage V1 (Phonograph) supports editing object and link types directly through Object Storage V1 (Phonograph) edit APIs. This interaction is deprecated and not compatible with OSv2. Before initiating the migration for an object type with user edits, ensure that your [usage is compatible](#incompatible-usage). Then, locate the object type in Ontology Manager and navigate to the **Datasources** tab.  Toggle on `Only allow edits via actions` to unblock the migration of that object type.
* User edits will be automatically disabled during the entire migration period, including soak period, starting from the moment of migration definition. New user edits cannot be posted during the migration process, but object reads will remain accessible without disruption.
* The migration provides the option to preserve the edit history and attribution of object types.
* Enabling this option will include edit history with the migration process. Note that this will incur additional compute costs for processing and storage.
* If the option to preserve edit history is not enabled, the edit history and attribution of object types will not be preserved during the migration and the latest state of each object instance from Object Storage V1 (Phonograph) will be migrated to Object Storage V2. Once the migration is complete, it will not be possible to recover the full edit history from Object Storage V1 (Phonograph). Users are required to acknowledge that when migrating to Object Storage V2, the history of user edits (Actions) will not be preserved, except for Action Logs.
* When migrating object types with decimal properties, additional action may be required to set the decimal precision or scale. The following errors may occur if the object contains a decimal property, or the precision or scale of the decimal needs to be set on that property:
* Error: `The current version of the object type has an invalid definition which Object Storage V2 is unable to index. ObjectsDataFunnel:DecimalPropertyTypeMissingPrecisionOrScale` when configuring the migration to Object Storage V2
* Error: `Precision does not match backing column.`
* Error: `Scale does not match backing column.`
* To resolve these errors related to object types with decimal properties, follow these steps:
1. Navigate to the **Properties** tab in Ontology Manager.
2. Select the property with the error.
3. Set the desired Precision and Scale values for that property. Using the **Fix** button will automatically set the Precision and Scale values based on your backing data.
### Incompatible usage
> **ℹ️ 注意**

> 如果无法访问 **Incompatible usage** 视图，请联系您的 Palantir 代表以启用此功能。
> **ℹ️ 注意**

> If the **Incompatible usage** view is not accessible, contact your Palantir representative about enabling this feature.
Object Storage V2 中的某些交互被认为是 [breaking changes](/docs/foundry/object-backend/object-storage-v2-breaking-changes/)，并且与 Object Storage V2 不兼容。这种 incompatible usage 会被跟踪并报告在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中。选择 **Incompatible usage** 告警将提供过去 30 天内任何 incompatible usage 的可视化，以协助修复。

Certain interactions in Object Storage V2 are considered [breaking changes](/docs/foundry/object-backend/object-storage-v2-breaking-changes/) and they are not compatible with Object Storage V2. This incompatible usage is tracked and reported in [Ontology Manager](/docs/foundry/ontology-manager/overview/). Selecting the **Incompatible usage** alert will provide a visualization of any incompatible usage in the last 30 days to assist in remediation.
![OSv1 to OSv2 migration incompatible usage visualization](/docs/resources/foundry/object-backend/migration3.png)
#### Non-blocking incompatible usage
某些 incompatible usage，例如直接对 Object Storage V1 (Phonograph) 端点的 API 调用，不会阻塞向 OSv2 启动迁移，但会在 Object Type 迁移到 OSv2 后失败。

Some incompatible usage, like direct API calls to Object Storage V1 (Phonograph) endpoints, will not block initiating a migration to OSv2 but will fail after the object type is migrated to OSv2.
![OSv1 to OSv2 migration warning](/docs/resources/foundry/object-backend/migration-warning.png)
您应调查 incompatible usage 并确定是否需要采取措施，例如将直接的 Object Storage V1 (Phonograph) 调用迁移到 [Object Set Service](/docs/foundry/object-backend/overview/#object-set-service-oss) 用于 Object queries/reads，[Actions](/docs/foundry/object-backend/overview/#actions) 用于 Object edits，以及 [Ontology Metadata Service](/docs/foundry/object-backend/overview/#ontology-metadata-service-oms) 用于 Object Type 元数据信息。如果这些 incompatible usage 已不再相关或可以无后果地中断，您可以在不进行修复的情况下启动迁移。

You should investigate incompatible usage and determine whether action is needed, such as migrating direct Object Storage V1 (Phonograph) calls to [Object Set Service](/docs/foundry/object-backend/overview/#object-set-service-oss) for object queries/reads, [Actions](/docs/foundry/object-backend/overview/#actions) for object edits, and [Ontology Metadata Service](/docs/foundry/object-backend/overview/#ontology-metadata-service-oms) for object type metadata information. If these incompatible usage are no longer relevant or can break without consequence, you can initiate the migration without remediation.
#### Blocking incompatible usage
OSv1 与 OSv2 之间的其他更改（例如不启用仅通过 actions 编辑）将主动阻塞 Ontology Manager 中的迁移。

Other changes between OSv1 and OSv2, such as not enabling editing by actions only, will actively block the migration in Ontology Manager.
![OSv1 to OSv2 migration error](/docs/resources/foundry/object-backend/migration-error.png)
在这种情况下，您必须在开始迁移之前移除所有不兼容的用法。

In this situation, you must remove any occurrences of the incompatible usage before starting the migration.
#### No incompatible usage
没有任何不兼容用法或破坏性更改的 Object Type 将在横幅中显示一个绿色对勾图标，以指示该 Object Type 已准备好进行迁移。

Object types without any incompatible usage or breaking changes will display a green tick icon in the banner to indicate that the object type is ready to migrate.
![OSv1 to OSv2 migration ready](/docs/resources/foundry/object-backend/migration-ready.png)
## Migrating an entity
### Starting a migration
要开始迁移，请导航到您的 Object Type 或带有 join table 的多对多 Link Type 的 **Datasources** 选项卡，然后进入 **Indexing Metadata** 部分。如果该 Object Type 符合迁移条件，您将能够选择 Object Storage V2 单选按钮，该按钮将打开一个用于选择迁移参数的向导。如果此部分不存在，则您很可能正在使用一个对所有 Object Type 和 join table Link Type 强制启用 Object Storage V2 的 Ontology 中。

To start the migration, navigate to the **Datasources** tab of your object type or many-to-many link type with a join table, and go to the **Indexing Metadata** section. If the object type is eligible for migration, you will be able to select the Object Storage V2 radio button that will open a wizard for selecting migration parameters. If this section is not present, you are most likely working in an ontology where Object Storage V2 is enforced for all object types and join table link types.
> **ℹ️ 注意**

> Ontology Metadata Service 会跟踪由 Object Storage V1 (Phonograph) 支持的 Object Type 的不兼容用法，并在尝试迁移具有不兼容用法的 Object Type 时触发警报。此外，您仍必须确保 Object Type schema 不包含任何破坏性更改。
> **ℹ️ 注意**

> The Ontology Metadata Service tracks incompatible usage of object types backed by Object Storage V1 (Phonograph) and will trigger an alert when attempting to migrate an object type with incompatible usage. Also, you must still ensure that the object type schema does not contain any breaking changes.
![OSv1 to OSv2 migration landing page](/docs/resources/foundry/object-backend/migration4.png)
### Transition windows
**Transition windows** 选项允许您为安全迁移设置首选时间窗口；例如，您可能希望设置一个 Object Type 使用案例活动最少的星期几和时间。请注意，在迁移过程开始后，可能需要长达 30 分钟才能启动第一个 Funnel pipeline。如果无法在第一个 transition window 内完成迁移，则 Object Set Service 将等到下一个 window 才开始从 OSv2 读取数据。

The **Transition windows** options allow you to set preferred time windows for a safe migration; for instance, you may want to set a day of the week and time when an object type's use case has minimal activity. Keep in mind that after the migration process begins, it may take up to 30 minutes to initiate the first Funnel pipeline. If the migration cannot be completed within the first transition window, then Object Set Service will wait until the next window to begin reading data from OSv2.
如果未设置 transition window，则迁移将在第一个 Funnel pipeline 成功后立即开始。

If no transition window is set, the migration will start as soon the first Funnel pipeline succeeds.
![OSv1 to OSv2 migration transition window](/docs/resources/foundry/object-backend/migration5.png)
> **ℹ️ 注意**

> transition window 将在第一次同步到 OSv2 成功完成后计算。这意味着如果第一次同步在已配置的 transition window 中间完成，迁移将不会将其视为可接受的 transition window，并将尝试采用下一个 window。
> **ℹ️ 注意**

> A transition window will be computed after the first sync to OSv2 finishes successfully. This means that if a first sync completes in the middle of a configured transition window the migration is not going to consider this as an acceptable transition window and will try to take the next one.
### Disabled action types
在迁移期间，用户将无法应用编辑，因为在从迁移定义开始的整个迁移期间（包括 soaking period），编辑将被自动禁用。请注意，Object 读取将保持可访问，不会中断。

During the migration, users will not be able to apply edits as they will be automatically disabled during the entire migration period, including the soaking period, starting from the moment of migration definition. Note that object reads will remain accessible without disruption.
### Soak period
如果您需要在迁移过程中回退到 Object Storage V1 (Phonograph)，这在 **soak period** 期间是可行的，无需重新索引数据。迁移框架将保持 Object Storage v1 (Phonograph) 索引与 Object Storage V2 (OSv2) 同步更新，直到 soak period 结束。Soak period 可以以天为单位进行设置，最长可达 14 天（可以选择指定小时数），并且仅在迁移通过 transition window 后才会开始。将 soak period 设置为 0 天将在 OSv2 索引就绪且 transition window 激活后立即删除该 Object Type 的 OSv1 索引。

If you need to revert to Object Storage V1 (Phonograph) during the migration process, this is possible without re-indexing data during the **soak period**. The migration framework will keep the Object Storage v1 (Phonograph) index up-to-date along with Object Storage V2 (OSv2) until the end of the soak period. The soak period can be set in increments of days, up to a maximum of 14 days (with the option to specify hours), and will only begin after the migration passes a transition window. Setting the soak period to 0 days will delete the OSv1 index for that object type as soon as the OSv2 index is ready and the transition window is activated.
在 soak period 期间，Foundry Ontology 后端将自动将所有查询路由到 OSv2，任何对 OSv1 的请求都将被拒绝。这段时间可用于验证在迁移后读取 Object Type 的工作流是否按预期工作。如果您在 soak period 期间遇到任何问题，您可以 [中止迁移](#aborting-the-migration) 以立即切换回使用 OSv1 索引。

During the soak period, the Foundry Ontology backend will automatically route all queries to OSv2 and any request to OSv1 will be rejected. This time period can be used to validate that the workflows that read object types are working as expected after the migration. If you experience any issues during the soak period, you can [abort the migration](#aborting-the-migration) to immediately switch back to using OSv1 indices.
Soak period 结束后，无法回滚到 OSv1。如有任何问题，您可以联系 Palantir Support。

After the soak period ends, it is not possible to rollback to OSv1. You may contact Palantir Support with any questions.
> **⚠️ 警告**

> 请注意，在 soak period 期间，Object Type 将在 OSv1 和 OSv2 中进行双索引；这将产生额外的计算和存储使用量。如果您希望避免额外的资源使用，可以在配置迁移时将 soak period 设置为 0 天。
> **⚠️ 警告**

> Note that object types will be dual-indexed in OSv1 and OSv2 during the soak period; this will incur additional compute and storage usage. If you would like to avoid the additional resource usage, you can set the soak period to 0 days when configuring the migration.
![OSv1 to OSv2 migration soak period](/docs/resources/foundry/object-backend/migration6.png)
### Migrating a writeback dataset
在 Object Storage V1 (Phonograph) 中，需要 [writeback datasets](/docs/foundry/slate/references-writeback/) 才能在 Object Type 或带有 join table 的多对多 Link Type 上启用用户编辑。Object Storage V2 用 [materialized datasets](/docs/foundry/object-edits/materializations/#comparison-of-writeback-datasets-and-materialized-datasets) 取代了 writeback datasets。Object Storage V2 不需要 materialized datasets 即可启用用户编辑。在 OSv2 中使用可选的 materialized datasets，您仅在下游使用需要时才需要创建 materializations。

In Object Storage V1 (Phonograph), [writeback datasets](/docs/foundry/slate/references-writeback/) are required to enable user edits on an object type or a many-to-many link type with a join table. Object Storage V2 replaces writeback datasets with [materialized datasets](/docs/foundry/object-edits/materializations/#comparison-of-writeback-datasets-and-materialized-datasets). Object Storage V2 does not require materialized datasets to enable user edits. With optional materialized datasets in OSv2, you only need to create materializations if they are required for downstream usage.
Object 和 Link Type 的 Writeback datasets 可以作为 OSv2 中的 materialization datasets 进行迁移。Materialization dataset 将保持相同的列，保留与现有下游 pipeline 的兼容性。此 toggle 仅在您正在其他应用程序中使用当前的 writeback dataset 时才相关。用户编辑仍将被迁移到 OSv2。

Writeback datasets of object and link types can be migrated as materialization datasets in OSv2. The materialization dataset will keep the same columns, retaining compatibility with existing downstream pipelines. This toggle is only relevant if you are using the current writeback dataset in other applications. User edits will still be migrated to OSv2.
> **ℹ️ 注意**

> 如果您选择不迁移 writeback dataset，则该 dataset 本身不会被删除。相反，该 dataset 将变为静态，并包含上次构建时的数据。
> **ℹ️ 注意**

> If you choose not to migrate the writeback dataset, the dataset itself will not get deleted. Instead, the dataset will be static and contain data from the last build time.
> **⚠️ 警告**

> 如果 writeback 数据集中包含未映射到任何 object type property 的列,这些列将在迁移过程中被丢弃。
> **⚠️ 警告**

> If the writeback dataset contains columns that are not mapped to any object type property, those columns will be dropped as part of the migration.
![Writeback dataset migration option](/docs/resources/foundry/object-backend/migration9.png)
### Aborting the migration
如果在切换到 Object Storage V2 后观察到性能下降或遇到 bug,您可以在 soak 期间安全地中止正在进行的迁移并回退到 OSv1。在整个迁移过程中,migration framework 会确保 OSv1 index 与任何新的数据同步保持一致。

If performance regression is observed or bugs are encountered after switching to Object Storage V2, you can safely abort an ongoing migration during the soak period and revert back to OSv1. Throughout the migration process, the migration framework ensures that the OSv1 index is kept up to date with any new data syncs.
如果正在迁移的 object type 存在现有用户编辑,在迁移完成之前,任何新的用户编辑都将被禁用。

If the object type being migrated has existing user edits, any new user edits will be disabled until the migration is completed.
### Sync failures
在迁移过程中,您的 object type 可能会同步失败。如果发生这种情况,您将在 object type 的 **Datasources** 选项卡的 **Indexing Metadata** 部分中看到 `PIPELINE_FAILED` 错误。如果出现这种情况,请按照[调试 funnel batch pipelines](/docs/foundry/object-indexing/funnel-batch-pipelines/#debug-a-pipeline) 的说明来调查并修复该问题。

Your object type may fail to sync during the migration process. If this is the case, you will see a `PIPELINE_FAILED` error in the **Indexing Metadata** section of your object types **Datasources** tab. If that happens, follow the instructions for [debugging funnel batch pipelines](/docs/foundry/object-indexing/funnel-batch-pipelines/#debug-a-pipeline) to investigate and remediate the issue.
![OSv1 to OSv2 migration failure](/docs/resources/foundry/object-backend/migration-failed.png)
### Bulk migrations
您可以使用相同的 transition window 和 soak time 配置批量运行迁移,方法是导航到左侧导航栏中的 **Object types** 部分,然后同时选择多个 object type。该过程和设置向导与迁移单个 object type 时相同。我们建议进行渐进式迁移,每次批量迁移少于 100 个 entities,以防止出现意外的复杂性或错误。

You can run migrations in bulk using the same transition window and soak time configurations by navigating to the **Object types** section in the left-hand navigation bar and selecting multiple object types at the same time. The process and setup wizard are the same as when migrating a single object type. We recommend gradual migrations that bulk-migrate less than 100 entities at a time to prevent unexpected complexity or errors.
此向导不会出现在仅启用了 OSv2 的 ontology 的 interface 中。

This wizard will not appear in the interface for ontologies that only have OSv2 enabled.
![OSv1 to OSv2 bulk migration](/docs/resources/foundry/object-backend/migration8.png)