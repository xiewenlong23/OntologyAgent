<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/foo-getting-started/
---
# Getting started with functions on objects
Functions 的核心特性之一是它们可以轻松访问已集成到 Foundry Ontology 中的数据。Ontology 为您的组织提供数据的语义建模，使得跨用例访问结构化数据和复用逻辑变得非常容易。

One of core features of functions is they can easily access data that has been integrated into the Foundry Ontology. The Ontology provides semantic modeling of data for your organization, which makes it easy to access structured data and reuse logic across use cases.
> **ℹ️ 注意: 先决条件**

> 本教程假定您已经创建并设置了一个 TypeScript 仓库。如果您还没有，请先完成 [Getting started](/docs/foundry/functions/getting-started/) 教程。
> **ℹ️ 注意: Prerequisites**

> This tutorial assumes that you have created and set up a TypeScript repository. If you haven't yet, complete the [Getting started](/docs/foundry/functions/getting-started/) tutorial first.
### Import Ontology types
您想在 function 中使用的任何 object、interface 或 link types 都必须导入到包含您仓库的 Project 中。选择 **Resource Imports** 侧边栏，即可查看已导入到 Project 中的 object types。

Any object, interface, or link types you want to use in your function must be imported into the Project that contains your repository. Selecting the **Resource Imports** side bar shows you the object types which have been imported into the Project.
![ontology-import-side-panel](/docs/resources/foundry/functions/ontology-import-side-panel.png)
> **ℹ️ 注意**

> 您的组织可能没有 Airport 和 Flight objects。在跟随操作时，请使用您有权访问的任何 object types。
> **ℹ️ 注意**

> Your organization may not have the Airport and Flight objects. Use any object types you have access to when following along.
若要导入其他 object types，您需要在 **Resource Imports** 侧边栏中选择 **Add** 按钮。如果尚未选择 Ontology，系统将提示您选择一个 Ontology。如果您已至少导入了一个 Ontology type，则所选的 Ontology 将自动解析。

To import additional object types, you will need to select the **Add** button in the **Resource Imports** side bar. If no Ontology has been selected you will be prompted to select an Ontology. If you have at least one imported Ontology type, the selected Ontology will automatically be resolved.
选择 Ontology 后，将出现一个搜索模态框。您的 Ontology 将取决于您组织中可用的 object types。首先选择几个 object types 以及连接它们的 link types。在本例中，我们将导入 Airport 和 Flight objects，以及它们之间的 link type。

Once an Ontology is selected, a search modal will appear. Your Ontology will depend on the object types available in your organization. Start by selecting a few object types and link types that connect them. In this example, we'll import the Airport and Flight objects, in addition to the link type between them.
![ontology-import-example](/docs/resources/foundry/functions/ontology-import-example.png)
选择 **Confirm selection** 将 Ontology types 导入到项目中。Code Assist 将自动重新启动，以重新生成代码绑定来反映您已导入的新 object 和 link types。

Choose **Confirm selection** to import the Ontology types into the project. Code Assist will automatically be restarted to regenerate code bindings to reflect the new object and link types you have imported.
在您的代码中，现在可以从 `@foundry/ontology-api` 包导入 Ontology types。如果您使用的是 private Ontology，则包名称将改为 `@foundry/ontology-api/<ontology-api-name>`。

In your code, you may now import Ontology types from the `@foundry/ontology-api` package. If you are using a private Ontology, the package name will instead be `@foundry/ontology-api/<ontology-api-name>`.
> **ℹ️ 注意: Private Ontologies**

> 如果您使用的是 private Ontology，请在以下所有示例中将 `@foundry/ontology-api` 替换为 `@foundry/ontology-api/your-private-ontology-api-name-here`。
> **ℹ️ 注意: Private Ontologies**

> If you are using a private Ontology, replace `@foundry/ontology-api` with `@foundry/ontology-api/your-private-ontology-api-name-here` in all the following examples.
### Add an object-backed function
接下来，让我们使用您刚刚导入的一个 object type 编写一个 function。您的代码将取决于您可用的 object types、properties 和 link types。切换回 **Code** 选项卡，尝试导入您刚刚添加的某个 object type：

Next, let's write a function using an object type you just imported. Your code will depend on the object types, properties, and link types available to you. Switch back to the **Code** tab, and try importing one of the object types you just added:
```typescript
import { Airport } from "@foundry/ontology-api";
```
然后，编写一个以该 object 作为输入的 function：

Then, write a function that takes that object as input:
```typescript
@Function()
public myObjectFunction(airport: Airport) {
airport.
}
```
一旦 Code Assist 启动，只需输入 `airport.` 即可查看可用的 properties 和 link types 的自动补全：

Once Code Assist has started, simply type `airport.` to see autocomplete for the properties and link types available to you:
![autocomplete](/docs/resources/foundry/functions/autocomplete.png)
在本例中，我们使用 [template string ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#syntax) 将 Airport 上的 `city` 和 `country` 字段组合成一个可读的位置信息：

In this example, we use a [template string ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#syntax) to combine the `city` and `country` fields on an Airport into a human-readable location:
```typescript
@Function()
public airportLocation(airport: Airport): string {
return `${airport.city}, ${airport.country}`;
}
```
根据您自己的 Ontology 试验这些 API，并编写一个根据您的 object type 返回值的 function。

Experiment with the APIs based on your own Ontology and write a function that returns a value based on your object type.
### Test in live preview
打开 **functions helper**,切换到 **Live Preview**,然后选择你在上面编写的 function。要在 live preview 中运行 object-backed function,你必须为该 object type 导入 backing datasource。请选择 **Run** 选项旁边的警告图标:

Open the **functions helper**, toggle to **Live Preview**, and choose the function that you wrote above. To run an object-backed function in live preview, you have to import the backing datasource for the object type. Select the warning icon next to the **Run** option:
![helper-datasource-import](/docs/resources/foundry/functions/helper-datasource-import.png)
然后,使用该对话框为你的 object types 导入 backing datasources:

Then, use the dialog to import the backing datasources for your object types:
![helper-datasource-import-dialog](/docs/resources/foundry/functions/helper-datasource-import-dialog.png)
导入 datasources 后,选择一个 object 并选择 **Run** 以查看结果:

After you've imported the datasources, choose an object and select **Run** to see results:
![helper-preview-run-foo](/docs/resources/foundry/functions/helper-preview-run-foo.png)
> **⚠️ 警告: Live preview permissions**

> Live preview 中 object types 的权限由 [TypeScript 仓库对每个 object type 底层 backing datasources 的权限](/docs/foundry/functions/permissions/#object-loading-permissions)决定。在测试 [用于创建通知的 functions](/docs/foundry/functions/configure-notifications/#configure-notifications) 时,不会强制执行接收者的权限。因此,一个创建通知的 function 在 live preview 中可能成功,但在 Foundry 其他地方的 action 中使用时可能会失败。
> **⚠️ 警告: Live preview permissions**

> The permissions on object types in live preview are determined by the [TypeScript repository's permissions on the backing datasources underlying each object type](/docs/foundry/functions/permissions/#object-loading-permissions). When testing [functions that create notifications](/docs/foundry/functions/configure-notifications/#configure-notifications), the recipients' permissions are not enforced. For this reason, a function that creates a notification may succeed in live preview but fail when used by an action elsewhere in Foundry.
> 了解更多关于 [为 actions 配置 notifications](/docs/foundry/action-types/notifications/) 的信息。
> Learn more about [configuring notifications for actions](/docs/foundry/action-types/notifications/).
### Publish the new function
通过提交你的代码并使用 **Branches** 选项卡发布新 tag 来发布新 function。一旦你的 function 已发布,你可以使用 **functions helper** 来测试它。

Publish the new function by committing your code and publishing a new tag using the **Branches** tab. Once your function has been published, you can test it using the **functions helper**.
![helper-run-foo](/docs/resources/foundry/functions/helper-run-foo.png)
function 发布后,你就可以开始在平台上的其他应用程序中使用它了。

After the function has been published, you can start using it in other applications throughout the platform.
### Next steps
本教程只是触及了 object functions 所能完成内容的表面。要了解更多信息,请参考以下资源:

This tutorial just scratches the surface of what you can do with functions on objects. To learn more, refer to these resources:
* 参考 [object API 文档](/docs/foundry/functions/api-objects-links/) 以了解你可以对 objects 执行哪些操作

* 阅读 [object Sets 文档](/docs/foundry/functions/api-object-sets/) 以了解按需搜索 objects 和 aggregations

* 了解 [在平台中使用 functions](/docs/foundry/functions/use-functions/) 的各种方式

* Refer to the [object API documentation](/docs/foundry/functions/api-objects-links/) to learn what you can do with objects
* Read the [object Sets documentation](/docs/foundry/functions/api-object-sets/) to learn about searching for objects and aggregations on-demand
* Learn about ways you can [use functions in the platform](/docs/foundry/functions/use-functions/)