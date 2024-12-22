# Weather Route Map

## Описание

Weather Route Map — это сервис, который позволяет узнать погоду на маршруте с возможностью добавления промежуточных точек

---

## Запуск проекта

1. Установите зависимости:
   * via uv
     ```bash
     uv sync
     ```
   * via pip
     ```bash
     pip install -r requirements.txt
     ```

2. Настройка переменных
   
   Переименуйте .env.example и настройте переменные
   
3. Запустите Flask-сервер:
   * via uv
     ```bash
     uv run web/app.py # or uv run flask --app web/app:create_app run (as a normal man)
     ```
   * via pip
     ```bash
     python web/app.py # flask --app web/app:create_app run (as a normal man)
     ```

4. Перейдите по адресу: http://HOST:PORT/ (по умолчанию http://127.0.0.1:5000/)

5. Кайфуйте!
