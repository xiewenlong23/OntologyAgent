<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/marketplace/
---
# Add Foundry Rules to a Marketplace products
使用 [Foundry DevOps](/docs/foundry/devops/overview/) 将您的 Foundry Rules workflow 包含在 [Marketplace products](/docs/foundry/devops/core-concepts/#product) 中，并使其他用户能够安装和重用它们。[了解如何创建您的第一个 product](/docs/foundry/foundry-devops/create-products/)。

Use [Foundry DevOps](/docs/foundry/devops/overview/) to include your Foundry Rules workflow in [Marketplace products](/docs/foundry/devops/core-concepts/#product) and enable other users to install and reuse them. [Learn how to create your first product](/docs/foundry/foundry-devops/create-products/).
## Supported features
支持所有 Foundry Rules 功能。

All Foundry Rules features are supported.
## Add Foundry Rules workflows to products
要将 Foundry Rules workflow 添加到 product 中，首先[创建一个 product](/docs/foundry/foundry-devops/create-products/)，然后选择 **Workshop Application** 内容类型，随后选择您的 [Foundry Rules 编写应用程序](/docs/foundry/foundry-rules/author-and-run-a-rule/)，如下所示。

To add a Foundry Rules workflow to a product, first [create a product](/docs/foundry/foundry-devops/create-products/) then select the **Workshop Application** content type, followed by your [Foundry Rules authoring application](/docs/foundry/foundry-rules/author-and-run-a-rule/), as below.
![Adding your Foundry Rules rules authoring application to your product](/docs/resources/foundry/foundry-rules/add-fr-workfhop.png)
添加 Workshop 应用程序后，转到 product 输入中的 **Foundry rules workflows** 部分，并包含您的 workflow。

After adding your Workshop application, go to the **Foundry rules workflows** section in your product's inputs and include your workflow.
![Adding the Foundry Rules workflow application to your product in the inputs section](/docs/resources/foundry/foundry-rules/including-fr-workflow.png)
一旦您的 workflow 被包含，额外的 object type 和 action types 将作为输入包含到您的 product 中。您可能希望将 `Rule` 和 `Proposal` object type 以及所有生成的 action types 都包含到您的 product 中。

Once your workflow has been included, additional object type and action types will be included as inputs to your product. You will likely want to include both the `Rule` and `Proposal` object types, along with all of the generated action types to your product.
![Adding the Rule and Proposal object types to your product](/docs/resources/foundry/foundry-rules/fr-add-object-types.png)
![Adding the Foundry Rules generated action types to your product](/docs/resources/foundry/foundry-rules/fr-add-action-types.png)
> **ℹ️ 注意**

> 当将 product 的安装模式设置为 `Production` 时，请确保在 Ontology Manager 应用程序的 `Datasources` 选项卡中为 `Rule` 和 `Proposal` object type 启用 `Only allow edits via actions`。如果不执行此步骤，用户在尝试创建 proposal 时将遇到 `Actions:PermissionDenied` 错误。
> **ℹ️ 注意**

> When setting your product's installation mode to `Production`, be sure to enable `Only allow edits via actions` for the `Rule` and `Proposal` object types in the `Datasources` tab of the Ontology Manager application. Without this step, users will encounter an `Actions:PermissionDenied` error when attempting to create a proposal.