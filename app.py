import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI-CRM Growth Brain Demo")
st.title("AI-CRM Growth Brain — Demo")

st.markdown("### Small demo: Lead scoring and AI follow-up suggestion")

# Sample data
df = pd.DataFrame({
    "Lead Name": ["Asha", "Ravi", "Priya"],
    "Score": [0.9, 0.2, 0.75],
    "Email": ["asha@x.com", "ravi@y.com", "priya@z.com"]
})

st.dataframe(df)

selected = st.selectbox("Pick a lead", df["Lead Name"])
st.write("Lead details:", df[df["Lead Name"] == selected])

if st.button("Generate Follow-up Message"):
    st.info(f"Hi {selected}, following up to share how our AI CRM can boost your sales by 20%! 🚀")
