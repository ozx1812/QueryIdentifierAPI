from fastapi import FastAPI
from typing import Optional, List, Dict
from pydantic import BaseModel
from enum import Enum
import re

app = FastAPI()

class Text(BaseModel):
    text: str


@app.get("/")
def home():
    return {"Query Identifier API"}



