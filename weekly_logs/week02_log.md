# Week 02 Log — Dataset Design

**Week:** 2  
**Date range:** 17/07/2026-24/07/2026
**Team:** 17
**Project:** Charge IQ Ev Station Utilization Analytics

---

## 1. Sprint Goal

The goal of this week is to define the data dictionary and source schemas for the ChargeIQ project, covering raw, reference, Silver, and streaming data fields. We will also generate small synthetic sample datasets for development and testing while ensuring the data is structured, reproducible, and free of real personal or company data.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |

Defined the ChargeIQ data dictionary and source schemas:	Student	Done:	docs/data_dictionary.md
Documented synthetic data generation assumptions:	Student	Done:	docs/synthetic_data_assumptions.md
Updated the synthetic data generator for ChargeIQ sample data:	Student	Done:	src/generate_synthetic_data.py
Generated small synthetic sample data files for the project:	Student	Done:	data_sample/raw/
Updated the Week 2 weekly progress log:	Student	Done:	weekly_logs/week02_log.md
Reviewed raw, reference, Silver, and streaming data requirements:	Student	Done:	docs/data_dictionary.md
Prepared the Week 2 deliverables for GitHub:	Student	Done:	GitHub repository

---

## 3. Key Decisions

Used synthetic data instead of real data.
Used a fixed random seed for reproducible data.
Adapted the generic template to the ChargeIQ project requirements.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
Understanding the project-specific fields:	Needed clarification:	Reviewed project documentation
Matching the template with ChargeIQ schemas:	Risk of incorrect fields:	Verified the Data Dictionary

---

## 5. Evidence Added to GitHub

docs/data_dictionary.md
docs/synthetic_data_assumptions.md
src/generate_synthetic_data.py
data_sample/raw/
weekly_logs/week02_log.md

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
Where AI helped:	Helped understand the template and structure the files.
What we changed after AI suggestion:	Modified the suggestions to match ChargeIQ requirements.
What we verified manually:	Checked fields, file names, and data formats.
What we can explain without AI:	We can explain the data dictionary, synthetic data, and project data structure.

---

## 7. Next Week Preparation

Validate the generated sample data.
Review data quality and validation requirements.
Prepare for the next stage of the data pipeline.
