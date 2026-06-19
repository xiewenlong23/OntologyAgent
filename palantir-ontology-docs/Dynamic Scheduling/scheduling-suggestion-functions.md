<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-suggestion-functions/
---
# Suggestion Function
在调度和资源分配工作流中,一个关键的挑战在于了解特定事件可以在何时何地发生,或者可以移动到何处。大多数调度都存在限制条件,且并非所有调度选项都同等合适;通过将这些限制条件和标准构建到逻辑中,工具可以帮助用户快速评估各种选择。Suggestion Functions 功能通过根据您的组织定义的逻辑,以可视化方式指示潜在的调度对象 puck 放置位置的适宜性,从而帮助引导用户行为。

A key challenge in scheduling and resource allocation workflows is knowing where and when specific events can occur or where they can be moved. Most schedules have limitations and not all schedule options are equally appropriate; by building these limitations and criteria into logic, tools can help users quickly evaluate choices. The Suggestion Functions feature helps guide user behavior by visually indicating the suitability of potential schedule object puck placement based on logic defined by your organization.
每个 Suggestion Function 都由一个 TypeScript function 提供支持。规则逻辑的输出可用于高亮显示可以进行分配的区域,或者与之相反,显示无法进行分配的区域。Application builder 可以选择通过 Workshop widget configuration 中的一个设置来强制执行这些建议。启用后,此功能将强制将 puck 放置到最近的高亮显示区域。

Each Suggestion Function is backed by a TypeScript function. The output of the rule logic can be used to highlight areas where an assignment can be made or, by contrast, areas where assignments cannot be made. Application builders have the option to enforce these suggestions through a setting in the Workshop widget configuration. When turned on, this feature will force placement of the puck to the closest highlighted region.
> **ℹ️ 注意**

> Scheduling Gantt Chart 中 Suggestion Functions 的结果是静态的。该 function 在应用程序初始加载时运行,之后执行的任何操作都**不会**被考虑。这对此功能是否适合您的工作流有一定的影响。
> **ℹ️ 注意**

> The results of the Suggestion Functions in the Scheduling Gantt Chart are static. The function is run during initial application load and any actions made afterwards are **not** accounted for. This has implications for whether this feature is suitable for your workflow.
以下是两个有效使用 Suggestion Functions 的示例。

Below are two examples of how Suggestion Functions can be used effectively.
在下图中,Suggestion Function 被编写为建议被分配人员(本例中为 "Susan")的首选位置。绿色区域表示 Garden City 是 Susan 的首选位置,而以灰色显示的 Sandbar 则不是首选位置。

In the following image, the Suggestion Function has been written to suggest the preferred location of the individual who is being assigned (in this case, “Susan”). The green area indicates that Garden City is Susan’s preferred location, while Sandbar, indicated in grey, is not preferred.

> 📷 **[图片: 示例:Suggestion function interface。]**

> 📷 **[图片: Example: Suggestion function interface.]**

在下面的示例中,应用程序用于将航班分配给飞行员。垂直时间段(以绿色显示)向调度员表明,他们不应调整航班的开始/结束时间,而只应调整作为飞行员的个人。

In the below example, an application is used to assign flights to pilots. The vertical slice of time (in green), indicates to the scheduler that they should not adjust the start/end time of the flight, but only the individual who is the pilot.

> 📷 **[图片: 示例:Suggestion function interface。]**

> 📷 **[图片: Example: Suggestion function interface.]**

## Functions interface
以下类型代表在从行(row)或 puck 触发时编写 Search Function 所需的信息,其中包括有关搜索组的详细信息。

The types below represent the necessary information to write a Search Function when triggered from either a row or a puck, which includes details about the search group.
```
/*
Suggestion functions take in a list of puck primary keys as well as
the Gantt's start/end time and returns a mapping of puck primary keys
to a mapping of row primary keys to an array of time slots.
*/

type ISuggestion = (
scheduleObjectPrimaryKeys: string[],
domainStart: Timestamp,
domainEnd: Timestamp,
) => FunctionsMap<string, FunctionsMap<string, Array<ISuggestionSlot>>>

/* Suggestion types */

export interface IDomain {
start: Long;
end: Long;
}

/* rating is used to determine the highlight color in widget UI. Based on
scale of -1 to 1. Closer to 1 and the highlight will be darker shade of
green. Closer to -1 and the highlight will be red.
*/

export interface ISuggestionSlot {
domain: IDomain;
rating: Float;
}

export type IValidSlots = Array<ISuggestionSlot>;
export type ISlotMappings = FunctionsMap<string, IValidSlots>;
export type ISuggestionResult = FunctionsMap<string, ISlotMappings>;

/*
In workflows where schedule objects have a set start/end time and may only change
assigned resources (vertical slice highlighted), the ALL_ROWS_ID can be used
as a shortcut.
*/

export const ALL_ROWS_ID = "__ALL_ROWS";

```