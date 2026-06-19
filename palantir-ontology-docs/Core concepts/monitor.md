<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/monitor/
---
# Monitor
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品，为平台中所有 business automation 提供单一入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
Monitor 是一种 resource，用于定义一个或多个 inputs 上的 condition，以及在满足 input condition 时应触发的任何 Actions 或通知。

A monitor is a resource that defines a condition on one or more inputs and any resulting Actions or notifications that should be triggered when the input condition is met.
## Storage
Object Monitor 保存在 Foundry Project 层级结构中,并支持标准的资源操作,如保存、共享、移动、删除以及基于角色的访问控制。

Object monitors are saved in the Foundry Project hierarchy and are supported by standard resource operations such as save, share, move, delete, and role-based access.
了解 [Foundry filesystem](/docs/foundry/compass/move-and-share-resources/) 的相关信息。

Learn about the [Foundry filesystem](/docs/foundry/compass/move-and-share-resources/).
Object Monitor 通过唯一资源标识符进行识别,格式如下:

Object monitors are identified by a unique resource identifier in the format:
```
ri.object-sentinel.main.monitor.0cabb748-cf89-4404-be3c-c8f198cb2a0b
```
## Retention
Object Monitor 的历史活动记录会保留六个月,之后将被永久删除。如果需要将历史活动记录存储超过该期限,可以使用 Actions 将数据存储在一个长期存在的 Object 中,该 Object 的管理和控制方式与 [Foundry Ontology](/docs/foundry/ontology/overview/) 中任何其他用户创建的 Object 相同。

Historical activity for object monitors is retained for six months and permanently deleted after that time. If historical activity must be stored beyond this date, you can use Actions to store data in a long-lived object that is managed and controlled like any other user-created object in the [Foundry Ontology](/docs/foundry/ontology/overview/).
当数据被删除时,该数据也会从 Object Monitor 应用程序的 **History**(历史)选项卡中移除。您可以通过首先点击一个 monitor 以展开概览面板,然后点击 **History** 来找到 **History** 选项卡。

When data is deleted, it is also removed from the monitor activity **History** tab in the Object Monitor application. You can find the **History** tab by first clicking on a monitor to expand the overview panel, then clicking **History**.
## Expiration
Object Monitor 始终具有过期日期。最长允许的过期日期为未来三个月,并且可以由具有该 monitor `Editor` 角色的用户随时更新。

Object monitors always have an expiration date. The longest permitted expiration date is three months in the future and can be updated at any time by a user with an `Editor` role on the monitor.
可以在 Object Monitors 应用程序界面中查看和延长过期日期。点击一个 monitor 以查看屏幕右侧的 monitor 概览面板。然后,点击 **Details**(详细信息)选项卡。

The expiration date can be viewed and extended in the Object Monitors application interface. Click on a monitor to view the monitor overview panel to the right side of your screen. Then, click on the **Details** tab.
![Monitor expiration date in details tab](/docs/resources/foundry/object-monitors/view_and_extend_monitor_expiration.png)
了解如何在 [Object Explorer](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-explorer) 或 [Object Monitors](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-monitors-application) 应用程序中创建新的 object monitor。

Learn how to create a new object monitor in [Object Explorer](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-explorer) or the [Object Monitors](/docs/foundry/object-monitors/create_new_object_monitor/#create-from-object-monitors-application) application.