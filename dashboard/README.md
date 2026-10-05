# Power BI EV Charging Station Analytics Dashboard

## Overview

This folder contains the final Power BI dashboard for the **EV Charging Station Analytics** project.

The Week 9 dashboard provides an executive and operational view of EV charging activity using only the approved **Gold outputs**.

The dashboard covers:

* EV charging sessions
* Energy consumption
* Estimated revenue
* Daily charging activity
* Station-wise performance
* City-band analysis
* Station operations
* Maintenance and reliability observations

---

## 1. Gold Source Register

The Power BI dashboard uses only the approved Gold outputs.

### `default.gold_overall_daily_activity`

**Grain:** One row per `activity_date`

**Purpose:** Overall daily EV charging activity.

**Main fields:**

* `activity_date`
* `total_session_count`
* `total_energy_kwh`
* `estimated_revenue_inr`

### `default.gold_station_daily_activity`

**Grain:** One row per `station_id + activity_date`

**Purpose:** Station-level EV charging activity.

**Main fields:**

* `station_id`
* `station_name`
* `city_band`
* `zone`
* `site_type`
* `activity_date`
* `daily_session_count`
* `daily_energy_kwh`
* `daily_estimated_revenue_inr`

### Source Rule

Power BI connects only to the approved Gold outputs.

**No raw, Bronze, or Silver source is connected directly to Power BI.**

---

## 2. Data Model

The PBIX contains the two approved Gold tables:

```text
default.gold_overall_daily_activity
default.gold_station_daily_activity
```

The two Gold tables remain **independent** because no unsafe relationship is required between the overall daily summary and station daily summary.

### Overall Gold Table

Used for:

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily EV Charging Sessions
* Activity Date filtering

### Station Gold Table

Used for:

* Station-wise Charging Sessions
* Sessions by City Band
* Station-level operational analysis

---

## 3. Dashboard Pages

The Week 9 dashboard contains three main dashboard views.

| Dashboard                               | Purpose                                 | Main Focus                                        |
| --------------------------------------- | --------------------------------------- | ------------------------------------------------- |
| EV Charging Station Analytics Dashboard | High-level view of EV charging activity | Sessions, energy, revenue, and daily activity     |
| EV Station Performance & Operations     | Station-level performance analysis      | Station-wise sessions, city bands, and operations |
| EV Charging Maintenance & Reliability   | Maintenance and reliability analysis    | Station reliability and operational observations  |

---

## 4. Executive Dashboard Visuals

The main EV Charging Station Analytics dashboard contains:

* **Total EV Charging Sessions**
* **Total Energy (kWh)**
* **Estimated Revenue (INR)**
* **Daily EV Charging Sessions**
* **Station-wise Charging Sessions**
* **Sessions by City Band**
* **Activity Date slicer**

### Gold Source Mapping

| Visual                         | Gold Source                           |
| ------------------------------ | ------------------------------------- |
| Total EV Charging Sessions     | `default.gold_overall_daily_activity` |
| Total Energy (kWh)             | `default.gold_overall_daily_activity` |
| Estimated Revenue (INR)        | `default.gold_overall_daily_activity` |
| Daily EV Charging Sessions     | `default.gold_overall_daily_activity` |
| Station-wise Charging Sessions | `default.gold_station_daily_activity` |
| Sessions by City Band          | `default.gold_station_daily_activity` |

---

## 5. Measure Register

| Dashboard Measure              | Owning Gold Table                     | Business Meaning                |
| ------------------------------ | ------------------------------------- | ------------------------------- |
| Total EV Charging Sessions     | `default.gold_overall_daily_activity` | Total charging sessions         |
| Total Energy (kWh)             | `default.gold_overall_daily_activity` | Total energy delivered          |
| Estimated Revenue (INR)        | `default.gold_overall_daily_activity` | Estimated charging revenue      |
| Daily EV Charging Sessions     | `default.gold_overall_daily_activity` | Daily charging session activity |
| Station-wise Charging Sessions | `default.gold_station_daily_activity` | Charging sessions by station    |
| Sessions by City Band          | `default.gold_station_daily_activity` | Charging sessions by city band  |

**No unsupported KPI was added.**

---

## 6. Interaction and Filter Behavior

The **Activity Date slicer** was tested using **February 2026**.

### Visuals responding to the Activity Date slicer

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily EV Charging Sessions

### Independent station-level visuals

* Station-wise Charging Sessions
* Sessions by City Band

This behavior is expected because the overall and station-level summaries are stored in separate independent Gold tables.

No unsafe relationship was added to force cross-filtering.

---

## 7. Validation and Reconciliation

The dashboard was validated against the approved Gold outputs.

### February 2026 Session Reconciliation

| Validation Item       |                                Result |
| --------------------- | ------------------------------------: |
| Power BI              |                                 `89K` |
| Gold validation query |                              `89,484` |
| Gold table            | `default.gold_overall_daily_activity` |
| Status                |                              **PASS** |

The Power BI KPI displays **89K** because the visual uses rounded display formatting. The underlying Gold value is **89,484**.

### Validation Checks

* Gold-only data sources verified.
* Activity Date slicer tested.
* Overall KPI values checked against Gold data.
* Dashboard visuals traced to approved Gold tables.
* February 2026 reconciliation completed successfully.

---

## 8. Dashboard Insights

Detailed Week 9 dashboard observations are documented in:

```text
docs/dashboard_insights.md
```

The insights include:

* Overall charging activity
* Daily activity observations
* Station-level analysis
* City-band analysis
* Gold source usage
* February 2026 reconciliation
* Dashboard limitations

---

## 9. Dashboard Evidence

The Week 9 screenshots are stored in:

```text
screenshots/
```

### Screenshot 1 — EV Charging Station Analytics Dashboard

```text
screenshots/Week_09_EV CHARGING STATION ANALYTICS DASHBOARD.png
```

Shows the overall EV charging analytics dashboard.

### Screenshot 2 — EV Station Performance & Operations

```text
screenshots/Week_09_EV STATION PERFORMANCE & OPERATIONS.png
```

Shows station-level performance and operational analysis.

### Screenshot 3 — EV Charging Maintenance & Reliability

```text
screenshots/Week_09_EV CHARGING MAINTENANCE & RELIABILITY.png
```

Shows maintenance and reliability-related dashboard information.

---

## 10. Refresh

The dashboard uses the approved Gold tables as its data sources.

Before or after a refresh, verify:

* Total EV Charging Sessions
* Total Energy (kWh)
* Estimated Revenue (INR)
* Daily charging trend
* Station-wise sessions
* City-band sessions
* Activity Date slicer behavior
* Gold reconciliation

The Gold outputs were validated before the final Week 9 dashboard review.

---

## 11. Known Limitations

* The dashboard is based on the approved Week 8 Gold summaries.
* Streaming metrics are not included.
* Live-event metrics are not included.
* Real-time charging activity is not included.
* Streaming and live-event work belongs to **Week 10**.
* The dashboard does not provide causal explanations for changes in charging activity.
* The overall and station-level Gold tables remain independent by design.

---

## 12. Repository Structure

The expected project structure is:

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

## 13. Final PBIX File

The final Power BI report should be saved as:

```text
dashboard/powerbi_dashboard.pbix
```

If the working file is currently named:

```text
powerbi_dashboard_1.pbix
```

validate it in Power BI Desktop and save the final approved version as:

```text
dashboard/powerbi_dashboard.pbix
```

---

## 14. GitHub File Management

To keep the GitHub repository clean:

* Keep only the approved final PBIX file.
* Do not repeatedly upload multiple large PBIX versions.
* Store dashboard screenshots in `screenshots/`.
* Store dashboard insights in `docs/dashboard_insights.md`.
* Keep the final report at `dashboard/powerbi_dashboard.pbix`.
* Do not connect Power BI directly to raw, Bronze, or Silver sources.

---

## 15. Final Status

| Component                        | Status                             |
| -------------------------------- | ---------------------------------- |
| Gold source validation           | **PASS**                           |
| Power BI Gold-only sourcing      | **PASS**                           |
| Activity Date slicer test        | **PASS**                           |
| February 2026 reconciliation     | **PASS**                           |
| Dashboard screenshots            | **AVAILABLE**                      |
| Dashboard insights documentation | **AVAILABLE**                      |
| Final PBIX location              | `dashboard/powerbi_dashboard.pbix` |

### Week 9 Dashboard Status: **COMPLETE**
