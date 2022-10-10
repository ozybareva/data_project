# Data Project

## Установка и запуск

При первом запуске необходимо создать виртуальное окружение, в нем запустить pip install -r requirements.txt

По аналогии с файлом .env.example создать .env, в котором прописать значения для переменных:

DB_POSTGRES_HOST, DB_POSTGRES_PORT, DB_POSTGRES_USER, DB_POSTGRES_PASS, DB_POSTGRES_NAME (имя базы данных, где будет создана таблица)

Далее необходимо запустить файл record_data_model.py для заполнения структуры модели данных

Затем запустить файл main.py для создания таблицы и ее заполнения данными из файла
