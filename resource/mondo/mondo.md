---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: nicolevasilevsky
  label: Nicole Vasilevsky
  orcid: 0000-0001-5208-3432
- category: Individual
  contact_details:
  - contact_type: github
    value: sabrinatoro
  label: Sabrina Toro
  orcid: 0000-0002-4142-7153
description: "The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions\
  \ across the world. The name Mondo comes from the Latin word \u2018mundus\u2019\
  \ and means \u2018for the world.\u2019"
domains:
- health
homepage_url: https://mondo.monarchinitiative.org/
id: mondo
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Mondo Disease Ontology
products:
- category: DataModelProduct
  description: OWL release of MONDO. The Complete ontology with merged imports.
  format: owl
  id: mondo.owl
  name: Mondo Disease Ontology OWL release
  original_source:
  - mondo
  product_url: https://purl.obolibrary.org/obo/mondo.owl
  secondary_source:
  - mondo
- category: DataModelProduct
  description: OBO release of MONDO.
  format: obo
  id: mondo.obo
  name: Mondo Disease Ontology OBO release
  original_source:
  - mondo
  product_url: https://purl.obolibrary.org/obo/mondo.obo
  secondary_source:
  - mondo
- category: DataModelProduct
  description: JSON release of MONDO (obograph json).
  format: json
  id: mondo.json
  name: Mondo Disease Ontology JSON release
  original_source:
  - mondo
  product_url: https://purl.obolibrary.org/obo/mondo.json
  secondary_source:
  - mondo
- category: ProcessProduct
  description: Utility code for supporting the operations of the Human Disease Ontology
  id: do.code.utils
  name: DO.utils
  original_source:
  - do
  product_url: https://github.com/DiseaseOntology/DO.utils
  secondary_source:
  - do
- category: MappingProduct
  description: MONDO SSSOM. Mappings from MONDO identifiers to other namespaces.
  format: sssom
  id: mondo.sssom
  name: MONDO SSSOM
  original_source:
  - do
  - hp
  - hgnc
  product_url: https://raw.githubusercontent.com/monarch-initiative/mondo/refs/heads/master/src/ontology/mappings/mondo.sssom.tsv
  secondary_source:
  - mondo
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.7
  format: kgx
  id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.7.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.7
  format: kgx
  id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.7.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Nodes for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.nodes
  name: Drug Approvals KP Graph Nodes
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_nodes_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
- category: GraphProduct
  description: Edges for the Drug Approvals KP, v0.3.9
  format: kgx
  id: drug-approvals-kp.graph.edges
  name: Drug Approvals KP Graph Edges
  original_source:
  - chebi
  - do
  - hp
  - mondo
  product_url: https://db.systemsbiology.net/gestalt/KG/drug_approvals_kg_edges_v0.3.9.tsv
  secondary_source:
  - drug-approvals-kp
repository: https://github.com/DiseaseOntology/HumanDiseaseOntology
---
MONDO Disease Ontology