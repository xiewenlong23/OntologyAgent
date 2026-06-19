<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/configure-timeseries-foundry-rules/
---
# Configure time series
> **ℹ️ 注意**

> 在 2022 年 7 月之前，Foundry Rules（以前称为 Taurus）要求用户创建自己的 transform 来运行 Foundry Rules。本节仅与您在 2022 年 7 月之前部署 Foundry Rules 的情况相关。
> **ℹ️ 注意**

> Prior to July 2022, Foundry Rules (previously known as Taurus) required users to create their own transform to run Foundry Rules. This section is only relevant if you deployed Foundry Rules prior to July 2022.
> **ℹ️ 注意**

> 这些说明假定时间序列已在您的 platform 中设置完成。了解更多关于 [在 Foundry 中使用时间序列](/docs/foundry/time-series/time-series-usage/) 的信息。
> **ℹ️ 注意**

> These instructions assume time series have already been set up in your platform. Learn more about [using time series in Foundry](/docs/foundry/time-series/time-series-usage/).
如果您正在创建新的 workflow，请按照步骤 [部署 Foundry Rules](/docs/foundry/foundry-rules/deploy-foundry-rules/)。如果您在 2022 年 7 月之前部署了 Foundry Rules，则需要执行以下额外的步骤以启用时间序列支持。

If you are creating a new workflow, follow the steps to [deploy Foundry Rules](/docs/foundry/foundry-rules/deploy-foundry-rules/). If you deployed Foundry Rules prior to July 2022, the additional steps described below are required to enable time series support.
## Workshop application
在 Workshop 应用中开始编写时间序列规则有两个步骤：

There are two steps to start writing time series rules in the Workshop application:
1. 必须开启 Rule Editor 中的 **Enable time series rules** 配置。要导航到此设置，请编辑您的 Workshop 模块，单击 Rule Editor widget，然后找到标记为 **Enable time series rules** 的选项。

1. The **Enable time series rules** configuration in the Rule Editor must be turned on. To navigate to this, edit your Workshop module, click on the Rule Editor widget, and find the option labeled **Enable time series rules**.

> 📷 **[图片: time series workshop flag]**

> 📷 **[图片: time series workshop flag]**

2. 要创建时间序列规则，source object 必须是 root object type。将您需要的所有 root object type 添加到 **Permitted object types** 集合中。此处添加的所有 object 也需要添加到 transforms pipeline 中。

2. To create time series rules, the source object must be the root object type. Add all the root object types you require to the set of **Permitted object types**. All objects added here will also need to be added to the transforms pipeline.
## Transforms pipeline
Foundry rules 作为 transform 的一部分运行。请确保您已按照说明设置 [pipeline](/docs/foundry/foundry-rules/configure-transforms-pipeline/)。

Foundry rules are run as part of a transform. Ensure you have already followed the instructions to set up [the pipeline](/docs/foundry/foundry-rules/configure-transforms-pipeline/).
## Additional inputs
本节提供访问时间序列 metadata 的权限。要使时间序列规则运行，您必须向 additional inputs 添加更多项：

This section provides the permissions to access time series metadata. For time series rules to run, you must add more items to the additional inputs:
* 对于支持时间序列数据的每个 time series sync，使用 `.addTimeseriesSyncRids` 添加 sync 的 RID。

* 对于上述时间序列 sync 中使用的每个 tick dataset，使用 `.addBackingDatasetRids` 添加 tick dataset 的 RID。这些是包含实际时间序列数据的数据集。

* 使用 `.addObjectRids` 添加 root 和 sensor object 的 RID。

* 使用 `.addLinkRids` 添加 root 和 sensor object 之间 relation 的 RID。

* For each time series sync that backs the time series data, add the sync RID using `.addTimeseriesSyncRids`.
* For each tick dataset used in the times series syncs above, add the RID of the tick datasets using `.addBackingDatasetRids`. These are the datasets containing the actual time series data.
* Add the RID of the root and sensor object using `.addObjectRids`.
* Add the RID of the relation between the root and sensor object using `.addLinkRids`.
### Example
```java
@AdditionalInputs
public static Set<InputSpec> additionalInputs = ImmutableOntologyInputs.builder()
.addObjectRids("ri.ontology.main.object-type.adc4f61c-7ddd-4be2-9ade-a3a0483e63e4") // root object
.addObjectRids("ri.ontology.main.object-type.98f40fe0-d36f-4fcc-b36c-dc3824be17b5") // sensor object
.ontologyBranchRid("ri.ontology.main.branch.00000000-0000-0000-0000-000000000000")
.ontologyRid("ri.ontology.main.ontology.00000000-0000-0000-0000-000000000000")

// Time series inputs
.addLinkRids("ri.ontology.main.relation.6e82c6be-2a9a-42be-9cf0-c84a706b4101") // root object <-> sensor Object
.addTimeseriesSyncRids("ri.time-series-catalog.main.sync.8023a1b6-bae0-4dbf-8df5-9a879d8e0be0") // time series sync
.addBackingDatasetRids("ri.foundry.main.dataset.7041bedc-c475-46f6-81b6-8b989f099447") // ticks dataset
.addBackingDatasetRids("ri.foundry.main.dataset.7ee6741c-ea3d-48aa-9ba3-ec43b2ce42e4") // sensor object backing dataset
.build()
.getInputSpecs();
```
### Project references
还需要使用 [Code Repository](/docs/foundry/code-repositories/ontology-imports/) 的 **Settings** 选项卡中的 **Ontology Imports** 辅助工具，将 root object type、sensor object type 以及它们之间的 relation 导入到 Project 中。

It is also necessary to import the root object type, the sensor object type, and the relation between them into the Project using the **Ontology Imports** helper within the **Settings** tab of the [Code Repository](/docs/foundry/code-repositories/ontology-imports/).
![Ontology imports helper in Code Repository](/docs/resources/foundry/foundry-rules/ontology_imports.png)
此外，如果支持时间序列的 time series sync 或 ticks dataset 与 transform 不在同一个 Project 中，则还必须使用 Project 视图的 **Project References** 部分将它们 [导入](/docs/foundry/compass/move-and-share-resources/) 到 Project 中。

Additionally, if the time series sync or the ticks dataset that backs it are not in the same Project as the transform, then these must also be [imported](/docs/foundry/compass/move-and-share-resources/) into the Project using the **Project References** section of the Project view.

> 📷 **[图片: Rules Workflow Project view]**

> 📷 **[图片: Rules Workflow Project view]**

> 📷 **[图片: Rules Workflow references]**

> 📷 **[图片: Rules Workflow references]**

