<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-getting-started/
---
# Getting started with Python functions
以下文档将指导您完成准备工作，以便在 Palantir 平台中使用 Python Function。您将学习如何创建 Python functions 仓库、提交和发布函数、在 live preview 中进行测试等。

The following documentation will guide you through the initial steps to prepare Python functions for use in the Palantir platform. You will learn how to create a Python functions repository, commit and publish a function, test in live previews, and more.
## Create a Python functions repository
导航到您选择的项目，通过选择 **+ New > Repository** 来创建一个新的代码仓库。选择 **Pythons functions** 模板来初始化您的仓库。我们建议将所有用于 Workshop 或基于 Ontology 的应用程序的函数分组到单个仓库中，以降低成本。

Navigate to a project of your choice and create a new code repository by selecting **+ New > Repository**. Select the **Pythons functions** template to initialize your repository. We recommend grouping all functions for use in Workshop or Ontology-based applications in a single repository to minimize costs.
![Create a Python function code repository.](/docs/resources/foundry/functions/python-functions-create-repo.png)
仓库创建后，导航到 `python-functions/python/python-functions/my_function.py` 文件。

Once the repository is created, navigate to the `python-functions/python/python-functions/my_function.py` file.
## Explore the repository
您的仓库将使用一个包含一些示例函数的 `my_function.py` 文件进行初始化，包括以下内容：

Your repository will be initialized with a `my_function.py` file containing some example functions, including the following:
```python tab="Python"
from functions.api import function, String

@function
def my_function() -> String:
return "Hello World!"
```
请注意，该函数遵循以下约束：

Notice that the function adheres to the following constraints:
* 函数必须使用 `functions.api` 包中的 `@function` 装饰器进行装饰，才能被识别为 Python function。您可以有多个 Python 文件，每个文件中包含多个函数，但*只有使用此装饰器的函数*才会被注册为 Python function。

* 函数必须声明其所有输入的类型以及输出的类型，可以使用 functions API 包中的类型或其对应的 Python 类型。例如，上述示例的输出类型声明为 functions API 中的 `String`，但也可以声明为对应的 Python 类型 `str`。

* The function must be decorated with `@function` from the `functions.api` package to be recognized as a Python function. You may have multiple Python files with multiple functions in each file, but *only the functions with this decorator* will be registered as Python functions.
* The function must declare the types of all of its inputs along with the type of its output, either using the type from the functions API package or its corresponding Python type. For example, the above example’s output type is declared as `String` from the functions API, but it may also be declared as the corresponding Python type `str`.
> **ℹ️ 注意**

> 即使您使用 API 类型（例如 `String`）声明参数的类型，您的函数在运行时也会接收到对应的 Python 类型（在本例中为 `str`）。
> **ℹ️ 注意**

> Even if you declare the type of an argument with the API type (for example, `String`), your function will be passed the corresponding Python type at runtime (in this example, `str`).
有关 Python function 中类型的完整概述，请参阅我们的 [类型参考文档](/docs/foundry/functions/types-reference/)。

For a full overview of types in Python functions see our [type reference documentation](/docs/foundry/functions/types-reference/).
## Test in live preview
添加新函数后，您可以在 **Functions** 助手工具中立即运行它。从屏幕左下角打开 **Functions** 助手工具，然后选择 **Live Preview**。选择 `add_seconds_to_datetime` 函数，输入值，然后选择 **Run** 来运行代码。

After you add the new function, you can run it immediately in the **Functions** helper. Open the **Functions** helper from the bottom left of the screen and select **Live Preview**. Choose the `add_seconds_to_datetime` function, enter input values, and select **Run** to run the code.
![Run your new function in the functions helper.](/docs/resources/foundry/functions/python-functions-live-preview.png)
选择右上角的 **Commit**，将您的更改提交到仓库的 `master` 分支。

Select **Commit** in the upper right to commit your changes onto the `master` branch of your repository.
### Commit and publish a function
编写函数后（或取消注释提供的某个示例函数），请按照以下步骤进行提交和发布。

Once you write a function (or uncomment one of the example functions provided), follow the steps below to commit and publish it.
1. 通过在 **Source control** 选项卡中选择 **Commit** 来提交您的更改，并添加提交信息。

2. 从屏幕顶部中间选择 **Branches** 选项卡，然后选择 **Tags and releases**。

3. 选择 **New tag** 并为该发布版本提供一个版本号。

1. Commit your changes by selecting **Commit** in the **Source control** tab and adding a commit message.
2. Select the **Branches** tab from the top center of the screen, then select **Tags and releases**.
3. Choose **New tag** and provide a version for the release.

> 📷 **[图片: 选择适当的版本]**

> 📷 **[图片: Select an appropriate version]**

4. 选择 **Tag and release** 并等待发布步骤完成。

4. Select **Tag and release** and wait for the release step to complete.
5. 检查通过后，选择 **Code** 选项卡，然后打开页面底部的 **Functions** 选项卡。您将在结果中看到 `my_function`。

5. Once the check is successful, select the **Code** tab, then open the **Functions** tab on the bottom of the page. You will see `my_function` in the results.
![Open the Functions helper.](/docs/resources/foundry/functions/python-functions-preview.png)
6. 选择该 function，然后选择 **Run** 来执行您刚刚发布的 function。

6. Select the function, then choose **Run** to execute the function that you just published.
![Run the function in the Functions helper.](/docs/resources/foundry/functions/python-functions-run.png)
## Add another function
现在，我们将向此 repository 添加一个更复杂的 function 以进行测试和发布。将以下代码复制并粘贴到 `my_function` 文件的底部。

Now, we will add a more complex function to this repository to test and publish. Copy and paste the code below to the bottom of the `my_function` file.
```python tab="Python"
from functions.api import function, String
from datetime import datetime, timedelta

@function
def add_seconds_to_datetime(start_time: datetime, elapsed_millis: int) -> str:
dt = start_time + timedelta(milliseconds=elapsed_millis)
return dt.isoformat()
```
有关如何在平台中使用 Python functions 的更多示例，请查看我们的文档：[在 Pipeline Builder 中使用 Python functions](/docs/foundry/functions/python-functions-builder/) 以及 [在 Workshop 中使用 Python functions](/docs/foundry/functions/python-functions-workshop/)。

For more examples of how to use your Python functions in the platform, review our documentation on [using Python functions in Pipeline Builder](/docs/foundry/functions/python-functions-builder/) and on [using Python functions in Workshop](/docs/foundry/functions/python-functions-workshop/).