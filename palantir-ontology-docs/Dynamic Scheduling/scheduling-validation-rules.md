<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-validation-rules/
---
# Validation rules
约束是任何调度工作流中固有的组成部分。从简单的时间限制到频繁变化的规则矩阵,规则的复杂性可以有很大的差异。Validation rules 允许您将这些约束编纂成规则,使最终用户能够在了解定义组织运营的限制和约束的前提下,构建和修改调度计划。

Constraints are an inherent part of any scheduling workflow. From simple time restrictions to frequently changing rule matrices, rules can range in complexity. Validation rules allow you to codify these constraints, enabling end users to build and modify schedules with an understanding of the limitations and restrictions that define your organization’s operations.
每个 validation rule 都由一个 TypeScript function 提供支持,该 function 用于评估 schedule object 的当前状态是否满足 function 逻辑中定义的某个条件。

Each validation rule is backed by a TypeScript function that evaluates whether the current state of a schedule object meets a certain condition as defined in the function logic.
用户可以在 Workshop 中 Scheduling Gantt Chart widget 的前端查看 validation rules 的结果。在初始加载时,所有规则都会根据 Ontology 的当前状态进行评估。每次对调度进行修改时,规则都会重新进行评估。此过程使用户能够了解其决策如何符合特定的约束和限制。

Users are presented with the results of validation rules on the front-end of the Scheduling Gantt Chart widget in Workshop. Upon initial load, all rules are evaluated based on the current state of the Ontology. With each modification to the schedule, the rules are re-evaluated. This process empowers users with the knowledge of how their decisions comply with specific constraints and restrictions.
以下是 Scheduling Gantt Chart widget 中调度约束的示例。在第一张图中,如切换按钮所示,应用了 **No Operator Overlaps** 规则。此选项可确保仅展示符合该规则的结果。下一张图展示了输出结果。在此示例中,两行之间存在冲突,操作员 Brad Evans 和 Ashley Brown 存在重叠。

Below is an example of scheduling constraints within a Scheduling Gantt Chart widget. In the first image, the rule **No Operator Overlaps** is applied, as indicated with the toggle. This option ensures that only results abiding by this rule will be presented. The following image demonstrates the output. In this example, there is a conflict between the two rows, where the operators, Brad Evans and Ashley Brown, are overlapping.

> 📷 **[图片: 示例 validation rules interface。]**

> 📷 **[图片: Example validation rules interface.]**

> 📷 **[图片: 不合规 validation rule 的示例。]**

> 📷 **[图片: Example of non-compliant validation rule.]**

## Orchestration
在 Workshop 的 Scheduling Gantt Chart 控件中,每次执行更改以验证调度时,都会调用验证规则。

In the Scheduling Gantt Chart widget in Workshop, the validation rules will be called each time a change is performed to validate the schedules.
```
1. Action "saveHandler" called on scenario
2. Validation rules called on updated scenario
3. Action "saveHandler" called on scenario
4. Validation rules called on updated scenario
etc ...
n. The user selects "Submit changes", and all Actions that have been applied to the scenario are applied to the Ontology
```

> 📷 **[图片: 合规验证规则示例。]**

> 📷 **[图片: Example of compliant validation rule.]**

## Implement validation rules
规则直接在 Scheduling Gantt Chart 控件中配置,允许您根据每个用例应用规则。要向 Scheduling Gantt Chart 控件添加规则:

Rules are configured directly in the Scheduling Gantt Chart widget, allowing you to apply rules on a per use case basis. To add a rule to your Scheduling Gantt Chart widget:
1. 导航到相关 Object Type 的 schedule data layer。

2. 向下滚动到 **Rules** 部分,然后选择 **Add new item**。

3. 在 **Rule Name** 文本框中,提供将向 Scheduling Gantt Chart 中的最终用户显示的规则描述。

4. 从下拉菜单中选择 **Constraint Type**。"HARD" 将以带感叹号的红色圆圈表示。"SOFT" 将以带感叹号的橙色三角形表示。

5. 从下拉菜单中选择 **Rule Function**。

6. 您的 Function 应具有 `scheduleObjectPrimaryKeys` 输入参数。您可以将此参数留空,因为控件将在运行时自动填充它。

1. Navigate to the schedule data layer for the relevant object type.
2. Scroll down to the **Rules** section and select **Add new item**.
3. In the **Rule Name** text box, provide a description of the rule that will be shown to end-users in the Scheduling Gantt Chart.
4. Select a **Constraint Type** from the drop down menu. “HARD” will be represented by a red circle with an exclamation point. “SOFT” will be represented by an orange triangle with an exclamation point.
5. Select the **Rule Function** from the drop down menu.
6. Your Function should have a `scheduleObjectPrimaryKeys` input argument. You can leave this argument empty as it will be autofilled by the widget at runtime.

> 📷 **[图片: Scheduling Gantt Chart 控件中的规则配置面板示例。]**

> 📷 **[图片: Example of rule configuration panel in Scheduling Gantt Chart widget.]**

### Functions interface
以下类型代表编写验证规则所需的信息,其中包括每个 Object 的规则状态。

The types below represent the necessary information to write a validation rule, which includes the status of the rule for each object.
```typescript
type IFoORule = (scheduleObjectPrimaryKeys: string[]) => Array<IRuleResult>

/*
Rule result is interpreted as follows:
true - Rule validated as passing
false - Rule validated as not passing
undefined - Rule is not relevant to the given schedule object
*/

interface IRuleResult {
result: boolean | undefined;
scheduleObjectPrimaryKey: string;
details?: Array<IRuleResultDetails>;
}

/*
By default the text on the pop-over card will display the rule name
as configured in the rule object

Optionally, you can explicitly define custom text based on the results
of rule evaluation

Additionally, you can provide a set of related puckIds to point users
towards why a rule is passing or failing
*/

interface IRuleResultDetails {
description: string;
relatedPuckIds: string[];
}
```
### Example Functions
以下是一个不包含验证核心逻辑的 Function 基本示例:

The following is a basic example of a Function without the core logic of the validation:
```typescript
import { Function, Integer } from "@foundry/functions-api";
import { Objects, TaskOrSchedule, ObjectSet} from "@foundry/ontology-api";

// For type definitions, review our public documentation

interface IRuleResultDetails {
description: string;
relatedPuckIds: string[];
}
interface IRuleResult {
result: boolean | undefined;
scheduleObjectPrimaryKey: string;
details?: Array<IRuleResultDetails>;
}
type IFoORule = (scheduleObjectPrimaryKeys: string[]) => Array<IRuleResult>

export class MyFunctions {

// NOTE: it is important that the input argument to a constraint function is named EXACTLY `scheduleObjectPrimaryKeys`.
// This is how the widget knows to send over the correct set of keys to this Function.
@Function()
public async evaluateIfTaskOrScheduleIsValid(scheduleObjectPrimaryKeys: string[]): Promise<Array<IRuleResult>> {
// Fetch all schedule Ontology Objects
const taskOrSchedules = await Objects.search().taskOrSchedule()
.filter(taskOrSchedule => taskOrSchedule.primaryKey.exactMatch(...scheduleObjectPrimaryKeys))
.allAsync();

// Iterate through every input key and generate a result entry for it
const ruleResults: Array<IRuleResult> = scheduleObjectPrimaryKeys.map(pk => {
const currentTaskOrSchedule = taskOrSchedules.find(taskOrSchedule => taskOrSchedule.primaryKey === pk);
// Do something with the object and validate something, ...

// Build the validation result
const currentValidationDetails: Array<IRuleResultDetails> = [];
currentValidationDetails.push(
{
description: "This is the description of the validation that passes or not",
relatedPuckIds: []
});

const currentResult: IRuleResult= {
result: true,
scheduleObjectPrimaryKey: pk,
details: currentValidationDetails,
};
return currentResult;
});

return ruleResults;
}
}

```
可以创建更复杂的验证规则。例如,规则可以检查以下内容:

More complex validation rules can be created. For example, rules can check the following:
* 调度是否按顺序排列(无间隔)
* 调度是否重叠
* 分配给调度的人员是否具有匹配的技能或认证

* If schedules are in sequence (no gap)
* If the schedules overlap
* If the person attributed to a schedule has the matching skills or certifications