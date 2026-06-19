<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/limits/
---
# Limits
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一款完全向后兼容的产品，为平台中的所有业务自动化提供单一入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
Object monitoring 实施多项限制以确保执行和触发效果的良好性能。这些限制及预期行为列于下表中。

Object monitoring implements several limits to ensure good performance for execution and triggering effects. These limits and the expected behavior are listed in the table below.
### Scale limits
| Description                                    | Limit       | Behavior when limit is reached |
| ---------------------------------------------- | ----------- | ------------------------------ |
| Number of times a monitor may trigger per hour | 12          | Monitor will be auto-disabled  |
| Number of times a monitor may trigger per day  | 96          | Monitor will be auto-disabled  |
| Max size of input for object added/removed condition | 100K     | Error message when saving the monitor OR runtime error when evaluating the monitor if the input set grows beyond 100K objects |
| Max number of subscribers to a single monitor  | 30           | Error message when saving the monitor |
| Max size of object type for realtime execution | 10M    | Error message when saving the monitor OR runtime error when evaluating the monitor if the total objects in the object type grows beyond the limit |