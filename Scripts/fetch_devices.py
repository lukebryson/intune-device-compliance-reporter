# fetch_devices.py

import requests
import json
from auth import get_access_token  # Reuse token function from auth.py

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

    # Step 5: Save all device data to a JSON file
    with open("devices.json", "w") as f:
        json.dump(all_devices, f, indent=2)
    print("✅ Device data saved to devices.json")

else:
    print("❌ Authentication failed. Cannot retrieve device data.")