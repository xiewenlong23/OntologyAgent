<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/ontology-migration/
---
# Migrate ontological resource between Ontologies
每个 Ontology 资源都会自动链接到其创建的 Ontology 中。创建之后，资源可以在不同的 Ontology 之间移动。在 Ontology 之间迁移资源会更改资源上的权限，但不会影响底层数据和输入 datasource 上的权限。在 Ontology 之间迁移 Object 时，默认情况下所有编辑都会被保留。

Every ontology resource is automatically linked to the ontology it is created in. After their creation, resources can be moved between ontologies. Migrating resources between ontologies also changes the permissions on the resources, however, it does not impact the permissions on the underlying data and the input datasources. When migrating objects between Ontologies all edits will be preserved by default.
要将资源从一个 Ontology 迁移到另一个 Ontology，请执行以下操作：

To migrate resources from one ontology to another, do the following:
1. 通过位于 **Ontology Manager** 右上角的 Ontology 切换器导航到拥有该资源的 Ontology。

![Ontology 选择下拉菜单的截图。](/docs/resources/foundry/ontologies/ontology-switcher.png)

1. Navigate to the ontology that owns the resource via the Ontology switcher located in the top right corner in the **Ontology Manager**.

![Screenshot of ontology selection dropdown menu.](/docs/resources/foundry/ontologies/ontology-switcher.png)

2. 在同一 Ontology 中选择 **Migrate resources** 以启动迁移流程。然后，使用顶部的 Ontology 选择下拉菜单选择目标 Ontology。

![Ontology 迁移目标选择的截图。](/docs/resources/foundry/ontologies/ontology-migration-switcher.png)

2. Select **Migrate resources** in the same ontology to start the migration process. Then, select the target ontology in the top row using the ontology selection dropdown menu.

![Screenshot of ontology migration target selection.](/docs/resources/foundry/ontologies/ontology-migration-switcher.png)

3. 选择要迁移的 Object Type、Link Type、Action Type 和 Workflow。将在当前 Ontology（左侧）和目标 Ontology（右侧）中显示要迁移资源选择的预览。请注意，除非 Object Type 最初是在默认 Ontology 中创建的，否则无法将 Object Type 从私有 Ontology 迁移到默认 Ontology。

![Ontology 迁移对话框的截图。](/docs/resources/foundry/ontologies/ontology-migration.png)

3. Select the object types, link types, action types, and workflows to migrate. A preview of the selection of resources to be migrated are shown in their current ontology (left) and in the target ontology (right). Note that it is impossible to migrate object types from a private ontology to the default ontology unless the object type was originally created in the default ontology.

![Screenshot of ontology migration dialog.](/docs/resources/foundry/ontologies/ontology-migration.png)

> **⚠️ 警告: 迁移到默认 Ontology**

> 请确保同时迁移相互关联的资源。如果所选内容中缺少相关的 Ontology 资源，则迁移会失败。
> **⚠️ 警告: Migrating to default ontology**

> Make sure that you are migrating connected resources together. The migration fails if related ontological resources are missing in the selection.
4. 完成选择后，选择 **Submit** 来迁移资源。

4. After completing the selection, select **Submit** to migrate the resources.