import os
from aiwriter.agents.context_builder import build_context
from aiwriter.agents.writer import write_essay
from aiwriter.agents.ranker import rank_essay
from aiwriter.env import DRAFTS_DIR

SCORE_THRESHOLD = 8


def all_scores_greater_than_threshold(scores, threshold=SCORE_THRESHOLD):
    return all(
        float(v) > threshold
        for v in scores.__dict__.values()
        if isinstance(v, (int, float))
    )


def agent_loop(
    max_iters: int = 6,
    length: int = 1000,
    style: str = "informal and analytical",
    audience: str = "sophisticated readers",
):
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    scores = None
    for i in range(1, max_iters + 1):
        if i == 1:
            context = build_context()
            essay = write_essay(
                context,
                length=length,
                style=style,
                audience=audience,
                rewrite=False,
            )
        else:
            essay = write_essay(
                str(context),
                length=length,
                style=style,
                audience=audience,
                rewrite=True,
            )
        context = essay
        draft_path = f"{DRAFTS_DIR}/draft_{i}.md"
        with open(draft_path, "w") as f:
            f.write(str(essay))

        scores = rank_essay(str(essay))
        score_path = f"{DRAFTS_DIR}/draft_score_{i}.md"
        with open(score_path, "w") as f:
            f.write(str(scores))

        print(f"Draft #{i} - {context.title}")
        print(f"Scores:\n\n{scores}")

        if all_scores_greater_than_threshold(scores, threshold=SCORE_THRESHOLD):
            print(f"All scores above {SCORE_THRESHOLD} at iteration {i}. Exiting loop.")
            break
