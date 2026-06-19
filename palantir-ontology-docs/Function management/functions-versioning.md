<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/functions-versioning/
---
# Function versioning
本文档介绍了用于 functions 的版本控制系统。Function 发布的版本由其发布者选择,并且在创建后不可变。应用合适的版本对于为您的 functions 使用者提供稳定可靠的体验至关重要。

This document describes the versioning system used for functions. Versions for function releases are chosen by their publishers and are immutable after creation. Applying appropriate versions is critical to providing consumers of your functions with a stable and reliable experience.
## Backward compatible changes vs. breaking changes
Functions 的版本控制系统区分向后兼容的变更(backward compatible changes)和 breaking changes。*Backward compatible changes* 是指不会中断您 functions 现有使用者的变更。不向后兼容的变更可以称为 *backward incompatible* 或 *breaking* 变更。

The versioning system for functions distinguishes between backward compatible changes and breaking changes. *Backward compatible changes* are changes that do not disrupt existing consumers of your functions. A change that is not backward compatible can be referred to as a *backward incompatible* or a *breaking* change.
Backward compatible changes 的一些示例包括:

Some examples of backward compatible changes are:
* 向 function 的签名中添加一个可选输入。

* 优化 function 的性能而不改变其预期行为。

* 修复 function 中的 bug 而不改变其预期行为。

* Adding an optional input to a function’s signature.
* Optimizing a function’s performance without changing its expected behavior.
* Fixing a bug in your function without changing its expected behavior.
Breaking changes 的一些示例包括:

Some examples of breaking changes are:
* 向 function 的签名中添加一个必需输入。

* 将 function 签名的输出类型从 integer 更改为 string。

* 删除一个 function。

* Adding a required input to a function’s signature.
* Changing the output type of a function’s signature from an integer to a string.
* Deleting a function.
在考虑对现有版本的变更是否向后兼容时,请问自己:此变更是否会导致现有版本的使用者出现中断,或需要其明确关注?

When considering whether a change to an existing version is backward compatible, ask yourself if the change would cause disruption to or require explicit attention from a consumer of the existing version.
请记住,最终由您来决定您 functions 的预期使用模式。

Remember that you are ultimately in charge of dictating the expected consumption patterns of your functions.
## The semantic versioning system
Functions 的版本遵循 [Semantic Versioning ↗](https://semver.org/) 系统进行管理。

Functions are versioned according to the [Semantic Versioning ↗](https://semver.org/) system.
在 Semantic Versioning 中，版本号采用 `X.Y.Z` 的形式，其中 `X`、`Y` 和 `Z` 分别称为主版本号、次版本号和修订版本号，都是非负整数（例如，`1.2.3`）。版本号还可以包含预发布标识符，方法是在修订版本号之后紧跟一个连字符，后接字母数字字符（例如，`1.2.3-rc1`）。

In Semantic Versioning, versions take the form `X.Y.Z` where `X`, `Y`, and `Z`—known as the major, minor, and patch versions respectively—are non-negative integers (for instance, `1.2.3`). A version may also include a prerelease identifier comprised of alphanumeric characters by appending a hyphen immediately following the patch version (for example, `1.2.3-rc1`).
> **ℹ️ 注意**

> 本页提供了 Semantic Versioning 的简要概述。我们建议您阅读 [完整规范 ↗](https://semver.org/)，因为遵守规范是发布可在其他应用程序中可靠使用的 functions 的重要方面。
> **ℹ️ 注意**

> This page provides a brief summary of Semantic Versioning. We encourage you to read the [full specification ↗](https://semver.org/) since adhering to the specification is an important aspect of publishing functions that can be reliably consumed in other applications.
### Choosing a release version
在发布 function 的新版本时，请考虑 Semantic Versioning 规范中的以下几点：

When publishing a new version of a function, consider the following points from the Semantic Versioning specification:
* 主版本号 `0`（`0.y.z`）用于初始开发阶段。在初始开发期间，function 可能随时发生变化，您的 functions 不应被视为稳定的供消费者使用。
* 当您进行不向后兼容的更改时，应递增主版本号。
* 当您以向后兼容的方式添加功能时，应递增次版本号。

* 当您进行向后兼容的 bug 修复时，应递增修订版本号。
* 预发布版本表示该版本不稳定，可能无法满足其关联正常版本所指定的预期兼容性要求。

* Major version `0` (`0.y.z`) is for initial development. During initial development, the function may change at any time and your functions should not be considered stable by consumers.
* The major version should be incremented when you make backward incompatible changes.
* The minor version should be incremented when you add functionality in a backward compatible manner.
* The patch version should be incremented when you make backward compatible bug fixes.
* A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version.
### Backward compatibility checks
在您发布新版本之前，系统会对您的 functions 执行向后兼容性检查。特别地，您将会收到关于以下任何破坏性更改的警告：

Backward compatibility checks are performed for your functions before you publish a new version. In particular, you will be warned about any of the following breaking changes:
* 删除 function。这包括在您的 Python 或 TypeScript function 代码仓库中删除 function。

* 删除 function 签名上的输入（即使是可选输入）。

* 调整 function 签名上输入的顺序。

* 向 function 签名添加必需的输入。

* 不正确的输入类型更改（例如 integer 改为 string）。请注意，扩展数值输入类型（如 integer 改为 float）将导致警告。

* 不正确的输出类型更改（例如 string 改为 optional string）。

* Dropping a function. This includes deleting a function in your Python or TypeScript function code repository.
* Dropping an input (even an optional one) on a function’s signature.
* Reordering an input on a function’s signature.
* Adding a required input to a function’s signature.
* Bad input type changes (such as integer to string). Note that widening a numeric input type (like integer to float) will result in a warning.
* Bad output type changes (such as string to optional string).
如果这些检查因任何原因失败，建议您发布一个主版本。但是，如果您仍处于初始开发阶段（即主版本仍为 `0`），则不适用此建议。

If these checks fail for any reason, it is recommended that you release a major version. However, this does not apply if you are still in the initial development phase (that is, you are still at major version `0`).
> **⚠️ 警告**

> Palantir 的内置检查并未涵盖所有类型的破坏性更改。例如，您的内部实现所产生的破坏性更改可能无法被检测到。仅基于这些检查的成功结果而发布次版本或修订版本是不安全的。
> **⚠️ 警告**

> Palantir's built-in checks are not exhaustive of all types of breaking changes. For instance, breaking changes from your internal implementation may not be detected. It is not safe to release a minor or patch version based solely on a successful outcome from these checks.
#### Caveat: Custom types
内部 functions 数据类型的表示目前缺少有关自定义类型字段可选性的足够信息。因此，您可能会注意到，对于自定义类型的输入和输出，向后兼容性检查会在添加或删除任何字段时发出警告，包括可选字段（例如 Typescript 中的 `quantity?: Integer` 或 Python 中的 `quantity: Integer = 0`）。

The internal functions data type representation currently lacks sufficient information regarding the optionality of custom type fields. As a result, you may notice that for custom type inputs and outputs, the backward compatibility checks will warn you when removing or adding any fields, including optional fields (such as `quantity?: Integer` in Typescript or `quantity: Integer = 0` in Python).
我们目前正在进行更改，以便今后在删除输出自定义类型的可选字段或添加输入自定义类型的可选字段时，您将不会收到警告。

We are currently making changes so that going forward you will not be warned when removing an optional field on an output custom type or adding an optional field on an input custom type.
> **ℹ️ 注意**

> 当删除输入自定义类型的可选字段时，您仍会收到警告。忽略消费者提供的任何字段通常被认为是不良实践，因为他们很可能期望所提供的字段能够决定您 function 的行为。
> **ℹ️ 注意**

> You will still receive a warning when removing an optional field on an input custom type. It is generally considered bad practice to ignore any fields provided by a consumer as they likely expect the provided fields to tell the behavior of your function.
### Restrict stable version tags
稳定的 Semantic Versioning 发布（非预发布版本）可以被下游生产应用程序立即使用，前提是这些应用程序已配置为通过版本范围（例如 `>=1.2.3 <2.0.0`）引用该 Function。这使得在以新稳定版本发布之前审查和测试代码更改变得非常重要。

Stable Semantic Version releases (non-prerelease versions) may be immediately consumed by downstream production applications if the applications have been configured to reference the Function by a version range (for example, `>=1.2.3 <2.0.0`). This makes it important to review and test code changes before releasing them in a new stable version.
您可以通过在受保护分支的仓库设置中 [启用开关](/docs/foundry/code-repositories/branch-settings/#restrict-stable-version-tags) 来对 Functions 稳定版本的发布施加限制。

It is possible to enforce restrictions on the release of stable versions of your Functions by [enabling a toggle](/docs/foundry/code-repositories/branch-settings/#restrict-stable-version-tags) in the repository settings for protected branches.
## Frequently asked questions
### Choosing release versions in the 0.y.z initial development phase
通常的做法是，任何破坏性更改在次版本中进行，而任何向后兼容的更改在修订版本中进行。这是许多开发领域中消费者所做的假设，例如 Node/NPM 生态系统，这从其广泛使用 [caret 范围 ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#caret-ranges-123-025-004) 中可见一斑。

It is common practice that any breaking changes be made in a minor release and any backward compatible changes be made in a patch release. This is an assumption made by consumers in many development spheres, such as the Node/NPM ecosystem, as demonstrated by their wide use of [caret ranges ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#caret-ranges-123-025-004).
### Accidentally releasing a backward incompatible change as a patch or minor version
一旦你意识到发布了一个破坏性变更，你应该纠正该问题，并在新的次要版本中恢复向后兼容性。

As soon as you realize that you’ve released a breaking change, you should correct the problem and restore backward compatibility in a new minor version.
请参考以下示例。

Consider the following example.
1. 你有一个名为 `myFunction` 的 function，版本为 `1.0.0`，它接受单个字符串输入。

2. 你为 `myFunction` 添加了一个新的必填输入，并在次要版本发布 `1.1.0` 中意外地发布了此更改。

1. You have a function called `myFunction` at version `1.0.0` which takes a single string input.
2. You add a new required input to `myFunction` and accidentally release this change in a minor version release `1.1.0`.
为了修复此问题，你可以回滚对该签名的破坏性变更（即移除你在 `1.1.0` 中添加的新必填输入），并在版本 `1.2.0` 中发布此更改。

To remediate this, you can revert the breaking change to the signature (that is, remove the new required input you added in `1.1.0`) and release this change in version `1.2.0`.
### Checking backward compatibility when a release fails or has not yet been published
对于 TypeScript 或 Python functions，你的 functions 可能会发布失败或需要几分钟才能发布成功。在这些情况下，内置的向后兼容性检查将无法运行。如果你希望在发布新版本之前查看这些检查的结果，你有以下几个选项：

In the case of TypeScript or Python functions, your functions may fail or take a few minutes to publish. In either of these cases, the built-in backward compatibility checks will be unable to run. If you want to see the results of these checks before making a new release, you have the following options:
* 如果上一次发布失败，你应该使用 "custom tag" 选项与上一次成功的 tag 进行比较。
* 如果上一次发布尚未完成，你应该等待其完成。

* If the last release failed, you should use the “custom tag” option to compare against the last successful tag.
* If the last release has not been published yet, you should wait for it to finish.