<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-monitors/create_new_object_monitor/
---
# Create a new object monitor
> **⚠️ 警告**

> Object Monitors 已被 [Automate](/docs/foundry/automate/overview/) 取代。Automate 是一个完全向后兼容的产品，为平台中所有业务自动化提供了统一的入口。
> **⚠️ 警告**

> Object Monitors are superseded by [Automate](/docs/foundry/automate/overview/). Automate is a fully backward-compatible product that offers a single entry point for all business automation in the platform.
> **ℹ️ 注意**

> 本教程假定您已经将数据集成到 Foundry Ontology 中。如果您需要先完成此操作，请在文档中了解如何 [创建您的 Ontology](/docs/foundry/ontology/overview/)。
> **ℹ️ 注意**

> This tutorial assumes you already have data integrated into your Foundry Ontology. If you need to do this first, learn how to [create your Ontology](/docs/foundry/ontology/overview/) in the documentation.
## Create from Object Explorer
在保存探索后，可以点击屏幕右上角的 **Monitor** 来创建 Monitor。可通过在探索视图中点击 **Save** 并选择 Project 或文件夹目标来保存探索。

Monitors can be created in Object Explorer after saving an exploration by clicking **Monitor** in the upper right of your screen. An exploration can be saved by clicking **Save** in the exploration view and selecting a Project or folder destination.

> 📷 **[图片: save_exploration_tooltip]**

> 📷 **[图片: save_exploration_tooltip]**

### Create an object monitor
保存探索后，点击 **Monitor** 打开一个视图，其中显示使用此探索作为输入的所有 object monitors。在新创建的探索中，此列表为空。

After saving the exploration, click **Monitor** to open a view showing all object monitors using this exploration as an input. In newly created explorations, this list is empty.

> 📷 **[图片: add_new_monitor_popover_zero_state]**

> 📷 **[图片: add_new_monitor_popover_zero_state]**

点击 **Add new Monitor** 以打开简化设置视图来创建新的 monitor。

Click **Add new Monitor** to open a simplified setup view for a new monitor.

> 📷 **[图片: create_new_monitor_object_explorer_view]**

> 📷 **[图片: create_new_monitor_object_explorer_view]**

添加 monitor 名称、可选的 description，以及 monitor [condition](/docs/foundry/object-monitors/condition/)。

Add a monitor name, optional description, and monitor [condition](/docs/foundry/object-monitors/condition/).

> 📷 **[图片: condition_dropdown_create_new_monitor_object_explorer_view]**

> 📷 **[图片: condition_dropdown_create_new_monitor_object_explorer_view]**

> **ℹ️ 注意**

> 包含嵌套子条件的高级 condition 无法从此视图配置。必须从 Object Monitors application 中创建和修改它们。
> **ℹ️ 注意**

> Advanced conditions containing nested sub-conditions cannot be configured from this view. Instead, they must be created and modified from the Object Monitors application.
您还可以选择将默认保存位置从 **Private** 更改为 Public project。如果您计划有其他订阅者，建议将保存的 exploration 和 monitor 存储在共享 Project 中。

You may also optionally change the default save location from **Private** to a Public project. If you plan to have additional subscribers, we recommend storing the saved exploration and monitor in a shared Project.

> 📷 **[图片: monitor_save_location_dialog]**

> 📷 **[图片: monitor_save_location_dialog]**

输入所需信息并点击 save 后，您将返回该 exploration 的 monitor 列表。该列表现在将包含新创建的 monitor。

After entering the required information and clicking save, you will return to the list of monitors for the exploration. This list will now contain the newly created monitor.

> 📷 **[图片: after_creation_monitor_list_object_explorer]**

> 📷 **[图片: after_creation_monitor_list_object_explorer]**

### After saving
monitor 保存后，将提供其他选项。

Additional options are available once a monitor has been saved.
关于 monitor 的元数据，包括其保存位置、创建时间和最后更新时间，显示在 **Details** 选项卡中。此选项卡还显示 [expiration date](/docs/foundry/object-monitors/monitor/#expiration)，并允许您将 expiration 延长至未来三个月。

Metadata about the monitor, including its save location, creation time, and last updated time, are shown in the **Details** tab. This tab also displays the [expiration date](/docs/foundry/object-monitors/monitor/#expiration) and allows you to extend the expiration three months into the future.

> 📷 **[图片: object_explorer_monitor_details_tab]**

> 📷 **[图片: object_explorer_monitor_details_tab]**

可以从 **Subscribers** 选项卡添加或删除订阅者，并且可以为每个订阅者启用或禁用通知。

Subscribers may be added or removed from the **Subscribers** tab, and notifications can be enabled or disabled per subscriber.

> 📷 **[图片: object_explorer_monitor_subscribers_tab]**

> 📷 **[图片: object_explorer_monitor_subscribers_tab]**

Action 可以从 **Actions** 标签页进行可选配置。

Actions may be optionally configured from the **Actions** tab.
了解更多关于使用 Object Monitors [配置 Actions](/docs/foundry/object-monitors/actions/) 的信息。

Learn more about [configuring Actions](/docs/foundry/object-monitors/actions/) with Object Monitors.

> 📷 **[图片: object_explorer_monitor_actions_tab]**

> 📷 **[图片: object_explorer_monitor_actions_tab]**

quick actions 下拉菜单提供了禁用或静默 monitor 的选项,以及通过将 monitor 移至回收站来删除它的选项。

The quick actions dropdown provides options for disabling or muting the monitor and an option to delete the monitor by moving it to the trash.

> 📷 **[图片: object_explorer_monitor_quick_actions_popover]**

> 📷 **[图片: object_explorer_monitor_quick_actions_popover]**

## Create from Object Monitors application
Object Monitors application 显示了给定用户跨所有 Project 的所有可用 monitor 的概览。按照以下步骤在 application interface 中创建一个新的 monitor。

The Object Monitors application shows an overview of all available monitors across all Projects for a given user. Follow these steps to create a new monitor in the application interface.

> 📷 **[图片: management_application_overview]**

> 📷 **[图片: management_application_overview]**

1. 通过点击右上角的 **Add Monitor** 创建一个新的 monitor。

1. Create a new monitor by clicking **Add Monitor** in the upper right corner.

> 📷 **[图片: management_app_create_new_monitor_zero_state]**

> 📷 **[图片: management_app_create_new_monitor_zero_state]**

2. 为新的 monitor 选择保存位置。对于将有多个订阅者的 monitor,我们建议将它们存储在共享的 Project 中。

2. Select a save location for the new monitor. For monitors that will have multiple subscribers, we recommend storing them in a shared Project.

> 📷 **[图片: management_app_change_save_location]**

> 📷 **[图片: management_app_change_save_location]**

3. 提供完整的 condition 配置。配置选项因您选择使用 [event](/docs/foundry/object-monitors/condition/#event) 还是 [threshold](/docs/foundry/object-monitors/condition/#threshold) condition 而异。monitor [inputs](/docs/foundry/object-monitors/input/) 必须使用在 Object Explorer 中创建的现有已保存 exploration。如果所需的 input exploration 不存在,请在 Object Explorer 中 [创建它](/docs/foundry/object-explorer/save-explorations/),然后返回此步骤。

3. Provide the full condition configuration. Configuration options vary depending on if you choose to use [event](/docs/foundry/object-monitors/condition/#event) or [threshold](/docs/foundry/object-monitors/condition/#threshold) conditions. The monitor [inputs](/docs/foundry/object-monitors/input/) must use existing saved explorations created in Object Explorer. If the required input exploration does not exist, [create it](/docs/foundry/object-explorer/save-explorations/) in Object Explorer and then return to this step.

> 📷 **[图片: management_app_threshold_condition_tab]**

> 📷 **[图片: management_app_threshold_condition_tab]**

> 📷 **[图片: management_app_event_condition_tab]**

> 📷 **[图片: management_app_event_condition_tab]**

可以从 **Subscribers** 标签页添加其他订阅者。

Additional subscribers may be added from the **Subscribers** tab.

> 📷 **[图片: management_app_subscriber_tab]**

> 📷 **[图片: management_app_subscriber_tab]**

4. 单击 **Save** 以保存并启用您的新 monitor。

4. Click **Save** to store and enable your new monitor.