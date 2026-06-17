# CareerForge AI Copilot

## Overview

CareerForge AI Copilot is an AI-powered career assistant that helps users analyze resumes, calculate ATS scores, identify skill gaps, and interact with a Retrieval-Augmented Generation (RAG) based career chatbot.

The system combines FastAPI, Sentence Transformers, ChromaDB, and Google Gemini to provide intelligent resume analysis and career guidance.

---

## Features

* Resume Upload and Parsing
* Resume Skill Extraction
* Job Description Skill Analysis
* ATS Score Calculation
* Semantic Resume Search
* Vector Embeddings using Sentence Transformers
* ChromaDB Vector Database
* Retrieval-Augmented Generation (RAG)
* Gemini-Powered Career Copilot
* FastAPI REST APIs
* Swagger Documentation

---

## Architecture

Resume PDF
↓
Resume Parser
↓
Text Chunking
↓
Sentence Embeddings
↓
ChromaDB Vector Store
↓
Retriever
↓
Gemini LLM
↓
Career Insights

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI / ML

* Sentence Transformers
* Google Gemini
* RAG Architecture

### Vector Database

* ChromaDB

### Document Processing

* PyMuPDF

---

## API Endpoints

### Upload Resume

POST /upload-resume

Uploads and analyzes a resume.

### Analyze Job Description

POST /analyze-job

Calculates ATS score and skill match.

### Ask Copilot

POST /ask-copilot

Queries the RAG-powered career assistant.

---

## Installation

```bash
git clone <repository-url>
cd CareerForge-AI-Copilot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn backend.main:app --reload
```

---

## Future Improvements

* Streamlit Frontend
* Resume Rewriter
* Interview Question Generator
* Skill Gap Analyzer
* Multi-Resume Comparison
* Resume Ranking System
* Job Recommendation Engine

---

## Author

Balaram Krishna
