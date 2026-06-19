<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/marketplace-functions/
---
# Add functions to a Marketplace product
使用 [Foundry DevOps](/docs/foundry/devops/overview/) 将您的 functions 包含在 [Marketplace products](/docs/foundry/devops/core-concepts/#product) 中，以便其他用户安装和复用。[了解如何创建您的第一个 product。](/docs/foundry/foundry-devops/create-products/)

Use [Foundry DevOps](/docs/foundry/devops/overview/) to include your functions in [Marketplace products](/docs/foundry/devops/core-concepts/#product) for other users to install and reuse. [Learn how to create your first product.](/docs/foundry/foundry-devops/create-products/)
## Supported features
DevOps packages 函数以供安装和复用，但不提供用户可见的源代码用于 [TypeScript V1 functions](/docs/foundry/functions/typescript-v1-getting-started/)。这意味着安装完成后，您将能够使用已安装的 TypeScript functions，但无法查看其源代码逻辑；与该 function 配套的 repository 将为空。

DevOps packages functions for installation and reuse but does not provide user-viewable source code for [TypeScript V1 functions](/docs/foundry/functions/typescript-v1-getting-started/). This means that after installation, you will be able to use the installed TypeScript functions, but you will not be able to view their source logic; the repository accompanying the function will be empty.
[Python](/docs/foundry/functions/python-getting-started/) 和 [TypeScript V2](/docs/foundry/functions/typescript-v2-getting-started/) functions 在 Marketplace 产品中确实包含用户可见的源代码。然而，在以 production mode 安装后，functions 的内容仍然无法被编辑。

[Python](/docs/foundry/functions/python-getting-started/) and [TypeScript V2](/docs/foundry/functions/typescript-v2-getting-started/) functions do include user-viewable source code in the Marketplace product. However, the contents of the functions still cannot be edited after installation when installed in production mode.
## Adding functions to products
要将 function 添加到产品中，请先 [create a product](/docs/foundry/foundry-devops/create-products/)。然后，如下所示添加一个 **Function** output。

To add a function to a product, [create a product](/docs/foundry/foundry-devops/create-products/). Then, add a **Function** output as shown below.
![Add a function output.](/docs/resources/foundry/functions/marketplace-add-function-output.png)
系统随后会提示您选择一个 function 和一个 version。在大多数情况下，您应该选择该 function 的最新版本。

You will then be prompted to choose a function and a version. In most cases, you should select the latest version of a function.
![Search for a function.](/docs/resources/foundry/functions/marketplace-function-search.png)
虽然您可以直接选择 functions，但我们建议先添加诸如 [Workshop applications](/docs/foundry/workshop/marketplace-workshop/) 之类的内容；这些资源所需的 functions 将作为 [inputs](/docs/foundry/foundry-devops/create-products/#add-inputs) 自动添加到您的产品中。

While you can select functions directly, we recommend first adding content such as [Workshop applications](/docs/foundry/workshop/marketplace-workshop/); the functions these resources require will be automatically added as [inputs](/docs/foundry/foundry-devops/create-products/#add-inputs) to your product.
![A Workshop application, adding functions automatically.](/docs/resources/foundry/functions/function-added-as-an-input.png)
## Use OSDK functions in Marketplace products
使用 OSDK 的 Python 和 TypeScript V2 functions 也可以打包为 Marketplace 产品中的 outputs。当您将一个使用 OSDK 的 function 作为 output 添加到您的 Marketplace 产品时，该 OSDK 也会作为 output 添加，而您 OSDK 中使用的 ontology entities 将作为 inputs 添加。

Python and TypeScript V2 functions that use OSDKs can also be packaged as outputs in Marketplace products. When you add a function that uses an OSDK as an output to your Marketplace product, the OSDK will also be added as an output while the ontology entities used in your OSDK will be added as inputs.
![OSDK function dependencies are added.](/docs/resources/foundry/functions/marketplace-function-dependencies-added.png)
安装您的 Marketplace 产品的用户随后可以重新映射您的 OSDK 中引用的 objects、links 和其他 ontology entities，使其指向产品安装所在 ontology 中的 entities。

Users who install your Marketplace product will then be able to remap the objects, links, and other ontology entities referenced in your OSDK to refer to entities in the ontology where the product is being installed.
![Remapping ontology inputs during Marketplace install.](/docs/resources/foundry/functions/marketplace-remap-object-input.png)
安装后，当该 function 被执行时，它将自动使用在安装过程中配置的 ontology entities。

When the function is executed after installation, it will automatically use the ontology entities that were configured during installation.
## Function overrides at installation
> **⚠️ 警告**

> 不支持在重写的 static functions 中调用 [queries](/docs/foundry/functions/query-functions/) 或 [making API calls](/docs/foundry/functions/api-calls/)。
> **⚠️ 警告**

> Calling [queries](/docs/foundry/functions/query-functions/) or [making API calls](/docs/foundry/functions/api-calls/) within overridden static functions is not supported.
可以通过在安装时提供一个本地定义的 function 来覆盖随 Marketplace 产品一起发布的 "static" function input，从而修改 function 行为的部分内容。为此，您可以使用 `@Static` 装饰器来指定某个特定的 function 可以被覆盖。

It is possible to modify parts of a function’s behavior at install time by providing a locally defined function which overrides the “static” function input that is shipped with your Marketplace product. To do this, you can specify that a particular function may be overridden by using the `@Static` decorator.
例如，考虑一个对给定数字取反的 function：

For example, consider a function that negates a given number:
```
// Normal function

import { Function, Double } from "@foundry/functions-api";

export class MyFunctions {

@Function()
public async modifyNumber(d: Double): Promise<Double> {
return -d;
}

}
```
要使此 function 可被覆盖，请按如下方式重写它：

To make this function overridable, rewrite it as follows:
```
// Overridable function

import { Function, Static, Double } from "@foundry/functions-api";

export class MyFunctions {

@Function()
public async modifyNumberByStaticFoo(
n: Double,
@Static() staticFunctionInput: (num: Double) => Promise<Double> = this.defaultFoo
): Promise<Double> {
return await staticFunctionInput(n);
}

private async defaultFoo(n: number) {
return -n;
}

}
```
在打包 static function 时，inputs 在安装过程中将显示为 `staticFunctionInputs`，如下所示。安装者随后可以提供他们自己的 function 逻辑，以覆盖默认行为。从概念上讲，`staticFunctionInputs` 充当可被覆盖的 function 的 function input parameters。

When packaging a static function, inputs will appear as `staticFunctionInputs` during installation, as shown below. Installers can then provide their own function logic that will override the default behavior. Conceptually, the `staticFunctionInputs` serve as function input parameters to the overridable function.
![Function override](/docs/resources/foundry/functions/marketplace-function-override.png)
例如，您可能拥有一个 supply chain optimization function，其逻辑在另一个上下文中需要进行微调。为此，请在打包之前指定该 function 是可被覆盖的，然后在安装时对其进行覆盖。

For example, you may have a supply chain optimization function whose logic needs slight adjustments in another context. To allow this, specify that the function is overridable before packaging it, and then override it during installation.