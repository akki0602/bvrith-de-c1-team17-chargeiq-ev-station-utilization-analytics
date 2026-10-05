# Dashboard Insights

**Week:** 9
**Purpose:** Document the key observations, Gold sources, dashboard pages, and validation results from the Power BI EV Charging Station Analytics Dashboard.

---

## 1. Dashboard Pages

The Week 9 dashboard contains the following dashboard views:

| Page / Dashboard                        | Purpose                                                 | Main Focus                                                                   |
| --------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------- |
| EV Charging Station Analytics Dashboard | High-level view of EV charging activity                 | Sessions, energy consumption, estimated revenue, and daily charging activity |
| EV Station Performance & Operations     | Analyze station-level performance and operations        | Station-wise charging activity, city bands, and operational performance      |
| EV Charging Maintenance & Reliability   | Analyze maintenance and reliability-related information | Charging station reliability and operational observations                    |

---

## 2. Key Insights

1. The dashboard provides a high-level view of EV charging activity using **charging sessions, energy consumption, and estimated revenue**.

2. The dashboard uses approved **Gold-level data** for reporting and visualization.

3. Overall charging activity is represented using:

   * Total EV Charging Sessions
   * Total Energy (kWh)
   * Estimated Revenue (INR)
   * Daily EV Charging Sessions

4. Station-level analysis provides a comparison of charging activity across different charging stations.

5. City-band analysis provides a high-level comparison of charging sessions across different city categories.

6. The dashboard supports date-based analysis through the **Activity Date slicer**.

7. The Activity Date slicer was tested using **February 2026**. The overall session, energy, revenue, and daily-session visuals responded to the selected date range.

8. Station-level visuals remained independent because they use the separate `default.gold_station_daily_activity` table.

9. On **2026-01-01**, the Gold table recorded:

   * **3,705 charging sessions**
   * **95,026.411 kWh** of energy
   * **INR 1,431,200.83** estimated revenue

10. On **2026-03-31**, the Gold table recorded:

* **1,990 charging sessions**
* **51,071.094 kWh** of energy
* **INR 739,181.22** estimated revenue

11. These two dates show different levels of daily charging activity. The available data does not establish the reason for the difference, so no causal explanation is claimed.

---

## 3. Gold Tables Used

The dashboard uses only the approved Gold outputs.

### `default.gold_overall_daily_activity`

**Grain:** One row per `activity_date`

**Purpose:** Overall daily EV charging activity.

**Important fields:**

* `activity_date`
* `total_session_count`
* `total_energy_kwh`
* `estimated_revenue_inr`

**Used for:**

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily EV Charging Sessions
* Activity Date filtering for overall visuals

### `default.gold_station_daily_activity`

**Grain:** One row per `station_id + activity_date`

**Purpose:** Station-level EV charging activity.

**Important fields:**

* `station_id`
* `station_name`
* `city_band`
* `zone`
* `site_type`
* `activity_date`
* `daily_session_count`
* `daily_energy_kwh`
* `daily_estimated_revenue_inr`

**Used for:**

* Station-wise Charging Sessions
* Sessions by City Band
* Station-level operational analysis

---

## 4. Dashboard Measure Register

| Dashboard Measure              | Gold Table                            | Business Meaning                |
| ------------------------------ | ------------------------------------- | ------------------------------- |
| Total EV Charging Sessions     | `default.gold_overall_daily_activity` | Total charging sessions         |
| Total Energy (kWh)             | `default.gold_overall_daily_activity` | Total energy delivered          |
| Estimated Revenue (INR)        | `default.gold_overall_daily_activity` | Estimated charging revenue      |
| Daily EV Charging Sessions     | `default.gold_overall_daily_activity` | Daily charging session activity |
| Station-wise Charging Sessions | `default.gold_station_daily_activity` | Charging sessions by station    |
| Sessions by City Band          | `default.gold_station_daily_activity` | Charging sessions by city band  |

No unsupported KPI was added.

---

## 5. Data Model and Interaction

The Power BI model contains the two approved Gold tables.

The Gold tables remain **independent** because no unsafe relationship is required between the overall daily summary and the station daily summary.

### Activity Date Slicer

The Activity Date slicer is based on:

`default.gold_overall_daily_activity`

The slicer affects:

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily EV Charging Sessions

The following station-level visuals remain independent:

* Station-wise Charging Sessions
* Sessions by City Band

This behavior is intentional because the two Gold summary tables remain independent.

---

## 6. Power BI Validation

The following validation checks were completed:

* Dashboard uses approved Gold outputs only.
* No raw source is directly connected to the dashboard.
* No Bronze source is directly connected to the dashboard.
* No Silver source is directly connected to the dashboard.
* Activity Date slicer interaction was tested.
* Overall KPI values were checked against Gold data.
* Dashboard visuals are traceable to the approved Gold tables.

### February 2026 Reconciliation

| Validation Item                     |                                Result |
| ----------------------------------- | ------------------------------------: |
| Power BI Total EV Charging Sessions |                                 `89K` |
| Gold Validation Query               |                              `89,484` |
| Gold Table                          | `default.gold_overall_daily_activity` |
| Status                              |                              **PASS** |

The Power BI KPI displays **89K** because the dashboard uses rounded display formatting, while the underlying Gold validation value is **89,484**.

---

## 7. Dashboard Screenshots / Evidence

All Week 9 dashboard screenshots are stored in the `screenshots/` folder.

### EV Charging Station Analytics Dashboard

```text
screenshots/Week_09_EV CHARGING STATION ANALYTICS DASHBOARD.png
```

This screenshot provides evidence of the main EV charging analytics dashboard and overall charging activity.

### EV Station Performance & Operations

```text
screenshots/Week_09_EV STATION PERFORMANCE & OPERATIONS.png
```

This screenshot provides evidence of station-level performance and operational analysis.

### EV Charging Maintenance & Reliability

```text
screenshots/Week_09_EV CHARGING MAINTENANCE & RELIABILITY.png
```

This screenshot provides evidence of the maintenance and reliability dashboard view.

---

## 8. Refresh

The dashboard uses the approved Gold tables as its data sources.

The Gold outputs were validated before the final Week 9 dashboard review.

After a refresh, the following should be checked:

* KPI values
* Daily charging trend
* Station-wise sessions
* City-band sessions
* Activity Date slicer behavior
* Reconciliation with the Gold output

---

## 9. Scope and Limitations

The dashboard is based on the approved Week 8 Gold summaries.

The reporting period covered by the available Gold observations is:

**2026-01-01 to 2026-03-31**

The dashboard provides descriptive information about EV charging activity. It does not establish causal reasons for changes in charging activity.

The Week 9 dashboard does not include:

* Streaming metrics
* Live-event metrics
* Real-time charging activity

Streaming and live-event metrics belong to **Week 10**.

---

## 10. Final Dashboard Summary

The Week 9 Power BI dashboard provides a consolidated view of:

* EV charging activity
* Charging sessions
* Energy consumption
* Estimated revenue
* Daily charging trends
* Station performance
* Operational activity
* City-band analysis
* Maintenance and reliability observations

The dashboard uses only the approved Gold outputs and does not connect directly to raw, Bronze, or Silver sources.

The February 2026 reconciliation successfully passed:

**Power BI:** `89K`
**Gold validation:** `89,484`
**Status:** **PASS**

The dashboard and supporting evidence are maintained in the project repository according to the Week 9 requirements.
