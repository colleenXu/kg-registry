---
activity_status: active
category: DataSource
contacts:
- category: Organization
  label: KEGG
description: The Kyoto Encyclopedia of Genes and Genomes (KEGG) is a database resource
  for understanding high-level functions and utilities of the biological system, such
  as the cell, the organism and the ecosystem, from molecular-level information, especially
  large-scale molecular datasets generated by genome sequencing and other high-throughput
  experimental technologies.
domains:
- biological systems
homepage_url: https://www.genome.jp/kegg/
id: kegg
layout: resource_detail
license:
  id: https://www.kegg.jp/feedback/copyright.html
  label: By request
name: KEGG
products:
- category: MappingProduct
  description: Rhea SSSOM
  format: sssom
  id: obo-db-ingest.rhea.sssom.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: Rhea SSSOM
  original_source:
  - rhea
  - reactome
  - kegg
  - metacyc
  - m-csa
  - ecocyc
  product_url: https://w3id.org/biopragmatics/resources/rhea/rhea.sssom.tsv
  secondary_source:
  - obo-db-ingest
- category: MappingProduct
  description: bigg.metabolite SSSOM
  format: sssom
  id: obo-db-ingest.bigg.metabolite.sssom.tsv
  license:
    id: http://bigg.ucsd.edu/license#license
    label: Custom
  name: bigg.metabolite SSSOM
  original_source:
  - chebi
  - bigg
  - biocyc
  - kegg
  - reactome
  product_url: https://w3id.org/biopragmatics/resources/bigg.metabolite/bigg.metabolite.sssom.tsv
  secondary_source:
  - obo-db-ingest
---
KEGG