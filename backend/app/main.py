from fastapi import FastAPI
from .api import router
from .db import create_tables
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="MemoryPal API")

@app.on_event("startup")
async def startup_event():
    create_tables()

app.include_router(router)