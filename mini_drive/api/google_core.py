from django.conf import settings
from services.google_api_client import DOCS_SERVICE, DRIVE_SERVICE


def create_textfile(name, data):
    """Создает текстовый файл с отправленным текстом в Google Docs"""
    body = {
        'title': name
    }
    document = DOCS_SERVICE.documents().create(
        body=body
    ).execute()
    document_id = document.get('documentId')
    document_title = document.get('title')
    doc_content = {
        'requests': [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': data
                }
            }
        ]
    }
    DOCS_SERVICE.documents().batchUpdate(documentId=document_id, body=doc_content).execute()
    print(f'Created document with title: {document_title}')
    print('Документ создан ссылка:')
    print(f'https://docs.google.com/document/d/{document_id}/')
    print('Содержимое успешно добавлено в документ.')
    return document_id


def set_user_permissions(document_id):
    """Выдает права доступа пользователю"""
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.EMAIL_USER
    }
    DRIVE_SERVICE.permissions().create(
        fileId=document_id,
        body=permissions_body,
        fields='id'
    ).execute()
