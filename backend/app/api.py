from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .models import Memory
from .db import get_db
from .embeddings import generate_embedding, search_similar
from .summarizer import summarize_memory
from .indexer import index_memory
from sqlalchemy.orm import Session
from typing import List
import openai
import os

router = APIRouter()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

class MemoryResponse(BaseModel):
    id: int
    conversation: str
    summary: str = None

@router.post("/chat", response_model=dict)
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        ai_response = response.choices[0].message.content
        conversation = f"User: {request.message}\nAI: {ai_response}"
        
        # Summarize if long
        summary = None
        if len(conversation) > 500:
            summary = summarize_memory(conversation)
        
        # Create memory
        db: Session = next(get_db())
        memory = Memory(conversation=conversation, summary=summary)
        db.add(memory)
        db.commit()
        db.refresh(memory)
        
        # Index for search
        index_memory(memory.id, conversation)
        
        return {"response": ai_response, "memory_id": memory.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/memories", response_model=List[MemoryResponse])
async def get_memories():
    db: Session = next(get_db())
    memories = db.query(Memory).all()
    return memories

@router.get("/memories/{memory_id}", response_model=MemoryResponse)
async def get_memory(memory_id: int):
    db: Session = next(get_db())
    memory = db.query(Memory).by_id(memory_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
    return memory

@router.get("/memories/search", response_model=List[MemoryResponse])
async def search_memories(query: str):
    similar_ids = search_similar(query)
    db: Session = next(get_db())
    memories = db.query(Memory).filter(Memory.id.in_(similar_ids)).all()
    return memories