# Week 09 Log — [Power BI Dashboard Refinement]

**Week:** 9  
**Date range:** [Add dates]  
**Team:** [Team 17]  
**Project:** [Charge IQ Ev Station Utilization Analytics]

---

## 1. Sprint Goal

Refine the existing Week 8 Power BI dashboard using only the approved Gold tables.
Validate dashboard filters, visuals, reconciliation, documentation, and evidence for final Week 9 review.


---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Validated `gold_overall_daily_activity` | Team 17 | Done | Week 9 notebook |
| Validated `gold_station_daily_activity` | Team 17 | Done | Week 9 notebook |
| Refined existing Power BI dashboard | Team 17 | Done | `powerbi_dashboard.pbix` |
| Added and tested Activity Date slicer | Team 17 | Done | `week09_04_filter_interaction.png` |
| Reconciled February session total | Team 17 | Done | `week09_05_filtered_reconciliation.png` |
| Documented dashboard insights | Team 17 | Done | `docs/dashboard_insights.md` |
| Updated dashboard README | Team 17 | Done | `dashboard/README.md` |

---

## 3. Key Decisions

- Continued using the same Week 8 Power BI report instead of creating a new dashboard.
- Used only the approved Gold tables.
- Kept the overall and station Gold tables independent because no unsafe relationship was required.
- Used an Activity Date slicer from `gold_overall_daily_activity`.
- Kept station-level visuals independent from the overall Gold slicer.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Independent Gold tables do not share the Activity Date slicer | Station-level visuals remain independent from overall Gold visuals | No action required; behaviour was validated and documented |

---

## 5. Evidence Added to GitHub

- `dashboard/powerbi_dashboard.pbix` updated
- `dashboard/README.md` updated
- `docs/dashboard_insights.md` updated
- `screenshots/week09_01_final_model.png`
- `screenshots/week09_02_refined_page_01.png`
- `screenshots/week09_04_filter_interaction.png`
- `screenshots/week09_05_filtered_reconciliation.png`
- `screenshots/week09_06_insights_evidence.png`
- Week 9 Power BI refinement notebook updated

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Helped structure documentation, dashboard notes, and validation steps. |
| What we changed after AI suggestion | Reviewed and adapted the suggestions to match the actual project work and dashboard. |
| What we verified manually | Power BI visuals, slicer behaviour, Gold table queries, and February reconciliation were manually verified. |
| What we can explain without AI | Gold table purpose, dashboard visuals, filtering behaviour, reconciliation, and project decisions. |

---

## 7. Next Week Preparation

- Begin Week 10 streaming implementation.
- Keep the Week 9 batch Power BI dashboard intact while adding the governed streaming branch.
