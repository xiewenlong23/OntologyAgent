<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/volume-usage/
---
# Ontology volume usage
Foundry 的 Ontology 是一个快速访问的存储层，允许您将对象定义绑定到交互式数据，以用于查询、links、scenarios 和 actions。Foundry Ontology 中的数据经过索引，可实现快速访问以及多个并发编辑者的安全编辑。Ontology volume 是索引对象集及其彼此之间 links 的总大小的度量。Ontology volume 是一个平均指标，对于瞬时读数，其单位为 GB；但在一个月内进行测量时，其单位为 GB-Month。

Foundry’s Ontology is a fast-access storage layer that allows you to bind object definitions to interactive data for queries, links, scenarios, and actions. Data in the Foundry Ontology is indexed for fast access and for safe edits by multiple simultaneous editors. Ontology volume is a measure of the total size of the indexed object sets and their links with each other. Ontology volume is an average metric that has the unit of GB for an instantaneous reading, but has the unit of GB-Month when measuring over the course of one month.
## Measuring Ontology volume
Ontology volume 通过测量支撑 object type 的索引大小来记录。每个 object type 都有一定数量的对象以及每个对象的 properties 数量。每个 property 的大小可以是任意的。索引的总大小通过对该 object type 的每个对象的每个索引 property 的大小求和来计算。

Ontology volume is recorded by measuring the size of the indexes that back the object type. Each object type has a number of objects and a number of properties per object. Each property can be of arbitrary size. The total size of the index is calculated by summing the size of each indexed property for every object of that object type.
> **ℹ️ 注意**

> 需要注意的是，Ontology volume 可能大于 dataset volume，因为 Ontology 数据无法压缩，并且 Ontology 索引需要额外的存储以支持更快的查询。
> **ℹ️ 注意**

> It’s important to note that Ontology volume can be larger than dataset volume because Ontology data cannot be compressed, and Ontology indexing requires additional storage to facilitate faster queries.
Foundry 平台每小时记录一次每个对象的 Ontology volume 测量值。在测量一段时间内的 Ontology volume 时，所有每小时测量值会在给定时间段内取平均值。在一个日历月内取平均值会产生 *GB-Month* 单位。

Every hour, the Foundry platform records a measurement of Ontology volume per object. When measuring Ontology volume over time, all hourly measurements are averaged over the given time period. Averaging over the course of one calendar month produces the *GB-Month* unit.
## Investigating Ontology volume usage
对象在 Ontology Manager 中进行管理，Ontology Manager 是所有对象管理和监控的中心。Ontology Manager 允许用户配置哪些 datasets 应成为对象、这些对象附加了哪些类型的 properties，以及在 object type 之间定义了哪些 link sets。

Objects are managed in the Ontology Manager, the hub for all administration and monitoring of objects. The Ontology Manager allows users to configure which datasets should become objects, what types of properties are attached to these objects, and which link sets are defined between object types.
对象及其相应 link type 的总 Ontology volume 列在 Resource Management Application 中。

The total Ontology volume for objects and their corresponding link types are listed in the Resource Management Application.
## Factors that drive Ontology volume
Ontology volume 实际上是对 Ontology 中所有 Object（包括其 Properties 和 Links）大小的度量。以下两个因素是总体 volume 的主要驱动因素。

Ontology volume is effectively a measure of the size of all objects in the ontology, including their properties and links. The following two factors are the main drivers of total volume.
* **每个 Object Type 中 Object 的数量和大小**

* 当从 dataset 创建 Ontology Object Type 时，dataset 的每一行都会对应一个被索引的 Object。因此，该 dataset 的行数与相应 Object Type 中 Object 的数量是 1:1 对应的。

* 此外，拥有更多列或包含更多数据（例如自由文本字段）的 dataset 会产生更大的单个 Object，因为每一列都会被转换为一个 Property。

* **使用 join table 时 Object 之间的 Link 数量**

* 在多对多关系中，Ontology 需要定义一个 join table 来基于主键定义 Object 之间的所有 Links。这些表会与 Object 一起在 Ontology 中被索引，并占用 Ontology volume。

* 通常情况下，look-up table 的大小随每条记录保持恒定，并随所定义 Link 数量的增长而线性增长。

* **The number and size of objects per object type**
* When creating an ontology object type out of a dataset, an object will be indexed per row of that dataset. Therefore, the number of rows in that dataset is tied 1:1 to the number of objects in the corresponding object type.
* Additionally, datasets that have more columns or that contain more data (e.g. free text fields) can produce individual objects that are larger, because each column is turned into a property.
* **The number of links between objects when using join tables**
* In many-to-many relationships, the Ontology requires the definition of a join table to define all of the links between objects based on their primary keys. These tables are indexed alongside the objects in the Ontology and use ontology volume.
* In general, look-up tables have a constant size per record and grow linearly in volume with the number of links that are defined.
## Managing Ontology volume
Ontology 旨在作为一个用于操作使用和查询的高速访问后端。在一般情况下，Ontology 最适合与从更大数据资产中合成的、经过高度精炼的数据一起使用。因此，Ontology 的 volume 应小于 Foundry transformation framework 中原始数据和中间数据的总体大小。

The Ontology is designed to be a fast-access backend for operational usage and querying. In the general case, the Ontology is best used with highly refined data that is synthesized from a larger data asset. The volume of the Ontology should therefore be smaller than the total raw and intermediate data size in Foundry’s transformation framework.
要管理 Ontology volume 的使用，请关注 Ontology 中定义的 Object Type 数量、每个 Object Type 中的 Object 数量以及每个 Object 的 Property 数量。总体而言，管理 Ontology volume 使用量的最佳方式是理解并有意识地管理 Object 数量、Property 数量以及 Property 大小。

To manage Ontology volume usage, pay attention to the number of object types that are defined in the Ontology, as well as the number of objects per object type and the number of properties per object. Overall, the best way to manage Ontology volume usage is to understand and deliberately manage object numbers, property counts, and property sizes.