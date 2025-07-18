---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@uniprot.org
  label: UniProt Consortium
description: UniProt Protein Knowledge Base
domains:
- biological systems
- proteomics
- biomedical
homepage_url: https://www.uniprot.org/
id: uniprot
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: uniprot
products:
- category: GraphProduct
  compression: targz
  description: UniProt proteins from microbes, as graph nodes and edges
  format: kgx
  id: kg-microbe.graph.uniprot
  name: KG-Microbe UniProt microbe transform
  original_source:
  - uniprot
  product_url: https://kghub.io/kg-microbe/KGMicrobe-transformed-uniprot-microbes-20240924.tar.gz
  secondary_source:
  - kg-microbe
- category: Product
  compression: gzip
  description: The Reviewed (Swiss-Prot) section of UniProt proteins
  format: kgx
  id: uniprot.swissprot.xml
  name: Reviewed (Swiss-Prot) XML
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Reviewed (Swiss-Prot) section of UniProt proteins
  format: fasta
  id: uniprot.swissprot.fasta
  name: Reviewed (Swiss-Prot) FASTA
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Unreviewed (TrEMBL) section of UniProt proteins
  format: xml
  id: uniprot.trembl.xml
  name: Unreviewed (TrEMBL) XML
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.xml.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Unreviewed (TrEMBL) section of UniProt proteins
  format: fasta
  id: uniprot.trembl.fasta
  name: Unreviewed (TrEMBL) FASTA
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
  secondary_source:
  - uniprot
- category: Product
  description: Tab-delimited file of systematic ID, primary gene name (where assigned),
    chromosome, product description, UniProtKB accession, all synonyms, and product
    type (protein coding, ncRNA, etc.) for each gene
  format: tsv
  id: pombase.genes-products
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase gene names and products
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv
  secondary_source:
  - pombase
- category: MappingProduct
  description: Tab-delimited file with the PomBase systematic identifier for each
    protein-coding gene mapped to the corresponding UniProt accession number
  format: tsv
  id: pombase.to-uniprot
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase to UniProt map
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/PomBase2UniProt.tsv
  secondary_source:
  - pombase
- category: MappingProduct
  description: Mapping between chembl_35 target chembl_ids and UniProt accessions
  id: chembl.map_to_uniprot
  is_public: true
  name: ChEMBL map to UniProt
  original_source:
  - chembl
  - uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
  secondary_source:
  - chembl
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to UniProt accession numbers
  format: tsv
  id: oma.mapping.uniprot
  name: OMA to UniProt Mapping
  original_source:
  - oma
  - uniprot
  product_url: https://omabrowser.org/oma/current/oma-uniprot.txt.gz
  secondary_source:
  - oma
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - medline
  - mesh
  - pid
  - do
  - diseases
  - drugcentral
  - go
  - gwas-catalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - clingen
  - clinvar
  - mgd
  - rgd
  - orphanet
  - psygenet
  - uniprot
  - disgenet
  - hp
  - gwascat
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
- category: MappingProduct
  compression: gzip
  description: Gene to RefSeq/UniProtKB collaboration data providing cross-references
    between gene records and protein databases
  format: tsv
  id: ncbigene.gene_refseq_uniprotkb_collab
  name: Gene RefSeq UniProtKB Collaboration Data
  original_source:
  - refseq
  - ncbigene
  - uniprot
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene_refseq_uniprotkb_collab.gz
repository: https://www.uniprot.org/help/downloads
---
UniProt Protein Knowledge Base