from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/documents']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=credentials)

document = service.documents().create(body={'title': 'New Document'}).execute()
document_id = document.get('documentId')

# Reading the Document
document = service.documents().get(documentId=document_id).execute()
print(f'Title: {document.get("title")}')
print('Content:')
for element in document.get('body').get('content'):
    print(element.get('paragraph').get('elements')[0].get('textRun').get('content'))


# Formatting Text
requests = [
    {
        'updateTextStyle': {
            'range': {
                'startIndex': 1,
                'endIndex': 13,
            },
            'textStyle': {
                'bold': True,
                'italic': True,
            },
            'fields': 'bold,italic'
        }
    }
]

result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
