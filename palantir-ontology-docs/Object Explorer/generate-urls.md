<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/generate-urls/
---
# Generate Object Explorer URLs
在开发 object view 的过程中，或者将 object view 集成到 Slate 应用程序或外部系统时，你可能需要生成链接到特定 object 的 URL 或搜索 object。

In the course of developing object views, or when integrating object views into Slate applications or external systems, you may need to generate URLs that link to a specific object or search for objects.
要了解如何创建链接到特定 Object View 的 URL，请参阅 Object Views 文档中的 [Generating Object Views URLs](/docs/foundry/object-views/generate-urls/)。

To learn about how to create a URL linking to a specific Object View, see [Generating Object Views URLs](/docs/foundry/object-views/generate-urls/) in the Object Views documentation.
## Generating a keyword-only search
如果你的文本包含特殊字符或空格，则需要对其进行编码：

If your text contains special character or spaces, you will need to encode it:
`encodeURIComponent("hello world");`
`encodeURIComponent("hello world");`
Create a URL:
`<BASEURL>/hubble/external/keyword/v0/<MY_ENCODED_TEXT>`
`<BASEURL>/hubble/external/keyword/v0/<MY_ENCODED_TEXT>`
## Linking to explorations
Object Explorer 可以打开指向特定 object type、已保存的 explorations 或带有 URL 中描述的过滤器的新搜索的链接。每种类型的链接都可以在默认的 Explore 视图中打开，其中包含显示聚合结果的图表，也可以通过将参数 `perspectiveId=results` 附加到链接 URL 的末尾，在表格 Results 视图中打开。

Object Explorer can open links to specific object types, saved explorations, or new searches with filters described in the URL. Each type of link can be opened in the default Explore view, with charts showing aggregate results, or in the tabular Results view by appending the parameter `perspectiveId=results` to the end of the link URL.
**打开 object type 进行 exploration**

**Opening an object type For exploration**
可以使用 `objectTypeId` URL 参数打开特定 object type 的 explorations。例如：

Explorations for specific object types can be opened with the `objectTypeId` URL parameter. For example:
`/workspace/hubble/exploration?objectTypeId=aircraft`.
`/workspace/hubble/exploration?objectTypeId=aircraft`.
要在 Results 视图中打开，请附加 `perspectiveId=results` 参数：

To open in the Results view, append the `perspectiveId=results` parameter:
`/workspace/hubble/exploration?objectTypeId=aircraft&perspectiveId=results`
`/workspace/hubble/exploration?objectTypeId=aircraft&perspectiveId=results`
**加载已保存的 Exploration 或 Object Set**

**Loading a Saved Exploration or Object Set**
使用 `saved` 路由来打开已保存的 exploration 或 object set。

Use the `saved` route to open a saved exploration or object set.
`/workspace/hubble/exploration/saved/ri.object-set.main.versioned-object-set.4b117663-06d7-4bd1-a2be-8e1ba20998cb`
`/workspace/hubble/exploration/saved/ri.object-set.main.versioned-object-set.4b117663-06d7-4bd1-a2be-8e1ba20998cb`
要加载由另一个 Foundry 应用程序创建的 object set，请使用 `external/objectSet` 路由。

To load an object set created by another Foundry application, use the `external/objectSet` route.
`/workspace/hubble/external/objectSet/v0/ri.object-set.main.object-set.f6916120-5b52-4312-8be4-9f5764983907`
`/workspace/hubble/external/objectSet/v0/ri.object-set.main.object-set.f6916120-5b52-4312-8be4-9f5764983907`
## \[Advanced] Generating a complex search
生成您的 filter 集合，使其如下所示：

Generate your set of filters to look like:
```json
{
"keyword": "",
"objectTypes": [
"google-reviews"
],
"filters": [
{
"type": "propertyFilter",
"objectType": "google-reviews",
"propertyType": "Description",
"value": {
"type": "textFilter",
"text": "hello"
}
},
{
"type": "propertyFilter",
"objectType": "google-reviews",
"propertyType": "rating",
"value": {
"type": "valuesFilter",
"values": ["3", "4"]
}
},
{
"type": "propertyFilter",
"objectType": "google-reviews",
"propertyType": "creation-date",
"value": {
"type": "dateRangeFilter",
"dateRangeFilter": {
"start": "2000-01-10",
"end": "2000-01-11"
}
}
},
{
"type": "linkFilter",
"objectType": "google-reviews",
"linkType": "restaurant-to-review",
"value": {
"type": "presenceFilter",
"matchType": "MUST_HAVE"
}
}
]
}
```
还有更多可用的 filter 类型，包括：

There are more types of filters available, including:
* **numberRangeFilter:** `min`（可选 number），`max`（可选 number）

* **relativeDateFilter:** `sinceDaysAgo`（可选 number），`untilDaysAgo`（可选 number）

* **timestampRangeFilter:** `startMillis`（可选 number），`endMillis`（可选 number）

* **relativeTimestampFilter:** `sinceMillisAgo`（可选 number），`untilMillisAgo`（可选 number）

* **numberRangeFilter:** `min` (optional number), `max` (optional number)
* **relativeDateFilter:** `sinceDaysAgo` (optional number), `untilDaysAgo` (optional number)
* **timestampRangeFilter:** `startMillis` (optional number), `endMillis` (optional number)
* **relativeTimestampFilter:** `sinceMillisAgo` (optional number), `untilMillisAgo` (optional number)
> **ℹ️ 注意**

> 此示例可能已过时 – 请使用以下说明了解最新格式。
> **ℹ️ 注意**

> This example may be out of date – use the instructions below to find out the latest format.
value 的类型必须与 Object Explorer 中该 property 默认显示的 widget 类型相匹配。例如：用于直方图 widget 的 `valuesFilter`；用于文本框的 `textFilter`。

The type of the value must match the type of widget that shows by default for that property in Object Explorer. For example: `valuesFilter` for a histogram widget; `textFilter` for textbox.
生成这些 filter 的推荐方法是：

The recommended way to generate these filters is:
1. 打开 Object Explorer 并构建一个示例搜索，为您希望生成的所有 filter 选择样本值

1. Open Object Explorer and build an example search, with sample values chosen for all the filters you wish to generate
2. 打开 Chrome 控制台（*右键* -> *检查元素*）。请确保检查的是 Object Explorer 提供的元素（例如返回的结果数量），而不仅仅是打开 Chrome 控制台。

2. Open the Chrome Console (*right click* -> *inspect element*). Make sure you inspect an element that Object Explorer provides, such as the resulting count, rather than just opening the Chrome Console.
3. 在控制台中运行 `await hubble_get_current_search()`。

3. Run `await hubble_get_current_search()` in the console.
这将返回当前筛选器集合的 JSON，您可以使用它来确定正确的格式，并为值添加替换。

This will return the JSON for your current set of filters, which you can use to work out the correct format, and add substitutions for the values.
> **ℹ️ 注意**

> 您可以使用多个 *PROPERTY* 筛选器，但只能使用 1 个 *LINK* 筛选器。
> **ℹ️ 注意**

> You can have many *PROPERTY* filters, but only 1 *LINK* filter.
4. 对其进行 URL 编码：

4. URL encode it:
`encodeURIComponent(<MY_FILTERS>);`
`encodeURIComponent(<MY_FILTERS>);`
5. 创建一个 URL：

5. Create a URL:
`<BASEURL>/hubble/external/search/v2/{<ENCODED-URL-FROM-ABOVE>}`
`<BASEURL>/hubble/external/search/v2/{<ENCODED-URL-FROM-ABOVE>}`