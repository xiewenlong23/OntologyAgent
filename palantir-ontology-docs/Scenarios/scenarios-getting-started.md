<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/scenarios-getting-started/
---
# Getting started
[Scenarios](/docs/foundry/vertex/scenarios-overview/) 允许您通过向系统提出"如果...会怎样？"的问题，来了解不同条件或决策路径的影响。Vertex 利用在 Foundry 中创建、发布和编排的现有模型，提供一个界面来可视化整个系统中建模的交互，并选择性地覆盖关键参数，以了解为达到最佳输出可以采取的替代 Actions。

[Scenarios](/docs/foundry/vertex/scenarios-overview/) allow you to understand the impact of different conditions or decision paths by asking "What if?" questions of your system. Vertex leverages existing models authored, published, and orchestrated within Foundry to provide an interface for visualizing modeled interactions across your system and selectively overriding key parameters to understand alternative Actions that can be taken to reach optimal outputs.
## Add Actions
您可以测试使用预配置的 Actions 来修改 Ontology 中的对象可能对您的本地和整个系统产生的潜在影响。

You can test how using pre-configured Actions to modify objects in your Ontology may potentially impact both your local and overall system.
### Select Actions
要开始添加 Actions，首先选择 **Add scenario** 按钮。这将创建一个新场景，您可以向其中添加 Actions。您可以通过选择该场景并选择 **Add Action** 按钮来展开场景部分。

To begin adding Actions, first select the **Add scenario** button. This will create a new scenario to which you can add Actions. You can expand the scenario section by selecting the scenario and selecting the **Add Action** button.
![Add Actions](/docs/resources/foundry/vertex/simulate-system-12.jpg)
选择要添加的 Action 后，您必须更新该 Action 的参数并选择 **Submit**，以将此 Action 保存在您的场景中。

After choosing which Action to add, you must update the parameters of the Action and select **Submit** to save this Action within your scenario.
![Configure Action](/docs/resources/foundry/vertex/simulate-system-13.jpg)
然后您可以运行此场景并查看您创建的 Actions 的效果。

You may then run this scenario and view the effects of the Actions you created.
您还可以添加其他 Actions，或继续向场景添加模型，以进一步模拟对您系统的影响。

You may also add additional Actions or continue on to add models to a scenario to further simulate the effects on your system.
## Select models \[Sunset]
> **⚠️ 警告: Sunset**

> 下面描述的模型选择、配置和运行流程处于 [sunset](/docs/foundry/platform-overview/development-life-cycle/) 阶段，将在未来的某个日期被弃用。仍提供全面支持。要继续在 Vertex 场景中使用模型，我们建议 [为模型配置一个 function](/docs/foundry/model-integration/functions-on-models/)，[导入该 function](/docs/foundry/functions/functions-on-models/) 到一个 [function-backed Action](/docs/foundry/action-types/function-actions-getting-started/)，然后按照 [上面列出的说明](#add-actions) 进行操作。
> **⚠️ 警告: Sunset**

> The model selection, configuration, and run process described below is in the [sunset](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be deprecated at a future date. Full support remains available. To continue using models in Vertex scenarios, we recommend [configuring a function for the model](/docs/foundry/model-integration/functions-on-models/), [importing that function](/docs/foundry/functions/functions-on-models/) into a [function-backed Action](/docs/foundry/action-types/function-actions-getting-started/), then following [the instructions listed above](#add-actions).
您可以从已在 Foundry 中发布并使用 [Modeling Objectives](/docs/foundry/model-integration/objectives/) 绑定到 Ontology 的现有模型或 functions 中进行选择。在 Vertex 中，您可以创建一个场景案例研究来调查和了解本地流程，并量化单个更改可能对本地和连接的系统产生的影响。

You can select from existing models or functions that have been published within Foundry and bound to the Ontology using [Modeling Objectives](/docs/foundry/model-integration/objectives/). Within Vertex, you can create a scenario case study to investigate and understand the local processes and quantify how individual changes may impact local and connected systems.
### New model selection
要开始一个新的调查，您可以从任何已发布的模型中进行选择。选择 **Add new model** 并搜索与您的流程相关的模型。

To start a new investigation, you can select from any published models. Select **Add new model** and search for the relevant model for your process.
![Select Model](/docs/resources/foundry/vertex/simulate-system-1.jpg)
这会将选定的模型添加到场景窗格中，并允许您选择正确的模型和配置版本以启动您的新案例研究。

This will add the selected model to the scenario pane and allow you to select the correct model and configuration versions to start your new case study.
![Model and Configuration Versions](/docs/resources/foundry/vertex/simulate-system-2.jpg)
### Default model selection
在探索现有系统或流程时，您可以选择从推荐的预配置默认模型运行场景。

When exploring an existing system or process, you can choose to run scenarios from the recommended pre-configured default models.
![Default Model](/docs/resources/foundry/vertex/simulate-system-3.jpg)
这会将相关模型添加到场景窗格中，并允许您选择正确的模型和配置版本以启动您的新案例研究。

This will add the relevant models to the scenario pane and allow you to select the correct model and configuration versions to start your new case study.
[详细了解可以为您的场景配置的选项。](/docs/foundry/vertex/scenarios-options/)

[Learn more about the options that can be configured for your scenario.](/docs/foundry/vertex/scenarios-options/)
## Select input/output parameters
您可以使用 **+ Add input or output** 选项将要在 scenario 表格中显示的 parameters 添加进来。从此处，您可以选择向 scenario 中添加单独的 time series、object properties 或 measures。这将打开一个搜索和选择框，其中包含所选模型可用的已配置 inputs/outputs。您也可以默认选择 **Add all parameters** 以添加所有已预配置的 parameters。任何已选择的 parameters 都将显示在 scenario 表格中；如果该 parameter 是一个 input，则可以在运行 scenario 之前通过在 scenario 表格中手动编辑该值来覆盖它。

You can add the parameters you want to display within the scenario table using the **+ Add input or output** option. From here, you can choose to add individual time series, object properties, or measures to your scenario. This will open a search and selection box with the configured inputs/outputs available for the selected model. You can also default to **Add all parameters** that have been pre-configured. Any parameters chosen will be shown within the scenario table; if the parameter is an input, it can be overridden by manually editing the value within the scenario table prior to running a scenario.
> **ℹ️ 注意**

> 一旦选择了模型，任何用作 input/output parameters 的 properties 都将显示在 object 选择面板中。
> **ℹ️ 注意**

> Once the model is selected, any properties used as input/output parameters will be shown in the object selection panel.
![Add Params](/docs/resources/foundry/vertex/simulate-system-7.jpg)
![Add Params 2](/docs/resources/foundry/vertex/simulate-system-8.jpg)
## Run a scenario
添加 parameters 后，将使用任何 time series parameters 当前所选的时间来显示 inputs 的 parameter 当前值。选择 **Run** 将生成一个 scenario，以根据所示的 input 值计算建模的 outputs。完成后，scenario 将显示一个绿色对勾以及生成 outputs 所用的时间。

Once parameters have been added, the current value of the parameter will be shown for the inputs using the currently selected time for any time series parameters. Selecting **Run** will generate a scenario to calculate the modeled outputs based on the input values shown. Once completed, the scenario will show a green checkmark and the time taken for outputs to be generated.
![Baseline Simulation](/docs/resources/foundry/vertex/simulate-system-9.jpg)
## Build your "what if" case study
为了测试可能的解决方案，您可以构建您的 case study 并通过 "what if" scenarios 进行迭代。

To test possible solutions, you can build your case study and iterate through "what if" scenarios.
通过选择要覆盖的 parameter 并输入新的模拟 input 来设置 input 覆盖条件。这将以高亮形式显示带有覆盖值的方框。

Input override conditions by selecting the parameter to override and inputting the new simulated input. This will highlight the box with the override.
![Overrides](/docs/resources/foundry/vertex/simulate-system-10.jpg)
使用 override 值运行 scenario 将显示新计算出的 outputs，以便与已运行的 baseline scenario 进行比较。您可以继续添加不同的 scenario 运行，以研究最优的 outputs。

Running a scenario with override values will show the newly calculated outputs for comparison to the baseline scenario that was run. You can continue to add different scenario runs to investigate the optimal outputs.
模拟值将作为与添加到 object node extended labels 中的读数（readouts）的对比显示出来。

Simulated values will be shown as comparisons to the readouts added to the object node extended labels.
完成一组 case study 后，您可以在 scenario 面板顶部对其进行重命名。您可能希望创建多个不同的 case studies，以研究同一系统下的不同条件。您也可以对各个 scenarios 进行重命名，以更好地描述所涉及的 Actions。

Once you have completed a set case study, you can rename this at the top of the scenario pane. You may want to create multiple different case studies to investigate different conditions across the same system. You may also rename individual scenarios to better capture the Actions which are involved.
![Rename Case Study](/docs/resources/foundry/vertex/simulate-system-11.jpg)
## Chained models
[了解如何配置 chained models。](/docs/foundry/vertex/chained-models/)

[Learn how to configure chained models.](/docs/foundry/vertex/chained-models/)