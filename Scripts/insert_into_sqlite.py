# insert_into_sqlite.py

import json
import sqlite3

# Load the cleaned device data
with open("cleaned_devices.json", "r") as file:
    devices = json.load(file)

# Connect to the SQLite database (or create it)
conn = sqlite3.connect("intune_devices.db")
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
