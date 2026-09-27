# Power BI Dashboard Folder

Save the final Power BI file here.

Expected file:

```text
dashboard/powerbi_dashboard.pbix
```

## 1. Gold Source Register

The dashboard uses only the approved Gold outputs.

` default.gold_overall_daily_activity ` 
- Grain: one row per ` activity_date `
- Purpose: overall daily EV charging activity
- Main fields:
  - ` activity_date `
  - ` total_session_count `
  - ` total_energy_kwh `
  - ` estimated_revenue_inr `
` default.gold_station_daily_activity `
- Grain: one row per ` station_id + activity_date `
- Purpose: station-level EV charging activity
- Main fields:
  - ` station_id `
  - ` station_name `
  - ` city_band `
  - ` zone `
  - ` site_type `
  - ` activity_date `
  - ` daily_session_count `
  - ` daily_energy_kwh `
  - ` daily_estimated_revenue_inr `

No raw, Bronze, or Silver source is connected directly to Power BI.

## 2. Model Map

The PBIX contains the two approved Gold tables.

The Gold tables remain independent because no unsafe relationship is required between the overall daily summary and station daily summary.

The date slicer from ` gold_overall_daily_activity ` filters the overall Gold visuals. Station-level visuals remain independent.

### 3. Page Register
## Executive Overview

Business purpose: Provide a high-level view of EV charging activity.

# Visuals:

- Total EV Charging Sessions
- Total Energy (kWh)
- Estimated Revenue (INR)
- Daily EV Charging Sessions
- Station-wise Charging Sessions
- Sessions by City Band
- Activity Date slicer

## Gold sources:

-  KPI and daily trend visuals → ` gold_overall_daily_activity `
- Station and city-band visuals → ` gold_station_daily_activity `


### 4. Measure Register
 | Dashboard Measure | Owning Gold Table | Business Meaning |
 | ----------------- | ----------------- | ---------------- |
 | Total EV Charging Sessions	| ` gold_overall_daily_activity	` |Total charging sessions |
 | Total Energy (kWh) |	` gold_overall_daily_activity `	| Total energy delivered |
 | Estimated Revenue (INR) |	` gold_overall_daily_activity `	| Estimated charging revenue |
 | Daily EV Charging Sessions	| ` gold_overall_daily_activity `	| Daily charging session activity |
 | Station-wise Charging Sessions	| ` gold_station_daily_activity	` | Charging sessions by station |
 | Sessions by City Band	| ` gold_station_daily_activity	` | Charging sessions by city band |

No unsupported KPI was added.

### 5. Interaction Notes

The Activity Date slicer was tested using February 2026.

Overall Gold visuals responded to the slicer:

- Total EV Charging Sessions
- Total Energy (kWh)
- Estimated Revenue (INR)
- Daily EV Charging Sessions

Station-level visuals remained independent:

- Station-wise Charging Sessions
- Sessions by City Band

This behaviour is expected because the two Gold summaries are independent.

## 6. Refresh

The dashboard uses the approved Gold tables as its data sources.

The Gold outputs were validated before the final Week 9 dashboard review.

## 7. Reconciliation

A February 2026 reconciliation was completed for Total EV Charging Sessions.

- Power BI: `89K`
- Gold query: `89,484`
- Gold table: `default.gold_overall_daily_activity`
- Status: PASS

## 8. Dashboard Insights

Detailed dashboard insights are documented in:

`docs/dashboard_insights.md`

## 9. Evidence

Week 9 screenshots are stored in:

`screenshots/`

Key evidence includes:

- `week09_01_final_model.png`
- `week09_02_refined_page_01.png`
- `week09_04_filter_interaction.png`
- `week09_05_filtered_reconciliation.png`
- `week09_06_insights_evidence.png`

## 10. Known Limitations

The dashboard is based on the approved Week 8 Gold summaries.

Streaming or live-event metrics are not included. These belong to Week 10.

## 11. PBIX File

The final Power BI report is:

`dashboard/powerbi_dashboard.pbix`

Rules:

- Power BI must connect to Gold outputs only.
- Do not connect dashboard visuals directly to raw source files.
- Save dashboard screenshots in `screenshots/`.
- Explain dashboard insights in `docs/dashboard_insights.md`.



Do not keep uploading multiple heavy PBIX versions into GitHub.
