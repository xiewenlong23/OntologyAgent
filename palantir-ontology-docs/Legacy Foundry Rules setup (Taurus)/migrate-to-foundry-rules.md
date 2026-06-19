<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/migrate-to-foundry-rules/
---
# Migrate to Foundry Rules
虽然 Taurus 继续获得长期支持,但一些组织可能希望将其现有的 Taurus 工作流程迁移到 Foundry Rules,以受益于其他功能,例如更轻松的更改和 pipeline 维护,以及开发的进一步更新。请注意,Taurus 继续获得长期支持。

While long-term support for Taurus continues, some organizations may wish to migrate their existing Taurus workflows to Foundry Rules to benefit from additional features, such as improved ease in making changes and performing pipeline maintenance, and further updates to development. Note that Taurus continues to receive long-term support.
通过将 Taurus 用例迁移到 Foundry Rules,您可能受益于:

By migrating Taurus use cases to Foundry Rules, you may benefit from:
* 简化的部署,可以在几分钟内从单个 Foundry Rules 配置页面完成。

* 通过对 Foundry Rules 配置的单步更改进行修改和维护。

* 开箱即用的执行,无需与 pipeline 代码交互,包括 streaming workflows。

* 内置的 code generator,支持需要自定义 pipeline 代码的高级 Foundry Rules 用例。

* A simplified deployment that can be completed in minutes from a single Foundry Rules configuration page.
* Modifications and maintenance via single-step changes to the Foundry Rules configuration.
* Out-of-the-box execution without the need to interact with pipeline code, including streaming workflows.
* A built-in code generator supporting advanced Foundry Rules use cases requiring custom pipeline code.
Foundry Rules 的最佳工作流针对的是单一特定用例以及您希望用户编写的单一类型规则。如果您拥有多个用户组和多个规则编写应用程序，可以考虑多次使用迁移向导来创建多个规则工作流。

The optimal Foundry Rules workflow targets one specific use case with one type of rule that you want your users to author. If you have multiple user groups and multiple rule authoring applications, you may consider creating multiple rule workflows by using the migration wizard multiple times.
## Migration considerations
在迁移到 Foundry Rules 之前，请考虑以下几点：

Prior to migrating to Foundry Rules, consider the following:
* 如果您将 Taurus 用作更大型的产品套件（例如供应链优化、反洗钱或面向汽车行业的 QMOS），则目前无需执行迁移。

* If you use Taurus as a larger product offering such as supply chain optimization, anti-money laundering, or QMOS for the automotive industry, no migration needs to be performed at this time.
* 如果您的 Taurus 用例较为复杂，并包含以下任意组合，则迁移将需要进行一些重构工作，您应权衡前文所述收益与所需更改的范围：

* 您的 Taurus workshop 模块具有多个针对不同用户组进行不同配置的规则编辑器 widget。

* 您的 Taurus 仓库使用了 Taurus 包的某些高级功能或以特定方式应用了规则逻辑。一个使用中的高级功能示例可能是：仓库运行 proposals 以创建潜在的影响分析。

* 您的 [rule actions](/docs/foundry/foundry-rules/configure-rule-actions/) 实现了可选可见性（optional visibility），并使用了 object locator、object set 或 attachment 字段类型。

* If you have a complex Taurus use case including any combination of the following, the migration will require some refactoring work, and you should consider the trade-off between the benefits outlined previously and extent of the changes required:
* Your Taurus workshop module has multiple rule editor widgets with different configurations for various user groups.
* Your Taurus repository uses advanced features of the Taurus packages or applies the rule logic in specific ways. An example of an advanced feature in use may be that the repository runs the proposals to create potential impact analyses.
* Your [rule actions](/docs/foundry/foundry-rules/configure-rule-actions/) implement optional visibility, use object locator, object set, or attachment field types.
* 如果您正在积极为 Taurus 用例添加更多输入数据集、Object Type 或规则输出，Foundry Rules 提供的新配置界面可能会带来更高的可维护性。即使您选择结合使用 Java 仓库和 Foundry Rules 工作流，您也将受益于部分代码生成功能。

* If you are actively adding more input datasets, object types, or rule outputs to your Taurus use case, the new configuration interface provided by Foundry Rules may add maintainability. Even if you choose to use a Java repository in combination with a Foundry Rules workflow, you will benefit from partial code generation.
### Migrate Taurus workflow to Foundry Rules workflow
以下流程将使用您现有的 Object Type 和 Workshop 模块，但会创建一个并行的 pipeline 和新的输出数据集，以避免对正在运行的 pipeline 造成干扰。

The following process uses your existing object types and Workshop modules but creates a parallel pipeline and new output datasets to prevent disruptions to operating pipelines.
升级到 V2 时，将执行以下流程：

When upgrading to V2, the following processes are performed:
* 检查工作流中的 time series

* 升级现有 application

* 如有必要，取消链接（unlink）旧 application
* 需要执行手动操作以最终完成迁移

* Checks for time series in your workflow
* Upgrades the existing application
* Unlinks the old application if necessary
* Manual actions required to finalize migration
首先，请按照以下说明操作：

To start, follow the instructions below:
1. 从 Foundry 工作区导航侧边栏导航至 **Foundry Rules**，然后进入 **Old Workflows** 选项卡。

1. Navigate to **Foundry Rules** from the Foundry workspace navigation sidebar and then to the **Old Workflows** tab.
2. 选择 Ontology，并从列表中找到 V1 archetype 或使用搜索字段。

2. Select the Ontology and find the V1 archetype from the list or use the search field.
![Archetype V1 existing](/docs/resources/foundry/foundry-rules/archetype-v1-existing@2x.png)
3. 选择 **Migrate from older Version**。

3. Select **Migrate from older Version**.
4. 选择主规则编辑器 Workshop 资源，并查看用于保存新 Foundry Rules 工作流的目标文件夹。必要时重命名工作流。然后，选择 **Start**。

4. Choose the main rule editor Workshop resource and review the destination folder in which to save the new Foundry Rules workflow. Rename the workflow if necessary. Then, select **Start**
![Archetype V1 existing](/docs/resources/foundry/foundry-rules/archetype-v1-input@2x.png)
5. Foundry Rules 迁移向导将检查您现有的设置中是否包含 [time series](/docs/foundry/foundry-rules/timeseries-concepts/)。如果包含，则需要配置 Link Type 和 time series 同步。完成其他配置后，选择 **Save Rules workflow**。

5. The Foundry Rules migration wizard will check whether your existing set up includes [time series](/docs/foundry/foundry-rules/timeseries-concepts/). If so, you will need to configure the link types and time series syncs. Select **Save Rules workflow** once you have completed the additional configuration.

> 📷 **[图片: Foundry Rules 升级向导]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

6. 某些资源可能需要导入到项目中。查看并展开以验证资源列表，然后完成所需的屏幕操作，最后选择 **Save**。

6. Some resources may need to be imported to the project. Review and expand to verify the list of resources and then complete the required on-screen actions, then select **Save**.

> 📷 **[图片: Foundry Rules 升级向导]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

> 📷 **[图片: Foundry Rules 升级向导]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

7. 选择 **Upgrade rules application**。

7. Select **Upgrade rules application**.

> 📷 **[图片: Foundry Rules 升级向导]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

8. 如果系统提示，选择 **Unlink old application**。

8. If requested, select **Unlink old application**.

> 📷 **[图片: Foundry Rules 升级向导]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

9. 最后，请注意屏幕上的指引，并根据您新升级 pipeline 的使用场景遵循相应的说明：

9. Finally, take note of the on-screen guidance and follow the appropriate instructions based on your use case for the newly upgraded pipeline:

> 📷 **[图片: Foundry Rules 升级向导]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

* 我的 Foundry Rules 输出直接馈入 Ontology object types。

* 如果您的 Outputs 馈入 Ontology object types（例如，未经过任何额外的转换），那么您需要替换此 object type 的 [objects' backing datasets](/docs/foundry/object-link-types/create-object-type/#add-a-backing-datasource-to-a-new-object-type)，以便 alerts 来自新版本的 Foundry Rules。

* My Foundry Rules outputs directly feed into Ontology object types.
* If your Outputs feed into Ontology object types (for example, without any additional transformations), then you need to replace the [objects' backing datasets](/docs/foundry/object-link-types/create-object-type/#add-a-backing-datasource-to-a-new-object-type) of this object type so that alerts will come from the new version of Foundry Rules.
> **⚠️ 警告**

> 此选项将导致 [如果 object types 是 V1 则丢失 object edits](/docs/foundry/object-link-types/edit-object-type/)。否则，如果您必须保留 edits，您可以 [keep the backing dataset ↗](https://stackoverflow.com/questions/72477419/how-to-safely-delete-an-object-property-without-losing-the-object-edits) 并确保其内容是新 rules output 的直接副本。
> **⚠️ 警告**

> This option will result in [lost object edits if object types is V1](/docs/foundry/object-link-types/edit-object-type/). Otherwise, if you must retain edits, you may [keep the backing dataset ↗](https://stackoverflow.com/questions/72477419/how-to-safely-delete-an-object-property-without-losing-the-object-edits) and ensure that its content is a direct copy of the new rules output.
* 我对 Foundry Rules 输出应用了额外的转换。

* 您应使用新的 output datasets 来替换之前转换中的 rule outputs。对于高级使用场景，您可以注册一个 [custom repository to compute the rule outputs](/docs/foundry/foundry-rules/customize-foundry-rules-pipeline/)。

* 我有其他 rule editor Workshop applications。

* 如果您的 rule editors 都具有相同的 inputs 和 outputs，您可以让它们全部引用此 Rules workflow。您可以使用 Archetype 部署菜单在左侧的 **Applications** 标签页中部署更多的 rule editor Workshop applications。如果您的 rule editors 服务于不同的使用场景并具有不同的配置，您应在专用的 workflow 中逐个迁移它们，方法是部署一个新的 Rules Archetype。

* I apply additional transformations on my Foundry Rules outputs.
* You should use the new output datasets to replace the previous rule outputs in your transformations. For advanced use cases, you can register a [custom repository to compute the rule outputs](/docs/foundry/foundry-rules/customize-foundry-rules-pipeline/).
* I have other rule editor Workshop applications.
* If your rule editors all have the same inputs and outputs, you can have all of them refer to this Rules workflow. You can deploy more rule editor Workshop applications using Archetype's deploy menu in the **Applications** tab on the left. If your rule editors serve different use cases and have different configurations, you should migrate each one in a dedicated workflow by deploying a new Rules Archetype.
10. 完成这些步骤后，选择 **Mark migration completed**。您的使用场景现在可以在新的 Foundry Rules 环境中运行了。

10. Once the steps have been completed, select **Mark migration completed**. Your use case is now operational on the new Foundry Rules setup.
## Verify migration
要检查迁移到 Foundry Rules 是否成功，请访问保存 rules output dataset 的项目链接。

To check that the migration to Foundry Rules succeeded, access the link to the project where the rules output dataset was saved.
打开 rules output dataset，选择 **Build** 或转到 Schedules 标签页并 **Add build schedule**。

Open the rules output dataset and select **Build** or go to the Schedules tab and **Add build schedule**.

> 📷 **[图片: Transformations]**

> 📷 **[图片: Transformations]**

构建成功表示升级到 Foundry Rules 的过程已成功完成。

A successful build indicates the upgrade process to Foundry Rules was completed successfully.
## FAQs
* 我收到警告，提示我的 outputs 包含在 V2 中不同的配置。如何解决此问题？

Action type 表单可以配置为接受各种类型的输入。这可以是简单的数字或日期，也可以是附件、object properties 或来自其他表单参数的派生值。虽然迁移向导会尝试尽可能接近原始配置进行重建，但此警告消息表明配置可能已发生更改。

* I was warned that my outputs contain configuration that is different in V2. How do I resolve this?
Action type forms can be configured to accept various types of input. This can be simple numbers or dates but also attachments, object properties, or derived values from other form parameters. While the migration wizard attempts to recreate a configuration as close to the original as possible, this message warning indicates there may have been changes to the configuration.
要解决此问题，请检查您 rule effects 的 output 配置，如下所示：

To resolve, review the output configuration for your rule effects, as below:

> 📷 **[图片: Rule action]**

> 📷 **[图片: Rule action]**

然后，在完成迁移的第五步后检查 rule editor 表单，以确保其继续按照您的用例正常运行，如下所示：

Then, check the rule editor form after completing step five of the migration to ensure it continues to behave according to your use case, as below:

> 📷 **[图片: Outputs review]**

> 📷 **[图片: Outputs review]**

* 为什么我的 dataset 构建成功但其中没有数据？

* Why does my dataset build succeed but has no data in it?
构建作业包含另一个名为 rules status dataset 的 dataset，其中包含每个 rule 及其未正确运行原因的信息。此外，您可能尚未重新运行 writeback dataset；请参阅 [Author and run a rule guide](/docs/foundry/foundry-rules/author-and-run-a-rule/#author-and-run-a-rule) 中的第四步。该 dataset 也可以在 Build 页面的 **Transforms Configuration** 部分下找到：

The build job includes another dataset called the rules status dataset that contains information for each rule and why it did not run properly. Additionally, you may have not yet rerun your writeback dataset; see step four on the [Author and run a rule guide](/docs/foundry/foundry-rules/author-and-run-a-rule/#author-and-run-a-rule). The dataset can also be found under the **Transforms Configuration** section of the Build page:

> 📷 **[图片: Transformations ]**

> 📷 **[图片: Transformations ]**

* 如果其他人在同时对 Rules application 进行更改，为什么我无法取消迁移？

* Why am I unable to cancel the migration if someone else makes changes simultaneously to the Rules application?

> 📷 **[图片: Foundry Rules upgrade wizard]**

> 📷 **[图片: Foundry Rules upgrade wizard]**

如果您已完成升级 Rules application 的阶段，而当您随后尝试 **Cancel** 迁移时其他用户正在对 Rules application 进行更改，则会发生此错误。

This error happens if you have completed the stage of upgrading the Rules application, while another user makes changes to the Rules application when you then attempt to **Cancel** the migration.
要解决此问题，请打开 Rules Workshop application 并发布较早的已迁移版本以撤消所做的手动更改。然后您将能够成功取消升级过程。

To resolve, open the Rules Workshop application and publish the older migrated version to undo the manual changes made. You will then be able to cancel the upgrade process successfully.
* 为什么迁移在没有恰好一个 rule editor 和一个 proposal reviewer widget 的情况下无法继续？

* Rules applications 可以设计为包含任意数量的 rule editor widget 和任意数量的 proposal widget，但在 Taurus 和 Foundry Rules 之间的配置方式不同。在 Taurus 中，可以使用独特的属性来配置 widget，例如每个 widget 中可使用不同的 inputs。迁移不会合并多个 widget 的配置，而是将一个 rule editor widget 转换为一个 Rules workflow。然而，在新的 Foundry Rules 设置中，不同的配置应各自成为独立的 Rules workflow。

* 要解决迁移中的此问题，您应考虑以下场景及相应的解决方法。之后，请重新完成迁移向导。请注意，Workshop 的更改是版本化的，以便在必要时支持还原更改：

* 您意外地有多个 rule editor widget，但仅有一个是相关的。您应从您的 workshop module 中删除不相关的 widget，然后重试迁移。

* 您有多个具有相同配置的 widget。您应仅保留一个 widget，删除其他所有 widget。迁移完成后，您可以复制并粘贴更新后的 widget 以重新创建 application 的设计。

* 您有多个具有不同配置的 widget。在这种情况下，您应将 Workshop module 拆分为多个 module，每个 module 包含一个 rule editor widget，并为每个 widget 创建一个 Rules archetype。在向导中选择 **Migrate from older version** 以从每个 Workshop module 创建配置，从而节省时间。

* Why doesn't the migration proceed without exactly one rule editor and proposal reviewer widget each?
* Rules applications can be designed with any number of rule editor widgets and any number of proposal widgets, but are configured differently between Taurus and Foundry Rules. In Taurus, it is possible to configure the widgets with unique attributes such as having different inputs available in each. The migration would not combine configurations of multiple widgets but rather, translate one rule editor widget to one Rules workflow. In the new Foundry Rules setup however, different configurations should each be their own Rules workflow.
* To resolve this issue for your migration, you should consider the following scenarios and appropriate resolutions. After that, complete the migration wizard again. Note that Workshop changes are versioned to support reverting changes if necessary:
* You have multiple rule editor widgets by accident and only one is relevant. You should remove the irrelevant widgets from your workshop module and try the migration again.
* You have multiple widgets with the same configuration. You should remove all widgets but one. After the migration, you can copy and paste the updated widget to recreate the design of your application.
* You have multiple widgets with different configurations. In this case, you should split the Workshop module into multiple modules with one rule editor widget each and create a Rules archetype for each. Select **Migrate from older version** on the wizard to create the configuration from each Workshop module to save time.