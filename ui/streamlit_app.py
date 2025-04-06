import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("🧠 SHL Assessment Recommendation Engine")
st.markdown("Enter a job description or a free-form query to get assessment suggestions.")

query_input = st.text_area("📝 Enter your job description or query:")
top_k = st.slider("🔢 Number of recommendations", 1, 10, 5)

if st.button("🔍 Recommend"):
    with st.spinner("Finding best matches..."):
        res = requests.post("http://localhost:8000/recommend", json={"query": query_input, "top_k": top_k})
        if res.status_code == 200:
            data = res.json()["recommendations"]
            st.success("Recommendations found!")
            st.table([{k: v for k, v in r.items() if k != 'score'} for r in data])
        else:
            st.error("Error fetching results. Is the FastAPI server running?")

url = st.text_input("🌐 Or paste a JD URL:")

if url:
    from utils.jd_utils import extract_text_from_url
    query_input = extract_text_from_url(url)
