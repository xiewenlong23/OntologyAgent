<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/create-object-type/
---
# Create an object type
创建和配置新 object type 的主要方式是使用 [**guided step-by-step helper**](#create-a-new-object-type-with-the-helper)。推荐使用该引导式 helper，但如果您在完成 object 创建过程之前退出了 helper，您也可以通过指定 metadata、backing datasource、property mappings 以及 keys（primary 和 title）[**手动**](#create-a-new-object-type-manually) 完成新 object type 的创建过程。

The primary way to create and configure a new object type is with a [**guided step-by-step helper**](#create-a-new-object-type-with-the-helper). The guided helper is the recommended method, but if you exit the helper before completing the object creation process, you can also [**manually**](#create-a-new-object-type-manually) complete the process by specifying the metadata, backing datasource, property mappings, and keys (primary and title) for the new object type.
创建新 object type 之后，您可以从分配的默认名称 [更改 API 名称](#configure-api-names)。

After creating a new object type, you can [change the API name](#configure-api-names) from the assigned default.
此页面还包含有关新 object type 创建过程的 [故障排除](#troubleshooting) 信息。

This page also contains [troubleshooting](#troubleshooting) information on the new object type creation process.
## Create a new object type with the helper
* [创建新的 object type](#create-a-new-object-type)

* [选择 backing datasource](#choosing-a-backing-datasource)

* [Object type metadata](#object-type-metadata)
* [为 object type 创建 properties](#create-properties-for-the-object-type)

* [配置 primary key 和 title key](#configure-the-primary-key-and-title-key)

* [生成 actions](#generate-actions)

* [保存位置](#save-location)

* [将更改保存到 ontology](#save-change-to-ontology)

* [Create a new object type](#create-a-new-object-type)
* [Choose a backing datasource](#choosing-a-backing-datasource)
* [Object type metadata](#object-type-metadata)
* [Create properties for the object type](#create-properties-for-the-object-type)
* [Configure the primary key and title key](#configure-the-primary-key-and-title-key)
* [Generate actions](#generate-actions)
* [Save location](#save-location)
* [Save change to ontology](#save-change-to-ontology)
### Create a new object type
要创建新的 Object Type，请从 Ontology Manager 主页中选择 **Create your first object type** 选项，或者在同一页面右上角选择 **New > Create object type**。

To create a new object type, select the **Create your first object type** option from the Ontology Manager homepage or choose **New > Create object type** located on top right on the same page.

> 📷 **[图片: Select object type from the New dropdown menu.]**

> 📷 **[图片: Select object type from the New dropdown menu.]**

**Create new object type** 助手将会出现。

The **Create new object type** helper will appear.

> 📷 **[图片: New object type datasource step.]**

> 📷 **[图片: New object type datasource step.]**

### Choosing a backing datasource
如果您在 Foundry 中已有包含用于支撑该 Object Type 数据的现有 datasource，则可以选择它。这将自动填充该 Object Type 的元数据。它还会将 backing datasource 的每一列映射到一个 property，但您可以在 **Properties** 步骤中丢弃已添加的 properties。

If you have an existing datasource in Foundry containing data to back the object type then you can select it. This will automatically populate the object type's metadata. It will also map every column of the backing datasource to a property, but you can discard added properties in the **Properties** step.
> **⚠️ 警告: Warning**

> Object Type 的 backing datasource 不得包含 `MapType` 或 `StructType` 列。
> **⚠️ 警告: Warning**

> A backing datasource for an object type may not contain `MapType` or `StructType` columns.
如果您没有包含该 Object Type 数据的现有 datasource，可以选择在没有现有 datasource 的情况下继续，并选择一个位置以生成用于权限管理的 dataset。如果您使用的是 Object Storage v1，则此选项不可用。由于 Object Type 的对象权限由其 backing datasources 的位置决定，因此系统将提示您选择一个位置，以便向其保存一个空 dataset。

If you do not have an existing datasource containing data for the object type, you can choose to continue without an existing datasource and select a location to generate a dataset for permissions. This option is not available if you are using Object Storage v1. As permissions of the objects of a type are determined by the location of their backing datasources, you will be prompted to choose a location to which you want to save an empty dataset.

> 📷 **[图片: New object type datasource location]**

> 📷 **[图片: New object type datasource location]**

### Object type metadata
在此步骤中，请提供有关您的新 Object Type 的以下信息：

In this step, provide the following information regarding your new object type:
* **Icon（图标）：** 选择默认图标以自定义 Object Type 的图标和颜色；当用户查看该类型的对象时，此图标和颜色将显示在用户应用程序中。

* **Name（名称）：** 在用户应用程序中显示给任何访问该类型对象的人员的名称。

* **Plural name（复数名称）：** 在用户应用程序中显示给任何访问该类型多个对象的人员的名称。

* **Description（描述）：** 在用户应用程序中为访问该类型对象的任何人员提供的说明性文本。例如，在 Object Explorer 中进行搜索的用户将在其搜索结果中查看该 Object Type 的描述。

* **Groups（分组）：** 选择此 Object Type 是否属于任何分组。这是一种组织您的 ontology 的机制，便于您稍后过滤要使用的 Object Types。

* **Icon:** Select the default icon to customize the icon and color of the object type; this icon and color will be displayed in user applications when a user views an object of this type.
* **Name:** The name shown to anyone accessing an object of this type in user applications.
* **Plural name:** The name shown to anyone accessing multiple objects of this type in user applications.
* **Description:** Explanatory text for anyone accessing the objects of this type in user applications. For example, users searching in Object Explorer will view the description of the object type in their search results.
* **Groups:** Choose whether this object type will be part of any groups. This is a mechanism for organizing your ontology, making it easier to filter for the object types you want to work with later.

> 📷 **[图片: New object type metadata step.]**

> 📷 **[图片: New object type metadata step.]**

### Create properties for the object type
在对话框的第三步中，您可以自定义 Object Type 将具有的 properties。如果您选择了现有的 Foundry datasource，则任何列都将自动映射，但可以在此步骤中丢弃。

In the third step of the dialog you can customize which properties the object type will have. If you have chosen an existing Foundry datasource, any columns will be mapped automatically, but can be discarded during this step.
每个 Object Type 至少需要一个 property。这是因为 Object Types 需要一个主键来唯一标识它们。该向导允许您添加任何其他所需的 properties。

Every object type requires at least one property. This is because object types need a primary key to uniquely identify them. The wizard allows you to add any other desired properties.
请注意，需要高级配置的 property 类型（例如 media）无法作为 bootstrapping 向导的一部分生成，必须在退出该向导后添加。

Note that property types that require advanced configuration, such as media, cannot be generated as part of the bootstrapping wizard and must be added after you have exited it.

> 📷 **[图片: New object type properties step]**

> 📷 **[图片: New object type properties step]**

### Configure the primary key and title key
作为 **Properties** 步骤的一部分，你需要选择一个 primary key 和 title key：

As part of the **Properties** step you need to choose a primary key and title key:
* **Title key：**作为该类型对象的显示名称的 property。

* 例如，将 `full name` property 选为 `Employee` object type 的 title key，则该 property 的值（如 "Melissa Chang"、"Akriti Patel" 或 "Diego Rodriguez"）将用作各个相应的 `Employee` object 的显示名称。

* **Primary key：**作为 object type 每个实例的唯一标识符的 property。底层 datasource 中每一行的该 property 值必须不同。

* 例如，`employee ID` property 的值将用于在组织内将 "Melissa Chang" 标识为唯一的员工。

* **Title key:** The property that acts as a display name for objects of this type.
* For example, selecting the `full name` property as the title key of the `Employee` object type would use the values of that property, such as “Melissa Chang”, “Akriti Patel”, or “Diego Rodriguez” as the display names for each respective notional `Employee` object.
* **Primary key:** The property that acts as a unique identifier for each instance of an object type. Each row in the backing datasource must have a different value for this property.
* For example, the value of the `employee ID` property will be used to identify “Melissa Chang” as a unique employee within the organization.
支持的 property 类型列表可以在 [object type properties documentation](/docs/foundry/object-link-types/properties-overview/#supported-property-types) 中找到。

A list of supported property types can be found in the [object type properties documentation](/docs/foundry/object-link-types/properties-overview/#supported-property-types).

> 📷 **[图片: New object type]**

> 📷 **[图片: New object type]**

> **⚠️ 警告**

> 在分配 primary key 之前，请务必检查你的底层 datasource 中是否存在重复项。你选择的 primary key 在 datasource 的每条记录中必须是唯一的。如果你的 ontology 正在使用 [Object Storage v2](/docs/foundry/object-backend/overview/)，重复的 primary key 将导致 [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) 错误，从而导致 build 失败。如果你使用的是 Object Storage v1 (Phonograph)，更新将显示为成功；但是，重复的 primary key 可能会对你的 ontology 造成意外更改。
> **⚠️ 警告**

> Be sure to check your backing datasources for duplicates before assigning a primary key. The primary key you select must be unique for every record in the datasource. If your ontology is using [Object Storage v2](/docs/foundry/object-backend/overview/), a duplicate primary key will cause [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) errors leading to a build failure. If you are using Object Storage v1 (Phonograph), an update will appear as successful; however, the duplicate primary keys can cause unexpected changes to your ontology.
> **⚠️ 警告**

> Primary key 应当是确定性的（deterministic）。如果 primary key 是非确定性的并在 build 时发生变化，则编辑内容可能会丢失，link 也可能会消失。编辑内容可能会丢失，是因为 ontology 的编辑与 object 的 primary key 相关联。如果 build 之间未协调更新 link ID，则 object 之间的 link 可能会消失。为确保 primary key 的确定性，你应当定义 pipeline 逻辑，使 primary key 是单个列或多个列的 function。避免使用编号行或随机 key 生成方式，因为这些方式可能导致 primary key 在不同的 build 运行之间发生变化。
> **⚠️ 警告**

> Primary keys should be deterministic. If the primary key is non-deterministic and changes on build, edits can be lost and links may disappear. Edits can be lost because ontology edits are associated with the primary key of the object. Links between objects can disappear if builds are not coordinated to update link IDs. To ensure deterministic primary keys, you should define pipeline logic such that the primary key is the function of either a single column or multiple columns. Avoid using numbered row or random key generation, since these can cause primary keys to change between build runs.
### Generate actions
你可以选择性地生成一组标准 actions 来编辑该类型的 objects，并分配可以运行这些 actions 的特定用户或组。

You can optionally generate a standard set of actions to edit objects of this type and assign a specific user or group that can run them.
请注意，即使你已经完成 object type 的创建并退出 helper，你仍然可以编辑这些 actions 或创建新的附加 actions。

Note that you can still make edits to these actions or create new additional actions even if you have finalized the object type and exited the helper.

> 📷 **[图片: New object type Actions step]**

> 📷 **[图片: New object type Actions step]**

如果你使用的是 Object Storage v1，则此步骤不可用。

This step is not available if you are using Object Storage v1.
### Save location
在最后一步中，选择一个 project 来保存该 object type。然后选择 **Create**。选择 **Create** 只会暂存你的更改，而**不会保存**它们。

In the final step, choose a project to save this object type to. Then, select **Create**. Selecting **Create** will only stage your changes and **will not save** them.

> 📷 **[图片: New object type Save location step.]**

> 📷 **[图片: New object type Save location step.]**

### Save change to ontology
返回 Ontology Manager，在右上角选择 **Save**，以 [对 ontology 进行更改](/docs/foundry/ontology-manager/save-changes/)。

Back in Ontology Manager, select **Save** in the upper right corner to [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/).
## Create a new object type manually
使用 helper 创建新的 object type 时，可以在完成上述 [**Create a new object type** helper instructions](#create-a-new-object-type-with-the-helper) 中的所有步骤之前选择 **Create**。在流程完成之前选择 **Create** 将退出 helper 并将你带到 **Overview** 页面。

When creating a new object type with the helper, it is possible to select **Create** before completing all the steps in the [**Create a new object type** helper instructions](#create-a-new-object-type-with-the-helper) above. Selecting **Create** before the process is complete will exit the helper and bring you to the **Overview** page.
此时，object type 尚未保存，在完成以下所有步骤之前无法保存。在 **Create a new object type** helper 之外手动完成创建过程的步骤如下所述：

At this point, the object type is unsaved and cannot be saved until all the steps below have been completed. The steps for completing the creation process manually (outside the **Create a new object type** helper) are described below:
* [为新 Object Type 添加元数据](#add-metadata-for-a-new-object-type)

* [为新 Object Type 添加 backing datasource](#add-a-backing-datasource-to-a-new-object-type)

* [添加新 Property](#add-a-new-property)

* [将单个 Property 映射到数据](#map-a-single-property-to-data)

* [将所有未映射的列映射为新 Property](#map-all-unmapped-columns-as-new-properties)

* [配置 primary key 和 title key](#configure-the-primary-key-and-title-key)

* [Add metadata for a new object type](#add-metadata-for-a-new-object-type)
* [Add a backing datasource to a new object type](#add-a-backing-datasource-to-a-new-object-type)
* [Add a new property](#add-a-new-property)
* [Map a single property to data](#map-a-single-property-to-data)
* [Map all unmapped columns as new properties](#map-all-unmapped-columns-as-new-properties)
* [Configure the primary key and title key](#configure-the-primary-key-and-title-key)
### Add metadata for a new object type
在 **Overview** 页面的元数据部分，您可以编辑 object type 的显示名称、复数显示名称、描述和 ID：

On the **Overview** page’s metadata section, you can edit the object type’s display name, plural display name, description, and ID:
1. **Display name:** 任何在用户应用程序中访问此类型对象的人所看到的名称。

2. **Plural display name:** 任何在用户应用程序中访问此类型多个对象的人所看到的名称。

3. **Aliases:** 用户搜索时将找到此 object type 的附加术语。

4. **Description:** 为任何在用户应用程序中访问此类型对象的人提供的说明文本。例如，在 Object Explorer 中搜索的用户将在其搜索结果中查看该 object type 的描述。

5. **Groups:** 用于对 object type 进行分类的一个或多个标签。

6. **ID:** object type 的唯一标识符，主要用于在配置用户应用程序时引用此类型的对象。
* ID 可以包含小写字母、数字和短横线。
* ID 的第一个字符**必须**是小写字母。

* 一旦 property 的 ID 被保存并在用户应用程序中被引用，对 property ID 的**任何**更改都将破坏该应用程序。

7. **Icon:** 从 object type 视图侧边栏选择默认图标，以自定义 object type 的图标和颜色；当用户查看此类型的对象时，此图标和颜色将显示在用户应用程序中。

8. **Backing datasource:** 用作此类型对象 property 值的数据源。

1. **Display name:** The name shown to anyone accessing an object of this type in user applications.
2. **Plural display name:** The name shown to anyone accessing multiple objects of this type in user applications.
3. **Aliases:** Additional terms that will find this object type when users search for them.
4. **Description:** Explanatory text for anyone accessing the objects of this type in user applications. For example, users searching in Object Explorer will view the description of the object type in their search results.
5. **Groups:** One or more labels that help categorize the object type.
6. **ID:** A unique identifier of the object type, primarily used to reference objects of this type when configuring a user application.
* An ID can contain lowercase letters, numbers, and dashes.
* The first character of an ID **must** be a lowercase letter.
* Once a property’s ID is saved and the property is referenced in user applications, **any** change to the property ID will break the application.
7. **Icon:** Select the default icon from the object type view’s sidebar to customize the icon and color of the object type; this icon and color will be displayed in user applications when a user views an object of this type.
8. **Backing datasource:** The source of the data used as property values for objects of this type.
![Overview page](/docs/resources/foundry/object-link-types/create-object-type-new-object-overview-page-annotated.png)
***
### Add a group to an object type
[Groups](/docs/foundry/object-link-types/type-groups/) 是用于对 object type 进行分类的标签。从 object type 元数据小部件中，您可以：

[Groups](/docs/foundry/object-link-types/type-groups/) are labels that help categorize object types. From the object type metadata widget, you can:
* 从现有 group 列表中添加一个 group。

* 通过输入该 group 的名称来创建一个新 group。

* 从您的 object type 中移除一个 group。

* Add a group from a list of existing groups.
* Create a new group by typing the name of that group.
* Remove a group from your object type.

> 📷 **[图片: 选择或添加新的 object type group]**

> 📷 **[图片: Choose or add a new object type group]**

Groups 可以在 [Ontology Manager 的 **Search** 栏和 **Search** 栏对话框](/docs/foundry/ontology-manager/navigation/#header-search-bar) 中进行搜索。Ontology Manager 中的 object type 表支持按 group 进行显示和过滤。Groups 还会显示在 [Object Explorer 主页](/docs/foundry/object-explorer/getting-started/#group-exploration-b-c-d) 上。

Groups are searchable in the [Ontology Manager's **Search** bar and **Search** bar dialog](/docs/foundry/ontology-manager/navigation/#header-search-bar). The table of object types in the Ontology Manager supports displaying and filtering by group. Groups are also displayed on the [Object Explorer home page](/docs/foundry/object-explorer/getting-started/#group-exploration-b-c-d).

> 📷 **[图片: 添加新的 object type group]**

> 📷 **[图片: Add a new object type group]**

> **⚠️ 警告: Warning**

> 在 object type 元数据中将 groups 作为标签使用，取代了之前向 primary key property 添加 `oe_home_page_object_type_group` 类型 class 的方法；该旧方法已不再可用。
> **⚠️ 警告: Warning**

> Groups as labels in object type metadata replace the previous method of adding `oe_home_page_object_type_group` type class to the primary key property; this previous method is no longer available.
***
### Add a backing datasource to a new object type
为了使用数据填充此类型对象的 property 值，您必须添加一个 backing datasource。您可以通过以下方式执行此操作：

In order to populate property values for objects of this type with data, you must add a backing datasource. You can do this by:
* 通过从 **Overview** 页面的 **Properties** 部分选择 **Create new**，或从 object type 视图侧边栏的 **Properties** 页面选择 **Edit property mapping** 按钮，进入 Property 编辑器。

* 然后，如下图所示，选择 **Add a backing datasource** 按钮。这将允许您选择 Foundry 中任何可用的 datasource 作为 backing datasource。

* 请注意，单个 datasource 只能用于支持一个 object type。

* Navigating into the Property editor by selecting **Create new** from the **Properties** section of the **Overview** page, or by selecting the **Edit property mapping** button from the **Properties** page of the object type view’s sidebar.
* Then, select the **Add a backing datasource** button as shown in the image below. This will allow you to select any of the available datasources in Foundry as a backing datasource.
* Note that a single datasource can only be used to back one object type.
![Edit backing dataset](/docs/resources/foundry/object-link-types/create-object-type-edit-backing-dataset.png)
### Add a new property
在 property 编辑器中，从屏幕右侧的 **Properties** 窗格中选择 **Add**。这将向 object type 添加一个新 property。

From within the property editor, select **Add** in the **Properties** pane on the right side of the screen. This will add a new property to the object type.
![Add a new property](/docs/resources/foundry/object-link-types/create-object-type-add-new-property.png)
### Map a single property to data
可以通过以下任何方式将 property 映射到 backing datasource 中的列：

It is possible to map properties to columns in a backing datasource in any of the following ways:
* [将列映射到新 property](#map-a-column-to-a-new-property)

* [将列映射到现有 property](#map-a-column-to-an-existing-property)

* [将 property 映射到列](#map-a-property-to-a-column)

* [Map a column to a new property](#map-a-column-to-a-new-property)
* [Map a column to an existing property](#map-a-column-to-an-existing-property)
* [Map a property to a column](#map-a-property-to-a-column)
#### Map a column to a new property
在屏幕左侧的 datasource 窗格中（见下图），您可以看到该 datasource 的所有列。将鼠标悬停在您要映射的列上，然后选择 **Add as a new property** 按钮，以创建一个映射到此列的新 property。Property ID、display name 和 base type 将根据列名推断得出。

In the datasource pane on the left side of the screen (see image below), you can see all of the columns of the datasource. Hover over the column you want to map and select the **Add as a new property** button to create a new property mapped to this column. The property ID, display name, and base type will be inferred from the name of the column.
![Add as a new property](/docs/resources/foundry/object-link-types/create-object-type-add-as-a-new-property.png)
#### Map a column to an existing property
在屏幕左侧的 datasource 面板中,您可以看到 datasource 的所有列。将鼠标悬停在未映射的列上,然后选择 **Add as a new property** 按钮。如果已存在 property ID 与列名匹配的 property,则该列将映射到现有的 property。

In the datasource pane on the left side of the screen, you can see all of the columns of the datasource. Hover over an unmapped column and select the **Add as a new property** button. If a property already exists with a property ID that matches the column name, the column will be mapped to the existing property.
#### Map a property to a column
在屏幕右侧的 properties 面板中,将鼠标悬停在您想要映射到列的 property 上,然后选择 **Map to a column**。这将打开一个下拉菜单,您可以从中选择要映射到该 property 的列。

In the properties pane on the right side of the screen, hover over the property you want to map to a column and select **Map to a column**. This will open a dropdown from which you can select the column you want to map to your property.
![Map a property to a column](/docs/resources/foundry/object-link-types/create-object-type-map-property-to-column.png)
### Map all unmapped columns as new properties
在 datasource 面板中 datasource 名称旁边,您会找到一个 **Add all unmapped columns as new properties** 按钮。选择该按钮将为 datasource 中所有未映射的列创建 properties。这些 properties 的 ID、display name 和 base type 将从 datasource 中相应的列推断得出。

Next to the datasource name in the datasource pane, you will find an **Add all unmapped columns as new properties** button. Selecting the button will create properties for all the unmapped columns in the datasource. The IDs, display names, and base types of the properties will be inferred from the corresponding columns in the datasource.
* 一旦 property 的 ID 被保存并且该 property 在用户应用程序中被引用,对 property ID 所做的 **任何** 更改都将破坏该应用程序。

* Once a property’s ID is saved and the property is referenced in user applications, **any** change to the property ID will break the application.
![Add all unmapped columns as new properties](/docs/resources/foundry/object-link-types/create-object-type-add-all-unmapped-columns-as-new-properties.png)
### Configure the primary key and title key
现在您已经创建了新的 object type、添加了 backing datasource 并将其映射到新的 properties,仍然需要在能够保存 object type 之前配置 primary key 和 title key。您可以导航到 property 编辑器中的 property 元数据面板(见下图),将 property 设置为 primary key 和 title key:

Now that you've created your new object type, added a backing datasource, and mapped it to new properties, you still need to configure the primary key and title key before being able to save your object type. You can navigate to the property metadata pane in the property editor (see image below) to set a property as the primary key and title key:

> 📷 **[图片: Configure primary key and title key]**

> 📷 **[图片: Configure primary key and title key]**

* **Primary key:** 作为 object type 每个实例唯一标识符的 property。backing datasource 中每一行的该 property 值必须不同。

* 例如,`employee ID` property 的值将用于在组织内将 "Melissa Chang" 标识为唯一的(名义上的)employee。

* 若要配置 primary key,请在 property 编辑器的 properties 面板中选择要分配为 primary key 的 property,然后勾选 **Primary key** 选项。

* 编辑会永久附加到您为其进行编辑的 primary key 值上。每当您更改 object type 的 primary key 时,系统将提示您删除所有现有编辑。

* **Title key:** 作为此类型 object 显示名称的 property。

* 例如,选择 `full name` property 作为 `Employee` object type 的 title key 将使用该 property 的值(如 "Melissa Chang"、"Akriti Patel" 或 "Diego Rodriguez")作为各个相应名义上的 `Employee` object 的 display name。

* 若要配置 title key,请在 property 编辑器的 properties 面板中选择要分配为 title key 的 property,然后勾选 **Title key** 选项。

请注意,在此之前,您的更改已被暂存但 **尚未保存**。要将您的新 object type 保存到 Ontology,请按照[如何将更改保存到 Ontology](/docs/foundry/ontology-manager/save-changes/)中的说明进行操作。

* **Primary key:** The property that acts as a unique identifier for each instance of an object type. Each row in the backing datasource must have a different value for this property.
* For example, the value of the `employee ID` property will be used to identify “Melissa Chang“ as a unique (notional) employee within the organization.
* To configure the primary key, select the property you want to assign to the primary key in the properties pane of the property editor and check the **Primary key** option.
* Edits are permanently attached to the primary key value you made them for. Any time you change the primary key of an object type, you will be prompted to delete all existing edits.
* **Title key:** The property that acts as a display name for objects of this type.
* For example, selecting the `full name` property as the title key of the `Employee` object type will use the values of that property, such as “Melissa Chang”, “Akriti Patel”, or “Diego Rodriguez” as the display names for each respective notional `Employee` object.
* To configure the title key, select the property you want to assign to the title key in the properties pane of the property editor and check the **Title key** option.
Note that until this point, your changes have been staged but **have not yet been saved**. To save your new object type to the Ontology, follow the instructions on [how to save changes to the Ontology](/docs/foundry/ontology-manager/save-changes/).
> **⚠️ 警告**

> 在分配 primary key 之前,请务必检查您的 backing datasources 中是否存在重复项。您选择的 primary key 在 datasource 的每条记录中必须是唯一的。如果您的 Ontology 正在使用 [Object Storage V2](/docs/foundry/object-backend/overview/),重复的 primary key 将导致 [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) 错误,从而导致构建失败。如果您使用的是 Object Storage V1(也称为 Phonograph),更新将显示为成功;但是,重复的 primary key 可能会导致 Ontology 出现意外更改。
> **⚠️ 警告**

> Be sure to check your backing datasources for duplicates before assigning a primary key. The primary key you select must be unique for every record in the datasource. If your Ontology is using [Object Storage V2](/docs/foundry/object-backend/overview/), a duplicate primary key will cause [Funnel batch pipeline](/docs/foundry/object-indexing/funnel-batch-pipelines/) errors leading to a build failure. If you are using Object Storage V1 (also known as Phonograph), an update will appear as successful; however, the duplicate primary keys can cause unexpected changes to your Ontology.
## Configure API names
API name 是在代码中以编程方式引用 object type 或 property 时所使用的名称。所有新创建的 object type 和 property 都会自动分配从其 display name 推断而来的 API name。[了解更多关于 API name 的信息。](/docs/foundry/functions/api-objects-links/)

An API name is the name used when referring to an object type or a property programmatically in code. All new object types and properties are automatically assigned API names that are inferred from their display names. [Learn more about API names.](/docs/foundry/functions/api-objects-links/)
您可以按如下方式更改自动分配的 API name:

You can change the automatically assigned API names as follows:
* Object type 的 API name 可以在该 object type 的 **Overview** 页面中进行编辑。

* Property 的 API name 可以在 property 编辑器的 properties 面板中进行编辑。

* An object type’s API name can be edited in the object type’s **Overview** page.
* A property’s API name can be edited in the properties pane of the property editor.
### Naming guidelines
Object type 的 API name 遵循函数式编码标准。Object type 的 API name 必须:

Object type API names follow functional coding standards. An object type’s API name must:
* 以大写字符开头,且仅由字母数字字符组成。

* 使用 PascalCase 编写(也称为 UpperCamelCase,即复合词中每个单词的首字母大写;例如 "ThisExampleName")。

* 在所有 object type 中唯一。
* 长度在 1 到 100 个字符之间。

* Begin with an uppercase character and consist of only alphanumeric characters.
* Be written in PascalCase (also known as UpperCamelCase, in which the first letter of each word in a compound word is capitalized; for instance, “ThisExampleName”).
* Be unique across all object types.
* Be between 1 and 100 characters long.

> 📷 **[图片: Object type API]**

> 📷 **[图片: Object type API]**

Property 的 API name 必须:

A property’s API name must:
* 以小写字符开头,且仅由字母数字字符组成。

* 使用 camelCase 格式编写(复合词中第一个单词之后的每个单词首字母大写;例如 "thisExampleName")。

* 在属于同一 Object Type 的所有 Property 中必须唯一。
* 长度介于 1 到 100 个字符之间。

* Begin with a lowercase character and consist of only alphanumeric characters.
* Be written in camelCase (in which the first letter of each word after the first word in a compound word is capitalized; for instance, “thisExampleName”).
* Be unique across all properties belonging to the same object type.
* Be between 1 and 100 characters long.

> 📷 **[图片: Property type API]**

> 📷 **[图片: Property type API]**

## Troubleshooting
### Mandatory object type fields
要保存新的 Object Type,以下 Object Type 字段不能为空:

To save a new object type, the following object type fields must not be empty:
* ID
* Display name
* Plural display name
* Backing datasource
* API name
* ID
* Display name
* Plural display name
* Backing datasource
* API name
此外,以下 Property 字段不能为空:

Additionally, the following property fields must not be empty:
* Property ID
* Property display name
* Backing column
* Property API name
* Title key
* Primary key
* Property ID
* Property display name
* Backing column
* Property API name
* Title key
* Primary key
### Valid ID checklist
#### Object type ID
Object type IDs:
Object type IDs:
* 可以由小写字母、数字和短横线组成。
* 应以字母开头。

* 在所有 Object Type 中必须唯一。

* Can be made up of lowercase letters, numbers, and dashes.
* Should start with a letter.
* Must be unique across all object types.
#### Property type ID
Property type IDs:
Property type IDs:
* 可以由大小写字母、数字、短横线和下划线组成。
* 应以字母开头。

* 在属于同一 Object Type 的所有 Property 中必须唯一。

* Can be made up of lowercase or uppercase letters, numbers, dashes, and underscores.
* Should start with a letter.
* Must be unique across all properties that belong to the same object type.
#### API name
根据函数式编码标准,Object Type 的 API name 必须:

In line with functional coding standards, an object type’s API name must:
* 仅由字母数字字符和下划线组成。

* 在所有 Object Type 中必须唯一。
* 长度介于 1 到 100 个字符之间。

* Consist of only alphanumeric characters and underscores.
* Be unique across all object types.
* Be between 1 and 100 characters long.
Property 的 API name 必须:

A property’s API name must:
* 是有效的 Unicode 字符。

* 在属于同一 Object Type 的所有 Property 中必须唯一。
* 长度介于 1 到 100 个字符之间。

* Be valid Unicode.
* Be unique across all properties belonging to the same object type.
* Be between 1 and 100 characters long.
注意,有一些保留关键字不能用作 API name。它们是:`ontology`、`object`、`property`、`link`、`relation`、`rid`、`primaryKey`、`typeId` 和 `ontologyObject`。

Note that there are a number of reserved keywords that cannot be used for API names. They are: `ontology`, `object`, `property`, `link`, `relation`, `rid`, `primaryKey`, `typeId`, and `ontologyObject`.
### Errors
#### Error: `Phonograph2:DatasetAndBranchAlreadyRegistered`
如果您收到错误 `Phonograph2:DatasetAndBranchAlreadyRegistered`，则您尝试保存的 Object Type 所依赖的 datasource 已经在 Ontology 中为另一个 Object Type 提供支持，无法再次使用。

If you receive the error `Phonograph2:DatasetAndBranchAlreadyRegistered`, the datasource backing the object type you are trying to save is already backing a different object type in the Ontology and cannot be used again.