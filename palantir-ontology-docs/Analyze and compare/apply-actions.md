<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/apply-actions/
---
# Apply Actions
在 Exploration 中，perspective 右上角的按钮将根据与您当前 object set 或选择的相关性对 actions 进行分类和列出。三个主要类别是用于数据回写的 **"Actions"**、用于将当前 exploration 带入其他平台应用程序的 **"Open In"**，以及用于将数据带出平台（例如导出到 Excel 电子表格）的 **"Export"**。

In an Exploration, buttons in the top right of the perspective will categorize and list actions with relevance to your current object set or selection. The three main categories are **“Actions”** for data writeback, **“Open In”** for bringing your current exploration to another platform application, and **“Export”** for bringing data out of the platform, such as to an Excel spreadsheet.
### Actions
在 Ontology 中配置的 [Action types](/docs/foundry/action-types/overview/) 将首先显示，并附带名称和描述。选择其中一个将打开一个表单，供您填写参数并提交 Action。您在 exploration 中当前选定的 object set（如果未选择任何对象，则为所有对象）会直接传递给该表单，因此只需配置其他参数。请注意，如果选定的 object 数量超过 1000，则 Actions 不可用。

[Action types](/docs/foundry/action-types/overview/) configured in the Ontology are displayed first with a name and description. Selecting one will open a form to allow you to fill in parameters and submit the Action. The current set of selected objects in your exploration (or all objects, if none are selected) is passed directly to the form, so only other parameters must be configured. Note that Actions are unavailable if the number of selected objects exceeds 1000.
Object Explorer 会使用相关的选定 object 预填 action 参数。如果对于预填哪个参数存在不确定性，则由用户自行决定，并且不提供任何预填值。

Object Explorer prefills action parameters with relevant selected objects. If there is uncertainty over which parameter to prefill, the decision is left to the user and no prefills are provided.
### Opening in other applications
如果有办法在另一个应用程序中打开您的当前结果集，它们将显示在 **"Open In"** 标题下。

If there are ways to open your current result set in another application, these will be displayed under the **"Open In"** heading.
### Export
导出对象集的方法（例如导出到 Excel 或将对象 ID 复制到剪贴板）会显示在这里。

Ways to export your object set, such as exporting to Excel or copying object IDs to your clipboard, appear here.