-- Test Queries
SELECT COUNT(*) AS total_devices
FROM device_compliance;
-- This query counts the total number of devices in the device_compliance table.

SELECT deviceName, emailAddress, operatingSystem, complianceState
FROM device_compliance
WHERE complianceState != 'compliant';
-- This query retrieves the device name, email address, operating system, and compliance state of devices that are not compliant.

SELECT deviceName, emailAddress, freeStoragePct, totalStorageBytes, freeStorageBytes
FROM device_compliance
WHERE lowStorage = 1;
--  Helps proactively flag devices at risk of performance issues.

SELECT deviceName, osVersion, emailAddress
FROM device_compliance
WHERE osVersion != '10.0.22631.5039' AND operatingSystem = 'Windows';
-- Check Devices Running Outdated OS Versions.

SELECT deviceName, emailAddress, osVersion
FROM device_compliance
WHERE operatingSystem = 'iOS';
-- Separates mobiles from Windows devices.