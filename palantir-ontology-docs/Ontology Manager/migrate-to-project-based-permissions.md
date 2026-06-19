<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/migrate-to-project-based-permissions/
---
# Migrate to project-based permissions
Ontology 资源（包括 object types、action types、link types、interfaces 和 shared properties）可以保存在特定项目中，并自动继承这些项目的权限。Object 和 link 的实例权限仍依赖于 backing datasource 的位置。一旦完成迁移，查看、编辑和管理 ontology 资源的权限将通过 [Compass](/docs/foundry/compass/overview/)（Palantir 平台的 filesystem）进行管理。[Project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/) 取代了之前的 ontology roles 和 datasource-derived permissions 模型。这是用于所有其他资源类型的相同权限模型。

Ontology resources, including object types, action types, link types, interfaces, and shared properties, can be saved within specific projects and automatically inherit permissions from those projects. Object and link instance permissions remain dependent on the backing datasource location. Once migrated permissions to view, edit, and manage ontology resources are managed through [Compass](/docs/foundry/compass/overview/), the Palantir platform's filesystem. [Project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/) replaces the previous ontology roles and datasource-derived permissions models. This is the same permission model used for all other resource types.
你可以使用我们的迁移工具将现有的 ontology 资源迁移到 [project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/)。该工具会建议将 ontology 资源放置到合适的项目中，同时确保它们获得正确的权限。

You can migrate your existing ontology resources to [project-based permissions](/docs/foundry/object-permissioning/ontology-permissions/) using our migration tool. This tool suggests the placement of ontology resources into appropriate projects while ensuring they receive the correct permissions.
> **⚠️ 警告**

> 一旦资源已迁移到 project-based permissions，便无法还原为 ontology roles 或 datasource-derived permissions。
> **⚠️ 警告**

> Once a resource has been migrated to project-based permissions, it cannot be reverted to ontology roles or datasource-derived permissions.
要为新的 ontology 资源启用 project-permissioning，ontology 所有者可以导航到 Ontology Manager 中的 **Ontology configuration** 选项卡，并开启 **Require new ontology resources be saved in a project**。启用后，用户在创建新的 ontology 资源时将被提示选择保存位置。

To turn on project-permissioning for new ontology resources, ontology owners can navigate to the **Ontology configuration** tab in Ontology Manager and toggle on **Require new ontology resources be saved in a project**. Once enabled, users will be prompted to choose a save location when creating new ontology resources.
## Limitations
在开始之前，请注意以下限制：

Before starting, be aware of the following limitations:
* 此功能尚不适用于 Default ontologies。如果你不确定自己的 ontology 类型，请联系 Palantir Support。

* Ontology 资源名称必须符合 Compass 规范。不允许使用正斜杠（"/"），且不允许重复的名称。虽然 aliases 允许显示重复的名称，但系统会通过附加 "(1)" 来删除重复项以确保路径唯一。

* 每个 ontology 资源必须具有唯一的名称

* 示例：`common/utility-room` 因包含正斜杠而无效

* Ontology 的资源必须保存在与该 ontology 本身同一 space 内的项目中。

* This feature is not yet available for Default ontologies. Contact Palantir Support if you are not sure of your ontology type.
* Ontology resource names must conform to Compass conventions. Forward slashes ("/") are not allowed, and duplicate names are not permitted. While aliases allow duplicate names to be rendered, the system removes duplicates by appending "(1)" to ensure unique paths.
* Each ontology resource must have a unique name
* Example: `common/utility-room` is invalid due to the forward slash
* An Ontology's resources must be saved in a project within the same space as the ontology itself.
## Approaches to migration
在开始迁移之前，请考虑您希望如何组织您的 ontology 资源：

Before starting the migration, consider how you want to organize your ontology resources:
* **将 ontology 资源与 datasource 或 use case 项目保存在一起：** 将 ontology 资源与其对应的 datasource 放在一起，可以确保跨资源和实例的权限一致。这种方法允许您在一个地方为整个 use case 授予权限，确保正确的用户可以一起查看、编辑或管理所有组件。

* **Save ontology resources alongside datasources or in use case projects:** Keeping ontology resources next to their corresponding datasources ensures consistent permissions across resources and instances. This approach lets you grant permissions to the entire use case in one place, ensuring the right users can view, edit, or manage all components together.
* **将 ontology 资源保存在专用项目中：** 专门创建一个或多个独立的项目用于存放 ontology 资源。授予这些项目广泛的访问权限，使所有需要的人都可以查看 ontology 资源。

* **Save ontology resources in a dedicated project:** Create one or more separate projects specifically for ontology resources. Grant broad access to these projects to make ontology resources viewable to everyone who needs them.
* **混合方法：** 将核心 ontology 资源保存到所有人都具有查看权限的单个项目中。将 use case 特定的资源保存在 use case 特定的项目中。这可以防止 ontology 选择器和搜索界面因充斥着 use case 特定的 ontology 资源而变得杂乱。

* **Hybrid approach:** Save core ontology resources into a single project that everyone has permissions to view. Save use case specific resources in use case specific projects. This prevents ontology pickers and search screens becoming cluttered with use case specific ontology resources.
> **ℹ️ 注意**

> Ontology 资源的权限与 object 和 link 实例的权限是分开的。此迁移仅影响 ontology 资源的权限。Object 和 link 实例的权限仍基于其底层的 datasource 位置。
> **ℹ️ 注意**

> Ontology resources have separate permissions from object and link instances. This migration affects only ontology resource permissions. Object and link instances permissions remain based on the backing datasource location.
### How migration changes Marketplace installs
在您迁移到 project permissioning 之前，ontology 资源存放在 **Ontology service project** 中，这是一个系统管理的项目，用于在旧版权限模型下存放某个 ontology 的所有 ontology 资源。在 Ontology service project 中，每个用户对 ontology 资源都有一个默认的 **Viewer** 授权，并且这些资源不带有文件分类。当您安装 Marketplace 产品时，ontology 资源会被放入此 Ontology service project，而非 ontology 的文件则会被放入安装用户选择的目标项目：

Before you migrate to project permissioning, ontology resources live in the **Ontology service project**, a system-managed project that holds all ontology resources for an ontology under the legacy permission models. In the Ontology service project, every user has a default **Viewer** grant on ontology resources, and the resources do not carry file classifications. When you install a Marketplace product, the ontology resources are placed in this Ontology service project, while the non-ontology files are placed in the target project the installing user chooses:
![A Marketplace install places ontology resources in the Ontology service project on the target environment, while non-ontology files are placed in the target project.](/docs/resources/foundry/ontology-manager/marketplace-setup-prior-to-ontology-in-projects-migration.png)
在您迁移到 project permissioning 之后，同一产品会将 ontology 资源直接安装到所选的目标项目中，与其他文件放在一起，并且项目的角色授权和分类将适用于这些资源：

After you migrate to project permissioning, the same product installs the ontology resources directly into the chosen target project alongside the rest of the files, and the project's role grants and classifications apply to them:
![A Marketplace install places ontology resources in the chosen target project after migration.](/docs/resources/foundry/ontology-manager/marketplace-setup-after-migration-to-ontology-in-projects.png)
Ontology service project 为每个用户提供默认的 Viewer 授权且不带有任何分类，因此与迁移前相比，目标项目更严格的角色授权（以及它强制执行的任何强制标记或最高分类）可能会缩小已安装 ontology 资源的可见范围。如果希望 ontology 资源与产品中的其他文件具有不同的可见性，请将产品拆分为两个链接的 Marketplace 产品：一个包含 ontology 资源，安装到权限更宽松的项目中；另一个包含其余文件，安装到权限更严格的项目中。

The Ontology service project gives every user a default Viewer grant and carries no classifications, so the target project's tighter role grants — along with any mandatory markings or maximum classification it enforces — can narrow the visibility of installed ontology resources compared to before migration. To keep the ontology resources at a different visibility from the other files in the product, split the product into two linked Marketplace products: one containing the ontology resources, installed into a more permissive project, and a second containing the remaining files, installed into a more restricted project.
![A Marketplace product split into two linked products so that ontology resources and non-ontology files can install into projects with different visibility.](/docs/resources/foundry/ontology-manager/splitting-marketplace-product-into-two-products.png)
## Use the migration assistant (recommended)
迁移助手可帮助您快速识别适合您的 ontology 资源的项目和位置。

The migration assistant helps you quickly identify suitable projects and locations for your ontology resources.
**访问迁移助手的方法：** 选择您的 ontology，导航至 **Ontology configuration** 页面，然后在 **Migrations** 部分下选择 **Proceed to migration**。

**To access the migration assistant:** Select your ontology, navigate to the **Ontology configuration** page, and select **Proceed to migration** under the **Migrations** section.
![Navigate to the Ontology configuration page, then use the "Proceed to migration" option.](/docs/resources/foundry/ontology-manager/proceed-to-migration.png)
关于资源迁移目的地的强建议会被预选以加速您的工作流程，而较弱的建议则不会被选中以供您审阅。确认您的选择后，继续执行迁移。在最终确定之前，您可以创建必要的 imports 或取消该操作。

Strong recommendations for where to move resources are preselected to accelerate your workflow, while weaker suggestions remain unselected for your review. After confirming your selections, proceed with the migration. Before finalizing, you can create necessary imports or cancel the operation.
![The migration assistant preselects strong recommendations for your review.](/docs/resources/foundry/ontology-manager/migration-assistant-recommendations.png)
这些建议可帮助您更快、更明智地做出资源放置决策。如果没有可用的建议，您可以在迁移助手的 **Individual resources** 选项卡中手动选择位置。

These recommendations help you make faster, more informed decisions about resource placement. If no recommendations are available, you can manually select locations in the **Individual resources** tab of the migration assistant.
![Manually select locations to migrate individual resources.](/docs/resources/foundry/ontology-manager/migration-assistant-individual-resources.png)
## Migrate resources directly
您也可以不使用助手来迁移资源，这在您确切知道资源应放置的位置或希望快速迁移特定资源时非常有用。

You can also migrate resources without using the assistant, which is useful when you know exactly where resources should go or want to migrate specific resources quickly.
* **批量迁移多个资源：** 选择您的 ontology，然后从左侧边栏的 **Resources** 部分选择一种资源类型。选择要迁移的项，然后使用下拉菜单选择 **Project permission migration**。

![通过选择资源然后使用下拉菜单中的选项来批量迁移资源。](/docs/resources/foundry/ontology-manager/project-based-perm-bulk-res-migration.png)

* **Bulk migrate multiple resources:** Select your ontology, then choose a resource type from the **Resources** section in the left sidebar. Select the items to migrate, then use the dropdown menu to select **Project permission migration**.

![Migrate resources in bulk by selecting the resources and then using the option in the dropdown menu.](/docs/resources/foundry/ontology-manager/project-based-perm-bulk-res-migration.png)

* **迁移单个资源：** 打开一个 ontology 资源，使用 **Overview** 页面上的 **Actions** 下拉菜单选择 **Project permission migration**。

![使用下拉菜单迁移单个资源。](/docs/resources/foundry/ontology-manager/project-based-perm-individual-res-migration.png)
* **Migrate an individual resource:** Open an ontology resource and use the **Actions** dropdown menu on the **Overview** page to select **Project permission migration**.

![Migrate an individual resource using the dropdown menu.](/docs/resources/foundry/ontology-manager/project-based-perm-individual-res-migration.png)