<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/upload-media/
---
# Upload media
Action 支持通过 action 表单或表格上传媒体文件。对于 Foundry 中的大多数使用场景，推荐使用向 media reference properties 上传的方式。

Actions support uploading media files using an action form or table. For most use cases in Foundry, uploading to media reference properties is the recommended method.
Media reference properties（由 [media sets](/docs/foundry/data-integration/media-sets/) 支持）相比 attachment properties 具有以下几项优势：

Media reference properties (backed by [media sets](/docs/foundry/data-integration/media-sets/)) offer several advantages over attachment properties:
* **可扩展性：** 支持数十亿级别的文件，提供高效的存储与检索能力。

* **内置转换功能：** 支持多种媒体转换和 LLM 能力，开箱即用。
* **高级预览：** 针对支持的格式提供内置渲染和丰富的预览功能。

* **格式支持：** 支持针对标准格式和专用格式（如 NITF、GeoTIFF 和 DICOM）的定制化工作流。

* **Scalability:** Support for billions of files with efficient storage and retrieval.
* **Built-in transformations:** Many media transformations and LLM capabilities are supported and easy to use out of the box.
* **Advanced previews:** Built-in rendering and rich preview functionality for supported formats.
* **Format support:** Support for tailored workflows on both standard formats and specialized formats, such as NITF, GeoTIFF, and DICOM.
用户可以通过文件选择器 interface 上传媒体文件，文件将在 action 成功提交后持久化到 media set 中。

Users can upload media files via a file-picker interface, with files persisted to the media set upon successful action submission.
> **⚠️ 警告**

> [Format conversions](/docs/foundry/media-sets-advanced-formats/media-overview/#additional-input-formats) 仅在 action 执行完毕且媒体文件已上传至 media set 之后才会发生。
> **⚠️ 警告**

> [Format conversions](/docs/foundry/media-sets-advanced-formats/media-overview/#additional-input-formats) only happen after the action completes and the media file has been uploaded to the media set.
## Configuration
有关配置 media reference properties 和设置媒体上传 action 的详细说明，请参阅 [Configure media reference properties](/docs/foundry/object-link-types/base-types/#configure-media-reference-properties) 和 [Upload media](/docs/foundry/media-sets-advanced-formats/upload-media/)。

For detailed instructions on configuring media reference properties and setting up media upload actions, see [Configure media reference properties](/docs/foundry/object-link-types/base-types/#configure-media-reference-properties) and [Upload media](/docs/foundry/media-sets-advanced-formats/upload-media/).
## Permissions
通过 action 上传媒体的权限由 [action submission criteria](/docs/foundry/action-types/submission-criteria/) 管理。如果用户满足 action submission criteria，则他们无需对后备 media set 拥有任何权限即可上传媒体。

Permissions for uploading media via an action are managed by the [action submission criteria](/docs/foundry/action-types/submission-criteria/). If users satisfy the action submission criteria, they do not need any permissions on the backing media set to upload media.
> **ℹ️ 注意**

> 当 media set 首次添加到 object type 或被 action type 引用时，将检查其 Edit 权限。将 media set 添加到您的 ontology 会将访问控制从 media set 委托给 ontology。这意味着任何能够管理该 object type 上 action 的人，都可以控制谁有权向该 media set 上传媒体。
> **ℹ️ 注意**

> Edit permission on a media set will be checked when it is added to an object type or referenced by an action type for the first time. Adding a media set to your ontology delegates access control from the media set to the ontology. This means that anyone who can manage actions on the object type, can control who is able to upload media to the media set.