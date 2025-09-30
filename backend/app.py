from fastapi import FastAPI
from pydantic import BaseModel
from flavorgraph import data, search, subs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FlavorGraph")

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, set to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IngredientRequest(BaseModel):
    available: list[str]

@app.get("/")
def read_root():
    return {
        "message": "Welcome to FlavorGraph API",
        "endpoints": {
            "/suggest": "POST - Send a list of available ingredients to get recipe suggestions",
            "/docs": "API documentation"
        }
    }

@app.post("/suggest")
def suggest(req: IngredientRequest):
    recipes = data.load_recipes()
    subs_map = data.load_subs()

    results = []
    for recipe in recipes:
        missing = [i for i in recipe["ingredients"] if i not in req.available]
        substitutions = {}

        # check substitutions for missing items
        for m in missing:
            if m in subs_map:
                for alt in subs_map[m]:
                    if alt in req.available:
                        substitutions[m] = alt
                        break

        results.append({
            "name": recipe["name"],
            "ingredients": recipe["ingredients"],
            "missing": missing,
            "substitutions": substitutions
        })

    return {"recipes": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
