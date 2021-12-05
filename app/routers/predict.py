from fastapi import APIRouter, Body
import sys
import os
import inspect
import math
sys.path.append('/../classes/Draw.py')
from classes.Draw import DrawPredict
from joblib import load
import numpy as np
from src.dataset import oddEvenPatterns, lowHighPatterns


router = APIRouter()

@router.post('/predict')
async def predict_draw_probability(data:DrawPredict = Body(..., embed=True)):
    """[summary]

    Args:
        data (Draw): [description]

    Returns:
        [type]: [description]
    """
    print("enculé")
    
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    model = load(parentdir + '/src/data/model/model.jolib')

    
    draw = np.array([data.N1,data.N2,data.N3,data.N4,data.N5, data.E1, data.E2])
    # add features
    draw = np.concatenate((draw, [lowHighPatterns(draw),oddEvenPatterns(draw)]), axis=0)
    draw = np.expand_dims(draw, axis=0)
    
    # predict probabilities
    proba = model.predict_proba(draw)
    proba =  proba.tolist()[0][1]


    return {
        'Proba gain (%)': round(proba * 100, 2),
        'Proba perte (%)': round((1-proba )* 100, 2)
    }
