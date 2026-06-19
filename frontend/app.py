import streamlit as st
import requests

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

        response = requests.post(
            "http://127.0.0.1:9000/upload-resume",
            files=files
        )

        if response.status_code == 200:

            data = response.json()

            # Save skills for ATS analysis
            st.session_state["resume_skills"] = data["skills"]

            st.success("Resume Uploaded Successfully")

            st.write("### Skills Found")
            st.write(data["skills"])

            st.write(
                f"Text Length: {data['text_length']}"
            )

        else:
            st.error(response.text)


# =========================
# TAB 2 - ATS Analyzer
# =========================

with tab2:

    st.header("ATS Analyzer")

    job_description = st.text_area(
        "Paste Job Description"
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

        elif job_description:

            response = requests.post(
                "http://127.0.0.1:9000/analyze-job",
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
                    f"{data['score']}%"
                )

                st.write("### Matched Skills")
                st.write(data["matched_skills"])

                st.write("### Missing Skills")
                st.write(data["missing_skills"])

            else:
                st.error(response.text)


# =========================
# TAB 3 - AI Copilot
# =========================

with tab3:

    st.header("CareerForge AI Copilot")

    question = st.text_input(
        "Ask a Question"
    )

    if st.button("Ask Copilot"):

        if question:

            response = requests.post(
                "http://127.0.0.1:9000/ask-copilot",
                json={
                    "question": question
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Answer Generated")

                st.write("### Question")
                st.write(data["question"])

                st.write("### Answer")
                st.write(data["answer"])

            else:
                st.error(response.text)