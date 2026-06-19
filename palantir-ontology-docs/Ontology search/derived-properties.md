<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/derived-properties/
---
# Derived properties \[Beta]
> **ℹ️ 注意: Beta**

> Derived properties（派生属性）处于开发的 [beta](/docs/foundry/platform-overview/development-life-cycle/) 阶段，可能在您的注册环境中不可用。在积极开发过程中，功能可能会发生变化。
> **ℹ️ 注意: Beta**

> Derived properties are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.
Derived properties（派生属性）是基于运行时根据对象上其他 Property 或 Link 的值计算得出的属性。这包括对链接对象的 Property 进行聚合或选择。派生属性随后可用于进一步的操作，例如在同一个请求中进行过滤、排序或聚合。派生属性使用计算中涉及的所有对象的 Security，因此不会暴露用户原本无法查看的信息。

Derived properties are properties that are calculated at runtime based on the values of other properties or links on objects. This includes aggregating on or selecting properties of linked objects. Derived properties are then available for further operations, such as filtering, sorting, or aggregating within the same request. Derived properties use the security of all objects involved in the calculation, so they do not expose information a user would otherwise be unable to see.
## Availability
派生属性可在以下工作流中使用：

Derived properties are available in the following workflows:
* **Ontology SDK：** 派生属性可以在 TypeScript OSDK 中与 `withProperties` 操作一起使用，以便返回或用于其他过滤、聚合或排序操作。TypeScript OSDK 必须运行 `@osdk/client` 包的 `2.2.0-beta.x` 版本或更高版本。有关更多详细信息，请参阅 [Developer Console](/docs/foundry/developer-console/overview/) 中的 API 文档。

* **Ontology SDK:** Derived properties can be used in the TypeScript OSDK with the `withProperties` operation, to be returned or used in additional filters, aggregations, or sorts. The TypeScript OSDK must be running the `2.2.0-beta.x` version of the `@osdk/client` package or later. Review the API documentation in [Developer Console](/docs/foundry/developer-console/overview/) for more details.
## Known limitations
作为一项正在积极开发中的 beta 特性，派生属性目前有一些功能限制。随着其他功能的构建，许多这些功能将逐步推出。当前的限制如下所列：

As a beta feature under active development, derived properties currently have some capability limitations. Many of these capabilities will become available over time as additional functionality is built. Current limitations are listed below:
* **OSv1 支持：** 包含派生属性的查询不能包含任何使用 [OSv1](/docs/foundry/object-backend/osv1-osv2-migration/) 索引的 Object Type。

* **Text search（文本搜索）：** 派生属性不能用于文本搜索或关键字过滤。

* **Structs in OSDK（OSDK 中的 Struct）：** 具体来说，在当前版本的 TypeScript OSDK 中，包含派生属性的查询不能包含任何 [struct](/docs/foundry/object-link-types/structs-overview/) Property Type。您可以在 Ontology SDK 中使用 `$select` 操作来排除 struct Property。

* **OSv1 support:** Queries with derived properties may not contain any object types indexed using [OSv1](/docs/foundry/object-backend/osv1-osv2-migration/).
* **Text search:** Derived properties cannot be used in text search or keyword filters.
* **Structs in OSDK:** Specifically in current versions of the Typescript OSDK, queries with derived properties may not contain any [struct](/docs/foundry/object-link-types/structs-overview/) property types. You can use a `$select` operation in Ontology SDK to exclude struct properties.