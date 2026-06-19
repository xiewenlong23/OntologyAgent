<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/rules/
---
# Rules
**Rule** 定义了 Action Type 的逻辑，用于将参数转换为 Ontology 编辑或其他 effect。Rule 主要分为两种类型：一种用于编辑 Ontology，另一种用于触发 Foundry 中的其他 effect。

**Rules** define the logic of the action type that transform the parameters into Ontology edits or other effects. There are two main types of rules: ones that edit the Ontology, and ones that trigger another effect in Foundry.
## Ontology rules
Ontology rule 会更改 Ontology 的特定元素。它们可以创建、修改或删除现有类型的 Object 和 Link。要创建或删除一对多或一对一 Link，需要使用 object rule 并修改 Object 上的外键 Property。

An Ontology rule changes specific elements of the Ontology. They can create, modify, or delete objects and links of existing types. To create or delete one-to-many or one-to-one links, object rules need to be used and the foreign key property on the object needs to be modified.
1. **Create object:** 可用于创建预定义类型的 Object。Object Type 的主键是必填 Property,必须填写。可以选择性地添加其他 Property。

2. **Modify object(s):** 可用于修改现有 Object,其主键源自 Object reference 参数。无法引用作为当前 Action 一部分创建的 Object。

3. **Create or modify object(s):** 可用于根据 Object reference 参数修改现有 Object。如果未选择 Object,则将使用自动生成的唯一 ID 或用户提交的主键创建一个新 Object。

4. **Delete object(s):** 可用于删除现有 Object,其主键源自 Object reference 参数。无法引用作为当前 Action 一部分创建的 Object。

5. **Create link(s):** 可用于在通过 Object reference 参数传递的 Object 之间创建多对多 Link。对于外键 Link,必须使用 **Modify object** 规则显式修改外键 Property。

6. **Delete link:** 可用于删除通过 Object reference 参数传递的 Object 之间的多对多 Link。对于外键 Link,必须使用 **Modify object** 规则显式修改外键 Property。

7. **Function rule:** 可用于引用 Ontology edit function,其输入源自 Action 的参数。当存在此规则时,不能配置其他规则,因为 function code 本身就能处理其他规则可执行的所有操作。详细了解 [function action types](/docs/foundry/action-types/function-actions-overview/)。

8. **Create object(s) of interface:** 可用于创建实现特定 Interface 的任何类型的 Object。详细了解 [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/)。

9. **Modify object(s) of interface:** 可用于修改实现特定 Interface 的类型的 Object。详细了解 [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/)。

10. **Delete object(s) of interface:** 可用于删除实现特定 Interface 的类型的 Object。详细了解 [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/)。

11. **Create link(s) on object(s) of interface:** 可用于在实现特定 Interface 的类型的 Object 之间创建 Link。详细了解 [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/)。

12. **Delete link(s) on object(s) of interface:** 可用于删除实现特定 Interface 的类型的 Object 之间的 Link。详细了解 [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/)。

1. **Create object:** Can be used to create an object of a predefined type. The primary key of the object type is a required property which has to be filled. Additional properties can be added optionally.
2. **Modify object(s):** Can be used to modify an existing object whose primary key is derived from object reference parameters. This cannot reference an object created as a part of the current action.
3. **Create or modify object(s):** Can be used to modify an existing object based on an object reference parameter. If an object is not selected, a new object will be created with either an automatically generated unique ID, or with a user submitted primary key.
4. **Delete object(s):** Can be used to delete an existing object whose primary key is derived from object reference parameters. This cannot reference an object created as a part of the current action.
5. **Create link(s):** Can be used to create a many-to-many link between objects that are passed via object reference parameters. For foreign key links, one has to use **Modify object** rule to explicitly modify the foreign key property.
6. **Delete link:** Can be used to delete a many-to-many link between objects that are passed via object reference parameters. For foreign key links, one has to use **Modify object** rule to explicitly modify the foreign key property.
7. **Function rule:** Can be used to reference an Ontology edit function whose inputs are derived from parameters of the action. When this rule is present, no other rule may be configured since function code alone is capable of handling everything that other rules can do. Read more about [function action types](/docs/foundry/action-types/function-actions-overview/).
8. **Create object(s) of interface:** Can be used to create objects of any type that implements a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).
9. **Modify object(s) of interface:** Can be used to modify objects of types that implement a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).
10. **Delete object(s) of interface:** Can be used to delete objects of types that implement a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).
11. **Create link(s) on object(s) of interface:** Can be used to create links between objects of types that implement a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).
12. **Delete link(s) on object(s) of interface:** Can be used to delete links between objects of types that implement a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).
### Values and parameters
在创建或修改 Link 和 Object 时,Rules 需要额外的值用于其操作。修改 Object 时,规则还定义了要修改的 Property。每个 Property 又会映射到由多个选项之一提供的值(Link 上的 Rules 只能采用 Object reference 参数):

When creating or modifying links and objects, the Rules require additional values for their operation. When modifying an object, the rules also define which properties are modified. Each property in return is mapped to a value provided by one of multiple options (Rules on links can only take object reference parameters):
* **From parameter:** 与 Property 类型相同的现有参数。默认情况下,添加到规则的每个新 Property 都会自动创建一个同名的参数,并被映射为采用此参数的值。

* **Object parameter property:** 现有 Object reference 参数的 Property。Object parameter 的 Property 类型需要与其映射到的 Property 类型相匹配。

* **Static value:** 仅存在于 Action Type 的 Rules 部分中的静态值。在 Workshop、Slate 或 Object Views 中与 Action 交互时,无法更改此值。

* **Current User/Time:** 字符串和时间戳 Property 也可以采用上下文值,形式为 Action 的当前用户或提交时间。与 **Static value** 一样,这些值在提交 Action 时无法交互,并且不能用于 Action Type 的其他部分。

* **From parameter:** An existing parameter of the same type as the property. By default, every new property being added to the rule will automatically create a parameter with the same name and will be mapped to take the value of this parameter.
* **Object parameter property:** A property of an existing object reference parameter. The property type of the object parameter needs to match the property type it is mapped to.
* **Static value:** A static value that only exists in the Rules part of the action type. This value is cannot be changed when interacting with the action in Workshop, Slate, or Object Views.
* **Current User/Time:** String and timestamp properties can also take on contextual values in the form of the actions current user or the time of submission. Just like the **Static value**, these values cannot be interacted with when submitting the action and cannot be used in other parts of the action type.
### Creating an object & many-to-many link
您也可以同时创建 Object 和多对多 Link。虽然仅创建多对多 Link 要求 Link 两侧的 Object 必须预先存在,但您可以通过一个 Action Type 同时创建两个实体。首先配置一个 **Create object** 规则,使用具有多对多 Link 的 Object Type。然后单击 **Add property** 下方的 **Add link** 按钮以选择 Link Type 并配置 Link。

You can also create objects and linked many-to-many at the same time. While just creating a many-to-many link requires objects on both sides of the link to exist prior, you can create both entities via one action type. Start by configuring a **Create object** rule with an object type that has a many-to-many link. Then click the **Add link** button below **Add property** to select the link type and configure the links.
要创建一对多或一对一 Link Type,只需编辑 Object 上的外键即可。

In order to create a one-to-many or one-to-one link type, simply edit the foreign key on the object.
### Invalid combinations
Action Type 可以包含 Ontology 规则的组合。当定义多个规则时,Action 后端会编译规则以针对每个 Object 生成单个 edit(例如,**Add object**、**Modify object(s)** 或 **Delete object(s)**)。例如,如果一个规则的结果将 Property 更新为 "A",但同一 Action Type 中的另一个规则将同一 Object 的 Property 更新为 "B",则最终 edit 仅会将 Property 更新为 "B"。规则的顺序会影响最终的 Object edit。因此,不支持以下 Object edit 组合:

Action types can include combinations of Ontology rules. When multiple rules are defined, the actions backend compiles rules to generate a single edit per object (e.g., **Add object**, **Modify object(s)**, or **Delete object(s)**). For example, if the result of one rule updates a property to "A", but another rule in the same action type updates the same object's property to "B", the resulting edit would just update the property to "B". The order of rules affects the final object edit. As a result, the following combinations of object edits are not supported:
* Object 不能在添加或修改之前被删除。

* Object 不能在添加之前被修改。

* 在一次表单提交中,Object 不能被创建两次。

* Objects cannot be deleted before they are added or modified.
* Objects cannot be modified before they are added.
* Objects cannot be created twice in one form submission.
## Other rules
有两类规则会触发 [side effect](/docs/foundry/action-types/side-effects-overview/):

There are two types of rules that trigger a [side effect](/docs/foundry/action-types/side-effects-overview/):
* [**Notification**](/docs/foundry/action-types/notifications/) 规则可用于发送有关该 Action 的通知。可以使用参数来自定义通知的内容和收件人。最终用户可以调整其偏好,以通过平台内推送通知、电子邮件或两者同时接收通知。通知在应用所有 Action edit 后发送,但通知的内容将根据应用 edit 之前的 Ontology 状态生成。

* [**Webhooks**](/docs/foundry/action-types/webhooks/) 使 Action 能够在应用该 Action 时向外部系统发出请求。Action 参数可以传递到 Webhook,然后 Webhook 又可以将参数传递到外部请求。Webhooks 可以配置为在应用 edit 之前或之后运行。

* [**Notification**](/docs/foundry/action-types/notifications/) rules can be used to send a notification about the action. Parameters may be used to customize the content of the notification and the recipients. End users may adjust their preferences to receive notifications via in-platform push notification, email, or both. Notifications are sent once all action edits have been applied, however the content of the notification will be generated based on the state of the Ontology before edits are applied.
* [**Webhooks**](/docs/foundry/action-types/webhooks/) enable an action to make a request to an external system when the action is applied. Action parameters can be passed into the webhook, which can in turn pass parameters through to the external request. Webhooks may be configured to run before or after edits are applied.
还有一个额外的高级规则会触发 [build](/docs/foundry/data-integration/builds/):

There is an additional advanced rule that triggers a [build](/docs/foundry/data-integration/builds/):
* [**Schedule**](/docs/foundry/action-types/trigger-schedule-build/) 规则可用于触发 schedule 的 build。Action 参数可以传递到 schedule,然后 schedule 又可以将参数传递到 build 中的底层 [parameterized transforms](/docs/foundry/building-pipelines/parameterization/)。Foundry 会在 build 开始后应用 Ontology edit。

* [**Schedule**](/docs/foundry/action-types/trigger-schedule-build/) rules can be used to trigger the build of a schedule. Action parameters can be passed into the schedule, which can in turn pass parameters to the underlying [parameterized transforms](/docs/foundry/building-pipelines/parameterization/) inside the build. Foundry applies Ontology edits after the build begins.