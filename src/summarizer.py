from hosted_client import generate_hosted_response
from ollama_client import generate_response
from pathlib import Path

def load_prompt() -> str:
    # Build the path to prompts/summarize.txt-
    # prompt_path = Path("prompts") / "summarize.txt"
    prompt_path = (
        Path(__file__).resolve().parent.parent
        / "prompts"
        / "summarize.txt"
    )
    # Read and return the prompt
    return prompt_path.read_text(encoding="utf-8")

def summarize_note(note: str, use_hosted: bool = False) -> str:
    template = load_prompt()
    prompt = template.format(note=note)

    if use_hosted:
        return generate_hosted_response(prompt)

    return generate_response(prompt)


# if __name__ == "__main__":
#     note = """Meeting notes:
# - Finish API integration before Friday
# - Ahmed will handle testing
# - Database migration still not completed
# - Main blocker: missing production credentials
# - Next meeting Monday morning"""
#     # note = """ذاكرت النهارده Linear Regression و Gradient Descent.
#     # فهمت إن Linear Regression بيستخدم لتوقع continuous values.
#     # الـ learning rate بيحدد حجم كل update أثناء training.
#     # بكرة هراجع Logistic Regression و Classification Metrics."""

#     summary = summarize_note(note)
#     print(summary)