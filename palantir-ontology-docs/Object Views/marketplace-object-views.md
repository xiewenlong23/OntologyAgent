<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/marketplace-object-views/
---
# Add Object Views to a Marketplace product
使用 [Foundry DevOps](/docs/foundry/devops/overview/) 将您的 Object View 包含在 [Marketplace products](/docs/foundry/devops/core-concepts/#product) 中,以便其他用户安装和重用。[了解如何创建您的第一个 product。](/docs/foundry/foundry-devops/create-products/)

Use [Foundry DevOps](/docs/foundry/devops/overview/) to include your Object Views in [Marketplace products](/docs/foundry/devops/core-concepts/#product) for other users to install and reuse. [Learn how to create your first product.](/docs/foundry/foundry-devops/create-products/)
## Supported features
Marketplace products 仅支持使用 [Workshop tab](/docs/foundry/object-views/config-object-views/) 构建器的 [Object View tabs](/docs/foundry/object-views/config-tabs/)。不支持旧版 Object View 构建器。如果您希望打包使用旧版构建器的 Object View tab,您应该首先使用 Workshop tab 构建器重建该 tab。

Marketplace products only support [Object View tabs](/docs/foundry/object-views/config-tabs/) that use the [Workshop tab](/docs/foundry/object-views/config-object-views/) builder. The legacy Object View builder is not supported. If you would like to package an Object View tab that leverages the legacy builder, you should first rebuild the tab with the Workshop tab builder.
## Add Object Views to products
要将 Object View 添加到 product 中,请先 [创建一个 product](/docs/foundry/foundry-devops/create-products/)。然后 [添加 outputs](/docs/foundry/foundry-devops/create-products/#add-outputs) 并选择 **Add ontology entities** 选项。

To add an Object View to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). [Add outputs](/docs/foundry/foundry-devops/create-products/#add-outputs) and then select the **Add ontology entities** option.
选择 Object View 后,您可以选择要在 product 中包含哪些 tabs。

Once you have selected an Object View, you can select which tabs you would like to include in your product.
![Add Object View tabs.](/docs/resources/foundry/object-views/marketplace-add-tabs.png)