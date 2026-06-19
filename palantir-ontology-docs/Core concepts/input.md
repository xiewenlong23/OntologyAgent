<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/input/
---
# Input
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品，为平台中所有 business automation 提供单一入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
Monitor inputs 是使用 [object sets](/docs/foundry/analytics/datasets-object-sets/#object-sets) 定义的。Monitor [condition](/docs/foundry/object-monitors/condition/) 随后可以引用 inputs 的属性。Input 可用于计算 metric（例如 aggregate），或用于监控何时从该 input 中添加或删除 objects。

Monitor inputs are defined using [object sets](/docs/foundry/analytics/datasets-object-sets/#object-sets). The monitor [condition](/docs/foundry/object-monitors/condition/) may then reference attributes of the inputs. An input may be used to calculate a metric such as an aggregate, or to monitor when objects are added or removed from that input.
Input object sets 是通过在 [Object Explorer](/docs/foundry/object-explorer/save-explorations/) 中构建 **saved exploration** 来创建的。您可以将 saved explorations 添加为 monitor inputs，可以[直接在 Object Explorer 中](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-explorer)添加，也可以在 [Object Monitors application](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-monitors-application) 中配置新 monitor 时添加。

Input object sets are created by building a **saved exploration** in [Object Explorer](/docs/foundry/object-explorer/save-explorations/). You can add saved explorations as monitor inputs [directly in Object Explorer](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-explorer), or when configuring a new monitor [in the Object Monitors application](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-monitors-application).
在 Object Monitors application 中查看 object monitor 时，monitor input 会显示在 overview 区域。点击 monitor 即可打开 overview 面板。

The monitor input is displayed in the overview section when viewing an object monitor in the Object Monitors application. Click on a monitor to open the overview panel.
![View input in Object Monitors app](/docs/resources/foundry/object-monitors/input_shown_in_management_app.png)
在 Object Explorer 中查看特定的 saved exploration 时，使用该 exploration 作为 input 的 object monitors 会显示在屏幕右上角的 **Monitor** 弹窗中。

When viewing a particular saved exploration in Object Explorer, object monitors that use this exploration as input are displayed in the **Monitor** popover in the upper right of your screen.
![List of monitors using saved exploration in Object Explorer](/docs/resources/foundry/object-monitors/list_of_monitors_for_exploration.png)