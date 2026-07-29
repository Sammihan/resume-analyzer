def calculate_ats_score(
    semantic_match,
    skill_coverage,
    contact_score,
    length_score,
):
    """
    Calculates the overall ATS score using
    weighted resume metrics.
    """

    ats_score = (
        semantic_match * 0.50
        + skill_coverage * 0.30
        + contact_score * 0.10
        + length_score * 0.10
    )

    return round(ats_score, 2)
