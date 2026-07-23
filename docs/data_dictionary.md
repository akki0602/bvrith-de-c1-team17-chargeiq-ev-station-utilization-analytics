# Data Dictionary

**Week:** 2  
**Purpose:** Define raw, reference, Silver, and streaming fields.

---

## 1. Source File Catalog

| File Name | Grain | Purpose | Approx. Rows | Notes |
|---|---|---|---:|---|
| `stations.csv` | One row per charging station | Store station information and operating details | 180 | Station master data |
| `chargers.json` | One row per charger | Store charger/connector details | 1,200 | JSON Lines format |
| `sessions.parquet` | One row per charging session | Store charging session history | 300,000 | Batch transactional data |
| `maintenance.csv` | One row per maintenance event | Store maintenance and fault history | 18,000 | Event history |
| `charger_status_event_drop_01.json` | One row per event | Streaming simulation | Streaming | JSON event file |
| `charger_status_event_drop_02.json` | One row per event | Streaming simulation | Streaming | Incremental JSON event file |

---

## 2. Raw File Schema: `stations.csv`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `station_id` | string | Yes | `STN0001` | Unique station ID |
| `station_name` | string | Yes | `Hyderabad Central Charge Hub 001` | Charging station name |
| `city_band` | string | Yes | `Hyderabad` | Operating city |
| `zone` | string | Yes | `Central` | Station zone |
| `site_type` | string | Yes | `PUBLIC_PARKING` | Station category |
| `connector_capacity` | integer | Yes | `5` | Number of charging connectors |
| `operating_start_hour` | integer | Yes | `0` | Opening hour |
| `operating_end_hour` | integer | Yes | `24` | Closing hour |
| `is_24x7` | boolean | Yes | `True` | 24×7 operation indicator |
| `station_status` | string | Yes | `ACTIVE` | Current station status |

---

## 3. Raw File Schema: `chargers.json`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `charger_id` | string | Yes | `CHG00001` | Unique charger ID |
| `station_id` | string | Yes | `STN0001` | Parent station ID |
| `charger_label` | string | Yes | `STN0001-C01` | Charger label |
| `connector_type` | string | Yes | `TYPE2_AC` | Connector type |
| `rated_power_kw` | decimal | Yes | `22.0` | Rated charger power |
| `install_date` | date | Yes | `2025-11-19` | Installation date |
| `operational_status` | string | Yes | `ACTIVE` | Charger operational status |
| `manufacturer_band` | string | Yes | `MFR02` | Manufacturer code |
| `firmware_major` | integer | Yes | `4` | Firmware version |
| `smart_meter_enabled` | boolean | Yes | `True` | Smart meter availability |
| `connector_position` | integer | Yes | `1` | Connector position |

---

## 4. Reference File Schema (`stations.csv`)

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `station_id` | string | Yes | `STN0001` | Reference station ID |
| `station_name` | string | Yes | `Hyderabad Central Charge Hub 001` | Station name |
| `city_band` | string | Yes | `Hyderabad` | Operating city |
| `zone` | string | Yes | `Central` | Station zone |
| `station_status` | string | Yes | `ACTIVE` | Station status |

---

## 5. Canonical Silver Table Design

Final Silver table name:

```text
silver_chargeiq_sessions
```

| Silver Field | Data Type | Source Mapping | Business Meaning |
|---|---|---|---|
| `session_id` | string | `sessions.session_id` | Canonical session ID |
| `station_id` | string | `sessions.station_id` | Charging station |
| `charger_id` | string | `sessions.charger_id` | Charger used |
| `vehicle_class` | string | `sessions.vehicle_class` | Vehicle category |
| `connector_type` | string | `sessions.connector_type` | Connector type |
| `arrival_ts` | timestamp | `sessions.arrival_ts` | Vehicle arrival time |
| `charge_start_ts` | timestamp | `sessions.charge_start_ts` | Charging start time |
| `charge_end_ts` | timestamp | `sessions.charge_end_ts` | Charging completion time |
| `departure_ts` | timestamp | `sessions.departure_ts` | Vehicle departure time |
| `energy_kwh` | decimal | `sessions.energy_kwh` | Energy delivered |
| `tariff_band` | string | `sessions.tariff_band` | Tariff category |
| `tariff_rate_inr_per_kwh` | decimal | `sessions.tariff_rate_inr_per_kwh` | Charging cost per kWh |
| `final_status` | string | `sessions.final_status` | Session completion status |

---

## 6. Streaming Event Schema

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `event_id` | string | Yes | `EVT000001` | Unique event ID |
| `event_ts` | timestamp | Yes | `2026-04-01T09:00:00` | Event timestamp |
| `event_type` | string | Yes | `SESSION_STARTED` | Event type |
| `station_id` | string | Yes | `STN0001` | Station ID |
| `charger_id` | string | Yes | `CHG00001` | Charger ID |
| `connector_type` | string | Yes | `TYPE2_AC` | Connector type |
| `rated_power_kw` | decimal | Yes | `22.0` | Rated charger power |
| `session_id` | string | Conditional | `LIVESES00001` | Live session ID |
| `status_from` | string | Conditional | `AVAILABLE` | Previous charger state |
| `status_to` | string | Yes | `OCCUPIED` | Current charger state |
| `energy_kwh_delta` | decimal | Yes | `3.394` | Incremental energy consumed |
| `occupancy_flag` | boolean | Yes | `True` | Charger occupancy status |
| `fault_code` | string | Conditional | `OCPP_TIMEOUT` | Fault code |
| `producer_run_id` | string | Yes | `RUN_W10_A` | Producer run identifier |
| `event_sequence_no` | bigint | Yes | `1` | Event sequence number |
| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `event_id` | string | Yes | `EVT-0001` | Unique event ID |
| `event_timestamp` | timestamp | Yes | `2026-07-03T10:15:00+05:30` | Event time |
| `event_type` | string | Yes | `[event type]` | Event category |
