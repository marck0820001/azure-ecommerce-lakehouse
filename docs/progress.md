# Project Progress

## Completed

- [x] Repository initialized
- [x] Olist dataset profiling
- [x] Python source-system simulator
- [x] Initial-load dataset generation
- [x] Monthly incremental batch generation
- [x] Azure Resource Group
- [x] ADLS Gen2 Storage Account
- [x] Hierarchical Namespace enabled
- [x] Lakehouse directory structure
- [x] Microsoft Entra ID / RBAC configuration
- [x] Azure Data Factory
- [x] ADLS Gen2 linked service using Managed Identity
- [x] Initial ingestion pipeline
- [x] Parameterized monthly ingestion pipeline
- [x] Metadata-driven master pipeline
- [x] Get Metadata + Filter + ForEach orchestration
- [x] Historical ingestion completed into Landing
- [x] ADF changes published

## Current checkpoint

```text
Olist
  ↓
Python source simulator
  ↓
ADLS Gen2 / source-drop
  ↓
Azure Data Factory
  ↓
ADLS Gen2 / landing
```

## Next

- [ ] Azure Databricks
- [ ] Secure Databricks → ADLS access
- [ ] PySpark Bronze layer
- [ ] Delta Lake tables
- [ ] Silver transformations
- [ ] Data Quality / Quarantine
- [ ] Idempotent MERGE logic
- [ ] Gold dimensional model
- [ ] Watermark / control table
- [ ] ADF + Databricks orchestration
- [ ] Power BI
- [ ] Automated tests
- [ ] GitHub Actions CI
- [ ] Final architecture diagram
- [ ] Demo video
