<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/functions/debug/
---
# Debug functions
> **⚠️ 警告**

> 以下文档特定于 TypeScript v1 functions。有关更[强大的功能](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2)，包括对 Ontology SDK 和可配置资源请求的支持，我们建议[迁移到 TypeScript v2](/docs/foundry/functions/typescript-v2-migration/)。
> **⚠️ 警告**

> The following documentation is specific to TypeScript v1 functions. For more [robust capabilities](/docs/foundry/functions/language-feature-support/#typescript-v1-vs-typescript-v2), including support for Ontology SDK and configurable resource requests, we recommend [migrating to TypeScript v2](/docs/foundry/functions/typescript-v2-migration/).
在编写 functions 时，您可能需要检查执行状态以修复代码正确性或性能方面的问题。以下是您可以用于此目的的功能。请注意，这些调试步骤也适用于 [unit tests](/docs/foundry/functions/unit-test-getting-started/)。

As you write functions, you will likely need to inspect the state of your execution to fix issues with code correctness or performance. Below are features you can use to do this. Note that these debugging steps also apply to [unit tests](/docs/foundry/functions/unit-test-getting-started/).
## Authoring debugger
使用 Code Repositories 中的调试器（debugger）工具来检查您的 unit test 运行时的行为。设置断点（breakpoint）以暂停 unit test 的执行，从而检查变量，并了解 functions 和 libraries。

Use the debugger tool in Code Repositories to examine the behavior of your unit test while it runs. Set breakpoints to pause the execution of the unit test in order to examine variables, and understand functions and libraries.
![Debugger overview panel.](/docs/resources/foundry/functions/debugger-overview.png)
## Set breakpoints
要使用调试器，您需要设置断点。这些断点指示调试器应暂停代码执行的具体位置，使您能够与变量进行交互。

To use the debugger, you need to set breakpoints. These breakpoints indicate the specific points where the debugger should pause the code execution, enabling you to interact with variables.
通过选择每行代码边距中的淡红色圆点来设置断点。调试器会在标记行运行*之前*暂停执行。如果需要，您可以在多个文件中设置多个断点。

Set a breakpoint by selecting the faded red dot in the margins of each line of code. The debugger suspends the execution *before* the marked line runs. You can set multiple breakpoints across several files, if needed.
![Debugger breakpoints.](/docs/resources/foundry/functions/debugger-breakpoint.png)
## Run the debugger
### During live preview
在代码中添加断点后，在 functions 面板中选择 **Run and debug**。

After adding breakpoints in your code, select **Run and debug**, located in the functions panel.
![Live preview debugger layout.](/docs/resources/foundry/functions/live-preview-debugger-run.png)
### During testing
在代码中添加断点后，在代码编辑器中 unit test 旁边选择 **Run test**。

After adding breakpoints in your code, select **Run test**, located next to the unit test in the code editor.
![Test debugger layout.](/docs/resources/foundry/functions/test-debugger-run.png)
## Use the debugger
调试器启动后,调试器面板将打开并在遇到的第一个断点处暂停。调试器左侧的栏允许你浏览代码、移除断点,以及完成或停止调试会话。

Once the debugger has started, the debugger panel will open and pause on the first breakpoint it encounters. The left bar of the debugger allows you to navigate the code, remove breakpoints, and finish or stop the debugging session.
在浏览代码时,编辑器会高亮显示下一行要执行的代码。使用以下按钮来推进调试器:

As you navigate the code, the editor highlights the line of code to be executed next. Use the following buttons to advance the debugger:
![Debugger controls.](/docs/resources/foundry/functions/debugger-controls.png)
1. **Resume execution(继续执行):** 继续执行直到完成,或直到被下一个断点暂停。

2. **Step over(单步跳过):** 执行该行代码,不进入内部函数。

3. **Step into(单步进入):** 如果该行代码中存在内部函数,则进入其中。

4. **Step out(单步跳出):** 跳出内部函数,推进调试器。

5. **Stop execution(停止执行):** 完全停止调试器。

6. **Remove breakpoints(移除断点):** 从 repository 中移除所有断点,运行单元测试时不会暂停执行。

7. **Settings(设置):** 切换调试器的开/关(不会清除断点)。

8. **Documentation(文档):** 打开文档以获取更多详细信息。

1. **Resume execution:** Continue execution until completion or until paused by the next breakpoint.
2. **Step over:** Execute the line of code without stepping into internal functions.
3. **Step into:** Navigate into internal functions if they exist in that line of code.
4. **Step out:** Navigate out of an internal function and advance the debugger.
5. **Stop execution:** Stop the debugger completely.
6. **Remove breakpoints:** Remove all breakpoints from the repository and run the unit test without pausing the execution.
7. **Settings:** Toggle the debugger on/off (without clearing the breakpoints).
8. **Documentation:** Open the documentation for additional details.
## Examine variables
在调试器运行时,你可以在代码执行的精确位置检查变量和数据。

While the debugger is running, you can examine the variables and data at the exact point of code execution.
### Frames
Frames(栈帧)表示调试器在其中处于活动状态或存在断点的函数。每个 frame 指示函数的名称,后跟文件名称以及函数所在代码的行号。

Frames represent the functions in which the debugger is active or in which breakpoints exist. Each frame indicates the name of the function followed by the name of the file and the line number in which the function is written.
选择一个 frame 以检查该 frame 内的变量,并针对该 frame 运行 console 命令。

Select a frame to examine the variables within that frame and run console commands against it.
### Variables
变量部分在 transform 执行时显示存储在局部和全局变量中的值。

The variables section displays the values stored in both local and global variables while the transform is executed.
![Debugger variables.](/docs/resources/foundry/functions/debugger-variables.png)
### Console
console 允许你在运行调试器时使用 JavaScript console 命令与数据进行交互。

The console allows you to interact with your data using JavaScript console commands while running the debugger.
> **ℹ️ 注意**

> 请注意,console 在所选 frame 的上下文中运行。尝试在属于不同 frame 的局部变量上执行命令将导致错误。
> **ℹ️ 注意**

> Note that the console operates within the context of the selected frame. Attempting to execute commands on variables local to a different frame will lead to an error.
![Debugger console.](/docs/resources/foundry/functions/debugger-console.png)
## Console logging
Functions 支持在执行期间输出 console logs 以用于调试。为此,只需使用 `console.log` 命令输出日志。例如:

Functions supports emitting console logs during execution for debugging purposes. To do so, simply use the `console.log` command to emit logs. For example:
```typescript
@Function()
public testConsoleLogging(n: Integer): Integer {
for (let i = 0; i < n; i++) {
console.log(`Iteration ${i}`);
}
return n;
}
```
以这种方式使用 console logs 对于调试正确性问题非常有用。你还可以添加 console logs 来识别代码中的性能瓶颈。有关如何提高 link traversal 逻辑性能的更多信息,请参阅 [optimizing performance](/docs/foundry/functions/optimize-performance/) 指南。

Using console logs in this way can be useful for debugging correctness issues. You can also add console logs to identify performance bottlenecks in your code. See the guide for [optimizing performance](/docs/foundry/functions/optimize-performance/) for more information on how to improve the performance of link traversal logic.
### During testing
当你在 **Authoring** 中使用 **Tests** 辅助工具运行 function 时,console logs 将被捕获并显示在下方:

When you run a function using the **Tests** helper in **Authoring**, console logs will be captured and displayed below:
![Console logging tests.](/docs/resources/foundry/functions/console-logging-tests.png)
### During live preview
当你在 **Authoring** 中使用 **Functions** 辅助工具运行 function 时,console logs 将被捕获并显示在下方,同时附带时间戳:

When you run a function using the **Functions** helper in **Authoring**, console logs will be captured and displayed below, along with timestamps:
![Console logging live preview.](/docs/resources/foundry/functions/console-logging-live-preview.png)