import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./memorypal.db")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")