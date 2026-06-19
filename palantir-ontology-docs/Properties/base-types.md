<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/base-types/
---
# Base types
Property base type 定义了可存储在 property 中的数据类型。有关所有受支持的 property base type 的完整参考，请参阅 [properties overview](./properties-overview.md/#supported-property-types)。

Property base types define the kind of data that can be stored in a property. For a complete reference of all supported property base types, see the [properties overview](./properties-overview.md/#supported-property-types).
**Base type** 用于在 objects 上定义 properties。property 的 base type 决定了用户应用程序中该 property 可用的操作集合。除 `Map` 和 `Binary` 类型外，所有 field type 都是有效的 base type。

**Base types** are used to define properties on objects. The base type of a property determines the set of operations available for that property in user applications. All field types are valid base types except for `Map` and `Binary` types.
Base type 还包括以下高级类型：

Base types also include the following advanced types:
* **Vector:** 一种用于在 objects 上存储 [vectors](/docs/foundry/announcements/2023-11/#configure-a-vector-property-type) 的类型，用于语义搜索。

* **`Geopoint`:** 一种用于定义表示地理 [points](/docs/foundry/geospatial/ontology/#points) 的 properties 的类型。

* **`Geoshape`:** 一种用于定义表示地理 [shapes](/docs/foundry/geospatial/ontology/#polygons-and-lines) 的 properties 的类型。

* **Attachment:** 一种用于在 objects 上存储文件的类型，用于 [functions on objects](/docs/foundry/functions/attachments/)。

* **Time series:** 一种用于将 property 定义为 [time series](/docs/foundry/time-series/time-series-overview/) 的类型。

* **Media reference:** 一种用于定义 [media file reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) 的类型。

* **Cipher text:** 一种用于存储使用 [Cipher](/docs/foundry/cipher/overview/) 编码的字符串值的类型。

* **Struct:** 一种用于定义具有 [multiple fields](/docs/foundry/object-link-types/structs-overview/) 的基于 schema 的 properties 的类型。

* **Vector:** A type for storing [vectors](/docs/foundry/announcements/2023-11/#configure-a-vector-property-type) on objects for use in a semantic search.
* **`Geopoint`:** A type for defining properties that represent geographic [points](/docs/foundry/geospatial/ontology/#points).
* **`Geoshape`:** A type for defining properties that represent geographic [shapes](/docs/foundry/geospatial/ontology/#polygons-and-lines).
* **Attachment:** A type for storing files on objects for use with [functions on objects](/docs/foundry/functions/attachments/).
* **Time series:** A type for defining a property as a [time series](/docs/foundry/time-series/time-series-overview/).
* **Media reference:** A type for defining a [reference to a media file](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references).
* **Cipher text:** A type for storing a string value encoded with [Cipher](/docs/foundry/cipher/overview/).
* **Struct:** A type for defining schema-based properties with [multiple fields](/docs/foundry/object-link-types/structs-overview/).
所有 base type 都可以用于数组中，以表示 property 的多个值，但 `Vector` 和 `Time series` 类型除外。

All base types may be used in arrays to represent multiple values for a property, excluding the `Vector` and `Time series` types.
## Complex property base types
某些 property base type 需要额外配置或具有特定的使用场景。有关以下 property base type 的信息，请参阅以下章节：

Some property base types require additional configuration or have specific use cases. Refer to the sections below for information on the following property base types:
* **[Media references](#media-references)：** 引用存储在 media sets 中的 media items。

* **[Struct types](#structs)：** 具有多个字段的复杂结构化数据。

* **[Media references](#media-references):** Reference media items stored in media sets.
* **[Struct types](#structs):** Complex structured data with multiple fields.
### Media references
**Media reference** property type 允许您在 objects 上拥有 media，例如图像、视频、音频文件和文档。[Media reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) 指向 [media set](/docs/foundry/data-integration/media-sets/) 中的特定 media item。media reference 包含有关 media file 的信息，这意味着 Foundry 可以在使用 media reference 的任何位置显示该 media。

A **media reference** property type allows you to have media on your objects, such as images, videos, audio files, and documents. A [media reference](/docs/foundry/media-sets-advanced-formats/media-overview/#media-references) points to a specific media item within a [media set](/docs/foundry/data-integration/media-sets/). The media reference contains information about the media file, which means Foundry can display the media wherever the media reference is used.
#### Media reference format
以下是一个 media reference 示例：

Below is an example media reference:
```json
{
"mimeType": "image/png",
"reference": {
"type": "mediaSetViewItem",
"mediaSetViewItem": {
"mediaSetRid": "ri.mio.main.media-set.00000000-0000-0000-0000-00000000000",
"mediaSetViewRid": "ri.mio.main.view.00000000-0000-0000-0000-00000000000",
"mediaItemRid": "ri.mio.main.media-item.00000000-0000-0000-0000-00000000000"
}
}
}
```
Media reference 包含以下内容：

The media reference includes the following:
* **`mimeType`：** 文件的 media type。

* **`reference`：** 包含 media set RID、view RID 和特定 media item RID 的 reference。

* **`mimeType`:** The file's media type.
* **`reference`:** A reference containing the media set RID, view RID, and specific media item RID.
#### Configure media reference properties
具有 media reference properties 的 Object Type 由 dataset 支持。支持的 dataset 必须包含一个 media reference 列，该列将映射到 media reference property。此列类型专为存储 media reference 值而设计，并确保 ontology objects 与 media sets 之间的正确集成。

Object types with media reference properties are backed by a dataset. The backing dataset must include a media reference column, which will map to the media reference property. This column type is specifically designed to store media reference values and ensures proper integration between your ontology objects and media sets.
![A media reference property's source.](/docs/resources/foundry/object-link-types/media-reference-source.png)
此外，media reference property 必须具有一个 **media source**，可以在 object type 的 **Capabilities** 选项卡中进行配置。此 media source 应为 media references 所指向的 media set。

Additionally, a media reference property must have a **media source**, which can be configured in the **Capabilities** tab of the object type. This media source should be the media set that the media references point to.
![Media reference properties in the "Capabilities" tab.](/docs/resources/foundry/object-link-types/media-reference-media-source.png)
### Structs
**Struct** 是一种 ontology 属性基础类型，允许用户创建具有多个字段的基于 schema 的 property。Struct property 是从 struct 类型的 dataset 列创建的。要了解更多关于 struct 的信息，请参阅完整的 [struct](/docs/foundry/object-link-types/structs-overview/) 文档。

A **struct** is an ontology property base type that allows users to create schema-based properties with multiple fields. Struct properties are created from struct type dataset columns. To learn more about structs, refer to the complete [struct](/docs/foundry/object-link-types/structs-overview/) documentation.