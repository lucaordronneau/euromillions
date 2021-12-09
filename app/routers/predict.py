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



# create the router
router = APIRouter()

# add post methode for predict path
@router.post('/predict')
# async function to predict the probability to win the lotterie for a draw given by the user
async def predictDrawProbability(data : DrawPredict) -> str:
    """
    This function return the probability to win and to lose (1-p(win)) the loterie for a draw given in input by the user

    Args:
        data (Draw): The input that the user want to estimated the probability to win the loterie. It is of type Draw

    Returns:
        [str]: return a json with : the probability to win and the probability to lose the lotery for the input given
    """    
    # call the function "loadModel" in src/predict.py to load the prediction model located in src/data/model
    model = loadModel()

    # add features to the input for the prediction
    draw = np.array([data.N1,data.N2,data.N3,data.N4,data.N5, data.E1, data.E2])
    
    # those features are probabilities calculated based on the number of the input 
    # for more info, see "lowHighPatterns" and "oddEvenPatterns" function in src/dataset.py
    draw = np.concatenate((draw, [lowHighPatterns(draw),oddEvenPatterns(draw)]), axis=0)
    
    # add dimention to the array to match the need of the sklearn predict function
    # from (9, ) -> (1,9) array, 9 being the 7 number in the input + the 2 probabilities features
    draw = np.expand_dims(draw, axis=0)
    
    # predict probabilities of the input
    proba = model.predict_proba(draw)
    
    # get only the probability to win the lotery to print the result 
    proba =  proba.tolist()[0][1]


    return {
        'Proba win (%)': round(proba * 100, 2), #print only two number after the coma 
        'Proba lose (%)': round((1-proba )* 100, 2)
    }



# add get method for the predict path       
@router.get('/predict', response_model=DrawPredict)
# async function to predict the draw that have the best probability to win the lotery
async def predictBestProba(numberOfDrawsToGenerate:int):
    """
    This function generate random plausible draws and return the one with the best probability to win the lotery. The user chose the number of draws to generate
    Args:
        numberOfDrawsToGenerate (int): The number of draw to generate and predict the probability

    Returns:
        [DrawPredict]: return the draw that was predicted having the best probability to win.
    """    
    
    # call the function "loadModel" in src/predict.py to load the prediction model located in src/data/model
    model = loadModel()

    # call the function "generateRandomDraws" with the arg given in input to generate random draws
    drawsGenerated = generateRandomDraws(numberOfDrawsToGenerate)
    
    # predict probabilities of generated draws
    proba = model.predict_proba(drawsGenerated)
    
    # get the best draw based on the probability to win lottery predicted by the model
    # init result with the worse probability to win possible (aka zero)
    maxProba = 0
    # for all the probability predicted by the model
    for i in range(len(proba)):
        # if, for a draw, its proba is better than the best seen to this point
        if proba[i][1] > maxProba:
            # the probability is saved
            maxProba = proba[i][1]
            # the draw that correspond the probability is saved
            bestDraw = drawsGenerated[i][0:7].tolist()
    
    # create a type DrawPredict variable to return instead of a str      
    draw = {}
    key = ['N1','N2', 'N3', 'N4', 'N5', 'E1', 'E2']
    # copy the draw in the DrawPredict var
    for i in range(len(key)):
        draw[key[i]] = bestDraw[i]
    

    return  draw
