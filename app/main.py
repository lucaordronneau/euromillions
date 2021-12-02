import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import sys
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'Hello, stranger'}

@app.get('/{name}')
async def get_name(name: str):
    return {'message': f'Hello, {name}'}

@app.post('/predict')
async def predict_draw_probability(data:Draw):
    data = data.dict()
    proba = 0.8
    return {
        'Proba gain': proba,
        'Proba perte': 1-proba
    }
    

