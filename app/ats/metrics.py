def calculate_skill_coverage(
    jd_skills,
    missing_skills,
):
    """
    Calculates how many required skills
    are covered by the resume.
    """

    if len(jd_skills) == 0:
        return 0

    matched_skills = len(jd_skills) - len(missing_skills)

    coverage = (matched_skills / len(jd_skills)) * 100

    return round(coverage, 2)


def calculate_contact_score(resume):
    """
    Calculates the contact information score
    based on the availability of:
    - Name
    - Email
    - Phone Number
    """

    score = 0

    if resume.get("name"):
        score += 33.33

    if resume.get("email"):
        score += 33.33

    if resume.get("phone"):
        score += 33.34

    return round(score, 2)


def calculate_length_score(resume):
    """
    Calculates the resume length score
    based on the number of words.
    """

    cleaned_text = resume["metadata"]["cleaned_text"]

    word_count = len(cleaned_text.split())

    if 300 <= word_count <= 700:
        return 100

    elif 200 <= word_count < 300:
        return 80

    elif 701 <= word_count <= 900:
        return 80

    else:
        return 50
