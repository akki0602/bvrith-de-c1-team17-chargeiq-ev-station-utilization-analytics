# Week 07 Log — Gold Aggregations & Validation

**Week:** 7
**Date range:** [5/09/2026-10/09/2026]
**Team:** 17
**Project:** [Charge iq -ev-station-utilization-analytics]

---

## 1. Sprint Goal

Build the Gold-layer aggregation tables from approved Trusted Silver data and validate the Gold outputs for scope, join safety, grain, measure reconciliation, and controlled rerun stability.

The week also focused on documenting KPI definitions, identifying data-quality exceptions, and producing evidence for the Gold-layer implementation.

---

## 2. Work Completed

| Task                                                                          | Owner     | Status | Evidence                                                |
| ----------------------------------------------------------------------------- | --------- | ------ | ------------------------------------------------------- |
| Read approved Trusted Silver session, station, charger and maintenance inputs | team 17  | Done   | `notebooks/05_gold_aggregations.ipynb`                  |
| Created Station-Day Gold aggregation                                          | team 17  | Done   | `gold_station_daily_activity`, `week07_06`, `week07_07` |
| Created Station-Week Gold aggregation                                         | team 17  | Done   | `gold_station_weekly_activity`                          |
| Created Station-Month Gold aggregation                                        | team 17  | Done   | `gold_station_monthly_performance`                      |
| Created Charger-Day Gold aggregation                                          |team 17   | Done   | `gold_charger_daily_performance`                        |
| Created Connector-Type-Day Gold aggregation                                   | team 17  | Done   | `gold_connector_type_daily`                             |
| Created Vehicle-Class-Day Gold aggregation                                    | team 17  | Done   | `gold_vehicle_class_daily`                              |
| Created Tariff-Band-Day Gold aggregation                                      | team 17  | Done   | `gold_tariff_band_daily`                                |
| Created Maintenance-Day Gold aggregation                                      | team 17  | Done   | `gold_maintenance_daily`                                |
| Created Maintenance-Month Gold aggregation                                    | team 17  | Done   | `gold_maintenance_monthly`                              |
| Created Overall-Day Gold aggregation                                          | team 17  | Done   | `gold_overall_daily_activity`                           |
| Validated Trusted session scope                                               | team 17  | Done   | `week07_03`                                             |
| Validated station lookup and identified duplicate `STN0179`                   | team 17  | Done   | `week07_04`                                             |
| Validated join population and amplification                                   | team 17  | Done   | `week07_05`                                             |
| Validated Station-Day grain and measures                                      | team 17  | Done   | `week07_08`                                             |
| Reconciled Gold session measures with Trusted inputs                          | team 17  | Done   | `week07_09`                                             |
| Performed controlled rerun validation                                         | team 17  | Done   | `week07_10`                                             |
| Verified all 10 Gold tables exist                                             | team 17  | Done   | Gold table verification output                          |

---

## 3. Key Decisions

* Gold aggregations use only approved Trusted Silver inputs; Candidate and Quarantine records are not used as Gold inputs.
* Station-Day aggregation uses `arrival_ts` to derive the activity date.
* Station lookup attributes are deduplicated by `station_id` before joining to the session aggregation to prevent join amplification.
* `gold_processed_at` is treated as an audit timestamp and is excluded from business-column controlled-rerun comparison.
* The Trusted station data contains one conflicting duplicate key, `STN0179`. The two records have different station attributes, so this is documented as a Trusted-source data-quality exception rather than being silently treated as a clean unique lookup.
* Join validation confirmed that this lookup issue did not amplify the Gold session population.

---

## 4. Blockers / Risks

| Blocker                                                                   | Impact                                                    | Help Needed                                                                                 |
| ------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Conflicting duplicate `station_id` `STN0179` exists in `trusted_stations` | The same station key maps to different station attributes | Document the Trusted-source data-quality exception and retain the protected Gold join logic |
| No other blocking issue identified during Gold validation                 | Gold aggregation and validation could proceed             | None                                                                                        |

---

## 5. Evidence Added to GitHub

* `notebooks/05_gold_aggregations.ipynb`
* `docs/gold_metrics_definition.md`
* `weekly_logs/week07_log.md`
* `screenshots/week07_01.png`
* `screenshots/week07_02.png`
* `screenshots/week07_03.png`
* `screenshots/week07_04.png`
* `screenshots/week07_05.png`
* `screenshots/week07_06.png`
* `screenshots/week07_07.png`
* `screenshots/week07_08.png`
* `screenshots/week07_09.png`
* `screenshots/week07_10.png`

---

## 6. AI Transparency Note

| Question                            | Response                                                                                                                                                                                                                                                                                |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Where AI helped                     | AI assisted with structuring the Gold aggregation logic, validation queries, reconciliation checks, controlled rerun comparison, and documentation structure.                                                                                                                           |
| What we changed after AI suggestion | The Station-Day Gold aggregation was implemented using the approved Trusted Silver tables and the station lookup was protected with `dropDuplicates(["station_id"])`. The validation process was also adapted to document the conflicting `STN0179` lookup key.                         |
| What we verified manually           | Trusted session scope, join row counts, unmatched rows, join amplification, Station-Day grain, null keys, invalid measures, session-count reconciliation, completed-session reconciliation, Gold table existence, and controlled rerun results were executed and checked in Databricks. |
| What we can explain without AI      | The team can explain the Gold table grains, input tables, aggregation measures, join logic, validation results, reconciliation checks, and the `STN0179` data-quality exception.                                                                                                        |

---

## 7. Next Week Preparation

* Review the completed Gold metrics and validation evidence before the next sprint.
* Ensure all required screenshots, documentation, notebook changes, and weekly logs are committed to GitHub.
* Be prepared to explain Gold table grain, KPI definitions, aggregation logic, reconciliation results, and documented data-quality exceptions.
