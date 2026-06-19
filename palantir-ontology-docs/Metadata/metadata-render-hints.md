<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/metadata-render-hints/
---
# Render hints
Foundry 使用 **render hints** 来向 [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) 以及平台中的用户应用程序传达 Ontology [properties](/docs/foundry/object-link-types/properties-overview/) 的使用信息。例如，字符串 property 上的 `sortable` render hint 会告知应用程序允许用户对该 property 进行排序，例如在时间线或图表中。

Foundry uses **render hints** to communicate information about the use of Ontology [properties](/docs/foundry/object-link-types/properties-overview/) to [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) and user applications in the platform. For example, the `sortable` render hint on a string property tells applications to allow users to sort on that property, as in a timeline or a chart.
许多 render hints 与 object type 的 reindex 性能相关。例如，您可以使用 render hints 告知 [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) 某个 property 不需要在应用程序中进行聚合或排序，从而使 Object Storage V1 在索引这些 property 时减少工作量。

Many render hints are tied to reindex performance for an object type. For instance, you can use render hints to indicate to [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) that a property does not need to be aggregated or sorted in applications, so that Object Storage V1 has less work to do when indexing those properties.
您可以在 property 编辑器的 properties 窗格中选中或取消选中 render hints（见下图）。

You can select and deselect render hints in the properties pane of the property editor (see image below).
![Render hints](/docs/resources/foundry/object-link-types/render-hints.png)
下表列出了每个可用 render hint 的 **Name** 和 **Description**。该表还提供了 render hints 在两个技术方面的信息："Adds raw index?" 和 "Requires reindex?"（将在下文说明）。

The following table shares the **Name** and **Description** for each of the available render hints. The table also provides information on two technical aspects of render hints: "Adds raw index?" and "Requires reindex?" (described below).
* **Adds raw index?**
* 为了应用添加 raw index 的 render hint，Object Storage V1 (Phonograph) 通过在存储 backing dataset 时创建另一个索引来存储 render hint 信息。

* 由于这个额外的索引，对于应用了 render hint 的 property，将有两列计入 Object Storage V1 (Phonograph) 索引的列总数中。

* 这就是为什么取消选中这些 render hints 可以提升 reindex 到 Object Storage V1 (Phonograph) 的性能。

* **Requires reindex?**
* 某些 render hints 一旦在 Ontology Manager 中保存其选择，就会立即在用户应用程序中生效。

* 对于其他需要 reindex 的 render hints，必须将 object type 的 backing datasources reindex 到 Object Storage V1 (Phonograph) 之后，更改才会反映在用户应用程序中。

* 您可以等待下一次触发的 reindex，也可以通过导航到 object type 的 **Datasources** 选项卡并在 **Phonograph** 窗格中选择蓝色的 **Reindex** 按钮来手动启动 reindex。

* **Adds raw index?**
* In order to apply a render hint that adds a raw index, Object Storage V1 (Phonograph) stores the render hint information by creating another index when storing the backing dataset.
* Because of this additional index, for the property with a render hint applied, two columns will be counted toward the total number of columns indexed into Object Storage V1 (Phonograph).
* This explains why deselecting these render hints improves performance of reindex into Object Storage V1 (Phonograph).
* **Requires reindex?**
* Some render hints will be immediately applied in user applications as soon as their selection is saved in the Ontology Manager.
* For other render hints that require a reindex, the object type's backing datasources must be reindexed into Objects Storage V1 (Phonograph) before the changes will be reflected in user applications.
* You can wait for the next triggered reindex or you can manually start the reindex by navigating to the **Datasources** tab of the object type and selecting the blue **Reindex** button in the **Phonograph** pane.
|Name   |Description    |Adds raw index?    |Requires reindex?  |
|---    |---    |---    |---    |
|Disable formatting |- **Enable** if property values should not be formatted in Object Views according to a browser location’s local numerical formatting standards.   |   |   |
|Identifier |- **Enable** to improve reindex performance and specify primary keys and foreign keys that have a numerical base type and don’t need to be formatted or treated as numbers.

    - For example, Object Views won’t format the property values as numbers and Object Explorer won’t enable filtering the keys by a range.    |   |   |
|Keywords   |- **Enable** to highlight this property in its own section when displaying properties in Object Views.     |   |   |
|Long text  |- **Enable** if property values contains a large amount of text.

    - For example, Object Views will display this property’s values in a more readable format.    |   |   |
|Low cardinality    |- **Enable** to indicate to applications that there are not many possible values for this property.

    - For example, some Object View widgets will only allow filtering on properties with not many possible values.

- The Searchable render hint **must also be selected** along with Low cardinality.     |yes    |yes    |
|Selectable |- **Enable** on string properties to allow users to perform aggregations on this property.

    - For example, this property will be aggregated in Object Explorer histograms and Object View charts.

- **Enable** on numeric and date properties to allow users to perform aggregation on exact term values and not only distributions.

- **Disable** to improve reindex performance if the property will not be aggregated in applications.

- **Enable** to use the Exact Match filter capability.

- The Searchable render hint **must also be selected** along with Selectable.     |yes    |yes    |
|Sortable   |- **Enable** on string properties to allow users to sort on this property.

    - Numeric and date properties are always sortable.

    - For example, timelines and charts in Object Views will be sorted on this property.

- **Disable** to improve reindex performance if the property will not be sorted on in applications.

- **Not recommended for arrays**, which will sort based on the minimum value in the array.

- The Searchable render hint **must also be selected** along with Sortable.     |yes    |yes    |
|Searchable |- **Disable** to improve reindex performance if the property will not be searched or sorted on in applications.

    - The performance improvements will be especially significant if the property contains large strings.

- Searchable **must be selected** in order for applications to apply the Selectable, Sortable, or Low cardinality render hints.     |yes    |yes    |
|Enable leading wildcards   |- **Enable** on string properties to support leading wildcard queries.

- The Searchable render hint **must also be selected** along with Enable leading wildcards.     |yes    |yes    |
|Enable regex queries   |- **Enable** on string properties to support regex queries.

- The Searchable render hint **must also be selected** along with Enable regex queries.     |yes    |yes    |