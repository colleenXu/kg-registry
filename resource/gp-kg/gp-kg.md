---
layout: resource_detail
activity_status: active
id: gp-kg
name: GP-KG
description: A knowledge graph for drug repurposing
domains:
- health
contacts:
- category: Individual
  label: Rong Xu
  contact_details:
  - contact_type: email
    value: rxx@case.edu
homepage_url: http://nlp.case.edu/public/data/GPKG-Predict/
repository: http://nlp.case.edu/public/data/GPKG-Predict/
products:
- id: gp-kg.graph
  name: GP-KG
  description: GP_KG.txt
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  category: GraphProduct
  node_count: 61146
  edge_count: 1246726
  secondary_source:
  - gp-kg
  original_source:
  - gp-kg
- id: gp-kg.process.kg-predict
  name: KG-Predict
  description: A computational framework for drug repurposing, used with GP-KG
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/code/
  category: ProcessProduct
  secondary_source:
  - gp-kg
  original_source:
  - gp-kg
publications:
- authors:
  - Gao Z
  - Ding P
  - Xu R
  doi: doi:10.1016/j.jbi.2022.104133
  id: doi:10.1016/j.jbi.2022.104133
  title: 'KG-Predict: A knowledge graph computational framework for drug repurposing'
  year: '2022'
category: KnowledgeGraph
---

GP-KG
