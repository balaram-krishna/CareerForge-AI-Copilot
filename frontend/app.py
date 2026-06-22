```python
import streamlit as st
import requests

BACKEND_URL = "https://careerforge-ai-copilot-3.onrender.com"

st.set_page_config(
    page_title="CareerForge AI Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerForge AI Copilot")
st.write("AI-Powered Resume & Career Assistant")

tab1, tab2, tab3 = st.tabs(
    [
        "📄 Upload Resume",
        "📊 ATS Analyzer",
        "🤖 AI Copilot"
    ]
)

# =========================
# TAB 1 - Resume Upload
# =========================

with tab1:

    st.header("Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"]
    )

    if uploaded_file:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        try:

            response = requests.post(
                f"{BACKEND_URL}/upload-resume",
                files=files
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["resume_skills"] = data.get(
                    "skills",
                    []
                )

                st.success("Resume Uploaded Successfully")

                st.write("### Skills Found")
                st.write(
                    data.get("skills", [])
                )

                st.write(
                    f"Text Length: {data.get('text_length', 0)}"
                )

            else:
                st.error(response.text)

        except Exception as e:
            st.error(f"Error: {e}")


# =========================
# TAB 2 - ATS Analyzer
# =========================

with tab2:

    st.header("ATS Analyzer")

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    if st.button("Analyze ATS Score"):

        resume_skills = st.session_state.get(
            "resume_skills",
            []
        )

        if not resume_skills:

            st.warning(
                "Please upload a resume first."
            )

        elif not job_description.strip():

            st.warning(
                "Please paste a Job Description."
            )

        else:

            try:

                response = requests.post(
                    f"{BACKEND_URL}/analyze-job",
                    json={
                        "resume_skills": resume_skills,
                        "job_description": job_description
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        "ATS Analysis Complete"
                    )

                    st.metric(
                        "ATS Score",
                        f"{data.get('score', 0)}%"
                    )

                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("### ✅ Matched Skills")
                        st.write(
                            data.get(
                                "matched_skills",
                                []
                            )
                        )

                    with col2:
                        st.write("### ❌ Missing Skills")
                        st.write(
                            data.get(
                                "missing_skills",
                                []
                            )
                        )

                    st.write(
                        "### 💡 Resume Improvement Suggestions"
                    )

                    suggestions = data.get(
                        "suggestions",
                        ""
                    )

                    if suggestions:

                        if isinstance(
                            suggestions,
                            list
                        ):

                            for item in suggestions:
                                st.write(f"• {item}")

                        else:
                            st.write(suggestions)

                    else:

                        st.info(
                            "No suggestions available."
                        )

                    with st.expander(
                        "Debug API Response"
                    ):
                        st.json(data)

                else:

                    st.error(
                        f"Backend Error: {response.text}"
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )


# =========================
# TAB 3 - AI Copilot
# =========================

with tab3:

    st.header("CareerForge AI Copilot")

    question = st.text_input(
        "Ask a Career Question"
    )

    if st.button("Ask Copilot"):

        if question.strip():

            try:

                response = requests.post(
                    f"{BACKEND_URL}/ask-copilot",
                    json={
                        "question": question
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        "Answer Generated"
                    )

                    st.write(
                        "### Question"
                    )

                    st.write(
                        data.get(
                            "question",
                            question
                        )
                    )

                    st.write(
                        "### Answer"
                    )

                    st.write(
                        data.get(
                            "answer",
                            "No answer returned."
                        )
                    )

                else:

                    st.error(
                        response.text
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )