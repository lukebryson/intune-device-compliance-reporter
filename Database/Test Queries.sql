-- Test Queries
SELECT COUNT(*) AS total_devices
FROM device_compliance;
-- This query counts the total number of devices in the device_compliance table.

SELECT COUNT(*) FROM device_compliance;
-- This query counts the total number of devices in the device_compliance table.

SELECT deviceName, emailAddress, operatingSystem, complianceState
FROM device_compliance
WHERE complianceState != 'compliant';
-- This query retrieves the device name, email address, operating system, and compliance state of devices that are not compliant.