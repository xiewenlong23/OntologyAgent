<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/interface-link-types-overview/
---
# Interface link type constraints
interface link type constraint 定义了在所有 implement 该 interface 的 object types 之间通用的 object-to-object 关系。用户可以为 link 指定 description，并为 link type 指定 API name 以供在代码中引用。当某个 object implement 一个带有 interface link type constraint 的 interface 时，该 object type 上的具体 link types 将用于满足 interface link type constraints。

An interface link type constraint defines an object-to-object relationship common across all object types implementing an interface. Users can specify a description for the link and an API name for the link type to use as a reference in code. When an object implements an interface with an interface link type constraint, concrete link types on the object type are used to fulfill interface link type constraints.

> 📷 **[图片: Interface link type creation.]**

> 📷 **[图片: Interface link type creation.]**

如上图中的示例所示，为了对 facility 及其服务的航空公司之间的关系进行建模，`Facility` interface 声明了一个可选的 one-to-many link type constraint，介于任何 implement `Facility` interface 的 object 与 `Airline` object type 之间。这意味着，如果 implement 该 interface 的 object type（例如 `Airport`）具有到 `Airlines` object type 的具体 link type，则可以通过 interface link type API name 访问该 link。

As shown in the example above, to model the relationship between a facility and the airlines it serves, the `Facility` interface declares an optional one-to-many link type constraint between any object that implements the `Facility` interface and the `Airline` object type. This means that if the implementing object type (for example `Airport`) has a concrete link type to the `Airlines` object type, that link can be accessed through the interface link type API name.
## Link type constraints
Link type constraints 定义了 interface link type 的参数。所有 implementing object types 必须具有满足这些 constraints 的 link（如果 link type 是必需的）。这些参数包括以下内容：

Link type constraints define the parameters of an interface link type. All implementing object types must have a link that satisfies these constraints if the link type is required. These parameters include the following:
* **Link target type：** interface 或 object type。

* **Target：** 特定的 interface 或 object type。

* **Cardinality：** one-to-one 或 one-to-many。

* Link 是否作为 object type implementation 的一部分必需。

* **Link target type:** An interface or an object type.
* **Target:** A specific interface or object type.
* **Cardinality:** One-to-one or one-to-many.
* Whether or not the link is required as part of object type implementation.
## Link target: Interface
当您想要对两个抽象 object types 之间的关系进行建模时，应使用类型为 `interface` 的 link target。

You should use a link target of type `interface` when you want to model the relationship between two abstract object types.
例如，您可以使用 interface link target 来建模 `Facility` 与发生 `Alert` 之间的关系。由于存在多种设施和多种告警类型，如果链接的两端只能使用单个 object type，则无法对二者之间的连接进行建模。相反，您可以通过定义一个 `Facility` interface、一个 `Alert` interface，以及在 `Facility` 上设置一个链接到 `Alert` interface 的 interface link 来建模此关系。然后，您可以定义一个实现 `Facility` interface 的 `Airport` object type，以及一个实现 `Alert` interface 的 `Flight Alert` object type。之后，您可以定义一个从 `Airport` 到 `Flight Alert` 的具体 link type，以满足 `Facility` interface 的 link type constraint。

For example, you can use an interface link target to model the relationship between `Facility` and the `Alert` where they occur. Because there are several kinds of facilities and several kinds of alerts, it would be impossible to model the connection between the two if you could only use a single object type for each end of the link. Instead, you can model this relationship by defining a `Facility` interface, an `Alert` interface, and an interface link on `Facility` that is set to link to the `Alert` interface. You can then define an `Airport` object type that implements the `Facility` interface and a `Flight Alert` object that implements the `Alert` interface. From there, you can define a concrete link type from `Airport` to `Flight Alert` to satisfy the `Facility` interface’s link type constraint.
## Link target: Object type
当 interface 与目标之间的关系是具体的，并且该具体性应由 link type constraint 强制执行时，您应该使用类型为 `object type` 的 link target。

You should use a link target of type `object type` when the relationship between the interface and the target is concrete and the specificity should be enforced by the link type constraint.
例如，您可以定义一个链接到 `Airlines` object type 的 `Facility` interface。该 interface link 将建模以下事实：无论设施类型是什么，您都期望它具有一个指向其所服务特定航空公司的链接。

For example, you could define a `Facility` interface that links to the `Airlines` object type. This interface link would model the fact that no matter what the facility type is, you expect it to have a link to the specific airlines that it serves.
## Cardinality
Interface link types 可以进一步指定为具有 `ONE` 或 `MANY` 基数（cardinality）。这些基数分别类似于一对一和一对多建模。`ONE` 基数表示实现该 interface 的每个 object 应链接到目标类型的一个 object。`MANY` 基数表示实现该 interface 的每个 object 可以链接到目标类型的任意数量的 object。

Interface link types can further be specified to have a `ONE` or `MANY` cardinality. These cardinalities are analogous to one-to-one and one-to-many modeling, respectively. A `ONE` cardinality indicates that each object implementing the interface should link to one object of the target type. A `MANY` cardinality indicates that each object implementing the interface may link to any number of objects of the target type.
您应根据 Ontology 的建模需求在 `ONE` 和 `MANY` 之间做出选择。在某些情况下，将链接的基数限制为单个 object 可能更为合理。例如，您可能希望将 `Driver's License` 与 `Person` 之间的关系建模为 `SINGLE` 基数链接，因为每个执照只能属于一个具体的个人。如果关系允许更大的灵活性，例如 `Company` 与其 `Shareholders` 之间的关系，您可能希望使用 `MANY` 基数链接，以表示每个公司可以拥有一个或多个具体股东。

You should decide between using `ONE` or `MANY` based on the modeling needs for your Ontology. In some cases, it may make more sense to restrict the cardinality of the link to a single object. For example, you may want to model the relationship between a `Driver's License` and a `Person` as a `SINGLE` cardinality link since each license can only belong to a single concrete individual. If the relationship allows for more flexibility, such as with a `Company` and its `Shareholders`, you may want to use a `MANY` cardinality link to signify that each company can have one or more concrete shareholders.