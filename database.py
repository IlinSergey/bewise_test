from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import func

from config import DB
from my_types import Question
from my_types import Quize as Qz

engine = create_engine(DB)
db_session = scoped_session(sessionmaker(bind=engine))


class Base(DeclarativeBase):
    pass


Base.query = db_session.query_property()


class Quize(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String())
    answer = Column(String())
    creation_date = Column(DateTime, default=func.now())
    request_count = Column(Integer)

    def __repr__(self):
        return f'Question: {self.question}, answer: {self.answer}'


class RequestCount(Base):
    __tablename__ = 'request_count'

    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=0)

    def __repr__(self):
        return f'Count: {self.count}'


def save_quize(quize_data: Qz) -> bool:
    quize = Quize(
        id=quize_data.id,
        question=quize_data.question,
        answer=quize_data.answer,
        request_count=quize_data.request_count,
    )
    try:
        db_session.add(quize)
        db_session.commit()
        return True
    except IntegrityError:
        return False


def get_question(request_count: int) -> list[Question]:
    try:
        questions = Quize.query.filter(Quize.request_count == (request_count - 1))
        result = [Question(question=row.question, answer=row.answer) for row in questions]
        return result
    except Exception:
        return []


def get_request_count() -> int:
    try:
        count = RequestCount.query.first()
        if count:
            return count.count
        else:
            return 0
    except Exception:
        return 0


def increment_count() -> None:
    count = RequestCount.query.first()
    if count:
        count.count += 1
    else:
        count = RequestCount(count=1)
        db_session.add(count)
    db_session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
