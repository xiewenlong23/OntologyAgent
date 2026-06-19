<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/customize-foundry-rules-pipeline/
---
# Customize your Foundry Rules pipeline
> **⚠️ 警告**

> 定制 Foundry Rules pipeline 是一项高级功能，面向经验丰富的 Foundry pipeline 作者。此定制可能会给 workflow 管理员带来更大的实施和维护负担。
> **⚠️ 警告**

> Customizing your Foundry Rules pipeline is an advanced feature intended for experienced Foundry pipeline authors. This customization can result in increased implementation and maintenance burden for workflow administrators.
Foundry Rules 默认情况下不要求用户编写任何 pipeline 逻辑。但是，某些用例需要对 Foundry Rules pipeline 进行定制，以实现原本无法实现的结果。

Foundry Rules does not require users to write any pipeline logic out of the box. However, some use cases warrant customizing the Foundry Rules pipeline in order to achieve an outcome that is otherwise not possible.
## Use cases
定制您的 Foundry Rules pipeline 可以带来多种潜在好处，包括：

Customizing your Foundry Rules pipeline can provide a number of potential benefits, including:
* 对不同规则子集的运行方式和运行时机进行细粒度控制。

* 能够在运行规则逻辑之前预处理 Foundry Rules 输入。

* 能够在 [incremental transform](/docs/foundry/transforms-python/incremental-overview/) 中运行 Foundry Rules。这要求规则逻辑与增量数据兼容。

* Granular control over how and when different rule subsets are run.
* The ability to pre-process Foundry Rules inputs before running the rule logic.
* The ability to run Foundry Rules inside an [incremental transform](/docs/foundry/transforms-python/incremental-overview/). This requires the rule logic to be compatible with incremental data.
> **ℹ️ 注意**

> 对 Foundry Rules 输出的后处理（例如添加列）可以通过专用的下游 transform 实现。我们不建议仅为 Foundry Rules 输出的后处理而定制 Foundry Rules pipeline。
> **ℹ️ 注意**

> Post-processing of Foundry Rules outputs (such as adding columns) can be achieved with a dedicated downstream transform. We do not recommend customizing the Foundry Rules pipeline solely for post-processing of Foundry Rules outputs.
## Instructions
> **ℹ️ 注意**

> 流式 workflow 目前不支持自定义 pipeline。
> **ℹ️ 注意**

> Custom pipelines are currently not supported for streaming workflows.
您可以通过启用 self-managed transform、选择自定义 transform 仓库、保存 Foundry Rules workflow，然后将 Foundry Rules pipeline 代码生成并保存到所选仓库，从而部署您自己的自定义 Foundry Rules pipeline。为此，请按照以下说明操作：

You can deploy your own custom Foundry Rules pipeline by enabling self-managed transforms, choosing a custom transform repository, saving the Foundry Rules workflow, and then generating and saving the Foundry Rules pipeline code to the selected repository. To do so, follow the instructions below:
1. 单击齿轮图标以打开高级设置菜单。

1. Click on the gear icon to open the advanced settings menu.

> 📷 **[图片: Foundry Rules workflow 配置头中的按钮，用于打开 advanced settings]**

> 📷 **[图片: Button in the Foundry Rules workflow configuration header to open advanced settings]**

2. 启用 **Enable self-managed transforms** 选项。

2. Enable the **Enable self-managed transforms** option.

> 📷 **[图片: advanced settings 中用于启用 self-managed transforms 的按钮]**

> 📷 **[图片: Button in the advanced settings to enable self-managed transforms]**

3. 在 **Transforms Configuration** 部分中点击 **Use a custom transform repository**。您可以选择 **Deploy a new repository**（推荐）或选择 **Select existing repository** 来查找并选择您所选的 repository。

3. Click on **Use a custom transform repository** in the **Transforms Configuration** section. You can either **Deploy a new repository** (recommended) or choose **Select existing repository** to find and select your chosen repository.

> 📷 **[图片: 使用 custom transform repository 的按钮]**

> 📷 **[图片: Button to use a custom transform repository]**

4. 保存您的 Foundry Rules workflow。

4. Save your Foundry Rules workflow.
5. 通过点击 **Generate** 来生成并复制您的 Foundry Rules pipeline 代码，然后点击 **copy**。

5. Generate and copy your Foundry Rules pipeline code by clicking **Generate**, and then clicking **copy**.

> 📷 **[图片: 用于生成和复制 Foundry Rules transform 代码的按钮]**

> 📷 **[图片: Buttons to generate and copy Foundry Rules transform code]**

6. 如果您之前选择了一个已存在的 repository，请在 `rules.transforms` 目录中创建一个名为 `FoundryRulesTransform` 的文件，并将复制的代码粘贴进去。如果在步骤 3 中选择了新部署的 repository，请找到 "FoundryRulesTransform" 并粘贴代码。

6. If you previously chose an existing repository, create a file named `FoundryRulesTransform` that lives inside the `rules.transforms` directory and paste the copied code in. If a newly deployed repository was chosen in step 3, find “FoundryRulesTransform” and paste in the code.