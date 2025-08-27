from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routing.article import router
app = FastAPI()

@app.get("/")
async def index():
    return { "message" : "Just testing the line .." }


#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router)