from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from openai import OpenAI  # type: ignore
import os

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def idea():
    # Get API key from environment variable (set in Vercel dashboard)
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "Error: OPENAI_API_KEY environment variable not set"
    
    client = OpenAI(api_key=api_key)
    prompt = [{"role": "user", "content": "Come up with a new idea to lose weight with AI"}]
    # Fixed model name - gpt-5-nano doesn't exist, using gpt-4o-mini or gpt-3.5-turbo
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=prompt
        )
        return response.choices[0].message.content or "No response from API"
    except Exception as e:
        return f"Error calling OpenAI API: {str(e)}"