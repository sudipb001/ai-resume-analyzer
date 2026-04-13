import pdfplumber

def extract_text_from_pdf(file) -> str:
    """
    Extract text from a PDF file using pdfplumber.

    Returns:
        str: Extracted text (can be empty if extraction fails)
    """

    text_chunks = []

    try:
        with pdfplumber.open(file) as pdf:
            if not pdf.pages:
                return ""

            for page_number, page in enumerate(pdf.pages, start=1):
                try:
                    page_text = page.extract_text()

                    if page_text:
                        text_chunks.append(page_text)

                except Exception as page_error:
                    # Skip problematic page, continue processing
                    print(f"[WARN] Failed on page {page_number}: {page_error}")
                    continue

    except Exception as e:
        # Entire PDF failed to open
        print(f"[ERROR] Failed to read PDF: {e}")
        return ""

    return "\n".join(text_chunks).strip()
