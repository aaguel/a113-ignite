# A113 Ignite 🎬

> A BookTok marketing intelligence tool for Disney Publishing × DramaBox
https://a113-ignite-57002663970.us-central1.run.app


## What it does

A113 Ignite takes a Disney Publishing book's metadata and predicts which short-form video content angles will perform on DramaBox — generating ready-to-use hooks, content ideas, audio recommendations, and captions for creators.

## How it works

1. **Hand-labeled dataset** — 35 Disney Publishing titles (2023–2026) labeled across 12 content angle categories
2. **Multi-label classifier** — scikit-learn logistic regression trained on structured book metadata (genre, tone, audience, franchise status, romance)
3. **Template engine** — maps predicted angles to concrete DramaBox content briefs
4. **FastAPI backend + polished frontend** — deployed on Google Cloud Run

## Content angles

`dark_academia` · `emotional_devastation` · `romance_slowburn` · `enemies_to_lovers` · `fandom_nostalgia` · `mystery_hook` · `identity_coming_of_age` · `aesthetic_vibes` · `fandom_franchise` · `found_family` · `cultural_identity` · `lgbtq+`

## Tech stack

- Python 3.11
- FastAPI + Uvicorn
- scikit-learn (LogisticRegression, OneVsRestClassifier)
- Google Cloud Run

## Live demo

🔗 https://a113-ignite-57002663970.us-central1.run.app

## Why A113?

A113 is a famous Easter egg in nearly every Pixar and Disney film — a nod to the CalArts classroom where many Disney animators studied. It appears as a room number, license plate, or equipment code across the Disney universe. Just like the Easter egg, A113 Ignite is hidden in plain sight — a tool built specifically for the Disney ecosystem.
