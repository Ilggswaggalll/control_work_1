from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    id: int
    age: int

BAD_WORDS = [
    "кринж", "кринжа", "кринжу", "кринжем", "кринже",
    "рофл", "рофла", "рофлу", "рофлом", "рофле",
    "вайб", "вайба", "вайбу", "вайбом", "вайбе"
]

class Feedback(BaseModel):
    name: str = Field(...,
        title="Имя пользователя",
        description="Имя пользователя, оставляющего отзыв",
        min_length=2,
        max_length=50
    )
    message: str = Field(...,
        title="Сообщение обратной связи",
        description="Текст отзыва",
        min_length=10,
        max_length=500
    )

    @field_validator('message')
    @classmethod
    def validate_message(cls, value):
        v = value.strip()
        if len(v) < 10:
            raise ValueError('Сообщение должно содержать минимум 10 символов')

        if len(v) > 500:
            raise ValueError('Сообщение не может превышать 500 символов')

        v_lower = v.lower()

        for bad_word in BAD_WORDS:
            if bad_word in v_lower:
                raise ValueError(f'Использование недопустимых слов (обнаружено: "{bad_word}")')

        return v

class FeedbackResponse(BaseModel):
    message: str

