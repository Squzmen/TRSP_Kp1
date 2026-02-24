# Контрольная работа №1 — FastAPI

## Структура проекта

```
project/
├── app.py
├── models.py
└── index.html
```

## Установка и запуск

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
```

Приложение запустится на http://127.0.0.1:8000

Задания и маршруты
Задание	Метод	Маршрут	Описание
1.1	GET	/	Возвращает JSON-приветствие
1.2	GET	/	Возвращает HTML-страницу (заменяет 1.1)
1.4	GET	/users	Возвращает данные пользователя
2.1	POST	/feedback	Принимает отзыв, сохраняет в список
Переключение между заданием 1.1 и 1.2
В app.py закомментировать функцию root() и раскомментировать root_html().

Проверка
Swagger UI:

```
http://127.0.0.1:8000/docs
Пример запроса к /feedback:
```

```bash
curl -X POST http://127.0.0.1:8000/feedback \
  -H "Content-Type: application/json" \
  -d '{"name": "Rustam", "message": "Отличный день!"}'
```

Ожидаемый ответ:

```json
{"message": "Feedback received. Thank you, Rustam."}
```

Зависимости
Python 3.10+

fastapi

uvicorn

pydantic


Либо создайте файл через PowerShell одной командой:

```powershell
New-Item README.md
notepad README.md
