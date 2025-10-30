# app.py - copy-paste into your repo (replace existing)
import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="AI-CRM Growth Brain — Demo", layout="centered")

# Header / Landing
st.title("🤖 AI-CRM Growth Brain — Demo")
st.subheader("Small demo: Lead scoring + AI follow-up generator")
st.markdown("Boost conversions, automate follow-ups, and visualize performance — LLM + Predictive ML.")

# Sample leads (replace with your dataset or DB later)
leads = pd.DataFrame([
    {"Lead Name":"Asha","Score":0.9,"Email":"asha@x.com"},
    {"Lead Name":"Ravi","Score":0.2,"Email":"ravi@y.com"},
    {"Lead Name":"Priya","Score":0.75,"Email":"priya@z.com"}
])

st.dataframe(leads, use_container_width=True)

# Pick a lead
lead_name = st.selectbox("Pick a lead", leads["Lead Name"].tolist())
lead_row = leads[leads["Lead Name"]==lead_name].iloc[0]

st.write("Lead details:")
st.table(pd.DataFrame([lead_row]))

# Personalization options for follow-up
st.markdown("### ✉️ Generate follow-up message")
product_name = st.text_input("Product name", "AI-CRM Growth Brain")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Persuasive"])
goal = st.selectbox("Goal", ["Schedule a demo", "Close the deal", "Share offer", "Get reply"])

# Button -> call LLM (OpenAI) to generate text
if st.button("Generate Follow-up Message"):
    # Build prompt
    prompt = f"""Write a {tone} follow-up message for {lead_name} (email {lead_row['Email']}) about {product_name}.
    The goal is to {goal}. Keep it concise, friendly, and conversion-focused. Include one clear CTA."""
    # Call OpenAI (backend); using OPENAI_API_KEY from environment
    import openai, os
    openai.api_key = os.getenv("OPENAI_API_KEY", "")
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini", # or gpt-4o if available
            messages=[{"role":"user","content":prompt}],
            max_tokens=150,
            temperature=0.6
        )
        text = resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        text = "⚠️ Error calling OpenAI: " + str(e)
    st.success(text)

# Growth Dashboard (simple charts)
st.markdown("### 📊 Growth Dashboard (sample)")
metrics = pd.DataFrame({
    "Metric":["Leads Scored","Follow-ups Sent","Conversions"],
    "Value":[int(len(leads)),  int(len(leads)*0.6), int(len(leads)*0.2)]
})
st.bar_chart(metrics.set_index("Metric"))

st.markdown("---")
st.markdown("Built by **Saket Gedam | AI Product Manager**")
