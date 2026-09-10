# Gold Metrics Definition

**Week:** 7
**Purpose:** Define dashboard-ready Gold tables and KPI formulas.

---

## 1. Gold Table Catalog

| Gold Table Name                    | Grain                            | Source Table(s)                                                                      | Purpose                                                                          |
| ---------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| `gold_station_daily_activity`      | One row per Station + Day        | `workspace.silver_layer.trusted_sessions`, `workspace.silver_layer.trusted_stations` | Daily station-level session activity, energy, duration and estimated revenue     |
| `gold_station_weekly_activity`     | One row per Station + Week       | `workspace.silver_layer.trusted_sessions`, `workspace.silver_layer.trusted_stations` | Weekly station-level session, completion, energy, duration and revenue reporting |
| `gold_station_monthly_performance` | One row per Station + Month      | `workspace.silver_layer.trusted_sessions`, `workspace.silver_layer.trusted_stations` | Monthly station performance and charging activity                                |
| `gold_charger_daily_performance`   | One row per Charger + Day        | `workspace.silver_layer.trusted_sessions`                                            | Daily charger-level charging activity and performance                            |
| `gold_connector_type_daily`        | One row per Connector Type + Day | `workspace.silver_layer.trusted_sessions`                                            | Daily charging activity grouped by connector type                                |
| `gold_vehicle_class_daily`         | One row per Vehicle Class + Day  | `workspace.silver_layer.trusted_sessions`                                            | Daily charging activity grouped by vehicle class                                 |
| `gold_tariff_band_daily`           | One row per Tariff Band + Day    | `workspace.silver_layer.trusted_sessions`                                            | Daily session, energy and tariff-related reporting                               |
| `gold_maintenance_daily`           | One row per Station + Day        | `workspace.silver_layer.trusted_maintenance`                                         | Daily maintenance activity and operational issue reporting                       |
| `gold_maintenance_monthly`         | One row per Station + Month      | `workspace.silver_layer.trusted_maintenance`                                         | Monthly maintenance activity and trend reporting                                 |
| `gold_overall_daily_activity`      | One row per Day                  | `workspace.silver_layer.trusted_sessions`                                            | Overall daily charging activity across the Trusted session population            |

---

## 2. KPI Definitions

### Session KPIs

| KPI Name                | Formula                                                       | Grain                    | Dashboard Page   | Notes                                         |
| ----------------------- | ------------------------------------------------------------- | ------------------------ | ---------------- | --------------------------------------------- |
| Session Count           | `COUNT(*)` over eligible Trusted session records              | Daily / Weekly / Monthly | Station Activity | Counts eligible charging sessions             |
| Completed Session Count | `SUM(CASE WHEN final_status = 'COMPLETED' THEN 1 ELSE 0 END)` | Daily / Weekly / Monthly | Station Activity | Counts sessions with final status `COMPLETED` |
| Completion Rate         | `Completed Session Count / Session Count`                     | Daily / Weekly / Monthly | Performance      | Calculate only where Session Count > 0        |

### Energy KPIs

| KPI Name                     | Formula                        | Grain                    | Dashboard Page | Notes                                      |
| ---------------------------- | ------------------------------ | ------------------------ | -------------- | ------------------------------------------ |
| Total Energy (kWh)           | `SUM(COALESCE(energy_kwh, 0))` | Daily / Weekly / Monthly | Energy         | Uses Trusted session energy                |
| Average Session Energy (kWh) | `AVG(energy_kwh)`              | Daily / Weekly / Monthly | Energy         | Average of available session energy values |

### Duration KPIs

| KPI Name                           | Formula                 | Grain                    | Dashboard Page      | Notes                                                  |
| ---------------------------------- | ----------------------- | ------------------------ | ------------------- | ------------------------------------------------------ |
| Average Session Duration (minutes) | `AVG(duration_minutes)` | Daily / Weekly / Monthly | Session Performance | Uses the Trusted session duration measure              |
| Average Occupied Minutes           | `AVG(occupied_minutes)` | Daily / Weekly / Monthly | Utilization         | Uses the Trusted occupied-time measure where available |

### Revenue KPI

| KPI Name                | Formula                                                               | Grain                    | Dashboard Page | Notes                                         |
| ----------------------- | --------------------------------------------------------------------- | ------------------------ | -------------- | --------------------------------------------- |
| Estimated Revenue (INR) | `SUM(COALESCE(energy_kwh, 0) * COALESCE(tariff_rate_inr_per_kwh, 0))` | Daily / Weekly / Monthly | Revenue        | Estimated from energy and Trusted tariff rate |

### Maintenance KPIs

| KPI Name                        | Formula                        | Grain           | Dashboard Page | Notes                                             |
| ------------------------------- | ------------------------------ | --------------- | -------------- | ------------------------------------------------- |
| Maintenance Record Count        | `COUNT(*)`                     | Daily / Monthly | Maintenance    | Counts Trusted maintenance records                |
| Maintenance Activity by Station | `COUNT(*) GROUP BY station_id` | Daily / Monthly | Maintenance    | Supports station-level maintenance trend analysis |

### Category KPIs

| KPI Name                   | Formula                            | Grain | Dashboard Page     | Notes                                   |
| -------------------------- | ---------------------------------- | ----- | ------------------ | --------------------------------------- |
| Sessions by Connector Type | `COUNT(*) GROUP BY connector_type` | Daily | Connector Analysis | Based on Trusted session connector type |
| Sessions by Vehicle Class  | `COUNT(*) GROUP BY vehicle_class`  | Daily | Vehicle Analysis   | Based on Trusted session vehicle class  |
| Sessions by Tariff Band    | `COUNT(*) GROUP BY tariff_band`    | Daily | Tariff Analysis    | Based on Trusted session tariff band    |

---

## 3. Gold Table Row Counts

The following Gold tables were physically verified in `workspace.default`.

| Gold Table                         | Verified Rows |
| ---------------------------------- | ------------: |
| `gold_station_daily_activity`      |        15,660 |
| `gold_station_weekly_activity`     |         2,436 |
| `gold_station_monthly_performance` |           522 |
| `gold_charger_daily_performance`   |       103,282 |
| `gold_connector_type_daily`        |           450 |
| `gold_vehicle_class_daily`         |           450 |
| `gold_tariff_band_daily`           |           270 |
| `gold_maintenance_daily`           |         7,184 |
| `gold_maintenance_monthly`         |           549 |
| `gold_overall_daily_activity`      |            90 |

---

## 4. Station-Day Gold Validation

The Station-Day Gold table `gold_station_daily_activity` was validated using the following checks.

### Scope

* Total Trusted sessions: **286,902**
* Eligible sessions: **286,902**
* Outside-scope sessions: **0**
* Scope reconciliation: **True**

### Join

* Pre-join eligible rows: **286,902**
* Post-join rows: **286,902**
* Unmatched station rows: **0**
* Join amplification: **0**
* Population preserved: **True**

### Grain and Measures

* Duplicate Station-Day groups: **0**
* Null key rows: **0**
* Invalid measure rows: **0**

### Measure Reconciliation

* Trusted eligible sessions: **286,902**

* Gold daily session total: **286,902**

* Difference: **0**

* Reconciliation: **True**

* Trusted completed sessions: **261,457**

* Gold completed total: **261,457**

* Difference: **0**

* Reconciliation: **True**

### Controlled Rerun

* Baseline Gold rows: **15,660**
* Rerun Gold rows: **15,660**
* Baseline minus rerun: **0**
* Rerun minus baseline: **0**
* Controlled rerun stable: **True**

---

## 5. Data Quality Exception

A duplicate `station_id` was identified in the Trusted station lookup:

**`STN0179`**

The two Trusted records contain conflicting station attributes, including different station names, city bands, zones and site types.

The Gold station lookup therefore applies station-level deduplication on `station_id` before joining station attributes to the session aggregation.

This exception is documented as a Trusted-source data-quality finding. It should not be represented as a clean lookup-uniqueness pass.

Despite the source exception, the Gold join validation confirmed zero unmatched rows and zero join amplification, and the eligible session population was completely preserved.

---

## 6. Validation Checks

Before using Gold tables for dashboard consumption, verify:

* Gold tables physically exist in the expected Gold catalog/schema.
* Gold row counts are recorded and reviewed.
* Gold keys match the declared grain.
* No duplicate business keys exist at the declared grain.
* Required dashboard fields do not contain unexpected nulls.
* Measures contain valid values.
* Gold session totals reconcile with the eligible Trusted session population.
* Completed-session totals reconcile with Trusted data.
* Joins do not cause row amplification or unexpected population loss.
* KPI formulas are documented and traceable to Trusted inputs.
* Controlled reruns using the same Trusted snapshot reproduce the same business rows.
* Candidate and Quarantine data are not used as Gold inputs.
* Any Trusted-source data-quality exceptions affecting dimensions or measures are explicitly documented.

---

## 7. Gold Consumption Boundary

Gold tables are designed as dashboard-ready analytical outputs.

The Gold layer consumes approved Trusted Silver data and provides aggregated business metrics at declared grains such as Station-Day, Station-Week, Station-Month, Charger-Day and category-Day.

Candidate and Quarantine records are excluded from Gold processing.

Any downstream dashboard or reporting layer should consume the documented Gold outputs rather than directly querying Candidate or Quarantine data.
