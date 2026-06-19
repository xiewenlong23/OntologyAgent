<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/shared-property-overview/
---
# Shared properties
**shared property** 是您的 ontology 中可以在多个 [object types](/docs/foundry/object-link-types/object-types-overview/) 上使用的 [property](/docs/foundry/object-link-types/properties-overview/)。共享属性允许在 object types 之间进行一致的数据建模以及对属性元数据的集中管理。虽然属性元数据在 objects 之间共享，但底层 object 数据并不共享。

A **shared property** is a [property](/docs/foundry/object-link-types/properties-overview/) that can be used on multiple [object types](/docs/foundry/object-link-types/object-types-overview/) in your ontology. Shared properties allow for consistent data modeling across object types and centralized management of property metadata. While property metadata is shared across objects, the underlying object data is not.
例如，在 Ontology Manager 中，您可能有 `Employee` 和 `Contractor` object types，它们都具有 `start date` 属性。通过创建 `start date` 共享属性并将其用于两个 object types，您可以使用一致的属性来建模数据，并在一个地方更新 `start date` 元数据，而不是在每个 object type 上分别更新。

For example, in Ontology Manager, you may have `Employee` and `Contractor` object types that both have the property `start date`. By creating a `start date` shared property and using it for both object types, you can model your data using a consistent property and update `start date` metadata in one place instead of on each object type.
共享属性可以[直接创建](/docs/foundry/object-link-types/create-shared-property/)，或者将 object types 上现有的属性转换为共享属性。添加到您的 ontology 后，共享属性可以[使用](/docs/foundry/object-link-types/use-shared-property/)在 object types 上，作为将数据本体化的一部分，并可以[编辑](/docs/foundry/object-link-types/edit-shared-property/)，方式类似于常规属性。

Shared properties can be [created directly](/docs/foundry/object-link-types/create-shared-property/), or existing properties on object types can be converted into shared properties. Once added to your ontology, shared properties can be [used](/docs/foundry/object-link-types/use-shared-property/) on object types as part of ontologizing your data and [edited](/docs/foundry/object-link-types/edit-shared-property/) in a manner similar to regular properties.
对象上的共享属性在其名称旁边用一个地球图标表示。

Shared properties on objects are denoted with a globe icon next to their name.

> 📷 **[图片: Ontology Manager 中的共享属性页面]**

> 📷 **[图片: Shared properties page in Ontology Manager]**

