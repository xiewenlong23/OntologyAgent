<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/required-properties/
---
# Required properties
Required properties 是 object type 中必须具有值的 properties。您可以使用此 object type property 来验证是否存在该 property 值为 null 的 objects，如果该 property 是 array property，则验证其值是否为空数组。此验证适用于来自 backing datasource 的数据以及通过 actions 进行的编辑。

Required properties are object type properties that must have a value. You can use this object type property to validate that there are no objects that have a null value for this property, or an empty array if it is an array property. This validation applies to data from the backing datasource and edits via actions.
## Summary of required properties
在使用 required properties 时，请牢记以下几点：

When working with required properties, keep the following in mind:
* **验证发生在数据被索引到 object 时：** 对 null 值的检查发生在 backing datasources 被索引到 Object Storage 时。这意味着，如果 required property 所对应的 backing column 包含 null 值，ontology 的修改本身仍将成功。

* **Array properties 不能为空：** 将 array property 设置为 required 可确保至少存在一个 item。

* **通过 actions 进行的更改会在 apply 时进行验证：** 如果您尝试通过 action 将 null 或空值写入 property，则该 action 将无法执行。

* **仅在 Object Storage V2 中可用：** Required properties 仅受使用 Object Storage V2 的 object types 支持。

* **Validation happens when data is being indexed into the object:** The check for null values happens as backing datasources are indexed into Object Storage. This means that the ontology modification itself will succeed if the column backing a required property contains null values.
* **Array properties cannot be empty:** Setting an array property to required ensures the presence of at least one item.
* **Changes via actions are validated at apply time:** If you attempt to write a null or empty value to a property via an action, the action will fail to execute.
* **Available only in Object Storage V2:** Required properties are only supported by object types leveraging Object Storage V2.
### Create a required property
1. 导航至 **Ontology Manager**。

2. 选择 object type，然后选择您要设置为 required 的 property。

3. 选择 **Create Property** 并填写所需的详细信息，包括 property 的 name、type 和 description。

4. 在 **Configuration** 部分下，打开 **Required** 开关。

5. **保存** 您对 Ontology 的更改，并等待 reindex 完成。

1. Navigate to **Ontology Manager**.
2. Choose the object type, and then the property you want to set as required.
3. Select **Create Property** and fill in the required details, including the property name, type, and description.
4. Under the **Configuration** section, toggle on the **Required** toggle.
5. **Save** your changes to the Ontology and wait for the reindex to be completed.
请注意，如果 property 的 backing column 中当前存在任何 null 值，reindex 将失败。要解决此问题，您必须更新 backing datasource 使该列不再包含 null 值，或者取消将 property 设置为 required。

Note that if there is any null value currently set on the backing column for the property, the reindex will fail. To fix this, you must either update the backing datasource to no longer have nulls in the column, or unset the property as required.

> 📷 **[图片: Required property toggled in configuration pane.]**

> 📷 **[图片: Required property toggled in configuration pane.]**

### Required properties that allow empty arrays
您可以将您的 required property 配置为允许空数组。这意味着该 property 仍会拒绝 null 值，但会接受空数组。这对于不能为 null 但可以配置为允许空数组的 mandatory control properties 非常有用。了解更多关于 [mandatory control properties](/docs/foundry/object-link-types/mandatory-control-properties/) 的信息。

You can configure your required property to allow empty arrays. This means that the property will still reject null values, but will accept empty arrays. This is useful for mandatory control properties which can never be null, but can be configured to allow empty arrays. Learn more about [mandatory control properties](/docs/foundry/object-link-types/mandatory-control-properties/).
需要特别注意的是，Actions 会将空数组写入任何映射到 parameter 的 property，即使该 parameter 未被设置。这意味着，如果您有一个允许空数组的 required property，并且在 Action 中将该 parameter 留空，则该 Action 将成功执行并将空数组写入 property。如果您不希望出现这种行为，并希望强制用户始终通过 Actions 为此 property 设置值，则不应在 required property 上允许空数组。

It is important to note that Actions will write an empty array to any property that is mapped to a parameter, but the parameter is not set. This means that if you have a required property that allows empty arrays, and you leave the parameter blank in an Action, the Action will succeed and write an empty array to the property. If you do not want this behavior and want to enforce that users always set a value for this property via Actions, you should not allow empty arrays on your required property.

> 📷 **[图片: Advanced required property configuration]**

> 📷 **[图片: Advanced required property configuration]**

### Required properties for object types with multiple backing datasources
您偶尔可能会遇到在由多个 datasources 支持的 object types 的 required properties 中出现 null 值的情况。当 object 的记录存在于某些 datasources 中，但在提供 required property 的 datasource 中不存在时，就会发生这种现象。

You may occasionally encounter situations where null values appear in required properties of object types backed by multiple datasources. This phenomenon occurs when a record for the object is present in some datasources, but absent in the datasource that supplies the required property.
以下示例说明了此行为。假设存在一个具有两个 backing datasources 的 `Movie` object type，以及一个 required 的 `Genre` property。

The following example illustrates this behavior. Assume there is a `Movie` object type with two backing datasources and a `Genre` property that is required.
**Datasource 1**
**Datasource 1**
| Movie Id | Title                | Box office | Regions                    |
| -------- | -------------------- | ---------- | -------------------------- |
| 101      | The Adventure Begins | 200m       | \["USA", "Canada", "UK"]    |
| 102      | Love in the City     | 75m        | \[]                         |
| 103      | Galactic Battles     | 500m       | \["USA", "UK", "Australia"] |
**Datasource 2**
**Datasource 2**
| Movie Id | Budget | Genre (Required) | Director           |
| -------- | ------ | ---------------- | ------------------ |
| 101      | 50m    | Adventure        | Michael John Smith |
| 102      | 20m    | Romance          | Jane Doe           |
| 103      | 150m   | Sci-Fi           |                    |
如果将一条新的 `Movie` 添加到两个 backing datasources 但未提供 `Genre` 的值，则该数据将无法索引到 Ontology。

If a new `Movie` is added to both backing datasources without providing a value for `Genre`, it will fail to index to the Ontology.
然而，假设只有 Datasource 1 拥有新 `Movie` object 的一行数据。

However, suppose only Datasource 1 had a row for the new `Movie` object.
**Datasource 1**
**Datasource 1**
| Movie Id | Title                | Box office | Regions                    |
| -------- | -------------------- | ---------- | -------------------------- |
| 101      | The Adventure Begins | 200m       | \["USA", "Canada", "UK"]    |
| 102      | Love in the City     | 75m        | \[]                         |
| 103      | Galactic Battles     | 500m       | \["USA", "UK", "Australia"] |
| 104      | Happy Ending         | 150m       | \["UK", "FRANCE"]           |
**Datasource 2**
**Datasource 2**
| Movie Id | Budget | Genre (Required) | Director           |
| -------- | ------ | ---------------- | ------------------ |
| 101      | 50m    | Adventure        | Michael John Smith |
| 102      | 20m    | Romance          | Jane Doe           |
| 103      | 150m   | Sci-Fi           |                    |
上述示例将成功索引到 Ontology 中，尽管生成的对象在必需 property 上没有值。

The example above will successfully get indexed into the Ontology, despite the fact that the resulting object would have no value for the required property.
| Property         | Value            |
| ---------------- | ---------------- |
| Movie Id         | 104              |
| Title            | Happy Ending     |
| Box Office       | 150m             |
| Regions          | \["UK", "FRANCE"] |
| Budget           |                  |
| Genre (Required) |                  |
| Director         |                  |
同样的情况也适用于通过 Action 编辑创建的对象。只要 `Movie` 对象只包含与 `Datasource 1` 中列相关联的 property，就可以成功创建或修改。但是，如果 Action 向对象添加了一个来自 `Datasource 2` 的 property（例如 `Budget`），则该 Action 将无效且无法执行。这是因为该对象现在将存在于 `Datasource 2` 上，因此必须设置 `Genre`。

The same applies to objects created via Action edits. `Movie` objects can be created or modified successfully, if they only contain properties tied to columns in `Datasource 1`. However if the Action adds a property to the object that is sourced from `Datasource 2`, such as `Budget`, then the Action will be invalid and will fail to execute. This is because the object will now be present on `Datasource 2` and thus `Genre` must be set.