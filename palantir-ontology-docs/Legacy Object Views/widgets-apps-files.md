<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/widgets-apps-files/
---
# Apps and Files
**Apps and Files widgets** enable embedding, displaying, and linking other Foundry apps within the current Object View. These Embedded Widgets can support assets built in other apps, such as [Quiver](/docs/foundry/quiver/overview/) or [Slate](/docs/foundry/slate/overview/). Additionally, they enable the Object View to display media, upload files, add hyperlinks or allow comments and conversations on that object.
If you are interested in building a more sophisticated object view, consider creating a [Workshop-backed tab](/docs/foundry/object-views/config-object-views/).
以下是一些小部件并非 object-aware。这意味着与 Object View 中其他小部件的交互会受到限制。

\* 示例 1：使用 Comments Widget 时，评论仅保存在该特定的 Object View 内，不会写回实际的 object。如果这些评论在特定 object 之外也可能有用，请考虑使用 Actions 来捕获它们。

\* 示例 2：使用 "Linked Files" 添加的文件会保存在 Foundry 中，但不会链接到 object。如果您希望这些文件可被重复使用，请考虑使用 [Actions attachments](/docs/foundry/action-types/upload-attachments/)。

\* 示例 3：嵌入 Slate 或 Contour 确实允许您传递参数，但它不发布或消费 filters，也无法与其他小部件（例如 Charts Widget）进行 cross-filtering。

Some of the widgets below are not object-aware. This means interaction with other widgets in the Object View is limited.
\* Example 1: Using the Comments Widget is only saved within that specific Object View, and does not write back to the actual object. If these comments might be useful outside the context of the specific object, consider using Actions to capture them.
\* Example 2: Adding files using “Linked Files” is saved in Foundry, but it’s not linked to the object. If you wish to have these files re-usable, consider using [Actions attachments](/docs/foundry/action-types/upload-attachments/).
\* Example 3: Embedding Slate or Contour does allow you to pass parameters, but it doesn’t publish or consume filters and doesn’t allow cross-filtering with other widgets such as the Charts Widget.
## Quiver Dashboard
有关如何将 Quiver dashboard 嵌入 Object View 中的详细步骤，请参阅 [Quiver dashboards documentation](/docs/foundry/quiver/dashboards-object-view/)。

For detailed steps on how to embed a Quiver dashboard in an Object View, see the [Quiver dashboards documentation](/docs/foundry/quiver/dashboards-object-view/).
## Slate Application
此 widget 在 object view 中显示一个 [Slate application](/docs/foundry/slate/overview/)，并支持两个应用程序之间的状态共享和交互。从 object view 到 Slate application，当前 object context 和 active filter state 可被使用。从 Slate application 到 object view，Slate 内提供了一组 events，这些 events 映射到 Object Explorer 中的行为，例如打开新的 Object 或 Exploration 选项卡以及更新 object view 过滤器。

This widget displays a [Slate application](/docs/foundry/slate/overview/) within an object view and supports state sharing and interactivity between the two applications. From the object view to the Slate application, the current object context and the active filter state are made available. From the Slate application to the object view, a set of events are provided within Slate which map to behaviors within Object Explorer, such as opening new Object or Exploration tabs and updating the object view filters.
### Configuration
**Slate Resource**
选择一个 Slate resource 进行显示。确保所有有权查看该 object 的用户也可以查看该应用程序。

**Slate Resource**
Chose a Slate resource to display. Ensure that all users with permission to view the object can also view the application.
Slate resource 采用"responsive"设计将获得最佳效果，因为应用程序将根据 object view 布局和可用屏幕尺寸调整大小。

A "responsive" design for the Slate resources will give the best results as the application will resize based on the object view layout and the available screen dimensions.
**Default Parameters**
默认情况下，当前 object 的 ID 及其 object type 会被传递到 Slate dashboard，并可以映射到 variables。这些可以关闭或更改其目标 variable。默认的 variable 名称为 `objectId` 和 `objectTypeId`。在 Slate application 中，确保在 Variable 选项卡中手动创建匹配的 Variables。

**Default Parameters**
By default the IDs of the current object and its object type are passed to the Slate dashboard and can be mapped to variables. These can be toggled off or have their target variables changed. The default variable names are `objectId` and `objectTypeId`. In the Slate application, ensure that the matching Variables are manually created in the Variable tab.
**Custom Parameters**
使用其他 custom parameters 将 property values 或 static、pre-defined values 传递到 Slate application。在 Slate application 中创建一个匹配的 Variable 来捕获这些 parameters 并在应用程序中使用它们。

**Custom Parameters**
Use additional custom parameters to pass either property values or static, pre-defined values into the Slate application. Create a matching Variable in the Slate application to capture these parameters and use them in the application.
### Using Parameters in Slate
配置的 parameters 会在 Slate application 加载时传递到其中。在配置 Slate application 时，每个 parameter 必须在 Variable 面板中创建一个对应的 Variable。[Learn more about how to use variables.](/docs/foundry/slate/concepts-variables/) 若要检查从 Object Explorer 传递到 Slate 的 parameters 的 keys 和 values，您可以从 object view editor 中的调试工具栏中选择"View parameters"。

The configured parameters are passed into the Slate application when it loads. When configuring your Slate application, each parameter must have a corresponding Variable created in the Variable panel. [Learn more about how to use variables.](/docs/foundry/slate/concepts-variables/) To check the keys and values of the parameters being passed from Object Explorer to Slate, you can select “View parameters” from the debugging toolbar within the object view editor.
### Accessing object view filters
object view 过滤器以 IObjectSetFilter 格式共享，以便与 Slate 中可用的 Object Set APIs 一起轻松使用。它们在更改时通过跨框架的 `postMessage` 自动发送到 Slate，也可以使用从 Slate 发送到 Object Explorer 的 event 手动请求。当您的 Slate dashboard 首次准备好接收这些过滤器时，可以使用此 request event 来触发过滤器的发送。

The object view filters are shared in the IObjectSetFilter format for easy use with the Object Set APIs available within Slate. They are automatically sent to Slate using a cross-frame `postMessage` when they change and can also be requested manually using an event sent from Slate to Object Explorer. This request event can be used to trigger sending the filters when your Slate dashboard is first ready to receive them.
要在 Slate 中捕获这些过滤器，您应配置一个 `slate.getMessage` event handler，该 handler 接收 post message payload，将其解析为 JSON，然后将结果设置到 variable 中。[Learn more about events.](/docs/foundry/slate/concepts-events/) 以下内容应足以将过滤器捕获到 variable 中：

To capture the filters within Slate you should configure a `slate.getMessage` event handler which takes the post message payload, parses it as JSON and then sets the result in a variable. [Learn more about events.](/docs/foundry/slate/concepts-events/) The following should be enough to capture the filters in a variable:
```js
const payload = {{slEventValue}}["payload"]
return JSON.parse(payload);
```
过滤器可以以两种格式使用。一种格式包含所有不包含其可能基于的 origin object type 的过滤器，另一种格式包含按 object type 分组的过滤器以及一个针对不基于特定 object type 的过滤器的单独列表。

There are two formats that the filters can be consumed in. One format contains all filters without the origin object type they may be based on, the other format contains the filters grouped by object type as well as a separate list for filters which are not based on a specific object type.
所有过滤器的 payload 具有以下形式：

The payload for all filters has the following shape:
```json
{
"type": "HUBBLE_SLATE_WIDGET // ACTIVE_FILTERS_UPDATED",
"payload": <IObjectSetFilter[]>
}
```
按 object type 分组的过滤器的 payload 具有以下形式：

The payload for filters grouped by object type has the following shape:
```json
{
"type": "HUBBLE_SLATE_WIDGET // ACTIVE_FILTERS_BY_OBJECT_TYPE_ID_UPDATED",
"payload": {
"filtersByObjectType": {
[objectTypeId]: <IObjectSetFilter[]>
},
"globalFilters": <IObjectSetFilter[]>
}
}
```
### Triggering events from Slate
Slate 可用于在 Object Explorer 中触发 events 的 event types 包括：

Event types available for Slate to trigger events within Object Explorer include:
* 在 Object Explorer 中打开一个新的 object 选项卡（使用 object RID）

* 在 Object Explorer 中打开一个新的 object 选项卡（使用 object primary key）

* 在 Object Explorer 中为给定的 object set 打开一个新的 exploration 选项卡

* 将 object set filters 发布到 object view

* 清除 object view 上的 object set filters

* 刷新当前 object view 上的数据

* 请求将 object view filters 重新发送到 Slate

* Open a new object tab in Object Explorer (using object RID)
* Open a new object tab in Object Explorer (using object primary key)
* Open a new exploration tab in Object Explorer for a given object set
* Publish object set filters to the object view
* Clear object set filters on the object view
* Refresh the data on the current object view
* Request resending the object view filters to Slate
使用 `slate.sendMessage` action 触发这些 events。通过此 action，从 custom logic 返回 event message object。[Learn more about events.](/docs/foundry/slate/concepts-events/) 每个 event 的预期格式如下所列。有关调试 event 集成的帮助，请使用 object view editor 的调试工具栏。当捕获到 post message 但 event payload 在某些方面不正确时，它将显示一条警告。

Trigger these events using the `slate.sendMessage` action. From this action, return the event message object from the custom logic. [Learn more about events.](/docs/foundry/slate/concepts-events/) The expected format for each event is listed below. For help debugging your event integrations, use the object view editor’s debugging toolbar. This will show a warning when a post message is captured but the event payload is incorrect in some way.
**在 Object Explorer 中打开一个新的对象标签页（使用 object RID）**

此事件主要依赖 `objectRid` 参数，但也可以选择性地传入 `tabId`，以便在特定的标签页上打开对象视图。

**Open a new object tab in Object Explorer (using object RID)**
This event primarily relies on the `objectRid` parameter but can optionally take a `tabId` if the object view should be opened on a specific tab.
```json
{
"type": "HUBBLE_SLATE_WIDGET // OPEN_OBJECT_BY_RID",
"payload": {
"objectRid": "...",
},
}
```
**在 Object Explorer 中打开一个新的对象标签页（使用对象主键）**

如果不知道 object RID，也可以使用对象的主键属性及其 object type ID 来加载对象视图。

**Open a new object tab in Object Explorer (using object primary key)**
If the object RID is not known then the object view can also be loaded using the object’s primary key properties along with its object type ID.
```json
{
"type": "HUBBLE_SLATE_WIDGET // OPEN_OBJECT_BY_PRIMARY_KEY",
"payload": {
"objectTypeId": "...",
"primaryKey": {
...
},
},
}
```
**在 Object Explorer 中为给定的 object set 打开一个新的 exploration 标签页**

通过提供一个 Object Set，可以打开一个新的 search/exploration 标签页。这些 object sets 的复杂度应保持有限，以避免在 exploration UI 中表示时出现问题。

**Open a new exploration tab in Object Explorer for a given object set**
A new search/exploration tab can be opened by providing an Object Set. These object sets should be of limited complexity in order to avoid issues with representing them within the exploration UI.
```json
{
"type": "HUBBLE_SLATE_WIDGET // OPEN_NEW_SEARCH_FOR_OBJECT_SET",
"payload": {
"objectSet": {
...
}
},
}
```
**将 object set filters 发布到 object view**

许多 object view widgets 可以发布影响视图中其他 widgets 的 filters。Slate widget 可以通过使用此事件发送要发布的 filters 来实现此操作。最近发布的 filters 将替换同一 Slate widget 之前发布的任何 filters，因此这些 filters 的状态应在 Slate 内部进行管理。Filters 应作为 Object Set Filters 进行过滤，这与 Object Set Service APIs 请求所使用的格式相同。可以为特定的 object types（`filtersByObjectType`）或全局 properties（`globalFilters`）提供 filters。

**Publish object set filters to the object view**
Many object view widgets can publish filters which effect other widgets in the view. The Slate widget can do this by sending the filters to be published using this event. The latest published filters will replace any filters previously published by the same Slate widget so the state of these filters should be managed internally within Slate. The filters should be filtered as Object Set Filters, the same format used with requests to the Object Set Service APIs. Filters can be provided for specific object types (`filtersByObjectType`) or for global properties (`globalFilters`).
```json
{
"type": "HUBBLE_SLATE_WIDGET // PUBLISH_OBJECT_SET_FILTER",
"payload": {
"filtersByObjectType": {
...
},
"globalFilters": {
...
}
},
}
```
**清除 object view 上的 object set filters**

可以使用此事件快速清除 object view 上已发布的 filters。它不需要 payload。

**Clear object set filters on the object view**
The published filters present on the object view can be quickly cleared using this event. It requires no payload.
```json
{
"type": "HUBBLE_SLATE_WIDGET // CLEAR_PUBLISHED_FILTERS"
}
```
**刷新当前 object view 上的数据**

如果对 object view 中显示的数据应用了更新，则可能需要触发数据刷新。可以使用此事件来执行此操作。它不需要 payload。

**Refresh the data on the current object view**
If updates have been applied to the data present within the object view it may be required to trigger a refresh of the data. This event can be used to do so. It requires no payload.
```json
{
"type": "HUBBLE_SLATE_WIDGET // REFRESH_OBJECT_VIEW"
}
```
**请求将 object view filters 重新发送到 Slate**

如上文 "Accessing object view filters" 部分所述，由其他 widgets 发布的 object view filters 通过 post message 发送到 Slate。当 Slate dashboard 已初始化并准备好处理这些 filters 时，应触发此事件来请求它们。Hubble 将发送一个单独的事件，其中包含这些 filters。您可以请求两种类型的 filters，一种格式包含所有 filters（无论其来源 object type），另一种包含按来源 object type 分组的 filters。这些请求不需要 payload。

**Request resending the object view filters to Slate**
As described above in the “Accessing object view filters” section, the filters present on the object view published by other widgets are sent to Slate using a post message. When the Slate dashboard has initialized and is ready to handle the filters is should fire this event to request them. A separate event will be sent from Hubble containing the filters. There are two types of filters you can request, one format contains all filters regardless of their origin object type, the other contains the filters grouped by their origin object type. These requests require no payload.
对于发送所有 filters：

For all filters send:
```json
{
"type": "HUBBLE_SLATE_WIDGET // REQUEST_ACTIVE_FILTERS"
}
```
对于发送按 object type 分组的 filters：

For filters grouped by object type send:
```json
{
"type": "HUBBLE_SLATE_WIDGET // REQUEST_ACTIVE_FILTERS_BY_OBJECT_TYPE"
}
```
## Media Preview
此 widget 在给定 attachment property 或某种类型媒体（图像、PDF 等）的 URL property 的情况下，显示单个大型内联媒体文件预览。

This widget shows a single large inline preview of a media file, given an attachment property or a property that is a URL of some type of media (image, PDF, etc.).
![media preview](/docs/resources/foundry/object-views/widgets_hu-media-preview.png)
### Configuration
要使用 Media Preview widget，您需要将当前视图中配置的对象设置为包含 attachment property。Attachment properties 将相关媒体存储在 Foundry 中，并通过继承其所属对象的权限来确保媒体的正确权限分配。请参阅 [此页面](/docs/foundry/action-types/upload-attachments/) 了解如何向 attachment property 添加媒体。

To use the Media Preview widget, you will need to configure the current object in view to include an attachment property. Attachment properties store the relevant media within Foundry and ensure that the media is correctly permissioned by inheriting the permissions from the object they have been added to. See [this page](/docs/foundry/action-types/upload-attachments/) to learn how to add media to your attachment property.
或者，Media Preview widget 也可以使用存储在 property 中的 URL 来显示 Foundry 上的现有媒体。查看对象视图的用户将需要同时具有该对象和媒体存储位置的访问权限。要将媒体添加到您的对象视图中，请按照以下步骤操作：

Alternatively, the Media Preview widget can also be used to display existing media on Foundry using URLs stored in a property. Users viewing the object view will require access to both the object and the location the media is stored. To add media to your object views, follow these steps:
1. **将媒体上传到 Foundry：** Datasets 可以用作存储任意文件集合的方式。要创建这样的 dataset，可以首先将文件上传到一个文件夹，然后在出现的弹出窗口中选择 **Bundle all files as a single dataset**。如果您只上传单个文件，此选项将显示为 **Upload to a dataset without a schema**。

1. **Upload media to Foundry:** Datasets can be used as a way to store a collection of arbitrary files. To create such a dataset, you can begin by uploading the files to a folder and, in the pop-up that appears, selecting **Bundle all files as a single dataset**. If you're only uploading a single file, this option will appear as **Upload to a dataset without a schema**.
![upload files as dataset](/docs/resources/foundry/object-views/widgets_hu-upload-files.png)
创建此 dataset 后，您可以根据需要添加其他文件。为此，请点击 dataset 预览右上角的 **Import**。

Once this dataset has been created, you can add additional files as needed. To do so, click **Import** on the top right of the dataset preview.
![import additional files](/docs/resources/foundry/object-views/widgets_hu-import-additional-files.png)
在出现的对话框中，选择要上传的其他文件。

In the dialog that appears, select additional files to upload.
![upload additional files](/docs/resources/foundry/object-views/widgets_hu-upload-additional-files.png)
2. **添加 URL 列：** 在当前 Object 的 backing dataset 中，添加一个新列，其中包含每行对应媒体文件的 URL。该 URL 应采用以下格式：`https://{my-foundry-url}/foundry-data-proxy/api/web/dataproxy/datasets/{dataset rid}/transactions/{transaction rid}/{filename}` 或 `https://{my-foundry-url}/foundry-data-proxy/api/web/dataproxy/datasets/{dataset rid}/views/{branch name}/{filename}`

* 示例：`https://{my-foundry-url}/foundry-data-proxy/api/web/dataproxy/datasets/ri.foundry.main.dataset.39ce332b-1d74-40ca-be35-5a5b48459a9a/transactions/ri.foundry.main.transaction.00000000-0000-30d2-8067-4b5d9c819f4c/sample-doc.pdf`

* 注意：如果您使用的是 PDF，URL 应以 `/foundry-data-proxy/api/dataproxy` 开头，**而不是** `/foundry-data-proxy/api/web/dataproxy`

3. **在 Ontology 中将该列标记为 `hubble:media_url`：** 在 Ontology 中为该列创建一个 Property，并为其分配一个 Typeclass，kind = `hubble`，name = `media_url`。

* 其他媒体 Typeclass：其他可选项包括 `hubble:icon` 和 `hubble:thumbnail`。它们将分别使用此 URL 作为 Object 的 icon 或搜索结果卡片中的 thumbnail。

4. **在 Object Explorer 中向 Object View 添加媒体 widget：** 目前有两种内置的媒体 widget：*Media Preview* 和 *Media Thumbnails*。如果您编辑 Object View 并点击 **Add Section**，可以看到每种 section 的描述。该 widget 需要设置 **Media Property**，即包含您希望预览的媒体 URL 的 Property。

2. **Add a URL column:** In the backing dataset of the current object in view, add a new column that contains the URL of the media file for each corresponding row. The URL should be of the format: `https://{my-foundry-url}/foundry-data-proxy/api/web/dataproxy/datasets/{dataset rid}/transactions/{transaction rid}/{filename}` OR `https://{my-foundry-url}/foundry-data-proxy/api/web/dataproxy/datasets/{dataset rid}/views/{branch name}/{filename}`
* Example: `https://{my-foundry-url}/foundry-data-proxy/api/web/dataproxy/datasets/ri.foundry.main.dataset.39ce332b-1d74-40ca-be35-5a5b48459a9a/transactions/ri.foundry.main.transaction.00000000-0000-30d2-8067-4b5d9c819f4c/sample-doc.pdf`
* Note: If you are using PDFs, the URL should start with `/foundry-data-proxy/api/dataproxy` and NOT `/foundry-data-proxy/api/web/dataproxy`
3. **Mark the column as a `hubble:media_url` in the Ontology:** Create a property for the column in the Ontology, and give it a Typeclass with kind = `hubble` and name = `media_url`.
* Other Media Typeclasses: Other possibilities are `hubble:icon` and `hubble:thumbnail`. These will use this URL as the icon for an object or as a thumbnail in the search results cards, respectively.
4. **Add a media widget to the object view in Object Explorer:** There are currently two types of built-in media widgets: *Media Preview* and *Media Thumbnails*. If you edit your object view and click **Add Section** you can see a description for each type of section. The widget requires set-up of the **Media Property**, the property containing the URL for the media you wish to preview.
其他可配置参数：

Other parameters to configure:
* Title（必填）：显示在 widget 标题上的标题。

* Icon（必填）：显示在 widget 标题上的图标。

* Help Info：在 tooltip 中显示额外的帮助信息。

* Height：用于渲染媒体 widget 的高度（以像素为单位）。

* Title (required): The title to be displayed on the widget header.
* Icon (required): The header to be displayed on the widget header.
* Help Info: Display additional help information in a tooltip.
* Height: Height (in pixels) to render the media widget.
## Hyperlink
Hyperlinks widget 创建一个按钮，用作指向网页的简单链接。您可以向 Object View 添加任意数量的链接，每个链接可以是静态的（即对所有 Object 实例使用相同的链接）或是按 Object 动态生成的链接。

The Hyperlinks widget creates a button that works as a simple link to a webpage. You can add any number of links to an object view and each can be either static (that is, the same link for all objects instances) or dynamic per-object link.
![Hyperlink.png](/docs/resources/foundry/object-views/widgets_hyperlink.png)
### Configuration
1. *Open Link In* - 选择是在浏览器同一标签页中打开（默认）、新标签页中打开，还是在弹出窗口中打开。弹出窗口可靠性较低；根据浏览器和已安装的扩展程序，可能会引发问题或被阻止。此设置将应用于所有 Object。

2. *Link Intent* - 5 种链接 "intent"，用于确定链接按钮的颜色。[Blueprint Intent ↗](https://blueprintjs.com/docs/#core/components/button.css) CSS class 应用于按钮（默认无）：

1. "None" - 灰色

2. "Primary" - 蓝色

3. "Success" - 绿色

4. "Warning" - 橙色

5. "Danger" - 红色

3. *URL Type* - 3 种 URL 配置类型：

1. Property - 包含 URL 的动态 Property，用作超链接目标。

1. 配置方法：(1) 选择 Object Type（通常为当前查看的 Object）；(2) 选择链接应取自的 Property 列。有一个切换选项可在值为 null 时隐藏超链接按钮。

2. 例如，您可以拥有 2 个 "Website" Object，两者都在您的 ontology 中定义了 `site_URL` 字段，其中 Object 1 的 `site_URL` 设置为 `https://palantir.com`，Object 2 的 `site_URL` 设置为 `https://palantir.com/uk`。

2. Hardcoded - 对所有 Object 显示的静态 URL。只需复制粘贴该 URL，并确保其以 `https://` 开头。

3. Templated - Templated URL 允许您根据 Object 的 Property 自定义链接。您可以通过用单花括号 `{ }` 包裹的方式在 URL 中引入任何 Property。

1. 例如，如果您有一个保存为 Property `report_rid` 的 report RID，您可以使用 URL 模板 `/workspace/report/{report_rid}` 创建一个按钮，以打开与每个 Object 关联的 report。

4. *Link Title* - 显示在超链接按钮上的文本标签。所有 Object 均显示相同的内容。

1. *Open Link In* - select whether to open on the same tab at the browser (default) on a different tab or in a pop-up window. Pop-ups are less reliable; may cause issues/get blocked depending on browser/installed extensions. This would apply across all objects
2. *Link Intent* - 5 link “intents” to determine the color of the link button. [Blueprint Intent ↗](https://blueprintjs.com/docs/#core/components/button.css) CSS class applied to the button (default is none):
1. “None” - grey
2. “Primary“ - blue
3. “Success” - green
4. “Warning” - orange
5. “Danger” - red
3. *URL Type* - 3 types of URL configurations:
1. Property - a dynamic property containing a URL to use as your hyperlink destination.
1. To configure: (1) select the object type (usually the object currently in view); (2) select the property column that the link should be taken from. There is a toggle option to hide the hyperlink button if the value is null.
2. For example, you could have 2 "Website" objects, both with the field `site_URL` defined in your ontology, where object 1 has the `site_URL` set to `https://palantir.com` and object 2 has the `site_URL` set to `https://palantir.com/uk`.
2. Hardcoded - a static URL to appear across all objects. Just copy-paste the url, and make sure it has `https://`
3. Templated - Templated URL allows you to customize the link based on a property of the object. You can bring any property in the URL by encapsulating between single curly brackets `{ }`.
1. For example, if you have a report RID saved as a property `report_rid`, you could have a button to open the report associated with each object by using the URL template `/workspace/report/{report_rid}`.
4. *Link Title* - the text label displayed on the hyperlink button. This will be the same for all objects.
**常见问题及注意事项：**

**Common issues and notes:**
* 如果超链接已损坏，用户将被重定向至 Object Explorer 的着陆页。

* If the hyperlink is broken, the user will be re-directed to the landing page of Object Explorer.
## Linked Files
Linked Files widget 使用户能够将当前查看的 Object 链接到文件，可以通过 resource selector 浏览以选择 Foundry 中已有的文件，或从本地机器上传新文件至 Foundry。

The Linked Files widget enables users to link the object in view to a file, either by browsing with a resource selector to select a file already in Foundry, or by uploading a new file to Foundry from their local machine.
![Linked files](/docs/resources/foundry/object-views/widgets_hu-linked-compass-resources.png)
### Configuration
此 section 没有可自定义的选项。您仍可在 Format 选项卡下更改标题及其他常规格式。

This section has no customization options. You can still change the title and other general formatting under the Format tab.
**常见问题及注意事项：**

**Common issues and notes:**
* 通过此 widget 上传的文件不会作为 Ontology 的一部分进行 writeback，即它们不会作为 Property 保存在当前 Object 上。要实现此目的，请考虑使用带 writeback 的 Foundry Forms。

* 目前无法隐藏两个选项之一，因此它始终同时显示 "Upload files" 和 "Link new file"。

* 目前无法为文件上传设置默认目标位置，因此用户每次上传时都必须在 Foundry 中浏览选择目标位置。

* Files uploaded through this widget are not written-back as a part of the ontology, i.e. they are not saved as a property on the current object. In order to achieve that, consider using Foundry Forms with writeback instead.
* There’s currently no way to hide one of the two options, so it always shows both “Upload files” and “Link new file”.
* There’s currently no way to set up a default destination for file uploads, so the user has to browse for a destination location in Foundry every time they make an upload.
## Iframe
您可以在 Object View 中以 "网页中的网页" 形式嵌入 Slate dashboard 或其他 Foundry 应用程序的 inline frame。使用 iframe 可以将当前 Object 的值传递给 Slate 中的 filter variables 或 Contour 中的 parameters。

You can embed an inline frame of a Slate dashboard or other Foundry application in the Object View as a "webpage within a webpage". Using an iframe enables you to pass values from the current object to filter variables in Slate or parameters in Contour.
### Configuration
要嵌入 iframe，您需要使用以下所述的 Handlebar 语法将链接配置为正确的 Foundry 地址。

To embed an iframe, you need to configure the link to the correct Foundry address using Handlebar syntax as described below.
1. **必填：** 复制您希望嵌入的页面的完整链接，并删除 `/workspace/` 之前的所有文本。

* Report 示例：对于 `https://EXAMPLE.palantirfoundry.com/workspace/report/ri.report.main.report.ABCDEF-1234-5678`，您应保留 `/workspace/report/ri.report.main.report.ABCDEF-1234-5678`。

* Slate 示例：对于 `https://EXAMPLE.palantirfoundry.com/workspace/slate/documents/SLATE_DOCUMENT_NAME`，您应保留 `/workspace/slate/documents/SLATE_DOCUMENT_NAME`。

2. **必填：** 添加 `embedded=true` 以仅显示完整视图。如果 `embedded=true` 是唯一参数，则添加前缀 `/?`；如果 `embedded=true` 附加在其他参数之后，则使用 `&`。

* Report 示例：`/workspace/report/ri.report.main.report.ABCDEF-1234-5678/?embedded=true`

* Slate 示例：`/workspace/slate/documents/SLATE_DOCUMENT_NAME/latest?&embedded=true`

3. **可选：** 向 Slate 传递值以过滤特定的 variables/parameters。在 Object Explorer 中使用 Object Type ID、特定 Object ID 或特定 Property ID。使用 `&` 并在花括号内声明您希望注入到 Slate 中的值，例如 `{{propertyID}}`。此语法基于 Handlebar。

* Report 示例：`/workspace/report/ri.report.main.report.ABCDEF-1234-5678/?PARAMETER_NAME={{propertyID}}&embedded=true`

* Slate 示例：`/workspace/slate/documents/SLATE_DOCUMENT_NAME/latest?VARIABLE_NAME={{propertyID}}&embedded=true`

1. **Required:** Copy the full link to the page you wish to embed, and remove all text before `/workspace/`.
* Report example: For `https://EXAMPLE.palantirfoundry.com/workspace/report/ri.report.main.report.ABCDEF-1234-5678` , you should keep `/workspace/report/ri.report.main.report.ABCDEF-1234-5678`.
* Slate example: For `https://EXAMPLE.palantirfoundry.com/workspace/slate/documents/SLATE_DOCUMENT_NAME`, you should keep `/workspace/slate/documents/SLATE_DOCUMENT_NAME`.
2. **Required:** Add `embedded=true` to simply show the full view. Add a prefix of `/?` if `embedded=true` is the only statement, or `&` if `embedded=true` is attached to other statements.
* Report example: `/workspace/report/ri.report.main.report.ABCDEF-1234-5678/?embedded=true`
* Slate example: `/workspace/slate/documents/SLATE_DOCUMENT_NAME/latest?&embedded=true`
3. **Optional:** Pass values to Slate to filter for specific variables/parameters. Use the object type ID, a specific object ID, or a specific property ID in Object Explorer. Use `&` and state which values you wish to inject to Slate within curly brackets, like `{{propertyID}}`. This is based on Handlebar syntax.
* Report example: `/workspace/report/ri.report.main.report.ABCDEF-1234-5678/?PARAMETER_NAME={{propertyID}}&embedded=true`
* Slate example: `/workspace/slate/documents/SLATE_DOCUMENT_NAME/latest?VARIABLE_NAME={{propertyID}}&embedded=true`
#### Other configurations
* 标准 iframe 与无 header iframe 之间的区别在于，无 header iframe 会隐藏 widget 的 header；widget header 通常包含一个 icon、一个标题，以及在配置中的 **Format** 选项卡下为 widget 添加标题的选项。

* iframe widget 允许您设置 widget 的高度。默认值为 500，需手动调整。

* 设置好 iframe 后，您将在 Object View 中的 widget 下方看到一个 helper 窗口（仅在编辑模式下显示）。该 helper 窗口包含 Object 特定的提示，并显示您可以传递给 Slate 和其他 Foundry 应用程序的 Properties 和 IDs。

* 通过向 URL 添加以下内容可隐藏 report header：`&__rp_headerBar=hidden`。

* 嵌入 Foundry 外部的外部网站在满足安全和策略要求的前提下可能可行。如果您认为您的用例有此需要，请联系您的 Palantir 代表。

* The difference between a standard iframe and a headerless iframe is that a headerless iframe hides the header of the widget; the widget header normally contains an icon, a title, and the option to add a title to the widget under the **Format** tab in the configuration.
* The iframe widget enables you to set the height of the widget. The default is 500, and it is adjusted manually.
* Once you set up the iframe, you will see a helper window underneath the widget in the object view (only displayed when in editing mode). The helper window includes object-specific hints and shows which properties and IDs you can pass on to Slate and other Foundry applications.
* Hiding the report header is possible by adding the following to the URL: `&__rp_headerBar=hidden`.
* Embedding external websites outside of Foundry may be possible subject to security and policy requirements. Contact your Palantir representative if you think this is necessary for your use case.
## Comments
此 widget 可为协作处理同一 Object 的用户启用本地对话框，并支持通过标记 `@user_name` 来提及其他用户。

This widget enables a local dialog box for users collaborating on an object, with the option to mention other users (by tagging `@user_name`).
这些评论不会被捕获到 Object 本身，也不会在 Foundry 全平台支持未来对该对话的搜索或复用。

These comments are not captured on the object itself and do not enable any future search or reuse of this conversation across Foundry.
### Configuration
此部分没有自定义选项。您仍可在 **Format（格式）** 选项卡下更改标题及其他常规格式设置。

This section has no customization options. You can still change the title and other general formatting under the **Format** tab.
### Comment behavior when the source dataset changes
如果 Object Type 的源数据集发生更改，则相应的评论 Feed 将会消失。

If the source dataset for an object type is changed, the corresponding comment feed will disappear.
### Writeback for comments
通过此 widget 添加的评论不会作为 Ontology 的一部分回写；也就是说，这些评论不会保存为当前 Object 的 Property。如果您的评论使用场景包括搜索、分析或从评论中学习，请考虑使用 Actions。

Comments added through this widget are not written back as part of the Ontology; that is, these comments are not saved as a property on the current object. If your commenting use case includes search, analysis, or learning from comments, consider using Actions.