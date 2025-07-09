from fastapi import FastAPI

app = FastAPI(title="Tauk Backend", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World from Tauk Backend"}

@app.get("/health")
async def health():
    return {"status": "healthy"} 