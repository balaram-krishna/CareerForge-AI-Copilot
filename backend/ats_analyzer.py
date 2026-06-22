from backend.services.jd_analyzer import extract_jd_skills

def calculate_ats_score(resume_skills, job_description):

    jd_skills = extract_jd_skills(job_description)

    matched_skills = []
    missing_skills = []

    resume_skills_lower = [s.lower() for s in resume_skills]

    for skill in jd_skills:

        if skill.lower() in resume_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total = len(jd_skills)

    score = (
        round((len(matched_skills) / total) * 100)
        if total > 0 else 0
    )

    suggestions = []

    if missing_skills:
        suggestions.append(
            f"Consider adding skills/projects related to: {', '.join(missing_skills)}"
        )

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }