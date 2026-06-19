<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/chained-models/
---
# Configure chained models \[Sunset]
> **⚠️ 警告: Sunset**

> Vertex 中的 Model chaining 处于 [sunset](/docs/foundry/platform-overview/development-life-cycle/) 阶段，并将在未来某个日期被弃用。仍将提供全面支持。要继续在 Vertex 场景中使用 models，我们建议 [为 model 配置一个 function](/docs/foundry/model-integration/model-functions-guide/) 并 [导入该 function](/docs/foundry/functions/functions-on-models/) 到一个 [function-backed Action](/docs/foundry/action-types/function-actions-getting-started/) 中。
> **⚠️ 警告: Sunset**

> Model chaining in Vertex is in the [sunset](/docs/foundry/platform-overview/development-life-cycle/) phase of development and will be deprecated at a future date. Full support remains available. To continue using models in Vertex scenarios, we recommend [configuring a function for the model](/docs/foundry/model-integration/model-functions-guide/) and [importing that function](/docs/foundry/functions/functions-on-models/) into a [function-backed Action](/docs/foundry/action-types/function-actions-getting-started/).
当您开始在您的建模 universe 中连接系统和流程时，您必须能够理解您系统的每个单独方面如何在全局范围内进行交互。Vertex 允许您将连接的 models 链接在一起，以理解和量化变化的端到端影响，从而实现最佳决策。

As you begin to connect systems and processes throughout your modeled universe, you must be able to understand how each individual aspect of your system interacts globally. Vertex allows you to chain together connected models to understand and quantify the end-to-end impact of changes, allowing for optimal decision-making.
将 model 添加到 case study 后，您可以选择 **+ Add New Model** 来搜索并选择其他相关 models。为映射到参数并用作后续 model 输入的 model output 生成的任何值将作为输入值传播到该 model。此值在输入单元格中使用链接图标表示。

Once you add a model to a case study, you can select **+ Add New Model** to search and select additional related models. Any value produced for a model output that is mapped to a parameter and used as input to a later model will propagate as the input value to that model. This value is denoted in the input cell using a link icon.
选定的模型将被添加到场景窗格中，您可以从输入/输出参数中进行选择，以在案例研究中显示。这些选择是根据每个显示的模型进行的。

Selected models will be added to the scenario pane where you can select from the input/output parameters to display in the case study. These are selected per model shown.
在任何选定的模型输入中添加覆盖项时，在您运行"假设"模拟时，将显示链式模型中受影响的输入，并且如果启用了相关选项，将触发运行一个基线场景。

Adding overrides in any of the selected model inputs will show impacted inputs in the chained models as you run "what if" simulations, and will trigger a baseline scenario to be run if the option is enabled.