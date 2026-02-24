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
| Задание | Метод | Маршрут |	Описание |
|:---:|:---:|:--|:-------------------------|
| 1.1 | GET |	/	| Возвращает JSON-приветствие |
| 1.2 |	GET |	/	| Возвращает HTML-страницу (заменяет 1.1) |
| 1.4 |	GET	| /users |	Возвращает данные пользователя, |
| 2.1	| POST|	/feedback |	Принимает отзыв, сохраняет в список |

Переключение между заданием 1.1 и 1.2

В app.py закомментировать функцию root() и раскомментировать root_html().

Проверка
Swagger UI:

```
http://127.0.0.1:8000/docs
```

Пример запроса к /feedback:
```
http://127.0.0.1:8000/docs
```

Найдите раздел POST /feedback

Нажмите Try it out

Вставьте в поле Request body:

```json
{
  "name": "Rustam",
  "message": "Отличный день! Мне нравится ходить в школу!"
}
```
Нажмите Execute

Ожидаемый ответ:

```json
{"message": "Feedback received. Thank you, Rustam."}
```

Зависимости
Python 3.10+

+ fastapi

+ uvicorn

+ pydantic

