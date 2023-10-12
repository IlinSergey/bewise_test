from fastapi import FastAPI

from my_types import Question
from service import get_quiz

app = FastAPI()


@app.get('/get_question/{questions_num}/')
@app.get('/get_question/{questions_num}')
async def get_guestion(questions_num: int):
    questions: list[Question] = await get_quiz(question=questions_num)
    return questions
