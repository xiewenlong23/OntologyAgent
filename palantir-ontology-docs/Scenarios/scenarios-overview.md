<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/scenarios-overview/
---
# Scenarios
Scenarios 允许您与建模的 Universe 进行交互，解锁提出"What if"问题的能力，以模拟不同的运营条件。要了解更多关于 Palantir 在将模型与组织成果连接方面的高层方法，请参阅 [Ontology 中的 Models](/docs/foundry/ontology/models/)。

Scenarios allow you to interact with your modeled universe, unlocking the ability to ask “What if” questions to simulate different operating conditions. To learn more about Palantir's high-level approach to connecting models with organizational outcomes, refer to [Models in the Ontology](/docs/foundry/ontology/models/).
针对您的 system graph 进行配置后，scenario 会评估 actions 以及一个或多个建模的 inputs，并计算 output value 以反映您数字孪生的真实世界交互。Vertex 的集成能力使您能够对多组交互进行建模，并自动将它们链接在一起，将一个模型的 outputs 作为另一个模型的 inputs 传递。这使您能够理解并跨多个系统与多个流程进行交互，以了解所提议变更的端到端影响。

Configured against your system graph, a scenario evaluates actions along with one or more modeled inputs and computes the output value to reflect the real-world interactions of your digital twin. The integrated power of Vertex allows you to model multiple sets of interactions and automatically chain these together to forward the outputs of one model as the inputs to another. This allows you to understand and interact with multiple processes across multiple systems to understand the end-to-end impact of a proposed change.
## Business logic and models in Foundry
为了模拟运营条件，您首先需要定义这些条件、它们的 Ontology 关系以及预期行为。您可以通过创建 [Functions on models](/docs/foundry/functions/functions-on-models/) 来实现这一点，在其中您可以基于 Foundry 中的 models 编写、评估和部署业务逻辑。

In order to simulate operating conditions, you first need to define these conditions, their ontological relationships, and expected behavior. You can do this through the creation of [Functions on models](/docs/foundry/functions/functions-on-models/) where you can author, evaluate, and deploy business logic based on models within Foundry.
将 models 视为接收预定义 inputs 集合并返回 calculated outputs 集合的 jobs。模型版本指定 input 和 output 参数，并可与您 system graph 中看到的 Object Type 一起配置。这使您能够将建模概念与数字孪生紧密对齐，以提供动态的系统交互。[了解更多关于 Foundry 中的机器学习和建模。](/docs/foundry/model-integration/overview/)

Consider models as jobs that take a pre-defined set of inputs and return a set of calculated outputs. The model version specifies the input and output parameters and can be configured alongside the ontological objects seen in your system graph. This allows you to closely align your modeled concepts with your digital twin to provide dynamic system interactions. [Learn more about Machine Learning and Modeling in Foundry.](/docs/foundry/model-integration/overview/).
一旦 [发布为 actions](/docs/foundry/action-types/function-actions-getting-started/)，Functions on models 将在 Vertex 中可供配置，您可以在其中交互式地运行 scenarios，以了解潜在运营条件的影响。

Once [published as actions](/docs/foundry/action-types/function-actions-getting-started/), Functions on models will be available for configuration in Vertex, where you can interactively run scenarios to understand the impact of potential operating conditions.
Foundry 中的 Functions 使代码作者能够编写可在运营上下文中快速执行的逻辑，例如旨在赋能决策流程的仪表板和应用程序。发布后，Functions 还可在 Vertex 中用于支持动态模拟案例研究。[了解更多关于 Functions 的信息。](/docs/foundry/functions/overview/)

Functions in Foundry enables code authors to write logic that can be executed quickly in operational contexts, such as dashboards and applications designed to empower decision-making processes. Once published, Functions can also be used in Vertex to support dynamic simulated case studies. [Learn more about Functions.](/docs/foundry/functions/overview/)
## Time series for scenarios
为了理解和与系统随时间的变化进行交互，将测量值塑造为时间序列至关重要，以便将这些值配置为模型的 inputs，从而生成 calculated time series outputs 进行比较。这将使您能够监控当前状态、查看历史趋势，并通过模拟对建模条件的覆盖来预测未来变化。

To understand and interact with changes to your system over time, it is critical to shape your measured values as time series in order to configure these as inputs to your model which will generate calculated time series outputs for comparison. This will allow you to monitor your current state, view historic trends, and predict future changes with simulated overrides to modeled conditions.
您可以在 [time series documentation](/docs/foundry/time-series/time-series-overview/) 中找到有关时间序列设置的更多信息。请联系您的 Palantir 代表以获取有关时间序列的进一步帮助。

You can find more information on time series setup in the [time series documentation](/docs/foundry/time-series/time-series-overview/). Contact your Palantir representative for further assistance with time series.