import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

credentials = None
__G_DRIVE_TOKEN_FILE = "token.pickle"
__OAUTH_SCOPE = ["https://www.googleapis.com/auth/drive"]
def get_credentials():
    credentials = None

    if os.path.exists(__G_DRIVE_TOKEN_FILE):
        with open(__G_DRIVE_TOKEN_FILE, "rb") as f:
            credentials = pickle.load(f)

    if (
        not credentials
        or not credentials.valid
        or credentials.expired
    ):
        if credentials and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", __OAUTH_SCOPE)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(__G_DRIVE_TOKEN_FILE, "wb") as token:
            pickle.dump(credentials, token)

    return credentials

# Get the credentials
credentials = get_credentials()
