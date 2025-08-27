from fastapi import FastAPI
from app.routing.article import router
app = FastAPI()

@app.get("/")
async def index():
    return { "message" : "Just testing the line .." }

app.include_router(router=router)