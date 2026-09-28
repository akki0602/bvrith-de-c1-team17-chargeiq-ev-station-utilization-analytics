# Dashboard Insights

**Week:** 9  
**Purpose:** Document the key observations, Gold sources, and validation results from the Power BI dashboard.

---

## 1. Dashboard Pages

| Page | Purpose | Main Visuals |
|---|---|---|
| Executive Overview | High-level view of EV charging activity | Summary cards, daily trend, station-wise sessions, city-band sessions, Activity Date slicer |


---

## 2. Key Insights

1. The dashboard provides a high-level view of EV charging activity using session count, energy consumption, and estimated revenue.

2. On 2026-01-01, the Gold table recorded 3,705 sessions, 95,026.411 kWh of energy, and estimated revenue of INR 1,431,200.83.

3. On 2026-03-31, the Gold table recorded 1,990 sessions, 51,071.094 kWh of energy, and estimated revenue of INR 739,181.22.

4. These two dates show different levels of daily charging activity. The available evidence does not establish the reason for the difference, so no causal explanation is claimed.

5. The Activity Date slicer was tested using February 2026. The overall session, energy, revenue, and daily-session visuals responded to the selected date range.

6. Station-wise and city-band visuals remained independent because they use the separate `default.gold_station_daily_activity` table. No unsafe relationship was added to force cross-filtering.

---

## 3. How the Dashboard Uses Gold Tables

| Dashboard Page | Gold Table Used | Important Fields |
|---|---|---|
| Executive Overview | `default.gold_overall_daily_activity` | `activity_date`, `total_session_count`, `total_energy_kwh`, `estimated_revenue_inr` |
| Executive Overview | `default.gold_station_daily_activity` | `station_name`, `city_band`, `activity_date`, `daily_session_count` |

### Gold Table Grain

- `default.gold_overall_daily_activity`: one row per `activity_date`
- `default.gold_station_daily_activity`: one row per `station_id + activity_date`

---

## 4. Power BI Validation

- Dashboard connects to approved Gold outputs only.
- Activity Date slicer interaction was tested.
- KPI values were checked against Gold table values.
- February 2026 session total reconciled:
  - Power BI: `89K`
  - Gold validation query: `89,484`
  - Status: PASS
- Screenshots are saved in `screenshots/`.
- Dashboard visuals are traceable to the approved Gold tables.

## 5. Evidence

- `week09_01_final_model.png` — final Power BI model
- `week09_02_refined_page_01.png` — refined dashboard page
- `week09_04_filter_interaction.png` — Activity Date slicer test
- `week09_05_filtered_reconciliation.png` — February reconciliation
- `week09_06_insights_evidence.png` — Gold data used for dashboard observations

## 6. Scope and Limitations

The observations above are based on the approved Gold outputs for the reporting period from 2026-01-01 to 2026-03-31.

The dashboard does not provide causal explanations for changes in activity.

Streaming or live-event metrics are not included in the Week 9 dashboard. Streaming work belongs to Week 10.
