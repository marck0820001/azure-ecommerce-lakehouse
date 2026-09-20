# Azure Data Factory

This folder documents the Azure Data Factory ingestion layer currently deployed in Azure.

> The exported ADF JSON definitions will be added later. The pipelines below are already implemented and published in Azure.

## Linked service

### `ls_adls_ecommerce`

- Connector: Azure Data Lake Storage Gen2
- Authentication: system-assigned Managed Identity
- Authorization: Azure RBAC
- Storage target: project ADLS Gen2 account

## Pipelines

### `pl_ingest_ecommerce_initial`

Purpose: copy full initial/master datasets from:

```text
source-drop/initial/
```

to:

```text
landing/initial/
```

The activity uses binary copy because ADF is only moving source files at this stage.

---

### `pl_ingest_ecommerce_batch`

Purpose: process one monthly transactional batch.

Parameter:

```text
p_batch_month
```

Example:

```text
2017-01
```

Source:

```text
source-drop/incremental/batch_month=2017-01/
```

Destination:

```text
landing/incremental/batch_month=2017-01/
```

The same pipeline is reused for every month.

---

### `pl_ingest_ecommerce_incremental_master`

Purpose: discover and orchestrate all available monthly batches.

Flow:

```text
Get Metadata
  ↓
Filter
  ↓
ForEach
  ↓
Execute Pipeline
  ↓
pl_ingest_ecommerce_batch
```

Main behavior:

- Get Metadata reads child items from `source-drop/incremental/`.
- Filter keeps folder items.
- ForEach iterates through batch folders.
- The folder name `batch_month=YYYY-MM` is converted to `YYYY-MM`.
- Execute Pipeline passes that value into `pl_ingest_ecommerce_batch`.
- The initial implementation runs sequentially for easier validation and debugging.

## Current limitation

The master pipeline discovers all available folders on each run, so it can reprocess previously landed batches.

This will be improved later with:

- watermark/control metadata;
- Delta Lake idempotency;
- MERGE-based processing.
