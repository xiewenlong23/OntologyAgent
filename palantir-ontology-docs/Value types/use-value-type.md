<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/use-value-type/
---
# Use value types
一旦您 [创建了一个 value type](/docs/foundry/object-link-types/create-value-type/)，就可以在整个 Foundry 中将其作为一种数据类型使用。Value type 可支持以下列出的使用场景。

Once you have [created a value type](/docs/foundry/object-link-types/create-value-type/), you can use it in as a data type across Foundry. Value types can be supported for the use cases listed below.
* 将 value type 分配给 Object Type Property。

* 将 value type 分配给 shared property。

* 使用 `logical type cast` 表达式将 value type 作为 logical type 分配给 Pipeline Builder pipeline property，并在写入 objects target 时在该 Property 上选择该 value type。

* Assigning a value type to an object type property.
* Assigning a value type to a shared property.
* Assigning a value type to a Pipeline Builder pipeline property as a logical type using the `logical type cast` expression and selecting the value type on the property when you write to the objects target.
要将 value type 分配给 Property，请在 Property 配置期间从下拉菜单中选择相应的 value type。

To assign a value type to a property, select the value type from the dropdown menu during property configuration.

> 📷 **[图片: Constraint update warning]**

> 📷 **[图片: Constraint update warning]**

> **⚠️ 警告**

> 如果您对包含未通过验证的属性值的 object property 应用 value type，则该 object type 将无法索引。您可以在 Ontology Manager 中的 object type 健康状态中查看此类索引失败，在那里您可以更正数据或更新 value type 以解决问题。
> **⚠️ 警告**

> If you apply a value type to an object property that contains property values that fail validation, that object type will fail to index. You can view such index failures in the object type health status in Ontology Manager, where you can correct your data or update your value type to fix the issue.