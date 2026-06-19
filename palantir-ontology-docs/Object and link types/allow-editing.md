<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/allow-editing/
---
# Allow users to edit objects and links
## Editing data from Foundry object applications
您可以允许 user applications（如 Workshop 和 Object Views）中的用户编辑 property 值、添加和删除 links，以及创建和删除 objects。您还可以根据用户所做的编辑配置 side effects（例如通知）。

You can allow users in user applications (like Workshop and Object Views) to edit property values, add and remove links, and create and delete objects. You can also configure side effects (like notifications) based on edits made by users.
配置此功能的支持方式是在 Ontology Manager 中创建和配置 action types。[了解有关如何设置 action types 的更多信息。](/docs/foundry/action-types/overview/)

The supported way to configure this functionality is to create and configure action types in the Ontology Manager. [Learn more about how to set up action types.](/docs/foundry/action-types/overview/)
本文档的其余部分涵盖了用户在执行 actions 之前需要在 object types 和 link types 上配置的内容。

The remainder of this documentation covers what needs to be configured on object types and link types before users can take actions.
## Editing data from external applications
[Objects API](/docs/foundry/api/ontology-resources/actions/apply-action/) 提供端点，供外部客户端在完全权限强制执行的情况下写入和更新 objects、properties 和 links。

The [Objects API](/docs/foundry/api/ontology-resources/actions/apply-action/) provides endpoints for external clients to write and update objects, properties, and links with full permissions enforcement.
## Set up the prerequisites
为了让用户能够执行 action type 配置中定义的 action，必须创建一个 writeback dataset。writeback dataset 在构建时会读取用户所做的编辑，并反映任何给定 object 的最新状态。

In order for a user to be able to take an action defined in an action type configuration, a writeback dataset must be created. The writeback dataset will read the edits made by users when it is built and will reflect the most up-to-date state of any given object.
> **ℹ️ 注意**

> 请注意，编辑内容会写入 writeback dataset，而不是 object type 或 link type 背后的 dataset。这确保了用户在分析中可以同时访问原始数据和编辑后的数据。
> **ℹ️ 注意**

> Note that edits are written to the writeback dataset and not the dataset backing an object type or link type. This ensures that users have access to both the original data and the edited data in their analyses.
要设置 writeback dataset：

To set up a writeback dataset:
1. 导航到要启用编辑功能的 object type 或 link type 的 **Datasources** 页面。

2. 在页面的 **Writeback dataset** 部分选择 **Generate** 以创建新的 writeback dataset。将打开一个对话框，要求您选择一个要放置该 dataset 的 Project。选择一个位置。

3. 确保您希望能够编辑该 object type 或 link type 的用户对 writeback dataset 具有编辑权限。

4. 确保您希望能够查看对 object type 或 link type 所做更改的用户对 writeback dataset 具有查看权限。

* 查看 objects 和 links 的能力由 object type 和 link type 的 backing datasources 控制。

* 查看 objects 和 links 编辑内容的能力由 writeback dataset 的权限控制。

* 如果用户仅具有前者的访问权限，他们只能看到未应用编辑的 object 状态。如果用户具有后者的访问权限，他们可以同时查看编辑内容以及 object 的当前状态。

1. Navigate to the **Datasources** page of the object type or link type you want to enable edits on.
2. Select **Generate** in the **Writeback dataset** portion of the page to create a new writeback dataset. A dialog will open asking you to choose a Project where you’d like to place the dataset. Select a location.
3. Make sure the users who you want to be able to edit the object type or link type have edit permissions on the writeback dataset.
4. Ensure that the users who you want to be able to view changes made to the object type or link type have view permissions on the writeback dataset.
* The ability to view objects and links is controlled by an object type and link type’s backing datasources.
* The ability to view the edits on objects and links is controlled by the permissions on the writeback dataset.
* If users have access to only the former, they can see only the object as it exists without edits applied. If users have access to the latter, they can see both the edits and the object as it exists at present.
> **ℹ️ 注意**

> 如果您希望 object type 中的某个 property 捕获最终用户手动输入的数据（通过 Action 或其他 writeback 方法），并且该数据在 Foundry 中尚不存在，则需要向该 object type 的 backing dataset 添加一个空列，并将其映射到 object type 中的新 property。您还需要启用编辑功能；这可以通过在 Object Storage V1 中创建 writeback dataset 或在 Object Storage V2 中切换启用编辑功能来完成。
> **ℹ️ 注意**

> If you want a property in your object type to capture manually-entered data from an end user (via an Action or other writeback method) and this data does not yet exist in Foundry, you will need to add an empty column to the object type’s backing dataset and map it to a new property in your object type. You also need to enable edits; this is done by creating a writeback dataset in Object Storage V1 or by toggling on edits in Object Storage V2.