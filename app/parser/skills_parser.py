from utils.skills_db import SKILLS
from config.section_aliases import SECTION_ALIASES


def extract_skills(text):

    lower_text = text.lower()

    start = -1

    for header in SECTION_ALIASES["skills"]:

        start = lower_text.find(header.lower())

        if start != -1:
            break

    if start == -1:
        return {"skills": []}

    end = len(text)

    END_SECTIONS = [
        "projects",
        "project",
        "education",
        "experience",
        "work experience",
        "professional experience",
        "internships",
        "internship",
        "certifications",
        "certification",
        "achievements",
        "summary",
        "objective",
    ]

    for section in END_SECTIONS:

        index = lower_text.find(section, start + 1)

        if index != -1:
            end = min(end, index)

    skills_section = text[start:end]

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in skills_section.lower():
            found_skills.append(skill)

    return {"skills": found_skills}
