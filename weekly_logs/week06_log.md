# Week 06 Log — Data Quality Implementation

**Week:** 6
**Date range:** [Add actual Week 6 dates]
**Team:** Team 17
**Project:** P17 ChargeIQ

---

## 1. Sprint Goal

Implement the approved Week 6 Data Quality (DQ) rules against the available Silver Candidate datasets.

Establish rule-level validation, Trusted/Quarantine routing, rule-occurrence tracking, and physical-record reconciliation while documenting unavailable upstream/configuration dependencies.

---

## 2. Work Completed

| Task                                                    | Owner   | Status  | Evidence                                                |
| ------------------------------------------------------- | ------- | ------- | ------------------------------------------------------- |
| Implemented station master DQ — DQ-CHG-002              | Team 17 | Done    | `04_data_quality_checks.ipynb`, Week 6 screenshots      |
| Implemented charger master DQ — DQ-CHG-001              | Team 17 | Done    | `04_data_quality_checks.ipynb`, Week 6 screenshots      |
| Implemented session identity DQ — DQ-SES-001            | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Implemented session reference/alignment DQ — DQ-SES-002 | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Implemented chronology/window DQ — DQ-SES-003           | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Implemented lifecycle DQ — DQ-SES-004                   | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Implemented occupancy/capacity DQ — DQ-SES-005          | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Implemented measures/ranges DQ — DQ-SES-006             | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Investigated physical-plausibility DQ — DQ-SES-007      | Team 17 | Blocked | Approved tolerance/efficiency configuration unavailable |
| Implemented maintenance integrity DQ — DQ-MNT-001       | Team 17 | Done    | `04_data_quality_checks.ipynb`                          |
| Investigated charger status-events DQ — DQ-EVT-001      | Team 17 | Blocked | Events Bronze/Candidate source unavailable              |
| Implemented Trusted/Quarantine routing                  | Team 17 | Done    | DQ output tables                                        |
| Implemented session DQ rule-occurrence tracking         | Team 17 | Done    | `dq_session_rule_occurrences`                           |
| Performed physical-record reconciliation                | Team 17 | Done    | Final reconciliation output                             |
| Created Week 6 DQ rule status                           | Team 17 | Done    | `week6_dq_rule_status`                                  |

### Reconciliation Results

| Domain      | Candidate | Trusted | Quarantine | Overlap | Variance |
| ----------- | --------: | ------: | ---------: | ------: | -------: |
| Stations    |       180 |     178 |          2 |       0 |        0 |
| Chargers    |     1,200 |   1,177 |         23 |       0 |        0 |
| Sessions    |   300,000 | 286,902 |     13,098 |       0 |        0 |
| Maintenance |    18,000 |  17,849 |        151 |       0 |        0 |

All available domains achieved zero Trusted/Quarantine overlap and zero physical-record variance.

---

## 3. Key Decisions

* Use `physical_record_id` as the physical-record reconciliation key.
* Route a physical record to Quarantine if it fails one or more applicable DQ rules.
* Retain all failed rule IDs for a record when multiple rules fail.
* Keep rule occurrences separate from physical quarantine-record counts.
* Do not invent DQ-SES-007 tolerance or efficiency thresholds when the approved configuration is unavailable.
* Do not fabricate charger status-event data when the required upstream Events source is unavailable.
* Quarantined records must not be promoted directly to Trusted without corrected-input replay through the DQ rules.

---

## 4. Blockers / Risks

| Blocker                                                            | Impact                                                                 | Help Needed                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------ |
| Approved DQ-SES-007 efficiency/tolerance configuration unavailable | DQ-SES-007 cannot be finalized without inventing an approved threshold | Obtain the approved project configuration              |
| Charger status-events Bronze/Candidate source unavailable          | DQ-EVT-001 cannot be implemented or validated                          | Obtain the upstream charger status-events source/table |

---

## 5. Evidence Added to GitHub

* `notebooks/04_data_quality_checks.ipynb`
* `docs/data_quality_summary.md`
* `weekly_logs/week06_log.md`
* `src/data_quality_rules.py`
* `screenshots/week06_*.png`

---

## 6. AI Transparency Note

| Question                            | Response                                                                                                                                                                                                                                  |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Where AI helped                     | AI was used to assist with DQ-rule implementation structure, PySpark code patterns, validation logic, routing logic, reconciliation checks, and documentation drafting.                                                                   |
| What we changed after AI suggestion | Code and rule implementation were adapted to the actual Week 5 Candidate schemas, available tables, approved Week 6 rule IDs, and project-specific constraints.                                                                           |
| What we verified manually           | Candidate record counts, Trusted/Quarantine counts, physical-record reconciliation, Trusted/Quarantine overlap, failed-rule occurrences, available schemas, and availability of upstream/configuration inputs were checked in Databricks. |
| What we can explain without AI      | The team can explain the DQ rules, why records are routed to Trusted or Quarantine, the reconciliation methodology, multi-rule failure handling, and why DQ-SES-007 and DQ-EVT-001 remain blocked.                                        |

---

## 7. Next Week Preparation

* Resolve the DQ-SES-007 approved efficiency/tolerance configuration dependency.
* Obtain and inspect the charger status-events source required for DQ-EVT-001.
* Complete the blocked DQ rules when their required inputs become available.
* Review Week 6 DQ outputs before downstream Gold-layer consumption.
* Prepare the validated Trusted datasets and DQ evidence for the next sprint.
