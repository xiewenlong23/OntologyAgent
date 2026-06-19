<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/legacy-foundry-rules-setup-taurus/
---
# Legacy Foundry Rules Setup (Taurus)
> **⚠️ 警告**

> 在 2022 年 7 月之前,Foundry Rules(以前称为 Taurus)需要额外的配置,并使用略有不同的概念。以下文档涵盖了此版本与较新版本的 Foundry Rules 之间的差异。
> **⚠️ 警告**

> Prior to July 2022, Foundry Rules (previously known as Taurus) required additional configuration and used slightly different concepts. The following documentation covers the differences between this and newer versions of Foundry Rules.
## Transforms pipeline
以前,Foundry Rules 不会自动生成 **transforms pipeline**,而是由用户负责创建和维护一个运行规则的 [Code Repository](/docs/foundry/code-repositories/overview/)。

Previously, instead of Foundry Rules generating the **transforms pipeline** automatically, users were required to create and maintain a [Code Repository](/docs/foundry/code-repositories/overview/) that ran the rules.
了解有关创建和[更新此代码仓库](/docs/foundry/foundry-rules/configure-transforms-pipeline/)的更多信息。

Learn more about creating and [updating this repository](/docs/foundry/foundry-rules/configure-transforms-pipeline/).
## Workshop application
[Rule inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) 不再需要在 [Workflow Configuration Editor](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/) 中配置,以前需要在 Workshop application 和 transforms pipeline 两处进行配置。

Instead of the [rule inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) being configured in the [Workflow Configuration Editor](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/), they were previously required to be configured in both the Workshop application and the transforms pipeline.
此外,rule outputs 以前需要在三个位置进行配置:Workshop application、transforms pipeline 以及 [Ontology Manager](/docs/foundry/ontology-manager/overview/)。在下面的 [Rule Actions](#rule-actions) 部分中了解更多关于旧版 rule outputs 的信息。

Additionally, rule outputs were configured in three locations: the Workshop application, the transforms pipeline, and the [Ontology Manager](/docs/foundry/ontology-manager/overview/). Learn more about legacy rule outputs in the [Rule Actions](#rule-actions) section below.
了解有关在 [Workshop application](/docs/foundry/foundry-rules/configure-workshop-app/) 和 [transforms pipeline](/docs/foundry/foundry-rules/configure-transforms-pipeline/) 中添加和移除 rule inputs 的更多信息。

Learn more about adding and removing rule inputs in the [Workshop application](/docs/foundry/foundry-rules/configure-workshop-app/) and the [transforms pipeline](/docs/foundry/foundry-rules/configure-transforms-pipeline/).
## Rule Actions
在 [workflow outputs](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/#workflow-outputs) 出现之前,output schema 强制执行是通过 Foundry Actions 实现的。Action 的参数表示 dataset 列,并且必须映射到 logic 输出的列或由用户输入的静态值。rule Action 可以从 [transform 内部](/docs/foundry/foundry-rules/configure-transforms-pipeline/#rule-action-datasets) 访问,以检索指定格式的所有匹配行。当检索指定 rule Action 的结果时,*生成的 dataset 将包含使用该 Action 的所有规则输出的行*。此设计旨在使所有 Foundry rules 的输出更易于保持一致性。作为 Foundry Actions,它们必须在 Ontology Manager 中进行配置。

Before [workflow outputs](/docs/foundry/foundry-rules/foundry-rules-workflow-configuration/#workflow-outputs), output schema enforcement was achieved with Foundry Actions. The parameters of the Action represent dataset columns and must be mapped to either columns outputted by the logic or static values inputted by the user. The rule Action can be accessed from [within the transform](/docs/foundry/foundry-rules/configure-transforms-pipeline/#rule-action-datasets) to retrieve all matching rows in the specified format. When retrieving the results for a specified rule Action, *the dataset produced will contain the rows output by all rules which use that Action*. This is designed to make it easier to achieve consistency in the output of all Foundry rules. Being Foundry Actions, they must be configured within the Ontology Manager.
了解有关[配置 rule Actions](/docs/foundry/foundry-rules/configure-rule-actions/) 的更多信息。

Learn more about [configuring rule Actions](/docs/foundry/foundry-rules/configure-rule-actions/).
> **ℹ️ 注意**

> 虽然 rule Actions 是使用 Foundry Actions 配置的,但 Actions 并不是直接在相关 objects 上执行的。目前,其唯一的作用是指定 output schema。
> **ℹ️ 注意**

> While rule Actions are configured with Foundry Actions, Actions are not executed directly on top of the relevant objects. Currently, the only effect is to specify the output schema.
> **ℹ️ 注意**

> 一些在 2021 年 1 月之前部署的旧版 Foundry Rules(以前称为 Taurus)需要升级才能使用 rule Actions。除非您被明确指示这样做,否则您可能不需要执行此操作。
> **ℹ️ 注意**

> Some legacy versions of Foundry Rules (previously known as Taurus) deployed prior to January 2021, need to upgrade in order to use rule Actions. Unless you've been specifically directed to, you likely do not need to do this.
> 了解有关[升级以使用 rule Actions](/docs/foundry/foundry-rules/upgrade-to-use-rule-actions/) 的更多信息。
> Learn more about [upgrading to use rule Actions](/docs/foundry/foundry-rules/upgrade-to-use-rule-actions/).