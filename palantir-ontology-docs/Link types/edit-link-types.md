<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/edit-link-types/
---
# Edit link types
> **⚠️ 警告: Warning**

> 编辑 link type 可能会产生 **破坏应用程序的后果 (application-breaking consequences)**，从而中断用户的工作流。在继续任何 link type 编辑之前，**请先** 阅读下面关于 [potential breaking changes](#potential-breaking-changes) 的部分。
> **⚠️ 警告: Warning**

> Editing a link type can have **application-breaking consequences** that can disrupt user workflows. Read the section below on [potential breaking changes](#potential-breaking-changes) **before** proceeding with any link type edits.
## Potential breaking changes
### Link type without writeback
需要 Object Storage V1 (Phonograph) 注销并重新注册 link type 的 backing datasource 的更改，将使该类型的 links 在重新索引期间在用户应用程序中**不可用**；这些更改将在下文中描述。

Changes that require Object Storage V1 (Phonograph) to unregister and reregister the backing datasource of a link type will make the links of that type **unavailable** in user applications during that reindex time; these changes are described below.
保存时，以下更改将注销并重新注册（或删除）link type 的 backing datasource：

The following changes will unregister and reregister (or delete) the backing datasource of a link type when saved:
* 更改多对多 link type 的 backing datasource。

* 更改 link type 的 cardinality。

* 更改 link type 的 foreign key。

* 删除 link type。

* Changing a many-to-many link type’s backing datasource.
* Changing the cardinality of a link type.
* Changing the foreign key of a link type.
* Deleting a link type.
当您尝试保存这些更改中的任何一项时，系统会警告您其对用户应用程序的潜在影响。

When you try to save any of these changes, you will be warned about the potential impact on user applications.

> 📷 **[图片: 警告：重建索引将使对象不可用]**

> 📷 **[图片: Warning: Reindexing will make objects unavailable]**

例如，如果一个 link type 在 Workshop 应用程序的 search around 中被使用，那么该 Workshop 应用程序将在重建索引完成之前一直处于不可用状态。您可以在 link type 的 **Datasources** 页面中的 **Phonograph** 面板中跟踪其重建索引的进度。

For example, if a link type is used in a search around in a Workshop application, that Workshop application will be broken until the reindex completes. You can track the progress of the reindex for a link type in the **Phonograph** pane of its **Datasources** page.

> 📷 **[图片: 在 Phonograph 中跟踪重建索引]**

> 📷 **[图片: Tracking reindex in Phonograph]**

[了解更多关于 Object Storage V1 (Phonograph) 的信息。](/docs/foundry/object-databases/object-storage-v1/)

[Learn more about Object Storage V1 (Phonograph).](/docs/foundry/object-databases/object-storage-v1/)
### Link type with writeback
如果一个 link type 启用了 writeback，在对该 link type 进行编辑时应格外小心。对 link type 所做编辑的历史记录存储在 Object Storage V1 (Phonograph) 中。每次构建 writeback 数据集时，都会重新应用编辑历史记录，以获得 writeback 数据集中已编辑链接的最终状态。当 link type 的 backing datasource 从 Object Storage V1 (Phonograph) 注销时，Objects Storage V1 (Phonograph) 中的编辑历史记录将被删除，并且未来 writeback 数据集的构建将会失败。

If a link type has writeback enabled, extra precaution should be taken when making edits to that link type. The history of edits made to a link type are stored in Object Storage V1 (Phonograph). Every time a writeback dataset is built, the history of edits is reapplied to get the final state of edited links in the writeback dataset. When the backing datasource of a link type is unregistered from Object Storage V1 (Phonograph), the history of edits in Objects Storage V1 (Phonograph) is deleted and future builds of the writeback dataset will fail.
除了[上一节](#link-type-without-writeback)中列出的需要注销的更改之外，对于具有 writeback 的 link type，当对 link type 的 backing datasource 的**任何**列进行 schema 更改时，都需要注销，即使该 link type **曾经**接收过编辑但当前未接收编辑。Schema 更改包括对列的名称和 base type 的更改。

In addition to the changes that require unregistering that were listed in the [previous section](#link-type-without-writeback), unregistering is required for link types with writeback when schema changes are made to **any** column of a backing datasource to a link type that has **ever** received edits, even if does not currently receive edits. Schema changes include changes to the name and base type of the column.
> **⚠️ 警告: 警告**

> Object Storage V1 (Phonograph) **不会**自动注销 link type 的 backing datasource 以响应这些 schema 更改之一。相反，重建索引将会失败，并且只有在撤销已保存的 schema 更改，或者您在 link type 的 Datasources 页面的 Phonograph 面板中手动注销并重新注册 link type 的 backing datasource 后，才会成功。
> **⚠️ 警告: Warning**

> Object Storage V1 (Phonograph) will **not** automatically unregister the backing datasource of a link type in response to one of these schema changes. Instead, the reindex will fail and will only succeed if the saved schema changes are undone, or if you manually unregister and reregister the backing datasource of a link type in the Phonograph pane of the link type’s Datasources page.
当您尝试保存任何可能擦除编辑历史记录的更改时，系统会警告您其对编辑的潜在影响。

When you try to save any changes that risk erasing the edits history, you will be warned about the potential impact on edits.

> 📷 **[图片: 关于编辑影响的警告]**

> 📷 **[图片: Warning about impact on edits]**

现在您已经了解了编辑现有 link type 时的注意事项，您可以安全地进行更改了。

Now that you understand the considerations in editing existing link types, you can safely make your changes.
## Edit an existing link type
* [导航到现有的 link type](#navigate-to-an-existing-link-type)

* [删除 link type](#delete-a-link-type)

* [更改 backing datasource](#change-a-backing-datasource)

* [编辑 link type 的元数据](#edit-a-link-types-metadata)

* [Navigate to an existing link type](#navigate-to-an-existing-link-type)
* [Delete a link type](#delete-a-link-type)
* [Change a backing datasource](#change-a-backing-datasource)
* [Edit a link type’s metadata](#edit-a-link-types-metadata)
### Navigate to an existing link type
您可以随时通过从主页侧边栏中选择 link type 页面并从列表中选择其他 link type 来更改您正在处理的 link type。您也可以随时在应用程序顶部的搜索栏中搜索新的 link type。阅读更多关于[导航](/docs/foundry/ontology-manager/navigation/)的信息。

You can always change the link type you are working on by selecting the link type page from the home page sidebar and selecting a different link type from the list. You can also always search for a new link type in the search bar in the application header. Read more about [navigation](/docs/foundry/ontology-manager/navigation/).
### Delete a link type
您可以通过选择 link type 视图侧边栏右上角的 ![...](/docs/resources/foundry/object-link-types/three-dots.png)（三个点）图标（见下图），然后从下拉菜单中选择 **Delete** 选项来删除 link type。将弹出一个对话框以确认您要将该 link type 暂存以进行删除。

You can delete an object type by selecting the ![...](/docs/resources/foundry/object-link-types/three-dots.png) (three dots) icon at the top right of the link type view sidebar (see image below) and then selecting the **Delete** option from the dropdown. A dialog will pop up to confirm you want to stage the link type for deletion.
* 请注意，link type 的删除只有在您保存更改后才会生效，并且将中断任何引用该 link type 的视图或应用程序。

* 请注意，具有 `active` 状态的 link type 无法被删除。阅读更多关于[状态](/docs/foundry/object-link-types/metadata-statuses/)的信息。

* Note that the deletion of the link type only takes effect after you save your changes, and will break any views or applications referencing the object type.
* Note that link types with an `active` status cannot be deleted. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).

> 📷 **[图片: Delete link type]**

[PARA_1]
您可以更改 backing datasource:

[PARA_2]
1. 导航至 link type 视图的 **Datasources** 页面。

2. 选择现有 datasource 旁边的 ![pen](/docs/resources/foundry/object-link-types/pen.png) **Select** 图标。这将允许您在 Foundry 中浏览并选择可用的 datasource。

[PARA_3]
> **⚠️ 警告: Warning**

> 更改 link type 的 backing datasource 将移除旧 datasource 中列与定义 link type 的 key 之间的任何连接。**只有在**您更改为与旧 datasource **具有相同 schema** 的新 datasource 时,Key 才会自动重新映射。否则,您需要将 key 重新映射到新 datasource。

[PARA_4]

> 📷 **[图片: Edit link type metadata]**

[PARA_5]
1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

> 📷 **[图片: Delete link type]**

### Change a backing datasource
您可以更改 backing datasource:

[PARA_2]
1. 导航至 link type 视图的 **Datasources** 页面。

2. 选择现有 datasource 旁边的 ![pen](/docs/resources/foundry/object-link-types/pen.png) **Select** 图标。这将允许您在 Foundry 中浏览并选择可用的 datasource。

[PARA_3]
> **⚠️ 警告: Warning**

> 更改 link type 的 backing datasource 将移除旧 datasource 中列与定义 link type 的 key 之间的任何连接。**只有在**您更改为与旧 datasource **具有相同 schema** 的新 datasource 时,Key 才会自动重新映射。否则,您需要将 key 重新映射到新 datasource。

[PARA_4]

> 📷 **[图片: Edit link type metadata]**

[PARA_5]
1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

You can change a backing datasource:
1. 导航至 link type 视图的 **Datasources** 页面。

2. 选择现有 datasource 旁边的 ![pen](/docs/resources/foundry/object-link-types/pen.png) **Select** 图标。这将允许您在 Foundry 中浏览并选择可用的 datasource。

[PARA_3]
> **⚠️ 警告: Warning**

> 更改 link type 的 backing datasource 将移除旧 datasource 中列与定义 link type 的 key 之间的任何连接。**只有在**您更改为与旧 datasource **具有相同 schema** 的新 datasource 时,Key 才会自动重新映射。否则,您需要将 key 重新映射到新 datasource。

[PARA_4]

> 📷 **[图片: Edit link type metadata]**

[PARA_5]
1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

1. Navigate to the **Datasources** page of the link type view.
2. Select the ![pen](/docs/resources/foundry/object-link-types/pen.png) **Select** icon next to the existing datasource. This will allow you to browse and select available datasources in Foundry.
> **⚠️ 警告: Warning**

> 更改 link type 的 backing datasource 将移除旧 datasource 中列与定义 link type 的 key 之间的任何连接。**只有在**您更改为与旧 datasource **具有相同 schema** 的新 datasource 时,Key 才会自动重新映射。否则,您需要将 key 重新映射到新 datasource。

[PARA_4]

> 📷 **[图片: Edit link type metadata]**

[PARA_5]
1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。
> **⚠️ 警告: Warning**

> Changing the backing datasource of a link type will remove any connection between columns in the old datasource and the keys that define your link type. Keys will be automatically remapped for you **only if** you change to a new datasource with the **same schema** as the old datasource. Otherwise, you will need to remap the keys to the new datasource.
![Select backing datasource](/docs/resources/foundry/object-link-types/edit-link-type-change-backing-datasource-annotated.png)
### Edit a link type’s metadata

> 📷 **[图片: Edit link type metadata]**

[PARA_5]
1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

> 📷 **[图片: Edit link type metadata]**

1. **Status:** 在 link type 窗格顶部选择现有 status 以打开可用 status 的下拉列表。从 `deprecated`、`experimental` 和 `active` status 中进行选择。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

2. **Key:** 从下拉列表中选择以更改外键,或在多对多 link type 中更改列映射。

* 请注意,在具有多对多 cardinality 的 link type 中,backing datasource 中的列必须映射到 object type 的 primary key。如果 object type 的 primary key property 的类型与 link type 的 backing datasource 中映射到的列的类型不同,将出现错误,阻止您保存。

* 在具有任何其他 cardinality 的 link type 中,应用程序要求其中一个 object type 的 key 必须映射到该 object type 的 Primary key,以确保 Cardinality 的"one"端是唯一的。

3. **API name:** 选择进入现有 API name 以更改其值。

* 请注意,您无法更改具有 `active` status 的 link type 的 API name。

* 详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* 详细了解 [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names)。

4. **Visibility:** 从 link visibility 列表中检查可见性。`prominent` link type 将提示应用程序向用户优先显示此 link type。`hidden` link type 将不会出现在用户应用程序中。

5. **Type classes:** 应用 type classes 作为可由应用程序解释的附加元数据。

* 有关更多信息,请参阅 [available type classes 的列表](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_6]
在 Foundry Ontology 中,link type 由以下元数据表示:

[PARA_7]
* **ID:** link type 的唯一标识符,主要用于在配置应用程序时引用此类型的 link。例如,`employee-employer` 可能是定义在 `Employee` 和 `Company` Object Type 之间的 link type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Link type 的 RID 将在整个平台的错误消息中被引用。

* **Status:** 向用户和其他 Ontology 构建者发出的信号,表明 link type 在开发过程中的阶段。它可以是 `active`、`experimental` 或 `deprecated`。默认情况下,`Employee → Employer` link type 将具有 `experimental` 状态。详细了解 [statuses](/docs/foundry/object-link-types/metadata-statuses/)。

* **Object types:** 通过 link type 定义关联的 object type。例如,`Employee → Employer` link type 将引用 `Employee` 和 `Company` Object Type。

* **Cardinality:** 指示应用程序 link type 中的每个 object type 是具有一个还是多个 object。例如,在 link type `Employee → Employer` 中,Employee Object Type 的 cardinality 为 `many`,而 Company Object Type 的 cardinality 为 `one`,因为许多 employee 链接到单个 employer。如果一个 direct report 可以有多个 manager,并且一个 manager 可以有多个 direct report,则 link type `Direct Report ↔ Manager` 中的 Employee Object Type 将各自具有 cardinality `many`。

* **Key:** 用于创建 link 的 property 或 column。

* 在一对一或一对多 cardinality link type 中,一个 Object Type 的 property(外键)引用另一个 Object Type 的 primary key property。外键和 primary key 之间的这种引用定义了 Object 之间的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 可能具有引用 `Company` Object Type 的 `company ID` property(primary key)的 `employer ID` property(外键)。

* 在多对多 cardinality link type 中,包含 primary key 对的表定义了两个 Object 之间的 link。这些 link type 需要指定一个 join table,同时映射这些 key,这些 key 告诉应用程序 join table 中的哪些列引用 link type 中哪些 Object Type 的 primary key。例如,为 `Direct Report ↔ Manager` link type 提供支持的 join table 可能包含成对的 `employee numbers`,其中每对代表一个 `Direct Report ↔ Manager` link。

* **Display name:** 在用户应用程序中访问此类型的 link 时向任何人显示的名称。Link type 的每一侧都有一个 display name。Link type 的一侧表示 *到* 该 Object Type 的 link。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 display name 是 `Employee`,而 `Company` Object Type 的 display name 是 `Employer`。

* **Plural display name:** 在用户应用程序中访问此类型的 link 且具有多个链接 Object Type 时向任何人显示的名称。例如,在 `Employee → Employer` link type 中,`Employee` Object Type 的 plural display name 是 `Employees`,而 `Company` Object Type 没有 plural display name,因为每个 employee 只能有一家公司。

* **API name:** 在代码中以编程方式引用 link type 时使用的名称。Link type 一侧的 API name 可用于返回该类型的 Object。例如,如果 `Employee → Employer` link type 中 Employee 一侧的 API name 是 `employee`,则调用 `Company.employee.get()` 将返回链接到这些 `Company` Object 的 `Employee` Object。详细了解 [API names](/docs/foundry/functions/api-objects-links/)。

* **Visibility:** 向用户应用程序指示如何显著地显示 link type 的一侧(引用 *到* 该侧 Object Type 的 link)。Link type 的 `prominent` 侧将引导应用程序向用户优先显示 link type 的这一侧。Link type 的 `hidden` 侧将不会出现在用户应用程序中。默认情况下,link type 的 Employee 和 Company 侧的 visibility 将为 `normal`。

* **Type classes:** 由用户应用程序解释的附加元数据。详细了解 [type classes](/docs/foundry/object-link-types/metadata-typeclasses/)。

[PARA_8]
[详细了解在 Ontology 中创建和配置 link type,以及 link type 元数据的验证要求。](/docs/foundry/object-link-types/create-link-type/)

[PARA_9]
[详细了解 properties(Object Type 的特征)。](/docs/foundry/object-link-types/properties-overview/)

[PARA_10]
**Link type** 是两个 Object Type 之间关系的 schema 定义。**Link** 指的是同一 Ontology 中两个 Object 之间该关系的单个实例。

[PARA_11]
例如,在 Ontology Manager 中,您可以在 `Employee` Object Type 和 `Company` Object Type 之间创建一个 link type,定义 `Employee` 和 `Employer` 之间的关系。Link 指的是 `Employee → Employer` link type 的单个实例,例如概念上的 employee "Melissa Chang" 与她的 employer "Acme, Inc." 之间的关系。

[PARA_12]
类似地,在 Ontology Manager 中,您可以在 `Flight` Object Type 和 `Aircraft` Object Type 之间创建一个 link type,定义 `Scheduled Flight` 和 `Assigned Aircraft` 之间的关系。Link 指的是 `Scheduled Flight → Assigned Aircraft` link type 的单个实例,例如 "JFK → SFO 24-02-2021" 与其分配的 aircraft "Boeing 737-123" 之间的关系。

[PARA_13]
Link 也可以存在于同一类型的两个 Object 之间。Link type `Direct Report ↔ Manager` 可以在 `Employee` Object Type 与其自身之间定义。

1. **Status:** Select the existing status at the top of the link type pane to open a dropdown of available statuses. Select from the `deprecated`, `experimental`, and `active` statuses.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
2. **Key:** Select from the dropdowns to change foreign keys, or column mappings in a many-to-many link type.
* Note that in a link type with many-to many cardinality, the columns in the backing datasource must map to the primary keys of the object types. If the type of the primary key property of the object type is not the same as the type of the column it is being mapped to in the link type’s backing datasource, an error will prevent you from saving.
* In a link type with any other cardinality, the application requires that the key of one of the object types must map to the Primary key of that object type, ensuring that the “one” side of the Cardinality is unique.
3. **API name:** Select into the existing API name to change its value.
* Note that you cannot change the API name for link types with an `active` status.
* Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* Read more about [valid API names](/docs/foundry/object-link-types/create-object-type/#configure-api-names).
4. **Visibility:** Check the visibility from the link visibility list. A `prominent` link type will prompt applications to show this link type first to users. A `hidden` link type will not appear in user applications.
5. **Type classes:** Apply type classes as additional metadata that can be interpreted by applications.
* Consult the [list of available type classes](/docs/foundry/object-link-types/metadata-typeclasses/) for more information.