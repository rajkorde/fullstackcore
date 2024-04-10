from fastapi import APIRouter

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
    answer = "Test answer"

    # get answer from client

    return {
        "question": question.question,
        "answer": answer
    }