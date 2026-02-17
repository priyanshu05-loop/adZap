from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AdZap AI Backend")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AdZap Backend Running"}
