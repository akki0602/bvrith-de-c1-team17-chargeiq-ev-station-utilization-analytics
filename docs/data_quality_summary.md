# Data Quality Summary

**Week:** 6
**Purpose:** Summarize approved data quality rules, failures, routing, and business impact.

---

## 1. Quality Rule Results

### Stations — DQ-CHG-002

| Rule ID    | Rule Name                | Severity | Passed Count | Failed Count | Business Impact                                                                                          |
| ---------- | ------------------------ | -------- | -----------: | -----------: | -------------------------------------------------------------------------------------------------------- |
| DQ-CHG-002 | Station master integrity | CRITICAL |          178 |            2 | Invalid station master records can cause incorrect capacity, operating-hour and station-level reporting. |

### Chargers — DQ-CHG-001

| Rule ID    | Rule Name                | Severity | Passed Count | Failed Count | Business Impact                                                                                                                           |
| ---------- | ------------------------ | -------- | -----------: | -----------: | ----------------------------------------------------------------------------------------------------------------------------------------- |
| DQ-CHG-001 | Charger master integrity | CRITICAL |        1,177 |           23 | Invalid charger references, station mappings or charger attributes can affect session joins, capacity analysis and charger-level metrics. |

### Sessions

| Rule ID    | Rule Name                               | Severity | Passed Count | Failed Count | Business Impact                                                                                                    |
| ---------- | --------------------------------------- | -------- | -----------: | -----------: | ------------------------------------------------------------------------------------------------------------------ |
| DQ-SES-001 | Session identity and uniqueness         | CRITICAL |     298,800* |       1,200* | Missing or duplicate session identity can distort session counts and downstream metrics.                           |
| DQ-SES-002 | Station/charger reference and alignment | CRITICAL |      299,100 |          900 | Invalid station/charger references can produce incorrect joins and charger/station metrics.                        |
| DQ-SES-003 | Chronology and reporting window         | MAJOR    |      289,996 |       10,004 | Invalid timestamps can make duration, utilization and time-based reporting unreliable.                             |
| DQ-SES-004 | Lifecycle consistency                   | MAJOR    |      299,798 |          202 | Inconsistent session lifecycle information can misrepresent completed, interrupted or cancelled charging sessions. |
| DQ-SES-005 | Occupancy and capacity                  | CRITICAL |      298,407 |        1,593 | Overlapping sessions or capacity violations can distort charger utilization and station occupancy metrics.         |
| DQ-SES-006 | Measures and ranges                     | MAJOR    |      289,945 |       10,055 | Invalid energy or duration measures can directly affect charging, utilization and operational KPIs.                |
| DQ-SES-007 | Physical plausibility                   | MAJOR    |            — |            — | Blocked because the approved efficiency/tolerance configuration is unavailable. No threshold was invented.         |

* DQ-SES-001 was evaluated in two stages. The initial null/blank check found 400 failures and the duplicate-identity check found 400 duplicate session IDs. The final corrected identity evaluation identified 1,200 affected records.

### Maintenance

| Rule ID    | Rule Name             | Severity | Passed Count | Failed Count | Business Impact                                                                              |
| ---------- | --------------------- | -------- | -----------: | -----------: | -------------------------------------------------------------------------------------------- |
| DQ-MNT-001 | Maintenance integrity | MAJOR    |       17,849 |          151 | Invalid maintenance references or chronology can affect fault, repair and recovery analysis. |

### Charger Status Events

| Rule ID    | Rule Name                         | Severity | Passed Count | Failed Count | Business Impact                                                                            |
| ---------- | --------------------------------- | -------- | -----------: | -----------: | ------------------------------------------------------------------------------------------ |
| DQ-EVT-001 | Status-event streaming governance | MAJOR    |            — |            — | Blocked because the required charger status-events Bronze/Candidate source is unavailable. |

---

## 2. Failed Record Examples

| Rule ID    | Sample Record ID    | Failure Reason                                                                    | Action / Handling |
| ---------- | ------------------- | --------------------------------------------------------------------------------- | ----------------- |
| DQ-CHG-002 | STNREC000176        | Missing station ID and invalid connector capacity                                 | Quarantined       |
| DQ-CHG-002 | STNREC000177        | Invalid operating-hour configuration                                              | Quarantined       |
| DQ-CHG-001 | CHGREC0001174       | Charger ID is NULL                                                                | Quarantined       |
| DQ-CHG-001 | CHGREC0001176       | Charger ID is NULL                                                                | Quarantined       |
| DQ-CHG-001 | CHGREC0001200       | Duplicate charger identity                                                        | Quarantined       |
| DQ-SES-002 | Session records     | Station/charger reference missing, unresolved or misaligned                       | Quarantined       |
| DQ-SES-003 | Session records     | Invalid chronology or reporting date outside approved Jan–Mar 2026 window         | Quarantined       |
| DQ-SES-005 | Session records     | Same-charger overlap or station capacity violation                                | Quarantined       |
| DQ-SES-006 | Session records     | Invalid energy/duration/occupied-minute measure                                   | Quarantined       |
| DQ-MNT-001 | Maintenance records | Unresolved reference, station/charger mismatch or invalid fault/repair chronology | Quarantined       |

---

## 3. What Should Block Gold Metrics?

The following conditions should block or flag Gold metrics:

* **CRITICAL DQ failures** should not flow into trusted Gold-consuming datasets because they can compromise identity, references, capacity or core master-data integrity.
* **DQ-SES-001** failures should block session-count metrics because duplicate or missing session identity can double-count or lose charging sessions.
* **DQ-SES-002** failures should block station/charger-level metrics because invalid references can create incorrect joins.
* **DQ-SES-005** failures should block or flag utilization and occupancy metrics because overlapping sessions and capacity violations affect operational calculations.
* **DQ-SES-003 and DQ-SES-006** failures should be excluded from affected time-based and measure-based metrics.
* **DQ-SES-007** must remain blocked until the approved physical-plausibility tolerance/efficiency configuration is provided.
* **DQ-EVT-001** must remain blocked until the required charger status-events source is available.

Only records that pass all applicable DQ rules should be promoted to the Trusted layer for downstream Gold processing.

---

## 4. Quality Summary

The Week 6 DQ implementation identified quality issues across the available Station, Charger, Session and Maintenance Candidate datasets. The largest session-level failure counts were observed in **DQ-SES-003 (10,004 failures)** and **DQ-SES-006 (10,055 failures)**. These failures are particularly important for dashboards because invalid timestamps and measures can directly affect duration, utilization, energy and operational KPIs. Critical reference and capacity failures were also quarantined to prevent unreliable station and charger metrics from reaching downstream layers. Failed records were routed to Quarantine while records passing all applicable rules were routed to Trusted. Multi-rule failures were retained as multiple rule occurrences while the physical record was quarantined only once. The mentor should review the high session failure volumes, the capacity/overlap violations, and the two blocked dependencies: the approved DQ-SES-007 tolerance/efficiency configuration and the missing DQ-EVT-001 status-events source.
