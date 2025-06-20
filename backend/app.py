from fastapi import FastAPI
import openai
import os

app = FastAPI()

# Replace with your actual API key
openai.api_key = os.getenv("your-openai-API-Key-here")

@app.get("/")
def read_root():
    return {"status": "ChatGPT Backend running"}

@app.post("/generate")
def generate(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if your access allows
        messages=[
            {"role": "system", "content": "You are a helpful AI coding assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=250,
    )
    return {"completion": response.choices[0].message.content}
