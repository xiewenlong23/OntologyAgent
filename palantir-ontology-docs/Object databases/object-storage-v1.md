<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-databases/object-storage-v1/
---
# Object Storage V1 (Phonograph) \[Planned deprecation]
> **⚠️ 警告: 计划弃用**

> Object Storage V1 (Phonograph) 处于[计划弃用](/docs/foundry/platform-overview/development-life-cycle/)阶段，将于 2026 年 6 月 30 日之后不可用。[将您的 Object Type 和 Link Type 迁移](/docs/foundry/object-backend/osv1-osv2-migration/) 到 Object Storage V2。有关更多信息，请参阅 [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) 中的 `Migrate object types and many-to-many link types from Object Storage v1 to v2` intervention。
> 如果您对工作流中的 OSv1 到 OSv2 迁移有疑问，请联系 Palantir Support。
> **⚠️ 警告: Planned deprecation**

> Object Storage V1 (Phonograph) is in the [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be unavailable after June 30, 2026. [Migrate your Object Types and Link Types](/docs/foundry/object-backend/osv1-osv2-migration/) to Object Storage V2. Reference the `Migrate object types and many-to-many link types from Object Storage v1 to v2` intervention in [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) for more information.
> Contact Palantir Support if you have questions about the OSv1 to OSv2 migration in your workflows.
本页面概述了 Ontology 的遗留 backing store——Object Storage V1 (Phonograph)。在较新的 Ontology 以及已完成迁移的 Ontology 中，Object Storage V2 是唯一选项。

This page provides an overview of the Ontology’s legacy backing store, Object Storage V1 (Phonograph). On newer ontologies and those that have completely migrated, Object Storage V2 is the only option.
![Object Storage V1 (Phonograph)](/docs/resources/foundry/object-databases/object-storage-phonograph.png)
## Purpose
当 datasource 作为 Ontology backing datasource 或 Ontology Manager 中的 writeback dataset 添加时，该 datasource 会被注册然后索引到 Phonograph 中进行存储。当用户应用程序想要显示 object backing data 时，会查询 Phonograph，然后应用程序显示查询结果。

When a datasource is added as an Ontology backing datasource or as a writeback dataset in the Ontology Manager, the datasource is registered and then indexed into Phonograph for storage. When user applications want to display object backing data, Phonograph is queried and the applications display the results.
## Registration
当 backing datasource 最初添加到 object type 或 link type 时，该 datasource 必须在 Phonograph 中注册。数据必须先在 Phonograph 中注册，然后才能被用户应用程序查询或显示。

When a backing datasource is initially added to an object type or link type, the datasource must be registered in Phonograph. Data must be registered in Phonograph before it can be queried by or displayed in user applications.
Object type 或 link type 的 **Datasources** 选项卡中的 Phonograph 部分会显示 backing datasources 是否已成功注册到 Phonograph。如果 object type 或 link type 的 backing datasources 尚未成功注册到 Phonograph，则在该 object type 或 link type 的 display name 旁边（位于主页和搜索结果中）会显示一个红色的 "not registered" 标签。

The Phonograph section of the **Datasources** tab of an object type or link type displays whether or not the backing datasources are successfully registered in Phonograph. If an object type or link type’s backing datasources have not been successfully registered in Phonograph, a “not registered” red label will appear next to the object type or link type’s display name on the home page and in search results.
![Object Storage V1 (Phonograph) Registration](/docs/resources/foundry/object-databases/object-storage-phonograph-registration.png)
注销 object type 或 link type 的 backing datasource 会阻止其数据出现在用户应用程序中，同时也会清除用户数据编辑的历史记录（存储在 Phonograph 中）。若要详细了解注销 Phonograph 中的 backing datasource 所可能造成的潜在破坏性更改，以及在 Ontology Manager 中哪些操作需要执行注销，请参阅[有关潜在破坏性更改的文档](/docs/foundry/object-link-types/edit-object-type/#potential-breaking-changes)。如果您的更改可能对编辑历史记录或用户应用程序产生破坏性影响，Ontology Manager 始终会向您发出警告。

Unregistering an object type or link type’s backing datasource prevents its data from appearing in user applications and also removes the history of user data edits (stored in Phonograph). To read more about the potentially destructive changes that may be caused by unregistering a backing datasource from Phonograph, as well as actions in the Ontology Manager that require unregistering, see the [documentation on potential breaking changes](/docs/foundry/object-link-types/edit-object-type/#potential-breaking-changes). The Ontology Manager will always warn you if your changes have potentially destructive impact on edit histories or user applications.
## Index status
当对 backing datasource 中的数据进行更新，或对 object type 或 link type 的定义进行 schema 更改时，将开始一次 sync，将更新后的数据重新索引到 Phonograph 中。此次 sync（通常称为 reindex）完成后，更新后的数据和 schema 将出现在用户应用程序中。

When updates are made to data in the backing datasource or when schema changes are made to the definition of an object type or link type, a sync will begin that reindexes the updated data into Phonograph. Once this sync, often referred to as a reindex, is complete, the updated data and schema will appear in user applications.
Object type 或 link type 的 **Datasources** 选项卡中的 Phonograph 部分会显示最近一次 reindex 的开始状态。该状态可以是 `success`、`in progress` 或 `failed`。如果 object type 或 link type 的 backing datasources 最近一次 reindex 失败，则在该 object type 或 link type 的 display name 旁边（位于主页和搜索结果中）会显示一个红色的 "failed" 标签。

The Phonograph section of the **Datasources** tab of an object type or link type displays the status of the last reindex to be started. The status can be `success`, `in progress`, or `failed`. If the last reindex of the backing datasources of an object type or link type has failed, a “failed” red label will appear next to the object type or link type’s display name on the home page and in search results.
![Index status: Failed](/docs/resources/foundry/object-databases/object-storage-phonograph-index-status-failed.png)
您可以 hover 或选择最近一次 sync 以获取更多详细信息，包括 sync 失败的原因。

You can hover over or select the last sync for more details, including why a sync may have failed.
## Incremental and batch reindexing
在 incremental indexing 中，仅对新数据更新进行索引。Object Storage V1 (Phonograph) 仅在该 datasource 的 [transaction type](/docs/foundry/data-integration/datasets/#transaction-types) 为 APPEND 或 UPDATE 时，才会对新的 datasource 事务进行增量索引。对于 SNAPSHOT 事务，OSv1 始终会触发 batch indexing（其中所有 objects 都会被重新索引）。

In incremental indexing, only new data updates are indexed. Object Storage V1 (Phonograph) indexes new datasource transactions incrementally only if the datasource [transaction type](/docs/foundry/data-integration/datasets/#transaction-types) is APPEND or UPDATE. For SNAPSHOT transactions, OSv1 always triggers batch indexing (in which all objects are reindexed).