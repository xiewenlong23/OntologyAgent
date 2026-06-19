<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/user-facing-error/
---
# User-facing errors
在平台的其他部分（例如 Workshop 或 Action）中运行 Function 时，您可能希望抛出一个带有详细消息的错误。为此，可以抛出一个 `UserFacingError`。例如：

When running functions in other parts of the platform, such as Workshop or actions, you may want to throw an error with a detailed message. To do so, throw a `UserFacingError`. For example:
```typescript tab="TypeScript v1"
import { Function, UserFacingError } from "@foundry/functions-api";
import { Employee } from "@foundry/ontology-api";

export class MyFunctions {
@Function()
public async searchExactlyFiveEmployees(employees: Employee[]): Proimse<string> {
if (employees.length != 5) {
throw new UserFacingError(`Pass in exactly 5 employees. Received ${employees.length}.`);
}

// search employees
}
}
```
```typescript tab="TypeScript v2"
import { Osdk } from "@osdk/client";
import { Employee } from "@ontology/sdk";
import { UserFacingError } from "@osdk/functions";

export default async function searchExactlyFiveEmployees(employees: Array<Osdk.Instance<Employee>>): Promise<string> {
if (employees.length != 5) {
throw new UserFacingError(`Pass in exactly 5 employees. Received ${employees.length}.`);
}

// search employees
}
```
```python tab="Python"
from functions.api import function, UserFacingError
from ontology_sdk import FoundryClient
from ontology_sdk.ontology.objects import Aircraft

@function()
def search_exactly_five_employees(
employees: list[Aircraft]
) -> str:
if not len(aircraft) == 5:
raise UserFacingError(f"Pass in exactly 5 employees. Received ${len(aircraft)}.")

# search employees
```
当在 [Workshop 应用程序](/docs/foundry/workshop/functions-use/) 中以 [Function-backed Action](/docs/foundry/action-types/function-actions-overview/) 的形式运行此代码，且员工数量不正确时，用户将看到以下错误：

When running this as a [Function-backed Action](/docs/foundry/action-types/function-actions-overview/) in a [Workshop application](/docs/foundry/workshop/functions-use/) with an incorrect number of employees, users will see the following error:
![user-facing-error](/docs/resources/foundry/functions/user-facing-error.png)
通过添加详细的面向用户的错误消息，您可以帮助 Function 的其他使用者快速识别并修复问题。

By adding a detailed user facing error message, you can help other users of your Function quickly identify and fix the issue.