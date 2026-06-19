<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/marketplace-ontology-types/
---
# Add object and link types to a Marketplace product
使用 [Foundry DevOps](/docs/foundry/devops/overview/) 将您的 object 和 link types 包含在 [Marketplace products](/docs/foundry/devops/core-concepts/#product) 中，以供其他用户安装和重用。[了解如何创建您的第一个 product。](/docs/foundry/foundry-devops/create-products/)

Use [Foundry DevOps](/docs/foundry/devops/overview/) to include your object and link types in [Marketplace products](/docs/foundry/devops/core-concepts/#product) for other users to install and reuse. [Learn how to create your first product.](/docs/foundry/foundry-devops/create-products/)
## Unsupported features
大多数 [object property types](/docs/foundry/object-link-types/properties-overview/) 在 Marketplace products 中受支持，但以下类型尚不可用：

Most [object property types](/docs/foundry/object-link-types/properties-overview/) are supported in Marketplace products, but the following are not yet available:
* [Cipher](/docs/foundry/cipher/overview/)
* Geo time
* Vector
* [Cipher](/docs/foundry/cipher/overview/)
* Geo time
* Vector
Marketplace products 尚不支持以下内容：

Marketplace products do not yet support the following:
* 包含 streaming datasources 的 object types

* 没有 datasource 的 object types

* Object types with streaming datasources
* Object types with no datasource
请注意，objects 本身无法与 Marketplace 一起打包。这意味着，例如，由 Actions 进行的 object 编辑无法打包到 Marketplace product 中。但是，可以打包 datasets 和 object types，以便在安装 Marketplace product 后创建新的 objects。

Note that objects themselves cannot be packaged with Marketplace. This means that, for example, object edits made by Actions cannot be packaged into a Marketplace product. However, datasets and object types can be packaged in order to create new objects after installation of a Marketplace product.
如果您需要对以上任何功能的支持，请联系您的 Palantir 代表。

If you require support for any of the above, contact your Palantir representative.
## Add object types to products
要将 object type 添加到 product 中，首先需要 [create a product](/docs/foundry/foundry-devops/create-products/)。 [Add outputs](/docs/foundry/foundry-devops/create-products/#add-outputs) 然后选择 **Add ontology entities** 选项。

To add an object type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). [Add outputs](/docs/foundry/foundry-devops/create-products/#add-outputs) and then select the **Add ontology entities** option.
然后系统会提示您选择一个 object type。选择 object type 后，您将看到相关 link type 的推荐，您可以根据需要将其添加到您的 product 中。

You will then be prompted to choose an object type. After selecting an object type, you will see recommendations for linked object types that you may want to add to your product.
![add object type](/docs/resources/foundry/object-link-types/marketplace-add-object-type-dialog.png)
## Add link types to products
要将 link type 添加到 product 中，首先 [create a product](/docs/foundry/foundry-devops/create-products/)，然后选择 **Link type** content type。

To add a link type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/) and then select the **Link type** content type.
然后系统会提示您选择一个 link type，如下所示。

You will then be prompted to choose a link type as below.
![add link type](/docs/resources/foundry/object-link-types/marketplace-add-link-type-dialog.png)
虽然您可以直接选择 link type，但我们建议先添加您的 object type，然后通过 [information panel](/docs/foundry/foundry-devops/create-products/#add-outputs) 选择相关的 link，如下所示。

While you can select link types directly, we recommend first adding your object types and then selecting relevant links via the [information panel](/docs/foundry/foundry-devops/create-products/#add-outputs) as below.
![add link type via panel](/docs/resources/foundry/object-link-types/marketplace-add-link-type-panel.png)
## Add shared properties to products
要将 shared property type 添加到 product 中，首先 [create a product](/docs/foundry/foundry-devops/create-products/)。然后，选择 **Shared property** content type，如下所示。

To add a shared property type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). Then, select the **Shared property** content type as shown below.
然后系统会提示您选择一个 shared property。

You will then be prompted to choose a shared property.
![Add a shared property to a Marketplace product.](/docs/resources/foundry/object-link-types/marketplace-add-shared-property-dialog.png)
## Add interface types to products
要将 interface type 添加到 product 中，首先 [create a product](/docs/foundry/foundry-devops/create-products/)。然后，选择 **Interface** content type，如下所示。

To add an interface type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). Then, select the **Interface** content type as shown below.
然后系统会提示您选择一个 interface。

You will then be prompted to choose an interface.
![Add an interface type to a Marketplace product.](/docs/resources/foundry/object-link-types/marketplace-add-interface-dialog.png)