<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/map/actions/
---
# Actions
在 Map 应用中使用 [Actions](/docs/foundry/map/integrate-actions/) 根据在地图上绘制的点、多边形或线条来创建或编辑对象。

Use [Actions](/docs/foundry/map/integrate-actions/) in the Map application to create or edit objects based on points, polygons, or lines drawn on the map.
## Actions on shapes and points
当您在地图上右键单击时,菜单中的 **Actions** 条目会显示所有适用于地理空间点的 actions,如下所示。

When you right-click on the map, the **Actions** entry in the menu shows all actions that apply to geospatial points, as shown below.
![Right-click actions menu](/docs/resources/foundry/map/actions-right-click-menu.png)
在您 [绘制形状](/docs/foundry/map/shapes/) 后,工具栏中的 **Actions** 按钮会显示所有适用于您绘制的多边形、线条或点的 actions:

After you [draw a shape](/docs/foundry/map/shapes/), the **Actions** button in the toolbar shows all actions that apply to the polygons, lines, or points you drew:
![Actions menu from shape tools](/docs/resources/foundry/map/actions-shape-menu.png)
从这些菜单中选择一个 action 后,可能还需要提供其他参数。在这种情况下,Map 会显示一个对话框供您输入其他参数:

After selecting an action from one of these menus, there may be additional parameters that you need to provide. When this is the case, the Map shows a dialog for you to input the additional parameters:
![Dialog with actions form](/docs/resources/foundry/map/actions-dialog.png)
如果没有其他参数，或者您在对话框中提交表单后，Map 应用程序将执行该 action，并将 action 创建的所有地理空间对象添加到您的地图中。

If there are no additional parameters, or after you submit the form in the dialog, the Map application executes the action and will add any geospatial objects created by the action to your map.
## Actions on Ontology objects
使用 **Selection** 面板中的 **Actions** 按钮对所选对象执行地理空间 action。选择一个 action 后，系统将根据该 action 中指定的配置提示您编辑或创建形状。

Use the **Actions** button in the **Selection** panel to execute geospatial actions on your selected object. After selecting an action, you will be prompted to edit or create a shape, depending on the configuration specified in the action.
![Apply action with shape update](/docs/resources/foundry/map/actions-update-shape.gif)
当您在形状绘制或编辑工具上单击 **Done** 时，可能还需要提供其他参数。在这种情况下，Map 会显示一个对话框，供您输入其他参数：

When you click **Done** on the shape drawing or editing tools, there may be additional parameters that you need to provide. When this is the case, the Map shows a dialog for you to input the additional parameters:
![Dialog with actions form](/docs/resources/foundry/map/actions-dialog.png)
如果没有其他参数，或者您在对话框中提交表单后，Map 应用程序将执行该 action，并更新您的地图以反映 action 创建或修改的所有对象。

If there are no additional parameters, or after you submit the form in the dialog, the Map application executes the action and will update your map to reflect any objects created or modified by the action.