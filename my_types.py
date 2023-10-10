from dataclasses import dataclass
from datetime import datetime


@dataclass
class Quize:
    id: int
    question: str
    answer: str
    creation_date: datetime
