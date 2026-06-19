<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/overview/
---
# Foundry Rules
Foundry Rules（以前称为 Taurus）使用户能够通过 point-and-click、low-code interface 在 Foundry 中主动管理复杂的业务逻辑。使用 Foundry Rules，用户可以创建规则，并将这些规则应用于 datasets、objects 和 time series，以满足各种用例，如告警生成或数据分类。

Foundry Rules (previously known as Taurus) enables users to actively manage complex business logic in Foundry with a point-and-click, low-code interface. With Foundry Rules, users can create rules and apply those rules to datasets, objects, and time series for a variety of use cases like alert generation or data categorization.
Foundry Rules 包含一组用于创建、管理和应用规则的组件：

Foundry Rules comprises a set of components for creating, managing, and applying rules:
* **规则（rule）** 是一组 *条件（conditions）*，这些条件组合在一起可以指定数据集中特定的数据行。
* 构成规则的**条件**应用于数据集的列，范围从简单的过滤器到复杂的聚合、连接或其他运算符。

* A **rule** is a set of *conditions* that, taken together, can specify particular rows of data in a dataset.
* The **conditions** that form a rule apply to the columns of a dataset and can range from simple filters to complex aggregations, joins, or other operators.
![Screenshot of filter group with rules and conditions](/docs/resources/foundry/foundry-rules/filter_group.png)
以下页面描述了几个[核心概念](/docs/foundry/foundry-rules/core-concepts/)并提供了如何[部署](/docs/foundry/foundry-rules/deploy-foundry-rules/)和[自定义](/docs/foundry/foundry-rules/customization/) Foundry Rules 的说明。

The following pages describe several [core concepts](/docs/foundry/foundry-rules/core-concepts/) and provides instructions for how to [deploy](/docs/foundry/foundry-rules/deploy-foundry-rules/) and [customize](/docs/foundry/foundry-rules/customization/) Foundry Rules.
## Example use cases
Foundry Rules 可以简化涉及复杂规则集的使用场景的管理过程，例如：

Foundry Rules can simplify the process of managing use cases that involve complex sets of rules, such as:
* **反洗钱（Anti-Money Laundering, AML）：** 通过针对每笔交易和聚合指标的规则标记可疑交易。
* **设备监控：** 根据传感器数据在潜在设备退化时发出警报（例如，当某些测量值达到特定值时）。

* **人群分群（Cohorting）：** 根据规则将实体分类为群组或"cohort"。例如，创建具有特定特征的客户群组，以便进行更有针对性的营销。

* **Anti-Money Laundering (AML):** Flag suspicious transactions through rules targeting both per-transaction and aggregated metrics.
* **Equipment monitoring:** Raise alerts for potential equipment degradation based on sensor data (e.g. when certain measurements reach specific values).
* **Cohorting:** Categorize entities into groups or "cohorts" based on rules. For example, creating groups of customers with particular features for better targeted marketing.