import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def load_recipes():
    with open(BASE / "recipes.json", "r") as f:
        return json.load(f)

def load_subs():
    with open(BASE / "subs.json", "r") as f:
        return json.load(f)
