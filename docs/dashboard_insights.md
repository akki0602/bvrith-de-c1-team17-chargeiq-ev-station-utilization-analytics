# Dashboard Insights

**Week:** 9  
**Purpose:** Explain what the Power BI dashboard shows.

---

## 1. Dashboard Pages

| Page | Purpose | Main Visuals |
|---|---|---|
| Page 1: Executive Overview | High-level summary of EV charging activity | Summary cards, daily trend chart, station-wise sessions, city-band sessions, activity-date slicer |


---

## 2. Key Insights

Write 5–8 insights from the dashboard.

1. The dashboard provides a high-level view of EV charging activity using daily session count, energy consumption, and estimated revenue from the approved Gold   outputs.
2. The daily activity data shows different levels of charging activity across the reporting period. On 2026-01-01, the Gold table recorded 3,705 sessions, 95,026.411 kWh of energy, and estimated revenue of INR 1,431,200.83.
3. On 2026-03-31, the Gold table recorded 1,990 sessions, 51,071.094 kWh of energy, and estimated revenue of INR 739,181.22.
4. The comparison between these two dates is an observation from the daily Gold data. The available evidence does not establish why the activity differed, so no causal explanation is claimed.
5. The Activity Date slicer successfully filters the visuals owned by "gold_overall_daily_activity". During the February 2026 interaction test, the overall session, energy, revenue, and daily-session visuals responded to the selected date range.
6. The station-level visuals remained independent of the overall date slicer because they use the separate "gold_station_daily_activity" table. No unsafe relationship was added simply to force cross-filtering.

---

## 3. How the Dashboard Uses Gold Tables

| Dashboard Page | Gold Table Used | Important Fields |
|---|---|---|
| Page 1: Executive Overview | default.gold_overall_daily_activity | activity_date, total_session_count, total_energy_kwh, estimated_revenue_inr |
| Page 1: Executive Overview | default.gold_station_daily_activity | station_name, city_band, activity_date, daily_session_count, daily_energy_kwh, daily_estimated_revenue_inr |

### Gold Table Grain

- default.gold_overall_daily_activity: one row per activity_date
- default.gold_station_daily_activity: one row per station_id + activity_date
---

## 4. Power BI Validation

- Dashboard connects to approved Gold outputs only.
- Date slicer interaction was tested.
- KPI totals were checked against Gold table values.
- February 2026 filtered session total reconciled:
  Power BI displayed `89K`, while the Gold validation query returned
  `89,484` sessions.
- Screenshots are saved in `screenshots/`.
- Dashboard story is traceable to the approved Gold tables.
