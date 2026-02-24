import requests
import os 
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embeddings(text_list): #making vector embeddings
    r=requests.post("http://localhost:11434/api/embed",json={'model':"bge-m3","input":text_list})
    embedding=r.json()['embeddings']
    return embedding

jsons=os.listdir('jsons') #list all jsons
# print(jsons)
my_dict=[]
chunk_id=0
for json_files in jsons:
    with open(f"jsons/{json_files}") as f:
        content=json.load(f)
        
    print(f"creating embeddings for {json_files}")
    
    embeddings=create_embeddings([c['text'] for c in content['chunks']])
    for i, chunk in enumerate(content['chunks']):
        # print(chunk)
        chunk['chunk_id']=chunk_id
        chunk["embedding"]=embeddings[i]
        chunk_id+=1
        my_dict.append(chunk)
        # break

df=pd.DataFrame.from_records(my_dict)
joblib.dump(df,"embedding.joblib")