<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontology/search-syntax/
---
# Search syntax
本页面描述了 Ontology 中不同类型搜索的语法。您可以在 Workshop 中使用 [filter list](/docs/foundry/workshop/widgets-filter-list/) 进行 Ontology 搜索,也可以从 [search bar](/docs/foundry/object-explorer/search-objects/) 使用 Object Explorer 进行搜索。

This page describes syntax for different kinds of searches in the Ontology. You can search in the Ontology from Workshop using the [filter list](/docs/foundry/workshop/widgets-filter-list/) or Object Explorer from the [search bar](/docs/foundry/object-explorer/search-objects/).
## Regular expression
Ontology 中的正则表达式 (regex) 搜索使用的语法与典型的正则表达式类似,但存在一些差异:

Regular expression (regex) search in the Ontology uses a syntax that is similar to typical regular expressions but with some differences:
* 字符串 Property 必须为正则表达式搜索建立索引。要在字符串 Property 上使用正则表达式搜索,该 Property 必须在 Ontology Manager 中为正则表达式搜索建立索引。要进行配置,请导航至 Object Type 的 **Properties** 标签页,然后选择 **Interaction** 标签页,接着选择 **Enable regex queries** 选项。

* 模式匹配整个值,而非子字符串。由于索引将完整字符串作为单个未分析的值进行存储,因此模式始终与整个字段值从头到尾进行匹配。这意味着搜索 `cat` 将仅匹配精确值 `cat`,而不会匹配包含该字符串的值,例如 `concatenate`。若要执行子字符串匹配,请在模式前后添加 `.*`,例如,`.*cat.*` 将匹配任何包含 `cat` 的值。
* 不支持 `^` 和 `$` 锚定符号。由于每次匹配已经隐式地从值的开头开始并在值的结尾结束,因此这些锚定符号是多余的。

* String properties must be indexed for regex search. To use regular expression search on a string property, the property must be indexed for regex search in Ontology Manager. To configure this, navigate to the **Properties** tab of your object type and select the **Interaction** tab, then choose the **Enable regex queries** option.
* Patterns match the full value, not substrings. Because the index stores the complete string as a single unanalyzed value, a pattern is always matched against the entire field value from start to end. This means searching for `cat` will only match the exact value `cat`, not values that contain it such as `concatenate`. To perform a substring match, add `.*` before and after your pattern, for example, `.*cat.*` would match any value containing `cat`.
* `^` and `$` anchors are not supported. Because every match already implicitly starts at the beginning and ends at the end of the value, these anchors are redundant.
### Supported operators
* `.` 匹配任意单个字符。

* 搜索 `c.t` 将匹配 `cat`、`cot`、`cut` 等。
* `?` 将前一个字符设置为可选(匹配零次或一次)。

* 搜索 `colou?r` 将同时匹配 `color` 和 `colour`。
* `+` 重复前一个字符一次或多次。

* 搜索 `go+d` 将匹配 `god`、`good`、`goood` 等,但不匹配 `gd`。
* `*` 重复前一个字符零次或多次。

* 搜索 `go*d` 将匹配 `gd`、`god`、`good`、`goood` 等。
* `{}` 定义前一个字符可以重复的最小和最大次数。`{2}` 表示前一个字符必须恰好重复两次,`{2,}` 表示前一个字符必须至少重复两次,`{2,4}` 表示前一个字符必须重复 2 到 4 次(含)。

* 搜索 `go{2}d` 将仅匹配 `good`。搜索 `go{2,4}d` 将匹配 `good`、`goood` 和 `gooood`。
* `|` 是 OR 运算符,允许您匹配一个模式或另一个模式。

* 搜索 `cat|dog` 将匹配 `cat` 或 `dog`。
* `()` 在表达式中形成一个组,以便运算符可以应用于整个组而不仅仅是前一个字符。

* 搜索 `(un)?happy` 将同时匹配 `happy` 和 `unhappy`,因为 `?` 使整个 `un` 组变为可选。
* `[]` 匹配方括号内列出的任意单个字符。

* 搜索 `gr[ae]y` 将同时匹配 `gray` 和 `grey`。您可以使用 `-` 来定义范围,因此 `[a-z]` 匹配任意小写字母,`[0-9]` 匹配任意数字,`[A-Za-z]` 匹配任意字母(不区分大小写)。如果序列以 `^` 开头,则该集合被取反,因此 `[^0-9]` 匹配任何非数字字符。如果 `-` 是第一个字符或使用 `\` 进行转义,则将其视为字面意义上的短横线。
* `"` 创建字符串字面量组,允许您匹配精确的短语,而不是将每个字符解释为正则表达式运算符。
* 搜索 `"v2.0"` 将匹配字面文本 `v2.0`。如果没有引号,`.` 将被视为通配符,可能会匹配 `v2X0` 或 `v200`。
* `\` 用作转义字符,允许您搜索那些本会被视为运算符的字符。它还提供简写的字符类:
* `\d` 匹配任意数字(`0`-`9`)。`\D` 匹配任何非数字字符(字母、标点符号、空格等)。

* `\s` 匹配任意空白字符,例如空格、Tab 符和换行符。`\S` 匹配任何非空白字符。
* `\w` 匹配任意单词字符(字母、数字和下划线:`a`-`z`、`A`-`Z`、`0`-`9`、`_`)。`\W` 匹配任何非单词字符,例如标点符号、空格等。

* 例如,搜索 `\d{3}-\d{4}` 将匹配 `555-1234` 或 `800-5678` 等模式。搜索 `\w+\s\w+` 将匹配任意由空格分隔的两个单词,例如 `hello world` 或 `John Smith`。要搜索字面意义上的点,请使用 `\`。例如,`example\.com` 将匹配 `example.com` 而不匹配 `exampleXcom`。

* `.` matches any single character.
* Searching for `c.t` would match `cat`, `cot`, `cut`, and so on.
* `?` makes the previous character optional (matches zero or one times).
* Searching for `colou?r` would match both `color` and `colour`.
* `+` repeats the previous character one or more times.
* Searching for `go+d` would match `god`, `good`, `goood`, and so on, but not `gd`.
* `*` repeats the previous character zero or more times.
* Searching for `go*d` would match `gd`, `god`, `good`, `goood`, and so on.
* `{}` defines the minimum and maximum number of times the preceding character can repeat. `{2}` means the previous character must repeat exactly twice, `{2,}` means the previous character must repeat at least twice, and `{2,4}` means the previous character must repeat between 2 and 4 times (inclusive).
* Searching for `go{2}d` would match only `good`. Searching for `go{2,4}d` would match `good`, `goood`, and `gooood`.
* `|` is the OR operator, allowing you to match one pattern or another.
* Searching for `cat|dog` would match either `cat` or `dog`.
* `()` forms a group within an expression so that operators can apply to the entire group rather than just the previous character.
* Searching for `(un)?happy` would match both `happy` and `unhappy`, because the `?` makes the entire `un` group optional.
* `[]` matches any single character listed inside the brackets.
* Searching for `gr[ae]y` would match both `gray` and `grey`. You can use `-` to define a range, so `[a-z]` matches any lowercase letter, `[0-9]` matches any digit, and `[A-Za-z]` matches any letter regardless of case. If the sequence begins with `^`, the set is negated, so `[^0-9]` matches any character that is not a digit. If `-` is the first character or escaped with `\`, it is treated as a literal dash.
* `"` creates groups of string literals, allowing you to match an exact phrase rather than interpreting each character as a regex operator.
* Searching for `"v2.0"` would match the literal text `v2.0`. Without the quotes, the `.` would be treated as a wildcard, potentially matching `v2X0` or `v200`.
* `\` is used as an escape character, allowing you to search for characters that would otherwise be treated as operators. It also provides shorthand character classes:
* `\d` matches any digit (`0`-`9`). `\D` matches any character that is not a digit (letters, punctuation, spaces, and so on).
* `\s` matches any whitespace character, such as spaces, tabs, and newlines. `\S` matches any character that is not whitespace.
* `\w` matches any word character (letters, digits, and underscores: `a`-`z`, `A`-`Z`, `0`-`9`, `_`). `\W` matches any character that is not a word character, such as punctuation, spaces, and so on.
* For example, searching for `\d{3}-\d{4}` would match patterns like `555-1234` or `800-5678`. Searching for `\w+\s\w+` would match any two words separated by a space, such as `hello world` or `John Smith`. To search for a literal dot, use `\.`. For example, `example\.com` would match `example.com` without matching `exampleXcom`.