---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: amos.bairoch@sib.swiss
  label: Amos Bairoch
  orcid: 0000-0002-2261-7130
- category: Organization
  contact_details:
  - contact_type: url
    value: https://web.expasy.org/groups/calipho/
  - contact_type: email
    value: cellosaurus@sib.swiss
  label: CALIPHO Group - SIB Swiss Institute of Bioinformatics
description: Cellosaurus is a knowledge resource on cell lines providing information on cell lines from vertebrates, invertebrates, and plants, including standardized nomenclature, cross-references to other databases, and information on problematic cell lines.
domains:
- biological systems
- health
homepage_url: https://www.cellosaurus.org/
id: cellosaurus
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Cellosaurus
products:
- category: GraphicalInterface
  description: Web interface for searching and exploring Cellosaurus data
  id: cellosaurus.site
  name: Cellosaurus Web Interface
  original_source:
  - cellosaurus
  product_url: https://www.cellosaurus.org/
  secondary_source:
  - cellosaurus
  is_public: true
- category: Product
  description: Complete Cellosaurus data in flat text format
  format: tsv
  id: cellosaurus.txt
  name: Cellosaurus Text
  original_source:
  - cellosaurus
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus.txt
  secondary_source:
  - cellosaurus
- category: Product
  description: Cellosaurus data in XML format
  format: xml
  id: cellosaurus.xml
  name: Cellosaurus XML
  original_source:
  - cellosaurus
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus.xml
  secondary_source:
  - cellosaurus
- category: MappingProduct
  description: Cellosaurus cross-references in tab-delimited format
  format: tsv
  id: cellosaurus.xrefs
  name: Cellosaurus Cross-references
  original_source:
  - cellosaurus
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus_xrefs.tsv
  secondary_source:
  - cellosaurus
- category: Product
  description: Complete Cellosaurus data in RDF format using the Turtle syntax
  format: ttl
  id: cellosaurus.rdf
  name: Cellosaurus RDF
  original_source:
  - cellosaurus
  product_url: https://ftp.expasy.org/databases/cellosaurus/cellosaurus.ttl
  secondary_source:
  - cellosaurus
- category: ProgrammingInterface
  description: RESTful API for programmatic access to Cellosaurus data
  id: cellosaurus.api.rest
  name: Cellosaurus API
  original_source:
  - cellosaurus
  product_url: https://api.cellosaurus.org/
  secondary_source:
  - cellosaurus
  is_public: true
- category: ProgrammingInterface
  description: SPARQL endpoint for querying Cellosaurus RDF data
  id: cellosaurus.api.sparql
  name: Cellosaurus SPARQL Endpoint
  original_source:
  - cellosaurus
  product_url: https://api.cellosaurus.org/sparql-editor
  secondary_source:
  - cellosaurus
  is_public: true
- category: ProcessProduct
  description: CLASTR tool for STR similarity search across cell lines
  id: cellosaurus.clastr
  name: CLASTR STR Similarity Search
  original_source:
  - cellosaurus
  product_url: https://www.cellosaurus.org/str-search/
  secondary_source:
  - cellosaurus
repository: https://github.com/calipho-sib/cellosaurus
publications:
- authors:
  - Bairoch A
  doi: doi:10.7171/jbt.18-2902-002
  id: doi:10.7171/jbt.18-2902-002
  preferred: true
  title: The Cellosaurus, a cell-line knowledge resource
  year: '2018'
---
Cellosaurus is a comprehensive knowledge resource on cell lines from vertebrates, invertebrates, and plants. It serves as a reference for cell line information, providing researchers with standardized nomenclature, cross-references to other relevant databases, and detailed information about cell line characteristics, authentication, and potential problems.

As of Release 52 (April 2025), Cellosaurus documents 163,868 cell lines, including 121,295 human, 29,536 mouse, and 3,115 rat cell lines. The database provides extensive information for each cell line entry, including:

- Standardized nomenclature and aliases
- Species of origin and cell type
- Transforming techniques used to establish the cell line
- Microbiological status (mycoplasma testing)
- Authentication information (STR profiles, karyotypes)
- Cross-references to other databases and literature
- Doubling time and culture conditions
- Genome sequence data availability
- Special designations and identifiers (e.g., RRID, CVCL)

A particularly important feature of Cellosaurus is its documentation of problematic (misidentified or contaminated) cell lines, helping researchers avoid using compromised cell lines in their experiments.

The database is recognized as a Global Core Biodata Resource (GCBR), an ELIXIR Core Data Resource, and an IRDiRC Recognized Resource. It is developed and maintained by the CALIPHO group at the SIB Swiss Institute of Bioinformatics.

Cellosaurus data is available through a user-friendly web interface, a RESTful API for programmatic access, a SPARQL endpoint for semantic web queries, and downloadable data files in various formats including text, XML, and RDF.