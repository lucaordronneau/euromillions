from fastapi import APIRouter, Body
import sys
import os
import inspect

from src.dataset import oddEvenPatterns, lowHighPatterns
from src.predict import generateRandomDraws, loadModel

sys.path.append('/../classes/Draw.py')
from classes.Draw import DrawPredict

from joblib import load
import numpy as np




router = APIRouter()

@router.post('/predict')
async def predictDrawProbability(data:DrawPredict):
    """[summary]

    Args:
        data (Draw): [description]

    Returns:
        [type]: [description]
    """    
    # load model
    model = loadModel()

    # add features to the entry
    draw = np.array([data.N1,data.N2,data.N3,data.N4,data.N5, data.E1, data.E2])
    draw = np.concatenate((draw, [lowHighPatterns(draw),oddEvenPatterns(draw)]), axis=0)
    draw = np.expand_dims(draw, axis=0)
    
    # predict probabilities
    proba = model.predict_proba(draw)
    proba =  proba.tolist()[0][1]


    return {
        'Proba gain (%)': round(proba * 100, 2),
        'Proba perte (%)': round((1-proba )* 100, 2)
    }



        
@router.get('/predict', response_model=DrawPredict)
async def predictBestProba(numberOfDrawsToGenerate:int):
    """[summary]

    Args:
        data (Draw): [description]

    Returns:
        [type]: [description]
    """    
    
    # load model
    model = loadModel()

    # generate draws
    drawsGenerated = generateRandomDraws(numberOfDrawsToGenerate)
    
    # predict probabilities of generated draws
    proba = model.predict_proba(drawsGenerated)
    
    # get the best draw based on the probability to win lottery predicted by the model
    maxProba = 0
    for i in range(len(proba)):
        if proba[i][1] > maxProba:
            maxProba = proba[i][1]
            bestDraw = drawsGenerated[i][0:7].tolist()
            
    draw = {}
    key = ['N1','N2', 'N3', 'N4', 'N5', 'E1', 'E2']
    for i in range(len(key)):
        draw[key[i]] = bestDraw[i]
    

    return  draw
