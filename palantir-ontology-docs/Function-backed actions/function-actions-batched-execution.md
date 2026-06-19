<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/function-actions-batched-execution/
---
# Batched execution
当 action 以批处理方式触发时，例如在 [Workshop inline edits](/docs/foundry/workshop/widgets-object-table/#inline-edits-cell-level-writeback) 或 [Automate](/docs/foundry/automate/execution-settings/) 中，backing function 通常会针对每个请求依次调用一次，并且所有编辑会在 action 调用结束时以原子方式应用。

When an action is triggered in batches, such as in [Workshop inline edits](/docs/foundry/workshop/widgets-object-table/#inline-edits-cell-level-writeback) or in [Automate](/docs/foundry/automate/execution-settings/), the backing function is usually called once per request in sequence, and all edits are applied atomically at the end of the action call.
或者，为了提高性能或解决编辑冲突，你可能希望将 function 配置为在单次执行中接收整个 action 调用批次。

Alternatively, to improve performance or resolve edit conflicts, you may wish to configure a function to receive the whole batch of action calls in a single execution.
要启用批处理执行，function 必须接收包含 *struct 列表*（也称为 "map" 或 "dictionary"）的 *单个 input parameter*。然后，你将能够启用批处理执行，并以通常将数据传递给 function 顶级 inputs 相同的方式将数据传递到此 struct 的字段中。

To enable batched execution, the function must receive *a single input parameter* containing *a list of structs* (also known as a "map" or "dictionary"). You will then be able to enable batched execution and pass data into the fields of this struct in the same way you would usually pass data to a function's top-level inputs.
使用批处理执行时：

When using batched execution:
* 单次 action 调用将触发单次 function 执行，list 输入参数中包含 *单条 entry*。

* 批量 action 调用将触发单次 function 执行，list 输入参数中包含 *多条 entry*。

* A single action call will invoke a single function execution with *a single entry* in the list input parameter.
* A batched action call will invoke a single function execution with *several entries* in the list input parameter.
### Example
代替使用具有以下签名的 function-backed action：

Instead of a function-backed action with the following signature:
```typescript
@OntologyEditFunction()
public updateDestination(flight: Flight, destination: Airport): void {
// update flight object
}
```
function 也可以接收一批（"batch"）请求，并在单次执行中处理所有请求：

A function can instead receive a "batch" of requests and process them all in a single execution:
```typescript
@OntologyEditFunction()
public updateDestinationBatch(batch: {flight: Flight, destination: Airport}[]): void {
batch.forEach(({flight, destination}) => {
// update flight object
});
}
```
然后，在配置 action type 时，可以为此 function 启用批量执行：

You can then enable batched execution for this function when configuring the action type:
![Batch execution toggle](/docs/resources/foundry/action-types/function_backed_actions_batch_execution_toggle.png)