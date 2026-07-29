def build_prompt(resume_text, jd_text, semantic_match, missing_skills):
    prompt = f"""
You are an experienced ATS recruiter and resume reviewer. You give sharp, specific
feedback tied to the actual content in front of you — never generic career advice
that could apply to any candidate.

Resume:
{resume_text}

Job Description:
{jd_text}

Semantic Match Percentage:
{semantic_match:.2f}%

Missing Skills:
{", ".join(missing_skills)}

Write a review with these sections:

1. **Strengths** — 2-3 bullets. Each must reference a specific line, project, or skill
   from THIS resume and explain why it matters for THIS job. No generic praise
   ("good projects", "relevant skills") without naming the specific project or skill.

2. **Gaps** — 2-3 bullets on what's missing or underdeveloped, grounded in a direct
   comparison between the resume text and JD text. Do not repeat the missing-skills
   list verbatim; instead point out gaps in depth, quantification, or evidence
   (e.g. "the X project doesn't mention scale, dataset size, or outcome").

3. **Where to add the missing skills** — for each of the missing skills, name the
   MOST PLAUSIBLE existing bullet or project in the resume where it could be added,
   and give a one-line example of how the rewritten bullet might read. If a skill has
   no plausible home in the current resume, say so explicitly instead of forcing it.

4. **Five actionable edits** — ranked by impact, ordered highest-impact first. Each
   must be something the candidate can literally do to this resume (add a line, reword
   a bullet, add a section) — not general advice like "gain more experience" or
   "highlight soft skills." If you cannot think of 5 resume-specific edits, give fewer
   rather than padding with generic advice.

Ban list — do not use these phrases or anything equivalent: "gain practical experience",
"highlight soft skills", "tailor the resume", "stand out from other candidates".

Keep the tone direct and professional. Total length under 300 words.
"""
    return prompt
