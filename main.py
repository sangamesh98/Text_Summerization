from fastapi import FastAPI
from summarizer import *
from pydantic import BaseModel

class data(BaseModel):
    text:str


from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()

# Add CORS middleware
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
def handle(r_text:data):
    text=summarizer(r_text.text)
    return str(text)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

# uvicorn main:app --reload