<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-functions-on-objects/
---
# Functions on objects
你可以使用 Python Ontology SDK 编写与 Ontology 交互的 functions。

You can write functions that interact with the Ontology using the Python Ontology SDK.
## Generate a Python Ontology SDK
若要生成 Python Ontology SDK 客户端，请导航到 [**Resource imports** sidebar](/docs/foundry/functions/resource-imports-sidebar/) 并选择

**Add > Ontology**。从那里，选择你所需的 Ontology，并导入你希望在 functions 中交互的任何 objects 和 links。保存以确认你的选择后，将出现一个横幅，提示相应的 OSDK 尚未创建。

To generate a Python Ontology SDK client, navigate to the [**Resource imports** sidebar](/docs/foundry/functions/resource-imports-sidebar/) and select
**Add > Ontology**. From there, select your desired Ontology and import any objects and links you would like to interact with in
your functions. After saving to confirm your selections, a banner will appear to indicate that a corresponding OSDK has not yet been created.
导航到 **SDK Generation** 标签页以生成并安装 OSDK。

Navigate to the **SDK Generation** tab to generate and install the OSDK.
![Create a new SDK.](/docs/resources/foundry/functions/python-sdk-create-new.png)
如果尚未生成 OSDK，系统将提示您为生成的包输入名称。
包名在生成第一个版本后无法更改。

If no OSDK has been generated, you will be prompted to enter a name for the generated package.
The package name cannot be changed after the first version has been generated.
选择 **Create new version** 后，您可以在此视图中监控生成进度。

After selecting **Create new version**, you can monitor the generation progress from this view.
![The SDK package being generated.](/docs/resources/foundry/functions/python-sdk-package-generating.png)
生成完成后，您需要使用

> 📷 **[图片: Install]**

按钮安装新生成的版本。

Once generation is complete, you will need to install the newly generated version with the

> 📷 **[图片: Install]**

button.
![The generated SDK package is ready to install.](/docs/resources/foundry/functions/python-sdk-package-ready-to-install.png)
这将在任务运行器面板中触发一个交互式安装。

一旦该任务成功完成（Task Runner 将显示 `BUILD SUCCESSFUL`），OSDK 的代码补全功能将在您的代码辅助会话中可用。

This will trigger an interactive install in the task runner panel.
Once that task completes successfully (the Task Runner will display `BUILD SUCCESSFUL`), code completion for the OSDK will be available in your code assist session.
`meta.yml` 文件也将被更新，以包含对生成包的引用。

您可以手动更新 `meta.yml` 而不使用安装助手，但如果您手动更新 `meta.yml`，则需要重新构建您的代码辅助会话以应用这些更改。

The `meta.yml` file will also be updated to include a reference to the generated package.
You can manually update `meta.yml` instead of using the installation helper, but if you manually update `meta.yml`, you will need to rebuild your code assist session to pick up the changes.
![The meta.yml includes the installed SDK package.](/docs/resources/foundry/functions/python-sdk-meta-yml-updated.png)
每当您在侧边栏中导入其他资源时，系统会提示您生成并安装包含这些资源的新版本 OSDK。

此外，如果您修改了已导入的资源（例如，向已导入的 Object Type 添加新 Property），则需要生成新的 OSDK 版本以应用这些更改。

Any time you import additional resources in the sidebar you will be prompted to generate and install a new version of the OSDK that includes these resources.
Additionally, if you modify imported resources (for instance, adding a new property to an already imported object type), you will need to generate a new OSDK version to pick up these changes.
## Examples
对于一个名为 `Aircraft` 的示例 Object Type，其 Property 为 `brand` 和 `capacity`，您可以编写一个接受 `Aircraft` 对象并对其进行汇总的 function，如下所示：

For an example object type named `Aircraft` with properties `brand` and `capacity`, you could write a
function that accepts an `Aircraft` object and summarizes it like so:
```python
from functions.api import function
from ontology_sdk.ontology.objects import Aircraft

@function
def aircraft_input_example(aircraft: Aircraft) -> str:
return f"{aircraft.brand} aircraft, holds {aircraft.capacity} passengers"
```
此外，如果您想搜索满足特定 capacity 阈值的 `Aircraft` 对象，可以编写以下代码：

Furthermore, if you wanted to search for `Aircraft` objects satisfying a certain capacity threshold, you could write the
following:
```python
from functions.api import function
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Aircraft
from ontology_sdk.ontology.object_sets import AircraftObjectSet

@function
def aircraft_search_example() -> AircraftObjectSet:
client = FoundryClient()
return client.ontology.objects.Aircraft.where(Aircraft.object_type.capacity > 100)
```
Python OSDK 还提供了 beta 功能，例如与 pandas DataFrames 的互操作性：

The Python OSDK also offers beta features such as interoperability with pandas DataFrames:
```python
from functions.api import function
from ontology_sdk.ontology.object_sets import AircraftObjectSet

@function
def aircraft_dataframe_example(aircrafts: AircraftObjectSet) -> int:
df = aircrafts.to_dataframe()
return df['capacity'].sum()
```
有关更多信息，请参阅 [Python Ontology SDK 文档](/docs/foundry/ontology-sdk/python-osdk/)。

Review the [Python Ontology SDK documentation](/docs/foundry/ontology-sdk/python-osdk/) for more information.