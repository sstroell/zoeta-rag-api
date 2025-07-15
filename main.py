from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Zoeta RAG API is online"}
