<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-search-functions/
---
# Search Functions
Search Functions 使用户能够快速找到并评估针对其调度工作流中出现的特定、独特问题的可能解决方案。

Search Functions enable users to quickly find and evaluate possible solutions to the specific, unique problems that arise in their scheduling workflow.
每个 Search Function 都由一个 TypeScript function 提供支持。这个灵活的 interface 允许构建者编写可以返回 pucks、time slots 或两者组合的 functions。此外，Search Functions 可以是 row-based 或 puck-based 的。

Each Search Function is backed by a TypeScript function. The flexible interface allows builders to write functions that can return pucks, time slots, or a combination of both. Additionally, Search Functions can be row-based or puck-based.
对于 row-based 的 Search Functions，用户必须右键单击空白区域，并将 row object 和 time 作为 function inputs 传入。对于 puck-based 的 Search Functions，用户必须右键单击 puck，以将 object 和 time 作为 function inputs 传入。

For row-based Search Functions, users must right-click on an empty space and pass in row object and time as function inputs. For puck-based Search Functions, users must right-click on a puck to pass in object and time as function inputs.
下图显示了返回 pucks 的 Search Function 的 interface。

The image below displays the interface for a Search Function returning pucks.

> 📷 **[图片: Example: search function returning pucks]**

> 📷 **[图片: Example: search function returning pucks]**

下图显示了返回 time slots 的 Search Function 的 interface。

The image below displays the interface for a Search Function returning time slots.

> 📷 **[图片: Example: search function returning time slots]**

> 📷 **[图片: Example: search function returning time slots]**

Search Function 执行后，将在 Scheduling Gantt Chart 中创建一个新的 search group，结果以黄色高亮显示。通过选择组标题右侧的插入符号（**^**），可以折叠和展开 search groups。此外，用户可以通过选择 **Results Overview** 选项来查看搜索结果的详细信息，这将打开一个包含 Search Function 输出的面板，如下图所示。

After a Search Function is executed, a new search group will be created in the Scheduling Gantt Chart with the results highlighted in yellow. Search groups can be collapsed and expanded by selecting the caret symbol (**^**) on the right side of the group header. Additionally, users can view search results in detail by selecting the **Results Overview** option to open a panel with the output of the Search Function, as displayed in the below image.

> 📷 **[图片: Search Function results overview interface.]**

> 📷 **[图片: Search Function results overview interface.]**

## Functions interface
以下类型表示从 row 或 puck 触发 Search Function 时所需编写的信息，包括有关 search group 的详细信息。

The types below represent the necessary information to write a Search Function when triggered from either a row or a puck, including details about the search group.
```
type IPuckSearch = (puck: ObjectReference) => ISearchResult
type IRowSearch = (rowId: string, selectedTime: Timestamp) => ISearchResult

/*
Search Functions can return time slots, pucks, or both. SLOT and PUCK
are used as types in IHighlight.
*/

export enum HighlightType {
SLOT = "SLOT",
PUCK = "PUCK",
}

/*
Used in IHighlight for functions that will return a set of timeslots.
*/

export interface IDomain {
start: Long;
end: Long;
}

/*
Used to determine what is highlighted in the UI after search function is run
*/

export interface IHighlight {
type: string;
// needed for "SLOT"
domain?: IDomain;
containerId?: string;
// needed for "PUCK"
schedulableObjectPrimaryKey?: string;
schedulableObjectTypeId?: string;
// optional
comment?: string;
}

/*
Defines the title of newly created search group and the rows the
function returns.
*/
export interface IRowGroup {
title: string;
containerIds: string[];
highlights: IHighlight[];
}

/*
Overall return type of function.
*/

export interface ISearchResult {
rowGroup?: IRowGroup;
sourcePuckIds?: string[];
error?: string;
}
```