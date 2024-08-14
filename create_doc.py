from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/documents']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=credentials)

# Create a Document
document = service.documents().create(body={'title': 'New Document'}).execute()
document_id = document.get('documentId')
print(f'Document ID: {document_id}')

# Modifying the Document
requests = [
    {
        'insertText': {
            'location': {
                'index': 1,
            },
            'text': 'Hello, world!'
        }
    }
]

result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
print(document)
