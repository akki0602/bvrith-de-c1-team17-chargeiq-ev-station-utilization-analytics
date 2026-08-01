# Week 04 Log — [Sprint Name]

**Week:** 4  
**Date range:** 31-07-2026 to 06-08-2026  
**Team:** 17 
**Project:** ChargeIQ - EV Station Utilization Analytics

---

## 1. Sprint Goal

The goal of this week was to read raw session data into Spark, understand the schema, and validate the dataset.  
We also ensured the data consistency after adding new columns and transformations.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Read raw data into DataFrame | Team | Done | screenshots/week04_raw_data.png |
| Checked schema using printSchema() | Team | Done | screenshots/week04_schema.png |
| Added new columns to dataset | Team | Done | screenshots/week04_new_columns.png |
| Validated data (row count & matching) | Team | Done | screenshots/week04_validation.png |
| Completed Bronze Ingestion Notebook | Team | Done | notebooks/02_bronze_ingestion.ipynb |

---

## 3. Key Decisions

- Used Spark DataFrame API for processing large-scale data
- Used `printSchema()` to understand structure before transformation
- Performed validation using row count comparison to ensure no data loss


---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|------|-------|--------|----------|
| Initial confusion in DataFrame creation | Medium | Resolved through practice |
| Schema understanding | Low | Used printSchema() |

---

## 5. Evidence Added to GitHub

- Raw data reading output screenshot  
- Schema output screenshot  
- New columns added screenshot  
- Data validation screenshot  

---

## 6. AI Transparency Note

| Question | Response |
|------|-------|--------|----------|
| Where AI helped | Helped in understanding Spark commands and structuring workflow |
| What we changed after AI suggestion | Simplified steps and used proper validation methods |
| What we verified manually | Schema correctness and row count matching |
| What we can explain without AI | Data reading, schema checking, and validation logic |

---

## 7. Next Week Preparation

- Perform data cleaning (handle missing/null values)  
- Remove duplicate records from dataset  
- Standardize column names and formats   
- Validate cleaned data for consistency  
