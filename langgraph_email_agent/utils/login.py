
import os
# Gmail API utils
# from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
# from base64 import urlsafe_b64decode, urlsafe_b64encode
from google.oauth2.credentials import Credentials


# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']


def _get_credentials() -> Credentials:
    creds = None

    # Load existing token
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Refresh if expired and refresh token exists
    if creds and creds.expired and creds.refresh_token:
        print("🔄 Refreshing token...")
        creds.refresh(Request())
    # First time login or no refresh token
    if not creds or not creds.valid:
        print("🌐 Launching OAuth consent screen...")
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )
        creds = flow.run_local_server(
            port=39677,
            access_type='offline',
            prompt='consent'  # <== 🔒 forces Google to send refresh_token again
        )

        # Save the token
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    print("✅ Auth complete")
    print("Valid:", creds.valid)
    print("Expired:", creds.expired)
    print("Refresh token:", creds.refresh_token is not None)
    return creds
