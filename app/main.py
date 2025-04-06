from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.recommender import recommend

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8501"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommend")
async def get_recommendation(request: Request):
    data = await request.json()
    query = data.get("query", "")
    num_recs = data.get("num_recommendations", 5)
    result = recommend(query, num_recs)
    return {"recommendations": result}
