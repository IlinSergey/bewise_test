import aiohttp
import asyncio
from my_types import Quize
from typing import Dict
from database import db_session, Quize as Qz
from sqlalchemy.exc import IntegrityError


def save_quize(quize_data: Quize) -> bool:
    quize = Qz(
        id=quize_data.id,
        question=quize_data.question,
        answer=quize_data.answer,
    )
    try:
        db_session.add(quize)
        db_session.commit()
        return True
    except IntegrityError:
        return False


def prepare_quize_data(data: Dict[str, any]) -> Quize:
    id = data['id']
    question = data['question']
    answer = data['answer']
    quize = Quize(id=id, question=question, answer=answer)
    return quize


async def get_quiz(question: int):

    async with aiohttp.ClientSession() as session:
        url = f'https://jservice.io/api/random?count={question}'
        async with session.get(url=url) as response:
            if response.status == 200:
                result = await response.json()
                for question_data in result:
                    quize = prepare_quize_data(data=question_data)
                    if save_quize(quize_data=quize):
                        print(quize)
                    else:
                        await get_quiz(1)


if __name__ == '__main__':
    asyncio.run(get_quiz(5))
