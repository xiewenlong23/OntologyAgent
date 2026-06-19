<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/create-link-type/
---
# Create a link type
我们建议使用下面概述的引导助手来创建和配置新的 link type。但是,如果您在完成对象创建过程之前退出助手,可以通过指定 link type、keys 以及新 link type 的 API 名称来手动完成该过程。

We recommend creating and configuring a new link type with the guided helper outlined below. However, if you exit the helper before completing the object creation process, you can manually complete the process by specifying the link type, keys, and API names for the new link type.
## Access the link type creation helper
导航至 Ontology Manager。要访问 link type 创建助手,请选择以下方法之一:

Navigate to Ontology Manager. To access the link type creation helper, choose one of the following methods:
* 从右上角选择 **New**,然后选择 **Link type**。

> 📷 **[图片: Select Link type option from the New dropdown menu.]**

* Select **New** from the top right corner, then select **Link type**.

> 📷 **[图片: Select Link type option from the New dropdown menu.]**

* 在左侧边栏中,选择 **Resources** 下的 **Link types**。然后,在 **Link types** 页面的右上角选择 **New link type**。

* In the left sidebar, select **Link types** under **Resources**. Then, select **New link type** in the top right corner of the **Link types** page.
* 导航到您要链接的 object type,然后从该 object type 的 **Overview** 页面上的 link type 图中选择 **Create new link type**。

![Create a new link type](/docs/resources/foundry/object-link-types/create-new-link-type-button.png)

* Navigate to an object type you want to link, then select **Create new link type** from within the link type graph on the object type’s **Overview** page.

![Create a new link type](/docs/resources/foundry/object-link-types/create-new-link-type-button.png)

## Configure a new link type
新的 link type 助手将引导您完成以下步骤:

The new link type helper will guide you through the following steps:
* [Choose the relationship type](#choose-the-relationship-type)
* [Define link resources](#define-link-resources)
* [Foreign key relationship type](#foreign-key-relationship-type)
* [Join table dataset relationship type](#join-table-dataset-relationship-type)
* [Backing object relationship type](#backing-object-relationship-type)
* [Define link type names](#define-link-type-names)
* [Save location](#save-location)
* [Save change to ontology](#save-change-to-ontology)
* [Choose the relationship type](#choose-the-relationship-type)
* [Define link resources](#define-link-resources)
* [Foreign key relationship type](#foreign-key-relationship-type)
* [Join table dataset relationship type](#join-table-dataset-relationship-type)
* [Backing object relationship type](#backing-object-relationship-type)
* [Define link type names](#define-link-type-names)
* [Save location](#save-location)
* [Save change to ontology](#save-change-to-ontology)
### Choose the relationship type
1. 在 **Create a new link type** 对话框的第一步中,为该 link 选择 relationship type。

2. 选择用于在两个对象之间定义 link 的 relationship type:

1. In the first step of the **Create a new link type** dialog, select the relationship type for the link.
2. Choose the relationship type for defining links between your two objects:
* **Object type foreign keys:** 支持 "one-to-one" 和 "many-to-one" 基数的 link types。此选项允许您选择表示外键的属性以及目标对象的相应主键。有关使用外键定义 link resources 的详情,请参阅 [below for details](#foreign-key-relationship-type)。

* **Join table dataset:** 适用于 "many-to-many" 基数的 link types。此选项允许您使用 join table dataset 作为 link 的后端。有关使用 dataset 定义 link resources 的详情,请参阅 [below for details](#join-table-dataset-relationship-type)。

* **Backing object type:** Object-backed link types 扩展了 many-to-one 基数 link types,提供对 object types 作为 link type 存储解决方案的 first-class 支持。有关由对象支持的 link resources 定义的详情,请参阅 [below for details](#backing-object-relationship-type)。有关更多信息,请参阅 [object-backed links](#object-backed-links) 部分。

* **Object type foreign keys:** Supports "one-to-one" and "many-to-one" cardinality link types. This option allows you to select properties that represent the foreign key and corresponding primary key for the desired objects. See [below for details](#foreign-key-relationship-type) in defining link resources with a foreign key.
* **Join table dataset:** For "many-to-many" cardinality link types. This option allows you to use a join table dataset to back the link. See [below for details](#join-table-dataset-relationship-type) in defining link resources with a dataset.
* **Backing object type:** Object-backed link types expand on many-to-one cardinality link types, providing first class support for object types as a link type storage solution. See [below for details](#backing-object-relationship-type) on defining link resources backed by an object. For additional information, refer to the [object-backed links](#object-backed-links) section.
在以下示例中,假设存在两个通过基数相互关联的 object type:`Aircraft` object type 和 `Flight` object type。基数类型包括:

In the examples below, assume that there are two object types that are related to each other through a cardinality: an `Aircraft` object type and a `Flight` object type. Cardinality types include:
* *One-to-one cardinality:* 这表示一个 `Aircraft` 应链接到单个 `Flight`。One-to-one 基数用作预期关系的指示符,但 one-to-one 基数不会被强制执行。

* *One-to-many cardinality:* 这表示一个 `Aircraft` 可以链接到多个 `Flights`。

* *Many-to-one cardinality:* 这表示多个 `Aircraft` 可以链接到一个 `Flight`。

* *Many-to-many cardinality:* 这表示一个 `Aircraft` 可以链接到多个 `Flights`,并且一个 `Flight` 可以链接到多个 `Aircraft`。

* *One-to-one cardinality:* This indicates that one `Aircraft` should be linked to a single `Flight`. The one-to-one cardinality serves as an indicator of the intended relationship, but the one-to-one cardinality is not enforced.
* *One-to-many cardinality:* This indicates that one `Aircraft` can be linked to many `Flights`.
* *Many-to-one cardinality:* This indicates that many `Aircraft` can be linked to one `Flight`.
* *Many-to-many cardinality:* This indicates that one `Aircraft` can be linked to many `Flights`, and one `Flight` can be linked to many `Aircraft`.
3. 选择 **Next** 进入下一步。

![Select the link type relationship type in the creation dialog](/docs/resources/foundry/object-link-types/create-link-relationship-type.png)

3. Select **Next** to proceed to the next step.

![Select the link type relationship type in the creation dialog](/docs/resources/foundry/object-link-types/create-link-relationship-type.png)

### Define link resources
#### Foreign key relationship type
[PARA_14]
在 one-to-one 或 many-to-one 基数 link type 中,您需要为该 link 定义 foreign key property 和 primary key properties。一个 object type 的 **foreign key** property 必须引用另一个 object type 的 **primary key** property。

In a one-to-one or many-to-one cardinality link type, you will define the foreign key property and primary key properties for the link. The **foreign key** property of one object type must refer to the **primary key** property of the other object type.
在 one-to-one 或 many-to-one 基数 link type 中,您需要为该 link 定义 foreign key property 和 primary key properties。一个 object type 的 **foreign key** property 必须引用另一个 object type 的 **primary key** property。

[/PARA_13]

[PARA_14]
例如,`Tail Number` property 是 `Aircraft` object type 上的 primary key。`Flight` object type 上的 `Flight Tail Number` property 是外键。当 `Aircraft` 的 `Tail Number` 与某个 `Flight` 的 `Flight Tail Number` 匹配时,将会在 `Aircraft` 和 `Flight` object types 之间创建 links。

For example, the `Tail Number` property is the primary key on the `Aircraft` object type. The `Flight Tail Number` property on the `Flight` object type is the foreign key. Links will be created between `Aircraft` and `Flight` object types when the `Tail Number` of the `Aircraft` matches a `Flight Tail Number` of a `Flight`.
1. 在 **Link resources** 步骤中,为您的 link 选择 object types。

1. In the **Link resources** step, choose the object types for your link.
2. 从右侧的下拉菜单中选择主键 object type(在我们示例中为 `Aircraft`)。

2. Select the primary key object type from the dropdown menu on the right (`Aircraft` in our example).
3. 从左侧的下拉菜单中选择外键 object type(在我们示例中为 `Flight`)。如果满足以下条件,创建对话框将自动检测并选择一个外键:

* 外键与所链接 object type 的主键匹配。

* 两个 object 的 property types 匹配。

3. Select the foreign key object type from the dropdown menu on the left (`Flight` in our example). The creation dialog will detect and automatically select a foreign key if the following conditions are met:
* The foreign key matches the primary key of the linked object type.
* The property types of both objects match.
4. 选择将构成 link 的 properties:

* 对于外键 object type,选择将用作源 object type 外键的 property(对于 `Flight` object types,选择 `Flight Tail Number`)。

* object type 的主键会自动选择,因为每个 object type 只有一个主键(对于 `Aircraft` object type,选择 `Tail Number`)。

4. Choose the properties that will form the link:
* For the foreign key object type, select the property that will be used as the foreign key for the source object type (`Flight Tail Number` for the `Flight` object types).
* The primary key of the object type is auto-selected since there is only one primary key for each object type (`Tail Number` for the `Aircraft` object type).
5. 选择 **Next** 继续。

![使用外键关系类型选择 link resources。](/docs/resources/foundry/object-link-types/create-link-foreign-key.png)

5. Select **Next** to continue.

![Select the link resources using a foreign key relationship type.](/docs/resources/foundry/object-link-types/create-link-foreign-key.png)

#### Join table dataset relationship type
在多对多 cardinality 中,选择一个包含第一个 object type 的主键(在我们示例中为 `Aircraft`)与第二个 object type(在我们示例中为 `Flight`)之间所有 link 组合的 datasource。

In a many-to-many cardinality, select a datasource that includes all combinations of links between the primary key of the first object type (`Aircraft` in our example) and the second object type (`Flight` in our example).
多对多 cardinality 需要一个 backing datasource,这是允许用户 [edit or write back](/docs/foundry/object-link-types/allow-editing/) 到 link type 所必需的。

A many-to-many cardinality, which requires a backing datasource, is required to enable users to [edit or write back](/docs/foundry/object-link-types/allow-editing/) to the link type.
1. 在 **Link resources** 步骤中,为您的 link 选择 object types。

2. 从左侧的下拉菜单中选择第一个 object type(`Flight`)。

3. 从右侧的下拉菜单中选择第二个 object type(`Aircraft`)。

4. 选择 join table dataset。选择一个包含与所选两个 object types 的主键匹配的列的 dataset。一个列只能映射到一个主键。

* 现在可以为新的 link types 自动生成 join table。**Generate join table** 选项将根据您所选的两个 object types 的主键创建一个具有正确 schema 的 dataset。这意味着,如果您拥有 user edit-backed 数据,或者您希望稍后提供生产数据,您可以更快地开始使用。

5. 选择 link type 的 backing datasource 中哪些列映射到每个所链接 object type 的主键。

6. 选择 **Next** 继续。

![选择 link type relationship type](/docs/resources/foundry/object-link-types/create-link-dataset.png)

1. In the **Link resources** step, choose the object types for your link.
2. Select the first object type from the dropdown menu on the left (`Flight`).
3. Select the second object type from the dropdown menu on the right (`Aircraft`).
4. Choose the join table dataset. Select a dataset that contains columns matching the primary keys for both selected object types. A column can only be mapped to one primary key.
* It is now possible to automatically generate a join table for new link types. The **Generate join table** option will create a dataset with the correct schema based on the primary keys of the two object types you have selected. This means that you can get started faster if you have user edit-backed data, or if you want to provide production data later on.
5. Select which columns in the link type’s backing datasource map to the primary keys of each of the linked object types.
6. Select **Next** to continue.

![Select link type relationship type](/docs/resources/foundry/object-link-types/create-link-dataset.png)

#### Backing object relationship type
在创建 object-backed link 之前,请确保已创建 [prerequisite](#prerequisites-for-creating-an-object-backed-link-type) object 和 links。

Before creating the object-backed link, ensure that the [prerequisite](#prerequisites-for-creating-an-object-backed-link-type) object and links have been created.
1. 选择在 prerequisites 中创建的 object types 以表示您所需的 link type。左右两侧的 objects 表示将链接在一起的两个实体。中间的 object 充当中介,并提供关于两个实体之间连接的额外元数据,并作为 link 的 backing。

2. 如果左侧和右侧的 objects 与中间的中介 object 之间存在多个 links,请使用下拉菜单选择左侧和右侧 objects 与中介 object 之间所需的 links。

![使用 object-backed link 选择 link resources。](/docs/resources/foundry/object-link-types/oblt-link-dialog.png)

1. Select the object types created in the prerequisites to represent your desired link type. The objects on the left and right represent the two entities that will be linked together. The object in the middle serves as the intermediary and provides additional metadata about the connection between the two entities, and backs the link.
2. If there are multiple links between the objects on the left and right and the intermediary object in the middle, use the dropdown menus to select the desired links between the left and right objects and the intermediary object.

![Select the link resources using an object-backed link.](/docs/resources/foundry/object-link-types/oblt-link-dialog.png)

### Define link type names
1. 在 **Link type names** 步骤中,为您的新的 link type 提供 display 和 API 名称。

2. 为 link type 的每一侧输入一个 display name。link type 的一侧表示到该 object type 的 link *to*。在我们示例中,`Aircraft` object type 的 display name 描述了从 `Flight` *to* `Aircraft` 的 link。您可以选择 display name `Assigned Aircraft`,因为一个 `Flight` 有一个 `Assigned Aircraft`。

3. API name 将根据 display name 自动生成,但您可以根据需要进行修改。

* API name 字段用于在代码中以编程方式引用 link type。link type 一侧的 API name 可用于返回该类型的 objects。例如,如果 link type 的 `Aircraft` 侧的 API name 为 `assignedAircraft`,那么调用 `Flight.assignedAircraft.get()` 将返回链接到这些 `Flight` objects 的 `Aircraft` objects。

* Link type API names *必须* 遵守以下规定:
* 以小写字符开头,且仅包含字母数字字符。

* 在与同一 object type 关联的所有 link types 中保持唯一。
* 长度在 1 到 100 个字符之间。

* 经过 NFKC 规范化处理。
* 不是保留关键字。

* [Learn more about API names.](/docs/foundry/functions/api-objects-links/)
4. 选择 **Next** 继续。

![为 link type 命名](/docs/resources/foundry/object-link-types/create-link-api.png)

1. In the **Link type names** step, provide the display and API names for your new link type.
2. Enter a display name for each side of the link type. A side of the link type represents the link *to* that object type. In our example, the display name for the `Aircraft` object type describes the link from `Flight` *to* `Aircraft`. You could choose the display name `Assigned Aircraft` since one `Flight` has one `Assigned Aircraft`.
3. The API name will be automatically generated based on the display name, but you can modify it if needed.
* The API name field is used when referring to a link type programmatically in code. The API name on a side of a link type can be used to return objects of that type. For example, if the API name on the `Aircraft` side of the link type is `assignedAircraft`, then calling `Flight.assignedAircraft.get()` will return the `Aircraft` objects linked to those `Flight` objects.
* Link type API names *must* adhere to the following:
* Begin with a lowercase character and consist of only alphanumeric characters.
* Be unique across all link types associated with the same object type.
* Be between 1 and 100 characters long.
* Be NFKC normalized.
* Not be a reserved keyword.
* [Learn more about API names.](/docs/foundry/functions/api-objects-links/)
4. Select **Next** to proceed.

![Name the link type](/docs/resources/foundry/object-link-types/create-link-api.png)

### Save location
在最后一步中,选择一个 project 以将此 link type 保存到其中。然后,**Submit**。完成这些步骤后,您的新 link type 将被创建,但尚未保存。

In the final step, choose a project to save this link type to. Then, **Submit**. After completing these steps, your new link type will be created, but not yet saved.

> 📷 **[图片: New link type Save location step.]**

> 📷 **[图片: New link type Save location step.]**

### Save change to ontology
返回到 Ontology Manager,选择右上角的 **Save** 以 [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/)。

Back in Ontology Manager, select **Save** in the upper right corner to [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/).
## Object-backed links
Object-backed link types 在多对一 cardinality link types 的基础上进行了扩展,作为 link type 存储解决方案为 object types 提供了一流的支持。Object-backed link types 允许在 link 上包含额外的元数据,并支持 restricted views。

Object-backed link types expand on many-to-one cardinality link types, providing first class support for object types as a link type storage solution. Object-backed link types allow for the inclusion of additional metadata on the link and support restricted views.
对于 object-backed link，除了 `Aircraft` 和 `Flight` 对象外，还需要为 `Flight Manifest` 假设一个额外的 object type。使用 object-backed link，您可以拥有一个 `Flight Manifest` object type，用于链接 `Aircraft` 和 `Flight` 对象。与 foreign key 或 data-set backed link 不同，这个 `Flight Manifest` 对象可以包含其他 properties，例如 `Pilot` 和 `First Mate`，以提供有关该 link 的其他元数据。

For object-backed links, in addition to the `Aircraft` and `Flight` objects, assume an additional object type for the `Flight Manifest`. With an object-backed link, you can have the `Flight Manifest` object type that links the `Aircraft` and `Flight` objects. Unlike a foreign key or data-set backed link, this `Flight Manifest` object can contain additional properties such as `Pilot` and `First Mate` to provide additional metadata on the link.
![Object-backed link overview.](/docs/resources/foundry/object-link-types/oblt_overview.png)
### Prerequisites for creating an object-backed link type
在创建 object-backed link type 之前，您必须首先完成以下操作：

Before you can create an object-backed link type, you must first do the following:
1. 在 link type 两侧创建 object types。有关更多详细信息，请参阅 [create an object type](/docs/foundry/object-link-types/create-object-type/)。

2. 创建将两个 object types 链接在一起的 backing object type。

3. 在 link type 的每一侧与 backing object type 之间创建多对一的 link types。有关更多详细信息，请参阅 [configure a new link type](#configure-a-new-link-type)。

1. Create the object types on either side of the link type. See [create an object type](/docs/foundry/object-link-types/create-object-type/) for additional details.
2. Create the backing object type that links the two object types together.
3. Create the many-to-one link types between each side of the link type to the backing object type. See [configure a new link type](#configure-a-new-link-type) for additional details.
对于上面的 `Aircraft`、`Flight` 和 `Flight Manifest` 示例，您需要创建以下资源：

For the `Aircraft`, `Flight`, and `Flight Manifest` example from above, you need to create the following resources:
1. 在 link type 两侧创建 object types。

1. `Aircraft` object type
2. `Flight` object type
2. 创建将两个 object types 链接在一起的 backing object type。

1. `Flight Manifest` object type
3. 在 link type 的每一侧与 backing object type 之间创建多对一的 link type。

1. `Aircraft` object type 和 `Flight Manifest` object type 之间的 link

2. `Flight` object type 和 `Flight Manifest` object type 之间的 link

1. Create the object types on either side of the link type.
1. `Aircraft` object type
2. `Flight` object type
2. Create the backing object type that links the two object types together.
1. `Flight Manifest` object type
3. Create the many-to-one link type between each side of the link type to the backing object type.
1. Link between the `Aircraft` object type and the `Flight Manifest` object type
2. Link between the `Flight` object type and the `Flight Manifest` object type
创建完这些资源后，您就可以创建 object-backed link type 了。

Once these have been created, you can create the object-backed link type.
### Convert existing links to object-backed link types
现有的 links 可以转换为 object-backed link types。在修改现有 links 之前，必须满足 object-backed link types 的 [prerequisites](#prerequisites-for-creating-an-object-backed-link-type)。

Existing links can be converted to object-backed link types. Before modifying existing links, the [prerequisites](#prerequisites-for-creating-an-object-backed-link-type) for object-backed link types must be fulfilled.
要修改现有 link 的 link type：

To modify the link type of an existing link:
1. 在 Ontology Manager 中打开该 link。

2. 在 **Configuration** 部分中，更新 join method 并选择 **Object type**。

3. 在 **Update link type to object-backed link type** 对话框中选择 backing object type。

4. 在 **Update link type to object-backed link type** 对话框中，从 link edges 到 backing object 选择 link type。

5. 选择 **Update to object-backed**。

1. Open the link in Ontology Manager.
2. In the **Configuration** section, update the join method and select **Object type**.
3. Select the backing object type in the **Update link type to object-backed link type** dialog.
4. Select the link type from the link edges to the backing object in the **Update link type to object-backed link type** dialog.
5. Select the **Update to object-backed**.
### Use object-backed link types
目前，object-backed link types 可以在 Object Explorer、Vertex 和 Workshop 中查看。选择一个 link 以查看该 link 的 backing object properties。请注意，在 Vertex 中，link 标题将显示该 link 的 backing object 标题。

Currently, object-backed link types can be viewed in Object Explorer, Vertex, and Workshop. Select a link to view the link's backing object properties. Note that in Vertex, the link title will display the link's backing object title instead.
## Troubleshooting
### Error: `Phonograph2:DatasetAndBranchAlreadyRegistered`
如果您收到错误 `Phonograph2:DatasetAndBranchAlreadyRegistered`，则您尝试保存的 link type 所对应的 backing datasource 已经在 Ontology 中 backing 另一个不同的 link type，无法再次使用。

If you receive the error `Phonograph2:DatasetAndBranchAlreadyRegistered`, the datasource backing the link type you are trying to save is already backing a different link type in the Ontology and cannot be used again.