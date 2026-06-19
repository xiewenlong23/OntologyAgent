<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-views/config-profiles/
---
# Configure profiles
**Profiles（配置文件）** 使您能够配置应如何向具有不同角色的用户展示 Object View。您可以使用 profiles 来控制 Object View [tabs](/docs/foundry/object-views/config-tabs/) 对不同用户的可见性,使其看到满足其特定需求的视图。

**Profiles** enable you to configure how Object Views should be surfaced to users with different roles. You can use profiles to control the visibility of Object View [tabs](/docs/foundry/object-views/config-tabs/) for different users so they see views specific to their needs.
### Configure a profile
Object Explorer 由名为 `Hubble` 的服务提供支持。要在 Object View 中将某个 group 用作 profile,请在 Platform Settings 的 [**Groups** tab](/docs/foundry/security/users-and-groups/) 中添加以下 Hubble 属性：

Object Explorer is powered by a service called `Hubble`. To use a group as a profile in Object View, add the following Hubble attributes from within the [**Groups** tab](/docs/foundry/security/users-and-groups/) in Platform Settings:
* `hubble:isProfile` : `true`
* `hubble:displayName` : `Set a name you want end user to see`
* \[OPTIONAL] `hubble:isDiscoverable` : `true`
* 将 `hubble:isDiscoverable` 属性设置为 `true` 将使 profile 对非该 group 成员的用户可见。省略此属性意味着只有 group 中的用户才能访问分配给此特定 profile 的视图。

* `hubble:isProfile` : `true`
* `hubble:displayName` : `Set a name you want end user to see`
* \[OPTIONAL] `hubble:isDiscoverable` : `true`
* Setting the `hubble:isDiscoverable` attribute to `true` will make the profile visible to users who are not members of the group itself. Omitting this attribute means that only users who are in the group can access views assigned to this specific profile.
> **ℹ️ 注意**

> 新创建的 profile 可能需要最多五分钟才能在 Object View 编辑器中可用。
> **ℹ️ 注意**

> Newly-created profiles may take up to five minutes to become available in the Object View editor.

> 📷 **[图片: 配置 Object View profile]**

> 📷 **[图片: Configure Object View profile]**

### Assign a profile to an Object View
Profile 是在 tab 级别进行分配的,这意味着对于每个 tab,您都可以分配特定的 profile。要向 tab 添加 profile,请访问编辑器侧边栏,点击 **Tab** 设置中的某个 tab,选择 **Visibility**,然后点击 **Add a profile**。

Profiles are assigned on a tab level, meaning that for each tab you can assign specific profiles. To add a profile to a tab, access the editor sidebar, click on a tab in the **Tab** settings, select **Visibility**, and click **Add a profile**.
![Add a profile to Object View tab](/docs/resources/foundry/object-views/add-profile-to-object-view-tab.png)
### Switch profiles as a user
将 profile 添加到 Object View 后,您可以在不同 profile 之间切换。在 Object View 头部选择 profile 类型以访问包含可用 profile 的下拉菜单。您也可以通过点击 Object View 顶部的 **Viewing Object As:** 来找到相同的下拉菜单。

Once you add a profile to an Object View, you can switch between profiles. Select the profile type in the Object View header to access a dropdown menu containing available profiles. You can find the same dropdown menu by clicking **Viewing Object As:** at the top of the Object View.
![switch profile view in Object View](/docs/resources/foundry/object-views/switch-object-view-profiles.png)
### Switch profiles as an editor
您还可以在编辑 Object View 时访问不同的 profile。这样做将使您能够查看每个 profile 可见的 tabs。

You can also access different profiles when editing an Object View. Doing so will allow you to see which tabs are visible to each profile.
![switch profile view as an editor in Object View](/docs/resources/foundry/object-views/switch-profile-view-editor.png)
### Set a default profile for a user
要为用户或用户组设置默认 profile,请将他们作为成员添加到支撑该 profile 的 group 中。仅当用户是单个 profile 的成员时,此操作才会生效。

To set a default profile for a user or user group, add them as a member to the group backing the profile. This action will work only if a user is a member of a single profile.
> **ℹ️ 注意**

> 每个 Object View 最多可以添加十个 profiles。
> **ℹ️ 注意**

> You can add a maximum of ten profiles to each Object View.