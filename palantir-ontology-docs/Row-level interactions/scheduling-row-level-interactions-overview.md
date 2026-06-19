<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-row-level-interactions-overview/
---
# Row-level interactions
Scheduling Gantt 图表上的每一行代表一个 `Resource` 对象。你的 `Resource` 例如可以表示：

Each row on the Scheduling Gantt chart represents a `Resource` object. Your `Resource` can for example, represent:
* 用于任务分配的技术人员
* 被调度维护的车辆
* 行程的人员分配

* Technicians for task assignment
* Vehicles being scheduled for maintenance
* Crew allocation for trips
你可以使用行级交互，使用户能够修改行对象的某些 properties、创建对象，或在你的 Workshop module 中触发事件。

You can use row-level interactions to enable users to modify certain properties of your row objects, create objects, or trigger events in your Workshop module.
![Example of row-level interactions.](/docs/resources/foundry/dynamic-scheduling/row-level-interactions.gif)