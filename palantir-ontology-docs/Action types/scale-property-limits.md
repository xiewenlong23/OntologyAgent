<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/action-types/scale-property-limits/
---
# Scale and property limits
存在若干限制,以确保被编辑的 Object Type 能够快速处理 edit 并更新面向用户的数据,不会降低在线应用程序的运行速度。提交的 Action 如果超出这些限制,将无法成功,并会向用户显示错误消息。

Several limits are in place to ensure edited object types can quickly process edits and update user-facing data without slowing down live applications. Actions submitted that exceed these limits will not succeed and will display an error message to the user.
## Configuration limits
`Allow multiple values` 切换开关允许用户向参数传递值列表。

The `Allow multiple values` toggle allows users to pass in a list of values to a parameter.
| Limit                                                                   | Maximum |
| ----------------------------------------------------------------------- | ------- |
| Number of elements in a primitive list parameter                        | 10,000  |
| Number of elements in an object reference list parameter                | 1,000   |
| Number of elements in a list parameter when used in submission criteria | 1,000   |
## Edit limits
| Limit                                                                 | Maximum                 |
| --------------------------------------------------------------------- | ----------------------- |
| Number of **object types** you can edit in a single action submission | 50                      |
| Number of **objects** you can edit in a single action submission      | 10,000                  |
| Each individual edit of an **object** in an action submission         | 32KB (OSv1), 3MB (OSv2) |
## Batch call limits
一个 Action 在一个批次中最多可被调用 10,000 次。当 Action 是 function-backed 且该 Function 未配置为使用 [batched execution](/docs/foundry/action-types/function-actions-batched-execution/) 时,此限制将降低至 20。

An action can be called a maximum of 10,000 times in a batch. This limit is reduced to 20 when the action is function-backed and the function is not configured to use [batched execution](/docs/foundry/action-types/function-actions-batched-execution/).
在执行 [edit limits](#edit-limits) 强制检查时,批处理 Action 调用中应用的 edit 视为单个组,无论批处理中的哪个请求导致了这些 edit。

The edits applied in a batched action call are treated as a single group when enforcing [edit limits](#edit-limits), regardless of which request in the batch was the cause of the edits.
附加限制可能适用,具体取决于调用应用程序。

Additional limits may apply, depending on the calling application.
## Supported property types
以下是受支持的单一和数组 Property 类型的规范。请注意,某些 Property 类型仅由对象存储 v2 (OSv2) 支持。

Below are specifications for supported single and array property types. Note that some property types are only supported by object storage v2 (OSv2).
### Single property types
| Property type | Parameter type | Supported |
| ------------- | -------------- | --------- |
| Attachment | Attachment | Yes |
| Boolean | Boolean | Yes |
| Byte | Integer | Yes |
| Cipher text | String | Yes |
| Date | Date | Yes |
| Decimal | Decimal | Yes |
| Double | Double | Yes |
| Float | Double | Yes |
| Geopoint | Geopoint | Yes |
| Geoshape | Geoshape | Yes |
| Geotime series reference | Geotime series reference | Yes (OSv2 only) |
| Integer | Integer | Yes |
| Long | Long | Yes |
| Mandatory control | - | Not supported as a property or in actions |
| Media reference | Media reference | Yes (OSv2 only) |
| String | String | Yes |
| Short | Integer | Yes |
| Struct | Struct | Yes (OSv2 only) |
| Timestamp | Timestamp | Yes |
| Time series reference | Time series reference | Yes (OSv2 only) |
| Vector | Double list | Yes (OSv2 only) |
### Array property types
| Array property type | List parameter type | Supported |
| ------------- | ------------------- | --------- |
| Attachment | Attachment | Yes |
| Boolean | Boolean | Yes |
| Byte | Integer | Yes |
| Cipher text | String | Yes |
| Date | Date | Yes |
| Decimal | Decimal | Yes |
| Double | Double | Yes |
| Float | Double | Yes |
| Geopoint | Geopoint | Yes |
| Geoshape | Geoshape | Yes |
| Geotime series reference | Geotime series reference | Yes (OSv2 only) |
| Integer | Integer | Yes |
| Long | Long | Yes |
| Mandatory control | Mandatory control | Yes |
| Media reference | - | Not supported in actions |
| String | String | Yes |
| Short | Integer | Yes |
| Struct | Struct | Yes (OSv2 only) |
| Timestamp | Timestamp | Yes |
| Time series reference | - | Not supported as a property or in actions |
| Vector | - | Not supported as a property or in actions |
## Supported properties
目前,无法使用 Action 来编辑 Object 的 **primary key**。修改 primary key 等同于删除一个 Object 然后再添加一个新的 Object;您可以使用 [rules](/docs/foundry/action-types/rules/#ontology-rules) 直接创建或删除 Object,而不是使用 Action 来编辑 primary key。

Currently, actions cannot be used to edit the **primary key** of an object. Modifying the primary key is equivalent to deleting an object and then adding a new object; instead of editing the primary key with an action, you can create or delete an object directly using [rules](/docs/foundry/action-types/rules/#ontology-rules).
## Notification recipients
使用 [side effect notifications](/docs/foundry/action-types/notifications/) 时,单个 Action 中最多可以通知 500 个收件人。当通知内容以 "From a function" 方式渲染时,此限制将减少到 50 个收件人。有关生成通知时需要考虑的限制的更多信息,请参阅有关 [notifications 的最大收件人限制](/docs/foundry/action-types/notifications/#maximum-recipient-limits) 的文档。

When using [side effect notifications](/docs/foundry/action-types/notifications/), a maximum of 500 recipients can notified in a single action. This limit is reduced to fifty recipients when notifications content is rendered "From a function". For further information about limits to account for when generating notifications, see the documentation on [maximum recipient limits for notifications](/docs/foundry/action-types/notifications/#maximum-recipient-limits).