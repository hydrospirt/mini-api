from django.conf import settings
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive'
]


CREDS = Credentials.from_service_account_info(
    scopes=SCOPES, info=settings.INFO
)

DRIVE_SERVICE = discovery.build('drive', 'v3', credentials=CREDS)
DOCS_SERVICE = discovery.build("docs", "v1", credentials=CREDS)
