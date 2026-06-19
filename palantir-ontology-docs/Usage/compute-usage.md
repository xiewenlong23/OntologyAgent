<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/compute-usage/
---
# Compute usage: Ontology indexing
Foundry 的 Ontology 将对象存储在 Ontology 索引中,这是一种针对快速访问进行了优化的存储格式。Foundry 数据集中的数据可以是任意大小或格式,因此需要进行数据转换才能将数据集数据准备好存储到 Ontology 索引中。此过程称为 *Ontology indexing*,可应用于任意大小的数据集和对象。Ontology indexing 的处理成本以 compute-seconds 衡量。本文档介绍了 Ontology indexing 如何使用 compute 以及如何管理 compute 用量。

Foundry’s Ontology stores objects in an Ontology index, a storage format optimized for rapid access. Data in Foundry datasets can be of any size or format, meaning a data transformation is required to prepare dataset data for storage in an Ontology index. This process is known as *Ontology indexing* and can be applied to datasets and objects of arbitrary size. The processing cost of Ontology indexing is measured compute-seconds. This documentation describes how Ontology indexing uses compute as well as how to manage compute usage.
## Measuring compute usage from Ontology indexing
Ontology Indexing 使用并行的 Spark 后端来读取任意大的数据集并将其转换为 Ontology 格式。运行 indexing 任务所使用的 compute 量取决于计算资源(driver 和 executors)的数量以及 indexing 任务本身的挂钟(wall-clock)总时长。

Ontology Indexing uses a parallelized Spark backend to read arbitrarily large sets of data and transform them into the Ontology format. The amount of compute that is used to run an indexing job is based on the amount of computational resources (driver and executors) and the total wall-clock duration of the indexing job itself.
有关 Spark 用量如何换算为 compute-seconds 的更多信息,请参阅主要的 [Usage Types](/docs/foundry/resource-management/usage-types/) 文档。您可以在下方找到 [Ontology Indexing 所用 compute-seconds 的计算示例](#example-indexing-compute-calculation)。

For more information on how Spark usage translates to compute-seconds, see the main [Usage Types](/docs/foundry/resource-management/usage-types/) documentation. Below, you can find [examples of the calculations for compute-seconds used by Ontology Indexing](#example-indexing-compute-calculation).
## Investigating usage from Ontology Indexing
Ontology indexing 任务会显示在 Foundry 的 Builds 应用中,并附加到正在被索引的对象上。Ontology indexing 任务是 Spark 任务,因此被归类为并行批处理 compute;因此,Ontology indexing 任务的衡量方式与同一后端上的其他任务(例如 Code Repositories 的 transforms 和 Contour 查询)相同。

Ontology indexing jobs are exposed in Foundry’s Builds application and are attached to the object that is being indexed. Ontology indexing jobs are Spark jobs and so are classified as parallelized batch compute; thus, Ontology indexing jobs can be measured in the same way as other jobs on the same backend, such as Code Repositories transforms and Contour queries.
Indexing 任务可根据其触发方式进行分类。

Indexing jobs can be categorized based on how they are triggered.
* *Ontology indexing 任务* 将数据集索引到 Ontology 后端。此 compute 用于从数据集生成已索引的对象。

* *Ontology export 任务* 将直接在 Ontology 中进行的编辑持久化到 Foundry transformation 框架中的数据集。这些任务通常比完整的 indexing 任务规模更小,因为 ontology export 任务通常处理的是编辑操作,而编辑操作只是整个对象集的严格子集。

* *Ontology indexing jobs* index datasets into the Ontology backend. This compute is used to produce indexed objects from datasets.
* *Ontology export jobs* persist edits made directly in the Ontology to datasets in the Foundry transformation framework. These jobs tend to be smaller than full indexing jobs as ontology export jobs are generally dealing with edits, which are strict subsets of the total object set.
## Drivers of usage for Ontology indexing
Ontology indexing 任务必须读取所有需要被索引的数据,并将其转换为 Ontology 后端能够快速存储、搜索和编辑的格式。

Ontology indexing jobs must read all of the data that needs to be indexed and transform it into a format that the Ontology backend can store, search, and edit quickly.
读取和索引数据时的 Compute 用量由以下因素决定:

Compute usage when reading and indexing data is driven by the following factors:
* **每个对象的记录数**

* 对象的数量会随着被索引数据集中记录数的增加而增加。每个对象都需要一定数量的计算操作才能完成 indexing,因此对象数量的增加会导致 indexing 所使用的 compute 量增加。

* **每个对象的 Property 数**

* 每个对象的每个 property 都必须由 indexing 任务单独进行分析,然后写入对象索引中。需要分析和索引的 property 越多,所使用的 compute 就越多。

* **每个 Property 的大小**

* 某些 property 的大小远大于其他 property。例如,包含大量内容的文本 property 在分析时比简单的数字 property 需要更多的空间和 compute。具有更大、更复杂 property 类型的对象将需要更多的 compute 来完成 indexing。

* **Number of records per object**
* The number of objects increases as the number of records in the dataset being indexed increases. Each object requires a certain number of computational operations for indexing, so increasing the number of objects increases the amount of compute used for indexing.
* **Number of properties per object**
* Each property of each object must be individually analyzed by the indexing job and then written into the object index. More compute is used if there are more properties to analyze and index.
* **Size of each property**
* Some properties are much larger than others. For instance, a text property containing a lot of content will require more space and compute to analyze than a simple number property. Objects with larger, more complex property types will require more compute to index.
Indexing 频率在 Ontology 更新的 compute 用量中也起着重要作用。上游数据集上设置的调度计划将触发对象的自动重新索引。在检查保持对象最新所带来的用量影响时,请考虑该对象及其上游数据集上的更新调度计划。

Indexing frequency also plays a large role in how much compute is used for Ontology updates. Schedules set on upstream datasets will trigger auto-reindexes of objects. When examining the usage implications of keeping an object up-to-date, consider the update schedules on that object and its upstream datasets.
## Managing Ontology indexing compute
可以对 Ontology indexing 任务进行优化以减少 compute 用量。优化最简单的方法是减少索引输入数据的大小,这会降低完成任务所需的工作量。这包括在可能的情况下执行以下操作:

Ontology indexing jobs can be optimized to reduce compute usage. The first and simplest method of optimization is to reduce the size of the input data for the index, which decreases the amount of work needed to complete the job. This involves doing the following where possible:
* 管理输入记录的数量

* 管理每个对象的 Property 数量

* 管理每个对象中每个 Property 的大小

* Managing the number of input records
* Managing the number of properties per object
* Managing the size of each property per object
另一种优化方法是配置 Ontology 索引作业以使用 changelog 策略进行索引。Changelog 索引通过在执行前将作业与现有对象进行比较，显著减少了每次索引作业需要创建或更新的对象数量。Changelog 索引需要更多的配置和对更新策略的遵守，但可以带来数量级的性能和效率提升。

Another optimization method is configuring Ontology index jobs to use changelog strategies for indexing. Changelog indexing significantly reduces the number of objects that need to be created or updated per indexing job by comparing the job against existing objects prior to execution. Changelog indexing requires more configuration and adherence to an update strategy, but can produce orders-of-magnitude performance and efficiency gains.
## Example indexing compute calculation
索引作业以并行化的 Spark 作业形式存在，可以在 Builds application 中查看。请参阅以下索引作业的示例。请注意，Ontology 索引作业将根据作业大小自动选择 driver 和 executor 的规模。

Indexing jobs take the form of parallelized Spark jobs and can be seen in the Builds application. See the following example for an indexing job. Note that Ontology indexing jobs will automatically choose the size of the driver and executors for the indexing job, depending on the size of the job.
```
Driver:
num_vcpu: 1
GiB_RAM: 6
Executors:
num_vcpu: 1
GiB_RAM: 4
num_executors: 2
Total Runtime: 10 seconds

Calculation:

driver_compute_seconds = max(num_vcpu, GiB_RAM / 7.5) * runtime_in_seconds
= max(1vcpu, 6GiB / 7.5) * 10sec
= 1 * 10 = 10 compute-seconds

executor_compute_seconds = max(num_vcpu, GiB_RAM / 7.5) * num_executors * runtime_in_seconds
= max(1vcpu, 4GiB / 7.5) * 2executors * 10sec
= 1 * 2 * 10 = 20 compute-seconds

total_compute_seconds = driver_commpute_seconds + exeucutor_compute_seconds
= 10 compute-seconds + 20 compute-seconds
= 30 compute-seconds

```