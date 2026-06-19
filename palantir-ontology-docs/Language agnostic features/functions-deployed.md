<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/functions-deployed/
---
# Deploy functions
## Prerequisites
本指南要求您已经编写并发布了一个 Python 或 TypeScript v2 Function。请参阅 [Python functions 入门](/docs/foundry/functions/python-getting-started/) 或 [TypeScript v2 functions 入门](/docs/foundry/functions/typescript-v2-getting-started/) 文档以获取教程。

This guide requires that you have already authored and published a Python or TypeScript v2 function. Review the [getting started with Python functions](/docs/foundry/functions/python-getting-started/) or [getting started with TypeScript v2 functions](/docs/foundry/functions/typescript-v2-getting-started/) documentation for a tutorial.
## Choose between deployed and serverless execution modes
如果您的注册账户启用了 serverless functions,新仓库将默认使用它。我们通常建议在大多数用例中使用 serverless functions。虽然在某些情况下已部署的 Function 可能有用,但 serverless 执行模式需要更少的维护,并可避免与长期部署相关的成本。

If serverless functions are enabled for your enrollment, new repositories will use it by default. We generally recommend serverless functions for most use cases. While a deployed function may be useful in some circumstances, the serverless execution mode requires less maintenance and avoids incurring the costs associated with long-lived deployments.
已部署的 Function 具有一些 serverless functions 所不具备的能力:

Deployed functions have some capabilities that are not available to serverless functions:
* 已部署 Function 的长期运行特性意味着如果该 Function 能够容忍重启,可能可以进行本地缓存。

* Serverless functions 支持使用所提供 source object 的 client 进行 [external sources](/docs/foundry/functions/api-calls/) 调用,但不支持第三方 client。您必须部署您的 Function 才能使用第三方 client 进行外部 API 调用。

* 已部署的 Function 支持 GPU 分配,以通过并行处理加速计算密集型的模型训练和推理工作流,而 serverless functions 不支持。

* The long-lived nature of deployed functions means that local caching may be possible if the function is tolerant to restarts.
* Serverless functions support [external sources](/docs/foundry/functions/api-calls/) using the client from the provided source object, but they do not support third-party clients. You must deploy your function to make external API calls with third-party clients.
* Deployed functions support GPU allocations to accelerate computationally intensive model training and inference workflows through parallel processing, while serverless functions do not.
已部署的 Function 具有一些不适用于 serverless 执行的限制:

Deployed functions have some limitations that do not apply to serverless execution:
* Serverless functions 允许按需执行同一 Function 的不同版本,从而使升级更安全。对于已部署的 Function,您一次只能运行单个 Function 版本。

* Serverless functions 仅在执行时产生费用,而已部署的 Function 只要部署在运行就会产生费用。

* Serverless functions 需要较少的前期设置和长期维护,因为基础设施是自动管理的。

* Serverless functions enable different versions of a single function to be executed on demand, making upgrades safer. With deployed functions, you can only run a single function version at a time.
* Serverless functions only incur costs when executed, while deployed functions incur costs as long as the deployment is running.
* Serverless functions require less upfront setup and long-term maintenance, as the infrastructure is managed automatically.
要为您的注册账户启用 serverless functions,请联系您的 Palantir 管理员。

To enable serverless functions for your enrollment, contact your Palantir administrator.
## Architecture
Function 可以以 serverless 模式运行,利用按需资源,也可以部署到长期运行的容器中。

Functions can be run in a serverless mode, leveraging on-demand resources, or they can be deployed to a long-lived container.
> **✅ 成功**

> 如果您的注册账户启用了 serverless functions,我们建议使用 serverless functions,而不是已部署的 Function。虽然在 [某些情况下已部署的 Function 很有用](#choose-between-deployed-and-serverless-execution-modes),但 serverless 执行器通常更加灵活。
> **✅ 成功**

> We recommend using serverless functions if enabled on your enrollment, rather than deployed functions. While there are [some cases where deployed functions are useful](#choose-between-deployed-and-serverless-execution-modes), the serverless executor is generally more flexible.
当您的 Function 被部署时,将创建一个长期运行的环境来处理传入的执行请求。该环境将根据请求量进行扩展,并偶尔由自动化进程重启。单个仓库中的所有 Function 由单个部署托管。

When your function is deployed, a long-running environment will be created to handle incoming execution requests. The environment will be scaled according to the request volume and occasionally restarted by automated processes. All functions from a single repository are hosted by a single deployment.
> **⚠️ 警告: 计算成本**

> 已部署的 Function 将为运行中的部署产生计算成本。Serverless functions 仅在执行时产生费用。
> **⚠️ 警告: Compute costs**

> Deployed functions will incur compute costs for the running deployment. Serverless functions will only incur costs when executed.
## Deploy a function
请按照以下步骤配置和部署 Function:

Follow the steps below to configure and deploy a function:
1. 打开您的 Function 仓库并导航至 **Branches** 选项卡,然后选择 **Tags and releases**。

2. 将鼠标悬停在您要部署的 Function 上,然后选择 **Open in Ontology Manager**。

1. Open your function repository and navigate to the **Branches** tab, then select **Tags and releases**.
2. Hover over the function you want to deploy, then select **Open in Ontology Manager**.
![Open the selected function in Ontology Manager.](/docs/resources/foundry/functions/python-functions-open-ontology-manager-v2.png)
3. 从左侧的版本选择器中选择您要使用的 function 版本。

4. 选择 **Configure execution**。

3. Select the version of the function you want to use from the version selector on the left.
4. Select **Configure execution**.
![Configure execution for a function.](/docs/resources/foundry/functions/python-functions-configure-execution.png)
5. 如果您的环境中启用了 serverless functions，您将看到一个用于在 serverless 和 deployed 之间切换的选项。如果未选择且不存在 deployment，则默认使用 serverless。

5. If serverless functions are enabled in your environment, you will see an option to switch between serverless and deployed. If unselected and no deployment exists, serverless will be used by default.
![The settings for a function in serverless mode.](/docs/resources/foundry/functions/python-functions-serverless-mode-configuration.png)
6. 选择 **Deployed** 执行模式选项。

6. Select the **Deployed** execution mode option.
7. 如果该 function 不存在 deployment，请选择 **Create deployment**。

7. If no deployment exists for the function, select **Create deployment**.
![The settings for a function in deployed mode without an existing deployment.](/docs/resources/foundry/functions/python-functions-create-deployment.png)
8. 首次创建 deployment 时，将应用默认配置。您可以向下滚动到页面末尾查看完整的配置。

8. Defaults will be applied for the configuration when the deployment is first created. You can view the entire configuration by scrolling down to the end of the page.
![The settings for a function in deployed mode.](/docs/resources/foundry/functions/python-functions-deployed-mode-configuration.png)
9. 根据需要修改 deployment 配置。您可以配置以下内容：

* 分配给 deployment 的计算资源，包括 CPU、GPU 和 memory。
* 基于请求负载进行自动扩缩容的最小限制和最大限制。

* 将在 deployment 启动时为其设置的环境变量。

* function 在返回超时错误之前允许运行的总时长。与其他 deployment 设置不同，timeout 是针对每个 function 版本单独配置的。

9. Modify the deployment configuration as needed. You can configure the following:
* The compute resources allocated to the deployment, including CPU, GPU, and memory.
* The minimum limit and the maximum limit for autoscaling based on request load.
* The environment variables that will be set for the deployment upon startup.
* The total duration the function is allowed to run before returning a timeout error. Unlike the other deployment settings, timeout is configured individually for each function version.
![Modifying the memory allocation for a function in deployed mode.](/docs/resources/foundry/functions/python-functions-modify-deployment-memory-allocation.png)
10. 选择 **Save and start deployment** 以保存所有更改并启动 deployment。您也可以选择 **Save without starting deployment** 以保存配置但不启动 deployment。

10. Select **Save and start deployment** to save any changes and launch the deployment. You may also select **Save without starting deployment** to save the configuration without launching the deployment.
![Save and start deployment for a function in deployed mode.](/docs/resources/foundry/functions/python-functions-save-and-start-deployment.png)
11. 如果选择了 **Save and start deployment** 选项，您需要等待托管该 function 的 deployment 启动。这可能需要几分钟时间。

11. If you chose to **Save and start deployment** option is selected, you will need to wait for the deployment that is hosting the function to start up. This may take a few minutes.
12. 若要验证 deployment 是否正在运行，请导航至包含该 function 的代码仓库并运行该 function。该 function 应成功执行并返回预期结果。

12. To verify that the deployment is running, navigate to the code repository containing the function and run the function. The function should execute successfully and return the expected result.
![Running a function in deployed mode.](/docs/resources/foundry/functions/python-functions-run-deployed-function.png)