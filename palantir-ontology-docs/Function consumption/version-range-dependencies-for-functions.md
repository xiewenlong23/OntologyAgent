<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/version-range-dependencies-for-functions/
---
# Version range dependencies for functions
除了依赖 Function 的固定版本外，某些应用程序（如 Workshop 和 Actions）还允许你在版本范围内依赖 Function。这样做可以在运行时启用自动升级，从而节省开发周期的时间，并为 [deployed functions](/docs/foundry/functions/functions-deployed/) 提供无停机时间的升级体验。

In addition to depending on a pinned version of a Function, some applications like Workshop and Actions allow you to depend on a Function at a version range. Doing so enables automatic upgrades at runtime, which can save you time in your development cycle and provide a downtime-less upgrade experience for [deployed functions](/docs/foundry/functions/functions-deployed/).
虽然版本范围依赖是一个强大的功能，但它也存在某些风险（例如，Actions 存在 [特定的权限后果](#permissions-and-provenance-in-actions)）。本文档解释了版本范围解析背后的机制，以便你更好地理解这些风险，并就版本范围依赖是否适合你的应用程序做出明智的决定。

While version range dependencies are a powerful feature, they also carry certain risks (for example, there are [permissioning consequences specific to Actions](#permissions-and-provenance-in-actions)). This documentation explains the mechanics behind version range resolution so that you can better understand these risks and make an informed decision on whether version range dependencies are suitable for your application.
> **ℹ️ 注意**

> 本文档假定你已具备向后兼容性和 Semantic Versioning 系统等主题的先验知识。如果你对这些主题不熟悉，请查看我们关于 [functions versioning](/docs/foundry/functions/functions-versioning/) 的文档。
> **ℹ️ 注意**

> This documentation page assumes prior knowledge on topics like backward compatibility and the Semantic Versioning system. If you are not familiar with these topics, review our documentation on [functions versioning](/docs/foundry/functions/functions-versioning/).
> 你还应该熟悉 [Semantic Versioning 规范 ↗](https://semver.org/#spec-item-11) 中定义的版本优先级规则。换句话说，你应该能够确定给定两个不同版本时哪个版本的优先级更低。例如，`1.0.0-rc.1` < `1.0.0` < `1.0.1` < `1.1.0` < `2.0.0`。
> You should also be familiar with the rules around version precedence as defined in the [Semantic Versioning specification ↗](https://semver.org/#spec-item-11). In other words, you should be able to determine, given two distinct versions, which one has lower precedence. For example, `1.0.0-rc.1` < `1.0.0` < `1.0.1` < `1.1.0` < `2.0.0`.
## Version ranges
最简单的形式下，版本范围是一组版本不等式，如果某个版本满足其所有不等式，则称该版本"满足"该范围。例如，版本 `1.2.0` 满足范围 `>=1.0.0 <2.0.0`。

In its simplest form, a version range is a collection of version inequalities, and a version is said to "satisfy" a range if it satisfies all of its inequalities. For example, version `1.2.0` satisfies the range `>=1.0.0 <2.0.0`.
> **ℹ️ 注意**

> 在内部，Function 版本范围的语义采用自 NPM，这是 JavaScript 生态系统中流行的包管理器。请查看 [NPM 关于版本范围的文档 ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#ranges) 以获取严格的定义。
> **ℹ️ 注意**

> Internally, the semantics of Function version ranges are adopted from NPM, a popular package manager for the JavaScript ecosystem. Review the [NPM documentation on version ranges ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#ranges) for a rigorous definition.
Workshop 和 Actions 等应用程序目前仅允许由向后兼容版本（即 minor 或 patch 升级）组成的版本范围。

Applications like Workshop and Actions currently only allow version ranges that comprise backward compatible versions (that is, minor or patch upgrades).
> **ℹ️ 注意**

> Workshop 和 Actions 使用的此向后兼容范围对应的 NPM 等价物是 [caret range ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#caret-ranges-123-025-004)。
> **ℹ️ 注意**

> The NPM equivalent of this backward compatible range used by Workshop and Actions is the [caret range ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#caret-ranges-123-025-004).
## Version range resolution
除了已部署的 Function 之外,当您依赖一个特定版本范围的 Function 时,一个满足该版本范围的具体版本将在运行时执行期间被选择。具体来说,最终将选择*最大的*满足条件的版本(可能需要几分钟时间来获取新版本)。

With the exception of deployed functions, when you depend on a Function at a version range, a concrete version that satisfies the range will be chosen at runtime during execution. In particular, the *maximum* satisfying version will be chosen on an eventual basis (it can take a few minutes to pick up new releases).
### Deployed functions
对于已部署的 Function,具体版本将解析为当前已部署的版本(如果该版本满足范围)。如果已部署的版本不满足范围,将会返回错误。

For deployed functions, a concrete version is instead resolved to the currently deployed version, if it satisfies the range. If the deployed version does not satisfy the range, an error will be returned.
## Risks
尽管 Function 开发人员被引导遵循 Semantic Versioning 规范和通用最佳实践,但在非主版本发布中意外引入 breaking change 总是有可能的。

While functions developers are guided towards the Semantic Versioning specification and general best practices, it is always possible for breaks to be accidentally introduced in non-major version releases.
如果您的应用程序遇到了 breaking change,它可能表现为多种问题,例如运行时失败或意外行为。

If your application picks up a breaking change, it can manifest in any number of problems, like runtime failures or unexpected behavior.
一旦发现 breaking change,您应立即联系该 Function 的开发人员,以便他们可以[发布修复版本](/docs/foundry/functions/functions-versioning/#accidentally-releasing-a-backward-incompatible-change-as-a-patch-or-minor-version),与此同时,您应将您的 Function 依赖固定(pin)到最后一个可用的工作版本。

Upon noticing a breaking change, you should immediately contact the developer of the Function so that they can [release a fix](/docs/foundry/functions/functions-versioning/#accidentally-releasing-a-backward-incompatible-change-as-a-patch-or-minor-version), and in the meantime, you should pin your Function dependency to the last working version.
> **⚠️ 警告**

> 需要注意的是,对于已部署的 Function 依赖,如果您的应用程序有严格的正常运行时间要求且不能容忍任何中断,您应使用固定版本(pinned version)依赖。
> **⚠️ 警告**

> With the caveat of deployed Function dependencies, if your application has strict uptime requirements and cannot tolerate any breaks, you should use pinned version dependencies.
### Permissions and provenance in Actions
在 [Function-backed Actions](/docs/foundry/action-types/function-actions-overview/) 中使用 Function 版本范围时,需要考虑有关权限(permissions)和来源(provenance)的重要事项,这些可能会影响 Action 的行为。有关这些影响的更多信息,请参阅 Actions 文档中关于 [auto upgrades](/docs/foundry/action-types/function-actions-getting-started/#auto-upgrades) 的内容。

When using Function version ranges in [Function-backed Actions](/docs/foundry/action-types/function-actions-overview/), there are important considerations around permissions and provenance that can affect Action behavior. For more information about these implications, refer to the Actions documentation on [auto upgrades](/docs/foundry/action-types/function-actions-getting-started/#auto-upgrades).