<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/instrumentation-telemetry/
---
# Instrumentation and telemetry in functions
你可以从你的 functions 中发出某些类型的 telemetry，以便对生产 workflows 进行监控和调试。

It is possible to emit certain types of telemetry from your functions to allow for monitoring and debugging of production workflows.
要了解如何查看由你的 functions 发出的 telemetry，请参阅我们的 [AIP 可观测性文档](/docs/foundry/aip-observability/overview/)。

To learn how to view telemetry emitted by your functions, see our [AIP observability documentation](/docs/foundry/aip-observability/overview/).
## Supported telemetry types
下表概述了每种 function 语言所支持的 telemetry 类型。请注意，针对所有 function 类型，系统会自动创建一个覆盖整个 function 执行总耗时的 span，以及一条请求日志。

The following table provides an overview of the types of telemetry supported by each function language. Note that a single span over the total execution duration of the function, along with a single request log, is automatically created for all function types.
| Language      | Logs | Spans                         | Metrics                         |
| ------------- | ---- | ----------------------------- | ------------------------------- |
| TypeScript v1 | Yes  | Only product-defined spans\[1] | Only product-defined metrics\[2] |
| TypeScript v2 | Yes  | Yes\[3]                        | Only product-defined metrics\[2] |
| Python        | Yes  | Yes\[3]                        | Only product-defined metrics\[2] |
\[1] TypeScript v1 functions 中的产品定义 span 包括 object 加载和 query 执行等操作。

\[1] Product-defined spans in TypeScript v1 functions include operations like object loads and query executions.
\[2] Foundry 会记录所有类型 functions 的总执行耗时。

\[2] Foundry records the total execution duration for all types of functions.
\[3] TypeScript v2 和 Python functions 会自动检测所有出站网络请求，但你也可以添加自定义 span。

\[3] TypeScript v2 and Python functions automatically instrument all outbound network requests, but custom spans can also be added.
### Logs
你可以从 functions 中发出自定义日志并追溯查看。以下示例演示了如何从 TypeScript v1、TypeScript v2 和 Python functions 中发出日志。

You can emit custom logs from functions and view them retroactively. The following examples demonstrate how to emit logs from TypeScript v1, TypeScript v2, and Python functions.
在 TypeScript v2 functions 中，Foundry 将设置 OpenTelemetry SDK 的全局 logger provider，你将能够从中获取一个 logger。如果你想使用第三方日志库，你必须将它们配置为通过从全局 logger provider 获取的 logger 来发出日志。

In TypeScript v2 functions, Foundry will set up the OpenTelemetry SDK's global logger provider, and you will be able to retrieve a logger from it. If you want to use third-party libraries for logging, you must configure them to emit logs through a logger obtained from the global logger provider.
```typescript tab="TypeScript v1"
export class MyFunctions {
@Function()
public myFunction(name: string): string {
console.log(`This is a custom log line ${name}.`);
return `Hello, ${name}!`;
}
}
```
```typescript tab="TypeScript v2"
import { logs } from "@opentelemetry/api-logs";

const logger = logs.getLogger("my-function");

export default function myFunction(name: string): string {
logger.emit({
attributes: { LOG_MESSAGE: "This is a custom log line." },
body: { name },
});

return `Hello, ${name}!`;
}
```
```python tab="Python"
import logging

from functions.api import function

logger = logging.getLogger(__name__)

@function
def my_function(name: str) -> str:
logger.info("This is a custom log line.")
return f"Hello, {name}!"
```
### Spans
你还可以在 TypeScript v2 和 Python functions 中创建自定义 span，以跟踪特定操作的耗时。以下示例演示了如何创建自定义 span。

You can also create custom spans in TypeScript v2 and Python functions to track the duration of specific operations. The following example demonstrates how to create a custom span.
在 TypeScript v2 和 Python functions 中，Foundry 将设置 OpenTelemetry SDK 的全局 tracer provider，您将能够从中获取一个 tracer。如果您希望使用第三方库进行追踪，您必须将它们配置为通过从全局 tracer provider 获取的 tracer 来发送 trace。

In TypeScript v2 and Python functions, Foundry will set up the OpenTelemetry SDK's global tracer provider, and you will be able to retrieve a tracer from it. If you want to use third-party libraries for tracing, you must configure them to emit traces through a tracer obtained from the global tracer provider.
```typescript tab="TypeScript v2"
import { trace } from "@opentelemetry/api";
import { Integer } from "@osdk/functions";

const tracer = trace.getTracer("my-function");

export default function sqrt(n: Integer): Integer {
const sqrt = tracer.startActiveSpan("my-custom-span", (span) => {
try {
return Math.sqrt(n);
} finally {
span.end();
}
});

return sqrt;
}
```
```python tab="Python"
import math

from functions.api import function

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

@function
def sqrt(n: int) -> int:
with tracer.start_as_current_span("my-custom-span"):
return math.sqrt(n)
```