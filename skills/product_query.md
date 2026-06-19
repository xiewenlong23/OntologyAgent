---
name: product_query
description: Query product information from the ontology
type: query
triggers:
  - intent: "查询商品"
  - intent: "搜索产品"
  - intent: "查找商品信息"
---

# Product Query Skill

When the user wants to query product information, follow these steps:

1. Use `entity_search` tool with `object_type: "product"`
2. Apply any filters provided by the user (category, price range, etc.)
3. Return the results in a readable format with key product details.

## Parameters
- `object_type`: Always set to "product"
- `filters`: Any property filters (category, brand, price_min, price_max)
- `limit`: Maximum number of results (default 20)
