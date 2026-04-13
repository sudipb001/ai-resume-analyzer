import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.scorer import calculate_score
from utils.ai_helper import get_ai_suggestions

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("AI Resume Analyzer")

st.write("Upload your resume and paste the job description to analyze match score.")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "Paste Job Description",
        height=200
    )



if uploaded_file and job_description:
    st.success("Ready to analyze")

    with st.spinner("Extracting text from PDF..."):
        raw_resume_text = extract_text_from_pdf(uploaded_file)

    if not raw_resume_text:
        st.error("Failed to extract text from PDF.")
        st.stop()


    # Clean both texts
    resume_text = clean_text(raw_resume_text)
    job_description_clean = clean_text(job_description)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.caption(f"Resume Length: {len(resume_text.split())} words")
        if len(resume_text.split()) < 50:
            st.warning("Resume text seems too short. PDF may be image-based or poorly extracted.")


    with col2:
        st.caption(f"Job Description Length: {len(job_description_clean.split())} words")


    # Calculate score
    score, missing_keywords, matched_keywords = calculate_score(
        resume_text,
        job_description_clean
    )

    # =============================
    # DASHBOARD SECTION
    # =============================

    st.divider()

    # =============================
    # DASHBOARD SECTION
    # =============================

    st.divider()

    if uploaded_file and job_description:

        with st.spinner("Processing resume..."):
            raw_resume_text = extract_text_from_pdf(uploaded_file)

        if not raw_resume_text:
            st.error("Failed to extract text from PDF.")
            st.stop()

        resume_text = clean_text(raw_resume_text)
        job_description_clean = clean_text(job_description)

        score, missing_keywords, matched_keywords = calculate_score(
            resume_text,
            job_description_clean
        )

        # -----------------------------
        # SCORE SECTION
        # -----------------------------
        st.subheader("Resume Match Score")

        col1, col2 = st.columns([1, 3])

        with col1:
            st.metric("Score", f"{score}%")

        with col2:
            st.progress(int(score))

        # -----------------------------
        # KEYWORDS SECTION
        # -----------------------------
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matched Keywords")
            if matched_keywords:
                st.success(", ".join(matched_keywords[:20]))
            else:
                st.warning("No strong matches found")

        with col2:
            st.subheader("Missing Keywords")
            if missing_keywords:
                st.error(", ".join(missing_keywords))
            else:
                st.success("No major missing keywords")

        # -----------------------------
        # AI SECTION
        # -----------------------------
        st.divider()

        st.info("AI analysis may take a few seconds.")

        if "ai_output" not in st.session_state:
            st.session_state.ai_output = None

        if st.button("Generate AI Suggestions"):
            with st.spinner("Analyzing with AI..."):
                st.session_state.ai_output = get_ai_suggestions(
                    resume_text,
                    job_description
                )

        if st.session_state.ai_output:
            st.subheader("AI Suggestions")
            st.write(st.session_state.ai_output)



else:
    st.info("Please upload a resume and enter job description")