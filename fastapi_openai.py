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

# pip install --upgrade google-api-python-client  //google-auth-httplib2 google-auth-oauthlib

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

def ai_response(msg):
    try:
        msg = msg
        prompt1 = f'''
            Please extract the following information from the given text and return it as a JSON object:

            weather
            location    

            This is the body of text to extract the information from:
            {msg}
        '''
        response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt1,
        max_tokens = 128,
        temperature = 0.5,
        )
        
        completes_txt = response["choices"][0]["text"]
        print(completes_txt)
        return {"message": f"receive: {msg} and response: {completes_txt}"}
    except Exception as e:
        return {"error": str(e)}

#while True: 
@app.post("/items/")
def create_item(msg: str ):
    return ai_response(msg)
    