from google import genai
from config import api

client = genai.Client(api_key=api)

def inference_gemini(prompt):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

    return response.text

print("BOT: Hi how may I help you?")
while True:
    prompt=input("User: ")  
    print(f"BOT response: {inference_gemini(prompt)}")

