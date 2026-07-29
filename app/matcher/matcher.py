from sklearn.metrics.pairwise import cosine_similarity

THRESHOLD = 0.80


def match_resume_with_jd(resume, job):

    resume_skills = set(resume["skills"])
    jd_skills = set(job["skills"])

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    extra = resume_skills - jd_skills

    if len(jd_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(matched) / len(jd_skills)) * 100

    return {
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing)),
        "extra_skills": sorted(list(extra)),
        "match_percentage": round(match_percentage, 2),
    }


def match_embeddings(resume_skills, resume_embeddings, jd_skills, jd_embeddings):
    matches = []
    for i in range(len(resume_embeddings)):

        best_similarity = 0
        best_match = None

        for j in range(len(jd_embeddings)):

            similarity = cosine_similarity([resume_embeddings[i]], [jd_embeddings[j]])[
                0
            ][0]

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = jd_skills[j]

        if best_similarity >= THRESHOLD:
            matches.append(
                {
                    "resume_skill": resume_skills[i],
                    "jd_skill": best_match,
                    "similarity": round(best_similarity, 2),
                }
            )
        else:
            matches.append(
                {
                    "resume_skill": resume_skills[i],
                    "jd_skill": "No Match",
                    "similarity": round(best_similarity, 2),
                }
            )
    return matches


def calculate_semantic_match(matches):

    total_skills = len(matches)

    if total_skills == 0:
        return 0.0

    matched_skills = 0

    for match in matches:

        if match["similarity"] >= THRESHOLD:
            matched_skills += 1

    return round((matched_skills / total_skills) * 100, 2)


def missing_skills(matches, jd_skills):

    matched_jd_skills = []

    for match in matches:
        if match["jd_skill"] != "No Match":
            matched_jd_skills.append(match["jd_skill"])

    missing_skills = []

    for skill in jd_skills:
        if skill not in matched_jd_skills:
            missing_skills.append(skill)

    return missing_skills
