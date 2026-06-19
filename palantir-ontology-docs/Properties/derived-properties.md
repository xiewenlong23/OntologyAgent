<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/derived-properties/
---
# Configure derived properties
> **ℹ️ 注意: Beta**

> Derived properties 目前处于 [beta](/docs/foundry/platform-overview/development-life-cycle/) 阶段，可能在您的注册中不可用。在积极开发过程中，功能可能会发生变化。
> **ℹ️ 注意: Beta**

> Derived properties are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.
## Overview
Derived properties 是指在运行时根据 linked objects 的值计算得出的 properties。Derived property 不直接存储数据，而是通过 link types 从连接的对象中提取信息，并可选择应用聚合操作，例如求平均值、计数或将值收集到列表中。

Derived properties are properties that are calculated at runtime based on values from linked objects. Instead of storing data directly, a derived property pulls information from objects connected through link types, optionally applying aggregations like averaging, counting, or collecting values into lists.
For example:
* `Department` object type 可以具有一个 derived property，用于表示 "Average employee salary"（员工平均薪资），该属性会从所有 linked `Employee` objects 的薪资值进行聚合。

* `Project` object type 可以具有一个 derived property，用于表示 "Lead engineer name"（首席工程师姓名），该属性从单个 linked `Engineer` object 中检索姓名。

* `Order` object type 可以具有一个 derived property，用于表示 "Product names"（产品名称），该属性将所有 linked `Product` objects 的产品名称收集到一个列表中。

* A `Department` object type could have a derived property for "Average employee salary" that aggregates salary values from all linked `Employee` objects.
* A `Project` object type could have a derived property for "Lead engineer name" that retrieves the name from a single linked `Engineer` object.
* An `Order` object type could have a derived property for "Product names" that collects all product names from linked `Product` objects into a list.
Derived properties 是 **read-only**（只读）的，无法通过 functions 或 actions 进行编辑。这些 properties 使用计算中涉及的所有 objects 的 security context，确保用户只能查看他们有权访问的信息。

Derived properties are **read-only** and cannot be edited by functions or actions. These properties use the security context of all objects involved in the calculation, ensuring users only see information for which they have access authorization.
## Configure a derived property
要在 object type 上配置 derived property，请按照以下步骤操作。

To configure a derived property on an object type, follow the steps below.
### 1. Open the property configuration panel
从 Object Type 的 **Properties** 选项卡中，选择 **New property** 或点击现有 property 进行编辑。这将打开 property 配置侧边面板。

From the **Properties** tab of your object type, select **New property** or click on an existing property to edit it. This opens the property configuration side panel.

> 📷 **[图片: Property source tab with derived properties option.]**

> 📷 **[图片: Property source tab with derived properties option.]**

### 2. Navigate to the Source tab
在 property 配置侧边面板中，选择 **Source** 选项卡以配置 property 的值来源。

In the property configuration side panel, select the **Source** tab to configure where the property gets its values.
### 3. Select the Linked objects source type
在 **Source type** 部分，选择 **Linked objects** 选项。这将启用 derived property 配置。

In the **Source type** section, choose the **Linked objects** option. This enables derived property configuration.
### 4. Select a link type
在 **Linked objects** 部分，从下拉菜单中选择一个 link type。这将决定该 property 将从哪些 object 派生值。

In the **Linked objects** section, select a link type from the dropdown. This determines which objects the property will derive values from.
* 下拉菜单显示来自当前 Object Type 的所有可用 link type。

* 选择一个 link type 后，您可以选择性地添加其他 link type，以遍历多层连接（最多 3 层）。

* 使用 **Add linked object** 可通过另一层 linked object 进行遍历。

* The dropdown menu shows all available link types from your current object type.
* After selecting a link type, you can optionally add additional link types to traverse multiple levels of connections (up to 3 levels).
* Use **Add linked object** to traverse through another level of linked objects.

> 📷 **[图片: Selecting a link type for the derived property.]**

> 📷 **[图片: Selecting a link type for the derived property.]**

### 5. Configure aggregation (if needed)
如果您的链接链中存在具有"many"基数（一个 object 链接到多个 object）的 link，则必须选择 **Aggregation** 来合并这些值：

If any link in your chain has a "many" cardinality (one object linking to multiple objects), you must select an **Aggregation** to combine the values:
可用的聚合方式：

Available aggregations:
* **Count：** 统计 linked object 的数量。

* **Average：** 计算数值字段的平均值。

* **Sum：** 计算数值字段的总和。

* **Minimum：** 选择最小值。

* **Maximum：** 选择最大值。

* **Approximate cardinality：** 估计唯一值的数量。

* **Exact cardinality：** 精确统计唯一值的数量。

* **Collect list：** 将所有值收集到一个有序列表中（保留重复值）。

* **Collect set：** 将所有唯一值收集到一个无序集合中。

* **Count:** Count the number of linked objects.
* **Average:** Calculate the average of numeric values.
* **Sum:** Calculate the sum of numeric values.
* **Minimum:** Select the minimum value.
* **Maximum:** Select the maximum value.
* **Approximate cardinality:** Estimate the number of unique values.
* **Exact cardinality:** Count the exact number of unique values.
* **Collect list:** Collect all values into an ordered list (preserves duplicates).
* **Collect set:** Collect all unique values into an unordered set.
### 6. Select the property to derive
选择 link type（以及必要的 aggregation）后，从 linked object type 中选择您要派生的 property：

After selecting a link type (and aggregation if needed), choose which property from the linked object type you want to derive:
* 下拉菜单显示来自链接链中最终 Object Type 的所有可用 property。

* 对于 **Count** 聚合，您无需选择 property，因为 object 将被自动计数。

* The dropdown menu shows all available properties from the final object type in your link chain.
* For **Count** aggregation, you do not need to select a property as objects are automatically counted.

> 📷 **[图片: Selecting an aggregation type for the derived property.]**

> 📷 **[图片: Selecting an aggregation type for the derived property.]**

### 7. Configure collection limit (for collect aggregations)
如果您选择了 **Collect list** 或 **Collect set** 作为聚合方式，您可以选择性地设置收集项数量的上限。默认上限为 10 个。

If you selected **Collect list** or **Collect set** as your aggregation, you can optionally set a limit on the number of items collected. The default limit is 10 items.
## Multi-hop derived properties
Derived property 支持遍历最多 **3 层** linked object。这允许您从与起始 Object Type 间接连接的 object 派生 property。

Derived properties support traversing up to **3 levels** of linked objects. This allows you to derive properties from objects that are indirectly connected to your starting object type.
For example:
* 一个 `Department` Object Type 可以通过遍历 `Employee` 对象到其关联的 `Project` 对象来派生"项目名称"。

* 关联链为：Department → Employee → Project

* A `Department` object type could derive "Project names" by traversing through `Employee` objects to their linked `Project` objects.
* The link chain would be: Department → Employee → Project

> 📷 **[图片: Configure multi hop derived property.]**

> 📷 **[图片: Configure multi hop derived property.]**

配置多跳（multi-hop）：

To configure multi-hop:
1. 选择您的第一个 link type。

2. 选择 **Add linked object** 添加另一层级。

3. 从新连接的对象类型中选择下一个 link type。
4. 重复以上步骤，最多可配置 3 个层级。

1. Select your first link type.
2. Select **Add linked object** to add another level.
3. Select the next link type from the newly-connected object type.
4. Repeat up to 3 levels total.
### Known limitations
* **OSv1 支持：** 包含派生 property 的 query 不能包含任何使用 [OSv1](/docs/foundry/object-backend/osv1-osv2-migration/) 索引的 Object Type。

* **文本搜索：** 派生 property 不能用于文本搜索或关键字筛选。

* **OSDK 中的 Struct：** 在当前版本的 TypeScript OSDK 中，包含派生 property 的 query 不能包含任何 [struct](/docs/foundry/object-link-types/structs-overview/) property type。您可以使用 `$select` 操作来排除 struct property。

* **Inline actions：** 配置了 inline actions 的 property 不能转换为派生 property。

* **值类型：** 具有值类型的 property 不能转换为派生 property。

* **必填 property：** 派生 property 不能被标记为必填（不可为空）。

* **Property type 约束：** 派生 property 不能具有 property type 约束。

* **显示格式：** 派生 property 不能具有 rule set bindings 或 base formatters。

* **主键：** 主键 property 不能是派生 property。

* **Ontology 条件：** Default ontology 不支持派生 property。

* **OSv1 support:** Queries with derived properties may not contain any object types indexed using [OSv1](/docs/foundry/object-backend/osv1-osv2-migration/).
* **Text search:** Derived properties cannot be used in text search or keyword filters.
* **Structs in OSDK:** In current versions of the TypeScript OSDK, queries with derived properties may not contain any [struct](/docs/foundry/object-link-types/structs-overview/) property types. You can use a `$select` operation to exclude struct properties.
* **Inline actions:** Properties with inline actions configured cannot be converted to derived properties.
* **Value types:** Properties with value types cannot be converted to derived properties.
* **Required properties:** Derived properties cannot be marked as required (non-nullable).
* **Property type constraints:** Derived properties cannot have property type constraints.
* **Display formatting:** Derived properties cannot have rule set bindings or base formatters.
* **Primary keys:** Primary key properties cannot be derived properties.
* **Ontology condition:** Derived properties are not supported for the Default ontology.