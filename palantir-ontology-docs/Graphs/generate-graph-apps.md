<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/vertex/generate-graph-apps/
---
# Generate a graph from other applications
您可以在其他 Foundry 应用程序中配置一个 link，该 link 将自动生成一个预填充的 Vertex graph。

You can configure a link within other Foundry applications that will automatically generate a pre-populated Vertex graph.
## Using URL parameters to generate a graph
您可以使用 URL 参数执行以下操作：

You can use URL parameters to perform the following actions:
* 从现有 graph 启动或创建新 graph。

* 通过指定 object ID 或 object set ID 向 graph 添加 objects。

* 运行 [**Search Around** function](/docs/foundry/vertex/generate-graph-functions/)。
* 设置时间选择器的时间范围。

* Start with an existing graph or create a new graph.
* Add objects to the graph by specifying an object ID or object set ID.
* Running a [**Search Around** function](/docs/foundry/vertex/generate-graph-functions/).
* Setting the time range of the time selector.
这些参数仅适用于创建新 graphs 的 URL（`/workspace/vertex/graph/create`）：

These parameters apply only to the URL that creates new graphs (`/workspace/vertex/graph/create`):
* `selectObjectRid`：如果指定的 object 存在，则选择该 object 并将 graph 居中显示。

* `objectRid`：将指定的 object 作为节点添加到 graph。

* `objectSetRid`：将指定 object set 中的所有 objects 作为节点添加到 graph。

* `searchAroundFnRid`：将指定 **Search Around** function 的结果添加到 graph。该 function 将使用单个 object（如果与 `objectRid` 参数一起使用）或 `objectSetRid` object set 中的所有 objects 进行调用。

* 必须与 `objectSetRid` 或 `objectRid` URL 参数结合使用。

* `selectObjectRid`: Selects and centers the graph on the specified object, if it is present.
* `objectRid`: Adds the specified object as a node to the graph.
* `objectSetRid`: Adds all objects in the specified object set as nodes to the graph.
* `searchAroundFnRid`: Adds to the graph the result of the specified **Search Around** function. The function will be called with either a single object if used with the `objectRid` parameter, or all the objects from the `objectSetRid` object set.
* Must be used in conjunction with either the `objectSetRid` or the `objectRid` URL parameter.
以下参数适用于现有 graphs（`/workspace/vertex/graph/{graphRid}`）和新创建的 graphs（`/workspace/vertex/graph/create`）的 URL：

The following parameters apply to URLs both for existing graphs (`/workspace/vertex/graph/{graphRid}`) and newly-created ones (`/workspace/vertex/graph/create`):
* `selectedTime`：设置所选时间。

* `startTime`：设置时间范围的开始时间。

* `endTime`：设置时间范围的结束时间。

* `selectedTime`: Sets the selected time.
* `startTime`: Sets the start time for a time range.
* `endTime`: Sets the end time for a time range.
> **ℹ️ 注意**

> 所有时间可以是 UNIX 时间戳（以毫秒为单位）或 ISO 格式的日期/日期时间（例如 `2020-02-15/2020-02-15 13:45:00 UTC`）。如果指定了 `selectedTime` 但未指定 `startTime` 和 `endTime` 中的至少一个，则时间范围将具有默认持续时间并以所选时间为中心。如果指定了 `startTime` 和 `endTime` 但未指定 `selectedTime`，则所选时间将与 `startTime` 相同。
> **ℹ️ 注意**

> All times can be either UNIX timestamps in milliseconds or ISO-formatted dates/datetimes (e.g. `2020-02-15/2020-02-15 13:45:00 UTC`). If `selectedTime` is specified but at least one of `startTime` and `endTime` is not, the time range will have the default duration and be centered around the selected time. If `startTime` and `endTime` are specified but `selectedTime` is not, the selected time will be the same as `startTime`.
## Generate a Vertex graph from other applications
设置好 URL 参数后，您可以使用此 link 从其他应用程序生成预配置的 graph。例如，在 Object Explorer 中使用 Hyperlinks Widget：

Once you set your URL parameter, you can use this link to generate the pre-configured graph from other applications. For example, using the Hyperlinks Widget in Object Explorer:

> 📷 **[图片: Add Link to Widget]**

> 📷 **[图片: Add Link to Widget]**

