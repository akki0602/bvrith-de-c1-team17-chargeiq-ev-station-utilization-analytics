# Week 08 Log — [Power BI Gold Export and Dashboard Preparation]

**Week:** 8  
**Date range:** [Add dates]  
**Team:** 17
**Project:** Chargeiq-ev-station-utilization-analytics

---

## 1. Sprint Goal

Build a Gold-only Power BI report from the approved Gold outputs, create the first working Power BI Report page, and validate the selected Gold exports against the corresponding Gold SQL results. The main focus was maintaining end-to-end traceability from the selected Gold tables to Power BI without using raw, Bronze, or Silver data directly.
---

## 2. Work Completed

| Task | Owner | Status | Evidence |
| Review and select approved Gold sources required for Power BI | Team 17 | Done | notebooks/06_powerbi_export.ipynb |
| Validate selected Gold tables, grain, row counts, date ranges and key fields | Team 17 | Done | notebooks/06_powerbi_export.ipynb |
| Create controlled Gold exports for Power BI | Team 17 | Done | data_sample/gold_exports/ |
| Reconcile Gold tables with exported/read-back data | Team 17 | Done | notebooks/06_powerbi_export.ipynb, screenshots/week08_gold_export_validation.png |
| Build the first Gold-only Power BI Report page | Team 17 | Done | notebooks/06_powerbi_export.ipynb, screenshots/week08_gold_export_validation.png |
| Create Power BI KPI and analytical visuals | Team 17 | Done | screenshots/week08_powerbi_report.png |
| Validate selected Power BI values against Gold results | Team 17 | Done | notebooks/06_powerbi_export.ipynb |
| Document Week 8 execution and evidence | Team 17 | Done | weekly_logs/week08_log.md |

---

## 3. Key Decisions
. Power BI uses approved Gold outputs only.
. Raw, Bronze and Silver datasets were not connected directly to Power BI.
. Two Gold tables were selected based on dashboard business requirements:
  . default.gold_overall_daily_activity
  . default.gold_station_daily_activity
. gold_overall_daily_activity was used for overall network KPIs and the daily charging-session trend.
. gold_station_daily_activity was used for station-level and city-band charging analysis.
. The two Gold tables were exported separately rather than being flattened into one combined file.
. The declared grain of each selected Gold table was rechecked before export.
. Exported data was read back and reconciled with the corresponding Gold results.
. Power BI was treated as the visualization/analytical layer and not as a replacement for Gold transformations.
. Week 8 focused on establishing a working Gold-only dashboard/model. Further presentation refinement and insight storytelling are reserved for Week 9.
---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
| PBIX file size | A large PBIX file may be difficult to manage in GitHub | Keep one final PBIX version and follow the project file-size guidance |
| Power BI source path | Export location must remain consistent for refresh/review | Use the controlled Gold export as the Power BI source |
| Floating-point precision | Very small differences can appear when comparing decimal totals | Treat the differences as floating-point precision when business totals reconcile |


---

## 5. Evidence Added to GitHub

notebooks/06_powerbi_export.ipynb
data_sample/gold_exports/
screenshots/week08_gold_export_validation.png
screenshots/week08_powerbi_report.png
weekly_logs/week08_log.md
dashboard/powerbi_dashboard.pbix

The Gold export validation confirmed:

Overall Gold rows: 90
Overall export rows: 90
Station Gold rows: 15,660
Station export rows: 15,660
Overall date range: 2026-01-01 to 2026-03-31
Station date range: 2026-01-01 to 2026-03-31
Station duplicate check: 0

The selected business totals were reconciled between Gold and the controlled exports.
---

## 6. AI Transparency Note

| Question | Response |
| AI helped with | Power BI planning, debugging, validation guidance, and documentation |
| What we changed | Adapted AI suggestions to our actual project requirements and Gold tables |
| What we verified | Gold data, exports, KPI values, Power BI sources, and dashboard results were manually checked |
| What we can explain | Gold-to-Power BI process, visuals, KPIs, and validation |
---

## 7. Next Week Preparation

Week 9 will continue with the same Power BI file and focus on dashboard refinement and insight development. Planned work includes improving visual presentation, testing filters and interactions, documenting evidence-based insights, and performing final reconciliation of the refined report values to the owning Gold sources.
