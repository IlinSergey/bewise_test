from dataclasses import dataclass


@dataclass
class Quize:
    id: int
    question: str
    answer: str
