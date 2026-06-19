<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-permissioning/overview/
---
# Object permissioning
Foundry Ontology 允许对所有 ontology entities 进行细粒度、强大且灵活的安全控制。这些 entities 包括 [object types](/docs/foundry/object-link-types/object-types-overview/)、[link types](/docs/foundry/object-link-types/link-types-overview/) 和 [action types](/docs/foundry/action-types/overview/)，以及 [objects and links](#objects-and-links)（即实际的数据）。

The Foundry Ontology allows for granular, robust, and flexible security controls for all ontology entities. These entities include [object types](/docs/foundry/object-link-types/object-types-overview/), [link types](/docs/foundry/object-link-types/link-types-overview/), and [action types](/docs/foundry/action-types/overview/), as well as [objects and links](#objects-and-links) (the data itself).
我们可以将 Ontology 的授权结构概念化为两个层次：ontology resources，以及 objects and links。

We can conceptualize the Ontology's authorization structure on these two levels: ontology resources, and objects and links.
## Ontology resources
Ontology resources（例如 object types、link types 和 action types）定义了 ontology 的 schema。例如，一个 object type 可能包括 display name、property names、property data types 和 description。这些 resources 并不涉及实际的 property 值或 primary key 值；实际的 property 值和 primary key 值包含在 objects and links 中。

Ontology resources such as object types, link types, and action types define the schema of the ontology. For example, an object type may include display name, property names, property data types, and description. These resources do not refer to the actual property values or primary key values; the actual property values and primary key values are contained in the objects and links.
[详细了解 ontology resources 的权限。](/docs/foundry/object-permissioning/ontology-permissions/)

[Learn more about permissions for ontology resources.](/docs/foundry/object-permissioning/ontology-permissions/)
## Objects and links
Objects and links 是 Ontology 中的数据，包含实际的 primary key 和 property 值。例如，一个 Airplane object type 可以拥有一个 object，其 `Plane ID` property 的值为 `my_plane_id1`，`Maximum Occupancy` property 的值为 `240`。

Objects and links are the data in the Ontology, with actual primary key and property values. For example, an Airplane object type can have an object with a `Plane ID` property having the value `my_plane_id1`, and a `Maximum Occupancy` property having value `240`.
[详细了解 objects and links 的权限。](/docs/foundry/object-permissioning/managing-object-security/)

[Learn more about permissions for objects and links.](/docs/foundry/object-permissioning/managing-object-security/)