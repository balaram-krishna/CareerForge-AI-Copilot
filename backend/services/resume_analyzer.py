SKILLS_DB = [
    "Python",
    "SQL",
    "FastAPI",
    "React",
    "Java",
    "JavaScript",
    "Node.js",
    "Docker",
    "Kubernetes",
    "AWS",
    "GCP",
    "Machine Learning",
    "Tableau",
    "Power BI",
    "Snowflake",
    "Oracle",
    "PostgreSQL",
    "MongoDB",
    "Redis",
    "Firebase",
    "GraphQL",
    "REST API",
    "RAG",
    "LLM",
    "OpenAI",
    "Gemini",
    "Vector Embeddings",
    "ChromaDB",
    "Qdrant",
    "Terraform",
    "Jenkins",
    "GitHub Actions"
]


def extract_skills(text):
    """
    Extract skills from resume text using keyword matching.
    """

    skills_found = []

    text = text.lower()

    for skill in SKILLS_DB:
        if skill.lower() in text:
            skills_found.append(skill)

    return sorted(list(set(skills_found)))


if __name__ == "__main__":

    sample_resume = """
    Python
    FastAPI
    Docker
    AWS
    React
    PostgreSQL
    """

    skills = extract_skills(sample_resume)

    print("Skills Found:")
    print(skills)