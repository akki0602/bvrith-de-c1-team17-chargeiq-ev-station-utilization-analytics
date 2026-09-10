```python
"""
Data Quality Rules
Project: P17 ChargeIQ
Team: 17
Week: 6

Purpose:
    Reusable PySpark helper functions for the approved Week 6
    Data Quality (DQ) rules.

Implemented:
    DQ-CHG-002  Station Master
    DQ-CHG-001  Charger Master
    DQ-SES-001  Session Identity
    DQ-SES-002  Station/Charger Reference and Alignment
    DQ-SES-003  Session Chronology / Reporting Window
    DQ-SES-004  Session Lifecycle
    DQ-SES-005  Occupancy / Capacity
    DQ-SES-006  Measures / Ranges
    DQ-MNT-001  Maintenance Integrity

Blocked:
    DQ-SES-007  Physical Plausibility
        Reason: Approved efficiency/tolerance configuration is unavailable.

    DQ-EVT-001  Status Event Streaming Governance
        Reason: Events Bronze/Candidate source is unavailable.

Important:
    - A physical record can fail multiple DQ rules.
    - All failed rule IDs should be retained.
    - Routing is performed once after all applicable rules are evaluated.
    - physical_record_id is the reconciliation key.
    - Rule occurrence counts are not physical-record counts.
"""

from pyspark.sql import functions as F
from pyspark.sql.window import Window


# ============================================================
# Constants
# ============================================================

REPORTING_START = "2026-01-01"
REPORTING_END = "2026-03-31"

DQ_SEVERITY = {
    "DQ-CHG-001": "CRITICAL",
    "DQ-CHG-002": "CRITICAL",
    "DQ-SES-001": "CRITICAL",
    "DQ-SES-002": "CRITICAL",
    "DQ-SES-003": "MAJOR",
    "DQ-SES-004": "MAJOR",
    "DQ-SES-005": "CRITICAL",
    "DQ-SES-006": "MAJOR",
    "DQ-SES-007": "MAJOR",
    "DQ-MNT-001": "MAJOR",
    "DQ-EVT-001": "MAJOR",
}


# ============================================================
# Generic reusable rules
# ============================================================

def required_field_rule(df, field_name):
    """
    Return records where a required field is null or blank.
    """
    return df.filter(
        F.col(field_name).isNull()
        | (F.trim(F.col(field_name).cast("string")) == "")
    )


def non_negative_rule(df, field_name):
    """
    Return records where a numeric field is negative.
    """
    return df.filter(F.col(field_name) < 0)


def duplicate_key_rule(df, key_field):
    """
    Return duplicate keys and their counts.
    """
    return (
        df.groupBy(key_field)
        .count()
        .filter(F.col("count") > 1)
    )


def valid_reference_rule(
    fact_df,
    reference_df,
    fact_key,
    reference_key
):
    """
    Return records from fact_df where fact_key does not exist
    in reference_df.
    """
    return fact_df.join(
        reference_df,
        fact_df[fact_key] == reference_df[reference_key],
        "left_anti"
    )


def null_or_blank_condition(field_name):
    """
    Reusable condition for null or blank string values.
    """
    return (
        F.col(field_name).isNull()
        | (F.trim(F.col(field_name).cast("string")) == "")
    )


# ============================================================
# Routing helpers
# ============================================================

def add_failed_rule(
    df,
    condition,
    rule_id,
    reason,
    affected_field
):
    """
    Add a failed DQ rule to a record.

    Existing failed_rule_ids are preserved so that a physical
    record can retain multiple rule failures.
    """

    return (
        df
        .withColumn(
            "failed_rule_ids",
            F.when(
                condition,
                F.array_union(
                    F.coalesce(
                        F.col("failed_rule_ids"),
                        F.array().cast("array<string>")
                    ),
                    F.array(F.lit(rule_id))
                )
            ).otherwise(
                F.coalesce(
                    F.col("failed_rule_ids"),
                    F.array().cast("array<string>")
                )
            )
        )
        .withColumn(
            "dq_failure_reasons",
            F.when(
                condition,
                F.array_union(
                    F.coalesce(
                        F.col("dq_failure_reasons"),
                        F.array().cast("array<string>")
                    ),
                    F.array(F.lit(reason))
                )
            ).otherwise(
                F.coalesce(
                    F.col("dq_failure_reasons"),
                    F.array().cast("array<string>")
                )
            )
        )
        .withColumn(
            "dq_affected_fields",
            F.when(
                condition,
                F.array_union(
                    F.coalesce(
                        F.col("dq_affected_fields"),
                        F.array().cast("array<string>")
                    ),
                    F.array(F.lit(affected_field))
                )
            ).otherwise(
                F.coalesce(
                    F.col("dq_affected_fields"),
                    F.array().cast("array<string>")
                )
            )
        )
    )


def initialize_dq_columns(df):
    """
    Initialize reusable DQ tracking columns.
    """

    return (
        df
        .withColumn(
            "failed_rule_ids",
            F.array().cast("array<string>")
        )
        .withColumn(
            "dq_failure_reasons",
            F.array().cast("array<string>")
        )
        .withColumn(
            "dq_affected_fields",
            F.array().cast("array<string>")
        )
    )


def add_route_column(df):
    """
    Route records after all applicable DQ rules are evaluated.

    PASS -> Trusted
    One or more failures -> Quarantine
    """

    return df.withColumn(
        "route",
        F.when(
            F.size(F.col("failed_rule_ids")) == 0,
            F.lit("TRUSTED")
        ).otherwise(
            F.lit("QUARANTINE")
        )
    )


# ============================================================
# DQ-CHG-002 — Station Master
# ============================================================

def check_station_master(df):
    """
    Apply DQ-CHG-002 to the station Candidate dataset.

    Checks:
        - station_id required
        - connector capacity valid
        - operating hours valid
        - 24x7 consistency
        - commission date required
        - station status/site type required
    """

    result = initialize_dq_columns(df)

    result = add_failed_rule(
        result,
        null_or_blank_condition("station_id"),
        "DQ-CHG-002",
        "station_id is null or blank",
        "station_id"
    )

    result = add_failed_rule(
        result,
        F.col("connector_capacity").isNull()
        | (F.col("connector_capacity") <= 0),
        "DQ-CHG-002",
        "connector capacity is missing or invalid",
        "connector_capacity"
    )

    result = add_failed_rule(
        result,
        F.col("operating_start_hour").isNull()
        | F.col("operating_end_hour").isNull()
        | (F.col("operating_start_hour") < 0)
        | (F.col("operating_start_hour") > 23)
        | (F.col("operating_end_hour") < 0)
        | (F.col("operating_end_hour") > 24),
        "DQ-CHG-002",
        "operating hours are missing or outside the approved domain",
        "operating_start_hour,operating_end_hour"
    )

    result = add_failed_rule(
        result,
        F.col("is_24x7").isNull(),
        "DQ-CHG-002",
        "24x7 indicator is missing",
        "is_24x7"
    )

    result = add_failed_rule(
        result,
        F.col("commission_date").isNull(),
        "DQ-CHG-002",
        "commission date is missing",
        "commission_date"
    )

    result = add_failed_rule(
        result,
        null_or_blank_condition("site_type"),
        "DQ-CHG-002",
        "site type is missing",
        "site_type"
    )

    result = add_failed_rule(
        result,
        null_or_blank_condition("station_status"),
        "DQ-CHG-002",
        "station status is missing",
        "station_status"
    )

    return add_route_column(result)


# ============================================================
# DQ-CHG-001 — Charger Master
# ============================================================

def check_charger_master(
    charger_df,
    trusted_station_df
):
    """
    Apply DQ-CHG-001 to the charger Candidate dataset.

    Checks:
        - charger_id required
        - duplicate charger identity
        - station reference resolves to trusted station
        - rated power is present and positive
        - install date is valid
        - operational status is present
        - connector position/type are present
    """

    result = initialize_dq_columns(charger_df)

    # Required charger identity
    result = add_failed_rule(
        result,
        null_or_blank_condition("charger_id"),
        "DQ-CHG-001",
        "charger_id is null or blank",
        "charger_id"
    )

    # Duplicate charger IDs
    duplicate_ids = (
        charger_df
        .groupBy("charger_id")
        .count()
        .filter(
            (F.col("count") > 1)
            & F.col("charger_id").isNotNull()
        )
        .select("charger_id")
        .withColumn("duplicate_flag", F.lit(True))
    )

    result = (
        result
        .join(duplicate_ids, "charger_id", "left")
        .withColumn(
            "duplicate_flag",
            F.coalesce(F.col("duplicate_flag"), F.lit(False))
        )
    )

    result = add_failed_rule(
        result,
        F.col("duplicate_flag"),
        "DQ-CHG-001",
        "charger_id is duplicated",
        "charger_id"
    )

    # Station reference
    trusted_station_ids = (
        trusted_station_df
        .select("station_id")
        .dropDuplicates()
    )

    unresolved_station = (
        result
        .join(
            trusted_station_ids,
            "station_id",
            "left"
        )
        .withColumn(
            "station_resolved",
            F.col("station_id").isNotNull()
            & F.col("station_id").isNotNull()
        )
    )

    unresolved_ids = (
        result
        .join(
            trusted_station_ids,
            "station_id",
            "left_anti"
        )
        .select("physical_record_id")
        .distinct()
        .withColumn("station_unresolved", F.lit(True))
    )

    result = result.join(
        unresolved_ids,
        "physical_record_id",
        "left"
    )

    result = add_failed_rule(
        result,
        F.coalesce(
            F.col("station_unresolved"),
            F.lit(False)
        ),
        "DQ-CHG-001",
        "station reference is unresolved",
        "station_id"
    )

    # Rated power
    result = add_failed_rule(
        result,
        F.col("rated_power_kw").isNull()
        | (F.col("rated_power_kw") <= 0),
        "DQ-CHG-001",
        "rated power is missing or invalid",
        "rated_power_kw"
    )

    # Install date
    result = result.withColumn(
        "_install_date_parsed",
        F.to_date("install_date")
    )

    result = add_failed_rule(
        result,
        F.col("_install_date_parsed").isNull(),
        "DQ-CHG-001",
        "install date is missing or cannot be parsed",
        "install_date"
    )

    # Status
    result = add_failed_rule(
        result,
        null_or_blank_condition("operational_status"),
        "DQ-CHG-001",
        "operational status is missing",
        "operational_status"
    )

    # Connector
    result = add_failed_rule(
        result,
        F.col("connector_position").isNull()
        | null_or_blank_condition("connector_type"),
        "DQ-CHG-001",
        "connector information is missing",
        "connector_position,connector_type"
    )

    return add_route_column(
        result.drop(
            "_install_date_parsed",
            "duplicate_flag",
            "station_unresolved"
        )
    )


# ============================================================
# DQ-SES-001 — Session Identity
# ============================================================

def check_session_identity(df):
    """
    Apply DQ-SES-001.

    Checks:
        - session_id must not be null/blank
        - duplicate session_id values are quarantined
    """

    result = initialize_dq_columns(df)

    result = add_failed_rule(
        result,
        null_or_blank_condition("session_id"),
        "DQ-SES-001",
        "session_id is null or blank",
        "session_id"
    )

    duplicate_ids = (
        df
        .filter(F.col("session_id").isNotNull())
        .groupBy("session_id")
        .count()
        .filter(F.col("count") > 1)
        .select("session_id")
        .withColumn("duplicate_session", F.lit(True))
    )

    result = result.join(
        duplicate_ids,
        "session_id",
        "left"
    )

    result = add_failed_rule(
        result,
        F.coalesce(
            F.col("duplicate_session"),
            F.lit(False)
        ),
        "DQ-SES-001",
        "session_id is duplicated",
        "session_id"
    )

    return result.drop("duplicate_session")


# ============================================================
# DQ-SES-002 — Station / Charger Reference
# ============================================================

def check_session_references(
    session_df,
    trusted_station_df,
    trusted_charger_df
):
    """
    Apply DQ-SES-002.

    Checks:
        - station exists
        - charger exists
        - charger belongs to stated station
    """

    result = session_df

    station_ref = (
        trusted_station_df
        .select(
            F.col("station_id").alias("_ref_station_id")
        )
        .dropDuplicates()
    )

    charger_ref = (
        trusted_charger_df
        .select(
            F.col("charger_id").alias("_ref_charger_id"),
            F.col("station_id").alias("_charger_station_id")
        )
        .dropDuplicates()
    )

    result = (
        result
        .join(
            station_ref,
            result.station_id == station_ref._ref_station_id,
            "left"
        )
        .join(
            charger_ref,
            result.charger_id == charger_ref._ref_charger_id,
            "left"
        )
    )

    station_missing = (
        F.col("station_id").isNull()
        | F.col("_ref_station_id").isNull()
    )

    charger_missing = (
        F.col("charger_id").isNull()
        | F.col("_ref_charger_id").isNull()
    )

    station_mismatch = (
        ~station_missing
        & ~charger_missing
        & (
            F.col("station_id")
            != F.col("_charger_station_id")
        )
    )

    result = add_failed_rule(
        result,
        station_missing,
        "DQ-SES-002",
        "station reference is missing or unresolved",
        "station_id"
    )

    result = add_failed_rule(
        result,
        charger_missing,
        "DQ-SES-002",
        "charger reference is missing or unresolved",
        "charger_id"
    )

    result = add_failed_rule(
        result,
        station_mismatch,
        "DQ-SES-002",
        "charger belongs to a different station",
        "station_id,charger_id"
    )

    return result.drop(
        "_ref_station_id",
        "_ref_charger_id",
        "_charger_station_id"
    )


# ============================================================
# DQ-SES-003 — Chronology / Reporting Window
# ============================================================

def check_session_chronology(df):
    """
    Apply DQ-SES-003.

    Checks:
        - required timestamps are present
        - timestamps are chronologically ordered
        - arrival/reporting date falls in Jan-Mar 2026
    """

    result = df

    timestamp_missing = (
        F.col("arrival_ts").isNull()
        | F.col("charge_start_ts").isNull()
        | F.col("charge_end_ts").isNull()
        | F.col("departure_ts").isNull()
    )

    chronology_invalid = (
        ~timestamp_missing
        & (
            (F.col("arrival_ts") > F.col("charge_start_ts"))
            | (F.col("charge_start_ts") > F.col("charge_end_ts"))
            | (F.col("charge_end_ts") > F.col("departure_ts"))
        )
    )

    reporting_window_invalid = (
        F.col("arrival_ts").isNull()
        | ~(
            F.to_date("arrival_ts").between(
                F.lit(REPORTING_START),
                F.lit(REPORTING_END)
            )
        )
    )

    result = add_failed_rule(
        result,
        timestamp_missing,
        "DQ-SES-003",
        "one or more required session timestamps cannot be parsed or are missing",
        "arrival_ts,charge_start_ts,charge_end_ts,departure_ts"
    )

    result = add_failed_rule(
        result,
        chronology_invalid,
        "DQ-SES-003",
        "session timestamps are out of chronological order",
        "arrival_ts,charge_start_ts,charge_end_ts,departure_ts"
    )

    result = add_failed_rule(
        result,
        reporting_window_invalid,
        "DQ-SES-003",
        "session reporting date is outside Jan-Mar 2026",
        "arrival_ts"
    )

    return result


# ============================================================
# DQ-SES-004 — Lifecycle
# ============================================================

def check_session_lifecycle(df):
    """
    Apply DQ-SES-004 using the lifecycle checks implemented
    for Week 6.

    COMPLETED:
        - charge_start_ts required
        - charge_end_ts required
        - departure_ts required
        - end_reason required
        - energy_kwh required

    INTERRUPTED / CANCELLED:
        - departure_ts required
        - end_reason required
    """

    completed_invalid = (
        (F.upper(F.col("final_status")) == "COMPLETED")
        & (
            F.col("charge_start_ts").isNull()
            | F.col("charge_end_ts").isNull()
            | F.col("departure_ts").isNull()
            | null_or_blank_condition("end_reason")
            | F.col("energy_kwh").isNull()
        )
    )

    interrupted_cancelled_invalid = (
        F.upper(F.col("final_status")).isin(
            "INTERRUPTED",
            "CANCELLED"
        )
        & (
            F.col("departure_ts").isNull()
            | null_or_blank_condition("end_reason")
        )
    )

    result = add_failed_rule(
        df,
        completed_invalid,
        "DQ-SES-004",
        "COMPLETED session is inconsistent with required lifecycle evidence",
        "final_status,charge_start_ts,charge_end_ts,departure_ts,end_reason,energy_kwh"
    )

    result = add_failed_rule(
        result,
        interrupted_cancelled_invalid,
        "DQ-SES-004",
        "INTERRUPTED/CANCELLED session is missing required lifecycle evidence",
        "final_status,departure_ts,end_reason"
    )

    return result


# ============================================================
# DQ-SES-005 — Occupancy / Capacity
# ============================================================

def check_session_occupancy(df):
    """
    Apply DQ-SES-005.

    Checks:
        1. Same charger cannot have overlapping sessions.
        2. Concurrent sessions at a station cannot exceed the
           station's approved connector capacity.

    This helper expects:
        station_id
        charger_id
        arrival_ts
        departure_ts
        connector_capacity
        physical_record_id
    """

    base = (
        df
        .filter(
            F.col("arrival_ts").isNotNull()
            & F.col("departure_ts").isNotNull()
            & (F.col("arrival_ts") <= F.col("departure_ts"))
        )
        .select(
            "physical_record_id",
            "station_id",
            "charger_id",
            "arrival_ts",
            "departure_ts",
            "connector_capacity"
        )
    )

    # Same-charger overlap
    a = base.alias("a")
    b = base.alias("b")

    charger_overlap = (
        a.join(
            b,
            (
                (F.col("a.charger_id") == F.col("b.charger_id"))
                & (
                    F.col("a.physical_record_id")
                    != F.col("b.physical_record_id")
                )
                & (
                    F.col("a.arrival_ts")
                    < F.col("b.departure_ts")
                )
                & (
                    F.col("b.arrival_ts")
                    < F.col("a.departure_ts")
                )
            ),
            "inner"
        )
        .select(
            F.col("a.physical_record_id").alias("physical_record_id")
        )
        .distinct()
        .withColumn(
            "charger_overlap_flag",
            F.lit(True)
        )
    )

    # Station capacity
    # Build event points and calculate active-session counts.
    starts = (
        base
        .select(
            "station_id",
            "physical_record_id",
            "connector_capacity",
            F.col("arrival_ts").alias("event_ts"),
            F.lit(1).alias("delta")
        )
    )

    ends = (
        base
        .select(
            "station_id",
            "physical_record_id",
            "connector_capacity",
            F.col("departure_ts").alias("event_ts"),
            F.lit(-1).alias("delta")
        )
    )

    events = starts.unionByName(ends)

    station_window = (
        Window
        .partitionBy("station_id")
        .orderBy(
            F.col("event_ts"),
            F.col("delta").asc()
        )
        .rowsBetween(
            Window.unboundedPreceding,
            Window.currentRow
        )
    )

    station_events = events.withColumn(
        "active_sessions",
        F.sum("delta").over(station_window)
    )

    capacity_failures = (
        station_events
        .filter(
            F.col("connector_capacity").isNotNull()
            & (
                F.col("active_sessions")
                > F.col("connector_capacity")
            )
        )
        .select("physical_record_id")
        .distinct()
        .withColumn(
            "capacity_exceeded_flag",
            F.lit(True)
        )
    )

    result = (
        df
        .join(
            charger_overlap,
            "physical_record_id",
            "left"
        )
        .join(
            capacity_failures,
            "physical_record_id",
            "left"
        )
    )

    result = add_failed_rule(
        result,
        F.coalesce(
            F.col("charger_overlap_flag"),
            F.lit(False)
        ),
        "DQ-SES-005",
        "sessions overlap on the same charger",
        "charger_id,arrival_ts,departure_ts"
    )

    result = add_failed_rule(
        result,
        F.coalesce(
            F.col("capacity_exceeded_flag"),
            F.lit(False)
        ),
        "DQ-SES-005",
        "concurrent sessions exceed station connector capacity",
        "station_id,connector_capacity"
    )

    return result.drop(
        "charger_overlap_flag",
        "capacity_exceeded_flag"
    )


# ============================================================
# DQ-SES-006 — Measures / Ranges
# ============================================================

def check_session_measures(df):
    """
    Apply DQ-SES-006.

    Checks implemented in Week 6:
        - energy_kwh cannot be null
        - energy_kwh cannot be negative
        - duration cannot be null/negative
        - occupied minutes cannot be null/negative

    Note:
        Project-approved configured numeric ranges were not
        available in the working environment, so no invented
        thresholds are applied here.
    """

    result = (
        df
        .withColumn(
            "_duration_minutes",
            (
                F.unix_timestamp("charge_end_ts")
                - F.unix_timestamp("charge_start_ts")
            ) / 60.0
        )
        .withColumn(
            "_occupied_minutes",
            (
                F.unix_timestamp("departure_ts")
                - F.unix_timestamp("arrival_ts")
            ) / 60.0
        )
    )

    result = add_failed_rule(
        result,
        F.col("energy_kwh").isNull()
        | (F.col("energy_kwh") < 0),
        "DQ-SES-006",
        "energy measure is missing or negative",
        "energy_kwh"
    )

    result = add_failed_rule(
        result,
        F.col("_duration_minutes").isNull()
        | (F.col("_duration_minutes") < 0),
        "DQ-SES-006",
        "charging duration is missing or negative",
        "charge_start_ts,charge_end_ts"
    )

    result = add_failed_rule(
        result,
        F.col("_occupied_minutes").isNull()
        | (F.col("_occupied_minutes") < 0),
        "DQ-SES-006",
        "occupied minutes are missing or negative",
        "arrival_ts,departure_ts"
    )

    return result.drop(
        "_duration_minutes",
        "_occupied_minutes"
    )


# ============================================================
# DQ-SES-007 — Physical Plausibility
# ============================================================

def check_session_physical_plausibility(df):
    """
    DQ-SES-007 is intentionally blocked.

    The approved rule requires a project-approved
    efficiency/tolerance configuration. No such configuration
    was available in the Week 6 working environment.

    Do not invent a tolerance threshold here.
    """

    return (
        df
        .withColumn(
            "dq_esi_007_status",
            F.lit("BLOCKED")
        )
        .withColumn(
            "dq_esi_007_reason",
            F.lit(
                "Approved efficiency/tolerance configuration unavailable"
            )
        )
    )


# ============================================================
# DQ-MNT-001 — Maintenance Integrity
# ============================================================

def check_maintenance_integrity(
    maintenance_df,
    trusted_station_df,
    trusted_charger_df
):
    """
    Apply DQ-MNT-001.

    Checks:
        - station resolves
        - charger resolves
        - charger belongs to stated station
        - repair/recovery events occur after the related fault
    """

    result = initialize_dq_columns(maintenance_df)

    trusted_stations = (
        trusted_station_df
        .select("station_id")
        .dropDuplicates()
        .withColumn("_station_exists", F.lit(True))
    )

    trusted_chargers = (
        trusted_charger_df
        .select(
            "charger_id",
            F.col("station_id").alias("_charger_station_id")
        )
        .dropDuplicates()
        .withColumn("_charger_exists", F.lit(True))
    )

    result = (
        result
        .join(trusted_stations, "station_id", "left")
        .join(trusted_chargers, "charger_id", "left")
    )

    station_unresolved = (
        F.col("station_id").isNull()
        | F.col("_station_exists").isNull()
    )

    charger_unresolved = (
        F.col("charger_id").isNull()
        | F.col("_charger_exists").isNull()
    )

    station_mismatch = (
        ~station_unresolved
        & ~charger_unresolved
        & (
            F.col("station_id")
            != F.col("_charger_station_id")
        )
    )

    result = add_failed_rule(
        result,
        station_unresolved,
        "DQ-MNT-001",
        "station reference is unresolved",
        "station_id"
    )

    result = add_failed_rule(
        result,
        charger_unresolved,
        "DQ-MNT-001",
        "charger reference is unresolved",
        "charger_id"
    )

    result = add_failed_rule(
        result,
        station_mismatch,
        "DQ-MNT-001",
        "charger does not belong to the stated station",
        "station_id,charger_id"
    )

    # Find the first fault timestamp for each maintenance incident.
    faults = (
        maintenance_df
        .filter(
            F.upper(F.col("event_type"))
            == "FAULT_REPORTED"
        )
        .groupBy(
            "incident_id",
            "charger_id"
        )
        .agg(
            F.min("event_ts").alias("_fault_ts")
        )
    )

    result = result.join(
        faults,
        ["incident_id", "charger_id"],
        "left"
    )

    chronology_invalid = (
        F.upper(F.col("event_type")).isin(
            "REPAIR_STARTED",
            "RECOVERY_CONFIRMED"
        )
        & F.col("_fault_ts").isNotNull()
        & (
            F.col("event_ts") <= F.col("_fault_ts")
        )
    )

    result = add_failed_rule(
        result,
        chronology_invalid,
        "DQ-MNT-001",
        "repair/recovery timestamp is not after the fault timestamp",
        "event_ts,related_fault_event_id"
    )

    return add_route_column(
        result.drop(
            "_station_exists",
            "_charger_exists",
            "_charger_station_id",
            "_fault_ts"
        )
    )


# ============================================================
# Rule Occurrences
# ============================================================

def build_rule_occurrences(
    routed_df,
    rule_name_map=None
):
    """
    Explode failed_rule_ids into one row per rule occurrence.

    A physical record that fails multiple rules produces multiple
    rule-occurrence rows but remains one physical record for
    Trusted/Quarantine reconciliation.
    """

    if rule_name_map is None:
        rule_name_map = {
            "DQ-CHG-001": "Charger Master",
            "DQ-CHG-002": "Station Master",
            "DQ-SES-001": "Session Identity",
            "DQ-SES-002": "Session Station/Charger Reference",
            "DQ-SES-003": "Session Chronology/Reporting Window",
            "DQ-SES-004": "Session Lifecycle",
            "DQ-SES-005": "Session Occupancy/Capacity",
            "DQ-SES-006": "Session Measures/Ranges",
            "DQ-SES-007": "Session Physical Plausibility",
            "DQ-MNT-001": "Maintenance Integrity",
            "DQ-EVT-001": "Status Event Streaming Governance",
        }

    mapping_expr = F.create_map(
        *[
            item
            for pair in rule_name_map.items()
            for item in (
                F.lit(pair[0]),
                F.lit(pair[1])
            )
        ]
    )

    return (
        routed_df
        .filter(F.size("failed_rule_ids") > 0)
        .select(
            "physical_record_id",
            F.explode("failed_rule_ids").alias("rule_id"),
            "source_system",
            "source_file",
            "run_id"
        )
        .withColumn(
            "rule_name",
            mapping_expr[F.col("rule_id")]
        )
        .withColumn(
            "severity",
            F.create_map(
                *[
                    item
                    for pair in DQ_SEVERITY.items()
                    for item in (
                        F.lit(pair[0]),
                        F.lit(pair[1])
                    )
                ]
            )[F.col("rule_id")]
        )
        .withColumn(
            "quarantined_at",
            F.current_timestamp()
        )
        .withColumn(
            "rework_status",
            F.lit("OPEN")
        )
    )


# ============================================================
# Reconciliation
# ============================================================

def reconcile_physical_records(
    candidate_df,
    trusted_df,
    quarantine_df
):
    """
    Reconcile physical_record_id between Candidate,
    Trusted and Quarantine.

    Acceptance:
        Candidate = Trusted + Quarantine
        Trusted ∩ Quarantine = empty
        Variance = 0
    """

    candidate_ids = (
        candidate_df
        .select("physical_record_id")
        .distinct()
    )

    trusted_ids = (
        trusted_df
        .select("physical_record_id")
        .distinct()
    )

    quarantine_ids = (
        quarantine_df
        .select("physical_record_id")
        .distinct()
    )

    candidate_count = candidate_ids.count()
    trusted_count = trusted_ids.count()
    quarantine_count = quarantine_ids.count()

    overlap = (
        trusted_ids
        .join(
            quarantine_ids,
            "physical_record_id",
            "inner"
        )
        .count()
    )

    variance = (
        candidate_count
        - trusted_count
        - quarantine_count
    )

    return {
        "candidate": candidate_count,
        "trusted": trusted_count,
        "quarantine": quarantine_count,
        "overlap": overlap,
        "variance": variance,
        "acceptance": (
            "PASS"
            if overlap == 0 and variance == 0
            else "FAIL"
        )
    }


# ============================================================
# Blocked Rule Status
# ============================================================

def get_blocked_rule_status():
    """
    Return the Week 6 rules that cannot currently be executed
    because their approved dependencies are unavailable.
    """

    return [
        {
            "rule_id": "DQ-SES-007",
            "status": "BLOCKED",
            "reason": (
                "Approved efficiency/tolerance configuration "
                "unavailable"
            ),
        },
        {
            "rule_id": "DQ-EVT-001",
            "status": "BLOCKED",
            "reason": (
                "Events Bronze/Candidate source unavailable"
            ),
        },
    ]


# ============================================================
# End of Week 6 DQ Rules
# ============================================================
```
