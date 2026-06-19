<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/permissions/
---
# Permissions
在平台中编写和执行 Functions 会涉及多种权限检查。本节概述了您需要了解的不同类型的权限以及可能遇到的常见问题。

Authoring and executing functions in the platform is subject to many kinds of permission checks. This section outlines the different types of permissions you should be aware of and common issues you may run into.
## Function authoring
必须为 Functions 仓库授予适当的权限，以便：

Functions repositories must be granted appropriate permissions to:
1. 访问 Ontology，以便能够生成正确的代码绑定。

2. 加载 Object 实例，以便运行 Function 执行的实时预览。

1. Access the Ontology so that proper code bindings can be generated.
2. Load objects in order to run a live preview of a function execution.
请注意，仓库权限必须显式授予，并且与授予您用户账户的权限不同。因此，您需要采取特定步骤将 Object Type、Link Type 和 backing datasource 导入到包含您仓库的 Project 中。

Note that repository permissions must be explicitly granted, and are not the same as the permissions granted to your user account. As a result, you have to take specific steps to import object types, link types, and backing datasources into the Project that contains your repository.
有关这些步骤的教程，请参阅 [this section](/docs/foundry/functions/ontology-imports/)。下面，我们将解释所导入的特定资源以及为这些资源授予的权限。

For a tutorial on these steps, see [this section](/docs/foundry/functions/ontology-imports/). Below, we explain the specific resources that are imported and the permissions granted for those resources.
### Ontology entity permissions
在仓库中，每当检查运行或 Code Assist 启动时，Functions 插件会根据仓库的权限加载最新的 Ontology，并为每个已加载的 Object Type 和 Link Type 生成代码绑定。加载的 Object Type 和 Link Type 集合取决于以下资源类型的导入情况：

In a repository, whenever checks run or Code Assist starts up, the functions plugins load the latest Ontology based on the repository’s permissions and generate code bindings for every object and link type that was loaded. The set of object and link types that are loaded depends on the imports of the following resource types:
* Ontologies
* Ontology branches
* [Object types](/docs/foundry/object-link-types/object-types-overview/)
* [Link types](/docs/foundry/object-link-types/link-types-overview/)
* Ontologies
* Ontology branches
* [Object types](/docs/foundry/object-link-types/object-types-overview/)
* [Link types](/docs/foundry/object-link-types/link-types-overview/)
在 Functions 仓库中，您可以通过导航到 **Settings** > **Ontology** 来导入所需的 Ontology 资源。此界面允许您选择要导入到 Project 中的 Object Type 和 Link Type。

In a functions repository, you can import the needed Ontology resources by navigating to **Settings** > **Ontology**. This interface allows you to choose object and link types to import into your Project.
![ontology-settings](/docs/resources/foundry/functions/ontology-settings-flights.png)
如果你的用户账户可以访问多个 Ontology，你也可以选择你想要使用的 Ontology。目前，不支持将多个 Ontology 导入到单个 Project 中。

If your user account has access to multiple Ontologies, you can also choose which Ontology you’d like to use. Currently, importing multiple Ontologies into a single Project is unsupported.
![ontology-picker](/docs/resources/foundry/functions/ontology-picker.png)
> **⚠️ 警告: Warning**

> 虽然上述 interface 出现在 functions repositories 中，但你导入的任何 Ontologies、object types 和 link types 都是在 **Project** 级别添加的。这意味着在一个 repository 中更改 imports 可能会影响同一 Project 中的其他 repositories。如果你希望拥有两个依赖于不同 Ontology 实体的 repositories，应将它们分离到不同的 Projects 中。
> **⚠️ 警告: Warning**

> Although the above interface shows up within functions repositories, any Ontologies, object types, and link types you import are added at the **Project** level. This means that changing imports in one repository can affect other repositories in the same Project. If you want to have two repositories that rely on different Ontology entities, you should separate them into different Projects.
### Object loading permissions
repository 中的 **functions helper** 允许用户通过两种方式执行 functions：通过执行已发布的 function，或在 live preview 中执行代码。在 live preview 中执行时，functions 代码会在 Code Assist 中编译并执行，Code Assist 是专为代码作者实现快速迭代而设计的基础设施。

The **functions helper** in a repository allows users to execute functions in two ways: by executing a published function, or by executing code in live preview. When executed in a live preview, functions code is compiled and executed in Code Assist, which is infrastructure designed to enable quick iteration for code authors.
由于它与 repository 关联，Code Assist 受到与代码生成相同的权限要求约束，如上所述。这意味着当在 live preview 中运行 function 时，你希望使用的每个 object type 的 backing datasources 必须导入到 Project 中。

Because it is tied to the repository, Code Assist is subject to the same permissions requirements as code generation, as described above. This means that when running a function in live preview, the backing datasources underlying each object type you wish to use must be imported into the Project.
在 functions helper 中，如果有 object types 导入到你的 Project 中，但没有导入相应的 datasource，则在 live preview 中会显示一条警告，提示你更新 imports：

In the functions helper, if there are object types imported into your Project without the corresponding datasource being imported, a warning will be displayed in live preview prompting you to update the imports:
![preview-backing-datasources](/docs/resources/foundry/functions/preview-backing-datasources.png)
对于大多数 object types，**Import backing datasources** 对话框会提示你导入一个 Foundry dataset。对于启用了 [row-level security](/docs/foundry/object-permissioning/configuring-rv-access-controls/) 的 object types，系统会提示你导入一个 [Restricted View](/docs/foundry/security/restricted-views/)。

In the case of most object types, the **Import backing datasources** dialog will prompt you to import a Foundry dataset. For object types that have [row-level security](/docs/foundry/object-permissioning/configuring-rv-access-controls/) enabled, you will be prompted to import a [Restricted View](/docs/foundry/security/restricted-views/).
## Published function execution
一旦 function 已发布，就可以被更广泛的用户使用，并可以配置为在 [Workshop](/docs/foundry/workshop/overview/) 和 [Actions](/docs/foundry/action-types/function-actions-overview/) 等应用程序中执行。在执行已发布的 function 的权限方面，仍有一些需要注意的事项。

Once a function has been published, it is ready for use by a broader audience of users and can be configured to execute in applications such as [Workshop](/docs/foundry/workshop/overview/) and [Actions](/docs/foundry/action-types/function-actions-overview/). There are still some considerations to keep in mind for permissions to execute a published function.
### Function permissions
为了执行 function，用户必须对发布该 function 的 repository 具有 **Viewer** 角色。通常，最佳做法是将 functions repositories 定位在与依赖该 repository 中 functions 的最终用户应用程序相同的 Project 中，无论这些应用程序是使用 Workshop、Slate 还是其他工具创建的。如果用户遇到指示他们缺乏读取 function 权限的错误（ReadFunctionsPermissionDenied），请检查他们是否对 repository 具有读取访问权限。[详细了解如何移动和共享资源。](/docs/foundry/compass/move-and-share-resources/)

In order to execute a function, a user must have **Viewer** role on the repository from which the function was published. Typically, it is best to locate functions repositories in the same Project as end-user applications that rely on functions in that repository, whether those applications are created using Workshop, Slate, or some other tool. If users encounter errors indicating that they lack permissions to read a function (ReadFunctionsPermissionDenied), check whether they have read access to the repository. [Learn more about how to move and share resources.](/docs/foundry/compass/move-and-share-resources/)
> **ℹ️ 注意**

> 侧边栏中的 **Check access** 面板可用于检查某人对 Workshop 或 Slate 应用程序的访问权限，包括对依赖 functions 的访问权限。有关更多信息，请参阅 [Check access 面板文档](/docs/foundry/security/checking-permissions/)。
> **ℹ️ 注意**

> The **Check access** panel in the sidebar can be used to check someone's access to a Workshop or Slate application, including access to dependent functions. For more information, see the [Check access panel documentation](/docs/foundry/security/checking-permissions/).
[Function-backed Actions](/docs/foundry/action-types/function-actions-overview/) 是一种特殊情况，其中最终用户不一定需要具有对 function 的读取访问权限即可应用使用它的 Action。管理员用户在配置 Action 以使用 function 时必须具有对 function 的读取访问权限。之后，用户将能够根据 [Action-level permissions](/docs/foundry/action-types/permissions/) 来应用 Action，而无需考虑其对 function 的访问权限。

[Function-backed Actions](/docs/foundry/action-types/function-actions-overview/) are a special case in which end users do not necessarily need read access to the function in order to apply an Action that uses it. An administrative user must have read access to a function when configuring an Action to use it. Afterwards, users will be able to apply the Action based on [Action-level permissions](/docs/foundry/action-types/permissions/), regardless of their access to the function.
### Object loading permissions
当 function 加载 object 数据时，无论是作为参数还是通过 [Object search](/docs/foundry/functions/api-object-sets/)，运行该 function 的最终用户的权限决定了加载哪些 objects。对于使用 row-level permissions 保护的 object types，这意味着执行同一 function 的不同用户可能会收到不同的结果。此行为是有意设计的——用户应只能看到他们有权访问的 objects，而此行为使得单个 function 能够适用于对单个 objects 具有不同访问权限的用户。

When a function loads object data, either as a parameter or via an [Object search](/docs/foundry/functions/api-object-sets/), the permissions of the end user running the function determine which objects are loaded. In the case of object types secured using row-level permissions, this means that different users executing the same function may receive different results. This behavior is intended—users should only see the objects they have access to, and this behavior enables a single function to work for users with differing access to individual objects.