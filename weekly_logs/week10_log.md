# Week 10 Log — Streaming Simulation

**Week:** 10  
**Date range:** 06/10/2026 
**Team:** Team 17  
**Project:** ChargeIQ — EV Station Utilization Analytics

---

## 1. Sprint Goal

Set up streaming ingestion for EV station events using JSON files and Structured Streaming.  
Process new events incrementally and create a simple live metric.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Defined streaming event schema | Student A | Done | streaming/kafka_event_schema.json |
| Set up JSON streaming | Student B | In progress | notebooks/07_streaming_simulation.ipynb |
| Prepared streaming data | Student C | In progress | data_sample/streaming/ |
| Documented streaming design | Student B| In progress | streaming/structured_streaming_design.md |

---

## 3. Key Decisions

- Used JSON event files for streaming simulation.
- Treated Kafka as a design-level concept rather than an implementation requirement.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Databricks-specific streaming code needed environment adaptation | Local execution was not direct | Verify Structured Streaming setup |
| Understanding streaming checkpoints |	Needed to maintain incremental processing	| Review checkpoint configuration
| Handling new JSON event files	| Required for testing incremental ingestion | Verify input file structure

---

## 5. Evidence Added to GitHub

- notebooks/07_streaming_simulation.ipynb
- streaming/structured_streaming_design.md
- streaming/kafka_event_schema.json
- weekly_logs/week10_log.md

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Understanding Structured Streaming, checkpoints, watermarking and deduplication. |
| What we changed after AI suggestion | Adapted the streaming setup to our project and environment. |
| What we verified manually | Checked the code, file paths, schema and streaming setup. |
| What we can explain without AI | Batch vs streaming, Structured Streaming, checkpoints and basic deduplication. |

---

## 7. Next Week Preparation

- Review the complete project pipeline from Raw to Dashboard.
- Prepare the repository and Presentation for the next sprint.
