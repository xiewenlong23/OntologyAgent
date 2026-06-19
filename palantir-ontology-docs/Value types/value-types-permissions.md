<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-link-types/value-types-permissions/
---
# Value type permissions
Value types 的权限管理通过平台 [space](/docs/foundry/platform-security-management/manage-orgs-and-spaces/#spaces) 进行管理。space 中的任何 value types 都会自动导入并可用于关联的 ontology。其他使用者可以将 value types 导入到他们的项目范围中，类似于用户可以将 transforms profiles 或 inputs 导入到 pipelines 中的方式。

Permissioning for value types is managed through platform [space](/docs/foundry/platform-security-management/manage-orgs-and-spaces/#spaces). Any value types in a space are automatically imported and made available for the associated ontology. Other consumers can import the value types into their project scopes, similar to how users can import transforms profiles or inputs to pipelines.
对 space 具有 View（读取）权限的用户可以将 value types 分配给该 space 及关联 ontology 中的 property types 或 shared property types。space 的 Editor 或 Owner 可以在该 space 中创建、编辑或删除 value types。

Users who have View (read) permissions to a space can assign value types to property types or shared property types in that space and associated ontology. An Editor or Owner of a space can create, edit, or delete value types in that space.