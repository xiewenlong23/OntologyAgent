<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/marketplace-action-types/
---
# Add action types to Marketplace product
使用 [Foundry DevOps](/docs/foundry/devops/overview/) 将您的 action types 包含在 [Marketplace products](/docs/foundry/devops/core-concepts/#product) 中，以便其他用户安装和重用。[了解如何创建您的第一个 product。](/docs/foundry/foundry-devops/create-products/)

Use [Foundry DevOps](/docs/foundry/devops/overview/) to include your action types in [Marketplace products](/docs/foundry/devops/core-concepts/#product) for other users to install and reuse. [Learn how to create your first product.](/docs/foundry/foundry-devops/create-products/)
## Supported features
大多数 action type 功能都受支持，但引用了[具有不受支持功能的 object types](/docs/foundry/object-link-types/marketplace-ontology-types/#unsupported-features) 的 actions 除外。在为您的 action type 准备打包时，请确保您的 action type [**Security & Submission criteria**](/docs/foundry/action-types/getting-started/#add-submission-criteria) 不引用任何用户；将所有用户引用更新为对组（groups）的引用。

Most action type features are supported, except actions that reference [object types with unsupported features](/docs/foundry/object-link-types/marketplace-ontology-types/#unsupported-features). When preparing your action type for packaging, ensure your action type [**Security & Submission criteria**](/docs/foundry/action-types/getting-started/#add-submission-criteria) does not reference a user; update any user references to refer to groups instead.
## Adding action types to products
要将 action type 添加到 product 中，首先[创建一个 product](/docs/foundry/foundry-devops/create-products/)，然后选择 **Action type** 内容类型，如下所示。

To add an action type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/) and then select the **Action type** content type as below.
![Add action type.](/docs/resources/foundry/action-types/marketplace-add-action-type.png)
然后系统将提示您选择一个 action type。

You will then be prompted to choose an action type.
![Add action type dialogue.](/docs/resources/foundry/action-types/marketplace-add-action-type-dialog.png)
虽然您可以直接选择 action types，但我们建议先添加诸如 [Workshop applications](/docs/foundry/workshop/marketplace-workshop/) 之类的内容，然后通过 dependencies 面板选择相关的 actions，如下所示。

While you can select action types directly, we recommend first adding content like [Workshop applications](/docs/foundry/workshop/marketplace-workshop/) and then selecting relevant actions via the dependencies panel as shown below.
![Add action type via panel.](/docs/resources/foundry/action-types/marketplace-add-action-type-panel.png)