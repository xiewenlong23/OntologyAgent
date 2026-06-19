<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/save-share/
---
# Save, share, and collaborate
有许多方法可以保存和共享您的 system graph 或 case study。

There are many ways to save and share your system graph or case study.
## Save a draft
在顶部工具栏中选择 **Save as** 将提示您将 graph 保存到相关的 Foundry 项目中。Graph 仅对有权访问其保存项目的用户可见。一旦首次保存草稿后，选择 **Save** 将更新其状态。

Selecting **Save as** on the top toolbar will prompt you to save a graph within a relevant Foundry project. A graph is only visible to those who have access to the project where it is saved. Once a draft has been saved for the first time, selecting **Save** will update the state.
如果您希望更广泛地共享此 graph，可以从顶部工具栏的 **Share** 菜单中开启 link sharing。通过此菜单，您可以选择允许用户在使用 share link 时拥有的相关权限角色。当其他人访问该链接时，您将在 **Roles** 下看到他们的用户名。

If you wish to share this graph more broadly, you can turn on link sharing from the **Share** menu in the top toolbar. From this menu, you can select the relevant permission role you want to allow users when using the share link. When others access the link you will see their usernames under **Roles**.
![Draft](/docs/resources/foundry/vertex/save_share_collaborate-draft.jpg)
共享 graph 不会授予用户访问其原本无权访问的任何其他资源的权限。在打开 graph 时，如果用户由于权限或数据被删除而无权访问 graph 中引用的任何 objects 或 time series，他们仍会看到 graph 的结构和形状。用户将看不到与 objects 相关的具体数据。

Sharing a graph will not grant users access to any other resources to which a user does not already have access. When opening a graph, if a user does not have access to any objects or time series referenced in the graph due to permissions or deleted data, they will still see the structure and shape of the graph. The user will not see the specific data pertaining to the objects.
## Duplicate existing graphs
如果您希望基于现有的 graph 进行工作，可以从 **Save** 下拉菜单中选择 **Duplicate**。此操作将提示您将 graph 的副本保存到您选择的新项目中。复制操作会创建一个新的 graph，您可以在不影响原始 graph 的情况下进行操作。

If you would like to work from an existing graph, you can select **Duplicate** from the dropdown **Save** menu. This action will prompt you to save a copy of the graph in a new project of your choice. Duplicating creates a new graph that you can work from without making changes to the original.
![Duplicate Graph](/docs/resources/foundry/vertex/save_share_collaborate-duplicate.jpg)
![Save](/docs/resources/foundry/vertex/save_share_collaborate-save.jpg)
## Version control
如果您希望跟踪 graph 随时间的变化，可以从 **Save** 下拉菜单中选择 **Enable versioning**。后续保存将创建 graph 的新版本。

If you would like to keep track of changes to your graph over time, you can select **Enable versioning** from the dropdown **Save** menu. Subsequent saves will create a new version of the graph.
![Enable Versioning](/docs/resources/foundry/vertex/enable_versioning.png)
完整的版本历史记录可以在 **Graph History** 侧边栏中查看。Graph 的先前版本可以以只读模式访问（当前版本号将显示在 resource header 中）。

A full version history can be viewed in the **Graph History** sidebar. Previous versions of the graph can be accessed in read-only mode (the current version number will be visible in the resource header).
![Graph History](/docs/resources/foundry/vertex/graph_history.png)
通过从 Graph History 侧边栏中选择 **Revert**，将创建一个新版本，其内容与所选版本相同。

By selecting **Revert** from the Graph History sidebar, a new version will be created with the same contents of the selected version.