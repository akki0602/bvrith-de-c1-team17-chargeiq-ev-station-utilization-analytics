# Week 05 Log — Silver Candidate Typing, Standardisation and Derivations

**Week:** 5
**Date range:** [Add actual Week 05 dates]
**Team:** Team 17
**Project:** P17 ChargeIQ — EV Station Utilization Analytics

---

## 1. Sprint Goal

Build the Silver Candidate layer for ChargeIQ by safely typing Bronze data, standardising approved categorical fields, retaining raw values and lineage, and deriving the required session and maintenance fields.

Validate that Silver Candidate preserves the original physical-record grain and reconciles with Bronze without silently dropping or duplicating records.

---

## 2. Work Completed

| Task                                                                          | Owner   | Status | Evidence                                    |
| ----------------------------------------------------------------------------- | ------- | ------ | ------------------------------------------- |
| Create Silver Candidate table for stations                                    | Team 17 | Done   | `notebooks/03_silver_transformations.ipynb` |
| Safely type station hours, capacity, boolean, date and coordinate-like fields | Team 17 | Done   | Silver transformation notebook              |
| Create Silver Candidate table for chargers                                    | Team 17 | Done   | `notebooks/03_silver_transformations.ipynb` |
| Safely type rated power, install date, firmware and connector position        | Team 17 | Done   | Silver transformation notebook              |
| Standardise approved charger connector/status fields                          | Team 17 | Done   | Silver transformation notebook              |
| Create Silver Candidate table for sessions                                    | Team 17 | Done   | `notebooks/03_silver_transformations.ipynb` |
| Safely type session timestamps and decimal/measure fields                     | Team 17 | Done   | Silver transformation notebook              |
| Retain raw values and Bronze lineage for typed fields                         | Team 17 | Done   | Silver transformation notebook              |
| Derive session duration and occupied minutes                                  | Team 17 | Done   | Silver transformation notebook              |
| Derive average power and energy-per-minute fields                             | Team 17 | Done   | Silver transformation notebook              |
| Derive lifecycle and utilization eligibility flags                            | Team 17 | Done   | Silver transformation notebook              |
| Derive peak time band and standardised categorical fields                     | Team 17 | Done   | Silver transformation notebook              |
| Create Silver Candidate maintenance table                                     | Team 17 | Done   | `notebooks/03_silver_transformations.ipynb` |
| Safely type maintenance event timestamp and planned flag                      | Team 17 | Done   | Silver transformation notebook              |
| Derive incident event sequence and recovery fields                            | Team 17 | Done   | Silver transformation notebook              |
| Reconcile Bronze and Silver Candidate physical record IDs                     | Team 17 | Done   | Validation cells / screenshots              |
| Perform controlled rerun validation                                           | Team 17 | Done   | Notebook rerun evidence                     |

---

## 3. Key Decisions

* Silver Candidate preserves the original physical-record grain and does not remove records during casting or enrichment.
* Safe conversions are used so that invalid source values remain visible through raw and typed shadow fields for later Data Quality processing.
* Approved categorical standardisation is applied without converting unknown values into valid categories.
* Session derivations are calculated from valid typed timestamps and measures.
* Maintenance sequencing is performed within incident lineage rather than through session joins.
* Bronze-to-Silver Candidate reconciliation is performed using `physical_record_id` at every entity grain.
* Silver Candidate is treated as **not trusted**; Data Quality rules in Week 06 determine whether records enter Trusted Silver or Quarantine.

---

## 4. Blockers / Risks

| Blocker                                   | Impact                                                   | Help Needed                                                        |
| ----------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------ |
| Some source values may fail safe casting  | Typed value can become NULL                              | Retain raw value and allow Week 06 DQ to evaluate the record       |
| Unknown categorical values may occur      | Incorrect default mapping could hide data-quality issues | Keep normalized value visible and retain the original value        |
| Derived values depend on valid timestamps | Invalid timestamps can prevent duration calculations     | Use conditional derivation and retain the raw/typed timestamp pair |
| Incorrect joins could change row grain    | Candidate reconciliation could fail                      | Use grain-safe transformations and validate physical record counts |

---

## 5. Evidence Added to GitHub

* `notebooks/03_silver_transformations.ipynb`
* `weekly_logs/week05_log.md`
* Week 05 Silver Candidate validation screenshots
* Candidate schema and count evidence
* Bronze-to-Candidate reconciliation evidence
* Controlled rerun evidence

---

## 6. AI Transparency Note

| Question                            | Response                                                                                                                                                                                                                               |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Where AI helped                     | AI helped structure the Silver Candidate transformation workflow, explain safe casting, suggest validation queries, and organize the notebook into transformation and validation stages.                                               |
| What we changed after AI suggestion | We adapted the suggested transformations to the approved ChargeIQ field dictionary, table names and project grain instead of blindly using generic transformations.                                                                    |
| What we verified manually           | We manually checked Candidate schemas, row counts, distinct `physical_record_id` counts, typed columns, derived fields, raw/typed values and Bronze-to-Candidate reconciliation.                                                       |
| What we can explain without AI      | We can explain why Silver Candidate uses safe casting, why raw values are retained, how session and maintenance derivations are produced, why Candidate records are not deleted, and why reconciliation is required before Week 06 DQ. |

---

## 7. Next Week Preparation

* Execute the 11 governed Week 06 Data Quality rules against the Silver Candidate tables.
* Create Trusted Silver and Quarantine outputs while retaining multi-rule failure evidence.
* Reconcile Candidate records against Trusted Silver and Quarantine.
* Prepare the controlled replay evidence for a corrected quarantined record.
