<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/overview/
---
# Action types
在 Ontology 中，用户可以通过应用 actions 来对 objects、properties 和 links 进行更改。一个 action 是一笔单一的交易(transaction),它根据用户定义的逻辑更改一个或多个 objects 的 properties。Actions 使用户能够处理和管理数据,同时关注整体目标而非特定的 property 编辑。

In the Ontology, users can make changes to objects, properties, and links by applying actions. An action is a single transaction that changes the properties of one or more objects, based on a user-defined logic. Actions enable users to handle and manage data while thinking about overall objectives instead of specific property edits.
**action type** 是一组可一次性执行的针对 objects、property values 和 links 的更改或编辑的定义。它还包括 action 提交时发生的副作用行为。

An **action type** is the definition of a set of changes or edits to objects, property values, and links that a user can take at once. It also includes the side effect behaviors that occur with action submission.
**Example:**
您可以创建一个 `Assign Employee` action type,用于定义用户如何更改给定 `Employee` object 的 `role` property 值。该 action type 可能需要 parameter 定义,以使用户能够以标准化表单输入新角色,并可以包含有关如何在 `Employee` object 与新 `Manager` object 之间自动创建 link 的规则。

You may create an `Assign Employee` action type that defines how users can change the `role` property value for a given `Employee` object. This action type could require a parameter definition enabling users to input the new role in a standardized form and can include rules for how to automatically create a link between the `Employee` object and that of a new `Manager`.
该 action 还可以:

The action could also:
* 包含一个通知 side effect,通知新旧 manager 此项更改。

* 验证授权员工(如人力资源部门的员工)可以执行该 action。

* Include a notification side effect that will notify the old and new manager of the change.
* Validate that authorized employees such as those working in human resources can perform the action.
设置这些 parameters 后,HR 员工便可以执行一个 action,例如将 "Melissa Chang" 的 `role` 更改为 "Product Manager"。

With these parameters set, an HR employee can then take an action to switch "Melissa Chang" to a "Product Manager" `role`, for example.
Foundry Ontology 并非抽象的数据模型,而是将每个本体概念映射到组织的实际数据,使该数据资产能够为实际应用提供支持。随着用户决策和洞察以 Ontology 编辑的形式被捕获,该数据资产的丰富性和价值也会不断增长。

Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. The data asset grows in richness and value as user decisions and insights are captured in the form of edits to the Ontology.
对 objects、property values 和 links 所做的任何更改都将在用户执行 action 时提交至 Ontology,并在所有用户应用中反映出来。同样,相同的 action 逻辑和验证可以在所有面向用户的应用中提供,从而确保对 Ontology 的编辑保持一致。包含用户编辑的最新版本的 object 数据将被捕获到 object type 的 writeback dataset 中。

Any changes made to objects, property values, and links will be committed to the Ontology when the user takes the action and will be reflected in all user applications. Likewise, the same action logic and validations can be made available across all user-facing applications, ensuring consistent edits to the Ontology. The most up-to-date version of object data with user edits incorporated will be captured in an object type's writeback dataset.
首先学习如何 [create an action type](/docs/foundry/action-types/getting-started/),或了解 [rules](/docs/foundry/action-types/rules/)、[parameters](/docs/foundry/action-types/parameter-overview/) 和 [submission criteria](/docs/foundry/action-types/submission-criteria/)。

Get started by learning how to [create an action type](/docs/foundry/action-types/getting-started/), or learn about [rules](/docs/foundry/action-types/rules/), [parameters](/docs/foundry/action-types/parameter-overview/), and [submission criteria](/docs/foundry/action-types/submission-criteria/).