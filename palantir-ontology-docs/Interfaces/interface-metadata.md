<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/interfaces/interface-metadata/
---
# Metadata reference
Interface 在 Ontology 中由以下元数据表示：

An interface is represented in the Ontology by the following metadata:
* **RID：** 为 Palantir 中的每个资源自动生成的唯一标识符。Interface 的 RID 将在整个平台的错误消息中被引用。

* **Icon（图标）：** 用作视觉标识符的图片和颜色，当用户在应用程序中查看该 interface 时会显示。Interface 的图标周围有虚线，以将其与 object type 图标在视觉上区分开来。例如，带有虚线包围的建筑图标可用于表示 `Facility` interface。

* **Display name（显示名称）：** 在用户应用程序中，任何访问该 interface 的人所看到的名称。例如，`Facility` interface 的显示名称可以是 "Facility"。

* **Description（描述）：** 关于该 interface 的说明性文本，任何人都可以在用户应用程序中阅读。例如，`Facility` interface 的描述可以是 "An abstract object type interface for representing airline facilities"。

* **API name（API 名称）：** 在代码中以编程方式引用该 interface 时使用的名称。例如，`Facility` interface 的 API 名称可以是 `facility`。

* **Status（状态）：** 向用户和 Ontology 构建者发出的信号，用于表示该 interface 在开发过程中所处的阶段。可以是 `active`、`experimental`、`example` 或 `deprecated`。默认情况下，`Facility` interface 将具有 `experimental` 状态。了解更多关于 [statuses](/docs/foundry/object-link-types/metadata-statuses/) 的信息。

* **Searchable（可搜索）：** 一个布尔值，用于指定该 interface 是否可搜索。可搜索的 interface 使用户能够一次性加载或搜索该 interface 的所有 object。可搜索的 interface 最多可包含 50 个实现它的 object type，而非可搜索的 interface 最多可包含 1,000 个。默认情况下，`Facility` interface 将是可搜索的。

* **RID:** An automatically generated unique identifier for every resource in Palantir. An interface’s RID will be referenced in error messages across the platform.
* **Icon:** A picture and color used as a visual identifier that will appear in applications when a user views this interface. Interfaces have dashed lines around their icons to visually distinguish them from object type icons. For example, the building icon surrounded by dashed lines may be used to depict the `Facility` interface.
* **Display name:** The name shown to anyone accessing this interface in user applications. For example, the display name for the `Facility` interface may be "Facility".
* **Description:** Explanatory text about the interface that anyone can read in user applications. For example, the description of the `Facility` interface may be "An abstract object type interface for representing airline facilities".
* **API name:** The name used when referring to the interface programmatically in code. For example, the API name of the `Facility` interface may be `facility`.
* **Status:** A signal to users and Ontology builders about where in the development process the interface stands. It can be `active`, `experimental`, `example`, or `deprecated`. By default, the `Facility` interface will have the `experimental` status. Learn more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* **Searchable:** A boolean value that specifies whether the interface is searchable. Searchable interfaces enable users to load or search all objects of the interface at once. Searchable interfaces are limited to 50 implementing object types, whereas non-searchable interfaces are limited to 1,000. By default, the `Facility` interface will be searchable.