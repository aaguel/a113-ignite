# main.py — A113 Ignite FastAPI backend
# Serves the classifier and template engine via a REST API

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.classifier import classifier
from app.templates import generate_brief
from app.data import GENRES, TONES, AUDIENCES

app = FastAPI(title="A113 Ignite", version="1.0.0")

# ── Request schema ────────────────────────────────────────────────────────────

class BookInput(BaseModel):
    title: str
    author: str
    audience: str       # CH, MG, YA, Adult
    genre: str
    tone: str
    is_franchise: bool
    is_series: bool
    has_romance: bool

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("app/static/index.html") as f:
        return f.read()

@app.post("/analyze")
async def analyze(book: BookInput):
    """
    Main endpoint — takes book metadata, returns full BookTok content brief.
    """
    # Run classifier
    predicted_angles = classifier.predict(
        audience=book.audience,
        genre=book.genre,
        tone=book.tone,
        is_franchise=book.is_franchise,
        is_series=book.is_series,
        has_romance=book.has_romance
    )

    # Generate content brief from predicted angles
    brief = generate_brief(book.title, book.author, predicted_angles)

    return brief

@app.get("/options")
async def options():
    """
    Returns valid dropdown options for the frontend form.
    """
    return {
        "audiences": AUDIENCES,
        "genres": GENRES,
        "tones": TONES
    }

@app.get("/health")
async def health():
    return {"status": "ok", "model_trained": classifier.trained}