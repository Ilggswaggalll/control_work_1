from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import User, Feedback, FeedbackResponse
from typing import List
app = FastAPI(
    title="Simple API",
    description="API на первую контрольную",
)

@app.get("/")
async def root():
    content = {"message": "Авторелоад действительно работает"}
    return JSONResponse(content=content, media_type="application/json, charset=utf-8")


user = User(
    name="MAX RKN",
    id=1,
    age=22
)



@app.get("/users")
async def get_user():
    return user

@app.post("/user",
          summary="Получить список пользователей",  # Описание для документации
          response_description="Список пользователей",  # Описание ответа
          response_model=List[User],  # Модель ответа
          tags=["Пользователи"]  # Группировка в документации
          )
async def adult_user():
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }




# 2ая кршка
feedback_storage = []

@app.post("/feedback", response_model=FeedbackResponse)
async def create_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return FeedbackResponse(message=feedback.message)

