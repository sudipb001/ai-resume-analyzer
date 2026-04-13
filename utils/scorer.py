def calculate_score(resume_text: str, job_desc_text: str):
    """
    Calculate match score between resume and job description.

    Returns:
        score (float)
        missing_keywords (list)
        matched_keywords (list)
    """

    if not resume_text or not job_desc_text:
        return 0.0, [], []

    # Tokenization (simple split)
    job_keywords = set(job_desc_text.split())
    resume_words = set(resume_text.split())

    # Remove very small tokens (noise like 'a', 'i')
    job_keywords = {word for word in job_keywords if len(word) > 2}

    if not job_keywords:
        return 0.0, [], []

    # Matching
    matched = job_keywords.intersection(resume_words)
    # missing = job_keywords - resume_words

    # Frequency-based importance (simple but effective)
    job_word_list = job_desc_text.split()

    word_freq = {}
    for word in job_word_list:
        if len(word) > 2:
            word_freq[word] = word_freq.get(word, 0) + 1

    missing = list(job_keywords - resume_words)

    # Sort missing by frequency (importance)
    missing_sorted = sorted(
        missing,
        key=lambda w: word_freq.get(w, 0),
        reverse=True
    )

    

    # Score
    score = (len(matched) / len(job_keywords)) * 100

    return round(score, 2), missing_sorted[:20], sorted(list(matched))
    
