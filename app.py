from flask import Flask, jsonify, request
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "FitBot is live!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are FitBot"},
            {"role": "user", "content": user_msg}
        ]
    )
    
    reply = completion.choices[0].message.content.strip()
    return jsonify({"reply": reply})

# required for vercel
def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)
