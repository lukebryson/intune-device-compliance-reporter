-- Query to get all data
SELECT
    deviceId AS "Device ID", 
    deviceName AS "Device Name",
    emailAddress AS "User",
    operatingSystem AS "Operating System",
    osVersion AS "OS Version",
    complianceState AS "Compliance State",
    isCompliant AS "Is Compliant",
    totalStorageBytes AS "Total Storage (Bytes)",
    freeStorageBytes AS "Free Storage (Bytes)",
    freeStoragePct AS "Free Storage (%)",
    lowStorage AS "Low Storage",
    lastSyncDateTime AS "Last Sync Date"
FROM device_compliance;

-- Query to get Windows devices with low storage that have checked in within the last 3 months
SELECT
    emailAddress AS "User",
    deviceName AS "Device Name",
    freeStoragePct AS "Free Storage (%)"
FROM device_compliance
WHERE lowStorage = 1 AND operatingSystem = 'Windows' AND date(lastSyncDateTime) >= date('now', '-3 months');

-- Query to get Windows devices that are not compliant and have checked in within the last 3 months
SELECT
    emailAddress AS "User",
    deviceName AS "Device Name",
    Model AS "Model"
FROM device_compliance
WHERE isCompliant = 0 AND operatingSystem = 'Windows' AND date(lastSyncDateTime) >= date('now', '-3 months');

-- Query to get iOS devices with low storage that have checked in within the last 3 months
SELECT
    emailAddress AS "User",
    deviceName AS "Device Name",
    freeStoragePct AS "Free Storage (%)"
FROM device_compliance
WHERE model != "iPhone 13" AND lowStorage = 0 AND operatingSystem = 'iOS' AND date(lastSyncDateTime) >= date('now', '-3 months');


-- Query to get iOS devices that are not compliant and have checked in within the last 3 months
SELECT
    emailAddress AS "User",
    deviceName AS "Device Name",
    Model AS "Model"
FROM device_compliance
WHERE isCompliant = 0 AND operatingSystem = 'iOS' AND date(lastSyncDateTime) >= date('now', '-3 months');

-- Test csv output
.mode csv
.headers on
.output device_compliance.csv
SELECT * FROM device_compliance;
.output stdout