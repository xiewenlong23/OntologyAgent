<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/custom-aliases/
---
# Custom aliases
Custom aliases 是存储字符串值(例如 configuration parameters、feature flags 或 environment-specific settings)的命名引用。通过使用 custom aliases 而不是硬编码值,可以将 function 逻辑与特定配置解耦,并使 functions 在不同环境中可移植。

Custom aliases are named references that store string values such as configuration parameters, feature flags, or environment-specific settings. By using custom aliases instead of hard-coding values, you can decouple your function logic from specific configurations and make your functions portable across environments.
## Define a custom alias
要定义 custom alias,请打开 TypeScript v2 或 Python code repository,然后按照以下步骤操作:

To define a custom alias, open a TypeScript v2 or Python code repository and follow the steps below:
1. 打开 **Resource imports** 侧边栏,然后选择 **Platform SDK** 选项卡。您将看到一个 custom aliases 部分。

1. Open the **Resource imports** side panel and select the **Platform SDK** tab. You will see a section for custom aliases.
![The Resource imports side panel showing the Platform SDK tab with the custom aliases option.](/docs/resources/foundry/functions/custom-aliases-sidebar.png)
2. 选择 **New alias** 打开 alias 创建对话框。为 alias 名称提供 **Key** 并提供要关联的 **Value**,然后选择 **Create**。

2. Select **New alias** to open the alias creation dialog. Provide a **Key** for the alias name and a **Value** to associate with it, then select **Create**.
![The new alias dialog with a key set to myAlias and a value set to someValue.](/docs/resources/foundry/functions/custom-aliases-create.png)
> **ℹ️ 注意**

> Alias keys 在 repository 内必须唯一。
> **ℹ️ 注意**

> Alias keys must be unique within the repository.
3. Custom alias 将出现在 **Custom aliases** 部分中。

3. The custom alias will appear in the **Custom aliases** section.
## Edit a custom alias
要编辑现有的 custom alias,请导航到 **Platform SDK** 选项卡中的 **Custom aliases** 部分。选择 alias 旁边的笔图标以就地编辑其值。您也可以单击 3 个点来编辑 alias key 或删除整个 alias。

To edit an existing custom alias, navigate to the **Custom aliases** section in the **Platform SDK** tab. Select the pen icon next to the alias to edit its value inline. You can also click on the 3 dots to edit the alias key or delete the alias altogether.
![The custom aliases list showing a created alias with an option to edit the value.](/docs/resources/foundry/functions/custom-aliases-edit.png)
## Use a custom alias in code
要在 function 中使用 custom alias,请导入 alias 实用程序并通过其 key 引用 alias:

To use a custom alias in your function, import the alias utility and reference the alias by its key:
```typescript tab="TypeScript v2"
import { Aliases } from "@osdk/functions";

export default function getCustomValue(): string {
return Aliases.custom("myAlias");
}
```
```python tab="Python"
from functions.aliases import custom
from functions.api import function

@function
def get_custom_value() -> str:
return custom("myAlias")
```
## Use custom aliases with Marketplace
当您将使用 custom aliases 的 function 添加到 [Marketplace product](/docs/foundry/functions/marketplace-functions/) 时,这些 aliases 会自动作为可配置的 parameters 出现在 **Inputs** 下。安装者可以为其环境设置适当的 alias 值,而无需修改 function source code。

When you add a function that uses custom aliases to a [Marketplace product](/docs/foundry/functions/marketplace-functions/), the aliases automatically appear as configurable parameters under **Inputs**. Installers can set the alias values appropriate for their environment without modifying the function source code.
![A Marketplace product showing the custom alias as a configurable parameter input alongside the function output.](/docs/resources/foundry/functions/custom-aliases-marketplace-product.png)
### Set a description
为了帮助安装者了解如何配置 alias,您可以为 alias parameter 添加描述。选择 **Inputs** 下的 alias 以打开 **Details** 面板,然后在 **General** 选项卡上输入描述。

To help installers understand how to configure the alias, you can add a description to the alias parameter. Select the alias under **Inputs** to open the **Details** panel, then enter a description on the **General** tab.
![The Details panel for a custom alias parameter showing a description field.](/docs/resources/foundry/functions/custom-aliases-set-description.png)
### Add presets
您可以为 alias 定义预设值,安装者在安装过程中可以从中选择。在 **Details** 面板中,选择 **Presets** 选项卡,然后选择 **Manual overrides** 以定义一组允许的值。

You can define preset values for the alias that installers can choose from during installation. In the **Details** panel, select the **Presets** tab and choose **Manual overrides** to define a set of allowed values.
![The Presets tab showing manual override configuration with preset values for the alias.](/docs/resources/foundry/functions/custom-aliases-add-presets.png)
### Installation experience
在安装过程中，安装程序会看到 alias 描述，并可以从预设值中进行选择或手动配置 alias。安装完成后，function 会将该 alias 解析为安装程序配置的值。

During installation, the installer will see the alias description and can choose from the preset values or configure the alias manually. After installation, the function resolves the alias to the value configured by the installer.
![The installation view showing the custom alias parameter with its description and preset value options.](/docs/resources/foundry/functions/custom-aliases-install.png)