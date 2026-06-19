<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/generate-urls/
---
# Generate Object View URLs
在开发 Object View 的过程中，您可能需要生成链接到特定对象的 URL 或搜索对象。

In the course of developing Object Views, you may need to generate URLs that link to a specific object or search for objects.
如果您是将这些视图嵌入到 iframe 中而不是作为链接提供，请附加 URL 查询参数 `embedded=true`，这样将在不加载 Workspace 侧边栏的情况下加载视图。

If you are embedding these views within an iframe rather than providing them as links, append a URL query parameter `embedded=true`, which will load the view without the Workspace sidebar.
> **ℹ️ 注意**

> 要了解如何创建链接到搜索或 Exploration 的 URL，请参阅 [生成 Object Explorer URL](/docs/foundry/object-explorer/generate-urls/)。
> **ℹ️ 注意**

> To learn how to create a URL linking to a search or Exploration, see [Generating Object Explorer URLs](/docs/foundry/object-explorer/generate-urls/).
## Generate object links
有两种方式可以链接到该 URL。

There are two ways to link into the URL.
**Option 1**
`/workspace/hubble/external/object/v0/<object-type-id>?<primary-key-property-id>=<primary-key-property-value>`
`/workspace/hubble/external/object/v0/<object-type-id>?<primary-key-property-id>=<primary-key-property-value>`
For example:
`/workspace/hubble/external/object/v0/aircraft?aircraftId=1234`
`/workspace/hubble/external/object/v0/aircraft?aircraftId=1234`
**Option 2**
`/workspace/hubble/external/search/v2/?objectId=<objectRid>`
`/workspace/hubble/external/search/v2/?objectId=<objectRid>`
当 primary key property 的值可能包含特殊字符时,推荐使用这种方式。

This way is recommended when the primary key property value could possibly have special characters.
此 URL 会在 Object Explorer 的上下文中加载 Object View。若要加载不包含任何额外包装的 Object View(例如,用于 iframe 中),可创建如下 URL:`/workspace/hubble/objects/<objectRid>`。

This URL loads the Object View within the context of Object Explorer. To load the Object View with no additional wrapping (for instance, to use within an iframe), create a URL like `/workspace/hubble/objects/<objectRid>`.