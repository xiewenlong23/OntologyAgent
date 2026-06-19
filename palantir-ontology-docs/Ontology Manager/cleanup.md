<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/cleanup/
---
# Ontology cleanup
Ontology 清理工具是删除 Object Type 的一种安全方式，并提供诸多优势，包括：

The Ontology cleanup tool is a safe way to delete object types, and provides a number of benefits, including:
* 更易于导航的 Ontology，没有多余的 Object Type

* 更具性能的 Ontology，因为搜索和加载在更少的 Object Type 上运行

* 没有多余存储成本负担的 Ontology

* An easier-to-navigate Ontology without excess object types
* A more performant Ontology as searches and loads are run over fewer object types
* An Ontology without the burden of excess storage costs
该工具旨在帮助 Ontology 编辑器判断删除 Object Type 的安全性，并提供 deprecation 选项，以通知 Object Type 使用者其将来会被删除。

The tool aims to help Ontology editors determine the safety of deleting an object type and provides a deprecation option which informs object type users of its future removal.
## Access Ontology cleanup tool
可以从 Ontology 清理工具的主页访问该视图。

The view can be accessed from the home page of the Ontology cleanup tool.
![Access the tool from the home page](/docs/resources/foundry/ontology-manager/cleanup-navigation-from-homepage.png)
当您选择 **Start cleanup** 时，该工具可能需要一些时间来根据 Ontology 的规模查找清理候选对象。

When you opt to **Start cleanup**, the tool may take time to find cleanup candidates based on the size of your Ontology.
![Start cleanup button](/docs/resources/foundry/ontology-manager/cleanup-start-cleanup-button.png)
生成的 object types 列表的操作方式与从主页访问的其他显示列表的页面类似。该列表可以按特定 flags 或您负责的 object type group 进行过滤。您还可以自定义表中显示的列。

The resulting list of object types operates similarly to the other pages accessed from the home page that display lists. The list can be filtered to specific flags or an object type group that you are responsible for. You can also customize which columns are displayed in the table.
![Cleanup filters](/docs/resources/foundry/ontology-manager/cleanup-filters.png)
默认情况下,表按 object type 触发的 flags 中的最高优先级排序。

By default, the table is sorted by the highest priority among the flags that an object type triggers.
## Cleaning up your Ontology
以下是一个示例,我们已将列表过滤到 "Planning" workflow,这是一个正在开发但从未发布的 workflow。

Here is an example where we have filtered down to the “Planning” workflow, a workflow that was being developed but never released.
![Cleanup filter example](/docs/resources/foundry/ontology-manager/cleanup-filter-example.png)
使用内联复选框选择三个 object types。

Select the three object types using the in-line checkboxes.
管理这些 object types 有三个选项:

There are three options for managing these object types:
* **Snooze:** 将 object types 从您的清理队列中隐藏一段可配置的时间。Snoozing 是一个仅影响执行该操作的用户的 action。

* **Deprecate:** 在每个显示 object type 状态的上下文中,将 object types 标记为已弃用。此选项通知用户迁移到不同的 object types,或标记该 object type 仍然有用。您可以设置一个弃用截止日期,以便用户知道他们有多长时间可以停止使用这些 object types。

* **Delete:** 从 Ontology 中删除 object types,并从 object storage 中删除相关数据。

* **Snooze:** Hide object types from your cleanup queue for a configurable amount of time. Snoozing is an action that will affect only the user that performs it.
* **Deprecate:** Show object types as deprecated in every context that displays object type status. This option informs users to move to different object types or flag that the object type is still useful. You can set a deadline along with a deprecation so users know how long they have to refrain from using these object types.
* **Delete:** Delete object types from the Ontology and remove associated data from object storage.
一旦您对队列中的 object type 执行了操作,它就会从队列中消失。使用表过滤器查看您已选择的所有 actions。

Once you act on an object type in your queue, it disappears from the queue. Use the table filters to view all the actions you have already selected.
Deprecation 和 deletion 的暂存方式与正常的 Ontology 修改相同。在上面的示例中,"Work Item" object type 包含带有用户编辑的 objects,因此可以将其弃用,而其他两个可以删除。点击右上角的 **Save** 可以将更改直接保存到 Ontology,或创建一个 proposal 以请求其他用户进行审核。

Deprecation and deletion are staged the same way as normal Ontology modifications. In the example above, the “Work Item” object type has objects with user edits, so it can be deprecated, while the other two deleted. Selecting **Save** in the top right enables saving the changes directly to the Ontology or creating a proposal to request review from another user.
![Cleanup staging example](/docs/resources/foundry/ontology-manager/cleanup-staging-example.png)
## Configure Ontology cleanup
Cleanup 页面包含一个子页面,允许您自定义使用的 flags 及其各自的优先级。

The cleanup page contains a subpage that allows you to customize the flags used and their respective priority.
![Cleanup configuration navigation](/docs/resources/foundry/ontology-manager/cleanup-configuration-navigation.png)
您可以在此页面上配置 flag 设置,选择使用默认设置或自定义 flags。

You can configure flag settings on this page, with a choice of using either the default set or custom flags.
![Cleanup configuration view](/docs/resources/foundry/ontology-manager/cleanup-configuration-view.png)
与从队列中 snooze object types 一样,这是一个不影响其他 Ontology 编辑器的个人自定义设置。

Like snoozing object types from the queue, this is an individual customization that does not affect other Ontology editors.
当您保存更改并返回主 **Cleanup** 选项卡时,系统将提示您重新计算 cleanup 队列。

When you save changes and return to the main **Cleanup** tab, you will be prompted to recalculate the cleanup queue.
请注意,如果使用自定义 flag 设置,将来添加的新 flags 在使用默认 flags 集时如果已启用,不会自动启用。

Note that if using a custom flag setup, new flags that get added in the future will not be automatically turned on if they are turned on when using the default set of flags.
## Ontology cleanup flags
以下 flags 列表旨在回答常见问题,但并不详尽:

The following list of flags is aimed at answering common issues, but is not exhaustive:
* **Past deprecation date:** Object type 当前具有 `deprecated` 状态,且弃用日期字段已过期。

* **Trashed datasource:** 支撑此 object type 的任何 datasource(无论是 dataset、restricted view 还是其他)已在 Compass 中被删除。

* **Datasource not updated in \[x] days:** 通过 Compass 检查支撑 datasource 的最后修改时间。

* **Description missing:** Object type 的描述为空。不会检查 object type 所有 properties 的描述。

* **Display name regex matches string:** 默认值 `\[test|deprecated\]` 将匹配 display name 中包含 `[test]` 或 `[deprecated]` 的 object types。例如,如果您的 Organization 的常见模式是使用前缀 `UAT -` 或 `Testing -` 标记处于用户验收测试中的 object types,则可以使用正则表达式 `UAT -|Testing -` 来查找所有匹配此模式的 object types。支持 ECMA (JavaScript) 正则表达式语法。

* **Phonograph deindexed:** 此 flag 仅应用于 Object Storage V1 中的 object types。Object Storage V2 没有等效的检查。

* **Past deprecation date:** Object type currently has the `deprecated` status and the deprecation date field is in the past.
* **Trashed datasource:** Any datasource (whether dataset, restricted view, or other) backing this object type has been trashed in Compass.
* **Datasource not updated in \[x] days:** Checks with Compass the time of the last modification to the backing datasource.
* **Description missing:** The object type has a blank description. Does not check for descriptions on all properties of the object type.
* **Display name regex matches string:** The default value of `\[test|deprecated\]` would match object types that have `[test]` or `[deprecated]` in their display names. For example, if a common pattern at your Organization is to mark object types in user acceptance testing with the prefix `UAT -` or `Testing -`, you would use the regex `UAT -|Testing -` to find all object types matching this pattern. Supports ECMA (JavaScript) regex syntax.
* **Phonograph deindexed:** Flag only applied to object types in Object Storage V1. There is no equivalent check for Object Storage V2.