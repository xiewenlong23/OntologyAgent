<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/machinery/core-concepts/
---
# Core concepts
我们建议在使用 Machinery 应用程序之前先回顾以下概念。

We recommend reviewing the following concepts before using the Machinery application.
## Process
在现实世界的流程中，文档、设备或个人等实体会随着时间的推移在 [states](#state) 之间转换。许多此类流程对象可以相互链接，以表示参与流程的多个实体。在 Machinery 中，您可以通过包含状态和操作的流程容器来对这些流程进行建模。这些流程容器可以相互链接，甚至可以嵌套。

In a real-world process, entities such as documents, equipment, or individuals transition through [states](#state) over time. Many of these process objects can be linked to each other to represent multiple entities involved in a process. In Machinery, you can model these processes via process containers which hold states and actions. These process containers can be linked to one another and even be nested.
流程中的实体（也称为"流程对象"）可以由 ontology 中的一个 Object Type 表示，例如 *Claim*、*Flight* 或 *Employee*。该 Object Type 必须具有一个字符串类型的 Property，用于表示对象的状态。

Entities within a process, also called "process objects", can be represented by an object type in your ontology, such as *Claim*, *Flight*, or *Employee*. That object type must have a string-type property that denotes the object's state.
## State
状态描述了对象的当前状况，例如包裹的 *in progress* 或 *delivered*。可能的状态必须是可枚举的。例如，`Name` Property 不适合作为状态，因为可能的名称数量是无限的。

A state describes the current condition of an object, such as *in progress* or *delivered* for a parcel. The possible states must be enumerable. For instance, a `Name` property would not be suitable because there are indefinitely many possible names.
状态转换显示为状态节点之间的边。

State transitions are shown as edges between state nodes.
在任何给定时间，每个对象必须处于可能状态中的**一个**。如果出现不属于此情况的情形，应将其建模为流程层次结构。例如，一个员工可以同时处于 *new-hire* 或 *onboarded* 状态，也可以同时处于 *paid* 或 *awaiting payment* 状态。这些应该是单独的流程，并由一个父流程跟踪该员工是否处于 *payable* 状态。

Every object must be in **one** of the possible states at any given time. Scenarios where this is not the case should be modeled as a process hierarchy. For example, an employee could have the state *new-hire* or *onboarded*, and also *paid* or *awaiting payment* at the same time. These should be separate processes, with a parent process tracking whether the employee is *payable*.
在 Ontology 中，状态被编码为 `State` Property 的字符串值。该值等同于 Machinery 中的状态 ID。要更改图中显示的状态标签，您可以覆盖其显示名称。

Within the Ontology, the state is codified as a string value of the `State` property. This value is equivalent to the state ID in Machinery. To change the state label shown on the graph, you can overwrite the display name.
Machinery 中的状态 ID 等同于您数据中的状态值。为避免输入错误或不一致，您可以使用枚举 [value type](/docs/foundry/object-link-types/value-types-overview/) 来支撑状态 Property。这将保证 ontology 中的数据只能采用一组预定义的值。Machinery 将检测此配置并保持流程状态的同步。

The state IDs in Machinery are equivalent to the state values in your data. To avoid typing errors or discrepancies, you can back your state property by an enumeration [value type](/docs/foundry/object-link-types/value-types-overview/). This will guarantee that the data in the ontology can only assume a predefined set of values. Machinery will detect this setup and keep the process states in sync.
## Action and automations
操作是状态转换的原因。平台内发生的状态更改由 [action](/docs/foundry/action-types/overview/) 定义。您可以将它们导入到 Machinery 图中，并限定它们在流程中的角色。

Actions are the cause of state transitions. State changes that happen within the platform are defined by an [action](/docs/foundry/action-types/overview/). You can import them to the Machinery graph and qualify their role in the process.
## Process log
流程的本质在于实体会随着时间发生变化。为了识别对象所经历路径中的模式，或计算诸如在某个状态中所花费的平均时间等指标，捕捉变化的时间维度至关重要。Machinery 通过维护一个 `Log` Object Type 来实现这一点，该 Object Type 跟踪对对象所做的每一次更改，无论这些更改来自外部数据源还是 Foundry actions。

The nature of a process is that entities undergo changes over time. To identify patterns in the paths that objects take or metrics like the average time spent in a state, it is essential to capture the time dimension of changes. Machinery does so by maintaining a `Log` object type that tracks every change made to an object, whether from external data sources or Foundry actions.
您可以像查看其他 Object Type 一样查看此 Object Type，但不应自行在其上定义 Action，因为 log Object Type 由 Machinery 自动维护。

You can view this object type like any other, but you should not define actions on it yourself, as the log object type is maintained automatically by Machinery.
每个 log Object Type 跟踪单个 Object Type Property 的更改。每个 Process 都可以拥有自己的 process log。

Each log object type tracks the changes of a single object type property. Each process can have a process log of its own.
对于在平台外部发生的 Process，您需要提供一个 changelog 格式的 dataset，用于跟踪哪个 Object 在什么时间进入了哪个状态。Machinery 会计算分析和监控所需的派生数据，例如前一个状态、状态之间的持续时间以及 Object 到此时间为止所经历的路径。

For processes happening outside the platform, you need to provide a dataset in changelog format that tracks which object went into which state at what time. Machinery computes derivations required for analysis and monitoring, such as the previous state, the duration between states, and the path that an object took until this time.