<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/compare-object-sets/
---
# Compare object sets
Comparison Views 为用户提供了比较两个已过滤对象集的选项。这些对象可以来自对象的动态过滤，也可以来自之前保存的 explorations。

Comparison Views provide users with the option to compare two filtered object sets. The objects may be derived from dynamic filtering of objects or from explorations saved previously.
## Entering Comparison Mode
要使用 Comparison Mode：

To use Comparison Mode:
* 进入 Object Explorer，打开一个 object type，并将其过滤到您想要比较的该类型的对象集。在下面的示例中，我们已过滤为离开纽约市的航班。

* 选择搜索栏下方的 **Compare** 按钮。选择 **Compare** 后，您可以选择一个比较对象集，例如：

* 一个现有的已保存 exploration，

* 给定类型的所有对象（例如 **All Flights**），或
* 您可以定义一个新的对象集进行比较。

* Go to Object Explorer, open an object type, and filter down to the set of objects of that type you want to compare. In the example below, we’ve filtered to flights leaving New York City.
* Select the **Compare** button below the search bar. After selecting **Compare**, you can choose a comparison set of objects, for instance:
* An existing saved exploration,
* All objects of the given type (such as **All Flights**), or
* You can define a new set of objects for comparison.
下面，我们正在将来自纽约市的航班与一个针对所有从加利福尼亚起飞的航班的现有 exploration 进行比较。

Below, we are comparing flights from New York City to an existing exploration for all flights departing California.
![Enter Comparison View](/docs/resources/foundry/object-explorer/comparison_enter.png)
要即时定义一个新的对象集进行比较（此过程称为 "dynamic filtering"），请选择 **Create new set of Flights**，如上图比较下拉菜单中所示。

To define a new object set on-the-fly for comparison (a process known as "dynamic filtering"), select **Create new set of Flights** as seen in the comparison dropdown in the image above.
这将打开一个视图，允许我们定义和编辑对象集，或更改用于比较集的颜色：

This brings up a view that allows us to define and edit the object set, or change the color used for the comparison set:
![Comparison Dynamic Filtering](/docs/resources/foundry/object-explorer/comparison_dynamic.png)
一旦进入 comparison mode，布局中的所有图表将更改为并排显示来自每个比较集的结果。这使我们能够查看事物的比较情况，例如来自纽约市与加利福尼亚的航班的最常见到达机场，或飞机注册号。OE 的所有功能在此比较视图中都得以保留，例如使用图表进行过滤的能力、查看表格视图中的结果的能力、actions、export 等等。

Once you enter the comparison mode, all of the charts in the layout will change to show the results from each of the compared sets side-by-side. This allows us to see how things compare, such as the most common arrival airports for flights from NYC versus CA, or aircraft registrations. All the functionality of OE is retained in this comparison view, for instance the ability to filter using the charts, the ability to see the results in the table view, actions, export, and so on.
![Comparison Generic](/docs/resources/foundry/object-explorer/comparison_generic.png)
## Filtering
如上所述，您可以联合应用这些比较集上的 filters 来缩小 comparison view 的范围。例如，您可能只想在比较中查看 A321 飞机上的航班，以便查看纽约的取消航班与加利福尼亚的取消航班的对比。这可以像在 OE 中通常做的那样，通过从搜索栏应用 filter（如下所示）或直接从图表应用来完成。

As mentioned above, you can jointly apply filters on these compared sets to narrow down the comparison view. For example, you may only want to see flights on an A321 airplane in the comparison in order to see how New York’s cancelled flights compare to those from California. This can be done in the same way as you normally would in OE by applying the filter from the search bar (as shown below) or directly from the chart.
![Comparison Filtering](/docs/resources/foundry/object-explorer/comparison_filter.png)
## Collaboration
### Saving Comparison Views
这些 Comparison Views 可以像 Explorations 一样通过单击右上角的 **Save** 按钮进行保存和共享。保存视图时，系统将提示您输入名称，您还可以提供可选的描述和/或自定义保存位置。

These Comparison Views can be saved and shared just like Explorations by clicking the **Save** button in the top-right. When saving the view, you will be prompted for a name, and you can also provide an optional description and/or a custom save location.

> 📷 **[图片: Save Comparison]**

> 📷 **[图片: Save Comparison]**

### Sharing Comparison Views
要共享您的 comparison，只需选择 **Save** 按钮左侧的 **Share** 按钮。系统将提示您决定要与哪些用户或组共享此 comparison、您要授予他们的访问级别，以及是否希望 comparison 为所有用户拥有默认角色。共享您的 comparison 不会共享对链接的 explorations 和/或底层对象的访问权限，因此任何给定的查看者除了需要具有对已保存 comparison 本身的访问权限外，还需要具有对数据的适当角色。

To share your comparison, simply select the **Share** button to the left of the **Save** button. You will be prompted to decide which users or groups you want to share this comparison with, what access level you want to grant them, and whether you want the comparison to have a default role for all users. Sharing your comparison will not share access to the linked explorations and/or underlying objects, so any given viewer will need to have the appropriate role for the data in addition to having access to the saved comparison itself.
### Searching for Comparison Views
这些已保存的 Comparisons 可以使用主页上的主 OE 搜索栏进行搜索。

These saved Comparisons can be searched for using the main OE search bar on the home page.
![Comparison Search Results](/docs/resources/foundry/object-explorer/comparison_search_result.png)