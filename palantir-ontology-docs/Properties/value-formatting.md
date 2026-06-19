<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/value-formatting/
---
# Add value formatting
**Value formatting**（值格式化）是指对 property 的值应用特殊的格式化器，将原始值转换为更易读的版本。在下图中，左侧（**Before**）显示的是未应用任何格式化的 `weight` 和 `value` 列。右侧（**After**）对 `weight` 列应用了单位（"kg"），`value` 列则以更紧凑的形式显示，并带有货币符号（"$100K"）。这些都是 numeric formatting（数字格式化）的示例。Ontology 还支持 date and time formatting（日期和时间格式化），以及 user ID formatting、resource RID formatting 和 artifact GID formatting。

**Value formatting** refers to applying a special formatter to the value of a property, transforming the raw value to a more readable version. In the image below, the left-hand side (**Before**) shows the `weight` and `value` columns without any formatting. The right-hand side (**After**) has a unit (“kg”) applied to the `weight` column and the `value` column is displayed in a more compact form with a currency sign (“$100K”). These are both examples of numeric formatting. The Ontology also supports date and time formatting, as well as user ID formatting, resource RID formatting, and artifact GID formatting.

> 📷 **[图片: Value formatting example]**

> 📷 **[图片: Value formatting example]**

## Supported value formatting
|Type	                   |Description	|
|---	                   |---	|
| Numeric formatting	   | Add currencies/units/prefixes, various types of notations (compact, scientific), and percentages. See the [numeric formatting section](#numeric-formatting-options) for more details. |
| Date and time formatting | Render timestamps and dates in a specific format as well as in a specific timezone. |
| Foundry ID formatting	   | Display a Foundry ID as a user's first and last name or group name. |
| Resource RID formatting  | Display a Foundry resource ID (RID) as an icon and resource name, with a clickable link that routes to that resource. |
| Artifact GID formatting  | Display an artifact global ID (GID) as an icon and artifact name, with a clickable link that routes to that artifact. |
## Add value formatting
在 property 编辑器中：

In the property editor:
1. 选择要添加 value formatting 的 property。

2. 在 properties 窗格的右侧面板上，您将看到取决于 property 基础类型的格式化类型（value formatting、numeric formatting、date and time formatting 等）。开启该格式化。

1. Select the property to which you want to add value formatting.
2. On the right hand side panel of the properties pane, you will see a type of formatting depending on the base type of the property (value formatting, numeric formatting, date and time formatting, etc.). Toggle on the formatting.

> 📷 **[图片: Value formatting toggle]**

> 📷 **[图片: Value formatting toggle]**

3. 额外的格式化选项可用于 numeric formatting 和 date and time formatting，如下所述：

* [Numeric formatting options](#numeric-formatting-options)
* [Date and time formatting options](#date-and-time-formatting-options)
4. 在选择可用的格式化选项时，您将看到 property 值在应用新格式化后如何呈现的预览。

3. Additional formatting options are available for numeric formatting and date and time formatting, as described below:
* [Numeric formatting options](#numeric-formatting-options)
* [Date and time formatting options](#date-and-time-formatting-options)
4. As you select the available formatting options, you will see a preview for how values of the property will be rendered with the new formatting applied.
### Numeric formatting options

> 📷 **[图片: Numeric formatting options]**

> 📷 **[图片: Numeric formatting options]**

| Name                   | Description | Usage |
| ---                    | --- | --- |
| **Numeric formatting** | On/Off toggle. | Toggle this to remove/add numeric formatting. |
| **Base type**	         | Contains various types of formatting available (Currency, Unit, Percentage, Prefix/Suffix, Fixed Values) as well as examples and descriptions of each type. |If `Capacity in Pounds` has an associated unit, select "Unit" from this dropdown. |
| **Use grouping**	     | Adds locale-aware comma separator.	| Toggle this on to go from 123456 to 123,456. |
| **Notation**	         | Contains Compact/Scientific and Engineer notations. | Choose compact to approximate values, like 123K. |
| **Preview result**     | View and test numeric formatting. | Add any number in the input that is similar to what you'd expect to see in your property's values for a preview of the formatting. |
### Date and time formatting options

> 📷 **[图片: Date and time formatting options]**

> 📷 **[图片: Date and time formatting options]**

|Name   |Description    |Example    |
|---    |---    |---    |
|**Date**   |Only the date (no time)    |`Wed, Jul 22, 2020`  |
|**Date and time (long)**   |Both the date and time, in long form   |`Wed, July 22, 2020, 1:00:00 PM` |
|**Date and time (short)**  |Both the date and time, in short form  |`Jul 22, 2020, 1:00 PM`  |
|**ISO instant**    |Both the date and time (ISO 8601 format)   |`2020-07-22T13:00:00.000Z`   |
|**Relative to now**    |The date relative to right now |`8 minutes ago`  |
|**Time**   |Only the time (no date)    |`1:00 pm`    |
> **ℹ️ 注意**

> 当格式化 **Relative to now**（相对于现在）时，application 仅会以相对时间的形式格式化最多 24 小时之前的内容。超过此时间后，它将以 **Date and time (short)** 形式呈现，并附带星期几：`Wed, Jul 22, 2020, 1:00 PM`。
> **ℹ️ 注意**

> When formatting **Relative to now**, applications will only format in relative terms up to 24 hours ago. After this, it will render in **Date and time (short)** form with the day of the week: `Wed, Jul 22, 2020, 1:00 PM`.

> 📷 **[图片: Relative to now]**

> 📷 **[图片: Relative to now]**

#### Time zones
如果您正在格式化时间戳，您可以指定渲染时间戳所用的时区，可以是您输入的静态时区，也可以是应用程序用户当前的时区。在输入静态时区时，您可以通过输入 UTC 偏移量或区域名称来搜索时区。

If you are formatting a timestamp, you can specify which timezone to render the timestamp, either as a static timezone that you input, or as the application user's current timezone. When entering a static timezone, you can search for a timezone by inputting the UTC offset or the locale name.
### User ID formatting
值格式化可应用于作为 Foundry/Multipass 用户 ID 或组 ID 的字符串，并通过选择 **Multipass username** 选项将其转换为显示用户的名字和姓氏或组名。当您创建了一个 [Action](/docs/foundry/action-types/overview/) 来编辑属性并将用户 ID 或组 ID 存储在某个属性字段中时，通常会使用此值格式化选项。在后端数据中，此信息将存储为用户的 Foundry 用户 ID 或组 ID，可以应用值格式化以渲染用户的名称或组名，而不是 ID。

Value formatting can be applied to strings that are Foundry/Multipass user IDs or group IDs and convert them to display the user's first and last name or the group name by selecting the **Multipass username** option. This value formatting option is typically used when you have created an [Action](/docs/foundry/action-types/overview/) that edits a property and stores a user ID or group ID in one of the property fields. In the backing data, this information will be stored as the user's Foundry user ID or group ID, and the value formatting can be applied to render the user's name or the group instead of the ID.
## FAQ
### Will this work with existing type classes?
值格式化优先于 UI 中现有的 type class。如果您同时配置了两者，将显示值格式化。但是，您可以在一个属性上使用值格式化，在另一个属性上使用 type class。

Value formatting takes precedence over existing type classes in the UI. If you have both configured, value formatting will be displayed. You can however, use value formatting on one property and type classes on another.
### Will this work with editable properties in Object Views?
值格式化支持配置用于 [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits) 的属性。具有旧版 `hubble:editable` type class 的属性将禁用值格式化。

Value formatting is supported for properties configured for [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits). Properties with the legacy `hubble:editable` type class will disable value formatting.