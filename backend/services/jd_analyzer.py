from backend.services.resume_analyzer import SKILLS_DB

def extract_jd_skills(job_description):

    skills_found = []

    text = job_description.lower()

    for skill in SKILLS_DB:

        if skill.lower() in text:
            skills_found.append(skill)

    return sorted(list(set(skills_found)))


if __name__ == "__main__":

    jd = """
    Looking for a Python Developer.

    Required Skills:
    Python
    FastAPI
    Docker
    AWS
    PostgreSQL
    """

    print(extract_jd_skills(jd))