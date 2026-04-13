import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_suggestions(resume_text: str, job_description: str) -> str:
    """
    Generate AI-based suggestions comparing resume and job description.
    """

    if not resume_text or not job_description:
        return "Insufficient data for AI analysis."

    prompt = f"""
You are an expert technical recruiter.

Compare the resume and job description.

Return ONLY structured output in this format:

Missing Skills:
- skill1
- skill2

Suggestions:
- suggestion1
- suggestion2

Important Rules:
- Be specific
- Do NOT be generic
- Do NOT hallucinate technologies
- Only use information from the input

Resume:
{resume_text[:3000]}

Job Description:
{job_description[:3000]}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,  # keep output stable
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI Error: {str(e)}"
