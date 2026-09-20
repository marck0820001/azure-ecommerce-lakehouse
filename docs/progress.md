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

## Planned next milestones

### Databricks and Bronze
- [ ] Azure Databricks workspace
- [ ] Cost-controlled compute / auto-termination
- [ ] Secure Databricks → ADLS access
- [ ] PySpark Bronze ingestion
- [ ] Delta Lake Bronze tables
- [ ] Technical ingestion metadata

### Silver and data quality
- [ ] Schema normalization
- [ ] Type casting
- [ ] Deduplication
- [ ] Null and business-rule validation
- [ ] Referential-integrity checks
- [ ] Quarantine area
- [ ] Curated Silver tables
- [ ] Idempotent Delta MERGE logic

### Gold and analytics
- [ ] dim_customers
- [ ] dim_products
- [ ] dim_sellers
- [ ] dim_date
- [ ] fact_orders
- [ ] fact_order_items
- [ ] Business aggregations

### Incremental control
- [ ] Watermark / control table
- [ ] Track last successful batch
- [ ] Avoid unnecessary historical reprocessing
- [ ] ADF + Databricks orchestration

### Delivery
- [ ] Power BI dashboard
- [ ] Automated tests
- [ ] GitHub Actions CI
- [ ] Export Azure artifacts
- [ ] Final architecture diagram
- [ ] Technical documentation
- [ ] End-to-end demo video
