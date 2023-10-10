from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from config import DB
from sqlalchemy.sql import func


engine = create_engine(DB)
db_session = scoped_session(sessionmaker(bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()


class Quize(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String())
    answer = Column(String())
    creation_date = Column(DateTime, default=func.now())

    def __repr__(self):
        return f'Question: {self.question}, answer: {self.answer}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
