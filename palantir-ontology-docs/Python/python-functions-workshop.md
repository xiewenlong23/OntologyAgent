<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-functions-workshop/
---
# Use a Python function in Workshop
## Prerequisites
本指南假设您已经编写并发布了一个 Python function。请参阅 [Python functions 入门](/docs/foundry/functions/python-getting-started/) 文档以获取教程。有关如何使用 Python SDK 查询 Ontology 的示例，请参阅 [Python Ontology SDK 文档](/docs/foundry/ontology-sdk/python-osdk/)。

This guide assumes you have already authored and published a Python function. Review the [getting started with Python functions](/docs/foundry/functions/python-getting-started/) documentation for a tutorial. For examples of how to query the Ontology using the Python SDK, see the [Python Ontology SDK documentation](/docs/foundry/ontology-sdk/python-osdk/).
## Use the Python function in Workshop
在 Workshop 中，从模块左侧的 **Variables** 标签页搜索 Python function。[Serverless 和 deployed functions](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) 都会在此处显示。Serverless function 始终可以在任何版本下运行，无需手动部署。Deployed function 将在 function 和 function 版本上显示一个包含三种状态之一的图标：

In Workshop, search for the Python function from the **Variables** tab to the left side of the module. Both [serverless and deployed functions](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) will appear here. Serverless functions can always be run at any version and do not need to be manually deployed. Deployed functions will show an icon with one of three states for both the function and the function version:
* **Running：** 此 function 和版本可以处理请求。

* **Stopped：** 此 function 和版本不可用。在 function 选择器中，将鼠标悬停在信息图标上，选择 **Configure**，然后选择 **Create and start deployment** 以使 function 可用。

* **Upgrading：** 此 function 和版本尚不可用。

* **Running:** This function and version can serve requests.
* **Stopped:** This function and version are not available. In the function selector, hover over the information icon, select **Configure** and then **Create and start deployment** to make the function available.
* **Upgrading:** This function and version are not yet available.

> 📷 **[图片: A Python function in Workshop]**

> 📷 **[图片: A Python function in Workshop]**

### Cut a new release
任何时刻，function 的代码仓库只有一个版本在运行。如需在最小化停机时间的前提下修改 function，我们建议添加一个新 function（例如 `function_v1`）并在其中进行修改，然后按照 [此处](/docs/foundry/functions/python-getting-started/#commit-and-publish-a-function) 的说明进行 tag 标记。在已发布 function 的 tags 和 releases 列表中，选择 **Open in Ontology Manager**。

Only one version of the function’s repository is hosted at a given time. To make changes to functions with limited downtime we recommend adding a new function (like `function_v1`) with the changes and tagging as described [here](/docs/foundry/functions/python-getting-started/#commit-and-publish-a-function). From your published functions under tags and releases, select **Open in Ontology Manager**.
在 Ontology Manager 中，选择要在应用中使用的 function 仓库版本，然后选择 **Upgrade**。

In Ontology Manager, select the version of the function repository you want to use in applications, then select **Upgrade**.

> 📷 **[图片: Upgrade deployed function]**

> 📷 **[图片: Upgrade deployed function]**

将该代码仓库下游所有正在使用 function 的应用更新到您已部署的新版本。请注意，之前的部署版本将不再运行，因此在更新过程中应用会有一小段停机时间。`function_v0` 和 `function_v1` 会同时存在，因此您虽然需要切换到新的部署版本，但无需更改正在使用的 function。当 `function_v0` 不再被使用时，您可以将其删除。

Update all downstream applications using functions from this repository to the new version you have deployed. Note that the previous deployment version will no longer be running so your applications will have a short downtime as you make this change. You will have `function_v0` and `function_v1` available at the same time so while you need to switch to the new deployment version, you do not have to change the function you are using. When `function_v0` is no longer used, you can delete the function.
### Debug errors
如果 function 在 Workshop 中未按预期运行，首先检查问题是否与 function 的逻辑或响应能力有关。如果存在逻辑问题，请检查后端代码仓库中的源代码。如果 function 出现无响应或抛出错误的问题，请按照以下步骤操作：

If your function is not working as expected in Workshop, first check if the issue is related to the logic or the responsiveness of the function. If there is an issue with the logic, inspect the source code in the backing code repository. If there is an issue with the function being unresponsive or throwing an error, follow the steps below:
1. 检查 function 选择器下拉菜单中选择的版本当前是否正在运行。

1. Check if the version you selected is currently running in the function selector dropdown menu.

> 📷 **[图片: Workshop function version selector.]**

> 📷 **[图片: Workshop function version selector.]**

2. 如果 function 未部署或状态为 `Upgrading`，将鼠标悬停在 function 的信息图标上并选择 **Configure**。这将带您进入 Ontology Manager，在其中可以选择 **Start Deployment** 以使 function 重新运行。

2. If the function is not deployed or `Upgrading`, hover over the function’s information icon and select **Configure**. This will take you to Ontology Manager where you can select **Start Deployment** to get your function running again.

> 📷 **[图片: Information about Python function version.]**

> 📷 **[图片: Information about Python function version.]**

3. 如果您的 function 状态为 `Running`，或您需要更多关于部署行为的信息，请在 Ontology Manager 中从左侧面板选择 **Deployment** 以查看详细日志。如果您选择 **View live**，还可以查看 SLS logs。

3. If your function is `Running` or you need more information about the deployment’s behavior, select **Deployment** from the left panel in Ontology Manager to view detailed logs. SLS logs are also available if you select **View live**.

> 📷 **[图片: View deployment logs in Ontology Manager.]**

> 📷 **[图片: View deployment logs in Ontology Manager.]**

## Create a function-backed column
要创建一个 function-backed 列，您必须发布一个满足以下要求的 function：

To create a function-backed column, you must publish a function that meets the following requirements:
* function 的输入参数必须包含一个 object set 参数（从 `ontology_sdk.ontology.object_sets` 导入），也可以选择性地包含其他输入参数。该 object set 参数将使得表格中显示的 objects 能够被传递到 function 中，从而生成所需的派生列。请注意，`list[ObjectType]` 参数在此场景下也可以使用，但该选项性能较差，不推荐使用。

* The function's input parameters must include an object set parameter (imported from `ontology_sdk.ontology.object_sets`) and can optionally include other input parameters. This object set parameter will enable the objects displayed in the table to be passed into the function to then generate the desired derived column. Note that a `list[ObjectType]` parameter will also work here, but this less performant option is not recommended.
* function 的返回类型必须是 `dict[ObjectType, ColumnType]`，其中 `ColumnType` 是该列所需的 [type](/docs/foundry/functions/types-reference/#types-reference)；或者使用 `dict[ObjectType, CustomType]` 以从 function 返回多个列。了解更多关于 [custom types](/docs/foundry/functions/types-reference/#structcustom-type) 的信息。

* The function's return type must be `dict[ObjectType, ColumnType]`, where `ColumnType` is the desired [type](/docs/foundry/functions/types-reference/#types-reference) for the column, or `dict[ObjectType, CustomType]` to return multiple columns from the function. Learn more about [custom types](/docs/foundry/functions/types-reference/#structcustom-type).
一旦满足上述条件的 function 被配置并发布后，您就可以在 [Object Table](/docs/foundry/workshop/widgets-object-table/#features-of-function-backed-properties) widget 配置中配置一个 function-backed property 列。

Once a function that meets the above criteria is configured and published, you can configure a function-backed property column within the [Object Table](/docs/foundry/workshop/widgets-object-table/#features-of-function-backed-properties) widget configuration.
一个返回单列的函数示例：

An example of a function returning one column:
```python
from functions.api import Date, Integer, String, function
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.object_sets import MyObjectTypeObjectSet
from ontology_sdk.ontology.objects import MyObjectType

@function
def function_backed_column_single_col(
selected_objects: MyObjectTypeObjectSet
) -> dict[MyObjectType, Integer]:
final_dict = {}

for curr_obj in selected_objects:
final_dict[curr_obj] = 10 # The value can be defined for any arbitrary logic

return final_dict
```
![An example of a function returning one column.](/docs/resources/foundry/functions/python-functions-advanced-single.png)
一个返回多列的函数示例：

An example of a function returning multiple columns:
```python
from dataclasses import dataclass

@dataclass
class CustomType:
column_name_a: int
column_name_b: int

@function
def function_backed_column_multiple_cols(
selected_objects: MyObjectTypeObjectSet, some_other_parameter: String
) -> dict[MyObjectType, CustomType]:
final_dict = {}

for curr_obj in selected_objects:
final_dict[curr_obj] = CustomType(column_name_a=10, column_name_b=20)

return final_dict

```
![An example of a function returning multiple columns.](/docs/resources/foundry/functions/python-functions-advanced-multiple.png)