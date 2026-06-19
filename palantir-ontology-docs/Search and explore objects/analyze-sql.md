<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/analyze-sql/
---
# Analyze objects using SQL \[Beta]
> **ℹ️ 注意: Beta**

> Ontology SQL 支持处于 [beta](/docs/foundry/platform-overview/development-life-cycle/) 阶段，可能在您的 enrollment 上不可用。在积极开发期间，功能可能会发生变化。请联系 Palantir Support 以请求启用 Ontology SQL。
> **ℹ️ 注意: Beta**

> Ontology SQL support is in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development. Contact Palantir Support to request enabling Ontology SQL.
使用 **Analyze using SQL** 功能可快速查看 object type 的分析结果。该功能包含一个 SQL "scratchpad"，您可以在其中运行只读 SQL 查询。与 [Dataset Preview](/docs/foundry/sql-warehousing/sql-console/) 类似，它支持以下功能：

Use the **Analyze using SQL** feature to view a quick analysis of object types. This feature consists of a SQL "scratchpad", where you can run read-only SQL queries. Similarly to [Dataset Preview](/docs/foundry/sql-warehousing/sql-console/), it supports the following features:
* Object type RID 的自动补全

* 在反引号（ \` ）内搜索其他 object type 以执行高效的 `JOIN` 查询
* 使用编辑器友好的功能，例如键盘快捷键来运行高亮显示的查询

* 输出执行 SQL 查询结果的预览表
* 调整列和底部面板的大小以适应您的偏好

* Autofill for object type RIDs
* Search for other object types within backticks ( \` ) to perform efficient `JOIN` queries
* Use editor-friendly features such as keyboard shortcuts to run highlighted queries
* Output a preview table for results of the executed SQL query
* Resize columns and the bottom panel to fit your preferences
按照以下步骤使用 Analyze using SQL：

Follow the steps below to use analyze using SQL:
1. 打开一个 exploration。

2. 在右上角菜单中选择 **Analyze using SQL**，以打开可调整的预览面板。

3. 在 **Code** 选项卡中,对数据集编写一个只读查询。

1. Open an exploration.
2. Select **Analyze using SQL** in the top right menu to open the adjustable preview panel.
3. In the **Code** tab, write a read-only query on the dataset.
![Example usage of the "Analyze using SQL" feature.](/docs/resources/foundry/object-explorer/analyze-sql-example.png)
您可以在查询中通过输入其名称来搜索任何 object type。将出现一个自动完成窗口,允许您快速选择并自动填充 object type 的完整 RID。

You can search for any object type in your query by typing its name. An autocomplete window will appear, allowing you to quickly select and autofill the full RID of the object type.
![An example of object RID autofilling](/docs/resources/foundry/object-explorer/object-rid-autofill.png)
或者,您可以使用 object type 的 API 名称,语法如下:

Alternatively, you can use the object type's API name with the following syntax:
```sql
`ontologyApiName`.`objectTypeApiName`
```
![An example of object API name querying.](/docs/resources/foundry/object-explorer/object-api-name-query.png)
要查询多对多 link type,您可以使用用反引号(`` `RID` ``)括起来的 link type 的 RID。

To query a many-to-many link type, you can use the link type's RID enclosed by backticks (`` `RID` ``).
## Requirements
Analyze using SQL 的工作原理是查询 Ontology 实体的 backing datasource 或 materialization。请注意以下要求:

Analyze using SQL works by querying the backing datasource or the materialization of an Ontology entity. Note the following requirements:
* 禁用编辑的 Ontology 实体必须具有单一 datasource。

* 启用了编辑、仅编辑 property 或具有多个 datasource 的实体需要 materialization。

* Ontology entities with edits disabled must have a singular datasource.
* Entities with edits enabled, edit-only properties, or multiple datasources require a materialization.
如果您尝试查询不满足这些要求的 Ontology 输入,代码编辑器将显示警告。

The code editor will display a warning if you attempt to query Ontology inputs that do not meet these requirements.
![A sample code editor warning stating that the object type needs materialization.](/docs/resources/foundry/object-explorer/object-needs-materialization-warning.png)
> **ℹ️ 注意**

> 查询不能在同一个查询中混合使用表格来源(例如 datasets、tables 或 restricted views)和 Ontology 输入。
> **ℹ️ 注意**

> Queries cannot mix tabular sources (such as datasets, tables, or restricted views) and Ontology inputs within the same query.
## Data freshness
对于启用了编辑的对象,Analyze using SQL 将查询该实体的 materialization。这意味着最近的更改(例如对对象执行的编辑或 actions)可能需要长达 30 秒才能出现在查询结果中。代码编辑器会在输出表上方显示有关此数据新鲜度窗口的提醒。

For objects with edits enabled, analyze using SQL will query the entity’s materialization. This means that recent changes such as edits or actions performed on objects may take up to 30 seconds to appear in the query results. The code editor displays a reminder about this data freshness window above the output table.
## Compatibility
SQL 引擎支持 **Spark SQL** 方言。在 Spark SQL 中,table name 等标识符应使用反引号(`)而不是单引号或双引号进行引用。

The SQL engine supports the **Spark SQL** dialect. In Spark SQL, identifiers such as table names should be quoted using backticks ( \` ) rather than single or double quotes.
下面的示例演示了此语法:

The example below demonstrates this syntax:
```sql
SELECT column_name FROM \`ri.ontology.main.object-type...\`;
```
有关 Spark SQL 方言及其语法的更多信息,请参阅 [official Spark SQL documentation ↗](https://spark.apache.org/docs/latest/sql-ref.html)。

For more information on the Spark SQL dialect and its syntax, refer to the [official Spark SQL documentation ↗](https://spark.apache.org/docs/latest/sql-ref.html).
## Query execution details and limitations
1. 每个查询在整个数据集上运行,并使用与 [Contour](/docs/foundry/contour/overview/) 相同的 compute backend。
2. 每个查询将返回最多 1,000 行的样本。

3. SQL 控制台的使用量将在 [resource management](/docs/foundry/resource-management/overview/) 中的 dataset 级别进行归因,归属于标记为 **Contour** 的 source 下。

1. Each query runs on the entire dataset and uses the same compute backend as [Contour](/docs/foundry/contour/overview/).
2. Each query will return a maximum sample of 1,000 rows.
3. Usage for SQL console will be attributed at the dataset level in [resource management](/docs/foundry/resource-management/overview/), under the source labeled **Contour**.