<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology-manager/export-import/
---
# Export, edit, and import an Ontology
> **ℹ️ 注意**

> 你不应依赖于导出的 JSON schema，因为它可能会随时间发生变化。
> **ℹ️ 注意**

> You should not depend on the exported JSON schema as it may change over time.
Ontology schema 定义存储在 [JSON 文件 ↗](https://en.wikipedia.org/wiki/JSON) 中。Ontology JSON 文件可以导出后使用代码编辑器或文本编辑器进行编辑，然后再导入回 Foundry。此导入/导出功能为高级用户提供了两种工作流程：

Ontology schema definitions are stored in a [JSON file ↗](https://en.wikipedia.org/wiki/JSON). An Ontology JSON file can be exported and edited with a code editor or text editor before being imported back into Foundry. This import/export functionality enables two workflows for advanced users:
* 如果你更喜欢在代码中进行 Ontology 编辑，可以通过导出 Ontology JSON 文件、直接在代码编辑器或文本编辑器中编辑该 JSON 文件，然后将修改后的 Ontology JSON 文件重新导入平台，从而绕过 Ontology Manager interface。

* 如果你想将一个 Ontology 的 working state 复制到另一个 Ontology，可以将该 Ontology 的当前状态导出为 JSON 文件，然后将复制的 JSON 重新导入平台（如有需要，可在代码编辑器中对 JSON 进行任何所需更改）。

* If you prefer to make Ontology edits in code, you can bypass the Ontology Manager interface by exporting the Ontology JSON file, editing the JSON file directly in a code editor or text editor, and then importing the modified Ontology JSON file back into the platform.
* If you’d like to copy the working state of one Ontology to another Ontology, you can export the Ontology’s current state as a JSON file and then import the copied JSON back into the platform (making any desired changes to the JSON in a code editor).
![Edit ontology JSON](/docs/resources/foundry/ontology-manager/import-export-edit-ontology-json.png)
## Export
你可以通过从应用程序主页选择 **Advanced** 设置页面，然后选择 **Export**，来导出你的 Ontology working state。

You can export your Ontology working state by selecting the **Advanced** settings page from the application’s home page and then selecting **Export**.
> **ℹ️ 注意**

> 你在 working state 中所做的任何更改都将包含在导出文件中。
> **ℹ️ 注意**

> Any changes you have in your working state will be included in the export.
## Import
你可以通过从应用程序主页选择 **Advanced** 设置页面，然后选择 **Import**，来导入之前导出的 Ontology working state。系统将提示你从本地驱动器中选择一个 Ontology 文件。

You can import a previously exported Ontology working state by selecting the **Advanced** settings page from the application’s home page and then selecting **Import**. You will be prompted to choose an Ontology file from your local drive.
接下来，选择 **Import**，这将从 JSON 文件在应用程序中重新创建整个 working state。你将在应用程序页头中看到文件中需要保存的更改数量。

Next, select **Import,** which will recreate the entire working state from the JSON file in the application. You will see the number of changes made in the file that need to be saved in the application header.
> **ℹ️ 注意**

> 具有在其 properties 上配置的 conditional formatting 规则的已导出 Ontology working state 无法导入到非导出来源的 Ontology 中。
> **ℹ️ 注意**

> An exported Ontology working state with conditional formatting rules configured on its properties cannot be imported to an Ontology other than the one it was exported from.
## Troubleshooting
### Error: `OntologyMetadata:UnreferencedRuleSets`
如果你收到错误 `OntologyMetadata:UnreferencedRuleSets`，则表示你正在尝试导入一个包含未在该 Ontology 中定义且无法传输的 conditional formatting 规则的 Ontology working state。你需要在导入之前从 Ontology working state 中删除这些 conditional formatting 规则。

If you receive the error `OntologyMetadata:UnreferencedRuleSets`, you are trying to import an Ontology working state with conditional formatting rules that are not defined in that Ontology and cannot be transferred over. You will need to delete the conditional formatting rules from the Ontology working state before importing.