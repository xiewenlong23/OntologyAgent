<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/function-actions-overview/
---
# Function-backed actions
在 action type 中，[rules](/docs/foundry/action-types/rules/) 定义了当应用该 action 时对象应如何更改。许多 action type 可以使用简单的 rules 进行定义，这些 rules 允许您创建、修改和删除对象，或者创建和删除对象之间的 link。

In an action type, [rules](/docs/foundry/action-types/rules/) define the ways objects should change when the action is applied. Many action types can be defined using simple rules which allow you to create, modify, and delete objects, or create and delete links between objects.
然而，在某些情况下，简单的 rules 不足以描述您希望进行的更改。例如，您可能希望：

In some cases, however, simple rules are not sufficient to describe the changes that you want to make. For example, you may want to:
* 修改当前链接在一起的多个对象。例如，您可能希望将 `Incident` 对象的 `status` 字段设置为 `Closed`，并将所有链接的 `Alert` 对象的 `status` 也设置为 `Resolved`。

* 根据某些更复杂的逻辑修改对象的 properties。例如，您可能希望根据读取自多个对象的某些业务逻辑来计算一个值，然后将该值写入到 object property 中。

* 创建多种不同类型的对象并在它们之间建立 link。

* Modify multiple objects that are currently linked together. For example, you may want to set the `status` field of an `Incident` object to `Closed`, and also set the `status` of all linked `Alert` objects to `Resolved`.
* Modify an object's properties based on some more complex logic. For example, you may want to compute a value based on some business logic that reads data from several objects, then write that value into an object property.
* Create several different types of objects and set up links between them.
为了支持此类用例，可以将 action types 配置为调用一个 [function](/docs/foundry/functions/overview/)，该 function 定义了应如何修改对象的逻辑。这些 action types 通常被称为 **function-backed actions**。通过使用 function，您可以创建任何复杂度的 action types，读取任意数量的对象并按需修改对象。

To support use cases like these, action types can be configured to call a [function](/docs/foundry/functions/overview/) that defines the logic of how objects should be modified. These action types are often referred to as **function-backed actions**. By using a function, you can create action types of any level of complexity, reading any number of objects and modifying objects as you see fit.
尽管 function-backed action types 非常灵活，但您应注意它们受 [action type 限制](/docs/foundry/action-types/scale-property-limits/)和 [function 执行限制](/docs/foundry/functions/manage-functions/#enforced-limits)的约束。

Although function-backed action types are very flexible, you should note that they are subject to both [action type limits](/docs/foundry/action-types/scale-property-limits/) and [function execution limits](/docs/foundry/functions/manage-functions/#enforced-limits).
通过跟随[教程](/docs/foundry/action-types/function-actions-getting-started/)开始使用 function-backed actions。

Get started with function-backed actions by following the [tutorial](/docs/foundry/action-types/function-actions-getting-started/).