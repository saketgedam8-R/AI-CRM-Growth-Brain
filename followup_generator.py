# followup_generator.py
import os
from openai import OpenAI

def generate_followup(lead_name: str,
                      product_name: str = "AI-CRM Growth Brain",
                      tone: str = "Professional",
                      goal: str = "Schedule a demo",
                      brief_points: str = "") -> str:
    """
    Returns a short personalized follow-up message for a lead using the new OpenAI API.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "ERROR: OpenAI API key not found. Add OPENAI_API_KEY to your app secrets."

    # Create client using new SDK format
    client = OpenAI(api_key=api_key)

    system_prompt = (
        "You are a concise, professional sales assistant that writes short, human, "
        "and persuasive follow-up messages tailored to the lead. Keep it under 3 sentences, "
        "include a clear CTA, and avoid jargon."
    )

    user_prompt = (
        f"Write a short {tone.lower()} follow-up message to {lead_name} about {product_name}. "
        f"Goal: {goal}. "
        f"{'Include these points: ' + brief_points if brief_points else ''} "
        "Keep it friendly, confident, and focused on value. End with a clear CTA."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=120,
            temperature=0.6,
        )

        message = response.choices[0].message.content.strip()
        return message

    except Exception as e:
        return f"⚠️ Error calling OpenAI API: {e}"
