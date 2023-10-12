from typing import Dict

import aiohttp

from database import (get_question, get_request_count, increment_count,
                      save_quize)
from my_types import Question, Quize


def prepare_quize_data(data: Dict[str, any], request_count) -> Quize:
    id = data['id']
    question = data['question']
    answer = data['answer']
    request_count = request_count
    quize = Quize(id=id, question=question, answer=answer, request_count=request_count)
    return quize


async def get_quiz(question: int) -> list[Question]:
    async with aiohttp.ClientSession() as session:
        url = f'https://jservice.io/api/random?count={question}'
        async with session.get(url=url) as response:
            if response.status == 200:
                request_count = get_request_count()
                increment_count()
                result = await response.json()
                question_list = []
                for question_data in result:
                    quize = prepare_quize_data(data=question_data, request_count=request_count)
                    if save_quize(quize_data=quize):
                        question_list.append(quize)
                    else:
                        await get_quiz(1)
                quize = return_quize(request_count=request_count)
                return quize


def return_quize(request_count: int) -> list[Question]:
    questions = get_question(request_count=request_count)
    return questions
