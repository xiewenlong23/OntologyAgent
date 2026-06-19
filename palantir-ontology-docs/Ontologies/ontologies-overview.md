<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/ontologies/ontologies-overview/
---
# Ontologies
Ontology 是一种存储 Ontology resources 或 entities 的 artifact，包括以下内容：

An ontology is an artifact which stores ontological resources or entities, including the following:
* [Object types](/docs/foundry/object-link-types/object-types-overview/)
* [Link types](/docs/foundry/object-link-types/link-types-overview/)
* [Action types](/docs/foundry/action-types/overview/)
* [Interfaces](/docs/foundry/interfaces/interface-overview/)
* [Shared properties](/docs/foundry/object-link-types/shared-property-overview/)
* [Object type groups](/docs/foundry/object-link-types/type-groups/)
* [Object types](/docs/foundry/object-link-types/object-types-overview/)
* [Link types](/docs/foundry/object-link-types/link-types-overview/)
* [Action types](/docs/foundry/action-types/overview/)
* [Interfaces](/docs/foundry/interfaces/interface-overview/)
* [Shared properties](/docs/foundry/object-link-types/shared-property-overview/)
* [Object type groups](/docs/foundry/object-link-types/type-groups/)
我们将这些 resources 称为 **Ontology resources**。Ontology 可以是私有的，并分配给单个 [organization](/docs/foundry/security/orgs-and-spaces/)，也可以在多个 organizations 之间共享。共享的 ontology 允许不同 organization 的用户安全地共享数据和 workflow。将 entities 分组到 ontology 中可确保只有指定 organization 的用户才能访问 Ontology entities。

We call these resources **Ontology resources**. An ontology can either be private and assigned to a single [organization](/docs/foundry/security/orgs-and-spaces/) or shared among multiple organizations. Shared ontologies allow users of different organizations to share data and workflows safely. Grouping entities in ontologies ensures that only users of the specified organizations can access ontological entities.
## Relation with spaces
Ontology 与 [space](/docs/foundry/security/orgs-and-spaces/#spaces) 以 1:1 的方式映射。当创建新 space 时，会同时创建一个具有相同名称的对应 ontology，并使用与该 space 相同的 organization [markings](/docs/foundry/security/markings/)。私有 space 将映射到私有 ontology，而共享 space 将映射到共享 ontology。

An ontology is mapped 1:1 with a [space](/docs/foundry/security/orgs-and-spaces/#spaces). When a new space is created, a corresponding ontology with the same name is simultaneously created with the same organization [markings](/docs/foundry/security/markings/) as the space. A private space will map to a private ontology, while a shared space will map to a shared ontology.