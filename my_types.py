from dataclasses import dataclass


@dataclass
class Quize:
    id: int
    question: str
    answer: str
    request_count: int


@dataclass
class Question:
    question: str
    answer: str
