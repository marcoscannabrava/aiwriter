import instructor
from pydantic import BaseModel
from aiwriter.env import MODEL, WRITER_SYSTEM_PROMPT, CRITERIA


class Essay(BaseModel):
    title: str
    content: str

    def __str__(self):
        return f"Title: {self.title}\n\nContent:\n{self.content}"


def write_essay(
    context: str,
    length: int = 1000,
    style: str = "informal and analytical",
    audience: str = "sophisticated readers",
) -> Essay:
    """Pass prompt to LLM and return the response."""
    from typing import cast

    llm = instructor.from_provider(MODEL)

    prompt = (
        WRITER_SYSTEM_PROMPT.replace("{{context}}", context)
        .replace("{{length}}", str(length))
        .replace("{{style}}", style)
        .replace("{{audience}}", audience)
        .replace("{{criteria}}", ", ".join(CRITERIA))
    )
    return cast(
        Essay,
        llm.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            response_model=Essay,
        ),
    )
