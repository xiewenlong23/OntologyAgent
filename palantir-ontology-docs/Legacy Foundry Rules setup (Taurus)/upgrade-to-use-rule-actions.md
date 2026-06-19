<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/upgrade-to-use-rule-actions/
---
# Upgrade to use rule Actions
> **⚠️ 警告**

> 这些步骤适用于旧版本的Foundry Rules（以前称为Taurus）。如果您刚刚开始部署Foundry Rules，则无需执行以下步骤，因为这些步骤已作为[默认设置](/docs/foundry/foundry-rules/deploy-foundry-rules/)的一部分包含在内。除非您被专门引导到本节，否则您可能不需要遵循这些步骤。
> **⚠️ 警告**

> These steps are for legacy versions of Foundry Rules (previously known as Taurus). If you are just starting to deploy Foundry Rules, then the following steps are unnecessary and are already included as part of the [default setup](/docs/foundry/foundry-rules/deploy-foundry-rules/). Unless you've been specifically directed to this section, you likely do not need to follow these steps.
以前，Foundry Rules仅支持规则的数据集[inputs](/docs/foundry/foundry-rules/rule-logic/#inputs)，并且没有[rule Action](/docs/foundry/foundry-rules/configure-rule-actions/)的概念。虽然在对象上编写规则是一项可选功能，但我们强烈建议升级以使用**rule Actions**，尤其是当您升级以使用对象时。

Previously, Foundry Rules only supported dataset [inputs](/docs/foundry/foundry-rules/rule-logic/#inputs) to rules and had no concept of a [rule Action](/docs/foundry/foundry-rules/configure-rule-actions/). While authoring rules on objects is an optional feature, we strongly recommend upgrading to use **rule Actions**, especially if you upgrade to use objects.
要在Foundry Rules中启用对象和rule Actions，请按照以下步骤操作：

To enable objects and rule Actions in Foundry Rules, follow the steps below:
*所有截图均使用名义数据。*

*All screenshots use notional data.*
1. **升级您的Foundry Rules transforms库版本：** 确保 `tau-execution:tau-execution-core` 在项目级别的 `build.gradle` 文件中至少为 `0.60.4` 版本：

* `compile "com.palantir.tau-execution:tau-execution-core:0.60.4"`
* 如果找不到 `build.gradle` 文件，请在 **Files** 侧边栏中勾选齿轮图标下的 **Show hidden files and folders** 选项。

1. **Upgrade your Foundry Rules transforms library version:** Ensure that `tau-execution:tau-execution-core` is on *at least* version `0.60.4`, in the Project level `build.gradle` file:
* `compile "com.palantir.tau-execution:tau-execution-core:0.60.4"`
* If you can't find the `build.gradle` file, then check the **Show hidden files and folders** option in the **Files** sidebar under the gear icon.
2. **更新逻辑版本：** 在Foundry Rules Workshop应用程序中使用编辑模式，导航到 **Rule Editor widget**，并将 **Logic Version** 更改为 "V1"。虽然更改此选择器没有破坏性影响，但在更改为V1后无法将版本更改回V0。但是，返回V0没有任何好处。

2. **Update the logic version:** Using edit mode in your Foundry Rules Workshop application, navigate to the **Rule Editor widget** and change the **Logic Version** to be "V1". While changing this selector has no destructive effects, it is not possible to change the version back to V0 after changing it to V1. However, there would be no benefit in returning to V0.

> 📷 **[图片: 在workshop应用程序中选择V1逻辑版本]**

> 📷 **[图片: Selecting V1 logic version within the workshop app]**

3. **将对象添加到Workshop应用程序：** 在同一Workshop应用程序中，将您希望在Foundry Rules中可用的任何Object Type添加到 **Permitted object types** object set变量中。此变量应是您希望公开的所有Object Type的union Object Set，如下所示。

3. **Add objects to the Workshop application:** In the same Workshop application, add any object types you wish to make available within Foundry Rules to the **Permitted object types** object set variable. This variable should be a unioned object set of all the object types you wish to expose, as shown below.
* 如果您正在从数据集切换到相应的对象，则应保持数据集在Foundry Rules中可用，直到所有现有规则都已迁移到使用该对象。但是，没有立即切换到使用对象的迫切需要，因为transform可以在同时声明两者的情况下继续运行。

* If you are switching from a dataset to a corresponding object, then you should keep the dataset available in Foundry Rules until all of the existing rules have been migrated to use the object. However, there is no urgency to switch to using the object immediately, as the transform can continue to function with both declared.

> 📷 **[图片: 向workshop应用程序添加其他输入对象]**

> 📷 **[图片: Adding additional input objects to workshop app]**

4. **添加rule Actions：** 在[Ontology Manager](/docs/foundry/ontology-manager/overview/)中创建合适的Foundry Action后，通过单击 **Add Rule actions** 将该Action添加到Workshop应用程序中。

4. **Add rule Actions:** After creating a suitable Foundry Action in the [Ontology Manager](/docs/foundry/ontology-manager/overview/), add the Action to the Workshop application by clicking **Add Rule actions**.
了解更多关于[配置](/docs/foundry/foundry-rules/configure-rule-actions/) rule Actions的信息。

Learn more about [configuring](/docs/foundry/foundry-rules/configure-rule-actions/) rule Actions.

> 📷 **[图片: 配置可用的rule actions]**

> 📷 **[图片: Configuring the available rule actions]**

> **ℹ️ 注意**

> 在将rule Action添加到Workshop配置后，所有现有规则将在下一次编辑每个规则时要求您配置一个rule Action。但是，请务必注意，即使没有为每个规则配置rule Action，旧的transforms管道也将继续工作。因此，迁移不会带来任何停机时间，迁移可以按照适合用户的节奏进行。
> **ℹ️ 注意**

> After adding a rule Action to the Workshop configuration, all existing rules will require you to configure a rule Action the next time each of them are edited. However, it is important to note that even without a rule Action configured for each rule, the old transforms pipeline will continue to work. Therefore, there is no downtime associated with migrating, and the migration can be done at a pace that suits the users.
5. **更新transforms管道代码：** 更新transforms管道的最简单方法是通过添加缺失的对象和Actions来更新Ontology Manager中现有的规则workflow template实例。然后，部署更新后的transform以用作参考。在部署参考之后，您可以[配置transforms管道](/docs/foundry/foundry-rules/configure-transforms-pipeline/)以将此新代码映射到您现有的workflow。

5. **Update the transforms pipeline code:** The simplest way to update the transforms pipeline is to update your existing instance of the rules workflow template within the Ontology Manager by adding the missing objects and Actions. Then, deploy the updated transform to use as a reference. After deploying the reference, you can [configure the transforms pipeline](/docs/foundry/foundry-rules/configure-transforms-pipeline/) to map this new code to your existing workflow.
> **ℹ️ 注意**

> 如上所述,要使新的 transforms 代码正常工作,所有 rules 都必须配置 rule Action。因此,我们建议在分支上进行 transform 更改,并在合并之前测试这些 transform 更改。
> **ℹ️ 注意**

> As noted above, for the new transforms code to work, all rules must have a rule Action configured. Therefore, we recommend making the transform changes on a branch and testing those transform changes before merging.