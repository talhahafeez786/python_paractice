import imp
import uvicorn
from readline import append_history_file
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return{"Hello" : "World"}


@app.get('/something')
def somethig():
    return{"Data" : "Something"}
    