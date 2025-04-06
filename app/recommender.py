import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embeddings.embedder import get_embedding

with open("data/shl_catalog.json", "r") as f:
    catalog = json.load(f)

catalog_embeddings = [get_embedding(item["description"]) for item in catalog]


async def recommend(data: dict):
    # Your recommendation logic here
    return {"recommendations": []}


def recommend(query: str, top_k=5):
    query_vec = get_embedding(query)
    print("Query vector shape:", query_vec.shape)

    scores = cosine_similarity([query_vec], catalog_embeddings)[0]
    scores = (scores - scores.min()) / (scores.max() - scores.min())

    print("All scores:", scores)

    top_indices = scores.argsort()[-top_k:][::-1]
    print("Top indices:", top_indices)
    print("Top scores:", [scores[i] for i in top_indices])

    results = [catalog[i] | {"score": float(scores[i])} for i in top_indices]

    return results
