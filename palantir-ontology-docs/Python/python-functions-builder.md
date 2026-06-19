<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-functions-builder/
---
# Use a Python function in Pipeline Builder
> **ℹ️ 注意**

> Pipeline Builder 同时支持 Java 和 Python 用户自定义函数 (UDF)。[详细了解 Java UDF](/docs/foundry/transforms-java/user-defined-functions/)。
> **ℹ️ 注意**

> Pipeline Builder supports both Java and Python user-defined functions (UDF). [Learn more about Java UDFs](/docs/foundry/transforms-java/user-defined-functions/).
## Prerequisites
本指南假定您已经编写并发布了一个 Python function。请查看我们的 [Python functions 入门](/docs/foundry/functions/python-getting-started/) 文档以获取教程。

This guide assumes you have already authored and published a Python function. Review our [getting started with Python functions](/docs/foundry/functions/python-getting-started/) documentation for a tutorial.
## Architecture
Python function 在 Pipeline Builder pipeline 中作为 sidecar 容器运行。这意味着该 function 无需部署，并且可以随 pipeline 的规模动态扩展。嵌入式 function 可以像 Pipeline Builder 中的其他 transform 一样进行 [preview](/docs/foundry/pipeline-builder/outputs-preview-pipeline/)。

Python functions run in a Pipeline Builder pipeline as a sidecar container. This means that the function does not need to be deployed and scales dynamically with the size of your pipeline. Embedded functions can be [previewed](/docs/foundry/pipeline-builder/outputs-preview-pipeline/) similarly to other transforms in Pipeline Builder.
## Use your function in a Pipeline Builder pipeline
按照以下步骤在您的 pipeline 中准备和配置 Python function：

Follow the steps below to prepare and configure a Python function in your pipeline:
1. 在 Pipeline Builder 中打开您要使用 Python function 的 pipeline。

1. Open the Pipeline Builder pipeline in which you want to use your Python function.

> 📷 **[图片: Pipeline Builder 中的 Python function。]**

> 📷 **[图片: A Python function in Pipeline Builder.]**

2. 通过以下两种方法之一将您的 UDF 导入到 Pipeline Builder：

* **从 graph 视图：**

1. 从 pipeline graph 的上部选择 **Reusables**，然后选择 **User-defined functions**。

> 📷 **[图片: Pipeline Builder 中的 'Reusables' 按钮。]**

2. 选择 **Import UDF** 并在可用 function 中搜索以找到您要使用的那一个。

3. 在 function 名称旁边选择 **Add**。该 function 随后应显示 **Imported** 标签。

> 📷 **[图片: 将 Python function 添加到 Pipeline Builder。]**

4. 关闭导入对话框，然后在 Pipeline Builder graph 上您要使用该 function 的位置选择 **Transform**。

5. 从 transform 列表中，在左侧找到 **UDFs** 选项卡以查看您已导入的 function。

* **使用 transform 选择器：**

1. 在 pipeline builder graph 上选择 **Transform**。

2. 输入您要导入的 UDF 的名称。

> 📷 **[图片: 在 Pipeline Builder 中搜索未导入的 UDF。]**

3. 选择 **Search unimported UDFs**。

4. 将鼠标悬停在所需的 UDF 上，然后选择 **Import**。

> 📷 **[图片: 在 Pipeline Builder 中导入 UDF。]**

3. 填写 transform 定义，指定输入列和参数，然后选择 **Apply**。

2. Import your UDF into Pipeline Builder using one of two methods:
* **From the graph view:**
1. Select **Reusables** from the upper part of the pipeline graph, then choose **User-defined functions**.

> 📷 **[图片: The 'Reusables' button in Pipeline Builder.]**

2\. Select **Import UDF** and search through the available functions to find the one you want to use
3\. Choose **Add** next to the function name. The function should then display an **Imported** tag.

> 📷 **[图片: Add Python function to Pipeline Builder.]**

4\. Close the import dialogue and select **Transform** on your Pipeline Builder graph where you would like to use the function.
5\. From the list of transforms, find the **UDFs** tab to the left to view your imported functions.
* **Use the transform picker:**
1. Select **Transform** on the pipeline builder graph.
2. Enter the name of the UDF you want to import.

> 📷 **[图片: Search unimported UDFs in Pipeline Builder.]**

3\. Select **Search unimported UDFs**.
4\. Hover over the desired UDF and select **Import**.

> 📷 **[图片: Import UDFs in Pipeline Builder.]**

3. Fill out the transform definition specifying the input columns and parameters, then select **Apply**.

> 📷 **[图片: Pipeline Builder 中已配置的 Python function transform。]**

> 📷 **[图片: Configured Python function transform in Pipeline Builder.]**

您现在应该可以在 Pipeline Builder graph 上看到您的 Python function，并可以预览该 function 的输出。

You should now see your Python function on your Pipeline Builder graph and can preview the output of the function.

> 📷 **[图片: Pipeline Builder 中的 Python function]**

> 📷 **[图片: Python function in Pipeline Builder]**

## External API calls in Pipeline Builder
要从 Pipeline Builder 向外部系统发起 API 调用，您可以发布一个 [可访问外部系统的 Python function](/docs/foundry/functions/api-calls/)。这将允许您编写与外部系统通信的逻辑，并将其用作 pipeline 的一部分。

To make API calls to an external system from Pipeline Builder, you can publish a [Python function with access to external systems](/docs/foundry/functions/api-calls/). This will allow you to write logic that communicates with external systems and use it as part of your pipeline.
要在 Pipeline Builder 中用作用户自定义函数 (UDF)，您函数中使用的所有 source 必须配置为可导入到 pipeline 中。要配置此设置，请导航到 Data Connection 中的 source，然后转到 **Connection settings > Code import configuration** 选项卡：

To be used as a user-defined function (UDF) in Pipeline Builder, all sources used in your function must be configured to be importable into pipelines. To configure this setting, navigate to the source in Data Connection, then to the **Connection settings > Code import configuration** tab:
![Allow source to be imported to pipelines.](/docs/resources/foundry/functions/allow-source-to-be-imported-to-pipelines.png)
在 source 上启用此选项并发布您的 Python function 后，即可像使用任何其他 Python function 一样在 pipeline 中使用它。

Once you have enabled this option on your source and published your Python function, it can be used in your pipeline in the same way as any other Python function.