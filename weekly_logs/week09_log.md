# Week 09 Log — Power BI Dashboard Refinement

**Week:** 9
**Date range:** 2026-09-29 to 2026-10-05
**Team:** Team 17
**Project:** Charge IQ EV Station Utilization Analytics

---

## 1. Sprint Goal

Refine the existing Week 8 Power BI dashboard using only the approved Gold tables.

Validate dashboard filters, visuals, reconciliation, documentation, and evidence for the final Week 9 review.

---

## 2. Work Completed

| Task                                            | Owner   | Status | Evidence                           |
| ----------------------------------------------- | ------- | ------ | ---------------------------------- |
| Validated `default.gold_overall_daily_activity` | Team 17 | Done   | Week 9 validation                  |
| Validated `default.gold_station_daily_activity` | Team 17 | Done   | Week 9 validation                  |
| Refined existing Power BI dashboard             | Team 17 | Done   | `dashboard/powerbi_dashboard.pbix` |
| Added and tested Activity Date slicer           | Team 17 | Done   | Dashboard validation               |
| Reconciled February 2026 session total          | Team 17 | Done   | Power BI and Gold validation       |
| Documented dashboard insights                   | Team 17 | Done   | `docs/dashboard_insights.md`       |
| Updated dashboard README                        | Team 17 | Done   | `dashboard/README.md`              |
| Added final dashboard screenshots               | Team 17 | Done   | `screenshots/`                     |

---

## 3. Key Decisions

* Continued using the existing Week 8 Power BI report instead of creating a new dashboard.
* Used only the approved Gold tables.
* Kept `default.gold_overall_daily_activity` and `default.gold_station_daily_activity` independent because no unsafe relationship was required.
* Used the Activity Date slicer from `default.gold_overall_daily_activity`.
* Verified that the overall Gold visuals respond to the Activity Date slicer.
* Kept station-level visuals independent from the overall Gold slicer.
* Used the existing dashboard structure for Week 9 refinement.
* Maintained separate dashboard views for analytics, station performance and operations, and maintenance and reliability.

---

## 4. Blockers / Risks

| Blocker / Risk                                                | Impact                                                             | Resolution                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------- |
| Independent Gold tables do not share the Activity Date slicer | Station-level visuals remain independent from overall Gold visuals | No action required; behavior was validated and documented |
| Large PBIX file size                                          | Repeated uploads can unnecessarily increase GitHub repository size | Keep only the approved final PBIX version in GitHub       |
| Dashboard is based on Week 8 Gold summaries                   | Streaming and live-event metrics are not available in Week 9       | Streaming implementation planned for Week 10              |

---

## 5. Dashboard Pages

The final Week 9 Power BI dashboard contains the following views:

| Dashboard Page                          | Purpose                                                                       |
| --------------------------------------- | ----------------------------------------------------------------------------- |
| EV Charging Station Analytics Dashboard | High-level overview of charging sessions, energy, revenue, and daily activity |
| EV Station Performance & Operations     | Station-level performance and operational analysis                            |
| EV Charging Maintenance & Reliability   | Maintenance and reliability-related analysis                                  |

---

## 6. Gold Sources Used

### `default.gold_overall_daily_activity`

**Grain:** One row per `activity_date`

Used for:

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily EV Charging Sessions
* Activity Date filtering

### `default.gold_station_daily_activity`

**Grain:** One row per `station_id + activity_date`

Used for:

* Station-wise Charging Sessions
* Sessions by City Band
* Station-level operational analysis

No raw, Bronze, or Silver source is connected directly to Power BI.

---

## 7. Validation and Reconciliation

The Activity Date slicer was tested using **February 2026**.

The following overall Gold visuals responded to the selected date range:

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily EV Charging Sessions

Station-level visuals remained independent:

* Station-wise Charging Sessions
* Sessions by City Band

### February 2026 Session Reconciliation

| Validation Item       |                                Result |
| --------------------- | ------------------------------------: |
| Power BI              |                                 `89K` |
| Gold validation query |                              `89,484` |
| Gold table            | `default.gold_overall_daily_activity` |
| Status                |                              **PASS** |

The Power BI value is displayed as `89K` because of rounded dashboard formatting. The underlying Gold value is `89,484`.

---

## 8. Evidence Added to GitHub

### Final Power BI Report

```text
dashboard/powerbi_dashboard.pbix
```

### Dashboard Documentation

```text
dashboard/README.md
docs/dashboard_insights.md
```

### Final Week 9 Screenshots

```text
screenshots/Week_09_EV CHARGING STATION ANALYTICS DASHBOARD.png
screenshots/Week_09_EV STATION PERFORMANCE & OPERATIONS.png
screenshots/Week_09_EV CHARGING MAINTENANCE & RELIABILITY.png
```

These screenshots provide evidence of the final Week 9 dashboard views.

---

## 9. AI Transparency Note

| Question                            | Response                                                                                                                                          |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Where AI helped                     | AI helped structure the dashboard documentation, README, insights, validation notes, and Week 9 log.                                              |
| What we changed after AI suggestion | The documentation was reviewed and adapted to match the actual Gold sources, dashboard structure, screenshots, and project requirements.          |
| What we verified manually           | Power BI visuals, Activity Date slicer behavior, Gold table values, dashboard structure, and February 2026 reconciliation were manually verified. |
| What we can explain without AI      | Gold table purpose, dashboard visuals, filtering behavior, reconciliation results, data-model decisions, and project decisions.                   |

---

## 10. Known Limitations

* The Week 9 dashboard is based on the approved Week 8 Gold summaries.
* Overall and station-level Gold tables remain independent.
* Station-level visuals do not respond to the overall Activity Date slicer.
* Streaming metrics are not included.
* Live-event metrics are not included.
* Real-time charging activity is not included.
* Streaming and live-event implementation belongs to Week 10.

---

## 11. Repository Structure

The final Week 9 repository structure is:

```text
dashboard/
└── powerbi_dashboard.pbix

docs/
└── dashboard_insights.md

screenshots/
├── Week_09_EV CHARGING STATION ANALYTICS DASHBOARD.png
├── Week_09_EV STATION PERFORMANCE & OPERATIONS.png
└── Week_09_EV CHARGING MAINTENANCE & RELIABILITY.png
```

---

## 12. Next Week Preparation

* Begin Week 10 streaming implementation.
* Keep the Week 9 batch Power BI dashboard intact.
* Add the governed streaming branch separately.
* Continue following the approved Gold and data-governance approach.
* Avoid replacing the validated Week 9 batch dashboard with unvalidated streaming data.
* Keep Week 9 evidence and documentation unchanged for final review.

---

## 13. Week 9 Final Status

| Component                    | Status    |
| ---------------------------- | --------- |
| Gold tables validated        | **DONE**  |
| Power BI dashboard refined   | **DONE**  |
| Activity Date slicer tested  | **DONE**  |
| February 2026 reconciliation | **PASS**  |
| Dashboard README             | **DONE**  |
| Dashboard insights           | **DONE**  |
| Final screenshots            | **DONE**  |
| Final PBIX                   | **DONE**  |
| Week 10 preparation          | **READY** |

### Week 9 Status: **COMPLETE**
