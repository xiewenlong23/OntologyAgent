<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/foundry-rules/deploy-workflow/
---
# Deploy workflow
您可以在 Rules 应用程序中部署新的 Foundry Rules workflow。通过该应用程序，为您的 workflow 生成 [所需的 objects](/docs/foundry/foundry-rules/object-model/) 和 Actions。

You can deploy a new Foundry Rules workflow from within the Rules application. From the application, generate the [required objects](/docs/foundry/foundry-rules/object-model/) and Actions for your workflow.
1. **部署新的 Rules workflow：** 在侧边栏中找到并选择 Foundry Rules 应用程序，然后选择 **Rule-based data pipeline**。

![Rules 应用程序中部署 Foundry Rules 的按钮](/docs/resources/foundry/foundry-rules/rules-workflow-create@2x.png)

1. **Deploy a new Rules workflow:** Find and select the Foundry Rules application in the sidebar, then select **Rule-based data pipeline**.

![Button in the Rules application to deploy Foundry Rules](/docs/resources/foundry/foundry-rules/rules-workflow-create@2x.png)

2. **提供配置：** 该应用程序将为您创建一个新项目，其中包含相关的 backing datasets、Foundry Rules workflow 和 Workshop 应用程序资源。

![Rules Workflow 配置页面](/docs/resources/foundry/foundry-rules/rules_workflow_deployment_configuration@2x.png)

2. **Provide configuration:** The application will create a new project for you that includes the relevant backing datasets, Foundry Rules workflow, and Workshop application resource.

![Rules Workflow configuration page](/docs/resources/foundry/foundry-rules/rules_workflow_deployment_configuration@2x.png)

* 选择相关的 [space](/docs/foundry/security/orgs-and-spaces/)。

* 选择相关的 [Ontology](/docs/foundry/ontology/overview/)。如果您有多个 Ontologies，请选择包含您要为其定义规则的所有 object types 的 Ontology。

* Rule editor 组用于 actions 的提交标准。该组中的用户能够创建用于添加、编辑、删除规则的 proposals，并决定 proposals。此配置作为起点，您稍后可以在规则 actions 上配置提交标准。要更改 action types 上的提交标准，请查看 [FAQ](#faq)。

* Choose the relevant [space](/docs/foundry/security/orgs-and-spaces/).
* Choose the relevant [Ontology](/docs/foundry/ontology/overview/). If you have multiple Ontologies, select the Ontology that contains all the object types on which you would like to define your rules.
* The Rule editor group is used for the submission criteria of the actions. Users in this group are able to create proposals to add, edit, delete rules, and also, to decide on proposals. This configuration is meant as a starting point as you can configure the submission criteria on the rule actions later. To change the submission criteria on the action types, review the [FAQ](#faq).
3. **部署：** 填写完字段后，选择 **Deploy**。部署过程在后台大约需要两到三分钟，在此期间您可以安全地离开页面。挂起和已完成的安装可以在主页的 **Pending installations** 或 **Existing Rule Workflows** 下找到。所有 workflows 在现有 workflows 列表中都使用默认名称 "Foundry Rules Workflow" 和时间戳。您可以通过重命名项目文件夹中的相应资源来重命名 workflow。

![Rules Workflow 配置页面](/docs/resources/foundry/foundry-rules/rules_workflow_deploy_pending.png)

3. **Deploy:** Once the fields have been completed, select **Deploy**. The deploy process takes about two to three minutes in the background during which you can safely navigate away. Pending and completed installations can be found on the main page under **Pending installations** or **Existing Rule Workflows**. All workflows have the default name "Foundry Rules Workflow" and a timestamp in the list of existing workflows. You may rename the workflow by renaming the corresponding resource in your project folder.

![Rules Workflow configuration page](/docs/resources/foundry/foundry-rules/rules_workflow_deploy_pending.png)

完成上述步骤后，请了解如何 [配置 workflow](/docs/foundry/foundry-rules/configure-workflow/)。

After completing the above steps, learn how to [configure the workflow](/docs/foundry/foundry-rules/configure-workflow/).
## FAQ
### How do I change the submission criteria on the action types?
要更新 action types 的提交条件，请导航至 Workshop application，选择 **Edit**。然后，查看右侧的 Rule Editor configuration panel，如下所示。

To update your submission criteria on the action types, navigate to the Workshop application, select **Edit**. Then, review the Rule Editor configuration panel on the right as shown below.
![Workshop application Rule editor configuration panel screen](/docs/resources/foundry/foundry-rules/workshop-application-config-panel.png)
然后，将光标悬停在 **Create add proposal action** 的 "Create a proposal to add a rule" 下拉选项旁边的 "i" 图标上。

Then, hover your cursor over the "i" icon inline with the **Create add proposal action**'s "Create a proposal to add a rule" dropdown option.
在新的弹出窗口中，选择 **View Action Configuration**。

From the new pop up, select **View Action Configuration**.
![Create a proposal to add a rule pop-up](/docs/resources/foundry/foundry-rules/view-action-configuration.png)
从这里，您将能够更改 [submission criteria](/docs/foundry/action-types/submission-criteria/)。

From here, you will be able to change the [submission criteria](/docs/foundry/action-types/submission-criteria/).