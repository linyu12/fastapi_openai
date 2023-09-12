import openai
import os
from dotenv import load_dotenv

from  fastapi import FastAPI, HTTPException
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# pip install fastapi uvicorn
# pip install fastapi==0.78.8
# pip install uvicorn==0.17.6
# uvicorn fastapi_openai:app --reload
# http://localhost:8000/docs#/

app = FastAPI()
'''app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)'''

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

#while True: 
@app.post("/items/")
def create_item(msg: str ):
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        max_tokens=128,
        temperature=0.5,
        )
        completes_txt = response["choices"][0]["text"]
        print(completes_txt)
        return {"message": f"receive: {msg} and response: {completes_txt}"}
    except Exception as e:
        return {"error": str(e)}
    