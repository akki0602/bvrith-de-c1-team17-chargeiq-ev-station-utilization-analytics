# Week 08 Log — [Sprint Name]

**Week:** 8  
**Date range:** [Add dates]  
**Team:** 17
**Project:** Chargeiq-ev-station-utilization-analytics

---

## 1. Sprint Goal

Build a Gold-only Power BI model from the approved Gold outputs, create the Network Operations Overview (PBI-01) page, and validate that the Power BI KPI values reconcile with the corresponding Gold SQL results.
The main focus was maintaining end-to-end traceability from Gold tables to Power BI without using raw, Bronze, or Silver data directly.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
Export Gold datasets for Power BI:	Student A:	Done:	notebooks/06_powerbi_export.ipynb
Build Gold-only Power BI data model:	Student B	:Done	:dashboard/
Create PBI-01 Network Operations Overview:	Student C:	Done:	screenshots/week08_*.png
Validate KPI values against Gold SQL:	Team 17	:Done:	Notebook validation outputs
Document Power BI source mapping and refresh details:	Team 17:	Done:	dashboard/README.md

---

## 3. Key Decisions
Power BI uses Gold outputs only as its data source.
Raw, Bronze, and Silver datasets were not used directly in the dashboard.
fact_charging_session and fact_maintenance_event remain separate because they have different declared grains.
Dimension-to-fact relationships follow the required one-to-many structure.
KPI values shown in Power BI are validated against the corresponding Gold SQL results.
The Power BI model is treated as an analytical/visualization layer rather than a second transformation layer.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
Power BI relationship and filter-direction issues:	May affect KPI and visual accuracy:	Review relationships and filter paths
KPI reconciliation with Gold SQL:	Requires careful validation of dashboard values:	Mentor review if discrepancies occur
PBIX file size:	May affect GitHub storage:	Follow the project’s file-size and evidence guidelines

---

## 5. Evidence Added to GitHub

notebooks/06_powerbi_export.ipynb added
Power BI-related files uploaded 
05_gold_aggregations.ipynb filename corrected 
04_data_quality_checks.ipynb filename corrected 

---

## 6. AI Transparency Note

| Question | Response |
Where AI helped:	AI helped with Power BI model planning, Gold KPI mapping, validation queries, and documentation.
What we changed after AI suggestion:	We reviewed the suggestions and adapted the model, relationships, and KPI mapping according to the approved project requirements.
What we verified manually:	We manually verified Gold-only data sources, relationships, KPI values against Gold SQL, and dashboard outputs.
What we can explain without AI:	We can explain the Gold export process, Power BI model, relationships, KPI calculations, Page 1 visuals, and reconciliation process.
---

## 7. Next Week Preparation

Build PBI-02: Station Utilization and Energy Demand page.
Build PBI-03: Charger Reliability and Maintenance page.
Configure and test dashboard filters and interactions.
Document 3–5 evidence-based insights.
Perform accessibility checks and Gold SQL reconciliation.
