import aiohttp
import asyncio
from my_types import Quize
from typing import Dict


def prepare_quize_data(data: Dict[str, any]) -> Quize:
    id = data['id']
    question = data['question']
    answer = data['answer']
    creation_date = data['airdate']
    quize = Quize(id=id, question=question, answer=answer, creation_date=creation_date)
    return quize


async def get_quiz(question: int):

    async with aiohttp.ClientSession() as session:
        url = f'https://jservice.io/api/random?count={question}'
        async with session.get(url=url) as response:
            if response.status == 200:
                result = await response.json()
                for question in result:
                    quize = prepare_quize_data(data=result)
                    print(quize)


if __name__ == '__main__':
    asyncio.run(get_quiz(1))
