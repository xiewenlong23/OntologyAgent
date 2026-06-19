<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/function-interfaces/
---
# Function interfaces
**Function interfaces** 允许 function 作者将其自定义逻辑与原生 Foundry 功能集成，并为定义消费应用程序与 functions 之间的契约提供了一种强大方式。

**Function interfaces** allow function authors to integrate their custom logic with native Foundry features and offer a powerful way of defining contracts between consuming applications and functions.
Function interfaces 定义了应用程序或用户应如何与 function 交互。这包括 function 的 inputs、outputs 和 errors。换句话说，function interface 描述了 function 的 signature，但 function interface 本身并不是一个 function。Function interfaces 旨在由 functions 来实现。

Function interfaces define how an application or user should interact with a function. This includes the function’s inputs, outputs, and errors. In other words, a function interface describes a function’s signature, but a function interface is not itself a function. Function interfaces are designed to be implemented by functions.
一些 Foundry 应用程序使用 function interfaces，以便在根据已知的 inputs、outputs 和 errors 执行实现该 interface 的 functions 时提供专门的行为。用户可以提供某些 function interfaces 的自有实现，Foundry 可以继续提供这种专门的行为。Foundry 中依赖某些 function interfaces 的应用程序可以发现所有实现该 interface 的 functions。

Some Foundry applications use function interfaces to provide specialized behavior when executing functions which implement the interface, given the known inputs, outputs, and errors. Users can provide their own implementations of certain function interfaces, and Foundry can continue providing this specialized behavior. Applications within Foundry which depend on certain function interfaces can discover all functions which implement that interface.
例如，AIP Logic 依赖 function interfaces 来允许用户将其自有的 LLMs 引入到 Logic functions 中。具体来说，AIP Logic 中的 [Use LLM](/docs/foundry/logic/blocks/#use-llm) block 允许用户选择 Palantir 提供的 LLMs 或 *registered* 的 LLMs。Registered models 是用户编写的 functions，它们实现了 Foundry 提供的 function interface；例如，chat completion function interface。这使得 AIP Logic 能够发现那些被明确定义为 chat completion 实现的 functions，它们具有通用 LLM 典型的 signature，并能够返回 AIP Logic 可以适当处理的 errors。未来，用户提供的 chat completion 实现将可在平台的其他部分中使用，例如 Pipeline Builder 和 Model Catalog。

For example, AIP Logic depends on function interfaces to allow users to bring their own LLMs into Logic functions. Specifically, the [Use LLM](/docs/foundry/logic/blocks/#use-llm) block in AIP Logic allows users to select Palantir-provided LLMs or *registered* LLMs. Registered models are user-authored functions that have implemented a function interface provided by Foundry; for instance, the chat completion function interface. This allows AIP Logic to discover functions that have been explicitly defined as being an implementation of a chat completion, have a signature typical of a generic LLM, and return errors which AIP Logic can handle appropriately. In the future, user-provided chat completion implementations will be usable in other parts of the platform, such as Pipeline Builder and Model Catalog.
[了解如何使用 registered models 功能注册 LLMs。](/docs/foundry/aip/bring-your-own-model/) 有关使用 function interfaces 的旧方法，请参阅 [使用 function interfaces 注册 LLM \[Legacy\]](/docs/foundry/aip/chat-completion-function-interface-quickstart/)。

[Learn how to register LLMs with the registered models feature.](/docs/foundry/aip/bring-your-own-model/) For the legacy method using function interfaces, see [Register an LLM using function interfaces \[Legacy\]](/docs/foundry/aip/chat-completion-function-interface-quickstart/).
## Palantir-provided function interfaces
以下列表包含 Palantir 当前提供的 function interfaces：

The following list contains the function interfaces currently provided by Palantir:
* [`ChatCompletion`](#chatcompletion)
* [`ChatCompletion`](#chatcompletion)
### `ChatCompletion`
**Description:**
**Description:**
* Functions 基于多轮和多用户文本对话历史生成上下文相关的文本响应。
* 非常适合对话式用例。

* Functions which generate contextually relevant text responses based on multi-turn and multi-user text conversation history.
* Ideal for conversational use cases.
**Foundry integrations:**
**Foundry integrations:**
* AIP Logic 中的 *Use LLM* board。

* 对 Pipeline Builder 的支持即将推出。

* The *Use LLM* board in AIP Logic.
* Support in Pipeline Builder coming soon.
**Documentation:**
**Documentation:**
* [**使用 function interfaces 注册 LLMs \[Legacy\]**](/docs/foundry/aip/chat-completion-function-interface-quickstart/)

* [**Register LLMs using function interfaces \[Legacy\]**](/docs/foundry/aip/chat-completion-function-interface-quickstart/)
## Type customization
为了提供更大的灵活性，在实现 function interface 时，您并不局限于所提供的 types。在某些情况下，您可能希望创建自己的 [custom types](/docs/foundry/functions/types-reference/#structcustom-type)。只要 function 与 function interface 上定义的 function [兼容 ↗](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#comparing-two-functions)，该 function 就会被编译器接受并成功发布。如果 function interface 为其定义的 input type 中所有字段都是可选的，则在自定义该 type 时必须至少共享一个公共可选字段。

To provide more flexibility, you are not limited to the provided types when implementing a function interface. In some cases, you may want to create your own [custom types](/docs/foundry/functions/types-reference/#structcustom-type). As long as a function is [compatible ↗](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#comparing-two-functions) with the function defined on the function interface, the function will be accepted by the compiler and successfully published. If the function interface defines an input type for which all fields are optional, at least one common optional field must be shared when customizing the type.
```typescript
...
interface CustomParams extends GenericCompletionParams {
modelSpecificParam?: string
}
...

// valid implementation
@ChatCompletion()
public async myRegisteredModel(
messages: FunctionsGenericChatCompletionRequestMessages,
params: CustomParams
): Promise<FunctionsGenericChatCompletionResponse> {
...
}
```
## Troubleshooting
Function interfaces 旨在保持灵活，并允许广泛的实现。但是，在实现 function interface 时您可能会遇到错误。以下是针对 TypeScript functions 的一些提示，可帮助您在自定义实现时避免这些错误。

Function interfaces are designed to be flexible and allow for a wide range of implementations. However, you may encounter errors when implementing a function interface. Here are some tips for TypeScript functions to help you avoid these errors when customizing your implementation.
### Error: `Function input name does not match the required input name of the function interface at the specific input position`
每个 parameter 的 input 名称必须与 function interface 上每个特定 input 位置所定义的 input 名称相匹配。正如 linting 所提示的，请确保每个 input 名称与 function interface 上声明的每个位置的 input 名称完全一致。

The input names of each parameter must match the input names defined on the function interface at each specific input position. As the linting suggests, ensure that each input name has the exact same input name as declared on the function interface at each position.
![Common errors: input names do not match.](/docs/resources/foundry/functions/byom-tutorial-common-errors-input-params-not-match.png)
### Error: `Function is missing input parameter of the function interface`
如果实现 function 未包含 function interface 上定义的每个必需 input，则会出现此错误。若要解决该错误，请确保 function interface 上声明的每个 input 都已包含在实现 function 中。

This error arises if the implementing function does not include every required input defined on the function interface. To resolve the error, ensure each input declared on the function interface is included in the implementing function.
![Common errors: required inputs not included.](/docs/resources/foundry/functions/byom-tutorial-common-errors-missing-input-params.png)
### Error: `Type {type1} is not assignable to type {type2}`
编译器可能会拒绝该实现 function，认定其与 interface 上定义的 function 不兼容。如果出现这种情况，请通过检查每个 type 的结构与 function interface 上定义的 type 进行对比，确保您的实现 function 与 function interface 上定义的 function 是 [兼容的 ↗](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#comparing-two-functions)。

The compiler may reject the implementing function as not compatible with the function defined on the interface. If so, ensure your implementing function is [compatible ↗](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#comparing-two-functions) with the function defined on the function interface by checking the structure of each type compared to the types defined on the function interface.
![Common errors: function not compatible with Chat completion decorator.](/docs/resources/foundry/functions/byom-tutorial-common-errors-function-not-compatible-with-interface.png)