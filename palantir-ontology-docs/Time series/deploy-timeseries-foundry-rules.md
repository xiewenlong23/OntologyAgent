<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/deploy-timeseries-foundry-rules/
---
# Deploy time series Foundry Rules
> **ℹ️ 注意**

> 这些说明假定时间序列已在您的平台中设置好。了解更多关于[在 Foundry 中使用时间序列](/docs/foundry/time-series/time-series-usage/)的信息。
> **ℹ️ 注意**

> These instructions assume time series have already been set up in your platform. Learn more about [using time series in Foundry](/docs/foundry/time-series/time-series-usage/).
要在 Foundry Rules 中启用时间序列功能，请首先按照[部署 Foundry Rules](/docs/foundry/foundry-rules/deploy-foundry-rules/) 的步骤进行操作。部署 Foundry Rules 后，需要执行以下步骤以启用时间序列支持：

To enable time series features in Foundry Rules, first follow the steps to [deploy Foundry Rules](/docs/foundry/foundry-rules/deploy-foundry-rules/). Once you deploy Foundry Rules, the steps described below are required to enable time series support:
1. 要创建时间序列规则，工作流的输入之一必须是时间序列根 Object Type。对于所有希望编写时间序列规则的输入 Object Type，请开启 **Enable time series** 开关。

![切换开关以将 Object Type 用作时间序列规则的输入](/docs/resources/foundry/foundry-rules/enable-timeseries-on-object.png)

1. To create time series rules, one of the workflow inputs must be a time series root object type. For all of the input object types that you wish to write time series rules on, toggle the **Enable time series** switch on.

![Switch to enable using an object type as an input to a time series rule](/docs/resources/foundry/foundry-rules/enable-timeseries-on-object.png)

2. 如果您的时间序列数据是使用 [time series properties](/docs/foundry/time-series/time-series-setup/) 设置的，那么无需其他配置步骤，您可以开始编写基于时间序列的规则。但是，如果您的时间序列数据是使用 measures 配置的，则必须完成以下步骤：

2. If your time series data has been set up using [time series properties](/docs/foundry/time-series/time-series-setup/), then there are no additional configuration steps required and you can begin authoring time series based rules. However, if your time series data has been configured using measures, you must complete the following steps:
* 在切换 **enable time series** 开关时，将打开一个对话框，提示您从 **Series object type** 选择到 **Root object type** 的 Link。

* 然后，在 transform configuration 部分，您必须添加支持这些 measures 的*所有* [time series syncs](/docs/foundry/time-series/time-series-syncs/)。

![添加时间序列 sync 的选择器](/docs/resources/foundry/foundry-rules/add-a-time-series-sync.png)

* On toggling the **enable time series** switch, a dialog will open prompting you to select the link from the **Series object type** to the **Root object type**.
* Then, in the transform configuration section, you must add *all* [time series syncs](/docs/foundry/time-series/time-series-syncs/) that back these measures.

![Selector to add a time series sync](/docs/resources/foundry/foundry-rules/add-a-time-series-sync.png)

