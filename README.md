# SHL Assessment Recommendation Engine

This project recommends SHL assessments for job roles or queries using semantic embeddings.

## 🛠 Tech Stack
- FastAPI (backend)
- Streamlit (frontend)
- Sentence Transformers (embedding)
- Scikit-learn (similarity)

## 🚀 How to Run
1. `pip install -r requirements.txt`
2. `uvicorn app.main:app --reload`
3. `streamlit run ui/streamlit_app.py`

## 📊 Evaluation
Run `evaluation.ipynb` to compute recall@3 over sample queries.

## 📸 Sample
See `/demo_outputs/` for screenshots and test runs.

## 📦 Deployment
- Can be deployed on Streamlit Cloud or Hugging Face Spaces.
