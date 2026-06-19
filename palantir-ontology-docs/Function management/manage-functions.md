<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/manage-functions/
---
# Manage published functions
发布后，可以使用 **Ontology Manager** 查看和管理所有类型的 functions。

Once published, all types of functions can be viewed and managed using the **Ontology Manager**.
## Searching for functions
要搜索 functions，请导航至 **Ontology Manager** 并选择 **Functions** 选项卡。

您可以按 function 的大多数元数据进行搜索，包括但不限于 function 名称、描述、API 名称和 RID。

To search for functions, navigate to the **Ontology Manager** and select the **Functions** tab.
You can search for functions by most metadata on the function, including but not limited to the function name, description, API name and RID.
![Search for functions in Ontology Manager](/docs/resources/foundry/functions/functions-search.png)
## Function overview page
在 Ontology Manager 中选择一个 function 后，您可以查看有关该 function 的基本信息，包括其输入和输出以及该 function 的任何相关使用历史记录。

After selecting a function in the Ontology Manager, you can view basic information about the function, including its inputs and outputs and any associated usage history for the function.
![View function overview in Ontology Manager](/docs/resources/foundry/functions/function-overview.png)
## Function configuration page
某些类型的 functions 允许您配置资源，例如 timeout 或 memory limits。

如果您的 function 支持任何配置选项，您可以在 **Configuration** 选项卡中查看和编辑它们。

如果此选项卡不存在，则表示该 function 不支持任何配置选项。

Some types of functions allow you to configure resources such as timeouts or memory limits.
If your function supports any configuration options, you can view and edit them in the **Configuration** tab.
If this tab is not present, the function does not support any configuration options.
> **ℹ️ 注意**

> Configuration overrides 是按每个 function version 应用的。根据您发布 function 的应用程序，新版本可能具有默认配置，您可能需要重新应用任何 configuration overrides。
> **ℹ️ 注意**

> Configuration overrides are applied on a per-function version basis. Depending on the application from which you publish your function, new versions may have the default configuration and you may need to reapply any configuration overrides.
例如，您可以按照下图所示配置 TypeScript function 的 timeout。

For example, you can configure the timeout on a TypeScript function as seen in the following image.
![Manage function runtime configurations in Ontology Manager](/docs/resources/foundry/functions/function-configuration.png)
### Configuration inheritance
Functions 在发布新版本时提供开箱即用的 configuration overrides 继承支持。配置根据 semantic version 规范从先前的稳定版本继承。如果发布的是非稳定版本，配置将从先前版本继承，无论其是否为稳定版本。

Functions provide out-of-the-box support for inheriting configuration overrides when publishing new versions. The configuration is inherited from the prior stable version according to the semantic version specification. If publishing a non-stable version, configurations will be inherited from the prior version, regardless of whether it is a stable release.
配置继承要求您的代码仓库包含更新的模板配置。您可以检查隐藏的 `templateConfiguration.json` 文件以确认您的代码仓库所基于的版本。

Configuration inheritance requires your repository to contain updated template configurations. You can check the hidden `templateConfiguration.json` file to confirm the version your repository is on.
* 对于 TypeScript v1 functions 代码仓库，您必须具有 `parentTemplateVersion >= 3.512.0`

* 对于 Python functions 代码仓库，您必须具有 `parentTemplateVersion >= 0.423.0`

* For TypeScript v1 functions repositories, you must have `parentTemplateVersion >= 3.512.0`
* For Python functions repositories, you must have `parentTemplateVersion >= 0.423.0`
## Consistent snapshots
Function-backed actions 在单次运行中的所有 read 请求自动使用一个 ontology snapshot。

Function-backed actions automatically use one ontology snapshot for all read requests in a single run.
一致的 snapshots 提供以下特性：

Consistent snapshots provide the following qualities:
* **数据一致性（Data consistency）：** 没有 snapshots 时，如果底层数据在请求之间发生变化，function 内的顺序 ontology 查询可能会返回不同版本的数据。使用 snapshots 时，您的 function 在 ontology 的一致视图上运行，类似于数据库事务中的 snapshot isolation。

* **性能提升（Improved performance）：** 在所有 ontology 请求中重用单个 snapshot 可显著提高 ontology read 性能。单个 function-backed action 及其中的任何查询都将获得此优势。

* **Data consistency:** Without snapshots, sequential ontology queries within a function could return different versions of data if the underlying data changed between requests. With snapshots, your function operates on a consistent view of the ontology, similar to snapshot isolation in a database transaction.
* **Improved performance:** Reusing a single snapshot across all ontology requests significantly improves ontology read performance. A single function-backed action, along with any queries within, receives this benefit.
### Snapshot configuration
如果您需要为高级用例显式管理 snapshots，可以使用以下选项在 [function configuration page](#function-configuration-page) 上配置 snapshot 行为：

If you need to explicitly manage snapshots for advanced use cases, you can configure the snapshot behavior on the [function configuration page](#function-configuration-page) using the following options:
* **Default (recommended)（默认（推荐））：** 除非遇到与 snapshot 相关的错误，否则请保持选中此选项。

* **Disable snapshots（禁用 snapshots）：** 当您需要在单次运行中的每次查询都获取最新数据时使用，或者当您因长时间运行的工作负载而遇到 snapshot 错误时使用。

* **Enable snapshots（启用 snapshots）：** 当您需要在所有 reads 中获得一致的时间点视图并希望获得更好的 read 性能，且您的 function 可以容忍数据在运行中途不更新时使用。对于大多数用例，不推荐使用此选项。

* **Default (recommended):** Leave this option selected unless you encounter snapshot-related errors.
* **Disable snapshots:** Use when you need the freshest data on each query during a run, or when you are hitting snapshot errors due to long-running workloads.
* **Enable snapshots:** Use when you need a consistent point-in-time view across all reads and want better read performance, and your function can tolerate data not updating mid-run. This is not recommended for most use cases.
> **⚠️ 警告**

> 默认情况下，带有 sources 的 function 针对实时数据运行，不使用快照。不建议强制使用快照，因为 functions 可以执行写入操作或调用外部系统。
> **⚠️ 警告**

> By default, functions with sources run against live data without snapshots. Enforcing snapshots is not recommended since functions can perform writes or invoke external systems.
## Enforced limits
设置了若干限制，以防止 functions 在执行时消耗过多资源。

Several limits are in place to prevent functions from consuming too many resources when they are executed.
### Time limit
Functions 默认的运行耗时限制为 **60 秒**。这些限制可以在 [function configuration page](#function-configuration-page) 上进行修改。

Functions are limited to **60 seconds** of elapsed run time by default. These limits can be modified on the [function configuration page](#function-configuration-page).
Functions 在 live preview 中运行时，即使在 function configuration page 上进行了修改，也允许运行最长 **280 秒**。

Functions are allowed to run for up to **280 seconds** when running in live preview, even if modified on the function configuration page.
> **⚠️ 警告**

> TypeScript v1 functions 还受到 **30 秒** 的 CPU 时间限制，且该限制不可配置。当 function 超过此阈值时，原因通常是数据加载逻辑效率低下。请参阅 [optimizing performance](/docs/foundry/functions/optimize-performance/) 部分，获取有关如何避免 CPU 超时的提示。
> **⚠️ 警告**

> TypeScript v1 functions are additionally limited to **30 seconds** of CPU time, which is not configurable. When a function exceeds this threshold, the cause is often inefficient data loading logic. Refer to the section on [optimizing performance](/docs/foundry/functions/optimize-performance/) for tips on how to avoid CPU timeouts.
### Memory limit
TypeScript v1、TypeScript v2 和 Python functions 之间的内存限制有所不同。

Memory limits differ between TypeScript v1, TypeScript v2, and Python functions.
#### TypeScript v1
Function 执行时的内存使用限制为 **128 Megabytes**。该限制很少被触及；在达到内存限制之前，functions 通常会先遇到时间限制或 object 加载限制。

Function execution is limited to **128 Megabytes** of memory usage. This limit is rarely reached; often, functions run into time limits or object loading limits before memory limits.
#### Deployed Python functions
已部署的 Python functions 默认内存使用为 **2 Gigabytes**。目前，已部署的 Python functions 无法在 function configuration page 上配置内存使用。

Deployed Python functions have **2 Gigabytes** of memory usage by default. Currently, deployed Python functions cannot configure memory usage on the function configuration page.
#### Serverless Python and TypeScript v2 functions
Serverless functions 默认内存使用为 **1024 Mebibytes**。可以在 [function configuration page](#function-configuration-page) 上将其配置为 **512 Mebibytes** 至 **5120 Mebibytes** 之间。

Serverless functions have **1024 Mebibytes** of memory usage by default. This can be configured from **512 Mebibytes** to **5120 Mebibytes** on the [function configuration page](#function-configuration-page).
### Multithreading
对于 TypeScript v1，function 执行在单线程上运行，在任意时刻仅允许一个计算任务。但是，您可以并行化 object sets 或 links 的加载。有关更多信息，请参阅 [optimizing performance](/docs/foundry/functions/optimize-performance/)。

For TypeScript v1, function execution is on a single thread, allowing only one computation at any given time. However, you can parallelize loading of object sets or links. Refer to [optimizing performance](/docs/foundry/functions/optimize-performance/) for more information.
对于 TypeScript v2 和 Python functions，您可以使用内置的 Node.js `worker_threads` 和 Python `threading` 库进行多线程处理。

For TypeScript v2 and Python functions, you can use multithreading with the built-in Node.js `worker_threads` and Python `threading` libraries.
### Object set limits with TypeScript v1
在使用 [object sets](/docs/foundry/functions/api-object-sets/) 时，如果出现以下情况，调用 `.all()` 或 `.allAsync()` 将抛出错误：

When using [object sets](/docs/foundry/functions/api-object-sets/), calling `.all()` or `.allAsync()` will throw an error if:
* 一次性从 object set 中加载的 objects 超过 **100,000 个**。通常，即使加载数万个 objects 也会遇到时间限制或内存限制。对于遇到此限制的使用场景，请考虑使用 [aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations) 获取汇总数据，或使用 [ordering and limiting](/docs/foundry/functions/api-object-sets/#ordering-and-limiting) 获取 objects 的子集。

* 一次使用的 [search arounds](/docs/foundry/functions/api-object-sets/#search-around) 超过 **3 个**。

* More than **100,000 objects** are loaded at once from the object set. In general, even loading tens of thousands of objects will run into time limits or memory limits. For use cases where you are running into this limit, consider fetching summary data using [aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations) or fetching a subset of objects using [ordering and limiting](/docs/foundry/functions/api-object-sets/#ordering-and-limiting).
* More than **3 [search arounds](/docs/foundry/functions/api-object-sets/#search-around)** are used at once.
某些 aggregation 和 bucketing 操作存在限制。有关详细信息，请参阅 [aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations) 部分。

Some aggregation and bucketing operations have limits. See the [aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations) section for details.