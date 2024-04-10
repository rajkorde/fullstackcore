from fastapi import APIRouter
from openai import OpenAI

from app.schemas.interaction import Question, Answer

router = APIRouter()

@router.post("/", status_code=201, response_model=Answer)
def answer(
    *,
    question: Question
) -> dict:
    """
    Get a question answered through AI
    """

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question.question}
        ]
    )
    answer = completion.choices[0].message.content

    # answer = "Test answer"

    # get answer from client

    return {
        "question": question.question,
        "answer": answer
    }