<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/type-groups/
---
# Object type groups
Object type groups 是一种分类原语，帮助用户更好地搜索和探索其 Ontology。Groups 通过 Ontology Manager 创建和管理，通常由 Ontology [owners and editors](/docs/foundry/object-link-types/type-groups/#group-permissions) 完成。

Object type groups are a classification primitive that help users better search and explore their ontology. Groups are created and managed using Ontology Manager, generally by ontology [owners and editors](/docs/foundry/object-link-types/type-groups/#group-permissions).
## Group configuration
Groups 通过 groups 菜单创建和管理，可在 Ontology Manager 侧边栏中访问。

Groups are created and managed via the groups menu, accessible in the Ontology Manager sidebar.
![Choose or add a new group](/docs/resources/foundry/object-link-types/groups-menu.png)
也可以通过在 object type 概览页面中选择 **Edit groups** 直接将 groups 添加到 object type。

Groups can also be added directly to object types by selecting **Edit groups** in the object type overview page.
![add a group to an object type](/docs/resources/foundry/object-link-types/group-add-to-object.png)
## Group search and discovery
Groups 可以在 [Ontology Manager 的 **Search** 栏和 **Search** 栏对话框](/docs/foundry/ontology-manager/navigation/#header-search-bar) 中搜索。Ontology Manager 中的 object type 表格支持按 group 进行显示和过滤。Groups 也会显示在 [Object Explorer 主页](/docs/foundry/object-explorer/getting-started/#group-exploration-b-c-d) 上。

Groups are searchable in [Ontology Manager's **Search** bar and **Search** bar dialog](/docs/foundry/ontology-manager/navigation/#header-search-bar). The table of object types in Ontology Manager supports displaying and filtering by group. Groups are also displayed on the [Object Explorer home page](/docs/foundry/object-explorer/getting-started/#group-exploration-b-c-d).
![Filter By Group](/docs/resources/foundry/object-link-types/object-type-groups-add.png)
## Group permissions
要查看 object type groups，用户必须对包含该 object type group 的项目拥有 **viewer** 权限。

To view object type groups, users must have **viewer** permission on the project that the object type group is in.
## Legacy group migration
截至 2024 年 5 月 22 日，本页所描述的 *group* 原语已取代旧版 groups 中基于 tag 的系统。

As of May 22, 2024, the *group* primitive described on this page has replaced the tag-based system of legacy groups.
在大多数情况下，遗留 groups 在此时已自动迁移为 object type groups。如果需要手动操作，Ontology 所有者会通过 Upgrade Assistant 干预收到通知。

In most cases, legacy groups were automatically migrated to object type groups at this time. Ontology owners were notified via an Upgrade Assistant intervention if manual action was necessary.
### Group name visibility
以前，如果某个 group 内的所有 object types 对某个用户不可发现（例如，由于底层 datasets 的访问控制），则该 group 对该用户也不可发现。正如上文关于 [group permissions](/docs/foundry/object-link-types/type-groups/#group-permissions) 部分所述，所有 groups 现在将对任何可以查看 ontology 的用户可发现。此更改使 group 可见性与其他 [ontology primitives](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) 保持一致，以提高治理中的清晰度和透明度。

Previously, if all object types inside a group were non-discoverable to a certain user (for example, due to access controls on backing datasets), the group was also non-discoverable to the user. As mentioned in the section above on [group permissions](/docs/foundry/object-link-types/type-groups/#group-permissions), all groups will now be discoverable to any user that can view the ontology. This change aligns group visibility with other [ontology primitives](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) to increase clarity and transparency in governance.
### Migration of partially visible groups
对一个或多个用户不可发现的遗留 groups 没有资格进行自动迁移。在这些情况下，Ontology 所有者会通过 Upgrade Assistant 干预收到通知，告知需要手动操作。

Legacy groups that were not discoverable to one or more users were not eligible for automatic migration. In these cases, ontology owners were notified via an Upgrade Assistant intervention that manual action was necessary.
2024 年 5 月 22 日，无法安全迁移的遗留 groups 在所有应用程序（例如 Workshop 和 Object Explorer）中对运营用户隐藏。为了提供向后兼容性，遗留 groups 的名称仍作为 [type class metadata](/docs/foundry/object-link-types/metadata-typeclasses/) 存储在 object types 上。

On May 22 2024, legacy groups that could not be safely migrated were hidden from operational users across all applications such as Workshop and Object Explorer. To provide backward compatibility, the names of legacy groups remain stored as [type class metadata](/docs/foundry/object-link-types/metadata-typeclasses/) on object types.
Ontology 所有者可以继续使用 Ontology Manager 手动迁移这些隐藏的遗留 groups。为此，请导航至左下角的 **Ontology Configuration** 菜单，然后选择 **Approve all Groups for migration**。

Ontology owners may continue to manually migrate these hidden, legacy groups using Ontology Manager. To do this, navigate to the **Ontology Configuration** menu in the bottom left corner and select **Approve all Groups for migration**.