<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/parameter-performance-considerations/
---
# Performance considerations for parameter configuration
Parameters 之间的依赖关系(例如在 [default values](/docs/foundry/action-types/parameters-default-value/) 和 [multiple-choice options](/docs/foundry/action-types/parameters-filter/) 的定义中)可能会影响 action 表单的加载时间。例如,考虑以下 action parameter 配置:

Dependencies between parameters, such as in the definitions of [default values](/docs/foundry/action-types/parameters-default-value/) and [multiple-choice options](/docs/foundry/action-types/parameters-filter/), can impact the time that it takes for an action form to load. For example, consider the following action parameter configuration:
1. 第一个 parameter 是 `object reference`,其 default value 为 `from single result of object set`。

2. 第二个 parameter 是一个 string,其 default value 是一个引用第一个 parameter 的 `object parameter property`。

3. 第三个 parameter 也是一个 string,没有 default value,但配置为使用 `get options from an object set` 的 `multiple choice` 下拉菜单。该 object set 定义引用了第二个 parameter。

1. The first parameter is an `object reference` with a `from single result of object set` default value.
2. The second parameter is a string with a default value that is an `object parameter property` referencing the first parameter.
3. The third parameter is also a string, with no default value, but configured as a `multiple choice` dropdown using `get options from an object set`. The object set definition references the second parameter.
当用户加载此 action 的 action 表单时,需要迭代地执行多个操作。

When a user loads an action form for this action, multiple operations need to be performed iteratively.
1. 首先,需要检索第一个 parameter 的 default value。

2. 然后,第二个 parameter 的 default value 需要从第一个 parameter 的值派生。

3. 最后,第三个 parameter 的选项需要从第二个 parameter 的值派生。

1. First, the default value for the first parameter needs to be retrieved.
2. Then, the second parameter's default value needs to be derived from the first parameter value.
3. Finally, the options for the third parameter need to be derived from the second parameter value.
在配置 action parameters 时,建议尽可能保持依赖层次结构的扁平化。在上述 action 的背景下,如果在第三个 parameter 的 object set 定义中引用第一个 parameter 而不是第二个 parameter,则可以并行派生第二个和第三个 parameter 所需的信息,从而减少从打开表单到表单完全可交互之间的总延迟。

When configuring action parameters, it is recommended to keep the dependency hierarchy as flat as possible. In the context of the action described above, referencing the first parameter instead of the second parameter in the third parameter's object set definition would allow the necessary information for the second and third parameter to be derived in parallel, reducing the total latency between opening the form and the form being fully interactive.