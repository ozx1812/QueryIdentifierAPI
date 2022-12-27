from fastapi import FastAPI
from typing import Optional, List, Dict
from pydantic import BaseModel
from query_service import classify_query_service

app = FastAPI()

class Text(BaseModel):
    text: str


@app.get("/")
def home():
    return {"Query Identifier API"}


@app.post("/query")
def classify_query(text: Text):
    return {"query_type": classify_query_service(text.text) }


