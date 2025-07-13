# 🍳 Local LLM Recipe Chatbot (FastAPI + Python)

A simple chatbot that suggests recipes based on ingredients entered by the user. This project uses FastAPI to expose a local API, and a Python CLI or Swagger UI to interact with the chatbot.

---

## 📁 Project Structure


LocalLLMChatbot/
│
├── app.py # FastAPI server with recipe logic
├── client.py # Command-line chatbot to test API
├── recipes.json # Dataset of ingredients and recipes
├── README.md # Documentation file
└── requirements.txt # Python dependencies (optional)



---

## ✅ Features

- 🧠 Suggests recipes based on user-provided ingredients.
- 🚀 FastAPI backend with a `/get-recipe/` endpoint.
- 🌐 Swagger UI for API testing.
- 🖥️ Simple CLI chatbot using Python.
- 🔧 Easily extendable to LLMs like TinyLlama or GPT2 for richer conversations.

---

## 🧑‍💻 Prerequisites

Ensure you have Python 3.8+ installed.

---

## 🔧 Step 1: Setup & Install Dependencies



# Install required packages
pip install fastapi uvicorn requests torch transformers





📦 Step 2: Prepare Dataset
Create a file named recipes.json with the following sample data:


[
  {
    "ingredients": ["egg", "onion"],
    "recipe": "Scrambled eggs with sautéed onions."
  },
  {
    "ingredients": ["tomato", "pasta"],
    "recipe": "Tomato pasta with garlic and herbs."
  }
]




🚀 Step 3: Start the FastAPI Server
Create a file app.py with the API code:


from fastapi import FastAPI
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



Start the server:

uvicorn app:app --reload



Go to http://127.0.0.1:8000/docs to test it interactively via Swagger UI.




🤖 Step 4: Test with CLI Chatbot
Create client.py to interact with your API:



import requests

while True:
    user_input = input("Enter ingredients (comma separated): ")
    ingredients = [i.strip().lower() for i in user_input.split(',')]
    
    response = requests.post("http://127.0.0.1:8000/get-recipe/", json={"ingredients": ingredients})
    
    if response.status_code == 200:
        print("🍽️  Recipe:", response.json()["recipe"])
    else:
        print("❌ Error:", response.status_code, response.text)


Run the script:

python client.py


Example input:

Enter ingredients (comma separated): egg, onion


📬 API Reference
POST /get-recipe/

Body: JSON object with ingredients list.

Returns: Recipe string based on matched ingredients.



🧠 Optional: Future Enhancements
🔁 Fine-tune GPT2 or TinyLlama on recipe text.

🌐 Add a web UI using Streamlit or HTML + JS.

🧠 Use sentence embeddings for better ingredient matching.

📦 Dockerize the application.

