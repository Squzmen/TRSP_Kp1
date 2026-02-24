from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, Feedback

app = FastAPI()
feedbacks = []

# Задание 1.1

# @app.get("/")
# def root():
#    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

# Задание 1.2

@app.get("/")
def root_html():
    return FileResponse("index.html")

# Задание 1.4
user = User(name="Александр Пшеничнов", id=1)

@app.get("/users")
def get_user():
    return user

# Задание 2.1
@app.post("/feedback")
def post_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}
