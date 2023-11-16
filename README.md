# Micro API Dajngo Rest Framework с иcпользованием Google Docs API

---
## О приложении
Для создания текстовых файлов в Google Drive
> На стадии разработки.
## Технологии
- Python 3.12
- google-api-python-client
- Django
- Django Rest Framework

## Установка:
- Клонируйте проект парсера на свой компьютер:
```
git@github.com:hydrospirt/mini-api.git
```
- Установите и активируйте виртуальное окружение c Python 3.12
```
cd ./mini-api/ &&
py -3.12 -m venv venv
```
Для Windows:
```
source venv/Scripts/Activate
```
Для Linux
```
source venv/bin/activate
```
- Установите зависимости из файла requirements.txt
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Создайте переменные окружения в основной папке проекта "mini-api"
```
touch .env
```
- Добавьте ваши данные в файл .env
```
ALLOWED_HOSTS=127.0.0.1
SECRET_KEY='Секретный код Django'
```

- Добавьте ваши данные в файл .env из JSON файла сгенерированого Google Oauth 2.0 Provider
```
YOUR_EMAIL=your_mail@gmail.com
TYPE=service_account
PROJECT_ID=Id проекта
PRIVATE_KEY_ID=ID приватного ключа
PRIVATE_KEY=Приватный ключ-----BEGIN PRIVATE KEY-----\nYOUR_KEY\n-----END PRIVATE KEY-----\n
CLIENT_EMAIL=mail сервисного аккаунта
CLIENT_ID=id сервисного аккаунта
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=ссылка из JSON
```
## Инструкции для запуска в Dev режиме на localhost
- Создать миграции:
```
cd ./mini_drive/ &&
python3 manage.py makemigrations
```
- Применить миграции:
```
python3 manage.py migrate
```
- Создать супер пользователя для входа в админ панель
```
python3 manage.py createsuperuser

Username (leave blank to use 'user'): # Придумайте логин (например, admin)
Email address:                        # укажите почту
Password:                             # придумайте пароль
Password (again):                     # повторите пароль
Superuser created successfully.
```
- Запустить приложение
```
python3 manage.py runserver
```
Ссылки приложения:
http://127.0.0.1:8000/admin/ # Панель Администрирования Django
http://127.0.0.1:8000/api/v1/txt/ # Основная ссылка API

Примеры запросов:
> На стадии разработки.

Скриншоты работы приложения:
> На стадии разработки.
Пример POST запроса и ответа от Django Rest Framework
![POST](https://github.com/hydrospirt/mini-api/blob/master/examples/1.png)
Пример работы системы логирования
![LOGGER](https://github.com/hydrospirt/mini-api/blob/master/examples/2.png)
Пример отображения созданного документа в Google Docs
![Docs]https://github.com/hydrospirt/mini-api/blob/master/examples/3.png
Снимок админ панели в Django
![ADMIN](https://github.com/hydrospirt/mini-api/blob/master/examples/4.png)
# Автор
Эдуард Гумен - [Cтраница GitHub](https://github.com/hydrospirt)
