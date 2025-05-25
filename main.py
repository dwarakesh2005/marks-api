from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data and convert array to dict
with open(os.path.join(os.path.dirname(__file__), "marks.json"), "r") as f:
    data_array = json.load(f)
    marks_data = {item["name"]: item["marks"] for item in data_array}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
