from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    title="Quote API",
    description="Simple FastAPI backend for Docker learning",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    {
        "id": 1,
        "text": "First, solve the problem. Then, write the code.",
        "author": "John Johnson"
    },
    {
        "id": 2,
        "text": "Programs must be written for people to read.",
        "author": "Harold Abelson"
    },
    {
        "id": 3,
        "text": "The best way to learn programming is by programming.",
        "author": "Unknown"
    },
    {
        "id": 4,
        "text": "Code is like humor. When you have to explain it, it is bad.",
        "author": "Cory House"
    },
    {
        "id": 5,
        "text": "Simplicity is the soul of efficiency.",
        "author": "Austin Freeman"
    }
]


@app.get("/")
def home():
    return {
        "message": "Quote API is running!",
        "status": "success"
    }


@app.get("/quote")
def get_random_quote():
    return random.choice(quotes)


@app.get("/quotes")
def get_all_quotes():
    return {
        "count": len(quotes),
        "quotes": quotes
    }