<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/value-types-versions/
---
# Value type versions
Value types 被版本化以处理破坏性和非破坏性编辑。Value type versions 包括两个部分：metadata 和 constraints。name、description 和 apiName 的 metadata 值可以在必要时随时更改。定义类型验证规则的 base type metadata 和 constraints 是不可变的。

Value types are versioned to handle breaking and non-breaking edits. Value type versions include two parts: metadata and constraints. The metadata values for name, description, and apiName can be changed whenever necessary. The base type metadata and the constraints that define the validation rules for the type are immutable.
如果您选择更新 value type 的 constraints，则会创建该 value type 的新版本。如果您的 value type 没有使用者，您可以自由地更改这些 constraints。但是，如果您对 constraints 进行破坏性更改并且您的 value type 有使用者，我们建议弃用当前的 value type 并创建一个新的 value type。这种方法可以避免潜在的运行时错误和数据不一致问题。

If you choose to update the constraints of a value type, a new version of the value type is created. If your value type has no consumers, you can freely change these constraints. However, if you make breaking changes to the constraints and your value type has consumers, we recommend deprecating the current value type and creating a new one instead. This approach avoids potential runtime errors and data inconsistencies.

> 📷 **[图片: Constraint update warning]**

> 📷 **[图片: Constraint update warning]**

当您对 value type 进行非破坏性更改时,也会创建一个新版本。这个新版本将自动传播到 Ontology,确保 Ontology 中所有使用该 value type 的地方都更新到最新版本。

When you make non-breaking changes to a value type, a new version is also created. This new version will automatically propagate to the Ontology, ensuring that all uses of the value type across the Ontology are updated to the latest version.