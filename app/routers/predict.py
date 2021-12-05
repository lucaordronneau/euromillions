from fastapi import APIRouter
import sys
import os
import inspect
sys.path.append('/../classes/Draw.py')
from classes.Draw import Draw
from joblib import load
import numpy as np
from src.dataset import oddEvenPatterns, lowHighPatterns

router = APIRouter()

@router.post('/predict')
async def predict_draw_probability(data:Draw):
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
    proba =  proba.tolist()[0][0]


    return {
        'Proba gain': proba,
        'Proba perte': 1-proba
    }