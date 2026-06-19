<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-edits/how-edits-applied/
---
# How user edits are applied
可以使用 Ontology Manager 中 **Datasources** 选项卡下的 **Edits** 开关来启用和禁用用户编辑，如下方截图所示。

User edits can be enabled and disabled using the **Edits** toggle in the **Datasources** tab of the Ontology Manager, as shown in the screenshot below.
![Object Edits toggle](/docs/resources/foundry/object-edits/edits.png)
## Edit objects via Actions
本节介绍 Ontology 如何通过 Actions 管理 object 编辑。

This section describes how the Ontology manages object edits with Actions.
当 Action 应用于 object、link 或 object set 时，数据修改逻辑会立即应用于 object database 中的 index，并定期以由 Funnel 拥有和管理的 Foundry dataset 的形式 flush 到持久化存储中。更多信息可在[用户编辑的持久化存储](#persistent-storage-of-user-edits)文档中找到。

When an Action is applied to an object, link, or object set, the data-modification logic is immediately applied to the index in the object databases and periodically flushed into a persistent store in the form of Foundry datasets owned and managed by Funnel. More information can be found in the documentation on [persistent storage of user edits](#persistent-storage-of-user-edits).
### User edits on live data
当 Action 被触发时，Actions service 会向 Funnel service 发送一条 modification instruction。该 instruction 存储在 Funnel 管理的 queue 中，并通过 offset tracking 来支持同时进行的用户编辑。Object Storage V2 会跟踪任何 object type 以及任何具有 join table 的多对多 link type 的 offsets。这些 offsets 会被应用于 object database 中实时索引的数据；如果作为 ontology query 一部分发生的 object read 发生在用户 modification 发送之后，则该 object read 将保证包含用户编辑。

When an Action is triggered, the Actions service sends a modification instruction to the Funnel service. This instruction is stored in a Funnel-managed queue that has offset tracking to support simultaneous user edits. Object Storage V2 tracks these offsets for any object type and any many-to-many link type with join tables. The offsets are applied to the live indexed data in the object database; if an object read occurring as part of an ontology query happens after a user modification is sent, the object read is guaranteed to contain the user edits.
### How to discard/wipe/delete existing user edits
已包含用户编辑的数据只能通过额外的用户编辑进行更新。除了通过额外的用户编辑（例如 object actions）来更新 object 或重新创建 object 之外，没有任何机制可以直接撤消单个用户编辑或删除。

Data already containing user edits can only be updated via additional user edits. There is no mechanism to directly undo a single user edit or deletion other than to make additional user edits (for example, object actions) to update the object or to recreate the object.
在某些情况下，可能需要丢弃所有现有的用户编辑，以便将所有 objects 的状态重置为与输入 datasource 中的状态一致。例如，您可能希望在 object type 上线至生产环境之前，删除在测试期间应用于该 object type 的所有用户编辑。

In some circumstances, it may be desirable to discard all existing user edits in order to reset the state of all objects to be the same as in the input datasource. For example, you may want to delete all user edits applied during testing of an object type before releasing the object type in production.
Object Storage V2 提供了一个 [schema migration framework](/docs/foundry/object-edits/schema-migrations/) 用于迁移用户编辑。["drop all edits"](/docs/foundry/object-edits/schema-migrations/#list-of-supported-schema-migrations-in-osv2) 指令可用于丢弃 object type 上所有现有的用户编辑。此迁移指令可以通过点击 Ontology Manager 中 **Datasources** 选项卡的 **Edits** 部分下的 **Delete edits** 按钮来应用。

Object Storage V2 offers a [schema migration framework](/docs/foundry/object-edits/schema-migrations/) for migrating user edits. The ["drop all edits"](/docs/foundry/object-edits/schema-migrations/#list-of-supported-schema-migrations-in-osv2) instruction can be used to discard all existing user edits on an object type. This migration instruction can be applied by clicking the **Delete edits** button in the **Edits** section of the **Datasources** tab in the Ontology Manager.
![Delete Object Edits ](/docs/resources/foundry/object-edits/drop_edits.png)
Object Storage V1 (Phonograph) 不支持 schema migration，但从 object type 中移除 writeback dataset 配置将删除所有现有的用户编辑，这可以作为一种 workaround（变通方案）。

Object Storage V1 (Phonograph) does not have schema migration support, but removing the writeback dataset configuration from the object type will delete all the existing user edits and can be used as a workaround.
## Ontology entity version control
在应用 Action 的过程中，object type 定义和 object instances 会因各种目的而被加载，例如 Action 校验、[Functions](/docs/foundry/action-types/function-actions-overview/) 和 Action [side effects](/docs/foundry/action-types/side-effects-overview/)。Object instances 在应用 Action 的过程中可能会发生变化，因此保证事务性（transactionality）非常重要，以避免潜在的数据正确性问题（例如将 Action 应用到错误版本的对象上）。

During the process of applying an Action, object type definitions and object instances are loaded for various purposes, such as Action validations, [Functions](/docs/foundry/action-types/function-actions-overview/), and Action [side effects](/docs/foundry/action-types/side-effects-overview/). Object instances may change over the course of applying an Action, so it is important to guarantee transactionality to avoid potential data correctness issues (such as applying the Action to the wrong version of an object).
Ontology 包含用于检查 object types 和 object instances 版本一致性的机制，Object Storage V1 (Phonograph) 和 Object Storage V2 之间的行为有所不同。

The Ontology includes mechanisms for checking version consistency of both object types and object instances, with differing behaviors between Object Storage V1 (Phonograph) and Object Storage V2.
### Entity version control between front-end consumers and the Actions server
考虑以下场景：用户在 [Action form](/docs/foundry/action-types/getting-started/#edit-parameters) 中以版本 `{V1, V2, V3, ...}` 加载 object property 值。前端消费端应用程序使用这些 object property 值调用 Actions 服务器的 `/apply` 端点，但该请求不包含版本信息。收到此请求后，Actions 服务器在 `/apply` 端点中以版本 `{V1', V2', V3', ...}` 加载 objects。请注意，无法保证前端加载的版本 `{V1, V2, V3, ...}` 与 Actions 服务器加载的版本 `{V1', V2', V3', ...}` 始终相同。

Consider the following scenario where a user loads the object property value at versions `{V1, V2, V3, ...}` in an [Action form](/docs/foundry/action-types/getting-started/#edit-parameters). The front-end consumer application calls the `/apply` endpoint of the Actions server with those object property values, but that request does not include the versions. Upon receiving this request, the Actions server loads the objects within the `/apply` endpoint at versions `{V1', V2', V3', ...}`. Note that there is no guarantee that the versions `{V1, V2, V3, ...}` loaded on the front end and the versions `{V1', V2', V3', ...}` loaded by the Actions server will always be the same.
### Entity version control within the Actions server
#### Object Storage V1 (Phonograph) \[Planned deprecation]
> **⚠️ 警告: 计划弃用**

> Object Storage V1 (Phonograph) 处于 [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) 阶段，将于 2026 年 6 月 30 日之后不可用。[将您的 Object Types 和 Link Types 迁移](/docs/foundry/object-backend/osv1-osv2-migration/) 到 Object Storage V2。有关更多信息，请参阅 [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) 中的 `Migrate object types and many-to-many link types from Object Storage v1 to v2` intervention。
> 如果您对工作流中的 OSv1 到 OSv2 迁移有疑问，请联系 Palantir Support。
> **⚠️ 警告: Planned deprecation**

> Object Storage V1 (Phonograph) is in the [planned deprecation](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be unavailable after June 30, 2026. [Migrate your Object Types and Link Types](/docs/foundry/object-backend/osv1-osv2-migration/) to Object Storage V2. Reference the `Migrate object types and many-to-many link types from Object Storage v1 to v2` intervention in [Upgrade Assistant](/docs/foundry/upgrade-assistant/overview/) for more information.
> Contact Palantir Support if you have questions about the OSv1 to OSv2 migration in your workflows.
在 Object Storage V1 (Phonograph) 中，Actions 服务器会跟踪已加载对象的版本，并在整个 Action 执行过程中从缓存中加载相同的版本。当在 Object Storage V1 (Phonograph) 中应用用户编辑时，对象版本会包含在请求中。Object Storage V1 (Phonograph) 然后会检查任何对象版本是否已更改，如果检测到更改将抛出 `StaleObject` 错误。

With Object Storage V1 (Phonograph), the Actions server tracks the version of a loaded object and loads the same version from the cache throughout the Action execution. When a user edit is applied in Object Storage V1 (Phonograph), the object version is included in the request. Object Storage V1 (Phonograph) then checks if any of the object versions have changed and will throw a `StaleObject` error if a change is detected.
这些检查确保了 Actions 服务器内的一般一致性。例如，Object Storage V1 保证 Action 将在同一版本的对象上生成同步 [webhook](/docs/foundry/action-types/webhooks/)、执行、验证并应用编辑。请注意，不会检查属性级别的对象更改，因此对对象不相关属性的用户编辑可能会触发 `StaleObject` 冲突。

These checks ensure general consistency within the Actions server. For example, Object Storage V1 guarantees that an Action will generate a synchronous [webhook](/docs/foundry/action-types/webhooks/), execute, validate, and apply edits on the same version of an object. Note that object changes at a property level are not checked, so user edits on irrelevant properties of an object can trigger `StaleObject` conflicts.
#### Object Storage V2
在 Object Storage V2 中，Actions 服务器在将用户编辑发布到 Funnel service 之前会执行自己的对象版本检查，但与 Object Storage V1 (Phonograph) 相比，仅对服务器收集的版本的一个有限子集进行检查。

With Object Storage V2, the Actions server performs its own object version checks before posting user edits to the Funnel service, but on a limited subset of the versions collected by the server as compared to Object Storage V1 (Phonograph).
Actions 服务器仅检查直接用于生成编辑的对象版本，例如某个对象 `A` 的某个属性被复制到对象 `B` 上时该对象 `A` 的版本，并且这些版本仅针对已编辑的对象版本进行检查。

The Actions server only checks the versions of objects that are directly used to generate edits, such as the version of some object `A` that had one of its properties copied onto object `B`, and these versions are only checked against edited object versions.
此行为降低了 `StaleObject` 冲突的发生频率，但代价是 OSv2 的保证较弱。在 Object Storage V2 中，Actions 服务在 Action `/apply` 期间始终以相同版本加载 objects，但不保证在 Action 执行过程中 edit generation 之外读取的对象未发生更改。

This behavior reduces the frequency of `StaleObject` conflicts, with a consequence of weaker guarantees with OSv2. In Object Storage V2, the Actions service always loads objects at the same versions throughout an Action `/apply`, but does not guarantee that objects read outside of edit generation have not changed during the course of an Action.
#### Cross-backend Actions
如果 Action type 同时修改 OSv1 和 OSv2 中的对象，则被视为 "cross-backend"。在这种情况下，Actions 服务会对以下内容执行检查：

An Action type is considered "cross-backend" if it modifies objects in OSv1 and OSv2 at the same time. In such cases, the Actions service performs checks on:
* OSv1 中所有已读取和/或已编辑的对象，以及

* OSv2 中所有已编辑的对象。

* All read and/or edited objects in OSv1, and
* All edited objects in OSv2.
## Persistent storage of user edits
对象数据库中所有 indexed data 均被视为临时的（ephemeral），需要以其他方式持久存储所有 Ontology 数据。类似地，通过 Actions 应用的用户编辑也必须持久存储。支撑 object types 的 Foundry datasources 已经以 Foundry datasets、restricted views 等形式进行了持久存储。

All indexed data in object databases are considered ephemeral, requiring persistent storing of all Ontology data in other ways. Similarly, user edits applied through Actions also must be stored persistently. The Foundry datasources that back object types are already persistently stored in the form of Foundry datasets, restricted views, and so on.
如 [Funnel pipelines 文档](/docs/foundry/object-indexing/funnel-batch-pipelines/) 中所述，Funnel service 拥有并管理多个 Foundry datasets，包括一个将来自 datasources 和用户编辑的数据合并的 merged dataset。该 merged dataset 是自动构建的；这确保了存储在队列中的用户编辑被持久存储在 Foundry 中，并且队列被清空以防止队列增长过大。默认情况下，此构建作业在以下情况下触发：

As discussed in the [Funnel pipelines documentation](/docs/foundry/object-indexing/funnel-batch-pipelines/), the Funnel service owns and manages several Foundry datasets, including a merged dataset that combines data coming from datasources and user edits. The merged dataset is automatically built; this ensures that user edits stored in the queue are persistently stored in Foundry and that the queue is emptied in order to prevent the queue from growing too large. By default, this build job is triggered:
* 只要在 object type datasources 中出现新的数据事务,或者

* 如果在 datasources 中没有新数据,则每 6 小时一次,前提是在任何 objects 上检测到 edits。

* Whenever there is a new data transaction in object type datasources, or
* In the absence of new data in the datasources, every 6 hours, if edits had been detected on any objects.
## Resolve conflicting user edits and datasource updates
Foundry Ontology 中的 objects 可以由 input datasources 和 user edits 共同创建和修改。当单个 object(即具有特定主键值的行或 object)同时从 input datasource 和 user edits 接收数据时,这些接收到的值必须通过 *conflict resolution strategy* 进行透明地解析。

Objects in the Foundry Ontology can be created and modified by both input datasources and user edits. When a single object (that is, a row or object with a specific primary key value) receives data from both the input datasource and user edits, these received values must be transparently resolved with a *conflict resolution strategy*.
> **⚠️ 警告**

> 删除操作不被视为 edit。一旦应用了删除操作,无论 datasource 状态如何,该 object 都将不再可见。如果该 object 之后被重新创建,它将不会继承之前的 edits。
> **⚠️ 警告**

> Deletions are not considered an edit. Once a deletion is applied, the object is no longer visible regardless of datasource state. If the object is later recreated, it will not inherit the previous edits.
有两种解决冲突的策略:

There are two strategies for resolving conflicts:
* [Strategy 1: Apply user edits (default)](#strategy-1-apply-user-edits-default)
* [Strategy 2: Apply most recent value](#strategy-2-apply-most-recent-value)
* [Strategy 1: Apply user edits (default)](#strategy-1-apply-user-edits-default)
* [Strategy 2: Apply most recent value](#strategy-2-apply-most-recent-value)
### Strategy 1: Apply user edits (default)
使用此策略时,一个 object 的最终状态始终由应用于该 object 的 user edits 决定,无论同一 object 中已编辑 properties 的 datasource 后续如何更新。

With this strategy, the final state of an object is always determined by the user edits applied to it, regardless of any future datasource updates for edited properties in the same object.
请参考下面的流程图,根据 user edits 和 datasource 更新来确定 objects 的最新状态。

Refer to the flow chart below to determine the latest state of your objects based on user edits and datasource updates.
![Object Edits Flowchart](/docs/resources/foundry/object-edits/object-edits-visibility-flowchart.png)
下表展示了在遵循 "user edits always win" conflict resolution strategy 的情况下,特定 object 在接收 user edits 和 input datasource 更新后的状态变化。

The table below shows how the state of a specific object would be updated after receiving user edits and input datasource updates, following the "user edits always win" conflict resolution strategy.
| Time | Current datasource row state | User edit | Final object state |  Explanation |
| --- | --- | --- | --- | --- |
| T0 | `columns = {pk_column = pk1, col1 = val1, col2 = val2}` |  | `properties = {pk_column = pk1, col1 = val1, col2 = val2}, deleted = false` |  |
| T1 | `columns = {}` |  | `properties = {}, deleted = true` | Row disappears from the datasource, and the object is no longer in the Foundry Ontology |
| T2 | `columns = {pk_column = pk1, col1 = val1, col2 = val2}` |  | `properties = {pk_column = pk1, col1 = val1, col2 = val2}, deleted = false` | Same row reappears in the datasource |
| T3 | `columns = {pk_column = pk1, col1 = val1, col2 = val2}` | Modify object: `properties = {pk_column = pk1, col2 = newVal2}` | `properties = {pk_column = pk1, col1 = val1, col2 = newVal2}, deleted = false` | User runs a `Modify object` Action |
| T4 | `columns = {}` |  | `properties = {}, deleted = true` | Row disappears from the datasource again, and the object is no longer in the Foundry Ontology |
| T5 | `columns = {pk_column = pk1, col1 = val1, col2 = val2}` |  | `properties = {pk_column = pk1, col1 = val1, col2 = newVal2}, deleted = false` | Same row reappears in the datasource, and the previous user edit is still applied to the object when the row reappears |
| T6 | `columns = {pk_column = pk1, col1 = newVal1, col2 = val2}` |  | `properties = {pk_column = pk1, col1 = newVal1, col2 = newVal2}, deleted = false` | An unedited property (`col1`) receives data update from the input datasource, and it is applied to the object |
| T7 | `columns = {pk_column = pk1, col1 = newVal1, col2 = val2}` | Delete object | `properties = {}, deleted = true` | User runs a `Delete object` Action, and the object is no longer in the Foundry Ontology |
| T8 | `columns = {pk_column = pk1, col1 = newVal1, col2 = val2, col3 = null}` |  | `properties = {}, deleted = true` |  |
| T9 | `columns = {pk_column = pk1, col1 = newVal1, col2 = val2, col3 = null}` | Create object: `properties = {pk_column = pk1, col3 = val3}` | `properties = {pk_column = pk1, col1 = null, col2 = null, col3 = val3}, deleted = false` | User runs a `Create object` Action |
| T10 | `columns = {pk_column = pk1, col1 = newVal1, col2 = newVal2, col3 = newVal3}` |  | `properties = {pk_column = pk1, col1 = null, col2 = null, col3 = val3}, deleted = false` | `col3` is updated in the input datasource but is no longer considered for the final state of the object due to the prior `Create object` Action |
| T11 | `columns = {pk_column = pk1, col1 = newVal1, col2 = newVal2, col3 = newVal3}` | Modify object: `properties = {pk_column = pk1, col2 = newVal22}` | `properties = {pk_column = pk1, col1 = null, col2 = newVal22, col3 = val3}, deleted = false` | User runs a `Modify object` Action |
| T12 | `columns = {}` |  | `properties = {pk_column = pk1, col1 = null, col2 = newVal22, col3 = val3}, deleted = false` | Row disappears from the datasource, but the object is still in the Foundry Ontology as it was last created by a user edit |
| T13 | `columns = {pk_column = pk1, col1 = newVal1, col2 = newVal2, col3 = newVal3}` | Delete object | `properties = {}, deleted = true` | Row reappears, but user runs a `Delete object` Action and the object is deleted |
| T14 | `columns = {pk_column = pk1, col1 = newVal1, col2 = newVal2, col3 = newVal3}` | Modify object: `properties = {pk_column = pk1, col2 = newVal2, col3 = val3}` | `properties = {}, deleted = true` | User runs a `Modify object` Action on a deleted object; any `Modify object` Action call will fail |
### Strategy 2: Apply most recent value
使用此策略时,user edits 会被有条件地应用;也就是说,只有当 user edit 的时间戳比来自 datasource 的给定 object 的时间戳值更新时,user edits 才会被应用。请注意,由于每次 edit 的时间戳是与来自 datasource 的未编辑时间戳值进行比较的,因此在同一个 object 上,较新的 user edits 可能会被应用,而较旧的 user edits 可能不会被应用。

With this strategy, user edits are conditionally applied; that is, user edits are only applied if the timestamp of the user edit is more recent than the timestamp value coming from the datasource for the given object. Note that because the timestamp of each edit is compared against the unedited timestamp value coming from the datasource, it is possible for some newer user edits to apply and older user edits to not apply on the same object.
#### Configuration
Conflict resolution strategies 在 object type 级别进行配置,并且仅支持 OSv2 object types。

Conflict resolution strategies are configured at the object type level and are only supported for OSv2 object types.
用户可以在 Ontology Manager 中的 **Datasources** 部分配置此选项。Object type 的每个 datasource 可以采用不同的 resolution strategy。例如,对于由两个 datasources 支持的 object type,一个 datasource 可以使用 `Apply user edits (default)`,而另一个 datasource 可以使用 `Apply most recent value`。`Apply most recent value` 选项要求 datasource 包含一个 timestamp 类型的 property;date property type 不适用于此选项。Timestamp property 用于比较并决定是否应用 user edit。Timestamp property 必须采用协调世界时(UTC)。

Users can configure this option in the Ontology Manager, under the **Datasources** section. Each datasource of the object type can have different resolution strategies. For example, for an object type backed by two datasources, one datasource can use `Apply user edits (default)` while the other datasource can use `Apply most recent value`. The `Apply most recent value` option requires that the datasource contains a property with the timestamp type; the date property type will not work for this option. The timestamp property is used to compare and decide whether a user edit should be applied. The timestamp property must be in Coordinated Universal Time (UTC).
![edits conflict resolution configuration](/docs/resources/foundry/object-edits/edits-conflict-resolution-configuration.png)
#### Behavior
一旦为某个 datasource 保存了 `Apply most recent value` conflict resolution strategy,对该 datasource 所支持 properties 的所有 user edits 都将被有条件地应用。

As soon as the `Apply most recent value` conflict resolution strategy is saved for a datasource, all user edits to properties backed by that datasource will be conditionally applied.
对于每个 conditional edit,resolution 的工作方式是将 backing datasource 中的 timestamp 值与该 edit 关联的时间戳进行比较。对于在 conflict resolution strategy 更改 *之后* 应用于这些 properties 的 user edits,将根据导致该 edit 的 action 提交的时间戳进行有条件地应用;而对这些 properties 的任何 *现有* edits,将根据 conflict resolution strategy 更改的时间戳进行有条件地应用。

For each conditional edit, the resolution works by comparing the timestamp value in the backing datasource with the timestamp associated with the edit. For user edits to those properties applied *after* the conflict resolution strategy was changed, they will be conditionally applied based on the timestamp of the action submission that resulted in that edit, and any *existing* edits to those properties will be conditionally applied based on the timestamp of the conflict resolution strategy change.
如果 backing datasource 中 timestamp property 的值早于与 user edit 关联的时间戳,则应用该 user edit;否则,该 edit 将被忽略。

The user edit is applied if the value of the timestamp property in the backing datasource is older than the timestamp associated with the user edit, otherwise the edit is ignored.
如果一次 edit 跨多个 datasources 更新 properties,那么这些 edits 是被有条件地应用还是始终应用,将由支持该 property 的 datasource 的 resolution strategy 决定。

If an edit updates properties across multiple datasources, then whether those edits will be conditionally applied or always applied will be determined by the resolution strategy of the datasource that backs the property.
请参考下方更新后的流程图，根据用户编辑和数据源更新来确定您对象的最新状态。

Refer to the updated flow chart below to determine the latest state of your objects based on user edits and datasource updates.
![Object Edits Flowchart Most Recent Value](/docs/resources/foundry/object-edits/object-edits-visibility-flowchart-most-recent-strategy.png)
以下示例说明了此行为。假设对于一个 `Ticket` object type，存在两个对象，在 backing datasource 中包含以下数据，且 `Apply most recent value` 选项已启用。

The following example illustrates this behavior. Assume there are two objects for a `Ticket` object type with the following data in the backing datasource, where the `Apply most recent value` option is enabled.
| Ticket ID | Title      | Timestamp                    | Priority | Type            |
|-----------|------------|------------------------------|----------|-----------------|
| 101       | Ticket One | January 1, 2010, 9:00 AM UTC |P1        | Product Bug     |
| 102       | Ticket Two |                              |P2        | Feature Request |
假设针对这些 ticket 已运行了三个 action：

Suppose three actions have been run on these tickets, namely:
* 两个 ticket 的 title 均在 2010 年 1 月 1 日上午 8:30 被设置为 "Ticket"。

* 两个 ticket 的 priority 均在 2010 年 1 月 1 日上午 9:30 被设置为 "P0"。

* 两个 ticket 的 Type 均在 2010 年 1 月 1 日上午 10:30 被设置为 "Unknown"。

* Both tickets had their title set to "Ticket" at 8:30 AM on January 1, 2010.
* Both tickets had their priority set to "P0" at 9:30 AM on January 1, 2010.
* Both tickets had their Type set to "Unknown" at 10:30 AM on January 1, 2010.
那么在 ontology 中观测到的这两个对象的状态如下：

Then the observed state of the two objects in the ontology would be:
| Ticket ID | Title      | Timestamp                    | Priority | Type    |
|-----------|------------|------------------------------|----------|---------|
| 101       | Ticket One | January 1, 2010, 9:00 AM UTC | P0       | Unknown |
| 102       | Ticket     |                              | P0       | Unknown |
对于 Ticket ID 为 101 的 ticket，Title property 的编辑未应用，因为该编辑是在 backing datasource 中 9:00 AM 时间戳之前创建的。然而，对另外两个 property 的编辑发生在 9:00 AM 之后，因此会反映在已解析的对象中。

For the ticket with Ticket ID of 101, the edit to the Title property was not applied, because that edit was created before the 9:00 AM timestamp in the backing datasource. However, the edits to the other two properties occurred after 9:00 AM, and so are reflected in the resolved objects.
对于 Ticket ID 为 102 的 ticket，backing datasource 中的 timestamp property 没有值，因此所有三个条件编辑都会被应用，与其关联的时间戳无关。

For the ticket with Ticket ID of 102, there is no value for the timestamp property in the backing datasource, so all three conditional edits are applied, regardless of their associated timestamps.
#### Edit-only properties
对于 [edit-only properties](/docs/foundry/object-link-types/edit-only-properties/)，无论输入数据源上的时间戳如何，用户编辑将始终应用。

For [edit-only properties](/docs/foundry/object-link-types/edit-only-properties/), user edits will always apply regardless of the timestamp on the input datasource.
回到 [上文](#behavior) 的 ticket 示例，请参考下表：

Returning to the ticket example [above](#behavior), consider the following table:
|Ticket ID| Title      | Timestamp                    | Priority | Team (edit-only property) |
|---------|------------|------------------------------|----------|---------------------------|
|102      | Ticket Two | January 1, 2050, 9:00 AM UTC | P2       | Sales                     |
假设使用一个 action type `Change team` 将 `Team` property 修改为 `Recruiting`。如果将 `Change team` action 应用于 `Ticket Two`，则 team 将被设置为 `Recruiting`。无论使用哪种策略来解决冲突，由于 `Team` 是 edit-only property，编辑都将应用。

Suppose an action type, `Change team` is used to modify the `Team` property to `Recruiting`. If the `Change team` action is applied to `Ticket Two`, the team will be set to `Recruiting`. Regardless of which strategy is used for resolving conflicts, since `Team` is an edit-only property, edits will apply.
当 Action 同时修改 edit-only property 和常规 property 时，行为保持不变。常规 property 编辑根据条件应用，而 edit-only property 编辑始终应用。

The behavior remains the same when an Action modifies both edit-only and normal properties. Normal property edits are applied based on conditions, while edit-only property edits always apply.
#### Only input datasource values considered
请注意，Ontology 仅将编辑时间戳与输入数据源中的 timestamp 值进行比较。即使用户通过用户编辑更改了 timestamp property，条件比较也只会发生在输入数据源的时间戳与用户编辑应用时间之间。

Note that the Ontology only compares edit timestamps against the timestamp value from the input datasource. Even if users change the timestamp property via user edits, the conditional comparison will only happen between the timestamp from the input datasource and the user edit application time.
由于这种行为，timestamp property 必须由输入数据源中的 timestamp 列提供支持。如果源系统未提供 timestamp 值来指示数据流的更新时间，则可以在数据管道中修改输入数据源的 timestamp 列。

As a result of this behavior, the timestamp property must be backed by a timestamp column from the input datasource. If the source system does not provide a timestamp value to indicate the update time of the data feed, the timestamp column of the input datasource can be modified in the data pipeline.
回到 [上文](#behavior) 的 ticket 示例，请参考下表：

Returning to the ticket example [above](#behavior), consider the following table:
| Ticket ID | Title       | Timestamp                    | Priority |
|-----------|-------------|------------------------------|----------|
| 101       | Ticket One  | January 1, 2010, 9:00 AM UTC | P1       |
假设使用一个 action type `Change Timestamp` 将上述 ticket 的 timestamp 修改为 `January 1, 2050, 9:00 AM UTC`。

Suppose an action type `Change Timestamp` is used to modify the timestamp of the above ticket to `January 1, 2050, 9:00 AM UTC`.
| Ticket ID | Title       | Timestamp                                                     | Priority |
|-----------|-------------|---------------------------------------------------------------|----------|
| 101       | Ticket One  | ~~January 1, 2010, 9:00 AM UTC~~ January 1, 2050, 9:00 AM UTC | P1       |
如果现在对 Ticket One 应用 `Change Priority` Action,优先级仍将被设置为 `P0`。

尽管显示了 Object 的时间戳,但比较只会发生在输入 datasource 的时间戳和用户编辑应用时间之间。

If the `Change Priority` action is now applied to Ticket One, the priority will still be set to `P0`.
Despite the timestamp of the object shown, the comparison will only happen between the timestamp from the input datasource and the user edit application time.