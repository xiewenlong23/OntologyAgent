<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/configure-sections/
---
# Configure sections
action form 可以使用 **sections** 进行自定义。这些 sections 提供 parameters 的逻辑分组，以组织 action form。Sections 还支持 columns、descriptions 和 conditional overrides。

The action form can be customized with **sections**. These sections provide a logical grouping of parameters to organize an action form. Sections also support columns, descriptions, and conditional overrides.

> 📷 **[图片: form overview]**

> 📷 **[图片: form overview]**

## Adding a section to an action form
在 Form 选项卡中，单击 **Add section**。这将打开一个详细的 section configuration modal，您可以在其中添加 title、选择 column 布局，并可选择地编写面向用户的 description。该 description 没有样式，并且与 parameter descriptions 不同，它将始终显示在 section 本身中，而不是在 tooltip 中。

In the Form tab, click **Add section**. This will open a detailed section configuration modal where you can add a title, choose a column layout, and optionally write a user-facing description. The description is not stylized and, unlike parameter descriptions, will always be shown in the section itself, not in a tooltip.
您可以将 parameters 组织在 columns 中，以更好地利用 form 中的空间或将相关的 parameters 组合在一起。一个 section 可以分为一个或两个 columns。当您使用在 form 中不需要太多空间的 parameters 时，分开的 columns 特别有用。

You can organize parameters in columns to make better use of the space within a form or to group related parameters closer together. A section can be divided into one or two columns. Separate columns are especially useful when you use parameters that don’t require a lot of space within the form.

> 📷 **[图片: section inside a form]**

> 📷 **[图片: section inside a form]**

Section 也是可折叠的,可以完全隐藏,并且可以使用 conditional overrides,为您提供更多自定义 form 行为的方式。所有这些 features 也会应用到 section 内部的参数上。结合使用这些 features,可以构建更智能的 forms,在适当的场景下呈现所需的参数。Section 可以在初始时隐藏,仅根据先前的参数显示。

Sections are also collapsible, can be hidden entirely, and can make use of conditional overrides, giving you more ways to customize the form behavior. All of the features will also apply to the parameters inside of the section. Using these features in combination allow for smarter forms which present required parameters under the appropriate circumstances. A section can be hidden at first and only shown based on a prior parameter.
## Adding parameters to a section
有两种方式可以将参数添加到 section 中:从 section configuration view 内部,或从 **Form** tab 内部。

There are two ways to add a parameter to a section: from within the section configuration view, or from within the **Form** tab.
在 section configuration view 中,点击 **Add new parameter**。在这里,在 section 内配置新添加的参数。或者,点击 **Add existing parameter** 将现有参数移动到 section 中。

In the section configuration view, click **Add new parameter**. From here, configure the newly added parameter inside the section. Alternatively, click **Add existing parameter** to move an existing parameter into the section.
**Form** tab 在单一概览中列出 section 及其参数。点击参数左侧的八个点,将其拖动到现有的 section 中。参数和 section 在 form 中的显示顺序基于它们在此 **Form Content** section 中的顺序。

The **Form** tab lists the sections with their parameters in a single overview. Click the eight dots on the left hand side of the parameter and drag it into an existing section. Parameters and sections display in the form based on their order in this **Form Content** section.