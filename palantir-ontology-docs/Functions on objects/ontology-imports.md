<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/ontology-imports/
---
# Import object, interface, and link types
您想在 function 中使用的任何 object、interface 或 link type 都必须导入到包含您代码仓库的 Project 中。选择 **Resource Imports** 侧边栏以查看已导入到该 Project 中的 object type。

Any object, interface, or link types you want to use in your function must be imported into the Project that contains your repository. Select the **Resource Imports** sidebar to view the object types which have been imported into the Project.
![ontology-import-side-panel](/docs/resources/foundry/functions/ontology-import-side-panel.png)
> **ℹ️ 注意**

> 您的 Organization 可能没有 `Airport` 和 `Flight` object。在执行这些步骤时,请使用您有权限访问的任何 object type。
> **ℹ️ 注意**

> Your Organization may not have the `Airport` and `Flight` objects. Use any object types you have access to when following these steps.
要导入其他 object type，您需要在 **Resource Imports** 侧边栏中选择 **Add** 按钮。如果未选择 ontology，系统将提示您选择一个 ontology。如果您已至少导入一个 ontology type，所选的 ontology 将自动被解析。

To import additional object types, you will need to select the **Add** button in the **Resource Imports** sidebar. If no ontology was selected, you will be prompted to select an ontology. If you have at least one imported ontology type, the selected ontology will automatically be resolved.
选择 ontology 后，将出现一个搜索模态框。您的 ontology 将取决于您 Organization 中可用的 object type。首先选择几个 object type 以及连接它们的 link type。在本例中，我们将导入 `Airport` 和 `Flight` object，以及它们之间的 link type。

Once an ontology is selected, a search modal will appear. Your ontology will depend on the object types available in your Organization. Start by selecting a few object types and link types that connect them. In this example, we'll import the `Airport` and `Flight` objects, in addition to the link type between them.
![ontology-import-example](/docs/resources/foundry/functions/ontology-import-example.png)
您也可以通过在 **Add** 按钮下选择 **Interfaces** 来导入 ontology interface。

You can also import ontology interfaces by selecting **Interfaces** under the **Add** button.
![The option to import interfaces under the "Add" dropdown.](/docs/resources/foundry/functions/interface-import-example.png)
选择 **Save** 将 ontology type 导入到 Project 中。Code Assist 将自动重启以重新生成代码绑定，从而反映您导入的新 object 和 link type。

Choose **Save** to import the ontology types into the Project. Code Assist will automatically restart to regenerate code bindings to reflect the new object and link types you imported.
在您的代码中，您现在可以从 `@foundry/ontology-api` 包中导入 ontology type。如果您使用的是私有 ontology，则包名称将改为 `@foundry/ontology-api/<ontology-api-name>`。

In your code, you may now import ontology types from the `@foundry/ontology-api` package. If you are using a private ontology, the package name will instead be `@foundry/ontology-api/<ontology-api-name>`.
Code Assist 启动后，您可以通过在 @foundry/ontology-api 包名称上使用 `Ctrl` + 点击来查看所有可用的 object type。打开的 index.ts 文件将显示您可以在代码中导入的所有有效 object type：

Once Code Assist starts, you can view all the available object types by using `Ctrl` + click on the @foundry/ontology-api package name. The open index.ts file shows all of the valid object types you can import into your code:
![ontology-api](/docs/resources/foundry/functions/ontology-api.png)
如果您有多个 ontology 的访问权限，可以使用选择器来选择您希望使用的 ontology。目前，不支持将多个 ontology 导入到单个 project 中。

If you have access to more than one ontology, you can use the selector to pick which ontology you would like to use. Currently, importing multiple ontologies into a single project is unsupported.