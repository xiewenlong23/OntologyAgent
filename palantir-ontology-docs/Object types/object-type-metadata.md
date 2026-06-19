<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/object-type-metadata/
---
# Metadata reference
Object Type 在 Ontology 中由以下元数据（metadata）表示：

An object type is represented in the Ontology by the following metadata:
* **ID:** Object Type 的唯一标识符，主要用于在配置 application 时引用此类型的对象。例如，`employee` 可以是 `Employee` Object Type 的 ID。

* **RID:** 为 Foundry 中的每个资源自动生成的唯一标识符。Object Type 的 RID 将在整个平台的错误消息中被引用。

* **Icon:** 用作 Object Type 视觉标识符的图片和颜色，当用户在 user application 中查看此类型的对象时显示。例如，可以使用人物图标来表示 `Employee` Object Type。

* **Display name:** 在 user application 中向访问此类型对象的任何人显示的名称。例如，`Employee` Object Type 的 display name 可以是 `Employee`。

* **Plural display name:** 在 user application 中向访问此类型多个对象的任何人显示的名称。例如，`Employee` Object Type 的 plural display name 可以是 `Employees`。

* **Description:** 关于 Object Type 的说明性文本，任何人都可以在 user application 中阅读。例如，`Employee` Object Type 的 description 可以是 `All full-time and part-time employees of Organization X`。

* **Groups:** Group 是帮助您对 Object Type 进行分类的标签。例如，`Employee` Object Type 可以属于 `HR` 和 `Employee 360` 这两个 groups。

* **API name:** 在代码中以编程方式引用 Object Type 时使用的名称。例如，`Employee` Object Type 的 API name 可以是 `Employee`。阅读更多关于 [API names](/docs/foundry/functions/api-objects-links/) 的信息。

* **Visibility:** 向 user application 提示应如何突出显示该 Object Type。`prominent` 的 Object Type 会使 applications 优先向用户显示此 Object Type。`hidden` 的 Object Type 将不会出现在 user applications 中。默认情况下，`Employee` Object Type 的 visibility 为 `normal`。

* **Status:** 向用户和其他 Ontology builders 表明 Object Type 在开发过程中的所处阶段。可以是 `active`、`experimental` 或 `deprecated`。默认情况下，`Employee` Object Type 的 status 为 `experimental`。阅读更多关于 [statuses](/docs/foundry/object-link-types/metadata-statuses/) 的信息。

* **Index status:** Object Type 及其 backing datasources 上次 reindex 的状态。可以是 `success`、`failed` 或 `not started`。阅读更多关于 [index statuses](/docs/foundry/object-databases/object-storage-v1/) 的信息。

* **Writeback:** 表明该 Object Type 是否已生成 writeback dataset，以及是否允许终端用户 `enabled` 或 `disabled` 编辑此类型的对象。阅读更多关于 [writeback datasets](/docs/foundry/object-link-types/allow-editing/) 的信息。

* **ID:** A unique identifier of the object type, primarily used to reference objects of this type when configuring an application. For example, `employee` may be the ID of the `Employee` object type.
* **RID:** An automatically generated unique identifier for every resource in Foundry. An object type’s RID will be referenced in error messages across the platform.
* **Icon:** A picture and color used as a visual identifier of the object type that will appear in user applications when a user views an object of this type. For example, the person icon may be used to depict the `Employee` object type.
* **Display name:** The name shown to anyone accessing an object of this type in user applications. For example, the display name for the `Employee` object type may be `Employee`.
* **Plural display name:** The name shown to anyone accessing multiple objects of this type in user applications. For example, the plural display name for the `Employee` object type may be `Employees`.
* **Description:** Explanatory text about the object type that anyone can read in user applications. For example, the description of the `Employee` object type may be `All full-time and part-time employees of Organization X`.
* **Groups:** A group is a label that helps you categorize your object types. For example, the `Employee` object type may belong to groups `HR` and `Employee 360`.
* **API name:** The name used when referring to the object type programmatically in code. For example, the API name of the `Employee` object type may be `Employee`. Read more about [API names](/docs/foundry/functions/api-objects-links/).
* **Visibility:** An indication to user applications for how prominently to display the object type. A `prominent` object type will lead applications to show this object type first to users. A `hidden` object type will not appear in user applications. By default, the `Employee` object type will have visibility `normal`.
* **Status:** A signal to users and other Ontology builders about where in the development process the object type stands. It can be `active`, `experimental`, or `deprecated`. By default, the `Employee` object type will have status `experimental`. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* **Index status:** The status of the last reindex of the object type and its backing datasources. It can be `success`, `failed`, or `not started`. Read more about [index statuses](/docs/foundry/object-databases/object-storage-v1/).
* **Writeback:** An indication of whether the object type has a writeback dataset generated, and whether allowing end users to make edits to objects of this type is `enabled` or `disabled`. Read more about [writeback datasets](/docs/foundry/object-link-types/allow-editing/).
[了解更多关于在 Ontology 中创建和配置 Object Type 的信息，以及关于 Object Type 元数据验证要求的信息。](/docs/foundry/object-link-types/create-object-type/)

[Learn more about creating and configuring an object type in the Ontology and about validation requirements for object type metadata.](/docs/foundry/object-link-types/create-object-type/)
[了解更多关于 Properties（Object Type 的特征）的信息。](/docs/foundry/object-link-types/properties-overview/)

[Learn more about Properties (characteristics of an object type).](/docs/foundry/object-link-types/properties-overview/)