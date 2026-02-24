import requests
import os 
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib 
from google import genai
from config import api

client = genai.Client(api_key=api)


def create_embeddings(text_list): #making vector embeddings
    r=requests.post("http://localhost:11434/api/embed",json={'model':"bge-m3","input":text_list})
    embedding=r.json()['embeddings']
    return embedding

# def inference(prompt):
#     r=requests.post("http://localhost:11434/api/generate",json={'model':"llama3.2","prompt":prompt,"stream":False})
#     response=r.json()
#     return response

def inference_gemini(prompt):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

    return response.text


df= joblib.load("embedding.joblib")
incoming_query=input("Ask a question: ")
question_embedding=create_embeddings(incoming_query)[0]
similarity=cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()


top=5
max_index=similarity.argsort()[::-1][0:top]

new_df= df.loc[max_index]
# print(new_df[['title', 'number', 'text']])

# for index, item in new_df.iterrows():
#      print([index, item['text'],item['number'],item['start:'], item["end"]])
    
prompt = f"""
### Role
You are an expert Video Content Assistant. Your goal is to help users find specific moments in video tutorials based on the provided transcript chunks.

### Context (JSON Data)
The following JSON contains the most relevant video segments found in our database. It includes the video title, transcript text, video number, and precise start/end timestamps.
{new_df[['title', 'text', 'number', 'start:', 'end']].to_json(orient="records")}

### User Question
"{incoming_query}"

### Instructions
1. **Analyze** the JSON data to find the most direct answer to the user's question.
2. **Identify** exactly which video (by number and title) contains the answer.
3. **Reference** the timestamps (start/end) so the user knows exactly where to watch.
4. **Summarize** the content found at those timestamps briefly.
5. **Tone**: Be helpful, concise, and direct.

### Response Format
- Start with a direct answer to the question.
- Use a bulleted list or a small table if multiple segments are relevant.
- End with a "Navigation Guide" (e.g., "Go to Video #6 at 04:16").
"""

with open("prompt.txt",'w',encoding="utf-8") as f:
    f.write(prompt)
    
# response=(inference_gemini(prompt))["response"]
# print(response)

response=(inference_gemini(prompt))
print(response)

with open("reponse.md",'w',encoding="utf-8") as f:
    f.write(response)