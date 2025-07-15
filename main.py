
from fastapi import FastAPI, Request
from app.query_engine import query_llama_index

app = FastAPI()

@app.post("/query")
async def get_answer(request: Request):
    body = await request.json()
    question = body.get("question", "")
    answer, source = query_llama_index(question)
    return {"answer": answer, "source": source}
