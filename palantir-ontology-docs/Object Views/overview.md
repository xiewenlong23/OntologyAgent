<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/overview/
---
# Object Views
Object View 是 object 数据的可重用表示形式。它们提供了一个中央枢纽,用于展示与 object 相关的所有信息,并包含有关 object 的关键信息,包括 property 数据、object links 和相关 applications。

Object Views are reusable representations of object data. They provide a central hub for all information related to an object and include key information about the object, including property data, object links, and related applications.
## Standard and configured Object Views
Object view 有两种类型:

There are two types of object views:
1. **Standard Object Views:** 标准化、开箱即用的表示形式,自动反映 object type 的配置。Standard Object Views 适用于所有 object types,提供了一种无需任何配置即可查看 object 数据的一致方式。[详细了解 standard Object Views。](/docs/foundry/object-views/standard-object-views/)

2. **Configured Object Views:** 使用 [Workshop](/docs/foundry/workshop/overview/) 构建的完全可定制的表示形式,您可以根据特定工作流的需求进行配置以提供情境化的体验。创建 configured Object View 后,它将成为默认视图,但用户始终可以切换回 standard Object View。

1. **Standard Object Views:** Standardized, out-of-the-box representations that automatically reflect an object type's configuration. Standard Object Views are available for all object types and provide a consistent way to view object data without any configuration. [Learn more about standard Object Views.](/docs/foundry/object-views/standard-object-views/)
2. **Configured Object Views:** Fully customizable representations built using [Workshop](/docs/foundry/workshop/overview/) that you can configure to provide contextualized experiences for specific workflows. When a configured Object View is created, it becomes the default view, though users can always switch back to the standard Object View.
Standard Object Views 与 configured Object Views 并存,作为一流(first-class)的查看选项。虽然在未创建 configured Object View 时,standard Object Views 默认显示,但即使在构建了 configured Object View 之后,它们仍然可访问。用户可以根据需要随时在 standard 和 configured Object Views 之间切换。

Standard Object Views exist alongside configured Object Views as a first-class viewing option. While standard Object Views display by default when no configured Object View is created, they remain accessible even after a configured Object View is built. Users can toggle between standard and configured Object Views at any time based on their needs.
![A standard Object View's full and panel form factors are displayed.](/docs/resources/foundry/object-views/standard-full-and-panel-object-view.png)
## Object View form factors
Standard 和 configured Object Views 都提供两种形式(form factors),以适应不同级别的详细信息。这些不同的 form factors 提供了 object 数据在不同工作流中显示方式的灵活性。

Both standard and configured Object Views are available in two form factors to accommodate different levels of detail. These different form factors offer flexibility in how object data appears across different workflows.
1. **Full Object Views:** object 的全面概览,代表所有相关信息的深入展示。

2. **Panel Object Views:** 旨在与其他 applications 集成,应专注于显示特定工作流最关键的数据。

1. **Full Object Views:** A comprehensive overview of an object, representing an in-depth display of all related information.
2. **Panel Object Views:** Intended for integration with other applications and should focus on displaying the most critical data for a specific workflow.
## Example: Configured Patient Object View
针对 `Patient` object 配置的 full Object View 可能包括:

A configured full Object View for a `Patient` object might include:
* **Core demographics, vitals, and care details:** 患者基本信息、健康状况和持续护理计划的全面概览。

* **Linked procedures, prescriptions, and diagnoses:** 医疗干预、开具的药物和确诊的合并列表,提供患者病史的整体视图。

* **Analytical trends from historical in-patient records:** 从既往住院记录中得出的洞察,突出患者健康状况随时间变化的模式和趋势。

* **Core demographics, vitals, and care details:** A comprehensive snapshot of the patient's basic information, health status, and ongoing care plans.
* **Linked procedures, prescriptions, and diagnoses:** A consolidated list of medical interventions, medications prescribed, and confirmed diagnoses, providing a holistic view of the patient's medical history.
* **Analytical trends from historical in-patient records:** Insights derived from past hospital stays, highlighting patterns and trends in the patient's health over time.
此 configured full Object View 可以作为有关患者所有相关信息的详尽资源,有助于做出更明智的医疗保健决策和制定个性化护理计划。

This configured full Object View could serve as an exhaustive resource for all relevant information about a patient, facilitating better-informed healthcare decisions and personalized care planning.
![Full patient Object View example.](/docs/resources/foundry/object-views/overview-full-object-view.png)
针对同一 `Patient` 对象配置的 Object View panel 可能仅显示人口统计和生命体征信息，因此当它出现在其他应用程序中时，可为用户提供便捷访问其工作流中最关键数据的入口。

The configured panel Object View for the same `Patient` object may only show the demographic and vital information, so when it appears in other applications it provides users with easy access to the most critical data for their workflow.
![Panel patient Object View example.](/docs/resources/foundry/object-views/overview-panel-object-view.gif)
[详细了解 object type 及其背后的 Ontology-based 数据建模概念。](/docs/foundry/ontology/core-concepts/)

[Learn more about object types and the concepts behind Ontology-based data modeling.](/docs/foundry/ontology/core-concepts/)