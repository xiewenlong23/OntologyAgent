<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/evaluation/
---
# Evaluation
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品，为平台中所有的业务自动化提供了统一的入口点。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
Object monitors 的评估和 Action 效果的执行由各个 subscriber 单独完成。这确保了依赖于用户属性的 data access permissions 和 Action validations 得到遵守，同时允许用户为其各自的工作流配置 object monitors。

Object monitors are evaluated and Action effects are executed individually by subscriber. This ensures that data access permissions and Action validations that rely on user attributes are respected while allowing users to configure object monitors for their individual workflows.
### Realtime evaluation
某些 input 和 condition 的组合支持 realtime evaluation。支持 realtime evaluation 的 object monitors 将被持续评估。Notifications 或 Actions 通常在检测到变化的数分钟内执行。如果从 pipeline build 同步大量更改，使用这些 objects 作为 inputs 的 monitors 的评估及其后续的 Actions 或 notifications 可能需要更长的时间来执行。

Some input and condition combinations support realtime evaluation. Object monitors that support it will be continuously evaluated. Notifications or Actions are usually executed within a few minutes of detected changes. If a large number of changes are synced from a pipeline build, the evaluation of monitors using those objects as inputs and its subsequent Actions or notifications may take a longer time to execute.
要支持 realtime evaluation，以下所有条件都必须满足：

To support realtime evaluation, all of the following must be true:
* input object type 已在 Ontology 配置中迁移至 [Object Storage V2](/docs/foundry/object-backend/overview/#evolution-of-the-ontology-backend)。

* input object type 的 object instances 少于 1000 万。如果一个 condition 正在以 realtime 方式被评估，并且由于新增 objects 导致 object type 增长超过此限制，monitor 将无法评估。

* input object set definition 仅在字符串、数字范围或布尔 properties 上使用 exact-match filters。

* input object set definition 不包含 linked object properties 或 array properties。

* rule 使用一个 [event condition](/docs/foundry/object-monitors/condition/#event) 来处理 input 中 objects 的添加或移除。

* The input object type has been migrated to [Object Storage V2](/docs/foundry/object-backend/overview/#evolution-of-the-ontology-backend) in the Ontology configuration.
* The input object type has less than 10 million object instances. If a condition is being evaluated in realtime and the object type grows beyond this limit due to new objects being added, the monitor will fail to evaluate.
* The input object set definition uses only exact-match filters on strings, ranges of numbers, or boolean properties.
* The input object set definition does not contain linked object properties or array properties.
* The rule uses an [event condition](/docs/foundry/object-monitors/condition/#event) for objects added or removed from input.
#### Scheduling monitors
> **ℹ️ 注意**

> Realtime evaluation 仅适用于来自 pipeline build 的更改。通过 Actions 所做的更改可能需要长达七个小时才能被 Object Monitors 检测到。若要缩短该时间，请为任何必须触发即时通知的 Action 添加一个 [notification rule](/docs/foundry/action-types/set-up-notification/#add-a-notification)。
> **ℹ️ 注意**

> Realtime evaluation only applies to changes coming from a pipeline build. Changes made through Actions may take up to seven hours before they are detected by Object Monitors. To shorten this time, include a [notification rule](/docs/foundry/action-types/set-up-notification/#add-a-notification) to any Action that must trigger an immediate notification.
虽然 realtime evaluation 目前不支持 scheduling monitors，但可以配置一个 function-backed Action，使其在 object monitor 检测到特定时间范围内的事件时运行，可使用 TypeScript 来检测当前时间/日期。以下代码片段展示了一个示例：

While realtime evaluation does not currently support scheduling monitors, it is possible to configure a function-backed Action to run when the object monitor detects an event between certain hours, using TypeScript to detect the current time/day. This code snippet shows an example:
```typescript
@Edits(ObjectType)
@OntologyEditFunction()
public someEditFunction(): void {
const currentTime = Timestamp.now()
const currentHour = currentTimestamp.getHours();
if (currentHour >= 0 && currentHour < 12) {
// Perform edits
}
}
```
### Non-realtime evaluation
无法实时评估的 Object monitor 将使用 polling 机制进行评估。Monitor 保证在上次评估后的 24 小时内进行评估。为了分摊大量 monitor 的评估负载，无法明确安排基于 polling 的评估的具体执行时间。基于 polling 的 monitor 的上次评估时间会被存储并显示在 Object Monitors application interface 的 monitor overview 面板中。

Object monitors that cannot be evaluated in realtime are evaluated using a polling mechanism. Monitors are guaranteed to evaluate within 24 hours of the previous evaluation. To distribute the load of evaluating for large numbers of monitors, the specific time when a polling-based evaluation occurs cannot be explicitly scheduled. The last-evaluated time for polling-based monitors is stored and displayed in the in the monitor overview panel of the Object Monitors application interface.
### Manual evaluation
非实时 object monitor 也可以从 Object Explorer interface 中手动评估。此选项主要用于设置非实时 monitor 时的测试。

Non-realtime object monitors may also be evaluated manually from the Object Explorer interface. This option is primarily intended for testing when setting up non-realtime monitors.
![Manual evaluation button in Object Explorer](/docs/resources/foundry/object-monitors/manual_evaluation_button.png)