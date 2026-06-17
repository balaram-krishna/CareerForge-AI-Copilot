def calculate_ats_score(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = list(resume_set.intersection(jd_set))
    missing = list(jd_set - resume_set)

    if len(jd_set) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_set)) * 100)

    return {
        "score": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }


if __name__ == "__main__":

    resume_skills = [
        "Python",
        "FastAPI",
        "Docker"
    ]

    jd_skills = [
        "Python",
        "FastAPI",
        "Docker",
        "AWS",
        "PostgreSQL"
    ]

    result = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    print(result)