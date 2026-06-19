<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-backend/object-storage-v2-breaking-changes/
---
# Breaking changes between Object Storage V1 and Object Storage V2
从 Object Storage V1 (Phonograph) 到 Object Storage V2 (OSv2) 的过渡是一次重大的架构转变,需要许多 breaking changes。旧版 Object Storage V1 (Phonograph) 拥有庞大的 API surface area,直接暴露了大量底层的 database 功能。相反,新的 Object Storage V2 架构通过 Object Data Funnel service 将 object 同步到专用的 object database 中,以获得在规模、性能、灵活性和安全性方面的改进。这种架构过渡带来两种主要类型的 breaking changes:

The transition from Object Storage V1 (Phonograph) to Object Storage V2 (OSv2) is a major architectural shift that requires a number of breaking changes. The legacy Object Storage V1 (Phonograph) has a large API surface area, exposing significant amounts of low-level database functionality directly. Conversely, the new Object Storage V2 architecture syncs objects through the Object Data Funnel service into specialized object databases to gain scale, performance, flexibility, and security improvements. This architectural transition leads to two main types of breaking changes:
* 专用的 object database 专为特定用例设计,可能无法提供与 Object Storage V1 相同的功能。这可能要求在 OSv2 中以与 OSv1 不同的方式对 workflow 进行建模。

* 分离在 Object Storage V1 中已合并的 [dimensions of concern](/docs/foundry/object-backend/overview/#object-storage-v2-architecture),需要重构某些直接与 OSv1 API 交互的现有 query。

* Specialized object databases, being designed for specific use cases, may not offer the same functionality as Object Storage V1. This may require workflows to be modeled differently in OSv2 than in OSv1.
* Separating [dimensions of concern](/docs/foundry/object-backend/overview/#object-storage-v2-architecture) that had been consolidated in Object Storage V1 requires refactoring of some existing queries that interact directly with OSv1 APIs.
这些 breaking changes 可能会阻碍某些由 OSv1 支持的 object type 在不进行重构或修复的情况下迁移到 OSv2。有关这些 issues 如何呈现给用户以及如何执行从 OSv1 到 OSv2 的迁移的更多信息,请参阅 [migrating to OSv2](/docs/foundry/object-backend/osv1-osv2-migration/) 的文档。

These breaking changes may block some OSv1-backed object types from migrating to OSv2 without refactoring or remediation. The documentation on [migrating to OSv2](/docs/foundry/object-backend/osv1-osv2-migration/) contains more information on how these issues are surfaced to the user, as well as how to perform a migration from OSv1 to OSv2.
## Permanent breaking changes
本节提供了 Object Storage V1 (Phonograph) 和 Object Storage V2 (OSv2) 之间 breaking changes 的列表。在尝试将任何 object type 迁移到 OSv2 之前,应先解决这些 breaking changes。OSv1 和 OSv2 之间的所有这些更改都旨在提升进入 Ontology 的数据质量、确保更具确定性的行为,并提高整个 platform 的可读性。

This section provides a list of breaking changes between Object Storage V1 (Phonograph) and Object Storage V2 (OSv2). These breaking changes should be addressed before trying to migrate any object type to OSv2. All of these changes between OSv1 and OSv2 are intended to improve the quality of data going into the Ontology, ensure more deterministic behavior, and increase legibility across the platform.
### Actions and edits
* OSv2 仅支持通过 Action 进行的用户编辑。所有对 OSv1 编辑 API 的现有直接 query 必须在迁移到 OSv2 之前重构为使用 Action。

* OSv2 将 "writeback dataset" 重命名为 "materialization"。在 OSv1 中,writeback dataset 是必需的;在 OSv2 中,materialization 是可选的。有关 materialized dataset 的更多详细信息,请参阅 [Materializations](/docs/foundry/object-edits/materializations/)。

* OSv2 only supports user edits via Actions. All existing direct queries on OSv1 edit APIs must be refactored to use Actions before migrating to OSv2.
* OSv2 renames "writeback datasets" as "materializations". In OSv1, writeback datasets are required; in OSv2, materializations are optional. See [Materializations](/docs/foundry/object-edits/materializations/) for more details on materialized datasets.
### Edit history
* 从 OSv1 迁移到 OSv2 提供了在 object 上保留 edit history 的选项。

* 启用此选项会将 edit history 包含在迁移过程中。请注意,这将产生额外的 compute cost,用于处理和存储。

* 如果不启用此选项,则来自 OSv1 的先前 edit 将保留;但是,来自 OSv1 的完整 edit history 在 OSv2 中将不可用。一旦迁移完成,将无法恢复来自 OSv1 的完整 edit history。在迁移到 Object Storage V2 时,用户必须确认除 Action Log 之外的用户编辑(Action)历史记录将不会被保留。

* 需要在 Ontology Manager 中为 OSv2 中的 object type 启用 [**Track user edit history**](/docs/foundry/object-edits/user-edit-history/),并且需要更新 object view 以添加 [Edit History widget](/docs/foundry/object-views/widgets-properties-links/#edit-history) 以显示用户 edit history。

* 用户还可以配置 [Action Log](/docs/foundry/action-types/action-log/) object type,以其他方式捕获 Action 如何影响 object;另请参阅 [Action Log Timeline widget](/docs/foundry/action-types/action-log/#action-log-timeline) 以跨目标 object 显示 Action 的历史记录。

* The migration from OSv1 to OSv2 provides the option to preserve edit history on the object.
* Enabling this option will include edit history with the migration process. Note that this will incur additional compute costs for processing and storage.
* If this is not enabled, previous edits from OSv1 will persist; however, the full edit history from OSv1 will not be available in OSv2. Once the migration is completed, it will not be possible to recover the full edit history from OSv1. Users are required to acknowledge that when migrating to Object Storage V2, the history of user edits (Actions) will not be preserved except for Action Logs.
* [**Track user edit history**](/docs/foundry/object-edits/user-edit-history/) will need to be enabled for object types in OSv2 within the Ontology Manager and object views will need to be updated to add the [Edit History widget](/docs/foundry/object-views/widgets-properties-links/#edit-history) to display user edit histories.
* Users may also configure [Action Log](/docs/foundry/action-types/action-log/) object types to otherwise capture how Actions affect objects; also, see the [Action Log Timeline widget](/docs/foundry/action-types/action-log/#action-log-timeline) to display a history of Actions across targeted objects.
### Data restrictions
OSv2 对主键和 Property 类型强制执行数据限制，以确保进入 Ontology 的数据质量。有关完整限制列表，请参阅 [OSv2 数据限制](/docs/foundry/object-indexing/data-restrictions/) 的文档。

OSv2 enforces data restrictions on primary keys and property types to ensure the quality of data going into the ontology. For the full list of restrictions, see the documentation on [OSv2 data restrictions](/docs/foundry/object-indexing/data-restrictions/).
### Changelog and incremental updates
* 对于具有 changelog datasource 的 Object Type，OSv2 不考虑 [legacy changelog datasets](/docs/foundry/building-pipelines/maintaining-incremental-performance/#changelog-datasets) 使用的 "latest timestamp wins" 语义。

* OSv2 默认以增量方式索引所有 pipeline；所有相关的 changelog 计算由 Funnel 在后台自动执行，使 "changelog python decorator" 变得多余。

* OSv2 对 geopoint properties 有更严格的验证。

* For object types with a changelog datasource, OSv2 does not consider the "latest timestamp wins" semantic used by [legacy changelog datasets](/docs/foundry/building-pipelines/maintaining-incremental-performance/#changelog-datasets).
* OSv2 indexes all pipelines incrementally by default; all relevant changelog calculations are automatically performed in the background by Funnel, rendering the "changelog python decorator" obsolete.
* OSv2 has stricter validations on geopoint properties.
### Monitoring
* OSv2 Object Type 只能通过 [monitoring views](/docs/foundry/monitoring-views/overview/) 进行监控，这取代了 [Object Storage V1 (Phonograph) sync status health check](/docs/foundry/health-checks/checks-reference/#sync-status)。

* OSv2 object types can only be monitored by [monitoring views](/docs/foundry/monitoring-views/overview/), which replaces the [Object Storage V1 (Phonograph) sync status health check](/docs/foundry/health-checks/checks-reference/#sync-status).
### Object Set Service (OSS) changes
* OSS APIs 不支持 query string；OSv1 支持 query string。

* OSS cardinality metrics **不**支持包含来自 Object Storage V1 和 Object Storage V2 对象的 Object Set，例如 multi-backend object sets。

* OSS APIs do not have query string support; OSv1 does have query string support.
* OSS cardinality metrics are **not** supported on object sets that contain objects from both Object Storage V1 and Object Storage V2, such as multi-backend object sets.
## Temporary breaking changes
本节列出了 Object Storage V1 (Phonograph) 与 Object Storage V2 (OSv2) 之间当前的功能差距。这些功能正在开发中，列表将在破坏性变更解决后更新。

This section lists out the current feature gap between Object Storage V1 (Phonograph) and Object Storage V2 (OSv2). These features are in development and the list will be updated as the breaking changes are resolved.
* OSv2 目前不支持在上下游目标之间通过 materialization 的路径连接 schedules。

* OSv2 目前不支持自定义 analyzers。

* Foundry Rules Archetypes 目前不支持 OSv2 的完整功能集。例如，由多个 datasources 支持的 Object Type 以及具有多个 materializations 的 Object Type 不受支持。有关更多详细信息，请参阅 [Foundry Rules 文档](/docs/foundry/foundry-rules/rule-logic/#inputs)。

* OSv2 currently does not support connecting schedules where the path between the upstream and downstream targets would go through a materialization.
* OSv2 currently does not support custom analyzers.
* Foundry Rules Archetypes currently does not support the full feature set of OSv2. For example, object types backed by multiple datasources and object types with multiple materializations are not supported. You can refer to the [Foundry Rules documentation](/docs/foundry/foundry-rules/rule-logic/#inputs) for more details.