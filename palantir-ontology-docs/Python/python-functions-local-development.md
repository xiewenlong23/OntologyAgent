<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/python-functions-local-development/
---
# Local development
您可以对 Python functions 仓库进行本地开发，从而在您的自定义环境中实现高速迭代。

You can carry out local development of Python functions repositories, allowing for high-speed iteration in your customized environment.
## Setting up local development for Python functions repositories
### Clone the repository
1. 在仓库的菜单栏中，选择 **Work locally** 以打开对话框并复制给定的仓库 URL。

![仓库顶部菜单栏，其中右侧有 "Work locally" 选项。](/docs/resources/foundry/functions/clone-repo.png)

!["Work locally" 对话框。](/docs/resources/foundry/functions/work-locally-dialog.png)

1. In the menu bar of your repository, select **Work locally** to open the dialog and copy the given repository URL.

![The top menu bar of a repository with the "Work locally" option to the right.](/docs/resources/foundry/functions/clone-repo.png)

![The "Work locally" dialog.](/docs/resources/foundry/functions/work-locally-dialog.png)

2. 使用命令行，在您本地机器上选择的目录中运行 `git clone <URI>`。然后使用 `cd` 命令导航到该仓库。

2. Using the command line, run `git clone <URI>` on your local machine in a directory of your choice. Then use the `cd` command to navigate to the repository.
### Limitations
* 授予的克隆 token 是短期且只读的，但可以推回您的仓库。

* 您仍然需要将更改推送到 Foundry 才能发布 artifact，或者如果您希望运行检查或构建。

* The token granted for cloning is short-lived and read-only, with the exception of pushing back to your repository.
* You will still need to push your changes to Foundry to publish artifacts, or if you wish to run checks or build.
## Set up the development environment
### Prerequisites
* 确保已安装 Java 17，并且环境变量 `JAVA_HOME` 指向正确的 Java 安装路径。可以从 [Oracle 网站 ↗](https://www.oracle.com/java/technologies/downloads/#java17) 下载 Java 17。

* Ensure Java 17 is installed and that the environment variable `JAVA_HOME` points to the right Java installation. Java 17 can be downloaded from the [Oracle website ↗](https://www.oracle.com/java/technologies/downloads/#java17).
> **ℹ️ 注意**

> 根据你的操作系统设置 `JAVA_HOME` 环境变量：
> **ℹ️ 注意**

> Setting the `JAVA_HOME` environment variable based on your operating system:
> * Windows：在 PowerShell 中运行 `SETX JAVA_HOME -m "<java-home-dir>"`。这会修改系统环境变量，你需要重启 shell 才能使更改生效。或者你可以运行 `[System.Environment]::SetEnvironmentVariable("JAVA_HOME", "<java-home-dir>")` 在当前进程中设置 `JAVA_HOME`。
> * Linux 或 macOS：运行 `export JAVA_HOME=<java-home-dir>`。
> * Windows: Run `SETX JAVA_HOME -m "<java-home-dir>"` in PowerShell. This modifies the system environment variable and you will need to restart the shell for changes to take effect. Alternatively you can run ` [System.Environment]::SetEnvironmentVariable("JAVA_HOME", "<java-home-dir>")` to set `JAVA_HOME` in the running process.
> * Linux or macOS: Run `export JAVA_HOME=<java-home-dir>`.
* 按照 [此处](/docs/foundry/code-repositories/repository-upgrades/#manual-branch-upgrade) 中概述的步骤，确保你的 repository 已升级到最新的 template 版本。

* 确保环境变量 `CI`、`JEMMA` 和 `CA` 未被设置。

* 如果在 Apple silicon Mac 上运行，请确保已安装 [Rosetta 2 ↗](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)。你可以在终端运行 `/usr/sbin/softwareupdate --install-rosetta --agree-to-license` 来安装 Rosetta 2。

* Ensure your repository is upgraded to the latest template version by following the steps outline [here](/docs/foundry/code-repositories/repository-upgrades/#manual-branch-upgrade).
* Ensure that the environment variables `CI`, `JEMMA`, and `CA` are not set.
* If running on an Apple silicon Mac, ensure that [Rosetta 2 ↗](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment) is installed. You can install Rosetta 2 by running `/usr/sbin/softwareupdate --install-rosetta --agree-to-license` in the terminal.
## Visual Studio Code
* 确保已安装 [Visual Studio Code ↗](https://code.visualstudio.com/)。

* 从 Visual Studio Code 网站或应用程序中的 **Extensions** 选项卡安装 [Python 扩展 ↗](https://marketplace.visualstudio.com/items?itemName=ms-python.python)。

* 若要自动生成用于配置 Visual Studio Code 的 Python 解释器的设置文件，请运行命令 `./gradlew vsCode`。

* Ensure you have [Visual Studio Code ↗](https://code.visualstudio.com/) installed.
* Install the [Python extension ↗](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Visual Studio Code site or from the **Extensions** tab in the application.
* To auto-generate settings files that configure the Python interpreter for Visual Studio Code, run the command `./gradlew vsCode`.
## PyCharm
* 若要设置 Python 开发环境，请运行命令 `./gradlew condaDevelop`。

* To set up a Python development environment, run the command `./gradlew condaDevelop`.
* 确保已在本地安装 [JetBrains PyCharm ↗](https://www.jetbrains.com/pycharm/)。

* Ensure you have [JetBrains PyCharm ↗](https://www.jetbrains.com/pycharm/) installed locally.
* 按照 [此处 ↗](https://www.jetbrains.com/help/pycharm/open-projects.html) 中概述的步骤导入项目。

* Import the project following the steps outlined [here ↗](https://www.jetbrains.com/help/pycharm/open-projects.html).
* 从状态栏上的 [Python Interpreter selector ↗](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#widget) 中选择 **Add New Interpreter**。

![add python interpreter screenshot](/docs/resources/foundry/functions/pycharm-add-python-interpreter.png)

* Choose **Add New Interpreter** from the [Python Interpreter selector ↗](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#widget) on the status bar.

![add python interpreter screenshot](/docs/resources/foundry/functions/pycharm-add-python-interpreter.png)

* 在 **Add Python Interpreter** 对话框的左侧窗格中，选择 **Virtualenv Environment**。

![configure python interpreter screenshot](/docs/resources/foundry/functions/pycharm-configure-python-interpreter.png)

* In the left-hand pane of the **Add Python Interpreter** dialog, select **Virtualenv Environment**.

![configure python interpreter screenshot](/docs/resources/foundry/functions/pycharm-configure-python-interpreter.png)

* 选择 **Existing environment**，并将 **Interpreter** 字段设置为 Conda 环境中的 Python 解释器。

* 对于 Unix，Python 解释器路径为 <code>\<your-conda-environment-dir>/bin/python</code>。

* 对于 Windows，Python 解释器路径为 <code>\<your-conda-environment-dir>\python.exe</code>。

* Choose **Existing environment** and set the **Interpreter** field to the Python interpreter from your Conda environment.
* For Unix, the Python interpreter path is <code>\<your-conda-environment-dir>/bin/python</code>.

* For Windows, the Python interpreter path is <code>\<your-conda-environment-dir>\python.exe</code>.
> **ℹ️ 注意**

> 根据是否启用了 test 插件，已安装的环境会包括 `./python-functions/build/conda/run-env`、`./python-functions/build/conda/test-env`，或两者兼有。如果你计划运行测试，应选择 test 环境。
> **ℹ️ 注意**

> Depending on whether the test plugin is enabled, the installed environments would include `./python-functions/build/conda/run-env`, `./python-functions/build/conda/test-env`, or both. You should pick the test environment if you plan on running tests.
* 选择 **Ok**。

* Select **Ok**.