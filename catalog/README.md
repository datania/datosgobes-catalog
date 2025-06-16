---
license: mit
configs:
- config_name: default
  data_files:
    - split: datasets
      path: dataset/datasets.parquet
    - split: publishers
      path: publisher/publishers.parquet
    - split: provinces
      path: province/provinces.parquet
    - split: spatial
      path: spatial/spatial.parquet
    - split: themes
      path: theme/themes.parquet
    - split: public_sectors
      path: public-sector/public-sectors.parquet
  default: true
---

# `datos.gob.es` Data Catalog

A snapshot of the `datos.gob.es` Data Catalog [produced by Datania](https://github.com/datania/datosgobes-catalog).
