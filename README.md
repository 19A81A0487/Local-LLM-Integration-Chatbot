# 🍳 Local LLM Recipe Chatbot

This project implements a **local AI-powered chatbot** that recommends recipes based on user-input ingredients. It uses **FastAPI** to expose an API and a simple Python interface to communicate with the model.

---

## 📌 Objective

- Set up a lightweight language model (LLM) or rule-based system locally.
- Train or fine-tune it using custom recipe data.
- Build an API to interact with the model.
- Create a simple chatbot interface to return recipe recommendations.

---

## 🧱 Project Structure

- **app.py** – FastAPI server exposing the `/get-recipe/` API.
- **recipes.json** – Dataset containing ingredients and recipes.
- **client.py** – Simple command-line chatbot to query the API.
- **README.md** – Documentation and usage guide.

---

## ⚙️ Key Features

- Suggests recipes based on entered ingredients.
- Works offline using local dataset or model.
- Easy-to-use API endpoint via FastAPI.
- CLI-based chatbot interface for real-time interaction.
- Easily extendable to use a fine-tuned LLM.

---

## 🔧 Setup Instructions

1. **Install Dependencies**
   - Use pip to install required packages like FastAPI, Uvicorn, Requests, Transformers, and Torch.
   - A virtual environment is recommended.

2. **Prepare Dataset**
   - Create a JSON file with a list of common ingredients and corresponding recipes.

3. **Start the Server**
   - Launch the FastAPI app and keep the server running to serve API requests.

4. **Access the API**
   - Use the Swagger UI at `http://127.0.0.1:8000/docs` to test the API.
   - The API accepts a list of ingredients and returns a suggested recipe.

5. **Chatbot Interface**
   - Use a simple Python script that collects user input, sends it to the API, and displays the response.

---

## 🧠 Model Fine-Tuning (Optional)

- You can fine-tune a small model (like GPT-2 or TinyLlama) using recipe-specific prompt-response format data.
- Hugging Face Transformers library can be used for training.
- Save and load the model locally for inference through the API.

---

## 🚀 Future Enhancements

- Add a web-based UI using Streamlit or HTML/CSS.
- Integrate LLM for more conversational responses.
- Add support for fuzzy ingredient matching using NLP embeddings.
- Convert to a Dockerized microservice for deployment.

---

## 📚 API Overview

- **POST `/get-recipe/`**
  - Accepts: JSON with a list of ingredients
  - Returns: A matching recipe as a text response

---

## 📄 License

Open-source. Free to use for educational and personal projects.

---



## 📥 Example Input

```json
{
  "ingredients": ["egg", "onion"]
}

📤 Example Output

{
  "ingredients": ["egg", "onion"],
  "recipe": "Scrambled eggs with sautéed onions."
}






## 👤 Author

**Venky Madasu**  
AI/ML Engineer | Data Scientist  
📧 venkannamadasu87@gmail.com

---
