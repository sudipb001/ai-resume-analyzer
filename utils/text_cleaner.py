import re


def clean_text(text: str) -> str:
    """
    Clean and normalize text for keyword matching.

    Steps:
    - Lowercase
    - Remove special characters
    - Normalize whitespace
    """

    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Replace non-alphanumeric characters with space
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Normalize multiple spaces/newlines → single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()
