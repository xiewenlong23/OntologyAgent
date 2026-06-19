<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/struct-main-fields/
---
# Struct main fields \[Beta]
> **ℹ️ 注意: Beta**

> Struct main fields 处于 [beta](/docs/foundry/platform-overview/development-life-cycle/) 阶段，可能在您的注册环境中尚不可用。在积极开发过程中，功能可能会有所变更。
> **ℹ️ 注意: Beta**

> Struct main fields are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.
**Struct main fields** 使您能够指定 [struct](/docs/foundry/object-link-types/structs-overview/) 的核心值和补充元数据。例如，一个 `Address` struct 可能包含将 `streetName` 和 `postalCode` 作为其主要值的字段，而其他字段（如 `collectionDate` 和 `collectorName`）则表示描述该 `Address` 如何获取的元数据。

**Struct main fields** enable you to designate a [struct's](/docs/foundry/object-link-types/structs-overview/) core value and supplementary metadata. For example, an `Address` struct may contain fields capturing `streetName` and `postalCode` as its main values, while other fields like `collectionDate` and `collectorName` represent metadata that describe how the `Address` was obtained.
许多 struct properties 都遵循这种模式：一个或多个字段包含您最希望在应用程序中显示的主要数据，而其他字段则提供上下文、跟踪信息或审计详细信息。

Many struct properties follow this pattern: one or more fields contain the primary data you care most about displaying in applications, while other fields provide context, tracking information, or audit details.
您可以将任何 [支持的 struct field types](/docs/foundry/object-link-types/structs-overview/#struct-configuration) 指定为 main fields。

You can designate any of the [supported struct field types](/docs/foundry/object-link-types/structs-overview/#struct-configuration) as main fields.
## When to use struct main fields
在以下情况下使用 struct main fields：

Use struct main fields when:
* 您的 struct 包含核心值字段以及表示补充元数据的字段。
* 您希望获得更清晰的表格显示效果，同时不丢失对元数据的访问。

* 您需要仅使用 struct 中的单个字段或字段子集来 [implement interfaces](/docs/foundry/interfaces/implement-interface/)。

* Your struct contains core value fields in addition to fields that represent supplementary metadata.
* You want cleaner table displays without losing access to metadata.
* You need to [implement interfaces](/docs/foundry/interfaces/implement-interface/) using only a single field or subset of fields from a struct.
## Configure struct main fields
1. 导航至 **Ontology Manager**。

2. 通过在左侧面板的 **Resources** 下选择 **Object types** 来搜索并选择您的 object type。

3. 从您 object type 的 **Properties** 选项卡中选择要配置的 struct property。

4. 从右侧 property editor 面板中出现的 **General** 选项卡的 **Struct fields** 部分选择要指定的字段。

1. Navigate to **Ontology Manager**.
2. Search for and select your object type by choosing **Object types** under **Resources** in the left panel.
3. Select the struct property to configure from your object type's **Properties** tab.
4. Choose the field to designate from the **Struct fields** section of the **General** tab that appears in the property editor panel on the right.

> 📷 **[图片: Main fields 配置位置]**

> 📷 **[图片: Main fields configuration location]**

5. 在选择 **Confirm** 之前，请在 **Edit {propertyName} struct field** 弹出窗口中开启 **Struct main field**。您可以指定多个 main fields，并通过点击并拖动字段面板来重新排列它们以提升清晰度。

5. Toggle on **Struct main field** in the **Edit {propertyName} struct field** popup window before you select **Confirm**. You can designate multiple main fields and reorder them for clarity by clicking and dragging a field's panel.

> 📷 **[图片: Struct main field toggle]**

> 📷 **[图片: Struct main field toggle]**

6. **保存** 您的更改。已配置的 main field 会在 **Struct fields** 列表中显示一个 **Struct main field** 标签。

6. **Save** your changes. Configured main fields display a **Struct main field** tag in the **Struct fields** list.

> 📷 **[图片: Struct main field tags]**

> 📷 **[图片: Struct main field tags]**

## How struct main fields appear in applications
支持 struct main fields 的应用在紧凑视图中仅显示 main fields，例如 [Workshop](/docs/foundry/workshop/overview/) 中的 [Object Table](/docs/foundry/workshop/widgets-object-table/) 和 [Object List](/docs/foundry/workshop/widgets-object-list/) widgets，同时提供通过展开视图或悬停来访问完整 struct 的方式。这使您能够快速浏览最重要的数据，而无需查看每个 struct field，同时在需要时仍可以检查完整的 struct。

Applications that support struct main fields display only the main fields in compact views, like the [Object Table](/docs/foundry/workshop/widgets-object-table/) and [Object List](/docs/foundry/workshop/widgets-object-list/) widgets in [Workshop](/docs/foundry/workshop/overview/), while providing access to the full struct through an expanded view or upon hover. This enables you to quickly scan the most important data without seeing every struct field, while still being able to inspect the complete struct when needed.
应用通过以下几种方式支持 struct main fields：

Applications support struct main fields in several ways:
* **仅 main fields：** 在表格或摘要卡片等紧凑视图中仅显示 main fields。

* **main fields 配合悬停：** 默认显示 main fields，并在悬停时显示元数据 fields。

* **完整 struct：** 在需要完整信息的详细视图或表单中显示所有 fields。

* **Main fields only:** Display only main fields in compact views like tables or summary cards.
* **Main fields with hover:** Show main fields by default and reveal metadata fields on hover.
* **Full struct:** Display all fields in detailed views or forms where complete information is needed.
## Use struct fields with interfaces
您可以将任何 struct field 映射到一个 interface property。在实现 interface 时，您可以从 struct property 中选择一个特定的 field 来满足 interface 合约并满足 property 要求。

You can map any struct field to an interface property. When implementing an interface, you can select a specific field from a struct property to satisfy the interface contract and fulfill the property requirement.
例如，如果 interface 要求一个名为 `cityName` 的 `String` property，您可以使用 struct property 的 `city` field 来满足该要求。interface 选择器会显示所有可用的 struct fields 及其类型，允许您选择合适的 field。

For example, if an interface requires a `String` property called `cityName`, you can fulfill it using a struct property's `city` field. The interface picker displays all available struct fields with their types, allowing you to choose the appropriate field.

> 📷 **[图片: Selecting a struct field to map to an interface property]**

> 📷 **[图片: Selecting a struct field to map to an interface property]**

将 struct field 映射到 interface property 后，implementation 会显示 struct property 以及正在使用的特定 field。

After mapping a struct field to an interface property, the implementation shows the struct property and the specific field being used.

> 📷 **[图片: Mapped struct field to interface property]**

> 📷 **[图片: Mapped struct field to interface property]**

Main fields 在选择器中使用 **Struct main field** 标签标记，便于识别。但是，您可以从 struct 中选择任何 field，无论其是否被指定为 main field。

Main fields are indicated with a **Struct main field** tag in the picker, making them easy to identify. However, you can select any field from the struct regardless of whether it is designated as a main field.
## Combine main fields with property reducers
将 struct main fields 与 [property reducers](/docs/foundry/object-link-types/property-reducers/) 结合使用，以在 struct array property 表示和 interface implementation 中实现更大的灵活性。单个 struct array property 可以实现需要 `Struct Array`、main field 的数组类型、`Struct` 或 main field 的基础类型的 interfaces。

Combine struct main fields with [property reducers](/docs/foundry/object-link-types/property-reducers/) to enable additional flexibility in struct array property representation and interface implementation. A single struct array property can implement interfaces requiring `Struct Array`, the main field's array type, `Struct`, or the main field's base type.
有关详细示例和实现选项，请参阅 [property reducers 文档](/docs/foundry/object-link-types/property-reducers/#combine-property-reducers-with-struct-main-fields)。

See the [property reducers documentation](/docs/foundry/object-link-types/property-reducers/#combine-property-reducers-with-struct-main-fields) for detailed examples and implementation options.
## Limitations and considerations
* **Query 行为：** Query 在所有 struct fields 上运行，而不仅仅是 main fields。您可以基于 struct 中的任何 field 进行搜索和过滤。

* **Query behavior:** Queries operate on all struct fields, not just main fields. You can search and filter based on any field in the struct.
## FAQs
### Can I change which fields are main fields later?
可以，您可以随时在 Ontology Manager 中重新配置主字段。这可能会导致某些 interface 实现失效，您需要进行更新。

Yes, you can reconfigure main fields in Ontology Manager at any time. This may render some interface implementations invalid, which you will need to update.
### Do main fields affect how Foundry stores data?
不会。主字段仅影响 Foundry 显示数据和实现 interfaces 的方式。底层的 struct 包含所有字段并保留完整信息，因此所有字段仍然可查询和访问。

No, main fields only affect how Foundry displays data and implements interfaces. The underlying struct contains all fields with full fidelity, so all fields remain queryable and accessible.
### Can I use main fields with struct arrays?
可以。主字段可同时用于*单一* struct 属性和 struct 数组属性。与 [reducers](/docs/foundry/object-link-types/property-reducers/) 结合使用时，您可以在 Foundry 表示该属性时获得最大的灵活性。

Yes. Main fields work with *both* single struct properties and struct array properties. When combined with [reducers](/docs/foundry/object-link-types/property-reducers/), you get maximum flexibility in how Foundry represents the property across applications.
### Do I need to configure main fields to use struct fields with interfaces?
不可以。您可以将任何 struct 字段映射到 interface 属性，无论其是否被指定为主字段。主字段仅在 interface 选择器中提供视觉指示，并影响应用程序在紧凑视图中显示该 struct 的方式。

No. You can map any struct field to an interface property regardless of whether it is designated as a main field. Main fields simply provide a visual indicator in the interface picker and affect how applications display the struct in compact views.