from ai.prompt import build_prompt
from ai.llm_client import get_llm_response


def generate_resume_suggestions(resume_text, jd_text, semantic_match, missing_skills):

    prompt = build_prompt(resume_text, jd_text, semantic_match, missing_skills)

    suggestions = get_llm_response(prompt)

    return suggestions
