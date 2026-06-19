<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/media/
---
# Media
Functions 使你能够在 [TypeScript v2](/docs/foundry/functions/typescript-v2-getting-started/)、[Python](/docs/foundry/functions/python-getting-started/) 和 [TypeScript v1](/docs/foundry/functions/typescript-v1-getting-started/) 中访问和修改 media。TypeScript v2 和 Python 使用 `Media` type 来读取、上传和转换 media,并通过 [Ontology edits](/docs/foundry/functions/edits-overview/) 和 OSDK 支持 media 上传。TypeScript v1 functions 提供了一个 `MediaItem` type,具有用于处理不同类型 media 的内置操作,无需外部库。

Functions enable you to access and modify media in [TypeScript v2](/docs/foundry/functions/typescript-v2-getting-started/), [Python](/docs/foundry/functions/python-getting-started/), and [TypeScript v1](/docs/foundry/functions/typescript-v1-getting-started/). TypeScript v2 and Python use the `Media` type to read, upload, and transform media, and support media uploads through [Ontology edits](/docs/foundry/functions/edits-overview/) and the OSDK. TypeScript v1 functions provide a `MediaItem` type with built-in operations for working with different kinds of media without external libraries.
如果你需要任何当前开箱即用不支持的操作，你可能需要使用外部库或编写自己的自定义代码。[详细了解如何向 Functions 仓库添加依赖项。](/docs/foundry/functions/add-dependencies/)

If you need any operations that don't currently exist out-of-the-box, you will likely need to use external libraries or write your own custom code. [Learn more about adding dependencies to functions repositories.](/docs/foundry/functions/add-dependencies/)
## TypeScript v2 and Python
使用 Ontology 编辑 Functions 来上传 media 并在 Ontology 中创建对象。上传后，你可以从对象中读取和下载 media 文件以供应用程序使用。[详细了解 Foundry 中的 media sets。](/docs/foundry/media-sets-advanced-formats/media-overview/)

Use Ontology edit functions to upload media and create objects in the Ontology. Once uploaded, you can read and download media files from objects for use in your application. [Learn more about media sets in Foundry.](/docs/foundry/media-sets-advanced-formats/media-overview/)
你可以通过将 media 上传到 Ontology 来获取一个 `Media` 实例，从而在 TypeScript v2 和 Python Functions 中构建 Ontology edits。`Media` 类型包装了一个 `MediaReference`，并提供 [更高级别的操作](#media-ontology-sdk-operations)，用于获取内容、获取 metadata，以及将 media 附加到对象。你可以使用 `Media` 来构建 Ontology edit，或者将现有的 media 作为参数传递给 Function。

You can construct Ontology edits in TypeScript v2 and Python functions by uploading media to the Ontology to obtain a `Media` instance. The `Media` type wraps a `MediaReference` and exposes [higher-level operations](#media-ontology-sdk-operations) for fetching contents, fetching metadata, and attaching media to objects. You can use the `Media` to construct an Ontology edit, or pass existing media into the function as a parameter.
### Use as a function input or output type
Functions 可以接受 `Media` 作为输入，通过 `uploadMedia` 上传数据来创建临时 media，或者从对象的 media reference Property 中获取 `Media`。Functions 也可以返回 `Media` 类型，无论是临时上传的还是来自对象的 media reference Property。在 Function 中，你可以获取 `Media` 的字节内容、获取其 metadata，或者通过 Ontology edits 将其附加到 Ontology 对象。在 Python 中，你还可以获取完整的 per-variant metadata；在 TypeScript v2 中，`fetchMetadata` 目前仅暴露高级别字段（`mediaType`、`sizeBytes`、`path`）。

Functions can take in a `Media` as an input, create temporary media by uploading data with `uploadMedia`, or retrieve `Media` from a media reference property on an object. Functions can return a `Media` type as well, whether it has been temporarily uploaded, or if it came from an object's media reference property. In a function, you can fetch the byte contents of the `Media`, fetch its metadata, or attach it to an Ontology object via Ontology edits. In Python, you can also fetch the full per-variant metadata; in TypeScript v2, `fetchMetadata` currently exposes only the high-level fields (`mediaType`, `sizeBytes`, `path`).
```typescript tab="TypeScript v2"
import type { Media } from "@osdk/client";

export default async function echoMedia(media: Media): Promise<Media> {
return media;
}
```
```python tab="Python"
from functions.api import function, Media
# The Media type may also be imported from foundry_sdk_runtime
# from foundry_sdk_runtime.media import Media

@function
def echo_media(media: Media) -> Media:
return media
```
### Upload media
使用 Ontology SDK 的 `uploadMedia`（TypeScript v2）和 `client.ontology.media.upload_media`（Python）辅助方法在 Function 内上传原始字节。两者都会返回一个 `Media`，然后你可以使用 Ontology edit 来编辑 Ontology 对象的 media property，或者从 Function 中返回该 `Media`。

Use the Ontology SDK `uploadMedia` (TypeScript v2) and `client.ontology.media.upload_media` (Python) helpers to upload raw bytes within a function. Both return a `Media`, which you can then edit an Ontology object media property with an Ontology edit or return from the function.
```typescript tab="TypeScript v2"
import type { Client, Media } from "@osdk/client";
import { uploadMedia } from "@osdk/functions";

export default async function uploadMediaItem(
client: Client,
body: string,
fileName: string,
): Promise<Media> {
const blob = new Blob([body], { type: "text/plain" });
const media: Media = await uploadMedia(
client,
{ data: blob, fileName }
);
return media;
}
```
```python tab="Python"
from ontology_sdk import FoundryClient
from foundry_sdk_runtime.media import Media
from functions.api import function

@function(beta=True)
def upload_media(body: str, media_set_filename: str) -> Media:
client = FoundryClient()
media: Media = client.ontology.media.upload_media(
body=body.encode("utf8"),
filename=media_set_filename,
)
return media
```
```python tab="Python (async)"
from ontology_sdk import FoundryClient
from foundry_sdk_runtime.media import Media
from functions.api import function

@function(beta=True)
async def upload_media(body: str, media_set_filename: str) -> Media:
client = FoundryClient()
media_coroutine = client.ontology.media.async_upload_media(
body=body.encode("utf8"),
filename=media_set_filename,
)
# media_coroutine is awaitable.
return await media_coroutine
```
> **ℹ️ 提示**

> media 上传是临时的，除非将其设置到 Ontology 对象的 media reference Property 上。当 Ontology edits 被应用时，media 便会持久化到该 Ontology 对象的 Property 上。
> **ℹ️ 提示**

> Uploading media is temporary, unless set to an Ontology object's media reference property. When the Ontology edits are applied, the media is then persisted on the Ontology object property.
### Upload media in Ontology edit functions
无论你是在 Function 内上传了 media，还是将 `Media` 作为输入传递给 Function，你都可以更新现有 Ontology 对象上的 media properties，或者使用 `Media` 参数创建新的 Ontology 对象。

Whether you uploaded media within a function or received a `Media` as an input to the function, you can update media properties on existing Ontology objects or create new Ontology objects with `Media` parameters.
```typescript tab="TypeScript v2"
// Ensure you are using TypeScript OSDK 2.16 or greater

import type { Client, Media } from "@osdk/client";
import { Aircraft } from "@ontology-sdk/sdk";
import type { Edits } from "@osdk/functions";
import { createEditBatch, uploadMedia } from "@osdk/functions";

async function uploadTextToNewPlane(client: Client): Promise<Edits.Object<Aircraft>[]> {
const batch = createEditBatch<Edits.Object<Aircraft>>(client);
const blob = new Blob(["Hello, world"], { type: "text/plain" });
const media: Media = await uploadMedia(
client,
{ data: blob, fileName: "/planes/aircraft.txt" }
);
batch.create(Aircraft, { myMediaProperty: media, /* ... */ });
return batch.getEdits();
}

export default uploadTextToNewPlane;
```
```python tab="Python"
# Ensure you are using Python OSDK 2.198 or greater

from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Aircraft
from functions.api import function, OntologyEdit
from foundry_sdk_runtime.media import Media

@function(beta=True, edits=[Aircraft])
def upload_text_to_new_plane() -> list[OntologyEdit]:
client = FoundryClient()
edits = client.ontology.edits()
media: Media = client.ontology.media.upload_media(
body="Hello, world".encode("utf8"),
filename="/planes/aircraft.txt",
)
edits.objects.Aircraft.create(
pk = "primary_key",
my_media_property=media,
# ...
)
return edits.get_edits()
```
> **ℹ️ 提示**

> 在 2.20 之前的 TypeScript OSDK generator 版本中，`uploadMedia` 返回的是一个 `MediaReference`。从 2.20 版本开始，`uploadMedia` 返回 `Media`，它包装了底层的 `MediaReference`，并提供更高级别的操作，例如 `fetchContents`、`fetchMetadata` 和 `getMediaReference()`。你可以直接将 `Media` 传递到 `createEditBatch` 操作中。
> **ℹ️ 提示**

> In TypeScript OSDK generator versions before 2.20, `uploadMedia` returned a `MediaReference`. Starting in version 2.20, `uploadMedia` returns a `Media`, which wraps the underlying `MediaReference` and exposes higher-level operations such as `fetchContents`, `fetchMetadata`, and `getMediaReference()`. You can pass a `Media` directly into `createEditBatch` operations.
### Passing a media reference parameter on action type
类型为 media reference 的 Action 参数可以作为参数传递给 Function。

Action parameters of type media reference can be passed to the function as a parameter.
下面的截图显示了一个 Action 将 media 参数传递给其 backing function。

The screenshot below shows an action passing a media parameter to its backing function.

> 📷 **[图片: media-tutorial-media-action-parameter.png]**

> 📷 **[图片: media-tutorial-media-action-parameter.png]**

### Media Ontology SDK operations
> **ℹ️ 提示**

> 以下方法适用于任何 `Media` 实例，包括从 `upload_media` 返回的实例，以及作为 Object Type 上的 `Media` Property 暴露的实例。
> **ℹ️ 提示**

> The methods below work on any `Media` instance, including those returned from `upload_media` and those exposed as `Media` properties on object types.
#### Retrieve media bytes data
你可以访问存储在 `Media` 上的原始数据。该方法的签名如下：

You can access the raw data stored on the `Media`. The signature for the method is as follows:
```typescript tab="TypeScript v2"
fetchContents(): Promise<Response>;

// "Response" is a standard interface on the JavaScript Fetch API
// https://developer.mozilla.org/en-US/docs/Web/API/Response
const mediaContents: Response = await myAircraft.myMediaProperty.fetchContents();

if (mediaContents.ok) {
const mediaMimeType = mediaContents.headers.get("Content-Type");

// Blob is a standard JavaScript type, representing a file-like object of immutable, raw data.
// https://developer.mozilla.org/en-US/docs/Web/API/Blob
// https://developer.mozilla.org/en-US/docs/Web/API/Response/blob
const mediaBlob: Blob = await mediaContents.blob();
}
```
```python tab="Python"
get_media_content(self) -> BytesIO: ...

from io import BytesIO

# https://docs.python.org/3/library/io.html#io.BytesIO
raw_data: BytesIO = my_aircraft.my_media_property.get_media_content()
```
### Get media metadata
你可以获取 `Media` 的 metadata：

You can retrieve the metadata of the `Media`:
```typescript tab="TypeScript v2"
fetchMetadata(): Promise<MediaMetadata>;

// Example usage:
const mediaMetadata = await myAircraft.myMediaProperty.fetchMetadata();
const sizeBytes = mediaMetadata.sizeBytes;
const mediaType = mediaMetadata.mediaType;
```
```python tab="Python"
from foundry_sdk_runtime.media import MediaMetadata

# Example usage:
media_metadata: MediaMetadata = my_aircraft.my_media_property.get_media_metadata()
path = media_metadata.path
size_bytes = media_metadata.size_bytes
media_type = media_metadata.media_type
```
在 Python 中，`get_media_full_metadata()` 返回一个 `MediaFullMetadata`，其 `item_metadata` 是一个按 media 类型区分的 discriminated union。在 variant class 上 narrow（或检查 `item_metadata.type`）以访问特定类型的字段：

In Python, `get_media_full_metadata()` returns a `MediaFullMetadata` whose `item_metadata` is a discriminated union over the media type. Narrow on the variant class (or check `item_metadata.type`) to access type-specific fields:
```python tab="Python"
get_media_full_metadata(self) -> MediaFullMetadata: ...

# Narrow on the variant class (or check item_metadata.type) to access type-specific fields.
# Other variants include AudioMediaItemMetadata, VideoMediaItemMetadata,
# SpreadsheetMediaItemMetadata, Model3dMediaItemMetadata, DicomMediaItemMetadata,
# EmailMediaItemMetadata, and UntypedMediaItemMetadata. See the full schema:
# https://github.com/palantir/foundry-platform-python/blob/develop/docs/v2/MediaSets/models/MediaItemMetadata.md

from foundry_sdk.v2.media_sets.models import (
DocumentMediaItemMetadata,
ImageryMediaItemMetadata,
)
from foundry_sdk_runtime.media import MediaFullMetadata

full_metadata: MediaFullMetadata = my_aircraft.my_media_property.get_media_full_metadata()
item = full_metadata.item_metadata

if isinstance(item, DocumentMediaItemMetadata):
page_count = item.pages
title = item.title
elif isinstance(item, ImageryMediaItemMetadata):
dimensions = item.dimensions
bands = item.bands
```
### Transform media
> **⚠️ 警告**

> 媒体转换功能仍处于 beta 开发阶段。在活跃开发期间，功能可能会发生变化。
> **⚠️ 警告**

> Media transformations are in the beta stage of development. Functionality may change during active development.
您可以转换媒体项（例如旋转、调整大小或重新编码图像、切片或渲染 PDF 页面，或运行 OCR）并等待结果。转换任务被提交后，会通过轮询直到完成，然后返回转换后的内容。

You can transform media items (such as rotating, resizing, or re-encoding images, slicing or rendering PDF pages, or running OCR) and wait for the result. The transformation job is submitted, it is polled to completion, and the transformed content is returned.
在 TypeScript v2 中，转换功能通过 `@osdk/api/unstable` 作为实验性辅助函数暴露。在 Python 中，可以在生成的 `FoundryClient` 上调用 `client.ontology.media.transform_and_wait`。异步版本 `async_transform_and_wait` 接受相同的参数，并可被 await。

In TypeScript v2, transformations are exposed through `@osdk/api/unstable` as an experimental helper. In Python, call `client.ontology.media.transform_and_wait` on a generated `FoundryClient`. The async variant `async_transform_and_wait` takes the same arguments and can be awaited.
```typescript tab="TypeScript v2"
// Ensure you are using @osdk/api 2.8.0 or greater for transformAndWait.
// "MediaTransformation" is a discriminated union:
// each variant (`$image`, `$video`, `$audio`, `$documentToText`, `$documentToImage`, `$documentToDocument`, `$audioToText`, etc.)
// selects a transformation kind, with its own encoding and operation fields.
// See the "MediaTransformation" type definition for a full set of variants and operations:
// https://github.com/palantir/osdk-ts/blob/main/packages/api/src/experimental/MediaTransformation.ts

import {
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
type MediaTransformation,
} from "@osdk/api/unstable";
import type { Client, Media } from "@osdk/client";
import { uploadMedia } from "@osdk/functions";

export default async function rotateImage(
client: Client,
media: Media,
): Promise<Media> {
const transformation: MediaTransformation = {
$image: {
$encoding: "jpg",
$operations: [{ $rotate: { $angle: "DEGREE_180" } }],
},
};

const result: Response = await client(
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
).transformAndWait({
mediaReference: media.getMediaReference(),
transformation,
options: { pollIntervalMs: 3000, pollTimeoutMs: 30000 },
});

if (!result.ok) {
// The transformation failed; inspect result.status / result.text() for details.
throw new Error(`Transformation failed with status ${result.status}`);
}

// Re-upload the transformed bytes so the function returns a Media.
return uploadMedia(client, { data: await result.blob(), fileName: "rotated.jpg" });
}
```
```python tab="Python"
from foundry_sdk.v2.media_sets.models import (
ImageTransformation,
JpgFormat,
RotateImageOperation,
)
from foundry_sdk_runtime.errors import (
MediaTransformationFailedError,
MediaTransformationTimeoutError,
)
from foundry_sdk_runtime.media import Media
from functions.api import function
from ontology_sdk import FoundryClient

@function(beta=True)
def image_transform(document: Media) -> Media:
client = FoundryClient()
transformation = ImageTransformation(
encoding=JpgFormat(),
operations=[RotateImageOperation(angle="DEGREE_180")],
)
try:
transformed_bytes: bytes = client.ontology.media.transform_and_wait(
media_reference=document.get_media_reference(),
transformation=transformation,
poll_interval_seconds=3.0,
poll_timeout_seconds=30.0,
)
except MediaTransformationFailedError:
# The transformation job reported FAILED status.
raise
except MediaTransformationTimeoutError:
# poll_timeout_seconds elapsed before the job completed.
raise
# Re-upload the transformed bytes so the function returns a Media.
return client.ontology.media.upload_media(body=transformed_bytes, filename="rotated.jpg")
```
#### Example: Run page-by-page OCR on a PDF with bounding box output
此工作流接受一个 PDF（已上传到 media set 或附加到 object），并对每一页运行 OCR，请求 hOCR 输出。hOCR 是在每个检测到的词和行上带有 `bbox` 属性的 HTML，因此您可以从同一响应中提取识别出的文本及其边界框坐标。每次 `transform_and_wait` 调用返回一页的字节；通过迭代以覆盖整个文档。

This workflow takes a PDF (uploaded to a media set or attached to an object) and runs OCR on every page, requesting hOCR output. hOCR is HTML with `bbox` attributes on every detected word and line, so you can extract both the recognized text and its bounding box coordinates from the same response. Each `transform_and_wait` call returns the bytes for one page; iterate to cover the whole document.
```typescript tab="TypeScript v2"
import {
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
type MediaTransformation,
} from "@osdk/api/unstable";
import type { Client, Media } from "@osdk/client";
import type { Integer } from "@osdk/functions";

export default async function ocrPdfPages(
client: Client,
media: Media,
pageCount: Integer,
): Promise<string[]> {
const transformAndWait = client(
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
).transformAndWait;
const mediaReference = media.getMediaReference();

const pageResults: string[] = [];
for (let pageNumber = 0; pageNumber < pageCount; pageNumber++) {
const transformation: MediaTransformation = {
$documentToText: {
$operation: {
$ocrOnPage: {
$pageNumber: pageNumber,
$parameters: {
$outputFormat: { $hocr: {} },
$languages: [{ $language: "ENG" }],
},
},
},
},
};

const result = await transformAndWait({
mediaReference,
transformation,
options: { pollTimeoutMs: 120_000 },
});
if (!result.ok) {
throw new Error(`OCR failed on page ${pageNumber}: ${result.status}`);
}
pageResults.push(await result.text());
}
return pageResults;
}
```
```python tab="Python"
from foundry_sdk.v2.media_sets.models import (
DocumentMediaItemMetadata,
DocumentToTextTransformation,
OcrHocrOutputFormat,
OcrLanguageWrapper,
OcrOnPageOperation,
OcrParameters,
)
from foundry_sdk_runtime.media import Media
from functions.api import function
from ontology_sdk import FoundryClient

@function(beta=True)
def ocr_pdf_pages(document: Media) -> list[bytes]:
"""Run OCR on every page of a PDF and return the hOCR bytes per page.

Each hOCR document includes `bbox` attributes on detected words, lines, and
paragraphs; parse with any HTML parser to recover both text and bounding
boxes in a single pass.
"""
client = FoundryClient()
metadata = document.get_media_full_metadata().item_metadata
if not isinstance(metadata, DocumentMediaItemMetadata) or metadata.pages is None:
raise ValueError("Expected a PDF document with a known page count")

media_reference = document.get_media_reference()
page_results: list[bytes] = []

for page_number in range(metadata.pages):
transformation = DocumentToTextTransformation(
operation=OcrOnPageOperation(
page_number=page_number,
parameters=OcrParameters(
output_format=OcrHocrOutputFormat(),
languages=[OcrLanguageWrapper(language="ENG")],
),
),
)
hocr_bytes: bytes = client.ontology.media.transform_and_wait(
media_reference=media_reference,
transformation=transformation,
poll_timeout_seconds=120.0,
)
page_results.append(hocr_bytes)

return page_results
```
密集的页面可能使 OCR 运行时远远超过默认的 function timeout。请参阅 [Manage published functions](/docs/foundry/functions/manage-functions/) 以配置 function 执行超时。

Dense pages can push OCR runtime well past the default function timeout. See [Manage published functions](/docs/foundry/functions/manage-functions/) to configure function execution timeouts.
#### Example: Render PDF pages as images and slice ranges
对于需要每一页可视化渲染的工作流（用于下游图像标注、嵌入或显示），请使用 `$documentToImage` 和 `$renderPage` 来获取特定页面的 PNG/JPG 图像。要将 PDF 的子范围提取为独立的 PDF 文档，请使用 `$documentToDocument` 和 `$slicePdfRange`。以下每个 function 都会重新上传转换后的字节，以便返回一个 `Media`。每个 function 都是一个独立的 module；已注册的 function 是该 module 的 `export default`。

For workflows that need the visual rendering of each page (for downstream image annotation, embedding, or display), use `$documentToImage` with `$renderPage` to get a PNG/JPG image of a specific page. To extract a sub-range of the PDF as its own PDF document, use `$documentToDocument` with `$slicePdfRange`. Each function below re-uploads the transformed bytes so it can return a `Media`. Each function is its own module; a registered function is the module's `export default`.
将单个页面渲染为 PNG 图像：

Render a single page as a PNG image:
```typescript tab="TypeScript v2"
import {
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
type MediaTransformation,
} from "@osdk/api/unstable";
import type { Client, Media } from "@osdk/client";
import { uploadMedia } from "@osdk/functions";

export default async function renderFirstPageAsPng(
client: Client,
media: Media,
): Promise<Media> {
const transformation: MediaTransformation = {
$documentToImage: {
$encoding: "png",
$operation: { $renderPage: { $pageNumber: 0, $width: 1200 } },
},
};
const result = await client(
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
).transformAndWait({ mediaReference: media.getMediaReference(), transformation });
if (!result.ok) {
throw new Error(`Render failed: ${result.status}`);
}
// Re-upload the rendered page so the function returns a Media.
return uploadMedia(client, { data: await result.blob(), fileName: "page.png" });
}
```
```python tab="Python"
from foundry_sdk.v2.media_sets.models import (
DocumentToImageTransformation,
PngFormat,
RenderPageOperation,
)
from foundry_sdk_runtime.media import Media
from functions.api import function
from ontology_sdk import FoundryClient

@function(beta=True)
def render_first_page_as_png(document: Media) -> Media:
"""Render page 0 of a PDF at 1200px wide as a PNG and return it as a Media."""
client = FoundryClient()
transformation = DocumentToImageTransformation(
encoding=PngFormat(),
operation=RenderPageOperation(page_number=0, width=1200),
)
rendered_png: bytes = client.ontology.media.transform_and_wait(
media_reference=document.get_media_reference(),
transformation=transformation,
)
# Re-upload the rendered page so the function returns a Media.
return client.ontology.media.upload_media(body=rendered_png, filename="page.png")
```
将页面范围切片为新的 PDF 文档：

Slice a page range into a new PDF document:
```typescript tab="TypeScript v2"
import {
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
type MediaTransformation,
} from "@osdk/api/unstable";
import type { Client, Media } from "@osdk/client";
import { uploadMedia } from "@osdk/functions";

export default async function sliceFirstTenPages(
client: Client,
media: Media,
): Promise<Media> {
const transformation: MediaTransformation = {
$documentToDocument: {
$encoding: "pdf",
$operation: {
$slicePdfRange: {
$startPageInclusive: 0,
$endPageExclusive: 10,
$strictlyEnforceEndPage: false,
},
},
},
};
const result = await client(
__EXPERIMENTAL__NOT_SUPPORTED_YET__transformAndWait,
).transformAndWait({ mediaReference: media.getMediaReference(), transformation });
if (!result.ok) {
throw new Error(`Slice failed: ${result.status}`);
}
// Re-upload the sliced PDF so the function returns a Media.
return uploadMedia(client, { data: await result.blob(), fileName: "slice.pdf" });
}
```
```python tab="Python"
from foundry_sdk.v2.media_sets.models import (
DocumentToDocumentTransformation,
PdfFormat,
SlicePdfRangeOperation,
)
from foundry_sdk_runtime.media import Media
from functions.api import function
from ontology_sdk import FoundryClient

@function(beta=True)
def slice_first_ten_pages(document: Media) -> Media:
"""Return a new PDF containing pages 0-9 of the input PDF as a Media."""
client = FoundryClient()
transformation = DocumentToDocumentTransformation(
encoding=PdfFormat(),
operation=SlicePdfRangeOperation(
start_page_inclusive=0,
end_page_exclusive=10,
strictly_enforce_end_page=False,  # tolerate documents shorter than 10 pages
),
)
sliced_pdf: bytes = client.ontology.media.transform_and_wait(
media_reference=document.get_media_reference(),
transformation=transformation,
)
# Re-upload the sliced PDF so the function returns a Media.
return client.ontology.media.upload_media(body=sliced_pdf, filename="slice.pdf")
```
#### Example: Annotate every page with detected bounding boxes
要生成可视化调试输出（每个 PDF 页面渲染后在顶部绘制其 OCR 检测到的边界框），请为每个页面链式执行三个转换。对于每一页，将该页面渲染为图像，对同一页面运行 OCR 以恢复词/行的边界框，然后重新上传渲染后的图像并使用 `$image.$annotate` 对其进行标注。页面数量来自 `get_media_full_metadata()`，该方法目前仅在 Python 中可用。每一步都调用 `transform_and_wait`，并将上一步的字节作为新上传的内容馈送到下一步，每个已标注的页面都会被重新上传，以便该 function 每一页返回一个 `Media`。

To produce a visual debugging output (each PDF page rendered with its OCR-detected bounding boxes drawn on top) chain three transformations for every page. For each page, render the page as an image, OCR the same page to recover word/line bounding boxes, then re-upload the rendered image and annotate it with `$image.$annotate`. The page count comes from `get_media_full_metadata()`, which is currently available in Python only. Each step calls `transform_and_wait` and feeds the bytes of the previous step into the next as a fresh upload, and each annotated page is re-uploaded so the function returns one `Media` per page.
```python tab="Python"
from foundry_sdk.v2.media_sets.models import (
AnnotateImageOperation,
Annotation,
BoundingBox,
BoundingBoxGeometry,
DocumentMediaItemMetadata,
DocumentToImageTransformation,
DocumentToTextTransformation,
ImageTransformation,
OcrHocrOutputFormat,
OcrLanguageWrapper,
OcrOnPageOperation,
OcrParameters,
PngFormat,
RenderPageOperation,
)
from foundry_sdk_runtime.media import Media
from functions.api import function
from ontology_sdk import FoundryClient

@function(beta=True)
def annotate_pdf_with_ocr_boxes(document: Media) -> list[Media]:
"""Render every page of a PDF, OCR each page to find text bounding boxes,
draw them on the rendered image, and return one annotated Media per page."""
client = FoundryClient()
media_reference = document.get_media_reference()

# Use the full metadata (Python only) to discover the page count.
metadata = document.get_media_full_metadata().item_metadata
if not isinstance(metadata, DocumentMediaItemMetadata) or metadata.pages is None:
raise ValueError("Expected a PDF document with a known page count")

annotated_pages: list[Media] = []
for page_number in range(metadata.pages):
# 1. Render the page as a PNG.
rendered_png: bytes = client.ontology.media.transform_and_wait(
media_reference=media_reference,
transformation=DocumentToImageTransformation(
encoding=PngFormat(),
operation=RenderPageOperation(page_number=page_number, width=1200),
),
)

# 2. OCR the same page in hOCR mode to get word-level bounding boxes.
hocr_bytes: bytes = client.ontology.media.transform_and_wait(
media_reference=media_reference,
transformation=DocumentToTextTransformation(
operation=OcrOnPageOperation(
page_number=page_number,
parameters=OcrParameters(
output_format=OcrHocrOutputFormat(),
languages=[OcrLanguageWrapper(language="ENG")],
),
),
),
poll_timeout_seconds=120.0,
)

# 3. Parse hOCR for bounding boxes in image pixels.
# The parse_hocr_bounding_boxes helper is omitted here; see the note below the example.
boxes: list[tuple[str, BoundingBox]] = parse_hocr_bounding_boxes(hocr_bytes)

# 4. Re-upload the rendered PNG as a temporary media item.
rendered_media = client.ontology.media.upload_media(
body=rendered_png, filename=f"page-{page_number}.png"
)

# 5. Annotate the rendered page with a Media transformation.
annotated_bytes: bytes = client.ontology.media.transform_and_wait(
media_reference=rendered_media.get_media_reference(),
transformation=ImageTransformation(
encoding=PngFormat(),
operations=[
AnnotateImageOperation(
annotations=[
Annotation(
geometry=BoundingBoxGeometry(bounding_box=box),
label=label,
)
for label, box in boxes
],
),
],
),
)

# 6. Re-upload the annotated page so the function returns a Media.
annotated_pages.append(
client.ontology.media.upload_media(
body=annotated_bytes, filename=f"page-{page_number}-annotated.png"
)
)

return annotated_pages
```
```python tab="Python (async)"
import asyncio

from foundry_sdk.v2.media_sets.models import (
AnnotateImageOperation,
Annotation,
BoundingBox,
BoundingBoxGeometry,
DocumentMediaItemMetadata,
DocumentToImageTransformation,
DocumentToTextTransformation,
ImageTransformation,
OcrHocrOutputFormat,
OcrLanguageWrapper,
OcrOnPageOperation,
OcrParameters,
PngFormat,
RenderPageOperation,
)
from foundry_sdk_runtime.media import Media
from functions.api import function
from ontology_sdk import FoundryClient

@function(beta=True)
async def annotate_pdf_with_ocr_boxes(document: Media) -> list[Media]:
"""Render every page of a PDF, OCR each page, annotate it, and return one Media per page."""
client = FoundryClient()
media_reference = document.get_media_reference()

metadata = document.get_media_full_metadata().item_metadata
if not isinstance(metadata, DocumentMediaItemMetadata) or metadata.pages is None:
raise ValueError("Expected a PDF document with a known page count")

async def annotate_page(page_number: int) -> Media:
# Render the page as a PNG and OCR the same page concurrently.
# Both transformations read from the same source document and are independent,
# so asyncio.gather lets them poll in parallel instead of one after the other.
rendered_png, hocr_bytes = await asyncio.gather(
client.ontology.media.async_transform_and_wait(
media_reference=media_reference,
transformation=DocumentToImageTransformation(
encoding=PngFormat(),
operation=RenderPageOperation(page_number=page_number, width=1200),
),
),
client.ontology.media.async_transform_and_wait(
media_reference=media_reference,
transformation=DocumentToTextTransformation(
operation=OcrOnPageOperation(
page_number=page_number,
parameters=OcrParameters(
output_format=OcrHocrOutputFormat(),
languages=[OcrLanguageWrapper(language="ENG")],
),
),
),
poll_timeout_seconds=120.0,
),
)

# Parse hOCR for bounding boxes (see the sync example) and re-upload the
# rendered PNG as a temporary media item, both concurrently.
boxes, rendered_media = await asyncio.gather(
async_parse_hocr_bounding_boxes(hocr_bytes),
client.ontology.media.async_upload_media(
body=rendered_png,
filename=f"page-{page_number}.png",
),
)

# Annotate the rendered page with a Media transformation.
annotated_bytes: bytes = await client.ontology.media.async_transform_and_wait(
media_reference=rendered_media.get_media_reference(),
transformation=ImageTransformation(
encoding=PngFormat(),
operations=[
AnnotateImageOperation(
annotations=[
Annotation(
geometry=BoundingBoxGeometry(bounding_box=box),
label=label,
)
for label, box in boxes
],
),
],
),
)

# Re-upload the annotated page so the function returns a Media.
return await client.ontology.media.async_upload_media(
body=annotated_bytes,
filename=f"page-{page_number}-annotated.png",
)

# Process every page concurrently.
return list(await asyncio.gather(*(annotate_page(p) for p in range(metadata.pages))))
```
此处省略了 `parse_hocr_bounding_boxes` 辅助函数。任何 HTML 解析器（例如 `lxml` 或 `BeautifulSoup`）都可以提取 `class="ocrx_word"` 元素及其 `title="bbox X1 Y1 X2 Y2 ..."` 属性，然后将其转换为 `BoundingBox(left=X1, top=Y1, width=X2-X1, height=Y2-Y1)`。

The `parse_hocr_bounding_boxes` helper is omitted here. Any HTML parser (such as `lxml` or `BeautifulSoup`) can extract `class="ocrx_word"` elements and their `title="bbox X1 Y1 X2 Y2 ..."` attributes, which you convert into `BoundingBox(left=X1, top=Y1, width=X2-X1, height=Y2-Y1)`.
## TypeScript v1
> **⚠️ 警告**

> Foundry 在执行 TypeScript v1 function 时会实施严格的内存限制。为确保不超过这些内存限制，您应仅与小于 20MB 的媒体文件交互。
> **⚠️ 警告**

> Foundry enacts strict memory limits when executing TypeScript v1 functions. To ensure you do not exceed those memory limits, you should only interact with media files under 20MB.
> **⚠️ 警告**

> TypeScript v1 不支持在 function 内上传媒体。以下示例涵盖将现有媒体传递到 Ontology 编辑中以及对 object type 的媒体属性进行操作。
> **⚠️ 警告**

> Uploading media within a function is not supported in TypeScript v1. The examples below cover passing existing media into Ontology edits and operating on media properties of object types.
### Setting existing media on an object
使用 Ontology edit function 将现有媒体项附加到 object：

Use Ontology edit functions to attach existing media items to objects:
```typescript tab="TypeScript v1"
import { OntologyEditFunction, MediaItem } from "@foundry/functions-api";
import { Aircraft } from "@foundry/ontology-api";

export class MyFunctions {
@OntologyEditFunction()
public async setExistingMediaToObject(
aircraft: Aircraft,
mediaItem: MediaItem
): Promise<void> {
// Ontology Edits with passed in MediaItems are supported
aircraft.myMediaProperty = mediaItem;
}
}
```
### Media item parameter on object types
以下示例展示了 object type 的 media reference property 上的 `isAudio` 媒体操作：

The following example shows the `isAudio` media operations on a media reference property of an object type:
```typescript tab="TypeScript v1"
MediaItem.isAudio(objectType.mediaReferenceProperty)
```
### Read raw media data
您可以通过选择 object 上的 media reference property 来访问媒体项。该方法的签名如下：

You can access a media item by selecting the media reference property on the object. The signature for the method is as follows:
```typescript tab="TypeScript v1"
// Blob is a standard JavaScript type, representing a file-like object of immutable, raw data.
// https://developer.mozilla.org/en-US/docs/Web/API/Blob
readAsync(): Promise<Blob>;
```
### Get media metadata
您可以访问 media item 的 metadata。该方法的签名如下：

You can access a media item's metadata. The signature for the method is as follows:
```typescript tab="TypeScript v1"
getMetadataAsync(): Promise<IMediaMetadata>;
```
### Type guards
TypeScript v1 中的 Type guards 允许您访问特定 media type 特有的功能。以下 Type guards 可用于 media item 的 metadata：

Type guards in TypeScript v1 allow you to access functionality that is specific to certain media types. The following type guards can be used on media item metadata:
* `isAudioMetadata()`
* `isDicomMetadata()`
* `isDocumentMetadata()`
* `isImageryMetadata()`
* `isSpreadsheetMetadata()`
* `isUntypedMetadata()`
* `isVideoMetadata()`
* `isAudioMetadata()`
* `isDicomMetadata()`
* `isDocumentMetadata()`
* `isImageryMetadata()`
* `isSpreadsheetMetadata()`
* `isUntypedMetadata()`
* `isVideoMetadata()`
举例来说，您可以使用 imagery Type guard 来提取图像特有的 metadata 字段：

As an example, you could use the imagery type guard to pull out image specific metadata fields:
```typescript tab="TypeScript v1"
const metadata = await myObject.mediaReference?.getMetadataAsync();
if (isImageryMetadata(metadata)) {
const imageWidth = metadata.dimensions?.width;
...
}
```
您也可以在 media item 的 namespace 上使用 Type guards，从而获得对特定类型 media item 访问更多方法的能力。您可以在此处使用的 Type guards 包括：

You can also use type guards on the media item namespace, which then gives you access to more methods on the type-specific media item. The type guards you can use here are:
* `MediaItem.isAudio()`
* `MediaItem.isDicom()`
* `MediaItem.isDocument()`
* `MediaItem.isImagery()`
* `MediaItem.isSpreadsheet()`
* `MediaItem.isVideo()`
* `MediaItem.isAudio()`
* `MediaItem.isDicom()`
* `MediaItem.isDocument()`
* `MediaItem.isImagery()`
* `MediaItem.isSpreadsheet()`
* `MediaItem.isVideo()`
### Document-specific operations
#### Text extraction
要从 document 中提取文本，您可以使用 optical character recognition (OCR) 或提取 media item 中嵌入的文本。

To extract text from a document, you can either use optical character recognition (OCR) or extract embedded text on the media item.
对于机器生成的 PDF，提取 PDF 中以数字方式嵌入的文本可能比使用 optical character recognition (OCR) 更快且/或更准确。以下是文本提取的用法示例：

For machine-generated PDFs, it may be faster and/or more accurate to extract text embedded digitally in the PDF rather than using optical character recognition (OCR). Below is an example of text extraction usage:
```typescript tab="TypeScript v1"
extractTextAsync(options: IDocumentExtractTextOptions): Promise<string[]>;
```
使用 TypeScript v1 时，可以以对象形式可选地提供以下参数：

When using TypeScript v1, the following can optionally be provided as an object:
* `startPage`：从零开始的起始页（包含，可以为空）

* `endPage`：从零开始的结束页（不包含，可以为空）。

* `startPage`: The zero-indexed start page (inclusive, can be empty)
* `endPage`: The zero-indexed end page (exclusive, can be empty).
如果 `startPage` 和 `endPage` 都留空，则将返回 document 中所有页的文本。

If both the `startPage` and `endPage` are left empty, the text for all pages in the document will be returned.
对于非机器生成的 PDF，最好使用 OCR 方法来提取文本。

For non-machine-generated PDFs, it would be best to use the OCR method for extracting text.
```typescript tab="TypeScript v1"
ocrAsync(options: IDocumentOcrOptions): Promise<string[]>;
```
以下参数可以可选地作为 TypeScript 对象提供：

The following can optionally be provided as a TypeScript object:
* `startPage`：从零开始的起始页（包含）。

* `endPage`：从零开始的结束页（不包含）。

* `languages`：要识别的语言列表（可以为空）。

* `scripts`：要识别的脚本列表（可以为空）。

* `outputType`：将输出类型指定为 `text` 或 `hocr`。

* `startPage`: The zero-indexed start page (inclusive).
* `endPage`: The zero-indexed end page (exclusive).
* `languages`: A list of languages to recognize (can be empty).
* `scripts`: A list of scripts to recognize (can be empty).
* `outputType`: Specifies the output type as `text` or `hocr`.
请注意，您需要使用 Type guards 才能访问特定 media type 的操作。以下示例使用 `isDocument()` Type guard 然后执行 OCR 文本提取：

Remember that you need to use type guards in order to access media-type specific operations. Here's an example of using the `isDocument()` type guard to then perform OCR text extraction:
```typescript tab="TypeScript v1"
import { MediaItem } from "@foundry/functions-api";
import { ArxivPaper } from "@foundry/ontology-api";

@Function()
public async firstPageText(paper: ArxivPaper): Promise<string | undefined> {
if (MediaItem.isDocument(paper.mediaReference)) {
const text = (await paper.mediaReference.ocrAsync({ endPage: 1, languages: [], scripts: [], outputType: 'text' }))[0];
return text;
}

return undefined;
}
```
### Audio-specific operations
#### Transcription
音频媒体项支持使用 transcribe 方法进行转录。其签名如下：

Audio media items support transcription using the transcribe method. The signature is as follows:
```typescript tab="TypeScript v1"
transcribeAsync(options: IAudioTranscriptionOptions): Promise<string>;
```
可以可选地传入以下参数以指定转录的执行方式：

The following can optionally be passed in to specify how the transcription should run:
* `language`：要转录的语言，通过 `TranscriptionLanguage` 枚举传入。

* `performanceMode`：以 `More Economical` 或 `More Performant` 模式运行转录，通过 `TranscriptionPerformanceMode` 枚举传入。

* `outputFormat`：通过传入 `type` 为 `plainTextNoSegmentData`（纯文本）或 `pttml` 的对象来指定输出格式。`pttml` 是一种 [类 TTML ↗](https://en.wikipedia.org/wiki/Timed_Text_Markup_Language) 格式，当 type 为 `plainTextNoSegmentData` 时，该对象还可以接受一个 Boolean 类型的 `addTimestamps` 参数。

* `language`: The language to transcribe, passed using the `TranscriptionLanguage` enum.
* `performanceMode`: Runs transcriptions in `More Economical` or `More Performant` mode, passed using the `TranscriptionPerformanceMode` enum.
* `outputFormat`: Specifies the output format by passing an object of `type` `plainTextNoSegmentData` (plain text) or `pttml`. `pttml` is a [TTML-like ↗](https://en.wikipedia.org/wiki/Timed_Text_Markup_Language) format where the object also takes a Boolean `addTimestamps` parameter if the type is `plainTextNoSegmentData`.
以下是一个为转录提供参数的示例：

An example of providing options for transcription:
```typescript tab="TypeScript v1"
import { Function, MediaItem, TranscriptionLanguage, TranscriptionPerformanceMode } from "@foundry/functions-api";
import { AudioFile } from "@foundry/ontology-api";

@Function()
public async transcribeAudioFile(file: AudioFile): Promise<string|undefined> {
if (MediaItem.isAudio(file.mediaReference)) {
return await file.mediaReference.transcribeAsync({
language: TranscriptionLanguage.ENGLISH,
performanceMode: TranscriptionPerformanceMode.MORE_ECONOMICAL,
outputFormat: {type: "plainTextNoSegmentData", addTimestamps: true}
});
}

return undefined;
}
```