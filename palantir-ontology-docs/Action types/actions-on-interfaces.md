<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/actions-on-interfaces/
---
# Actions on interfaces
您可以创建适用于所选 interface 的所有 objects 的通用 action。可以通过两种主要方式在 action 中使用 interface：

You can create generic actions that apply to all objects of a chosen interface. There are two main ways you can use interfaces from within actions:
* **Interface action rules：** 用于创建、修改、删除和链接已配置 interface 的 objects。

* **Interface reference parameters：** 用于引用已配置 interface 的 objects。该参数是 "Modify" 和 "Delete" interface action rules 所必需的，但也可被任何其他 action rules 使用。

* **Interface action rules:** To create, modify, delete, and link objects of the configured interface.
* **Interface reference parameters:** To reference objects of the configured interface. This parameter is required by the "Modify" and "Delete" interface action rules, but can also be used by any other action rules.
> **⚠️ 警告**

> Interface action submission criteria 统一适用于实现该 interface 的所有 object types。在创建 interface action 之前，请仔细审查哪些用户将有权在所有实现该 interface 的 object types 上创建、修改或删除 objects。[详细了解如何对 interface actions 建立控制](#limitations-of-interface-action-rules)。
> **⚠️ 警告**

> Interface action submission criteria apply uniformly to all object types that implement the interface. Before you create an interface action, carefully review which users will have permission to create, modify, or delete objects across all object types that implement the interface. [Learn more about establishing control over interface actions](#limitations-of-interface-action-rules).
## Using action on interface rules
当编辑可以应用于实现该 interface 的所有 object types 时，您可以使用 interface action rules。换句话说，您只能使用 interface action rules 来修改 *interface shared properties* 或删除 objects。例如，如果 "Feature request" 和 "Bug" 是 "Ticket" interface 的 object types，则可以使用 "Create a ticket" action type 来创建 bugs 和 feature requests，但不能创建特定于 bugs 或 feature requests 的任何 property types。

You can use interface action rules whenever the edits can apply to all the object types that implement the interface. In other words, you can use interface action rules only to modify the *interface shared properties* or to delete objects. For example, if “Feature request” and “Bug” are object types of the “Ticket” interface, you can use a “Create a ticket” action type to create bugs and feature requests, but you cannot create any property types that are specific to bugs or feature requests.
![Using action on interface rules](/docs/resources/foundry/action-types/action_on_interface_rules.png)
### Creating a new interface action type
要设置新的 interface action type，请从 Ontology Manager 中的 **New** 菜单中选择 **Action type**。

To set up a new interface action type, choose **Action type** from the **New** menu in Ontology Manager.
1. 在 **Interfaces** 下，选择所需的 interface 和 rule type。

1. Under **Interfaces**, pick the desired interface and rule type.
![Creating new interface](/docs/resources/foundry/action-types/action_on_interface_new_interface.png)
2. 添加要包含在 action 中的 shared properties（如果适用）。

3. 添加 metadata 以描述您的 action type。请记住，此 metadata 应适用于实现该 interface 的所有 object types。

4. 在 **Submission criteria** 下，选择可以执行该 action 的用户（稍后可以应用更复杂的条件）。请记住，只要用户具有编辑权限，这些权限将适用于实现该 interface 的所有 object types。

5. 选择 **Create** 以完成 action type 的创建。

2. Add the shared properties that you want to include in the action (if applicable).
3. Add metadata to describe your action type. Remember that this metadata should apply to all the object types that implement the interface.
4. Under **Submission criteria**, choose the users that can execute the action (you can apply more complex criteria later on). Remember that these permissions will apply to all object types that implement the interface, as long as the user has permissions to edit them.
5. Select **Create** to finalize the action type.
### “Create” actions on interfaces
由于该 action type 仅与 interface 关联，因此将自动生成一个 "Object type" 参数，用于指示应创建的 object type。如果使用表单或表格，系统将提示用户从列表中选择 object type。

Because the action type is only associated with an interface, an “Object type” parameter will be automatically generated to indicate the object type that should be created. If using a form or a table, the user will be prompted to pick an object type from a list.
![Create actions on interface](/docs/resources/foundry/action-types/action_on_interface_create_action.png)
请注意，**没有 primary key 无法创建 objects**。因此，在 rule 中未分配 primary key 的任何 object type 在提交时都会失败。为避免此类失败，请确保 interface 和 Create rule 都包含一个 interface property，该 property 可在实现该 interface 的 object types 中用作 primary key。

Note that **objects cannot be created without a primary key**. Therefore, any object type without a primary key assigned in the rule will fail during submission. To avoid failures of this type, make sure that both the interface and the Create rule include an interface property that can be used as the primary key in the object types that implement the interface.
![Action on interface without primary key](/docs/resources/foundry/action-types/action_on_interface_primary_key.png)
### “Modify” actions on interfaces
Interface 上的 "Modify" 规则可以修改所配置 interface 的任何 object。将生成一个 "interface reference" 参数，该参数受所选 interface 的约束。"interface reference" 参数与 "object reference" 参数类似,不同之处在于 "interface reference" 参数会显示实现该 interface 的任何类型的 object。如果使用 form 或 table,用户随后可以从列表中选择一个 object。

"Modify" rules on an interface can modify any object of the configured interface. An “interface reference” parameter will be generated, constrained to the selected interface. The "interface reference" parameter is similar to the “object reference” parameter, with the exception that the "interface reference" parameter shows objects of any type that implements the interface. If using a form or a table, the user could then pick an object from a list.
请注意,主键值*无法被任何 action type 修改*。因此,如果 action 尝试修改所选 object type 的主键 property,则该 action 将在提交时失败。务必确保 action 规则不会修改那些可能被实现该 interface 的某些 object type 用作主键的 property。

Note that primary key values *cannot be modified* by any action type.  Therefore, an action will fail on submission if the action tries to modify a primary key property for a selected object type. Always ensure that the action rule does not modify properties that are likely to be used as a primary key by some of the object types that implement the interface.
在下面的示例中,"Title" property 被错误地用作 "Bug" object type 的主键。"Edit ticket" action 将在提交时失败,因为该 action 试图更改 bug 的主键。

In the example below, the “Title” property is incorrectly used as the primary key for the “Bug” object type. The “Edit ticket” action will fail on submission because the action attempts to change the primary key of the bug.
![Action on interface modify primary key](/docs/resources/foundry/action-types/action_on_interface_primary_key_modify.png)
### "Delete" actions on interfaces
"Delete" action 规则可以分配一个 "interface reference" 参数,而不是 object reference 参数。这个受特定 interface 约束的 interface reference 将指示要删除的 object。如果使用 form 或 table,用户随后可以从列表中选择一个 object。

"Delete" action rules can have an "interface reference" parameter assigned to them, instead of an object reference parameter. This interface reference, constrained to a specific interface, will indicate the object to be deleted. If using a form or a table, the user could then pick an object from a list.
### "Create link" actions on interfaces
"Create interface link" 规则允许您使用 interface 上定义的 interface link constraint 来创建 link。要配置 "Create interface link" 规则:

"Create interface link" rules allow you to create links using an interface link constraint defined on an interface. To configure a "Create interface link" rule:
1. 选择您要在其上创建 link 的 interface。

2. 选择 interface 上定义的 interface link constraint。如果 link constraint 是介于两个 interface 之间,则 source 和 destination 参数都将自动生成为 interface reference 参数。如果 link constraint 是介于一个 interface 和一个 object type 之间,则 source 将是 interface reference 参数,destination 将是 object reference 参数。

1. Select the interface you want to create links on.
2. Select the interface link constraint defined on the interface. If the link constraint is between two interfaces, both the source and destination parameters will be automatically generated as interface reference parameters. If the link constraint is between an interface and an object type, the source will be an interface reference parameter and the destination will be an object reference parameter.
(可选)如果您不想使用 action 自动生成的参数,您也可以手动配置 source 和 destination object。这些可以是:

Optionally, you can also configure the source and destination objects manually if you do not want to use the parameters autogenerated by actions. These can be:
* 引用现有 object 的 interface reference 或 object reference 参数。

* 由同一 action type 中的 "Create object" 或 "Create object(s) of interface" 规则创建的 object。

* An interface reference or object reference parameter referencing an existing object.
* An object created by a "Create object" or "Create object(s) of interface" rule within the same action type.
> **⚠️ 警告**

> 如果 object type 的 link constraint 存在多个具体的 link 实现,则该 action 将失败。此外,创建 one-to-many link 会修改关系中 many 一方的外键。如果您的 action type 还使用 "Create object" 或 "Modify object(s)" 规则修改外键,请确保没有冲突。
> **⚠️ 警告**

> If there are multiple concrete link implementations on the object type for the link constraint, the action will fail. Additionally, creating a one-to-many link modifies the foreign key on the many side of the relationship. Ensure there are no conflicts if your action type also modifies the foreign key using a "Create object" or "Modify object(s)" rule.
### "Delete link" actions on interfaces
"Delete interface link" 规则允许您使用 interface 上定义的 interface link constraint 来删除 link。要配置 "Delete interface link" 规则:

"Delete interface link" rules allow you to delete links using an interface link constraint defined on an interface. To configure a "Delete interface link" rule:
1. 选择您要在其上删除 link 的 interface。

2. 选择 interface 上定义的 interface link constraint。如果 link constraint 是介于两个 interface 之间,则 source 和 destination 参数都将自动生成为 interface reference 参数。如果 link constraint 是介于一个 interface 和一个 object type 之间,则 source 将是 interface reference 参数,destination 将是 object reference 参数。

1. Select the interface you want to delete links on.
2. Select the interface link constraint defined on the interface. If the link constraint is between two interfaces, both the source and destination parameters will be automatically generated as interface reference parameters. If the link constraint is between an interface and an object type, the source will be an interface reference parameter and the destination will be an object reference parameter.
(可选)您也可以手动配置 source 和 destination object,而不是使用自动生成的参数。这些参数必须是引用现有 object 的参数——即 interface reference 或 object reference 参数。

Optionally, you can also manually configure the source and destination objects instead of using the autogenerated parameters. These must be parameters referencing existing objects — either interface reference or object reference parameters.
> **⚠️ 警告**

> 如果 object type 的 link constraint 存在多个具体的 link 实现,则该 action 将尝试删除所有具体的 link 实现。
> **⚠️ 警告**

> If there are multiple concrete link implementations on the object type for the link constraint, the action will attempt to delete all the concrete link implementations.
### Executing actions on interfaces
使用 interface action 规则创建的 action 可以应用于其 object type 实现该 interface 的 object,就像任何特定于 object 类型的 action type 一样。对于给定的 object,所有可应用于该 object 的特定于 object 类型的以及基于 interface 的 action 都将出现在 action 下拉列表中。

Actions created with interface action rules can be applied to objects whose object type implements the interface, just like any object-specific action type. For a given object, all object-type-specific and interface-based actions that can be applied to that object will appear in the action dropdown.
## Permissions
Interface action 规则遵循与 object action type 相同的权限。

Interface action rules follow the same permissions as object action types.
有关更多详细信息，请参阅 [action type permissions](/docs/foundry/action-types/permissions/) 文档。

See the documentation on [action type permissions](/docs/foundry/action-types/permissions/) for more details.
## Level of support
随着 interface action rules 和 reference parameters 支持的扩展，Palantir 平台上的可用性可能会有所不同。

As support for interface action rules and reference parameters expands, availability will vary across the Palantir platform.
### Supported applications and services
* **Ontology Manager：** 创建 interface action types 以及在 submission criteria 和 overrides 中配置 interface parameters。

* **Object Explorer 和 Object Views：** 渲染 interfaces 上定义的 actions。

* **Ontology Manager:** Creation of interface action types and configuration of interface parameters in submission criteria and overrides.
* **Object Explorer and Object Views:** Rendering of actions defined on interfaces.
### Limitations of interface action rules
* Submission criteria 在实现该 interface 的所有 object types 上统一应用，因此您无法在单个 interface action 中为每个 object type 配置不同的权限。若要限制访问，请在 [Ontology Manager](/docs/foundry/ontology-manager/overview/) 中通过选择其 **Interfaces** 选项卡并在该 interface 的 **Interface action control** 部分中控制从 interface 继承的 actions，从而为特定 object types 禁用 interface actions。对 interface actions 应用更细粒度的权限控制的功能正在积极开发中。

* 尚不支持 action logs。

* 接口（interfaces）上的 actions 无法与 functions 一起使用。

* Submission criteria apply uniformly across all object types that implement the interface, so you cannot configure different permissions per object type within a single interface action. To restrict access, disable interface actions for specific object types in [Ontology Manager](/docs/foundry/ontology-manager/overview/) by selecting its **Interfaces** tab and establishing control over actions inherited from an interface in the **Interface action control** section. The ability to apply more granular permission controls to interface actions is under active development.
* Action logs are not yet supported.
* Actions on interfaces cannot be used with functions.