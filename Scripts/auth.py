# auth.py

import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET_VALUE = os.getenv("CLIENT_SECRET_VALUE")

# Microsoft Identity token endpoint
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

def get_access_token():
    """
    Retrieves an OAuth2 access token from Microsoft Identity Platform
    using the client credentials flow.
    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    body = {
        "client_id": CLIENT_ID,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": CLIENT_SECRET_VALUE,
        "grant_type": "client_credentials"
    }

    response = requests.post(TOKEN_URL, headers=headers, data=body)

    if response.status_code == 200:
        token = response.json().get("access_token")
        print("Access token retrieved.")
        return token
    else:
        print(" Failed to retrieve access token.")
        print(response.text)
        return None
    
if __name__ == "__main__":
    token = get_access_token()
    print(token)