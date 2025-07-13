import requests

while True:
    user_input = input("Enter ingredients (comma separated): ")
    ingredients = [i.strip().lower() for i in user_input.split(',')]
    
    response = requests.post("http://127.0.0.1:8000/get-recipe/", json={"ingredients": ingredients})
    
    if response.status_code == 200:
        print("🍽️  Recipe:", response.json()["recipe"])
    else:
        print("❌ Error:", response.status_code, response.text)
