from backend.services.llm_service import model


def generate_resume_suggestions(
    resume_skills,
    matched_skills,
    missing_skills,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Resume Skills:
{resume_skills}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Job Description:
{job_description}

Give:
1. ATS Match Summary
2. Top Resume Improvements
3. Skills to Learn
4. Resume Enhancement Suggestions

Keep the response concise.
"""

    try:

        response = model.generate_content(prompt)

        if not response:
            return "No suggestions generated."

        if not hasattr(response, "text"):
            return "No text returned from Gemini."

        return response.text

    except Exception as e:

        print("RESUME IMPROVER ERROR:", str(e))

        return f"ATS suggestion generation failed: {str(e)}"