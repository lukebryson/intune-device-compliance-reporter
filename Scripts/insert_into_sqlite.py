# insert_into_sqlite.py

from datetime import datetime
import json
import sqlite3

# Defining the database name with a timestamp to avoid overwriting previous databases
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
db_name = f"Database/intune_devices_{timestamp}.db"

# Load the cleaned device data
with open("cleaned_devices.json", "r") as file:
    devices = json.load(file)

# Connect to the SQLite database (or create it)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create the table (if it doesn't already exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS device_compliance (
    deviceId TEXT PRIMARY KEY,
    deviceName TEXT,
    emailAddress TEXT,
    model TEXT,
    operatingSystem TEXT,
    osVersion TEXT,
    complianceState TEXT,
    isCompliant BOOLEAN,
    totalStorageBytes INTEGER,
    freeStorageBytes INTEGER,
    freeStoragePct REAL,
    lowStorage BOOLEAN,
    lastSyncDateTime TEXT
);
""")

# Insert each device one at a time
for device in devices:
    cursor.execute(f"""
    INSERT OR REPLACE INTO device_compliance (
        deviceId, deviceName, emailAddress, model, operatingSystem, osVersion,
        complianceState, isCompliant, totalStorageBytes, freeStorageBytes,
        freeStoragePct, lowStorage, lastSyncDateTime
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    );
    """, (
        device["deviceId"],
        device["deviceName"],
        device["emailAddress"],
        device["model"],
        device["operatingSystem"],
        device["osVersion"],
        device["complianceState"],
        device["isCompliant"],
        device["totalStorageBytes"],
        device["freeStorageBytes"],
        device["freeStoragePct"],
        device["lowStorage"],
        device["lastSyncDateTime"]
    ))

# Save changes and close the connection
conn.commit()
conn.close()

print(f"✅ {len(devices)} records inserted into device_compliance table.")


# test_transform_device.py

from Scripts.fetch_devices import transform_device

def test_low_storage_flag():
    device = {
        "id": "123",
        "deviceName": "Test Device",
        "emailAddress": "test@example.com",
        "operatingSystem": "Windows",
        "osVersion": "10.0.22631.3447",
        "complianceState": "compliant",
        "totalStorageSpaceInBytes": 100000000,
        "freeStorageSpaceInBytes": 5000000,
        "lastSyncDateTime": "2024-12-31T10:30:00Z"
    }
    result = transform_device(device)
    assert result["lowStorage"] == True
