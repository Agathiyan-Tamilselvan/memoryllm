# MemoryPal Starter

A simple LLM-powered memory assistant ("Memory Pal") that lets you chat with an AI, stores your conversations as memories, and retrieves/summarizes them using embeddings.

## Features
- Chat with an LLM (OpenAI GPT-3.5-turbo).
- Store and retrieve memories (conversations).
- Semantic search via embeddings.
- Automatic summarization for long memories.
- Web UI for chatting and viewing memories.

## Setup
1. Clone this repo.
2. Copy `.env.example` to `.env` and add your OpenAI API key: `OPENAI_API_KEY=your_key_here`.
3. Run `docker-compose up` to build and start the app.
4. Access the frontend at `http://localhost:3000` and API at `http://localhost:8000`.

## API Endpoints
- `POST /chat`: Send a message and get a response (stores memory).
- `GET /memories`: List all memories.
- `GET /memories/search?query=...`: Search memories by embedding similarity.
- `GET /memories/{id}`: Get a specific memory.

## Tech Stack
- Backend: FastAPI (Python), SQLAlchemy, sentence-transformers, OpenAI.
- Frontend: React (Vite), Axios.
- Database: SQLite (via Docker).
- Containerization: Docker Compose."# memoryllm" 
