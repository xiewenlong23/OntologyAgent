<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/scenarios-options/
---
# Scenario options
### Time window selection
您可以指定运行 scenario 的时间窗口。您应选择一个在 scenario 范围内的 objects 具有已知数据的时间。

You can specify the time window for running your scenario. You should select a time where there is known data for the objects in scope of the scenario.
![Time Window](/docs/resources/foundry/vertex/simulate-system-4.jpg)
### Advanced options
您可以配置在设定时间段（分钟）内的 time series smoothing。

You can configure time series smoothing over set periods (minutes).
![Advanced Options](/docs/resources/foundry/vertex/simulate-system-5.jpg)
### Scope
对于基于 object 的 System Graphs，您可以选择将 scenario 的 scope 设置为仅显示 graph 中的 objects，以限制可用的 input/output parameters。

For object-based System Graphs, you can choose to set the scope of the scenario to objects shown only in the graph to limit available input/output parameters.
![Set Scope](/docs/resources/foundry/vertex/simulate-system-6.jpg)
### Run baseline scenario
您可以选择在运行包含 actions 或 overrides 的 scenario 时，是否同时运行一个额外的 baseline scenario。此 baseline scenario 将在不应用任何 actions 或 overrides 的情况下运行您所选择的 models，为您提供一个 baseline，以便与其他 scenarios 进行比较，从而更好地评估您的 actions 所产生的影响。

You may choose whether you want to run an additional baseline scenario whenever you are running a scenario which contains either actions or overrides. This baseline scenario will run the models you have chosen without any actions or overrides, providing you with a baseline against which to compare your other scenarios and better judge the impacts of your actions.
## Select input/output parameters
您可以使用 **+ Add input or output** 选项将要在 scenario 表格中显示的 parameters 添加进来。从此处，您可以选择向 scenario 中添加单独的 time series、object properties 或 measures。此操作将打开一个搜索和选择框，其中包含所选模型可用的已配置 inputs/outputs。您也可以默认选择 **Add all parameters** 以添加所有已预配置的 parameters。任何已选择的 parameters 都将显示在 scenario 表格中。如果该 parameter 是一个 input，您可以在运行 scenario 之前通过在 scenario 表格中手动编辑该值来覆盖它。

You can add the parameters you want to display within the scenario table using the **+ Add input or output** option. From here, you can choose to add individual time series, object properties, or measures to your scenario. This action will open a search and selection box with the configured inputs/outputs available for the selected model. You can also default to **Add all parameters** that have been pre-configured. Any parameters chosen will be shown within the scenario table. If the parameter is an input, you can override it by manually editing the value within the scenario table prior to running a scenario.
> **ℹ️ 注意**

> 一旦选择了模型，任何用作 input/output parameters 的 properties 都将显示在 object 选择面板中。
> **ℹ️ 注意**

> Once the model is selected, any properties used as input/output parameters will be shown in the object selection panel.
![Add Params](/docs/resources/foundry/vertex/simulate-system-7.jpg)
![Add Params 2](/docs/resources/foundry/vertex/simulate-system-8.jpg)