<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/view-usage/
---
# Ontology metrics
可以将 Ontology Manager 配置为显示 Object Type 和 Link Type 的使用指标。

The Ontology Manager can be configured to show usage metrics for object types and link types.
## Key terminology
* **Reads（读取次数）：** 当应用程序为指定的 Object Type 加载对象时，会记录一次读取。这可以包括在 Workshop 中的表格里显示对象、为给定的 Object Type 搜索返回所有对象、对 Object Type 的 Property 进行聚合等。请注意，一次读取代表来自 [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) 或 Object Set Service (OSS) 的一次加载请求。许多对象一次性被加载或聚合时，仅会记录为一次读取。还请注意，Ontology Manager 中发生的任何 Object Type 或 Link Type 使用情况均不包含在内。

* **Writes（写入次数）：** 当应用程序因 [Action](/docs/foundry/action-types/overview/)、[Function](/docs/foundry/functions/overview/)、Foundry Form、直接的 Object Explorer 编辑或 API 调用而对该类型的对象进行编辑时，会记录一次写入。请注意，一次写入代表发送到 [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) 的一次编辑请求。许多对象一次性被批量编辑时，仅会记录为一次写入。

* **Interactions（交互次数）：** 过去 30 天内对该类型对象的读取和写入总数。

* **Active users（活跃用户数）：** 在过去 30 天内触发读取和写入记录的唯一用户 ID 数量。

* **Reads:** A read is recorded when an application loads objects for a specified object type. This can include displaying objects in a table in Workshop, returning all objects from search for a given object type, aggregating a property on an object type, and so on. Note that one read represents one load request from [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/) or the Object Set Service (OSS). Many objects loaded or aggregated at once will only be recorded as a single read. Also note that any object type or link type usage happening in Ontology Manager is not included.
* **Writes:** A write is recorded when an application makes edits to objects of this type as the result of an [Action](/docs/foundry/action-types/overview/), [Function](/docs/foundry/functions/overview/), Foundry Form, direct Object Explorer edit, or API call. Note that one write represents one edit request sent to [Object Storage V1 (Phonograph)](/docs/foundry/object-databases/object-storage-v1/). Many objects edited in bulk at once will only be recorded as a single write.
* **Interactions:** The total number of reads and writes on objects of this type over the last 30 days.
* **Active users:** The number of unique user IDs that triggered the reads and writes recorded over the last 30 days.
## Viewing usage
在 Ontology Manager 中有两个地方可以查看 Object Type 和 Link Type 的使用情况：

There are two places in the Ontology Manager to view object type and link type usage:
* **Overview** 选项卡上的使用图表：过去 30 天使用情况的高级摘要，使 Ontology 用户能够快速了解对此资源进行重大更改的影响。

* A usage graph on the **Overview** tab: High-level summary of usage over the last 30 days, enabling Ontology users to quickly understand the implications of making a breaking change to this resource.
![Usage graph on the overview tab](/docs/resources/foundry/ontology-manager/oma-user-interface-overview-usage.png)
> **⚠️ 警告: Warning**

> 如果您在预期能看到使用统计信息的图表中看到 "No usage for the last 30 days"（过去 30 天无使用情况），则可能是尚未配置内部表。请联系您的 Palantir 代表以获取更多信息。
> **⚠️ 警告: Warning**

> If you see “No usage for the last 30 days” in the usage graph when you would expect to see usage statistics, then it’s possible that internal tables may not have been configured. Contact your Palantir representative for more information.
* 专用的 **Usage** 选项卡：资源的详细使用指标。用户可以查看过去 30 天内每个 Object Type 的使用者、使用时间以及所在的 Foundry 应用程序。此功能旨在通过更清晰地了解更改的影响，来帮助 Ontology 用户更安全地进行 Ontology 更改。也可以通过点击 **Overview** 选项卡中图表上的 **See more** 来访问 **Usage** 选项卡。

* A dedicated **Usage** tab: Detailed usage metrics for resources. Users can see, over the last 30 days, who has used each object type, when, and in which Foundry applications. The feature is intended to help Ontology users make Ontology changes more safely by providing a clearer understanding of a change's impact. The **Usage** tab can also be accessed by clicking **See more** on the usage graph in the **Overview** tab.
![Usage tab](/docs/resources/foundry/ontology-manager/oma-user-interface-usage-tab.png)
## Enabling Ontology usage
**Overview** 选项卡上的使用情况以及 **Usage** 选项卡中的详细使用指标，是通过 Control Panel 中的 **Ontology settings** 选项卡使用 **Ontology metrics** 切换开关来配置的。此切换开关只能由 Ontology 管理员启用或禁用，更改可能需要长达 60 分钟才能在 Ontology Manager 中生效。

Usage on the **Overview** tab and detailed usage metrics in the **Usage** tab are configured from the **Ontology settings** tab in Control Panel using the **Ontology metrics** toggle. This toggle can only be enabled or disabled by Ontology administrators and changes may take up to 60 minutes to take effect in Ontology Manager.
## Shared Ontology usage
如果您的组织与其他组织共享一个 Ontology，则所有已开启 Ontology metrics 的组织的用户都可以访问 **Usage** 选项卡。显示的使用指标仅包含有权访问该 Object Type 的用户以及来自已启用 Ontology metrics 的组织的用户的使用情况。有关更多信息，请参阅 [启用 Ontology 使用情况](#enabling-ontology-usage) 中概述的步骤。

If your organization shares an Ontology with another organization, then the **Usage** tab will be accessable by users of all organizations that have the Ontology metrics turned on. The usage metrics displayed only includes the usage from users who have access to the object type and those who are from organizations that have the Ontology metrics enabled. See the steps outlined in [Enabling Ontology usage](#enabling-ontology-usage) for more information.