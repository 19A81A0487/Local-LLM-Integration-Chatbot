from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe Chatbot API!"}

# Load recipe data
with open("recipes.json", "r") as f:
    recipe_data = json.load(f)

class IngredientsInput(BaseModel):
    ingredients: list[str]

def find_recipe(user_ingredients):
    for item in recipe_data:
        if all(ing.lower() in item['ingredients'] for ing in user_ingredients):
            return item['recipe']
    return "Sorry, no matching recipe found for those ingredients."

@app.post("/get-recipe/")
async def get_recipe(data: IngredientsInput):
    recipe = find_recipe(data.ingredients)
    return {"ingredients": data.ingredients, "recipe": recipe}
