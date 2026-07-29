from analyzer.resumee_analyze import analyze_resume
from analyzer.jd_analyzer import analyze_job_description

from matcher.embeddings import generate_embeddings

from matcher.matcher import (
    match_embeddings,
    calculate_semantic_match,
    missing_skills,
)

from ai.suggestion_generator import generate_resume_suggestions
from ats.metrics import (
    calculate_skill_coverage,
    calculate_contact_score,
    calculate_length_score,
)

from ats.ats_score import calculate_ats_score


def analyze_resume_against_jd(resume_pdf, jd_pdf):

    resume = analyze_resume(resume_pdf)
    jd = analyze_job_description(jd_pdf)

    resume_skills = resume["skills"]
    jd_skills = jd["skills"]

    resume_embeddings = generate_embeddings(resume_skills)
    jd_embeddings = generate_embeddings(jd_skills)

    matches = match_embeddings(
        resume_skills,
        resume_embeddings,
        jd_skills,
        jd_embeddings,
    )

    semantic_match = calculate_semantic_match(matches)

    missing = missing_skills(matches, jd_skills)

    skill_coverage = calculate_skill_coverage(
        jd["skills"],
        missing,
    )

    contact_score = calculate_contact_score(
        resume,
    )

    length_score = calculate_length_score(
        resume,
    )

    ats_score = calculate_ats_score(
        semantic_match,
        skill_coverage,
        contact_score,
        length_score,
    )
    suggestions = generate_resume_suggestions(
        resume_text=resume["metadata"]["cleaned_text"],
        jd_text=jd["metadata"]["cleaned_text"],
        semantic_match=semantic_match,
        missing_skills=missing,
    )

    return {
        "semantic_match": semantic_match,
        "ats_score": ats_score,
        "missing_skills": missing,
        "suggestions": suggestions,
    }
