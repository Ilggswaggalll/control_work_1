from fastapi import FastAPI
from pydantic import BaseModel

calculate_app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float


@calculate_app.post("/calculate")
async def calculate(numbers: Numbers):
    return {"result": numbers.num1 + numbers.num2}