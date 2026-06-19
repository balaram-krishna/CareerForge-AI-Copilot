from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from backend.services.rag_pipeline import ingest_resume
from backend.services.vector_store import clear_collection

from backend.services.resume_parser import extract_text_from_pdf
from backend.services.resume_analyzer import extract_skills
from backend.services.jd_analyzer import extract_jd_skills
from backend.services.ats_engine import calculate_ats_score
from backend.services.copilot import ask_copilot

app = FastAPI(
    title="CareerForge AI Copilot",
    description="AI-Powered Resume Analysis, ATS Scoring, and RAG Career Assistant",
    version="1.0.0"
)


# =========================
# Request Models
# =========================

class JobAnalysisRequest(BaseModel):
    resume_skills: list[str]
    job_description: str


class CopilotRequest(BaseModel):
    question: str


# =========================
# Home Route
# =========================

@app.get("/")
def home():
    return {
        "message": "CareerForge AI Copilot Backend is Running"
    }


# =========================
# Resume Upload Endpoint
# =========================

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Remove previous resume vectors
    clear_collection()

    # Store newly uploaded resume
    ingest_resume(file_path)

    extracted_text = extract_text_from_pdf(file_path)

    skills = extract_skills(extracted_text)

    return {
        "filename": file.filename,
        "skills": skills,
        "text_length": len(extracted_text)
    }


# =========================
# ATS Analysis Endpoint
# =========================

@app.post("/analyze-job")
def analyze_job(request: JobAnalysisRequest):

    jd_skills = extract_jd_skills(
        request.job_description
    )

    result = calculate_ats_score(
        request.resume_skills,
        jd_skills
    )

    return result


# =========================
# CareerForge AI Copilot
# =========================

@app.post("/ask-copilot")
def copilot_chat(request: CopilotRequest):

    answer = ask_copilot(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }