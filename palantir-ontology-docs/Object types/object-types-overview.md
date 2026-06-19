<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/object-types-overview/
---
# Object types
**Object type** 是真实世界实体或事件的 schema 定义。

**Object 或 object instance** 是指 Object Type 的单个实例；一个 object 对应于一个真实世界的实体或事件。

**Object set** 是指多个 object instances 的集合；也就是说，object set 代表一组真实世界的实体或事件。

An **object type** is the schema definition of a real-world entity or event.
An **object or object instance** refers to a single instance of an object type; an object corresponds to a single real-world entity or event.
An **object set** refers to a collection of multiple object instances; that is, an object set represents a group of real-world entities or events.
例如，在 Ontology Manager 中，您可以创建一个 `Employee` Object Type，用于定义"All employees"或该类型所有对象的特征。Object 是指 `Employee` Object Type 的单个实例，例如假设的员工"Melissa Chang"、"Akriti Patel"或"Diego Rodriguez"。像"All tenured employees"这样的一组对象就代表一个 object set。

For example, in the Ontology Manager, you may create an `Employee` object type that defines the characteristics for “All employees” or all objects of that type. An object refers to a single instance of the `Employee` object type, like the notional employees “Melissa Chang”, “Akriti Patel”, or “Diego Rodriguez.” A group of objects like “All tenured employees” represents an object set.
同样地，在 Ontology Manager 中，您可以创建一个 `Flight` Object Type，用于定义"All flights"或该类型所有对象的特征。Object 是指 `Flight` Object Type 的单个实例，例如"JFK → SFO 2021-02-24"或"TLV → LHR 2020-04-16"。像"All arrived flights"这样的一组对象就代表一个 object set。

Similarly, in the Ontology Manager, you may create a `Flight` object type that defines characteristics for “All flights” or all objects of that type. An object refers to a single instance of the `Flight` object type, like “JFK → SFO 2021-02-24” or “TLV → LHR 2020-04-16.” A group of objects like “All arrived flights” represents an object set.
支撑 Ontology 的概念在 dataset 的结构中具有类似的概念。Ontology 中 Object Type 的定义类似于 dataset 的定义，而 Object 的定义类似于 dataset 中一行的定义。Object set 的定义类似于 dataset 中一组经过筛选的行。例如，一个 `Employee` dataset 可以定义"All employee rows"的 schema。在这种情况下，一行对应于单个员工，如"Melissa Chang"、"Akriti Patel"或"Diego Rodriguez"。如果您根据 tenure 过滤该 dataset，您将获得一组代表"All tenured employees"的行。

The concepts underpinning the Ontology have analogous concepts in the structure of a dataset. The definition of an object type in the Ontology is analogous to that of a dataset, while the definition of an object is analogous to that of a row in the dataset. The definition of an object set is analogous to a filtered set of rows in a dataset. For example, an `Employee` dataset may define the schema for “All employee rows.” In this case, a single row refers to a single employee, like “Melissa Chang,” “Akriti Patel,” or “Diego Rodriguez." If you filter the dataset based on tenure, you will have a set of rows that represent “All tenured employees.”
Foundry Ontology 并非一个抽象的数据模型，而是将每个 ontology 概念映射到组织的实际数据，使该数据资产能够为实际应用提供支持。通过在 Ontology Manager 中向 Object Type 添加 backing datasources，可以在 user applications 中创建和显示 Objects。要创建 `Employee` 类型的对象，组织将向 `Employee` Object Type 添加 backing datasources，并将其员工目录和其他企业数据接入 Ontology。

Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. Objects are created and displayed in user applications by adding backing datasources to an object type in the Ontology Manager. To create objects of type `Employee`, an organization will add backing datasources to the `Employee` object type and connect their employee directory and other enterprise data into the Ontology.
首先，请了解如何 [create an object type](/docs/foundry/object-link-types/create-object-type/)。

Get started by learning how to [create an object type](/docs/foundry/object-link-types/create-object-type/).