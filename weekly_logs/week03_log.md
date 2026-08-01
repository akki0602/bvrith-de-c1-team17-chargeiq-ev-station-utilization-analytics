# Week 03 Log — Databricks Setup & Data Exploration

**Week:** 3  
**Date range:** 24 July 2026 – 30 July 2026  
**Team:** Team 17  
**Project:** P17 CHARGEIQ-EV STATION UTILIZATION ANALYTICS **

---

## 1. Sprint Goal

The objective of this sprint was to set up the Databricks environment and perform initial exploration of the ChargeIQ sample datasets. The team focused on loading the data, validating schemas, verifying row counts, and conducting basic data profiling to ensure the datasets were ready for the next phase of the data engineering pipeline.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Configured the Databricks development environment | Team | Done | Databricks Workspace |
| Loaded the ChargeIQ sample datasets into Databricks | Team | Done | `notebooks/01_data_exploration.ipynb` |
| Explored the datasets by displaying sample records | Team | Done | Notebook Output |
| Validated dataset schemas and verified row counts | Team | Done | `week03_schema_and_row_count.png` |
| Performed basic data profiling and checked for null values | Team | Done | Profiling Queries |
| Documented observations and updated project artifacts | Team | Done | GitHub Repository |
| Updated the Week 03 Sprint Log and AI Transparency Note | Team | Done | `weekly_logs/week03_log.md` |

---

## 3. Key Decisions

- Standardized the use of Databricks notebooks and Apache Spark for dataset exploration and validation.
- Completed schema verification and basic data quality assessment to establish confidence in the sample datasets before subsequent project tasks.
- --
## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Initial familiarization with the Databricks workspace and notebook environment | Low | Reviewed official Databricks documentation and completed basic practice exercises |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/01_data_exploration.ipynb`
- Added `screenshots/week03_databricks_data_loaded.png`
- Added `screenshots/week03_schema_and_row_count.png`
- Updated `weekly_logs/week03_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assisted in suggesting data exploration techniques, Spark DataFrame operations, notebook organization, and documentation improvements. |
| What we changed after AI suggestion | The team customized the notebook and profiling steps to align with the ChargeIQ project requirements and verified all outputs before finalizing the work. |
| What we verified manually | Verified successful data loading, dataset schemas, row counts, sample records, null-value checks, and profiling results within the Databricks environment. |
| What we can explain without AI | The complete Databricks setup process, data loading workflow, schema validation, row count verification, data profiling techniques, and all engineering decisions made during this sprint. |

---

## 7. Next Week Preparation

- Begin implementing the Bronze Layer by ingesting raw datasets into Delta tables.
- Preserve raw data and metadata while preparing datasets for transformation into the Silver layer.
