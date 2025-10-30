# followup_generator.py
import os
import openai

def generate_followup(lead_name: str,
                      product_name: str = "AI-CRM Growth Brain",
                      tone: str = "Professional",
                      goal: str = "Schedule a demo",
                      brief_points: str = "") -> str:
    """
    Returns a short personalized follow-up message for a lead using OpenAI.

    - lead_name: recipient name (e.g., "Asha")
    - product_name: product title for context
    - tone: "Professional" | "Casual" | "Urgent" | etc.
    - goal: short goal like "Schedule a demo", "Request feedback"
    - brief_points: optional short 1-2 lines with bullet points to include
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "ERROR: OpenAI API key not found. Add OPENAI_API_KEY to your app secrets."

    openai.api_key = api_key

    system_prompt = (
        "You are a concise, professional sales assistant that writes short, human, "
        "and persuasive follow-up messages tailored to the lead. Keep it <= 3 sentences, "
        "include a clear call-to-action, and avoid jargon. "
    )

    user_prompt = (
        f"Write a short {tone.lower()} follow-up message to {lead_name} about {product_name}. "
        f"Goal: {goal}. "
        f"{'Include these points: ' + brief_points if brief_points else ''} "
        "Keep it friendly, confident, and focused on value. End with a clear CTA."
    )

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=120,
            temperature=0.6,
            n=1,
        )

        text = resp["choices"][0]["message"]["content"].strip()
        return text

    except Exception as e:
        return f"ERROR: OpenAI request failed: {e}"
