# AI Resume Analyzer

A Streamlit web application that analyzes how well a resume matches a job description. Upload a PDF resume, paste a job description, and get an instant match score, keyword gap analysis, and AI-powered improvement suggestions.

---

## Why This Project

Most job applications are filtered out before a human even reads the resume — not because the candidate is unqualified, but because the resume doesn't align with the job description.

This tool gives you a quick, structured way to:

- See exactly how well your resume matches a job posting
- Identify keywords you're missing
- Get specific AI suggestions to improve your chances of being shortlisted

---

## Features

- **PDF Resume Upload** — extracts text from multi-page PDFs
- **Job Description Input** — paste any job posting
- **Match Score** — percentage score based on keyword overlap
- **Matched Keywords** — words present in both resume and job description
- **Missing Keywords** — gaps sorted by importance (frequency in job description)
- **AI Suggestions** — GPT-powered analysis with missing skills and actionable recommendations
- **Clean Dashboard UI** — built with Streamlit, no frontend setup needed

---

## Tech Stack

| Tool                                                        | Purpose                         |
| ----------------------------------------------------------- | ------------------------------- |
| [Streamlit](https://streamlit.io/)                          | Web UI                          |
| [pdfplumber](https://github.com/jsvine/pdfplumber)          | PDF text extraction             |
| [OpenAI API](https://platform.openai.com/) (`gpt-4.1-mini`) | AI suggestions                  |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variable management |
| Python 3.11+                                                | Runtime                         |

---

## Project Structure

```
ai-resume-analyzer/
├── app.py              # Streamlit UI and app logic
├── main.py             # Entry point (CLI placeholder)
├── pyproject.toml      # Project metadata and dependencies
├── README.md
├── .env                # API keys (not committed)
└── utils/
    ├── pdf_parser.py   # PDF text extraction via pdfplumber
    ├── text_cleaner.py # Lowercase, remove special chars, normalize whitespace
    ├── scorer.py       # Keyword matching and score calculation
    └── ai_helper.py    # OpenAI API integration
```

Each utility module has a single responsibility, making the codebase easy to extend or test independently.

---

## How It Works

1. The uploaded PDF is parsed page-by-page using `pdfplumber`
2. Both the resume and job description are cleaned: lowercased, special characters removed, whitespace normalized
3. Job description keywords (words longer than 2 characters) are extracted and scored by frequency
4. A match score is calculated: `(matched keywords / total job keywords) × 100`
5. Missing keywords are returned sorted by how often they appear in the job description (most important first)
6. On demand, the resume and job description are sent to `gpt-4.1-mini` which returns structured missing skills and specific suggestions

---

## Setup

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-resume-analyzer
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
uv run streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Usage

1. Open the app in your browser
2. Upload your resume as a PDF file
3. Paste the full job description into the text area
4. Review your match score, matched keywords, and missing keywords
5. Click **Generate AI Suggestions** for detailed improvement advice

---

## Limitations

This is a keyword-matching system with real-world constraints:

- **Image-based PDFs will fail** — no OCR support; the PDF must contain selectable text
- **No semantic understanding** — synonyms are not matched (e.g., `JS` ≠ `JavaScript`)
- **No context awareness** — a keyword match doesn't mean the experience level matches
- **Equal keyword weighting** — all matched words count the same regardless of importance
- **AI suggestions may vary** — results depend on the quality and length of inputs

Use this tool as a guide to improve alignment, not as a definitive hiring signal.

Possible Improvements
OCR support for scanned resumes
Skill synonym mapping
Weighted scoring system
Embedding-based similarity
Resume rewriting using AI
Export results (PDF/CSV)
Course Context

This project is designed as a practical, real-world mini project.

Focus is on:

Clean structure
Practical trade-offs
Real limitations (not hidden)
License

This project is for educational purposes.

---

## Optional Improvement (Later)

You can later add:

- Screenshot of UI
- Demo GIF
- Hosted version link

---
