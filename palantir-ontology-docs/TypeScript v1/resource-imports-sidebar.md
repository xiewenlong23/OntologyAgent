<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/resource-imports-sidebar/
---
# Import resources into Code Repositories
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更[强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 和可配置 resource requests 的支持，我们建议[迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
Code Repositories 中的 **Resource imports** 侧边栏提供了一个集中式 interface，用于在 TypeScript functions 仓库内管理已导入的 Foundry resources。该侧边栏允许您导入、移除以及查看各种 resources 的详细信息，包括 Ontology types、LMS language models、live deployments 以及外部系统（如 REST APIs）。

The **Resource imports** sidebar in Code Repositories offers a centralized interface to manage imported Foundry resources within your TypeScript functions repository. The sidebar allows you to import, remove, and view details of various resources, including Ontology types, LMS language models, live deployments, and external systems such as REST APIs.
![Resource Imports sidebar](/docs/resources/foundry/functions/resource-imports-sidebar.png)
## Select an Ontology
导入 object 和 link types 需要一个 Ontology。选择 Ontology：

An Ontology is required to import object and link types. To choose an Ontology:
1. 选择 **Add** 打开 resource 选择器菜单，然后选择 **Ontology** 开始导入 Ontology types。如果未选择任何 Ontology，将自动打开 Ontology 选择器对话框。

1. Choose **Add** to open the resource selector menu, and then choose **Ontology** to begin importing Ontology types. If no Ontology is selected, this will automatically open the Ontology selector dialog.
如果您已经导入了至少一个 Ontology type，则会自动选择该 type 所属的 Ontology。要更改 Ontology，请选择所选 Ontology 名称旁边的 **Edit** 按钮以打开 Ontology 选择器对话框。

If you have already imported at least one Ontology type, that type's Ontology is automatically selected. To change the Ontology, choose the **Edit** button next to the selected Ontology's name to open the Ontology selector dialog.
![Ontology selector dialog](/docs/resources/foundry/functions/sidebar-ontology-picker.png)
您仓库中所有导入的资源必须与同一个 Ontology 关联。请注意，在更改 Ontology 后导入资源将覆盖来自其他 Ontology 的任何现有导入。

All imported resources within your repository must be associated with the same Ontology. Note that importing resources after changing the Ontology will overwrite any existing imports from other Ontologies.
## Import resources
> **⚠️ 警告**

> 现代版本的 TypeScript v1 模板会在提交到您仓库的 `resources.json` 文件中维护仓库导入的当前状态。
> **⚠️ 警告**

> Modern versions of the TypeScript v1 template maintain the current state of repository imports in a `resources.json` file checked into your repository.
> 如果您在侧边栏中遇到关于无法解析文件的警告，请参阅 [file-based ontology imports](#file-based-repository-imports) 部分，了解有关预期文件格式以及解决该问题的故障排除步骤的信息。
> If you encounter warnings about an unresolvable file in the sidebar, see the [file-based ontology imports](#file-based-repository-imports) section for information about the expected file format and troubleshooting steps for resolving the issue.
要使用侧边栏导入资源：

To import resources using the sidebar:
1. 使用侧边栏右上角的 **Add** 按钮并选择所需的资源类型。这将打开该资源的选择器对话框。
2. 使用搜索栏和过滤器来定位您要导入的资源。
3. 选择一个资源以显示其包含详细信息的预览面板。

4. 使用 **Select** 按钮将资源添加到您的选择中。

5. 展开购物车面板以查看您的选择，并通过选择 **Confirm selection** 进行确认。

1. Use the **Add** button in the top right of the sidebar and select the desired resource type. This will open the selector dialog for that resource.
2. Use the search bar and filters to locate the resources you want to import.
3. Choose a resource to display its preview panel with detailed information.
4. Use the **Select** button to add resources to your selection.
5. Expand the cart panel to review your selection and confirm by choosing **Confirm selection**.
确认选择后，Code Assist 将重新启动，以重新运行必要的代码生成任务来应用您的更改。

After confirming your selection, Code Assist will be restarted to re-run the necessary code generation tasks to apply your changes.
![Example resource selector dialog](/docs/resources/foundry/functions/language-model-import-dialog.png)
了解更多关于导入特定类型资源的信息：

Learn more about importing resources of a specific type:
* [Ontology types](/docs/foundry/functions/ontology-imports/)
* [Language models](/docs/foundry/functions/language-models-python-tsv2/#import-a-language-model)
* [Live deployments](/docs/foundry/functions/functions-on-models/#import-a-live-deployment-in-a-repository)
* [External sources](/docs/foundry/functions/webhooks/)
* [Ontology types](/docs/foundry/functions/ontology-imports/)
* [Language models](/docs/foundry/functions/language-models-python-tsv2/#import-a-language-model)
* [Live deployments](/docs/foundry/functions/functions-on-models/#import-a-live-deployment-in-a-repository)
* [External sources](/docs/foundry/functions/webhooks/)
## Manage imported resources
资源在侧边栏中按类型分类：

Resources are categorized by type in the sidebar:
* Ontology：Object、Interface 和 Link Type

* Models：LMS 模型和 live deployment

* Sources：外部系统，例如 REST API

* Ontology: Object, interface, and link types
* Models: LMS models and live deployments
* Sources: External systems such as REST APIs
选择侧边栏顶部的相应资源图标以按类型进行过滤，或使用文本输入按名称搜索。要移除资源，请将鼠标悬停在资源图标上并选择 **Remove** 按钮。要同时添加或移除多个资源，请使用选择器对话框。要查看更多详细信息，请选择已导入的资源以打开其预览面板。

Choose the corresponding resource icon at the top of the sidebar to filter by type or use the text input to search by name. To remove a resource, hover over the resource icon and choose the **Remove** button. To add or remove multiple resources simultaneously, use a selector dialog. To view more details, select an imported resource to open its preview panel.
某些资源类型可能与其他资源之间存在依赖关系。例如，Link Type 是在其各自的 Object Type 下组织的。如果导入的资源具有依赖关系，则会在资源标题旁边显示一条消息，例如 "(1 link type)"。要查看资源的依赖关系，请将鼠标悬停在资源图标上并选择出现的箭头符号。

Some resource types may have dependencies between other resources. For instance, link types are organized under their respective object types. If an imported resource has dependencies, a message like "(1 link type)" will be displayed next to the resource title. To view a resource's dependencies, hover over the resource icon and select the chevron that appears.
![Resource Imports sidebar filter controls](/docs/resources/foundry/functions/resource-imports-sidebar-filters.png)
## Importing resources without API names
资源必须具有 API name 才能在 TypeScript Functions 仓库中的代码内被引用。如果资源缺少 API name，则会显示警告。将鼠标悬停在警告标志上以了解更多信息，或通过选择 **Add API name** 轻松配置 API name。或者，选择 **Learn more** 以查看有关为特定资源类型添加 API name 的文档。

Resources must have an API name to be referenced within code in TypeScript functions repositories. If a resource lacks an API name, a warning is displayed. Hover over the warning sign to learn more or easily configure an API name by choosing **Add API name**.  Alternatively, choose **Learn more** to see documentation about adding an API name tailored to the specific resource type.
![Resource Imports sidebar API name warning](/docs/resources/foundry/functions/resource-imports-sidebar-api-name-warning.png)
## Import resources with value type dependencies
某些资源依赖于 [value types](/docs/foundry/object-link-types/value-types-overview/) 来定义用于与其交互的数据类型，例如 function interface。对于这些资源，其 value type 依赖项会自动导入到仓库中，以便与该资源一起使用。

Some resources depend on [value types](/docs/foundry/object-link-types/value-types-overview/) to define the datatypes used to interact with them, for example, function interfaces. For these resources, their value type dependencies are imported into the repository automatically so that they are available to use along with the resource.
在某些情况下，导入此类资源的组合可能会导致 value type 依赖项冲突。当不同资源依赖于同一 value type 但版本不同时，就会发生这种情况。不可能同时导入同一 value type 的两个版本，这会导致编译错误。此错误会在侧边栏中伴随一条警告，使您能够查看具有冲突依赖项的资源。

In some cases, importing a combination of such resources can result in a value type dependency conflict. This occurs when different resources have a common value type they depend on at differing versions. It is not possible to have both versions of the same value type imported, and this causes a compilation error. This error is accompanied by a warning in the sidebar, allowing you to view the resources with conflicting dependencies.
![Value type conflicts warning](/docs/resources/foundry/functions/value-type-conflicts-warning.png)
## File-based repository imports
现代版本的 TypeScript v1 模板使用检入到您代码仓库中的 `resources.json` 文件来维护代码仓库导入的当前状态。这为您提供了完整的 Git 语义，使您能够 review、branch 和 revert 您的导入更改。资源导入侧边栏可通过自动将条目插入 `resources.json` 文件来帮助您更新此文件。

Modern versions of the TypeScript v1 template maintain the current state of repository imports using a `resources.json` file checked into your repository. This gives you full Git semantics, allowing you to review, branch, and revert changes to your imports. The resource import sidebar helps you update this file by automatically inserting entries into the `resources.json` file.
如果 `resources.json` 文件处于无效状态，侧边栏中将出现一条警告，通知您该文件无法处理。如果遇到此错误，请确保您的文件包含一个具有以下数据的 JSON 对象：

If the `resources.json` file is in an invalid state, a warning will appear in the sidebar informing you that the file cannot be processed. If you encounter this error, ensure that your file contains a single JSON object with the following data:
| Field                | Type                                        |
|----------------------|---------------------------------------------|
| `objectTypes`        | Array of `{ rid: string }`                  |
| `linkTypes`          | Array of `{ rid: string }`                  |
| `sources`            | Array of `{ rid: string }`                  |
| `functions`          | Array of `{ rid: string, version: string }` |
| `valueTypes`         | Array of `{ rid: string, version: string }` |
| `functionInterfaces` | Array of `{ rid: string, version: string }` |
| `_comment`           | String                                      |
| `version`\[1]         | Integer                                     |
\[1] `version` 字段用于表示 `resources.json` 文件的版本和格式。目前仅支持 `version: 1`。`version: 0` 用于表示您的代码仓库必须从之前的代码仓库范围导入工作流进行迁移。当提交包含 `version: 0` 时，此迁移将通过应用于您代码仓库的 patch 自动处理。

\[1] The `version` field is used to express the version and format of the `resources.json` file. Currently only `version: 1` is supported. `version: 0` is used to indicate that your repository must undergo a migration from the prior, repository-wide imports workflow. This migration is handled automatically with a patch applied to your repository when a commit with `version: 0` is made.
请注意，由于 `resources.json` 文件已检入到您的代码仓库，您可以查看 commit 历史记录并使用该历史记录将文件 revert 回工作状态。

Note that because the `resources.json` file is checked into your repository, you can view the commit history and use the history to revert the file back to a working state.
## Enable resource types
默认情况下，某些 resource type 可能未启用供您的代码仓库使用。已启用的 resource type 由您的 `functions.json` 文件确定。以下是典型默认 `functions.json` 文件的内容。

By default, some resource types may not be enabled for use in your repository. The enabled resource types are determined by your `functions.json` file. This is the contents of a typical default `functions.json` file.
```json
{
"useOntologyApiNames" : true,
"enableModelFunctions" : false,
"enableModelGraphFunctions" : false,
"enableDiscoverImproperOntologyAccess": false,
"enableQueries": false,
"enableModelMetadata": false,
"useDeploymentApiNames": true,
"enableVectorProperties": true,
"enableTimeSeriesProperties": false,
"enableExternalSystems": false,
"enableMediaReferenceProperties": false
}
```
如果在 `functions.json` 文件中未启用相应的 flag 就导入资源，可能会导致您的代码仓库中的 checks 失败。要使用导入的 live deployments，请将 `enableModelFunctions` 设置为 true。要使用导入的 sources，请将 `enableExternalSystems` 设置为 true。

Importing resources without enabling the corresponding flag in your `functions.json` file may cause checks to fail in your repository. To use imported live deployments, set `enableModelFunctions` to true. To use imported sources, set `enableExternalSystems` to true.