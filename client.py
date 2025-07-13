import requests

while True:
    user_input = input("Enter ingredients (comma separated): ")
    ingredients = [i.strip().lower() for i in user_input.split(',')]
    response = requests.post("http://127.0.0.1:8000/get-recipe/", json={"ingredients": ingredients})
    print("Bot:", response.json()["recipe"])
