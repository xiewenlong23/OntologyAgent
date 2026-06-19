<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-edits/schema-migrations/
---
# Manage schema changes
## Changing object type schema
基于 Foundry Ontology 构建的 Workflow 和 Application 应随着组织需求的变化而演进；在某些情况下，这种演进可能涉及以需要在其他地方进行额外更改的方式更新 Object Type 的 schema（即"破坏性更改"）。Schema 的破坏性更改示例包括更改现有 Property 的数据类型、更改 Object Type 的 backing datasource，或更改 Object Type 的主键。有关[破坏性 Schema 更改的完整列表](#list-of-breaking-schema-changes)，请参见下文。

Workflows and applications built on the Foundry Ontology should evolve as an organization's needs change; in some cases, this evolution may involve updating the schema of object types in a way that requires additional changes elsewhere ("breaking changes"). Examples of breaking changes to the schema include changing the data type of an existing property, changing an object type’s backing datasource, or changing the primary key of an object type. See below for a [full list of breaking schema changes](#list-of-breaking-schema-changes).
在 Object Storage V1 (Phonograph) 中，用户界面不鼓励此类 Schema 更改，尤其是当 Object Type 已收到用户编辑时。这是因为在 OSv1 中无法迁移此类用户编辑；相反，破坏性更改将导致现有用户编辑丢失，除非执行耗时且复杂的人工干预。

In Object Storage V1 (Phonograph), the user interface discourages such schema changes, particularly when an object type has received user edits. This is because such user edits cannot be migrated in OSv1; instead, breaking changes will result in the loss of existing user edits unless time-consuming and complex manual intervention can be performed.
Object Storage V2 取消了对 Schema 更改的这一限制，以促进灵活且迭代的 Workflow 构建。为此，OSv2 提供了一个 Schema 迁移框架，其中包含一系列预定义的迁移，可在发生破坏性 Schema 更改后应用于现有的用户编辑。Ontology Manager 会自动检测破坏性 Schema 更改，并指导用户从预定义列表中选择迁移选项。有关[受支持迁移的完整列表](#list-of-supported-schema-migrations-in-osv2)，请参见下文。

Object Storage V2 removes this restriction on schema changes to facilitate flexible and iterative workflow building. To that end, OSv2 provides a schema migration framework with a list of predefined migrations that can be applied to existing user edits after a breaking schema change. The Ontology Manager automatically detects breaking schema changes and guides users to select a migration option from the predefined list. See below for a [full list of supported migrations](#list-of-supported-schema-migrations-in-osv2).
### Example workflow
在此示例 Workflow 中，用户从已具有现有用户编辑的 Object Type 中删除 `Description` Property。Ontology Manager 会自动将此识别为破坏性 Schema 更改，并显示一条警告，指出需要进行迁移，如下方截图所示。

In this example workflow, a user deletes the `Description` property from an object type that has existing user edits. Ontology Manager automatically identifies this as a breaking schema change and displays a warning that a migration is required, as seen in the screenshot below.
![Breaking change warning](/docs/resources/foundry/object-edits/breaking_changes.png)
除了显示警告外，当用户希望将其更改保存到 Ontology 时，Ontology Manager 将在 **Review changes** 界面中显示一个 **Migrations** 选项卡。在用户为该破坏性更改定义迁移之前，Ontology Manager 将阻止用户保存更改。这可以防止该更改破坏其他 Workflow。

In addition to displaying a warning, Ontology Manager will present a **Migrations** tab in the **Review changes** interface when the user wants to save their changes to the Ontology. Ontology Manager will block the user from saving changes until they define a migration for the breaking change. This prevents the change from breaking other workflows.
当用户导航至 **Migrations** 选项卡时，Ontology Manager 会根据破坏性更改的类型显示可用的迁移选项，如下所示。

When the user navigates to the **Migrations** tab, the Ontology Manager displays the available migration options based on the type of breaking change, as shown below.
![Review edits](/docs/resources/foundry/object-edits/edits_review.png)
一旦用户在 Ontology Manager 中指定并保存 Schema 更改，就会在后端为该 Object Type 创建一个新的 Schema 版本，并编排相应的 [replacement Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/#funnel-batch-pipelines) 来更新该 Object Type 的索引。新的 Object Type 版本将在 replacement pipeline 完成并且新版本被声明为已完全 [hydrated by object databases](/docs/foundry/object-indexing/funnel-batch-pipelines/#hydration) 后，立即可供 Object Set Service (OSS) 和其他 Ontology API 的使用者查询。

Once a schema change is specified and saved by a user in the Ontology Manager, a new schema version is created for the object type in the backend, and a corresponding [replacement Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/#funnel-batch-pipelines) is orchestrated to update the index of the object type. The new object type version will be queryable by the Object Set Service (OSS) and other consumers of the Ontology APIs as soon as the replacement pipeline is completed and the new version is declared to be fully [hydrated by object databases](/docs/foundry/object-indexing/funnel-batch-pipelines/#hydration).
## List of breaking schema changes
以下 Ontology 中的更改被视为破坏性 Schema 更改：

The following changes in the Ontology are considered to be breaking schema changes:
* 更改 Object Type 的输入数据源

* 更改 Object Type 的主键

* 更改 Property 的数据类型

* 更改已收到用户编辑的 Property 的 ID

* 删除已收到用户编辑的 Property

* 删除已收到用户编辑的 struct field

* 更改 struct field 的数据类型

* Changing the input datasources of an object type
* Changing the primary key of an object type
* Changing the data type of a property
* Changing the ID of a property that has received user edits
* Deleting a property that has received user edits
* Deleting a struct field that has received user edits
* Changing the data type of a struct field
## List of non-breaking schema changes
以下 Ontology 中的更改**不**被视为破坏性 schema 更改：

The following changes in the Ontology are **not** considered to be breaking schema changes:
* 更改已收到用户编辑的 property 的显示名称、title key、render hints、type classes 或可见性

* 删除从未收到用户编辑的 property，或对从未收到用户编辑的 property 进行 schema 更改

* 删除从未收到用户编辑的 struct field，或对从未收到用户编辑的 struct field 进行 schema 更改

* Changing the display name, title key, render hints, type classes, or visibility of a property that has received user edits
* Deleting properties or making schema changes to properties that have never received user edits
* Deleting struct fields or making schema changes to struct fields that have never received user edits
## List of supported schema migrations in OSv2
以下是 Object Storage V2 中当前支持的全部 schema 迁移列表。

Below is the full list of schema migrations that are currently supported in Object Storage V2.
* **Drop all property edits（删除所有 property 编辑）：** 此迁移指令会删除 object type 上特定 property 的所有现有用户编辑。该 object type 上其他 property 的用户编辑不受影响。当从 object type 中删除某个 property 且没有新的 property 作为替代时，通常会使用此指令。

* **Drop all property edits:** This migration instruction drops all existing user edits on a specific property of an object type. User edits on other properties of the object type are not impacted. This instruction is generally used when deleting a property from an object type and there is no new property as a replacement.
* **Drop all struct field edits（删除所有 struct field 编辑）：** 此迁移指令会删除 object type 的 struct property 中特定 struct field 的所有现有用户编辑。同一 struct property 上其他 struct field 的用户编辑不受影响。当从 struct property 中删除某个 struct field 且没有新的替代 struct field 时，通常会使用此指令。

* **Drop all struct field edits:** This migration instruction drops all existing user edits on a specific struct field within a struct property of an object type. User edits on other struct fields on the same struct property are not impacted. This instruction is generally used when deleting a struct field from a struct property, and there is no new replacement struct field.
* **Drop all edits（删除所有编辑）：** 此迁移指令会删除 object type 上所有 property 的所有现有用户编辑。当此迁移运行时，该 object type 的所有 object 的状态会重置为 input datasource 中的数据。要执行此迁移，请导航到该 object type 的 **Datasources** 选项卡，然后在 **Edits** 部分中选择 **Delete edits**。

* **Drop all edits:** This migration instruction drops all existing user edits on all properties of an object type. When this migration runs, the state of all objects of an object type is reset to data in the input datasources. To execute this migration, navigate to the  **Datasources** tab of the object type and select **Delete edits**, located in the **Edits** section.
* **Move edits（移动编辑）：** 此迁移指令会移动特定 property 或整个 object type 上所有现有的用户编辑。此指令通常用于以下两种情况：

* 当现有 property 被重命名或删除，并由新的 property 替代时；或

* 当 object type 的 input datasource 正在被另一个 datasource 替代时。

* **Move edits:** This migration instruction moves all existing user edits on a specific property or on the entire object type. This instruction is generally used in two cases:
* When an existing property is renamed or deleted and being replaced by a new property, or
* When the input datasource of an object type is being replaced by another datasource.
* **Move struct field edits（移动 struct field 编辑）：** 此迁移指令会将特定 struct field 上所有现有的用户编辑移动到另一个 struct field。当现有 struct field 被删除并由新的 struct field 替代时，通常会使用此指令。

* **Move struct field edits:** This migration instruction moves all existing user edits on a specific struct field to another struct field. This instruction is generally used when an existing struct field is deleted and being replaced by a new struct field.
* **Cast property to new type（将 property 强制转换为新类型）：** 此迁移指令会将特定 property 上现有用户编辑的数据类型强制转换为该 property 的新数据类型。支持的数据类型强制转换列表如下：

* Attachment → String
* Boolean → String
* Date → String
* Double → Integer
* Double → Long
* Double → String
* Geopoint → String
* Geoshape → String
* Integer → Long
* Integer → Double
* Integer → String
* Long → Integer
* Long → Double
* Long → String
* Mandatory marking → String
* String → Integer
* String → Long
* String → Double
* String → Boolean
* String → Date
* String → Timestamp
* String → Geopoint
* String → Geoshape
* Timestamp → String
* **Cast property to new type:** This migration instruction casts the data type of existing user edits on a specific property to the new data type of the property. The list of supported data type casts are:
* Attachment → String
* Boolean → String
* Date → String
* Double → Integer
* Double → Long
* Double → String
* Geopoint → String
* Geoshape → String
* Integer → Long
* Integer → Double
* Integer → String
* Long → Integer
* Long → Double
* Long → String
* Mandatory marking → String
* String → Integer
* String → Long
* String → Double
* String → Boolean
* String → Date
* String → Timestamp
* String → Geopoint
* String → Geoshape
* Timestamp → String
* **Cast struct field to new type（将 struct field 强制转换为新类型）：** 此迁移指令会将特定 struct field 上现有用户编辑的数据类型强制转换为该 struct field 的新数据类型。支持的数据类型强制转换列表如下：

* Boolean → String
* Date → String
* Double → Integer
* Double → Long
* Double → String
* Geopoint → String
* Integer → Long
* Integer → Double
* Integer → String
* Long → Integer
* Long → Double
* Long → String
* String → Integer
* String → Long
* String → Double
* String → Boolean
* String → Date
* String → Timestamp
* String → Geopoint
* Timestamp → String
* **Cast struct field to new type:** This migration instruction casts the data type of existing user edits on a specific struct field to the new data type of the struct field. The list of supported data type casts are:
* Boolean → String
* Date → String
* Double → Integer
* Double → Long
* Double → String
* Geopoint → String
* Integer → Long
* Integer → Double
* Integer → String
* Long → Integer
* Long → Double
* Long → String
* String → Integer
* String → Long
* String → Double
* String → Boolean
* String → Date
* String → Timestamp
* String → Geopoint
* Timestamp → String
* **Revert migration（回滚迁移）：** 此迁移指令会回滚先前应用的 schema 迁移。当通过 Ontology Manager 中的 **History** 部分回滚已保存的 Ontology 更改时，通常会使用此指令。

* 要回滚迁移，请导航到目标 ontology 的 Ontology Manager 中的 **History** 部分，展开历史事件中的 **Migrations** 部分，打开迁移事件上的 **...** 菜单，然后选择 **Revert**。迁移回滚后，请在 Ontology Manager 中保存所做的修改。

* **Revert migration:** This migration instruction reverts a previously-applied schema migration. This instruction is generally used when a saved Ontology change is being reverted through the **History** section in the Ontology Manager.
* To revert a migration, navigate to the **History** section in the Ontology Manager for the desired ontology, expand the **Migrations** section within the history event, open the **...** menu on the migration event, and select **Revert**. Once the migrations have been reverted, save the modifications within the Ontology Manager.
![Revert migration](/docs/resources/foundry/object-edits/revert_migration.png)
> **ℹ️ 注意**

> 您一次最多只能应用 500 个 schema 迁移。如果 schema 更改的数量超过此限制，则必须分批执行迁移。
> 当前的 schema 迁移框架不支持对 object type 的主键 property 应用迁移指令。
> **ℹ️ 注意**

> You can only apply up to 500 schema migrations at a single time. If the number of schema changes exceeds this limit, the migration must be performed in batches.
> The current schema migration framework does not support applying migration instructions on the primary key property of object types.