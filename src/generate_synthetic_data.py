"""
Synthetic Data Generator Template

Week: 2
Purpose:
    Generate small educational CSV/JSON sample datasets for the assigned project.

Important:
    - Do not generate or use real personal/company/customer data.
    - Keep GitHub sample files small.
    - Use a fixed random seed so data can be recreated.
    - Update this file based on your project-specific manual.
"""

from pathlib import Path
import csv
import json
import random
from datetime import datetime, timedelta

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data_sample" / "raw"
STREAMING_DIR = BASE_DIR / "data_sample" / "streaming"

RAW_DIR.mkdir(parents=True, exist_ok=True)
STREAMING_DIR.mkdir(parents=True, exist_ok=True)


def generate_stations_file() -> None:
    """Create a small reference file. Replace fields with project-specific values."""
    output_path = RAW_DIR / "stations.csv"
    rows = [
        {"reference_id": "REF-001", "reference_name": "Sample A", "category": "Category 1"},
        {"reference_id": "REF-002", "reference_name": "Sample B", "category": "Category 2"},
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def generate_source_file(row_count: int = 100) -> None:
    """Create a small synthetic ChargeIQ maintenance source file."""

    output_path = RAW_DIR / "maintenance.csv"
    start_time = datetime(2026, 1, 1, 9, 0, 0)

    fieldnames = [
        "physical_record_id",
        "maintenance_id",
        "incident_id",
        "station_id",
        "charger_id",
        "event_ts",
        "event_type",
        "fault_category",
        "fault_code",
        "severity",
        "status_after",
        "related_fault_event_id",
        "planned_flag",
        "notes_code",
        "batch_date",
        "source_system"
    ]

    event_types = [
        "INSPECTION",
        "FAULT_REPORTED",
        "REPAIR_STARTED",
        "REPAIR_COMPLETED",
        "RECOVERY"
    ]

    fault_categories = [
        "POWER_MODULE",
        "CONNECTOR",
        "COMMUNICATION",
        "COOLING"
    ]

    fault_codes = [
        "PWR_DERATE",
        "CONN_ERROR",
        "OCPP_TIMEOUT",
        "TEMP_HIGH"
    ]

    severities = ["MINOR", "MAJOR", "CRITICAL"]

    statuses = [
        "OPEN",
        "IN_PROGRESS",
        "RESOLVED"
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, row_count + 1):

            ts = start_time + timedelta(
                minutes=random.randint(0, 3000)
            )

            event_type = random.choice(event_types)

            writer.writerow({
                "physical_record_id": f"PR-{i:06d}",
                "maintenance_id": f"MNT-{i:08d}",
                "incident_id": f"INC-{random.randint(1, 50):06d}",
                "station_id": f"STN{random.randint(1, 180):04d}",
                "charger_id": f"CHG{random.randint(1, 1200):05d}",
                "event_ts": ts.isoformat(),
                "event_type": event_type,
                "fault_category": random.choice(fault_categories),
                "fault_code": random.choice(fault_codes),
                "severity": random.choice(severities),
                "status_after": random.choice(statuses),
                "related_fault_event_id": "",
                "planned_flag": random.choice([True, False]),
                "notes_code": f"NOTE{random.randint(1, 10):02d}",
                "batch_date": ts.date().isoformat(),
                "source_system": "MAINTENANCE_SYSTEM"
            })


def generate_streaming_events(
    batch_number: int = 1,
    event_count: int = 50
) -> None:
    """Create ChargeIQ streaming charger status events as JSON Lines."""

    output_path = STREAMING_DIR / (
        f"charger_status_event_drop_{batch_number:02d}.json"
    )

    start_time = datetime(2026, 4, 1, 9, 0, 0)

    event_types = [
        "AVAILABLE",
        "OCCUPIED",
        "SESSION_STARTED",
        "SESSION_COMPLETED",
        "FAULTED",
        "OFFLINE",
        "RESTORED"
    ]

    connector_types = [
        "TYPE2_AC",
        "CCS2",
        "CHADEMO"
    ]

    status_values = [
        "AVAILABLE",
        "OCCUPIED",
        "FAULTED",
        "OFFLINE"
    ]

    with output_path.open("w", encoding="utf-8") as f:

        for i in range(1, event_count + 1):

            event_type = random.choice(event_types)

            event = {
                "event_id": f"EVT-{batch_number:02d}-{i:05d}",
                "schema_version": "1.0",
                "event_ts": (
                    start_time + timedelta(seconds=i * 30)
                ).isoformat(),
                "event_type": event_type,
                "station_id": f"STN{random.randint(1, 180):04d}",
                "charger_id": f"CHG{random.randint(1, 1200):05d}",
                "connector_type": random.choice(connector_types),
                "rated_power_kw": random.choice(
                    [7.4, 11.0, 22.0, 50.0, 60.0]
                ),
                "session_id": f"SES{random.randint(1, 300000):09d}",
                "status_from": random.choice(status_values),
                "status_to": random.choice(status_values),
                "energy_kwh_delta": round(
                    random.uniform(0, 5), 3
                ),
                "occupancy_flag": event_type in [
                    "OCCUPIED",
                    "SESSION_STARTED"
                ],
                "fault_code": (
                    random.choice([
                        "OCPP_TIMEOUT",
                        "POWER_FAILURE",
                        "TEMP_HIGH"
                    ])
                    if event_type == "FAULTED"
                    else None
                ),
                "producer_run_id": f"RUN_W10_{batch_number}",
                "event_sequence_no": i
            }

            f.write(json.dumps(event) + "\n")


def main() -> None:
    generate_stations_file()
    generate_source_file(row_count=100)
    generate_streaming_events(batch_number=1, event_count=50)
    generate_streaming_events(batch_number=2,event_count=50)
    print("Synthetic sample data generated successfully.")


if __name__ == "__main__":
    main()
