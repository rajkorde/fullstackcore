from fastapi import APIRouter, HTTPException
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

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question.question}
            ]
        )
        answer = completion.choices[0].message.content
    except:
        return HTTPException(status_code=500, detail="LLM failed to generate response.")

    # answer = "Test answer"

    return {
        "question": question.question,
        "answer": answer
    }