<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions/
---
# Ontology permissions
对 ontology resources 的查看、编辑和管理权限是通过 [Compass](/docs/foundry/compass/overview/)（Palantir 平台的 filesystem）进行管理的。Ontology resources 保存在项目中，所选项目决定了谁可以查看、编辑和管理它们。

The permissions to view, edit, and manage ontology resources are managed through [Compass](/docs/foundry/compass/overview/), the Palantir platform's filesystem. Ontology resources are saved into a project, and the selected project determines who can view, edit, and manage them.
此能力对新 ontologies 默认启用。对于现有 ontologies，ontology owner 必须 [手动启用该能力，并且现有的 ontology resources 需要迁移](/docs/foundry/ontology-manager/migrate-to-project-based-permissions/)。此能力暂不适用于 Default Ontologies。如果您不确定自己的 ontology 类型，请联系 Palantir Support。

This capability is enabled for new ontologies. For existing ontologies, an ontology owner must [enable the capability manually, and existing ontology resources require migration](/docs/foundry/ontology-manager/migrate-to-project-based-permissions/). This capability is not yet available for Default Ontologies. If you are unsure of your ontology type, contact Palantir Support.
这种基于项目的权限管理方法取代了之前的权限模型：[ontology roles and datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/)。它带来了多项优势：

This project-based permissions approach replaces the previous permission models: [ontology roles and datasource-derived permissions](/docs/foundry/object-permissioning/ontology-permissions-legacy/). It comes with multiple benefits:
* **统一的权限模型：** Ontology resources 使用与其他资源类型相同的权限系统，因此您只需在一个地方学习和管理权限。
* **批量管理：** 在项目或文件夹级别设置权限，可一次性控制多个资源的访问，无需对单个资源分别设置权限。

* **权限可解释性：** **Security** 选项卡会显示查看和编辑 object type 所需的权限，以及查看实例或运行 actions 所需的权限。

* **额外的隐私控制：** 通过应用 marking 或将资源放置在用户缺乏角色授权的项目中，来隐藏敏感的 ontology resources。

* **Compass 策展原语：** 使用 portfolios 和 tags 来组织 ontology resources，并使用 role grants 或 markings 向用户隐藏不相关的资源。

* **Unified permission model:** Ontology resources use the same permission system as other resource types, so you only need to learn and manage permissions in one place.
* **Bulk management:** Set permissions at the project or folder level to control access across multiple resources at once, eliminating the need to set permissions on individual items.
* **Permissions explainability:** The **Security** tab displays the required permissions to view and edit an object type, and the required permissions to see instances or run actions.
* **Additional privacy controls:** Hide sensitive ontology resources by applying a marking or by placing them in a project where the user lacks a role grant.
* **Compass curation primitives:** Use portfolios and tags to organize ontology resources, and role grants or markings to hide irrelevant resources from users.
迁移到 projects 不会更改对 backing datasource 有访问权限的人员。要查看 objects，用户仍需同时拥有 object type 和 datasource 的权限。

Migrating to projects does not change who has access to the backing datasource. To see objects, users continue to need permissions on both the object type and the datasource.
## Example of project-based permission
考虑一个名为 `Building` 的 object type，它作为文件保存在项目 `A` 中。您查看、编辑或管理 `Building` 的能力取决于您在项目 `A` 中的角色。如果您是项目 `A` 中的 `Editor`，则可以编辑 `Building` object type。要查看特定的 `Building` objects（例如 `Empire State Building`），您需要 object type 上的 `Viewer` 角色，以及对 backing datasource 的访问权限，或通过 [object and property security policies](/docs/foundry/object-permissioning/managing-object-security/#object-and-property-security-policies) 授予的访问权限，具体取决于 object type 的安全配置方式。

Consider an object type called `Building` saved as a file in project `A`. Your ability to view, edit, or manage `Building` depends on your role in project `A`. If you are an `Editor` in project `A`, you can edit the `Building` object type. To view specific `Building` objects (like `Empire State Building`), you need the `Viewer` role on the object type and either access to the backing datasource or access granted through [object and property security policies](/docs/foundry/object-permissioning/managing-object-security/#object-and-property-security-policies), depending on how the object type's security is configured.
![Ontology resources in a project.](/docs/resources/foundry/object-permissioning/ontology-in-project.png)
如果您仅拥有 object type 的查看权限，则只能查看诸如 schema 和联系信息之类的信息，而无法查看实际数据。如果您需要帮助理解所需的权限，请查看 Compass 项目侧边栏。

If you only have viewing rights for the object type, you can only see information such as schema and contact information, not the actual data. If you need help understanding the permissions required, review the Compass project side panel.
## Viewing object types and objects
Object types 的权限管理与 objects 不同。要查看 object type，您必须拥有该 object type 的 View 权限，但无需 backing datasource 的 View 权限。

Object types are permissioned differently from objects. To see an object type, you must have View permissions on the object type, but do not need View permissions for the backing datasource.
要查看对象，您必须持有该 Object Type 的查看权限并具有对数据的访问权限。对底层数据的访问权限由 Object Type 的安全配置决定：

To see objects, you must hold View permissions on the object type and access to the data. Access to the underlying data is determined by the object type's security configuration:
* **[对象和属性安全策略](/docs/foundry/object-permissioning/managing-object-security/#object-and-property-security-policies)：** 对象可见性由直接配置在 Object Type 上的策略决定，与底层数据源的权限无关。

* **[数据源策略](/docs/foundry/object-permissioning/managing-object-security/#data-source-policies)：** 对象可见性由底层数据源的权限决定。您必须持有该底层数据源的查看权限才能查看对象。

* **[Object and property security policies](/docs/foundry/object-permissioning/managing-object-security/#object-and-property-security-policies):** Object visibility is governed by policies configured directly on the object type, independent of the backing datasource permissions.
* **[Data source policies](/docs/foundry/object-permissioning/managing-object-security/#data-source-policies):** Object visibility is governed by the permissions on the backing data source. You must hold View permissions on the backing data source to see the objects.
有关配置对象安全性的更多信息，请参阅 [对象安全性管理文档](/docs/foundry/object-permissioning/managing-object-security/)。有关 Object Type（schema）和对象（数据）之间区别的更多信息，请参阅 [对象权限文档](/docs/foundry/object-permissioning/overview/)。

For more information on configuring object security, review the [documentation on managing object security](/docs/foundry/object-permissioning/managing-object-security/). For more information on the distinction between object types (schema) and objects (data), review the [documentation on object permissions](/docs/foundry/object-permissioning/overview/).
当对象位于项目中时，必须将底层数据源导入到项目中，对象才能被索引。如果项目中尚无该底层数据源，在创建对象时系统会提示您进行导入。

When objects are in projects, the backing datasource must be imported into the project for the object to index. If the backing datasource is not already in the project, you are prompted to import it during object creation.
## Edit permissions for links and actions
根据您要编辑的资源，您需要具备相应的编辑权限：

You will need the appropriate edit permissions depending on the resource you would like to edit:
* **对于 Link：** 您必须同时持有 Link Type 以及相关 Object Type 的编辑权限。

* **对于 Action：** 您必须持有 Action Type 以及该 Action 所编辑的所有 ontology 资源类型的编辑权限。

* **For links:** You must hold edit permissions on both the link type and the linked object types.
* **For actions:** You must hold edit permissions on the action type and on all ontology resource types edited by the action.
## Packaging and installing with different permission models
Marketplace 产品使用与其打包时相同的权限模型进行安装。**Ontology configuration** 中的 **Require new ontology resources be saved in a project** 开关仅影响新 ontology 资源的创建——它不会改变 Marketplace 在 **target environment**（产品安装的环境）相对于 **source environment**（产品打包的环境）安装产品的方式。

A Marketplace product installs using the same permission model it was packaged with. The **Require new ontology resources be saved in a project** toggle in **Ontology configuration** only affects creation of new ontology resources — it does not change how Marketplace installs a product on the **target environment** (where the product is installed) relative to the **source environment** (where it was packaged).
* **使用 Ontology roles 打包：** 使用 Ontology roles 进行安装。
* **使用项目权限打包：** 使用项目权限进行安装。

* **发布后源已迁移到项目权限：** 下次升级时，目标环境的 ontology 资源将迁移到项目权限。

* **Packaged with Ontology roles:** installs using Ontology roles.
* **Packaged with project permissioning:** installs using project permissioning.
* **Source migrated to project permissioning after publishing:** the target's ontology resources are migrated to project permissioning on the next upgrade.
## Classification-based access controls (CBAC)
当 ontology 资源保存在由

[基于分类的访问控制 (CBAC)](/docs/foundry/security/classification-based-access-controls/)
管理的项目中时，适用以下规则：

When ontology resources are saved in projects governed by
[classification-based access controls (CBAC)](/docs/foundry/security/classification-based-access-controls/),
the following rules apply:
* 创建资源时，您必须指定一个文件分类。
* 文件分类必须等于或低于

[项目最大分类](/docs/foundry/security/classification-based-access-controls/#project-maximum-classification)。

* 如果未指定分类，Object Type 的物化将失败。

* You must specify a file classification when creating the resource.
* The file classification must be equal to or lower than the
[project maximum classification](/docs/foundry/security/classification-based-access-controls/#project-maximum-classification).
* Object type materializations fail if no classification is specified.
### Marketplace and file classifications
文件分类并非 ontology 专属——它们适用于所有文件。以下规则在此处单独列出，是因为它们会影响项目权限与 [基于分类的访问控制](/docs/foundry/security/classification-based-access-controls/) 的交互方式。Marketplace 不会在产品本身内部携带文件分类。

File classifications are not ontology-specific — they apply to all files. The rules below are called out here because they affect how project permissioning interacts with [classification-based access controls](/docs/foundry/security/classification-based-access-controls/). Marketplace does not carry file classifications inside the product itself.
* **发布时：** Marketplace 不跟踪文件分类。如果 Marketplace 存储的分类低于将要下放的任何分类，它会检查用户是否对这些标记持有 declassify 权限。

* **安装时：** 每个已安装的文件采用目标项目的分类。如果目标项目的分类低于 Marketplace 存储的分类，则安装用户必须对这些标记持有 declassify 权限。
* **升级时：** 文件分类不会更改。安装时设置的分类可以手动编辑，且这些手动编辑会在后续升级中保留。

* **At publish time:** Marketplace does not track file classifications. If the classification of the Marketplace store is lower than any of the classifications that will be dropped, it checks that the user has declassify permissions on those markings.
* **At install time:** each installed file takes the classification of the target project. If the target project's classification is lower than the classification of the Marketplace store, the installing user must hold declassify permissions on those markings.
* **On upgrade:** file classifications are not changed. The classifications set at install time can be edited manually, and those manual edits persist through later upgrades.
![Marketplace prompts for declassify permissions when the source and target project carry different classification markings.](/docs/resources/foundry/object-permissioning/ontology-in-projects-marketplace-file-classifications.png)
## Previous permission models
以前，ontology 资源的权限管理因 ontology 授权模型而异。下表总结了当前每种模型的资源管理方式。请参阅 [文档以了解有关这些旧版权限系统的更多信息](/docs/foundry/object-permissioning/ontology-permissions-legacy/)。

Previously, permissioning ontology resources varied based on your ontology authorization model. The table below summarizes how resources are currently managed for each model. Refer to the [documentation to learn more about these legacy permission systems](/docs/foundry/object-permissioning/ontology-permissions-legacy/).
| Legacy Ontology permission models | Description                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ontology roles**           | - Ontology resources are permissioned in Ontology Manager using ontology specific roles (Ontology `viewer`, Ontology `editor`, and Ontology `owner`). They are not a resource of a project.             |
| **Datasource-derived**       | - Ontology resources derive their permissions from the backing datasource of the object. For example, you have `editor` on the object type if and only if you are editor on the backing datasource. |