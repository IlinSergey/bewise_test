from fastapi import FastAPI
from service import get_quiz
from my_types import Quize

app = FastAPI()


@app.get('/get_question/{questions_num}/')
@app.get('/get_question/{questions_num}')
async def get_guestion(questions_num: int):
    question: Quize = await get_quiz(question=questions_num)
    return {'question': question.question,
            'answer': question.answer,
            }
