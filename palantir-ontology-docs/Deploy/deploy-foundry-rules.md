<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/deploy-foundry-rules/
---
# Deploy Foundry Rules
> **ℹ️ 注意**

> Foundry Rules 的预期总部署时间约为 30 分钟。
> **ℹ️ 注意**

> The expected total deployment time for Foundry Rules is approximately 30 minutes.
部署 Foundry Rules 涉及部署每个 [component](/docs/foundry/foundry-rules/core-concepts/)，具体包括 Workshop 应用程序、backing objects 和 Actions，以及 Foundry Rules workflow 配置。首先部署模板，然后配置 workflow，最后编写并运行规则。这些步骤在以下文档中进行了说明：

Deploying Foundry Rules involves deploying each [component](/docs/foundry/foundry-rules/core-concepts/), specifically the Workshop application, the backing objects and Actions, and the Foundry Rules workflow configuration. This is done by first deploying a template, then configuring the workflow, and finally authoring and running a rule. These steps are described in the documentation below:
1. [部署 workflow 模板：](/docs/foundry/foundry-rules/deploy-workflow/) <em class="bp3-text-muted"> 预计时间约 3 分钟</em>

2. [配置 workflow：](/docs/foundry/foundry-rules/configure-workflow/) <em class="bp3-text-muted"> 预计时间约 10 分钟</em>

3. [编写并运行规则：](/docs/foundry/foundry-rules/author-and-run-a-rule/) <em class="bp3-text-muted"> 预计时间约 10 分钟</em>

1. [Deploy workflow template:](/docs/foundry/foundry-rules/deploy-workflow/) <em class="bp3-text-muted"> Expected time ~ 3 mins</em>
2. [Configure workflow:](/docs/foundry/foundry-rules/configure-workflow/) <em class="bp3-text-muted"> Expected time ~ 10 mins</em>
3. [Author and run a rule:](/docs/foundry/foundry-rules/author-and-run-a-rule/) <em class="bp3-text-muted"> Expected time ~ 10 mins</em>
如果在部署过程中遇到任何问题，请查看 [故障排查参考](/docs/foundry/foundry-rules/common-issues/) 页面。

If you encounter any issues during deployment, review the [troubleshooting reference](/docs/foundry/foundry-rules/common-issues/) page.
有关如何修改 Foundry Rules 产品（例如启用可选功能、添加自定义 properties 或更改编辑器权限）的信息，请查看 [自定义 Foundry Rules](/docs/foundry/foundry-rules/customization/) 页面。

For information about how to modify the Foundry Rules product (for instance by enabling optional features, adding custom properties, or changing editor permissions), review the [customize Foundry Rules](/docs/foundry/foundry-rules/customization/) page.
> **ℹ️ 注意**

> 在 2022 年 7 月之前，Foundry Rules（以前称为 Taurus）需要更多配置，包括用户编写的 transform。如果您在此日期之前部署了 Foundry Rules，请详细了解这些 [配置和概念](/docs/foundry/foundry-rules/legacy-foundry-rules-setup-taurus/)。
> **ℹ️ 注意**

> Prior to July 2022, Foundry Rules (previously known as Taurus) required more configuration, including a user-authored transform. If you deployed Foundry Rules before this date, learn more about these [configurations and concepts](/docs/foundry/foundry-rules/legacy-foundry-rules-setup-taurus/).