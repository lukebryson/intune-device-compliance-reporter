# fetch_devices.py

import requests
import json
from auth import get_access_token  # Reuse token function from auth.py

# Transform and clean the raw device data
def transform_device(device):
    """Cleans and extracts only the fields needed for reporting."""
    try:
        total = int(device.get("totalStorageSpaceInBytes") or 0)
        free = int(device.get("freeStorageSpaceInBytes") or 0)
        free_pct = (free / total * 100) if total else None
    except (ValueError, TypeError, ZeroDivisionError):
        total, free, free_pct = 0, 0, None

    return {
        "emailAddress": device.get("emailAddress"),
        "deviceName": device.get("deviceName"),
        "operatingSystem": device.get("operatingSystem"),
        "osVersion": device.get("osVersion"),
        "complianceState": device.get("complianceState"),
        "isCompliant": device.get("complianceState") == "compliant",
        "totalStorageBytes": total,
        "freeStorageBytes": free,
        "freeStoragePct": round(free_pct, 2) if free_pct is not None else None,
        "lowStorage": free_pct is not None and free_pct < 10,
        "lastSyncDateTime": device.get("lastSyncDateTime")
    }

# Step 1: Get access token
access_token = get_access_token()

if access_token:
    # Step 2: Define the Microsoft Graph API endpoint
    endpoint = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    all_devices = []  # Store all device records here

    # Step 3: Handle pagination to fetch all devices
    while endpoint:
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            data = response.json()
            devices = data.get("value", [])
            all_devices.extend(devices)

            # Continue if there's another page of results
            endpoint = data.get("@odata.nextLink", None)
        else:
            print("❌ Failed to retrieve device data:", response.status_code)
            print(response.text)
            break

    # Step 4: Output total device count
    print(f"✅ Retrieved {len(all_devices)} devices")

    # Step 5: Transform and clean the data
    cleaned_devices = [transform_device(device) for device in all_devices]

    # Step 6: Save cleaned data to JSON
    with open("cleaned_devices.json", "w") as f:
        json.dump(cleaned_devices, f, indent=2)
    print("✅ Cleaned device data saved to cleaned_devices.json")

else:
    print("❌ Authentication failed. Cannot retrieve device data.")
