import os

script_dir = os.path.dirname(os.path.abspath(__file__))

CONTEXT_FILE = os.getenv("AIWRITER_CONTEXT_FILE", "context.txt")
CONTEXT_FULL_FILE = os.getenv("AIWRITER_CONTEXT_FULL_FILE", "full_context.txt")
CONTEXT_DIR = os.getenv("AIWRITER_CONTEXT_DIR", "context")

MODEL = os.getenv("AIWRITER_MODEL", "anthropic/claude-sonnet-4-20250514")
ESSAY_FILE = os.getenv("AIWRITER_ESSAY_FILE", "essay.txt")

CRITERIA = "clarity,conciseness,relevance,engagement,accuracy".split(",")
CRITERIA_FILE = os.getenv("AIWRITER_CRITERIA", "criteria.txt")
if os.path.exists(CRITERIA_FILE):
    with open(CRITERIA_FILE) as cf:
        CRITERIA = [c.strip() for c in cf.read().split(",") if c.strip()]

SCORES_FILE = os.getenv("AIWRITER_SCORES", "scores.txt")

DRAFTS_DIR = os.getenv("AIWRITER_DRAFTS_DIR", "drafts")


thinker_prompt_file = (
    open("AIWRITER_THINKER_SYSTEM_PROMPT_FILE", "r")
    if os.path.exists("AIWRITER_THINKER_SYSTEM_PROMPT_FILE")
    else open(os.path.join(script_dir, "agents/thinker.prompt"), "r")
)
THINKER_SYSTEM_PROMPT = thinker_prompt_file.read()
thinker_prompt_file.close()

writer_prompt_file = (
    open("AIWRITER_WRITER_SYSTEM_PROMPT_FILE", "r")
    if os.path.exists("AIWRITER_WRITER_SYSTEM_PROMPT_FILE")
    else open(os.path.join(script_dir, "agents/writer.prompt"), "r")
)
WRITER_SYSTEM_PROMPT = writer_prompt_file.read()
writer_prompt_file.close()
