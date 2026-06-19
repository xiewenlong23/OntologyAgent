<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-edits/permission-checks/
---
# Permission checks when applying an Action
应用 Action 时的权限检查取决于您是在编辑 [single-datasource object](#edits-of-single-datasource-objects) 还是 [multi-datasource object](#edits-of-multi-datasource-objects)。

The permission checks when applying an Action depend on whether you are editing a [single-datasource object](#edits-of-single-datasource-objects) or a [multi-datasource object](#edits-of-multi-datasource-objects).
## Edits of single-datasource objects
如果 object type 由单个 datasource 支持，则只要满足以下条件，Action 就允许用户编辑 object：

If an object type is backed by a single datasource, Actions allow a user to edit an object as long as:
* 用户可以查看/加载 object（有关详细信息，请参阅 [Object Permissioning](/docs/foundry/object-permissioning/overview/) 部分），**并且**

* 用户通过 action 中定义的 [submission criteria](/docs/foundry/action-types/submission-criteria/#submission-criteria)。

* The user can view/load the object (see the [Object Permissioning](/docs/foundry/object-permissioning/overview/) section for details), **and**
* The user passes [submission criteria](/docs/foundry/action-types/submission-criteria/#submission-criteria) defined in the action.
创建新 object 时，用户必须能够查看 object type 的输入 datasource；如果用户无权访问输入 datasource，则 Action 运行将失败。

When creating new objects, the user must be able to view the input datasource of the object type; the Action run will fail if the user does not have access to the input datasource.
## Edits of multi-datasource objects
Object type 可以具有来自 [多个 datasource](/docs/foundry/object-permissioning/multi-datasource-objects/) 的 property。在这种情况下，用户对给定 object 可以具有不同级别的访问权限，如下所示：

Object types can have properties that come from [more than one datasource](/docs/foundry/object-permissioning/multi-datasource-objects/). In these cases, users can have varying levels of access on a given object, as follows:
* 用户可以查看整个 object；例如，用户可以访问所有 datasource 以及这些 datasource 中的所有行。

* 用户可以查看 datasource 的子集；例如，用户可以访问某些 datasource 中的所有行，而其他 datasource 中的行则无权访问。

* 用户可以在 datasource 子集中查看行的子集；例如，用户可以对某些行访问完整的 object，对某些行访问部分 object，对剩余行则无法访问 object。

* User can view the entire object; for example, the user may have access to all datasources as well as all rows in these datasources.
* User can view a subset of datasources; for example, the user may have access to all rows in some datasources and none of the rows in the other datasources.
* User can view a subset of rows in subset of datasources; for example, the user may have access to the full object for some rows, partial access to objects for some rows, and no access to objects for the remaining rows.
如果 object type 有多个 datasource，则应用 Action 时的权限检查更为复杂，因为强制执行约束以确保用户必须能够查看整个 object 才能编辑它（与 single-datasource object 一样）可能非常具有限制性。

If an object type has multiple datasources, the permission checks when applying an Action are more complicated, since enforcing constraints to ensure that the user must be able to view the entire object to edit it (as with single-datasource objects) can be very restrictive.
以下权限规则针对可应用于 object 的不同类型的 Action 实施。

The following permission rules are implemented for different kinds of Actions that can be applied to an object.
### Create object
> Scenario: The given object exists in datasources `D[i..k, m..n]`. The user is creating the object by setting values for properties only in `D[i..k]`.
除非用户可以查看 `D[i..k]` 的 backing datasource，否则不允许创建 object。对 `D[m..n]` 不检查任何权限。`D[m..n]` 的值默认为 `null`。

The user is not allowed to create the object unless they can view the backing datasource of `D[i..k]`. No permission is checked on `D[m..n]`. The values of `D[m..n]` default to `null`.
如果 `D[i..k]` 中的任何一个在过去包含该对象（但现在已将对象标记为已删除），则用户必须拥有在所有 `D[i..k]` 中查看该行/对象的权限，才能重新创建该对象。

If any of `D[i..k]` contained the object in the past (but have the object marked as deleted now), the user must have permissions to see the row/object in all of `D[i..k]` in order to recreate the object.
### Edit or modify object
> Scenario: The object exists in datasources `D[i..k, m..n]`. The user is editing properties mapped to `D[i..k]`.
只要用户能够查看 `D[i..k]` 中属性的现有值，就允许编辑这些属性。映射到 `D[m..n]` 的属性不进行权限检查。

The user is allowed to edit properties provided they can view existing values of properties in `D[i..k]`. No permission is checked on properties mapped to `D[m..n]`.
`D[m..n]` 在校验期间将显示为 `null`。如果校验在使用 `null` 值的情况下通过，用户可以应用该 Action。

`D[m..n]` will show up as `null` during the validation. The user can apply the Action if the validations pass with the `null` values.
### Delete object
> Scenario: The object exists in datasources `D[i..k, m..n]`.
如果用户无法查看整个对象（即来自 `D[i..k, m..n]` 的所有属性），则不允许删除该对象。

The user is not allowed to delete the object if they cannot view the entire object (in other words, all the properties coming from `D[i..k, m..n]`).
### Create link
> Scenario: Object1 exists in datasources `D1[i..k]` and object2 exists in datasources `D2[m..n]`.
只要用户能够在任何数据源 `D1[i..k]` 和 `D2[m..n]` 中分别加载 object1 和 object2，就允许创建该 Link。不对单个属性或数据源进行权限检查。

The user is allowed to create the link as long as they can load both object1 and object2 in any of the datasources `D1[i..k]` and `D2[m..n]`, respectively. No permission is checked on individual properties or datasources.
### Delete link
> Scenario: Object1 exists in datasources `D1[i..k]` and object2 exists in datasources `D2[m..n]`.
只要用户能够在任何数据源 `D1[i..k]` 和 `D2[m..n]` 中分别加载 object1 和 object2，就允许删除该 Link。不对单个属性或数据源进行权限检查。

The user is allowed to delete the link as long as they can load both object1 and object2 in any of the datasources `D1[i..k]` and `D2[m..n]`, respectively. No permission is checked on individual properties or datasources.