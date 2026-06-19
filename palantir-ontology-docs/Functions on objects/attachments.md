<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/attachments/
---
# Attachments
> **⚠️ 警告**

> TypeScript v1 functions 在具有严格内存限制的环境中执行。在处理文件数据时，内存限制可能会很快被超出；我们建议仅与 20MB 以下的 attachments 进行交互。Python 和 TypeScript v2 functions 的默认限制为 1GB，可在 Ontology Manager 中进行调整。
> **⚠️ 警告**

> TypeScript v1 functions are executed in an environment that has strict memory limits. Exceeding these memory limits can happen quickly when dealing with file data; we recommend only interacting with attachments under 20MB. Python and TypeScript v2 functions have a default limit of 1GB, which can be adjusted in Ontology Manager.
Attachment 是行为类似于 object property 的文件。Attachments 作为临时文件上传，并通过 [actions 附加到 objects](/docs/foundry/action-types/upload-attachments/)。一旦附加到 object，attachment 就会被持久化，并且可以像访问其他 properties 一样进行访问。

An attachment is a file that acts like an object property. Attachments are uploaded as temporary files and [attached to objects using actions](/docs/foundry/action-types/upload-attachments/). Once attached to an object, an attachment is persisted and can be accessed similarly to other properties.
## Attachments in functions
Attachments 可以作为来自 actions 的输入传递给 functions，也可以作为 object 上的 properties 进行访问。您还可以在 functions 中创建并返回 attachments。

Attachments can be passed into functions as inputs from actions, or accessed as properties on objects. You can also create and return attachments in functions.
在使用 Python 时，attachments 通过 [API Gateway](/docs/foundry/api/ontologies-v2-resources/attachments/attachment-basics/) 进行管理。Attachment 类型在 [Python OSDK](/docs/foundry/ontology-sdk/python-osdk/) 中提供。

When using Python, attachments are managed using the [API Gateway](/docs/foundry/api/ontologies-v2-resources/attachments/attachment-basics/). An attachment type is provided in the [Python OSDK](/docs/foundry/ontology-sdk/python-osdk/).
以下是按语言划分的 attachments 导入语法：

Below is the import syntax for attachments by language:
```typescript tab="TypeScript v1"
import { Attachment } from "@foundry/functions-api";
```
```typescript tab="TypeScript v2"
import { Attachment } from "@osdk/functions";
```
```python tab="Python"
# For convenience, the OSDK Attachment type is re-exported from the Python functions `functions.api` package.
from functions.api import Attachment
```
## Read attachment data
附件上提供了一个 read 方法用于读取其原始数据。该方法的签名如下：

A read method is provided on attachments to read their raw data. The signature for the method is as follows:
```typescript tab="TypeScript v1"
// Blob is a standard JavaScript type, representing a file-like object of immutable, raw data.
// https://developer.mozilla.org/en-US/docs/Web/API/Blob
readAsync(): Promise<Blob>;
```
```typescript tab="TypeScript v2"
// Response interface is part of the Fetch API, and is provided by `undici` in the TypeScript v2 environment.
// https://developer.mozilla.org/en-US/docs/Web/API/Response
fetchContents(): Promise<Response>;
```
```python tab="Python"
# BytesIO is a standard Python type, representing a binary stream.
# https://docs.python.org/3/library/io.html#io.BytesIO
def read(self) -> BytesIO: ...
```
您可能需要使用相关库或编写自定义代码来处理复杂的文件类型。例如，PDF 文件必须使用合适的库进行解析。[详细了解如何向 functions 仓库添加依赖项](/docs/foundry/functions/add-dependencies/)。

You may need to use libraries or write your own custom code for handling complex file types. For example, PDFs must be parsed with an appropriate library. [Learn more about adding dependencies to functions repositories](/docs/foundry/functions/add-dependencies/).
### File parsing in TypeScript v1
TypeScript v1 functions 不支持文件系统。通常，与解析文件数据相关的依赖会依赖于 `fs` 模块，而该模块在 functions 环境中不可用。此限制可能导致在编译和执行过程中出现 `fs` 模块相关错误。为了解决此限制，您可以引入对内存文件系统（例如 `memfs`）的依赖。然后，将该依赖以 `fs` 名称进行别名映射。

TypeScript v1 functions do not offer filesystem support. Often, dependencies related to parsing file data will rely on the `fs` module, which is not available in the functions environment. This restriction may cause `fs` module errors during compilation and execution. To work around this restriction, you can introduce a dependency on an in-memory file system (`memfs`, for example). Then, alias the dependency under the `fs` name.
以下示例展示了在 `package.json` 文件中使用 NPM 依赖 `memfs` 的方式：

Below is an example using the NPM dependency `memfs` in a `package.json` file:
```json
"fs": "npm:memfs@^x.x.x"
```
## Create attachments
Functions 也可以用于创建附件并将其附加到对象上。为了使在 functions 中创建的附件能够被持久化，function 必须执行 [Ontology edit](/docs/foundry/functions/api-ontology-edits/)，将附件链接到对象。

Functions can also be used to create attachments and attach them to objects. For attachments created in functions to be persisted, the function must make an [Ontology edit](/docs/foundry/functions/api-ontology-edits/) that links the attachment to an object.
> **⚠️ 警告**

> 未附加到对象的附件只能由上传者查看，并且会在一定时间后自动删除。
> TypeScript v2 functions 不支持创建附件。
> **⚠️ 警告**

> Attachments that are not attached to an object can only be viewed by the uploader and are automatically deleted after a certain period of time.
> TypeScript v2 functions do not support creating attachments.
要创建附件，请使用附件上的 upload function。各语言中 upload function 的签名如下：

To create an attachment, use an upload function on the attachment. The signature for the upload function by language is as follows:
```typescript tab="TypeScript v1"
import { Attachments, Attachment } from "@foundry/functions-api";

// On Attachments:
uploadFile(filename: string, blob: Blob): Promise<Attachment>;
```
```python tab="Python"
from ontology_sdk import FoundryClient
from foundry_sdk_runtime.attachments import AttachmentMetadata

# On FoundryClient:
def upload(file_path: str, attachment_name: str) -> AttachmentMetadata: ...
# `file_path` is a local file to be uploaded.
```
以下示例展示了上传文件并将生成的附件分配给对象的过程。

The following example shows the process for uploading a file and assigning the resulting attachment to an object.
```typescript tab="TypeScript v1"
import { Attachments, Attachment, OntologyEditFunction } from "@foundry/functions-api";

@OntologyEditFunction()
public async updateMaintenanceLog(aircraft: Aircraft): Promise<void> {
const aircraftMaintenanceLogData: Blob = await aircraft.maintenanceLog.readAsync();
const completedMaintenanceLogData: Blob = await completedMaintenanceLog.readAsync();

// You will likely need to rely on libraries or custom code to create the `Blob` object, which is
// passed as a parameter into the `uploadFile` method.

// Compare the current aircraft logs and completed logs and create a new maintenance log.
const updatedMaintenanceLogData: Blob;

aircraft.maintenanceLog = await Attachments.uploadFile("maintenance-log.txt", updatedMaintenanceLogData);
}
```
```python tab="Python"
from io import BytesIO

from functions.api import function, Attachment, OntologyEdit
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Aircraft

@functions(edits=[Aircraft])
def update_maintenance_log(
aircraft: Aircraft,
completed_maintenance_log: Attachment
) -> list[OntologyEdit]:
client = FoundryClient()
ontology_edits = client.ontology.edits()

maintenance_log_data: BytesIO = aircraft.maintenance_log.read()
completed_maintenance_log_data: BytesIO = completed_maintenance_log.read()

# Compare the current aircraft logs and completed logs and create a new maintenance log
updated_maintenance_log_data: BytesIO = get_updated_maintenance_log(
maintenance_log_data,
completed_maintenance_log_data
)

editable_aircraft = ontology_edits.objects.Aircraft.edit(aircraft)

with open("updated-maintenance-log.txt", "wb") as f:
f.write(updated_maintenance_log_data.getbuffer())

editable_aircraft.maintenance_log = client.ontology.attachments.upload(
"updated-maintenance-log.txt",
"my_attachment"
)

return ontology_edits.get_edits()
```