# auth.py

import os
from dotenv import load_dotenv
import requests

# Load variables from .env file
load_dotenv()

# Get credentials from environment variables
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET_VALUE = os.getenv("CLIENT_SECRET")

# Construct the token request
url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "client_id": CLIENT_ID,
    "scope": "https://graph.microsoft.com/.default",
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

# Send the request and print the access token (for now)
response = requests.post(url, headers=headers, data=data)
print(response.json())  # ✅ You should see an "access_token"
