from pydantic import BaseModel

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    question: str
    answer: str