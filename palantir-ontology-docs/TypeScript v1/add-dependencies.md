<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/add-dependencies/
---
# Add npm dependencies
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更 [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 和可配置资源请求的支持，我们建议 [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
Functions 仓库使用 [npm ↗](https://www.npmjs.com/) 来管理依赖项，包括用于基于 Foundry ontology 生成代码以及在代码中发现 functions 的包。您可以使用 `npm` 将外部依赖项安装到您的仓库中，使用标准包来满足以下用途：操作数字和日期、执行统计计算或处理 XML 等数据格式。

Functions repositories use [npm ↗](https://www.npmjs.com/) for managing dependencies, including packages for generating code based on the Foundry ontology and discovering functions in your code. You can use `npm` to install external dependencies into your repositories, using standard packages for purposes such as manipulating numbers and dates, performing statistical calculations, or working with data formats such as XML.
请注意，functions 运行时仅支持纯 JavaScript 库——任何依赖于 NodeJS 运行时并进行系统调用的包均不受支持。

Note that the functions runtime only supports pure JavaScript libraries—any package that relies on a NodeJS runtime and makes system calls is not supported.
## Enable fetching dependencies from the public npm registry
默认情况下，functions 仓库不会从公共 npm registry 获取包。

By default, functions repositories do not fetch packages from the public npm registry.
如果您的仓库尚未从公共 npm registry 获取依赖项，当您在 Code Repositories 中打开 `package.json` 文件时，将出现一个用于启用该功能的横幅。

If your repository does not already fetch dependencies from the public npm registry, a banner for enabling it will appear when you open a `package.json` file in Code Repositories.
![Enable an external npm in Code Repositories.](/docs/resources/foundry/functions/external-npm.png)
## Add dependencies in Code Repositories
您可以使用 **Code Repositories** 中的 Libraries 侧边栏向您的 functions 仓库添加包。搜索所需的包，然后选择一个结果以查看诸如最新版本之类的详细信息。结果包括来自 Foundry 和 <https://npmjs.com> 的包。

You can add packages to your functions repository using the Libraries sidebar in **Code Repositories**. Search for the desired package, and select a result to view details like the latest version. Results include packages from Foundry and <https://npmjs.com>.
![Add a library from the Code Repositories sidebar.](/docs/resources/foundry/functions/npm-installation-controls.png)
选择是将包添加到 `package.json` 文件中的 `dependencies` 还是 `devDependencies`。选择 **Add and install library** 将包添加到您的仓库中。

Choose whether to add the package to `dependencies` or `devDependencies` in your `package.json` file. Select **Add and install library** to add the package to your repository.
![Confirm the library dependency changes before adding a library.](/docs/resources/foundry/functions/npm-backing-repositories.png)
如果包的来源仓库尚未配置为 backing repository，则会弹出一个对话框，提示您导入其他资源。**Add and install library** 按钮会自动将该包及其依赖项导入到您的 functions 仓库，并更新您的 `package.json` 和 `package-lock.json`。

If the package's originating repository is not yet configured as a backing repository, a dialog will prompt you to import additional resources. The **Add and install library** button automatically imports the package and its dependencies into your functions repository, updating your `package.json` and `package-lock.json`.
一旦正在运行的安装任务完成，该包即可在您的仓库中使用。

Once the running install tasks have finished, the package will be ready for use within your repository.
如果您使用的 `typescript-functions` 模板版本低于 0.520.0，则通过 task runner 进行的安装将被禁用。在这种情况下，请提交您已更新的 `package.json` 文件，确保检查成功通过，然后重启 Code Assist 以使新包可用。

If you are using a `typescript-functions` template version lower than 0.520.0, installation through the task runner will be disabled. In this case, commit your updated `package.json` file, ensure checks pass successfully, then restart Code Assist to make the new package available.
## Manually add dependencies
您可以通过在 Code Repositories 中修改 `package.json` 文件来手动添加包。如果您需要安装特定版本的包，这将非常有用。打开 `package.json`，使用从 <https://npmjs.com> 选择的相应版本添加您的依赖项，然后选择 **Commit**。在验证检查成功通过后，重启 Code Assist 以使新包可用。

You can manually add a package by modifying the `package.json` file in Code Repositories. This can be useful if you need to install a specific package version. Open `package.json`, add your dependency with a relevant version chosen from <https://npmjs.com>, and select **Commit**. After verifying that checks pass successfully, restart Code Assist to make the new package available.
![Restart Code Assist by hovering over the status bar and selecting the status symbol.](/docs/resources/foundry/functions/restart-code-assist.png)
以下是在仓库中手动将 `d3-array` 包添加到 `package.json` 文件的示例：

Below is an example of adding the `d3-array` package manually to the `package.json` file in a repository:
```typescript
"dependencies": {
...
"d3-array": "^2.3.1"
},
"devDependencies": {
...
"@types/d3-array": "^2.0.0"
}
```